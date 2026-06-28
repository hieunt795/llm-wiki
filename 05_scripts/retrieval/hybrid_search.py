"""
hybrid_search.py — Hybrid Search v3.3 (Graphify + BM25 + Fuzzy Heatmap)
Usage:
  python 05_scripts/hybrid_search.py "fiscal dominance"
  python 05_scripts/hybrid_search.py "interest rate" --top 3 --no-wiki
  python 05_scripts/hybrid_search.py "central bank" --no-raw
  python 05_scripts/hybrid_search.py "LCR" --raw-only
  python 05_scripts/hybrid_search.py "private credit" --json

Pipeline:
  STEP 1 — Graphify: query graph.json for structural neighbors (wiki link graph)
  STEP 2 — BM25:     rank wiki + raw index by relevance score
  STEP 3 — Heatmap:  fuzzy context windows from top-scoring source files

Changes v3.3:
  - CLI --budget is now applied to graphify neighbor retrieval
  - CLI supports --no-raw for wiki-only heatmap search
  - RRF scores are printed with useful precision

Changes v3.2:
  - Graphify: reads graphify-out/graph.json directly (no CLI dependency)
  - BM25: uses direct Python import (no subprocess / python vs python3 issue)
  - File paths: all resolved from WIKI_ROOT
  - Returns structured dict usable by deepdive_search
"""

import json
import argparse
import sys
import re
from pathlib import Path

# Force UTF-8 output on Windows
if sys.platform == 'win32':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')

SCRIPT_DIR  = Path(__file__).parent
WIKI_ROOT   = SCRIPT_DIR.parent.parent
GRAPH_JSON  = WIKI_ROOT / "graphify-out" / "graph.json"

# Ensure 05_scripts/ is on path
if str(SCRIPT_DIR.parent) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR.parent))

from wiki_search import build_index, rank, semantic_merge, WIKI_DIR


# ── Graphify graph query ───────────────────────────────────────────────────────

def _load_graph():
    """Load and cache graph.json. Returns (nodes_by_id, links) or ({}, [])."""
    if not GRAPH_JSON.exists():
        return {}, []
    try:
        data = json.loads(GRAPH_JSON.read_text(encoding="utf-8", errors="ignore"))
        nodes = data.get("nodes", [])
        links = data.get("links", [])
        nodes_by_id = {n["id"]: n for n in nodes}
        return nodes_by_id, links
    except Exception:
        return {}, []


def graphify_query(query: str, budget: int = 20) -> dict:
    """
    Query graph.json for nodes matching the query string.
    Returns dict: { 'matched_nodes': [...], 'neighbors': [...], 'thesis': str }
    Each node: { 'id', 'label', 'community', 'source_file', 'relation', 'direction' }
    """
    nodes_by_id, links = _load_graph()
    if not nodes_by_id:
        return {"matched_nodes": [], "neighbors": [], "thesis": ""}

    q_lower = query.lower()
    q_terms = [t for t in q_lower.split() if len(t) > 2]

    # Score each node by label match
    def node_score(n):
        label = n.get("norm_label", n.get("label", "")).lower()
        s = 0
        if q_lower in label:
            s += 100
        for t in q_terms:
            if t in label:
                s += 20
        return s

    scored_nodes = [(node_score(n), n) for n in nodes_by_id.values()]
    scored_nodes = [(s, n) for s, n in scored_nodes if s > 0]
    scored_nodes.sort(key=lambda x: -x[0])
    matched = [n for _, n in scored_nodes[:5]]

    if not matched:
        return {"matched_nodes": [], "neighbors": [], "thesis": ""}

    # Gather neighbors for top matched node
    primary = matched[0]
    p_id    = primary["id"]
    thesis  = ""
    neighbors = []
    seen_ids  = set()

    for lnk in links:
        src_id = lnk.get("source", lnk.get("_src", ""))
        tgt_id = lnk.get("target", lnk.get("_tgt", ""))
        rel    = lnk.get("relation", lnk.get("label", lnk.get("type", "")))

        # Capture thesis edge
        if src_id == p_id and rel == "has_thesis":
            tgt = nodes_by_id.get(tgt_id, {})
            thesis = tgt.get("label", "")
            continue

        # Skip pure code edges (contains/calls/imports) — only keep reference edges
        if rel in ("contains", "calls", "imports", "defines", "uses"):
            continue

        if src_id == p_id and tgt_id not in seen_ids:
            tgt = nodes_by_id.get(tgt_id, {})
            if tgt:
                neighbors.append({
                    "id": tgt_id, "label": tgt.get("label", tgt_id),
                    "community": tgt.get("community", "?"),
                    "source_file": tgt.get("source_file", ""),
                    "relation": rel, "direction": "out"
                })
                seen_ids.add(tgt_id)

        elif tgt_id == p_id and src_id not in seen_ids:
            src = nodes_by_id.get(src_id, {})
            if src:
                neighbors.append({
                    "id": src_id, "label": src.get("label", src_id),
                    "community": src.get("community", "?"),
                    "source_file": src.get("source_file", ""),
                    "relation": rel, "direction": "in"
                })
                seen_ids.add(src_id)

        if len(neighbors) >= budget:
            break

    return {
        "matched_nodes": [{"id": n["id"], "label": n.get("label",""), "community": n.get("community","?"),
                           "source_file": n.get("source_file","")} for n in matched],
        "neighbors": neighbors[:budget],
        "thesis": thesis,
    }


