"""
deepdive_search.py — Deep Research: Detect → Drill → Draft (v2.1)
Usage:
  python 05_scripts/deepdive_search.py "fiscal dominance"
  python 05_scripts/deepdive_search.py "LCR mechanics" --threshold 3
  python librarian.py deepdive "interest rate corridor"

Pipeline:
  STAGE 1 — DETECT:  wiki_search top results → evaluate confidence/[LLM]/source_refs
  STAGE 2 — DRILL:   hybrid_search on RAW sources for thin/missing topics
  STAGE 3 — DRAFT:   output structured expansion proposal to 04_outputs/drafts/

Trigger criteria for "thin" node:
  - confidence ≤ threshold (default: 2)
  - body text contains "[LLM]" placeholder
  - body text has no source_refs section
  - node not found in wiki at all
"""

import argparse
import json
import sys
import io
import re
from pathlib import Path
from datetime import datetime

# Force UTF-8 on Windows
if sys.platform == 'win32':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')

SCRIPT_DIR  = Path(__file__).parent
WIKI_ROOT   = SCRIPT_DIR.parent.parent
WIKI_DIR    = WIKI_ROOT / "03_wiki"
DRAFTS_DIR  = WIKI_ROOT / "04_outputs" / "drafts"
DRAFTS_DIR.mkdir(parents=True, exist_ok=True)

# ── Import search modules ─────────────────────────────────────────────────────
sys.path.insert(0, str(SCRIPT_DIR.parent))
from wiki_search import build_index, rank, semantic_merge, WIKI_DIR as _WD
from hybrid_search import hybrid_search


# ── Thin-node detector ────────────────────────────────────────────────────────
def is_thin(node: dict, threshold: int) -> tuple[bool, list[str]]:
    """Returns (thin: bool, reasons: list[str])."""
    reasons = []
    conf = node.get("confidence", "?")
    if isinstance(conf, int) and conf <= threshold:
        reasons.append(f"confidence={conf} ≤ {threshold}")
    body = node.get("_raw_text", "").lower()
    if "[llm]" in body:
        reasons.append("body contains [LLM] placeholder")
    if "source_refs" not in body and "source_ref" not in body:
        reasons.append("no source_refs section")
    return bool(reasons), reasons


# ── Format context snippet for draft ─────────────────────────────────────────
def fmt_raw_hit(hit: dict) -> str:
    lines = [
        f"### RAW: {hit['id']}",
        f"- file: `{hit['file']}`",
        f"- score: {hit['score']:.3f}",
    ]
    if hit.get("thesis"):
        lines.append(f"- thesis: {hit['thesis'][:200]}")
    ctx = hit.get("context", "").strip()
    if ctx:
        lines.append("- heatmap context:")
        lines.append("```")
        lines.append(ctx[:600])
        lines.append("```")
    return "\n".join(lines)


