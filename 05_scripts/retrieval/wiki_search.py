"""
wiki_search.py — Token-efficient Wiki + Raw Search Tool (v3.6)
Usage:
  python wiki_search.py "CPI"
  python wiki_search.py "fiscal dominance" --top 5 --no-raw
  python wiki_search.py "private credit" --type concept
  python wiki_search.py "interest rate" "bond price" --show-related
  python wiki_search.py "forward fx" --json --top 10
"""

import json
import re
import sys
import time
import math
import pickle
import argparse
import yaml
from pathlib import Path
from collections import Counter

# Force UTF-8 on Windows BEFORE any other imports that touch stdout
if sys.platform == 'win32':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    import os
    os.environ['PYTHONIOENCODING'] = 'utf-8'

# Ensure 05_scripts/ is on sys.path regardless of CWD
# This fixes subprocess invocations from WIKI_ROOT (librarian.py)
SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT  = SCRIPT_DIR.parent.parent
if str(SCRIPT_DIR.parent) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR.parent))

from search_utils import load_synonyms, expand_query, highlight_snippet, route_query
from fts5_engine import setup_fts5

WIKI_DIR   = WIKI_ROOT / "03_wiki"

CACHE_DIR            = WIKI_ROOT / ".cache"
CACHE_FILE           = CACHE_DIR / "wiki_search_cache.pkl"
CACHE_TTL            = 600   # seconds
CACHE_FORMAT_VERSION = 3     # v3: dirs_key always includes raw, stale-raw check added

RAW_SOURCE_SUBSTRINGS = {".pdf", "raw_sources", "_raw", "perry_central_bank",
                          "during_fixed_income", "tuckman", "neftci", "deep_dive"}

# ── BM25 parameters ───────────────────────────────────────────────────────────
BM25_K1      = 1.5
BM25_B       = 0.75
AVG_DOC_LEN  = 500


# ── YAML frontmatter ──────────────────────────────────────────────────────────
def extract_frontmatter(text: str) -> dict:
    try:
        if text.startswith("---"):
            end = text.find("---", 3)
            if end != -1:
                return yaml.safe_load(text[3:end]) or {}
    except Exception:
        pass
    return {}


# ── Line-based context around first keyword hit ───────────────────────────────
def get_context_with_lines(file_path: Path, term: str, window: int = 10) -> str:
    try:
        lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        for i, line in enumerate(lines):
            if term.lower() in line.lower():
                start = max(0, i - window)
                end   = min(len(lines), i + window + 1)
                return "\n".join(f"{ln+1}: {lines[ln]}" for ln in range(start, end))
    except Exception:
        return "Could not read context."
    return "No context found."


# ── Wikilinks (deduplicated, filtered) ────────────────────────────────────────
def extract_wikilinks(text: str, exclude_self: str = "") -> list:
    raw_links = re.findall(r'\[\[([^\]|#]+)', text)
    seen, filtered = set(), []
    for link in raw_links:
        link = link.strip()
        ll   = link.lower()
        if ll == exclude_self.lower():
            continue
        if any(pat in ll for pat in RAW_SOURCE_SUBSTRINGS):
            continue
        if ll in seen:
            continue
        seen.add(ll)
        filtered.append(link)
    return filtered


# ── Build index for ONE directory ─────────────────────────────────────────────
def _build_index_for_dir(search_dir: Path, source_label: str) -> list:
    if not search_dir.exists():
        return []
    index = []
    for md_file in sorted(search_dir.rglob("*.md")):
        if source_label == "wiki" and (
            md_file.name.startswith("_") or md_file.name.startswith(".")
        ):
            continue
        try:
            text     = md_file.read_text(encoding="utf-8", errors="ignore")
            file_fm  = extract_frontmatter(text)
            sections = re.split(r'\n(?=#+ )', text)
            for i, section_text in enumerate(sections):
                heading_match = re.search(r'^#+ (.+)', section_text)
                heading       = heading_match.group(1) if heading_match else md_file.stem
                fm            = file_fm
                node_id       = f"{md_file.stem}::{heading}"
                if len(section_text.strip()) < 50 and i > 0:
                    continue
                index.append({
                    "id":            node_id,
                    "stem":          md_file.stem,
                    "label":         heading,
                    "source_file":   str(md_file.relative_to(WIKI_ROOT)),
                    "source":        source_label,
                    "type":          fm.get("type", "section"),
                    "confidence":    fm.get("confidence", "?"),
                    "tags":          fm.get("tags", []),
                    "aliases":       fm.get("aliases", []),
                    "thesis":        fm.get("thesis", heading),
                    "snippet":       section_text[:200],
                    "_raw_text":     section_text,
                    "search_text":   f"{node_id} {heading} {section_text[:1000]}".lower(),
                    "mtime":         md_file.stat().st_mtime,
                    "half_life_years": fm.get("half_life_years", 10),
                })
        except Exception:
            continue
    return index