def format_graphify_output(g: dict) -> str:
    """Format graphify result for human-readable output."""
    if not g["matched_nodes"]:
        return "  [No matches in graph.json]"

    lines = []
    primary = g["matched_nodes"][0]
    lines.append(f"  Primary match: [{primary['id']}]  community={primary['community']}")
    if g["thesis"]:
        lines.append(f"  Thesis: {g['thesis'][:180]}")
    if len(g["matched_nodes"]) > 1:
        others = [n["label"] for n in g["matched_nodes"][1:]]
        lines.append(f"  Also matched: {', '.join(others[:4])}")

    if g["neighbors"]:
        out_n = [n for n in g["neighbors"] if n["direction"] == "out"]
        in_n  = [n for n in g["neighbors"] if n["direction"] == "in"]
        if out_n:
            lines.append(f"  Links TO ({len(out_n)}): " +
                         ", ".join(f'[[{n["label"]}]]' for n in out_n[:8]))
        if in_n:
            lines.append(f"  Links FROM ({len(in_n)}): " +
                         ", ".join(f'[[{n["label"]}]]' for n in in_n[:8]))
    return "\n".join(lines)


# ── File reader ────────────────────────────────────────────────────────────────

def read_file_safe(file_path: Path) -> str:
    try:
        return file_path.read_text(encoding='utf-8', errors='ignore')
    except UnicodeDecodeError:
        try:
            return file_path.read_text(encoding='utf-16', errors='ignore')
        except Exception:
            return ""
    except Exception:
        return ""


# ── Fuzzy heatmap ─────────────────────────────────────────────────────────────

def get_fuzzy_heatmap_context(file_path: Path, query: str,
                               window: int = 5, num_samples: int = 5) -> str:
    """
    Find lines containing query terms, return context windows distributed
    evenly (0%, 25%, 50%, 75%, 100%) across all hit positions in the file.
    """
    terms = [t.lower() for t in query.split() if len(t) > 3]
    if not terms:
        return ""

    content_raw = read_file_safe(file_path)
    if not content_raw:
        return f"[Could not read: {file_path.name}]"

    content = content_raw.splitlines()
    hits = [i for i, line in enumerate(content) if any(t in line.lower() for t in terms)]
    if not hits:
        return ""

    if len(hits) <= num_samples:
        selected = hits
    else:
        selected = []
        for p in [0.0, 0.25, 0.5, 0.75, 1.0]:
            idx = int(p * (len(hits) - 1))
            val = hits[idx]
            if val not in selected:
                selected.append(val)

    output_blocks = []
    for line_idx in selected:
        start = max(0, line_idx - window)
        end   = min(len(content), line_idx + window + 1)
        block = []
        for j in range(start, end):
            prefix = ">>>" if j == line_idx else "   "
            block.append(f"      {prefix} L{j+1}: {content[j].strip()}")
        output_blocks.append("\n".join(block))

    return "\n      [... skip to next heatmap section ...]\n".join(output_blocks)


# ── Main search function ───────────────────────────────────────────────────────

