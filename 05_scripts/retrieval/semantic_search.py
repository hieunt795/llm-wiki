# -*- coding: utf-8 -*-
"""
semantic_search.py — Semantic search over wiki embedding index (v1.1)
======================================================================
Search bằng meaning, không chỉ keyword.
Ví dụ: "chính phủ kiểm soát ngân hàng" → tìm ra "Fiscal Dominance"

USAGE:
  python 05_scripts/semantic_search.py "fiscal dominance nhật bản"
  python 05_scripts/semantic_search.py "LCR thanh khoản" --top 10
  python 05_scripts/semantic_search.py "yield curve control" --wiki-only
  python 05_scripts/semantic_search.py "transfer pricing" --threshold 0.4
  python 05_scripts/semantic_search.py "BOJ intervention" --json

REQUIRES:
  Index built by: python 05_scripts/embed_index.py --build
"""

import argparse
import json
import sys
import io
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT  = SCRIPT_DIR.parent.parent
CACHE_DIR  = WIKI_ROOT / ".cache"
INDEX_PATH = CACHE_DIR / "wiki_embed.index"
META_PATH  = CACHE_DIR / "wiki_embed.meta.json"

MODEL_NAME = "BAAI/bge-m3"

# Lazy-load model và index (chỉ load một lần per process)
_model = None
_index = None
_meta  = None


def _load_resources():
    global _model, _index, _meta
    if _model is not None:
        return True

    try:
        from sentence_transformers import SentenceTransformer
        import faiss
    except ImportError as e:
        print(f"ERROR: {e}", flush=True)
        print("  Run: pip install sentence-transformers faiss-cpu --break-system-packages", flush=True)
        return False

    if not INDEX_PATH.exists():
        print("ERROR: Index not found. Build it first:", flush=True)
        print("  python 05_scripts/embed_index.py --build", flush=True)
        return False

    try:
        _model = SentenceTransformer(MODEL_NAME)
    except Exception as e:
        print(f"ERROR: Cannot load model '{MODEL_NAME}' — {e}", flush=True)
        print("  Download/cache the model first, or run on a machine with Hugging Face access.", flush=True)
        return False
    _index = faiss.read_index(str(INDEX_PATH))
    _meta  = json.loads(META_PATH.read_text(encoding="utf-8"))
    return True


def semantic_search(
    query: str,
    top_k: int = 10,
    threshold: float = 0.30,
    wiki_only: bool = False,
    raw_only: bool = False,
) -> list[dict]:
    """
    Search và trả về list of results sorted by cosine similarity.
    Each result: {score, id, title, file, source, thesis, tags, confidence}
    """
    if not _load_resources():
        return []

    import numpy as np

    query_vec = _model.encode(
        [query],
        normalize_embeddings=True,
        convert_to_numpy=True,
    ).astype("float32")

    if _index.d != query_vec.shape[1]:
        print(
            f"ERROR: Embedding dim mismatch. Index={_index.d}, model={query_vec.shape[1]}. "
            "Rebuild with: python 05_scripts/embed_index.py --build",
            flush=True,
        )
        return []

    # Source filters need the full candidate pool because wiki/raw vectors share
    # one FAISS index and one source can crowd out the other in the first page.
    k = _index.ntotal if (wiki_only or raw_only) else min(top_k * 10, _index.ntotal)
    scores, indices = _index.search(query_vec, k)

    results = []
    file_counts: dict[str, int] = {}
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0 or score < threshold:
            continue

        node = _meta[idx]

        if wiki_only and node["source"] != "wiki":
            continue
        if raw_only and node["source"] != "raw":
            continue

        file_key = str(node.get("file", "")).replace("\\", "/").lower()
        tags = node.get("tags", [])
        is_clippings = isinstance(tags, list) and "clippings" in tags
        cap = 1 if is_clippings else 2
        if file_counts.get(file_key, 0) >= cap:
            continue
        file_counts[file_key] = file_counts.get(file_key, 0) + 1

        thesis = node.get("thesis", "")
        if node.get("source") == "raw" and str(thesis).strip() == Path(node.get("file", "")).stem:
            thesis = node.get("title") or node.get("snippet", "")
        display_score = float(score) * (0.55 if is_clippings else 1.0)

        results.append({
            "score":      round(display_score, 4),
            "id":         node["id"],
            "title":      node["title"],
            "file":       node["file"],
            "source":     node["source"],
            "page":       node.get("page"),
            "thesis":     thesis,
            "snippet":    node.get("snippet", ""),
            "tags":       node.get("tags", []),
            "confidence": node.get("confidence", "?"),
        })

        if len(results) >= top_k:
            break

    return results


def print_results(results: list[dict], query: str, as_json: bool = False):
    if as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    if not results:
        print(f"No results for: '{query}'", flush=True)
        return

    print(f"\n== SEMANTIC SEARCH: '{query}' ({len(results)} results) ==", flush=True)
    print("=" * 60, flush=True)

    for i, r in enumerate(results, 1):
        source_label = f"[{r['source'].upper()}]"
        conf = f"conf={r['confidence']}" if r['confidence'] != '?' else ""
        tags = ", ".join(r['tags'][:4]) if r['tags'] else ""

        page_label = f" p.{r['page']}" if r.get("page") else ""
        print(f"\n#{i} [score={r['score']:.3f}] {source_label}{page_label} {conf}", flush=True)
        print(f"    {r['title']}", flush=True)
        print(f"    FILE: {r['file']}", flush=True)
        # Raw chunks: hiện snippet (text thực tế của trang)
        # Wiki nodes: hiện thesis (súc tích hơn)
        if r["source"] == "raw" and r.get("page") and r.get("snippet"):
            snippet = r["snippet"][:200].replace("\n", " ").strip()
            snippet = snippet + ("..." if len(r["snippet"]) > 200 else "")
            print(f"    SNIPPET: {snippet}", flush=True)
        elif r.get("thesis"):
            thesis_short = r["thesis"][:150] + ("..." if len(r["thesis"]) > 150 else "")
            print(f"    THESIS: {thesis_short}", flush=True)
        if tags:
            print(f"    TAGS: {tags}", flush=True)

    print(flush=True)


def main():
    parser = argparse.ArgumentParser(
        description="semantic_search.py v1.1 — Meaning-based wiki search"
    )
    parser.add_argument("query",        type=str,            help="Search query (any language)")
    parser.add_argument("--top",        type=int, default=8, help="Max results (default: 8)")
    parser.add_argument("--threshold",  type=float, default=0.30,
                        help="Min cosine similarity 0.0–1.0 (default: 0.30)")
    parser.add_argument("--wiki-only",  action="store_true", help="Search wiki nodes only")
    parser.add_argument("--raw-only",   action="store_true", help="Search raw sources only")
    parser.add_argument("--json",       action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if not args.json:
        print(f"[semantic_search] Loading model ...", end=" ", flush=True)

    results = semantic_search(
        query=args.query,
        top_k=args.top,
        threshold=args.threshold,
        wiki_only=args.wiki_only,
        raw_only=args.raw_only,
    )

    if not args.json:
        print("done.", flush=True)

    print_results(results, args.query, as_json=args.json)


if __name__ == "__main__":
    main()