# ── Build full index, with pickle cache ───────────────────────────────────────
def build_index(wiki_dir: Path, raw_dir, use_wiki: bool, use_raw: bool) -> list:
    # Key encodes both dirs so cache is invalidated if either changes.
    # Always include canonical raw_dir path to avoid stale-cache-with-no-raw bug.
    raw_root = Path(raw_dir) if raw_dir is not None else WIKI_ROOT / "02_sources"
    if not raw_root.is_absolute():
        raw_root = WIKI_ROOT / raw_root
    canonical_raw = str(raw_root.resolve())
    dirs_key = f"{wiki_dir.resolve()}|{canonical_raw}"
    CACHE_DIR.mkdir(exist_ok=True)

    # Try pickle cache first (avoids filesystem scan on repeated runs)
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "rb") as f:
                cached = pickle.load(f)
            age = time.time() - CACHE_FILE.stat().st_mtime
            if (age < CACHE_TTL
                    and cached.get("dirs_key") == dirs_key
                    and cached.get("cache_format_version") == CACHE_FORMAT_VERSION):
                index = cached["index"]
                cached_sources = {n["source"] for n in index}
                # If cache missing raw entries but raw needed → fall through to cold build
                if use_raw and "raw" not in cached_sources:
                    pass
                else:
                    # FTS5 /tmp DB may be gone (new session) — rebuild silently
                    setup_fts5(index)
                    return [n for n in index
                            if (use_wiki and n["source"] == "wiki")
                            or (use_raw  and n["source"] == "raw")]
        except Exception:
            pass

    # Cold build: always index BOTH wiki and raw so the cache is complete
    index = []
    index += _build_index_for_dir(wiki_dir, "wiki")
    index += _build_index_for_dir(raw_root, "raw")

    setup_fts5(index)

    try:
        with open(CACHE_FILE, "wb") as f:
            pickle.dump({
                "dirs_key":             dirs_key,
                "cache_format_version": CACHE_FORMAT_VERSION,
                "index":                index,
            }, f)
    except Exception:
        pass

    return [n for n in index
            if (use_wiki and n["source"] == "wiki")
            or (use_raw  and n["source"] == "raw")]


# ── BM25-style scorer with field boosting + phrase proximity ──────────────────
def score(node: dict, phrases: list, terms: list) -> float:
    s = 0.0

    raw_aliases = node.get("aliases", [])
    safe_aliases = []
    if isinstance(raw_aliases, list):
        for a in raw_aliases:
            if isinstance(a, str):
                safe_aliases.append(a)
            elif isinstance(a, dict):
                safe_aliases.extend(str(v) for v in a.values())

    fields = {
        "title":   (node.get("label", "").lower(),             5),
        "thesis":  (str(node.get("thesis", "")).lower(),       4),
        "aliases": (" ".join(safe_aliases).lower(),            3),
        "body":    (node.get("_raw_text", "").lower(),         1),
    }

    for _field, (text, boost) in fields.items():
        if not text:
            continue
        # Phrase matching
        for phrase in phrases:
            if phrase in text:
                tf = text.count(phrase)
                s += (tf / (BM25_K1 + tf)) * 100 * boost * 1.5
            words = phrase.split()
            if len(words) > 1:
                pattern = r'.{0,20}'.join(re.escape(w) for w in words)
                if re.search(pattern, text):
                    s += 20 * boost
        # Term matching
        for t in terms:
            if t in text:
                tf = text.count(t)
                s += (tf / (BM25_K1 + tf)) * 20 * boost

    return s


