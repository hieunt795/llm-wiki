# -*- coding: utf-8 -*-
"""
embed_index.py — Semantic embedding index builder (v2.2)
=========================================================
Build và persist FAISS vector index từ wiki nodes + raw PDF chunks.

Chunking strategy:
  - Wiki nodes (03_wiki/**/*.md)  → 1 vector per file (đã ngắn)
  - Raw sources (02_sources/**/*.md) → 1 vector per <!-- Page N --> chunk

INSTALL (chạy một lần):
  pip install sentence-transformers faiss-cpu watchdog --break-system-packages

USAGE:
  python 05_scripts/embed_index.py --build          # Build full index
  python 05_scripts/embed_index.py --build --watch  # Build + auto-reindex khi file thay đổi
  python 05_scripts/embed_index.py --stats          # Xem thống kê index hiện tại

OUTPUT:
  .cache/wiki_embed.index     — FAISS binary index
  .cache/wiki_embed.meta.json — id → {file, page, thesis, tags, ...} mapping
"""

import argparse
import json
import re
import time
import sys
import io
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR  = Path(__file__).parent
WIKI_ROOT   = SCRIPT_DIR.parent
WIKI_DIR    = WIKI_ROOT / "03_wiki"
RAW_DIR     = WIKI_ROOT / "02_sources"
CACHE_DIR      = WIKI_ROOT / ".cache"
INDEX_PATH     = CACHE_DIR / "wiki_embed.index"
META_PATH      = CACHE_DIR / "wiki_embed.meta.json"
MANIFEST_PATH  = CACHE_DIR / "wiki_embed.manifest.json"  # file → mtime mapping

MODEL_NAME   = "BAAI/bge-m3"
CHUNK_SIZE   = 1800  # max chars per chunk for dense retrieval input
MIN_CHUNK    = 200   # skip chunks shorter than this


def _resolve_device(device: str = "auto") -> str:
    if device != "auto":
        return device
    try:
        import torch
        return "cuda" if torch.cuda.is_available() else "cpu"
    except Exception:
        return "cpu"


def _resolve_batch_size(batch_size: int | None, device: str) -> int:
    if batch_size is not None:
        return batch_size
    return 128 if device == "cuda" else 32


# ── Parse frontmatter ─────────────────────────────────────────────────────────