# ── Main pipeline ─────────────────────────────────────────────────────────────
def deep_dive(query: str, threshold: int = 2) -> None:
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug     = re.sub(r"[^\w]+", "_", query.lower())[:40].strip("_")
    out_file = DRAFTS_DIR / f"{date_str}_{slug}_deepdive.md"

    print(f"\n{'='*60}")
    print(f"[DEEPDIVE v2.1] Query: '{query}'  threshold={threshold}")
    print(f"{'='*60}")

    # ── STAGE 1: DETECT — wiki BM25 + semantic RRF ───────────────────────────
    index_exists = (WIKI_ROOT / ".cache" / "wiki_embed.index").exists()
    detect_mode  = "BM25+semantic" if index_exists else "BM25-only"
    print(f"\n--- [STAGE 1: DETECT — {detect_mode}] ---")
    raw_dir_path = WIKI_ROOT / "02_sources"
    index = build_index(WIKI_DIR, raw_dir_path, use_wiki=True, use_raw=False)

    phrases = [query.lower()]
    terms   = query.lower().split()
    scored  = rank(index, phrases, terms, top_n=20)

    # Semantic merge — critical for deepdive: concept queries often miss BM25
    if index_exists:
        scored = semantic_merge(scored, query, wiki_only=True)

    wiki_hits = [(s, n) for s, n in scored if n["source"] == "wiki"][:8]

    thin_nodes  = []
    solid_nodes = []
    for sc, node in wiki_hits:
        thin, reasons = is_thin(node, threshold)
        if thin:
            thin_nodes.append((sc, node, reasons))
            print(f"  ⚠ THIN  [{node['id']}]  conf={node.get('confidence','?')}  → {', '.join(reasons)}")
        else:
            solid_nodes.append((sc, node))
            print(f"  ✓ SOLID [{node['id']}]  conf={node.get('confidence','?')}")

    if not wiki_hits:
        print(f"  ✗ NOT FOUND in wiki — escalating to RAW directly")
        thin_nodes = []  # treat entire query as thin

    # ── STAGE 2: DRILL — hybrid_search on RAW ────────────────────────────────
    print(f"\n--- [STAGE 2: DRILL — hybrid_search RAW sources] ---")
    drill_needed = bool(thin_nodes) or not wiki_hits
    raw_results  = []

    if drill_needed:
        h_out = hybrid_search(query, top=3, use_wiki=False, use_raw=True, as_json=True)
        raw_results = h_out.get("raw", [])
        if raw_results:
            print(f"  Found {len(raw_results)} RAW hits:")
            for r in raw_results:
                print(f"    → [{r['id']}]  score={r['score']:.3f}  file={r['file']}")
        else:
            print(f"  No RAW hits found for '{query}'")
    else:
        print(f"  Skipped (all wiki nodes solid at threshold={threshold})")

    # ── STAGE 3: DRAFT ────────────────────────────────────────────────────────
    print(f"\n--- [STAGE 3: DRAFT → {out_file.name}] ---")

    draft_lines = [
        f"---",
        f"title: DeepDive — {query}",
        f"date: {date_str}",
        f"query: \"{query}\"",
        f"threshold: {threshold}",
        f"wiki_hits: {len(wiki_hits)}",
        f"thin_nodes: {len(thin_nodes)}",
        f"raw_hits: {len(raw_results)}",
        f"status: draft",
        f"---",
        f"",
        f"# DeepDive: {query}",
        f"",
        f"## STAGE 1 — Wiki Coverage",
        f"",
    ]

    if not wiki_hits:
        draft_lines.append(f"> ✗ **NOT FOUND** in wiki. Topic needs SPAWN node.")
    else:
        for sc, node, *rest in [(s, n, r) for s, n, r in thin_nodes] + [(s, n, []) for s, n in solid_nodes]:
            reasons = rest[0] if rest else []
            status  = "⚠ THIN" if reasons else "✓ SOLID"
            draft_lines.append(f"- {status} `{node['id']}` conf={node.get('confidence','?')}")
            if reasons:
                draft_lines.append(f"  - Issues: {', '.join(reasons)}")
            if node.get("thesis"):
                draft_lines.append(f"  - Thesis: {node['thesis'][:200]}")

    draft_lines += [
        f"",
        f"## STAGE 2 — RAW Source Evidence",
        f"",
    ]

    if not raw_results:
        draft_lines.append("> No RAW hits found. Consider manual `librarian.py scout` or `librarian.py section`.")
    else:
        for hit in raw_results:
            draft_lines.append(fmt_raw_hit(hit))
            draft_lines.append("")

    draft_lines += [
        f"## STAGE 3 — Expansion Proposal",
        f"",
        f"> **Action required:** Review RAW evidence above, then:",
        f"",
    ]

    if not wiki_hits:
        draft_lines.append(f"- [ ] SPAWN new wiki node: `03_wiki/concepts/{slug}.md`")
        draft_lines.append(f"- [ ] Fill thesis, mechanism, source_refs from RAW evidence above")
    else:
        for _, node, reasons in thin_nodes:
            node_file = node.get("source_file", "")
            draft_lines.append(f"- [ ] UPDATE `{node_file}` — address: {', '.join(reasons)}")
            draft_lines.append(f"      Add source_refs from RAW hits above")

    draft_lines += [
        f"",
        f"---",
        f"*Generated by deepdive_search.py v2.1 on {date_str}*",
    ]

    draft_text = "\n".join(draft_lines)
    out_file.write_text(draft_text, encoding="utf-8")

    summary = (f"wiki={len(wiki_hits)} hits, thin={len(thin_nodes)}, "
               f"raw={len(raw_results)} hits → draft: {out_file.name}")
    print(f"\nSUMMARY: {summary}")
    print(f"Draft saved → {out_file}")


def main():
    parser = argparse.ArgumentParser(description="DeepDive Search v2.1 — Detect → Drill → Draft")
    parser.add_argument("query",                           help="Research query")
    parser.add_argument("--threshold", type=int, default=2, help="Thin-node confidence threshold (default: 2)")
    parser.add_argument("--top",       type=int, default=8, help=argparse.SUPPRESS)  # forwarded by pipeline, ignored here
    args = parser.parse_args()
    deep_dive(args.query, threshold=args.threshold)


if __name__ == "__main__":
    main()