def _file_key(node: dict) -> str:
    raw = node.get("source_file") or node.get("file") or node.get("stem") or ""
    return str(raw).replace("\\", "/").lower()


def _is_clippings_node(node: dict) -> bool:
    tags = node.get("tags", [])
    return isinstance(tags, list) and "clippings" in tags


def _confidence_int(node: dict) -> int | None:
    conf = node.get("confidence", "?")
    if isinstance(conf, int):
        return conf
    if isinstance(conf, str) and conf.strip().isdigit():
        return int(conf.strip())
    return None


def _passes_node_filters(node: dict, filter_type: str | None, min_confidence: int) -> bool:
    if filter_type and filter_type.lower() not in str(node.get("type", "")).lower():
        return False
    if min_confidence > 0:
        conf = _confidence_int(node)
        if conf is None or conf < min_confidence:
            return False
    return True


LOW_SIGNAL_HEADINGS = {
    "index", "contents", "table of contents", "copyright", "dedication",
    "references", "bibliography", "acknowledgements", "acknowledgments",
}


def _is_low_signal_text(text: str) -> bool:
    compact = re.sub(r"\s+", "", text or "")
    if not compact:
        return True
    alnum = sum(1 for ch in compact if ch.isalnum())
    return alnum < 20 or (alnum / max(len(compact), 1)) < 0.25


def _semantic_display_thesis(sem_r: dict, stem: str) -> str:
    thesis = str(sem_r.get("thesis", "")).strip()
    title = str(sem_r.get("title", "")).strip()
    snippet = str(sem_r.get("snippet", "")).strip()
    stem_l = stem.lower()

    if thesis and thesis.lower() != stem_l:
        return thesis
    if title and title.lower() != stem_l:
        return title
    return snippet[:200]


def _semantic_content_is_meaningful(sem_r: dict, stem: str) -> bool:
    title = str(sem_r.get("title", "")).strip()
    snippet = str(sem_r.get("snippet", "")).strip()

    heading = title
    if "—" in heading:
        heading = heading.rsplit("—", 1)[1].strip()
    heading_l = heading.lower()

    if heading_l in LOW_SIGNAL_HEADINGS:
        return False
    if _is_low_signal_text(snippet) and (not heading or heading_l == stem.lower()):
        return False
    return bool(_semantic_display_thesis(sem_r, stem).strip())


# ── Recency decay: score × exp(-ln2 × age / half_life) ───────────────────────
def recency_decay(node: dict, now: float) -> float:
    mtime = node.get("mtime", 0.0)
    hl    = node.get("half_life_years", 10.0)
    if mtime <= 0 or hl <= 0:
        return 1.0
    age_years = (now - mtime) / (365.25 * 86400)
    return math.exp(-math.log(2) * age_years / hl)


# ── MMR-style ranking: BM25 + decay + evidence boost + diversity penalty ──────
def rank(nodes: list, phrases: list, terms: list, top_n: int = 20) -> list:
    now = time.time()
    scored = []
    for n in nodes:
        s = score(n, phrases, terms) * recency_decay(n, now)
        if s <= 0:
            continue
        text = n.get("_raw_text", "").lower()
        if "source_refs" in text or "evidence" in n.get("tags", []):
            s *= 1.5   # boost well-sourced nodes
        if "[llm]" in text:
            s *= 0.5   # penalise LLM-only placeholders
        scored.append((s, n))

    scored.sort(key=lambda x: -x[0])

    # MMR diversity: penalise tag-overlap + per-file cap (max 2 per file,
    # max 1 for clippings)
    final = []
    file_counts: dict = {}
    while scored and len(final) < top_n:
        best_s, best_n = scored.pop(0)
        file_key = _file_key(best_n)
        cap = 1 if _is_clippings_node(best_n) else 2
        if file_counts.get(file_key, 0) >= cap:
            continue
        file_counts[file_key] = file_counts.get(file_key, 0) + 1
        if _is_clippings_node(best_n):
            best_s *= 0.55
        final.append((best_s, best_n))
        best_tags = set(best_n.get("tags", []))
        if not best_tags:
            continue
        for i in range(len(scored)):
            cand_tags = set(scored[i][1].get("tags", []))
            if cand_tags:
                overlap = len(best_tags & cand_tags) / len(best_tags | cand_tags)
                if overlap > 0.3:
                    scored[i] = (scored[i][0] * (1 - overlap), scored[i][1])
        scored.sort(key=lambda x: -x[0])

    return final