def hybrid_search(query: str, top: int = 3, use_wiki: bool = True, use_raw: bool = True,
                  as_json: bool = False, budget: int = 20) -> dict:
    """
    Full hybrid search pipeline:
      1. Graphify graph.json → structural neighbors
      2. BM25 index → scored wiki + raw results
      3. Fuzzy heatmap → context windows from source files

    Returns:
      { 'graphify': dict, 'wiki': [...], 'raw': [...] }
    """
    results = {"graphify": {}, "wiki": [], "raw": []}

    if not as_json:
        print(f"\n[HYBRID SEARCH v3.3] Query: '{query}'  wiki={use_wiki}  raw={use_raw}")

    # ── Step 1: Graphify structural neighbors ─────────────────────────────────
    g_result = graphify_query(query, budget=budget)
    results["graphify"] = g_result

    if not as_json:
        print("\n=== STEP 1: GRAPHIFY — Structural Neighbors ===")
        print(format_graphify_output(g_result))

    # ── Step 2: BM25 + Semantic RRF merge ────────────────────────────────────
    index_exists = (WIKI_ROOT / ".cache" / "wiki_embed.index").exists()
    step2_label  = "BM25 + SEMANTIC RRF" if index_exists else "BM25 (no semantic index)"
    if not as_json:
        print(f"\n=== STEP 2: {step2_label} ===")

    index  = build_index(WIKI_DIR, WIKI_ROOT / "02_sources",
                         use_wiki=use_wiki, use_raw=use_raw)
    phrases = [query.lower()]
    terms   = query.lower().split()
    scored  = rank(index, phrases, terms, top_n=max(top * 12, 60))

    # Semantic merge via RRF — auto if index exists, graceful fallback if not
    if index_exists:
        scored = semantic_merge(
            scored, query,
            wiki_only=not use_raw,
            raw_only=not use_wiki,
        )
    wiki_hits = [(s, n) for s, n in scored if n["source"] == "wiki"][:top]
    raw_hits  = [(s, n) for s, n in scored if n["source"] == "raw"][:top]

    # ── Step 3: Fuzzy heatmap for each result ────────────────────────────────
    for source_label, hits, key in [("WIKI", wiki_hits, "wiki"), ("RAW", raw_hits, "raw")]:
        if not hits:
            continue
        if not as_json:
            print(f"\n[{source_label}] Top {len(hits)} results:")

        for i, (sc, node) in enumerate(hits, 1):
            rel_path = node.get("source_file", "")
            abs_path = WIKI_ROOT / rel_path if rel_path else None
            context  = ""
            if abs_path and abs_path.exists():
                context = get_fuzzy_heatmap_context(abs_path, query)

            entry = {
                "id":      node.get("id", ""),
                "score":   sc,
                "file":    rel_path,
                "thesis":  str(node.get("thesis", "")),
                "tags":    node.get("tags", []),
                "context": context,
            }
            results[key].append(entry)

            if not as_json:
                print(f"  #{i} [{source_label}] {node.get('id','')[:70]}  score={sc:.3f}")
                print(f"      file: {rel_path}")
                thesis = str(node.get("thesis", ""))
                if thesis and thesis != node.get("id",""):
                    print(f"      thesis: {thesis[:120]}")
                if context:
                    print(f"      Heatmap (+/-5 lines):")
                    print(context[:800])
                print()

    if not as_json:
        print(f"[HYBRID SEARCH v3.3] Done — graphify={len(g_result.get('neighbors',[]))} neighbors"
              f"  wiki={len(results['wiki'])}  raw={len(results['raw'])}")

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hybrid Search v3.3 — Graphify + BM25 + Heatmap")
    parser.add_argument("query",           help="Search query")
    parser.add_argument("--top", type=int, default=3, help="Max results per source group (default: 3)")
    parser.add_argument("--no-wiki",       action="store_true", help="Skip wiki BM25 results")
    parser.add_argument("--no-raw",        action="store_true", help="Skip raw source results")
    parser.add_argument("--raw-only",      action="store_true", help="Alias for --no-wiki")
    parser.add_argument("--json",          action="store_true", help="Output as JSON")
    parser.add_argument("--budget", type=int, default=20, help="Max graphify neighbors (default: 20)")
    args = parser.parse_args()

    no_wiki = args.no_wiki or args.raw_only
    out = hybrid_search(args.query, top=args.top,
                        use_wiki=not no_wiki, use_raw=not args.no_raw,
                        as_json=args.json, budget=args.budget)
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))