def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Returns (meta_dict, body_text). meta_dict is {} if no frontmatter."""
    if not text.startswith("---"):
        return {}, text

    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    frontmatter = text[3:end]
    body = text[end + 4:]

    meta = {}
    current_key = None
    current_list = []

    for line in frontmatter.splitlines():
        if line.startswith("  - ") or line.startswith("- "):
            val = line.strip().lstrip("- ").strip().strip('"')
            if current_key:
                current_list.append(val)
        elif ":" in line and not line.startswith(" "):
            if current_key and current_list:
                meta[current_key] = current_list
            current_list = []
            k, _, v = line.partition(":")
            current_key = k.strip()
            meta[current_key] = v.strip().strip('"')
        else:
            current_list = []
            current_key = None

    if current_key and current_list:
        meta[current_key] = current_list

    return meta, body


def _norm_list(val) -> list:
    if isinstance(val, list):
        return [str(v) for v in val]
    if isinstance(val, str) and val:
        return [val]
    return []


# ── Wiki node → single entry ──────────────────────────────────────────────────

def parse_wiki_node(md_path: Path) -> dict | None:
    """1 vector per wiki node file."""
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None

    meta, body = _parse_frontmatter(text)
    if not meta and not body.strip():
        return None

    thesis = str(meta.get("thesis", "")).strip()
    if not thesis:
        for line in body.splitlines():
            s = line.strip()
            if s and not s.startswith("#") and not s.startswith("<!--"):
                thesis = s[:300]
                break

    tags    = _norm_list(meta.get("tags", []))
    aliases = _norm_list(meta.get("aliases", []))
    title   = str(meta.get("title", md_path.stem)).strip()

    parts = [title] + aliases + tags
    if thesis:
        parts.append(thesis[:400])
    embed_text = " | ".join(p for p in parts if p)

    if not embed_text.strip():
        return None

    return {
        "id":         f"{md_path.stem}::wiki",
        "title":      title,
        "file":       str(md_path.relative_to(WIKI_ROOT)).replace("\\", "/"),
        "source":     "wiki",
        "page":       None,
        "thesis":     thesis[:300],
        "snippet":    thesis[:200],
        "tags":       tags,
        "aliases":    aliases,
        "confidence": str(meta.get("confidence", "?")),
        "embed_text": embed_text,
    }


# ── Heading-based chunker ─────────────────────────────────────────────────────

def _split_by_headings(body: str) -> list[tuple[str, str]]:
    """
    Split markdown body theo ## và ### headings.
    Trả về list of (heading_title, section_text).
    Section không có heading → title = ""
    """
    # Match ## hoặc ### (không lấy # level 1 vì thường là title cả file)
    pattern = re.compile(r'^(#{2,3})\s+(.+)$', re.MULTILINE)
    matches = list(pattern.finditer(body))

    if not matches:
        return [("", body.strip())]

    sections = []

    # Text trước heading đầu tiên
    pre = body[:matches[0].start()].strip()
    if pre:
        sections.append(("", pre))

    for idx, m in enumerate(matches):
        heading_title = m.group(2).strip()
        start = m.end()
        end   = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        section_text = body[start:end].strip()
        sections.append((heading_title, section_text))

    return sections


def _sliding_window(text: str, chunk_size: int, overlap: int = 150) -> list[str]:
    """
    Chia text dài thành các window overlap nhau.
    Dùng khi section > chunk_size.
    """
    windows = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        windows.append(text[start:end])
        if end >= len(text):
            break
        start += chunk_size - overlap
    return windows


def _is_toc_text(text: str) -> bool:
    """Phát hiện TOC / index pages — ít semantic value."""
    pipe_density = text.count("|") / max(len(text), 1)
    dot_density  = text.count("....") / max(len(text), 1)
    return pipe_density > 0.05 or dot_density > 0.01


# ── Raw source → heading-based chunks ────────────────────────────────────────

def parse_raw_chunks(md_path: Path) -> list[dict]:
    """
    Split raw .md theo ## / ### headings → 1 vector per section.
    - Section dài > CHUNK_SIZE → sliding window (overlap 150 chars)
    - Section ngắn < MIN_CHUNK → merge với section tiếp theo
    - TOC / index pages → skip
    Fallback về page-based chunking nếu không có headings.
    """
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    meta, body = _parse_frontmatter(text)

    book_title = str(meta.get("title", md_path.stem)).strip()
    tags       = _norm_list(meta.get("tags", []))
    aliases    = _norm_list(meta.get("aliases", []))
    file_rel   = str(md_path.relative_to(WIKI_ROOT)).replace("\\", "/")
    stem       = md_path.stem

    raw_sections = _split_by_headings(body)

    # Merge sections ngắn vào section kế tiếp
    merged_sections = []
    buffer_title = ""
    buffer_text  = ""

    for heading, sec_text in raw_sections:
        combined = (buffer_text + " " + sec_text).strip()
        if not buffer_text:
            buffer_title = heading
            buffer_text  = sec_text
        elif len(buffer_text) < MIN_CHUNK:
            # Merge: giữ heading của buffer, append text mới
            buffer_text  = combined
            if not buffer_title:
                buffer_title = heading
        else:
            merged_sections.append((buffer_title, buffer_text))
            buffer_title = heading
            buffer_text  = sec_text

    if buffer_text.strip():
        merged_sections.append((buffer_title, buffer_text))

    chunks = []
    chunk_idx = 0

    for heading, sec_text in merged_sections:
        if _is_toc_text(sec_text):
            continue
        if len(sec_text.strip()) < MIN_CHUNK:
            continue

        # Section vừa → 1 chunk
        if len(sec_text) <= CHUNK_SIZE:
            windows = [sec_text]
        else:
            # Section dài → sliding window
            windows = _sliding_window(sec_text, CHUNK_SIZE, overlap=150)

        for w_idx, window in enumerate(windows):
            window = window.strip()
            if len(window) < MIN_CHUNK:
                continue

            # ID: stem::h{idx} hoặc stem::h{idx}_w{w_idx}
            chunk_id = f"{stem}::h{chunk_idx}"
            if len(windows) > 1:
                chunk_id = f"{stem}::h{chunk_idx}_w{w_idx}"

            # Title hiển thị
            display_title = f"{book_title} — {heading}" if heading else book_title

            # BGE-M3 does not require E5-style passage prefixes.
            parts = [stem]
            if heading:
                parts.append(heading)
            parts += tags
            parts.append(window[:CHUNK_SIZE])
            embed_text = " | ".join(p for p in parts if p)

            chunks.append({
                "id":         chunk_id,
                "stem":       stem,
                "title":      display_title,
                "file":       file_rel,
                "source":     "raw",
                "page":       None,
                "heading":    heading,
                "thesis":     book_title[:200],
                "snippet":    window[:200],
                "tags":       tags,
                "aliases":    aliases,
                "confidence": "?",
                "embed_text": embed_text,
            })

        chunk_idx += 1

    # Fallback: nếu không có heading nào → page-based (code cũ)
    if not chunks:
        page_pattern = re.compile(r'<!--\s*Page\s+(\d+)\s*-->', re.IGNORECASE)
        parts_pg = page_pattern.split(body)
        i = 1
        while i < len(parts_pg) - 1:
            try:
                page_num  = int(parts_pg[i])
                page_text = parts_pg[i + 1].strip()
                i += 2
            except (ValueError, IndexError):
                i += 1
                continue
            if len(page_text) < MIN_CHUNK or _is_toc_text(page_text):
                continue
            embed_text = " | ".join(
                p for p in [stem] + tags + [page_text[:CHUNK_SIZE]] if p
            )
            chunks.append({
                "id":         f"{stem}::p{page_num}",
                "stem":       stem,
                "title":      f"{book_title} — Page {page_num}",
                "file":       file_rel,
                "source":     "raw",
                "page":       page_num,
                "heading":    "",
                "thesis":     book_title[:200],
                "snippet":    page_text[:200],
                "tags":       tags,
                "aliases":    aliases,
                "confidence": "?",
                "embed_text": embed_text,
            })

    return chunks


# ── Collect all entries ───────────────────────────────────────────────────────

def collect_all() -> list[dict]:
    entries = []

    # Wiki nodes — file-level
    wiki_count = 0
    for md in sorted(WIKI_DIR.rglob("*.md")):
        if md.name.startswith("_") or md.name.startswith("."):
            continue
        node = parse_wiki_node(md)
        if node:
            entries.append(node)
            wiki_count += 1

    # Raw sources — page-level chunks
    raw_files = 0
    chunk_count = 0
    for md in sorted(RAW_DIR.rglob("*.md")):
        if md.name.startswith("_") or md.name.startswith("."):
            continue
        chunks = parse_raw_chunks(md)
        if chunks:
            entries.extend(chunks)
            raw_files += 1
            chunk_count += len(chunks)
        else:
            # Fallback: treat as wiki-style node if no page markers
            node = parse_wiki_node(md)
            if node:
                node["source"] = "raw"
                entries.append(node)
                raw_files += 1
                chunk_count += 1

    return entries, wiki_count, raw_files, chunk_count


# ── Build FAISS index ─────────────────────────────────────────────────────────

def build_index(verbose: bool = True, batch_size: int | None = None, device: str = "auto") -> bool:
    try:
        from sentence_transformers import SentenceTransformer
        import faiss
        import numpy as np
    except ImportError as e:
        print(f"ERROR: Missing dependency — {e}", flush=True)
        print("  Run: pip install sentence-transformers faiss-cpu --break-system-packages", flush=True)
        return False

    CACHE_DIR.mkdir(exist_ok=True)
    resolved_device = _resolve_device(device)
    resolved_batch_size = _resolve_batch_size(batch_size, resolved_device)

    if verbose:
        print(f"[embed_index v2.2] Loading model: {MODEL_NAME} on {resolved_device} ...", flush=True)

    t0 = time.time()
    try:
        model = SentenceTransformer(MODEL_NAME, device=resolved_device)
    except Exception as e:
        print(f"ERROR: Cannot load model '{MODEL_NAME}' — {e}", flush=True)
        print("  Download/cache the model first, or run the build on a machine with Hugging Face access.", flush=True)
        return False

    if verbose:
        print(f"[embed_index] Model loaded in {time.time()-t0:.1f}s", flush=True)
        print(f"[embed_index] Collecting + chunking ...", flush=True)

    entries, wiki_count, raw_files, chunk_count = collect_all()

    if not entries:
        print("ERROR: No entries found.", flush=True)
        return False

    if verbose:
        print(f"[embed_index] {wiki_count} wiki nodes + {raw_files} raw files → {chunk_count} raw chunks", flush=True)
        print(f"[embed_index] Total vectors: {len(entries)}. Encoding with batch_size={resolved_batch_size} ...", flush=True)

    texts = [e["embed_text"] for e in entries]
    t1 = time.time()
    embeddings = model.encode(
        texts,
        batch_size=resolved_batch_size,
        show_progress_bar=verbose,
        normalize_embeddings=True,
        convert_to_numpy=True,
    )

    if verbose:
        print(f"[embed_index] Encoded {len(texts)} vectors in {time.time()-t1:.1f}s", flush=True)

    # Build FAISS IndexFlatIP (cosine via normalized dot product)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings.astype("float32"))

    faiss.write_index(index, str(INDEX_PATH))

    # Save metadata (strip embed_text)
    meta_out = [{k: v for k, v in e.items() if k != "embed_text"} for e in entries]
    META_PATH.write_text(
        json.dumps(meta_out, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    size_kb = INDEX_PATH.stat().st_size // 1024
    if verbose:
        print(f"[embed_index] Saved: {INDEX_PATH.name} ({size_kb} KB), {len(entries)} vectors", flush=True)
        print(f"[embed_index] Total time: {time.time()-t0:.1f}s", flush=True)

    # Save manifest: file → mtime (dùng cho incremental build sau này)
    manifest = {}
    for md in sorted(WIKI_DIR.rglob("*.md")):
        if not md.name.startswith("_") and not md.name.startswith("."):
            rel = str(md.relative_to(WIKI_ROOT)).replace("\\", "/")
            manifest[rel] = md.stat().st_mtime
    for md in sorted(RAW_DIR.rglob("*.md")):
        if not md.name.startswith("_") and not md.name.startswith("."):
            rel = str(md.relative_to(WIKI_ROOT)).replace("\\", "/")
            manifest[rel] = md.stat().st_mtime
    _save_manifest(manifest)
    if verbose:
        print(f"[embed_index] Manifest saved: {len(manifest)} files tracked", flush=True)

    return True


# ── Incremental build ────────────────────────────────────────────────────────

def _load_manifest() -> dict:
    """Load file → mtime manifest. Returns {} nếu chưa có."""
    if not MANIFEST_PATH.exists():
        return {}
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_manifest(manifest: dict):
    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def incremental_build(verbose: bool = True, batch_size: int | None = None, device: str = "auto") -> bool:
    """
    Chỉ encode các files mới/thay đổi so với lần build trước.
    Files bị xóa → remove vectors tương ứng.
    Files không đổi → giữ nguyên vectors từ index cũ.

    Fallback về full build nếu index cũ không tồn tại hoặc dim thay đổi.
    """
    if not INDEX_PATH.exists() or not META_PATH.exists():
        if verbose:
            print("[embed_index] No existing index → falling back to full build", flush=True)
        return build_index(verbose=verbose, batch_size=batch_size, device=device)

    # Nếu chưa có manifest → init từ files hiện tại (coi tất cả là "đã index")
    # → lần incremental đầu tiên sẽ không encode lại gì cả, chỉ track từ đây về sau
    if not MANIFEST_PATH.exists():
        if verbose:
            print("[embed_index] No manifest found → initializing from current files ...", flush=True)
        manifest = {}
        for md in sorted(WIKI_DIR.rglob("*.md")):
            if not md.name.startswith("_") and not md.name.startswith("."):
                rel = str(md.relative_to(WIKI_ROOT)).replace("\\", "/")
                manifest[rel] = md.stat().st_mtime
        for md in sorted(RAW_DIR.rglob("*.md")):
            if not md.name.startswith("_") and not md.name.startswith("."):
                rel = str(md.relative_to(WIKI_ROOT)).replace("\\", "/")
                manifest[rel] = md.stat().st_mtime
        _save_manifest(manifest)
        if verbose:
            print(f"[embed_index] Manifest initialized: {len(manifest)} files tracked", flush=True)
            print(f"[embed_index] Nothing to encode — index is up to date.", flush=True)
        return True

    try:
        from sentence_transformers import SentenceTransformer
        import faiss
        import numpy as np
    except ImportError as e:
        print(f"ERROR: {e}", flush=True)
        return False

    CACHE_DIR.mkdir(exist_ok=True)
    t0 = time.time()
    resolved_device = _resolve_device(device)
    resolved_batch_size = _resolve_batch_size(batch_size, resolved_device)

    if verbose:
        print(f"[embed_index incremental] Loading model: {MODEL_NAME} on {resolved_device} ...", flush=True)
    try:
        model = SentenceTransformer(MODEL_NAME, device=resolved_device)
    except Exception as e:
        print(f"ERROR: Cannot load model '{MODEL_NAME}' — {e}", flush=True)
        print("  Download/cache the model first, or run the build on a machine with Hugging Face access.", flush=True)
        return False
    if verbose:
        print(f"[embed_index] Model loaded in {time.time()-t0:.1f}s", flush=True)

    # Load existing index + meta + manifest
    old_index = faiss.read_index(str(INDEX_PATH))
    old_meta  = json.loads(META_PATH.read_text(encoding="utf-8"))
    manifest  = _load_manifest()

    # Kiểm tra dim consistency
    test_vec = model.encode(["test"], normalize_embeddings=True, convert_to_numpy=True)
    current_dim = test_vec.shape[1]
    if old_index.d != current_dim:
        if verbose:
            print(f"[embed_index] Dim mismatch ({old_index.d} vs {current_dim}) → full rebuild", flush=True)
        return build_index(verbose=verbose, batch_size=batch_size, device=device)

    # Scan tất cả .md files hiện tại → build mtime map
    current_files = {}
    for md in sorted(WIKI_DIR.rglob("*.md")):
        if not md.name.startswith("_") and not md.name.startswith("."):
            rel = str(md.relative_to(WIKI_ROOT)).replace("\\", "/")
            current_files[rel] = md.stat().st_mtime

    for md in sorted(RAW_DIR.rglob("*.md")):
        if not md.name.startswith("_") and not md.name.startswith("."):
            rel = str(md.relative_to(WIKI_ROOT)).replace("\\", "/")
            current_files[rel] = md.stat().st_mtime

    # Phân loại: changed / new / deleted
    changed = {f for f, mt in current_files.items()
               if abs(mt - manifest.get(f, 0)) > 1.0}  # 1s tolerance
    deleted = {f for f in manifest if f not in current_files}

    if verbose:
        print(f"[embed_index] Files: {len(current_files)} total | "
              f"{len(changed)} changed/new | {len(deleted)} deleted", flush=True)

    if not changed and not deleted:
        if verbose:
            print(f"[embed_index] Nothing changed — index is up to date.", flush=True)
        return True

    # Build vectors từ changed/new files
    new_entries = []
    for rel_path in sorted(changed):
        abs_path = WIKI_ROOT / rel_path.replace("/", "\\")
        if not abs_path.exists():
            continue
        # Wiki node hay raw?
        if "03_wiki" in rel_path:
            node = parse_wiki_node(abs_path)
            if node:
                new_entries.append(node)
        else:
            chunks = parse_raw_chunks(abs_path)
            if chunks:
                new_entries.extend(chunks)
            else:
                node = parse_wiki_node(abs_path)
                if node:
                    node["source"] = "raw"
                    new_entries.append(node)

    # Tập hợp stems của files thay đổi + deleted → cần remove khỏi old index
    changed_stems = set()
    for rel_path in changed | deleted:
        changed_stems.add(Path(rel_path).stem)

    # Filter old vectors: giữ lại những gì không thuộc changed/deleted files
    kept_meta = []
    kept_vecs  = []
    old_vecs   = faiss.extract_index_ivf if hasattr(faiss, 'extract_index_ivf') else None

    # Extract all vectors từ old index
    all_old_vecs = np.zeros((old_index.ntotal, old_index.d), dtype="float32")
    old_index.reconstruct_n(0, old_index.ntotal, all_old_vecs)

    for i, node in enumerate(old_meta):
        node_stem = node.get("stem", Path(node.get("file", "")).stem)
        if node_stem in changed_stems:
            continue  # drop — sẽ được re-encode
        kept_meta.append(node)
        kept_vecs.append(all_old_vecs[i])

    if verbose:
        print(f"[embed_index] Kept {len(kept_meta)} old vectors, "
              f"dropped {len(old_meta) - len(kept_meta)}", flush=True)
        print(
            f"[embed_index] Encoding {len(new_entries)} new/changed entries with batch_size={resolved_batch_size} ...",
            flush=True,
        )

    # Encode new entries
    if new_entries:
        texts = [e["embed_text"] for e in new_entries]
        t1 = time.time()
        new_vecs = model.encode(
            texts,
            batch_size=resolved_batch_size,
            show_progress_bar=verbose,
            normalize_embeddings=True,
            convert_to_numpy=True,
        ).astype("float32")
        if verbose:
            print(f"[embed_index] Encoded {len(texts)} vectors in {time.time()-t1:.1f}s", flush=True)
    else:
        new_vecs = np.zeros((0, current_dim), dtype="float32")

    # Merge: kept + new
    if kept_vecs:
        kept_arr = np.stack(kept_vecs).astype("float32")
        if len(new_entries) > 0:
            final_vecs = np.concatenate([kept_arr, new_vecs], axis=0)
        else:
            final_vecs = kept_arr
    else:
        final_vecs = new_vecs

    final_meta = kept_meta + [{k: v for k, v in e.items() if k != "embed_text"}
                               for e in new_entries]

    # Save index
    new_index = faiss.IndexFlatIP(current_dim)
    new_index.add(final_vecs)
    faiss.write_index(new_index, str(INDEX_PATH))

    META_PATH.write_text(
        json.dumps(final_meta, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    # Update manifest
    new_manifest = {f: mt for f, mt in current_files.items()}
    _save_manifest(new_manifest)

    size_kb = INDEX_PATH.stat().st_size // 1024
    elapsed = time.time() - t0
    if verbose:
        print(f"[embed_index] Saved: {INDEX_PATH.name} ({size_kb} KB), "
              f"{len(final_meta)} vectors", flush=True)
        print(f"[embed_index] Total time: {elapsed:.1f}s", flush=True)

    return True


# ── Watchdog auto-reindex ─────────────────────────────────────────────────────

def watch_and_reindex():
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        print("  Run: pip install watchdog --break-system-packages", flush=True)
        return

    import threading

    _rebuild_timer = None
    _lock = threading.Lock()

    class WikiHandler(FileSystemEventHandler):
        def on_modified(self, event):
            if not event.is_directory and event.src_path.endswith(".md"):
                self._schedule_rebuild(event.src_path)

        def on_created(self, event):
            if not event.is_directory and event.src_path.endswith(".md"):
                self._schedule_rebuild(event.src_path)

        def _schedule_rebuild(self, path):
            nonlocal _rebuild_timer
            with _lock:
                if _rebuild_timer is not None:
                    _rebuild_timer.cancel()
                _rebuild_timer = threading.Timer(10.0, _do_rebuild, args=[path])
                _rebuild_timer.start()

    def _do_rebuild(trigger_path):
        print(f"\n[embed_index] Change: {Path(trigger_path).name} -> rebuilding ...", flush=True)
        build_index(verbose=False)
        print(f"[embed_index] Index updated.", flush=True)

    observer = Observer()
    observer.schedule(WikiHandler(), str(WIKI_DIR), recursive=True)
    observer.schedule(WikiHandler(), str(RAW_DIR), recursive=True)
    observer.start()

    print(f"[embed_index] Watching (Ctrl+C to stop) ...", flush=True)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# Stats

def print_stats():
    if not INDEX_PATH.exists() or not META_PATH.exists():
        print("No index found. Run: python 05_scripts/embed_index.py --build", flush=True)
        return

    meta = json.loads(META_PATH.read_text(encoding="utf-8"))
    size_kb = INDEX_PATH.stat().st_size // 1024
    wiki_count  = sum(1 for n in meta if n["source"] == "wiki")
    raw_count   = sum(1 for n in meta if n["source"] == "raw")
    paged_count = sum(1 for n in meta if n.get("page") is not None)
    mtime = INDEX_PATH.stat().st_mtime
    from datetime import datetime
    built_at = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")

    print(f"[embed_index v2.2] Index stats:", flush=True)
    print(f"  Total vectors : {len(meta)}", flush=True)
    print(f"  Wiki nodes    : {wiki_count} (file-level)", flush=True)
    print(f"  Raw chunks    : {raw_count} ({paged_count} page-level)", flush=True)
    print(f"  Index size    : {size_kb} KB", flush=True)
    print(f"  Built at      : {built_at}", flush=True)
    print(f"  Model         : {MODEL_NAME}", flush=True)


# CLI

def main():
    parser = argparse.ArgumentParser(description="embed_index.py v2.2 -- BGE-M3 semantic index")
    parser.add_argument("--build",         action="store_true", help="Full rebuild index")
    parser.add_argument("--incremental",   action="store_true", help="Only encode changed/new files")
    parser.add_argument("--init-manifest", action="store_true", help="Init manifest from current files (no encoding)")
    parser.add_argument("--watch",         action="store_true", help="Watch for file changes + auto-reindex")
    parser.add_argument("--stats",         action="store_true", help="Show index stats")
    parser.add_argument("--batch-size",    type=int, default=None, help="Embedding batch size; default auto (128 on cuda, 32 on cpu)")
    parser.add_argument("--device",        type=str, default="auto", choices=["auto", "cpu", "cuda"], help="Embedding device")
    args = parser.parse_args()

    if args.stats:
        print_stats()
        return

    if args.init_manifest:
        manifest = {}
        for md in sorted(WIKI_DIR.rglob("*.md")):
            if not md.name.startswith("_") and not md.name.startswith("."):
                rel = str(md.relative_to(WIKI_ROOT)).replace("\\", "/")
                manifest[rel] = md.stat().st_mtime
        for md in sorted(RAW_DIR.rglob("*.md")):
            if not md.name.startswith("_") and not md.name.startswith("."):
                rel = str(md.relative_to(WIKI_ROOT)).replace("\\", "/")
                manifest[rel] = md.stat().st_mtime
        _save_manifest(manifest)
        print(f"[embed_index] Manifest initialized: {len(manifest)} files tracked → {MANIFEST_PATH}", flush=True)
        return

    if args.incremental:
        ok = incremental_build(verbose=True, batch_size=args.batch_size, device=args.device)
        if not ok:
            sys.exit(1)
    elif args.build:
        ok = build_index(verbose=True, batch_size=args.batch_size, device=args.device)
        if not ok:
            sys.exit(1)

    if args.watch:
        watch_and_reindex()

    if not args.build and not args.watch and not args.stats:
        parser.print_help()


if __name__ == "__main__":
    main()