# ── Format a single result ─────────────────────────────────────────────────────
def format_result(node: dict, show_related: bool, detail: bool, terms: list) -> str:
    file_p  = WIKI_ROOT / node["source_file"]
    context = "No context found."
    for term in (terms or [node["label"]]):
        context = get_context_with_lines(file_p, term)
        if context != "No context found.":
            break
    res = [
        f"--- RESULT ID: {node['id']} ---",
        f"SOURCE: {node['source']} | FILE: {node['source_file']}",
        f"CONFIDENCE: {node.get('confidence', '?')}",
        f"THESIS: {node.get('thesis', '')}",
        f"EVIDENCE (Line-based Context):\n{context}",
    ]
    if detail and node.get("snippet"):
        res.append(f"SNIPPET: {node['snippet']}")
    if show_related:
        links = extract_wikilinks(node.get("_raw_text", ""), exclude_self=node.get("stem", ""))
        if links:
            res.append(f"RELATED: {', '.join(links[:20])}")
    if node.get("tags"):
        res.append(f"TAGS: {', '.join(node['tags'])}")
    res.append("SUGGESTED_EXPANSION: Search more lines around provided context if thesis is unclear.")
    return "\n".join(res)


# ── Print / collect one result group ──────────────────────────────────────────
def print_group(label: str, scored: list, top_n: int,
                show_related: bool, detail: bool, as_json: bool, terms: list) -> list:
    results = scored[:top_n]
    if not results:
        return []
    if not as_json:
        print(f"\n{'='*2} {label} {'='*(52 - len(label))}")
        for i, (sc, node) in enumerate(results, 1):
            print(f"#{i} [score={sc:.2f}]")
            print(format_result(node, show_related, detail, terms))
            print()
    return [{"score": sc, "source": node["source"], "id": node["id"],
             "thesis": node["thesis"], "snippet": node["snippet"][:200],
             "file": node["source_file"], "tags": node["tags"]}
            for sc, node in results]


# ── Main ──────────────────────────────────────────────────────────────────────
def _rrf_merge(keyword_scored: list, sem_results: list, k: int = 60) -> list:
    """
    Reciprocal Rank Fusion — chuẩn công nghiệp để merge 2 ranked lists.
    RRF score = 1/(k + rank_keyword) + 1/(k + rank_semantic)

    Key design:
    - Dedup theo NODE ID (không phải file) → giữ nguyên section-level granularity
    - Semantic match: thử id exact, rồi fallback stem match (file::section → file)
    - Semantic-only nodes được thêm vào nếu không có keyword match tương ứng
    """
    # Build rank maps: node_id → rank (1-based)
    kw_rank = {}
    for rank_i, (_, node) in enumerate(keyword_scored, 1):
        node_id = node.get("id", "")
        kw_rank[node_id] = rank_i
        # Fallback: match bằng stem (file name không extension)
        stem = node.get("stem", Path(node.get("source_file", "")).stem)
        if stem and stem not in kw_rank:
            kw_rank[stem] = rank_i

    sem_rank = {}
    for rank_i, r in enumerate(sem_results, 1):
        sem_rank[r["id"]] = rank_i
        # Fallback: match bằng stem từ file path
        stem = Path(r["file"]).stem
        if stem and stem not in sem_rank:
            sem_rank[stem] = rank_i

    # Collect all unique candidates by node id
    kw_nodes  = {node.get("id", ""): (sc, node) for sc, node in keyword_scored}
    sem_nodes = {r["id"]: r for r in sem_results}

    all_ids = set(kw_nodes.keys()) | set(sem_nodes.keys())

    merged = []
    seen_ids = set()

    for candidate_id in all_ids:
        if candidate_id in seen_ids:
            continue

        # Keyword rank
        rrf_kw = 0.0
        node   = None
        if candidate_id in kw_nodes:
            _, node = kw_nodes[candidate_id]
            r_kw   = kw_rank.get(candidate_id, len(keyword_scored) + 1)
            rrf_kw = 1.0 / (k + r_kw)

        # Semantic rank — exact id match, then stem fallback
        rrf_sem = 0.0
        sem_r   = sem_nodes.get(candidate_id)
        if sem_r is not None:
            r_sem   = sem_rank.get(candidate_id, len(sem_results) + 1)
            rrf_sem = 1.0 / (k + r_sem)
        elif node is not None:
            stem    = node.get("stem", Path(node.get("source_file", "")).stem)
            r_sem   = sem_rank.get(stem)
            if r_sem:
                rrf_sem = 1.0 / (k + r_sem)

        rrf_score = rrf_kw + rrf_sem

        # Build output node
        if node is None and sem_r is not None:
            stem = Path(sem_r["file"]).stem
            thesis = sem_r.get("thesis", "")
            snippet = sem_r.get("snippet", "")
            # Skip semantic-only nodes that are clearly TOC/index/copyright noise,
            # but keep raw chunks whose snippet/title carries the actual meaning.
            if not _semantic_content_is_meaningful(sem_r, stem):
                continue
            display_thesis = _semantic_display_thesis(sem_r, stem)
            # Semantic-only: synthesize minimal node
            node = {
                "id":              sem_r["id"],
                "stem":            stem,
                "label":           sem_r["title"],
                "source_file":     sem_r["file"],
                "source":          sem_r["source"],
                "thesis":          display_thesis,
                "snippet":         snippet[:200],
                "tags":            sem_r.get("tags", []),
                "aliases":         [],
                "type":            "",
                "confidence":      sem_r.get("confidence", "?"),
                "_raw_text":       snippet or display_thesis,
                "search_text":     display_thesis,
                "mtime":           0,
                "half_life_years": 10,
            }

        if node:
            seen_ids.add(candidate_id)
            merged.append((rrf_score, node))

    merged.sort(key=lambda x: x[0], reverse=True)

    # Remove display duplicates caused by semantic stem fallback. Keep distinct
    # sections from the same raw file when their headings/theses differ.
    deduped = []
    seen_content_by_file: dict[str, list[str]] = {}
    for rrf_s, node in merged:
        file_key = str(node.get("source_file", "")).replace("\\", "/").lower()
        content_key = re.sub(
            r"\s+",
            " ",
            str(node.get("thesis") or node.get("label") or node.get("snippet") or ""),
        ).strip().lower()

        duplicate = False
        for prev_content in seen_content_by_file.get(file_key, []):
            if content_key == prev_content:
                duplicate = True
                break
            shorter, longer = sorted((content_key, prev_content), key=len)
            if len(shorter) >= 40 and longer.startswith(shorter):
                duplicate = True
                break

        if duplicate:
            continue

        seen_content_by_file.setdefault(file_key, []).append(content_key)
        deduped.append((rrf_s, node))

    merged = deduped

    # Per-file cap: max 2 nodes per file; max 1 for clippings-tagged files
    file_counts: dict = {}
    capped = []
    for rrf_s, node in merged:
        file_key = _file_key(node)
        is_clippings = _is_clippings_node(node)
        cap = 1 if is_clippings else 2
        count = file_counts.get(file_key, 0)
        if count >= cap:
            continue
        file_counts[file_key] = count + 1
        # Soft penalty for clippings-tagged nodes (secondary sources)
        if is_clippings:
            rrf_s *= 0.55
        capped.append((rrf_s, node))

    capped.sort(key=lambda x: x[0], reverse=True)
    return capped


def semantic_merge(keyword_scored: list, query: str,
                   wiki_only: bool = False, raw_only: bool = False) -> list:
    """
    Merge keyword BM25 results với semantic search dùng RRF.
    - Luôn chạy nếu FAISS index tồn tại (.cache/wiki_embed.index)
    - Graceful fallback về keyword-only nếu index chưa build
    - wiki_only / raw_only filter áp dụng cho cả 2 sources

    Trả về merged list theo RRF score — có thể dùng thay thế all_scored trực tiếp.
    """
    index_path = WIKI_ROOT / ".cache" / "wiki_embed.index"
    if not index_path.exists():
        return keyword_scored  # no index → fallback gracefully

    try:
        from semantic_search import semantic_search
    except ImportError:
        return keyword_scored

    sem_results = semantic_search(
        query,
        top_k=30,
        threshold=0.28,
        wiki_only=wiki_only,
        raw_only=raw_only,
    )
    if not sem_results:
        return keyword_scored

    return _rrf_merge(keyword_scored, sem_results)


def main():
    parser = argparse.ArgumentParser(description="Wiki + Raw Search Tool v3.6")
    parser.add_argument("query",     nargs="+",          help="Search terms")
    parser.add_argument("--top",     type=int, default=5, help="Max results per group")
    parser.add_argument("--type",    dest="filter_type",  help="Filter by type: concept, mechanism, ...")
    parser.add_argument("--show-related", action="store_true", help="Show wikilinks")
    parser.add_argument("--detail",  action="store_true",      help="Show body snippet")
    parser.add_argument("--json",    action="store_true",      help="Output as JSON")
    parser.add_argument("--min-confidence", type=int, default=0, help="Min confidence (1-5)")
    parser.add_argument("--raw-dir", default="02_sources",     help="Raw sources dir name")
    parser.add_argument("--no-raw",  action="store_true",      help="Search wiki only")
    parser.add_argument("--no-wiki", action="store_true",      help="Search raw only")
    parser.add_argument("--no-semantic", action="store_true",
                        help="Disable semantic merge (keyword BM25 only)")
    args = parser.parse_args()

    # Query routing + synonym expansion
    route   = route_query(" ".join(args.query))
    sources = route.get("sources", ["both"])
    use_wiki = ("wiki" in sources or "both" in sources) and not args.no_wiki
    use_raw  = ("raw"  in sources or "both" in sources) and not args.no_raw
    raw_dir  = WIKI_ROOT / args.raw_dir if use_raw else None

    syn_map         = load_synonyms()
    phrases         = [q.lower() for q in args.query]
    expanded_phrases = expand_query(phrases, syn_map)
    terms           = " ".join(expanded_phrases).split()
    query_str       = " | ".join(expanded_phrases)

    index_exists = (WIKI_ROOT / ".cache" / "wiki_embed.index").exists()
    use_semantic = not args.no_semantic and index_exists
    mode_label   = "RRF(keyword+semantic)" if use_semantic else "keyword-only"
    if not args.json:
        print(f"Searching: [{query_str}]  wiki={use_wiki}  raw={use_raw}  top={args.top}  mode={mode_label}",
              file=sys.stderr)

    # Single build_index call
    index = build_index(WIKI_DIR, raw_dir, use_wiki, use_raw)

    index = [n for n in index
             if _passes_node_filters(n, args.filter_type, args.min_confidence)]

    # BM25 rank
    all_scored = rank(index, phrases, terms, top_n=max(args.top * 8, 40))

    # Semantic merge via RRF (auto if index exists)
    if use_semantic:
        all_scored = semantic_merge(
            all_scored, " ".join(args.query),
            wiki_only=args.no_raw,
            raw_only=args.no_wiki,
        )
        all_scored = [(s, n) for s, n in all_scored
                      if _passes_node_filters(n, args.filter_type, args.min_confidence)]

    wiki_scored = [(s, n) for s, n in all_scored if n["source"] == "wiki"]
    raw_scored  = [(s, n) for s, n in all_scored if n["source"] == "raw"]

    wiki_out = print_group(f"WIKI ({WIKI_DIR.name})", wiki_scored,
                           args.top, args.show_related, args.detail, args.json, terms)
    raw_out  = print_group(f"RAW  ({args.raw_dir})",  raw_scored,
                           args.top, args.show_related, args.detail, args.json, terms)

    if args.json:
        print(json.dumps({"wiki": wiki_out, "raw": raw_out},
                         ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()



