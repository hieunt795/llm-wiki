"""
claim_auditor.py — F.I.T.S.E.R.B.V.L Claim Auditor (v2.0)
===========================================================
Kiểm chứng tính đúng đắn của một wiki node / draft so với toàn bộ wiki.

Steps:
  F — Fit:          Tìm nodes liên quan qua BM25
  I — Inconsistency: Phát hiện nodes mâu thuẫn tiềm năng
  T — Thesis:       Kiểm tra thesis có tồn tại và đủ dài không
  S — Sources:      Kiểm tra source_refs trong frontmatter
  E — Epistemic:    Phát hiện [LLM] placeholder (chưa verify)
  R — Related:      Liệt kê wikilinks hiện có
  B — Bias:         Cảnh báo nếu chỉ có 1 nguồn
  V — Validation:   Kiểm tra confidence score
  L — Links:        Phát hiện broken wikilinks (link đến node không tồn tại)

Usage:
  python claim_auditor.py path/to/node.md
  python claim_auditor.py 03_wiki/mechanisms/Fiscal_Dominance.md
"""

import sys
import re
import yaml
import argparse
from pathlib import Path

# Fix Windows terminal UTF-8 encoding without replacing stdio wrappers
if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT  = SCRIPT_DIR.parent.parent
WIKI_DIR   = WIKI_ROOT / "03_wiki"


def read_file(path):
    try:
        return Path(path).read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return ""


def extract_frontmatter(content):
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            try:
                return yaml.safe_load(content[3:end]) or {}
            except Exception:
                pass
    return {}


def extract_wikilinks(content):
    links = re.findall(r'\[\[([^\]|#]+)', content)
    return [l.strip() for l in links if len(l.strip()) > 2]


def get_all_wiki_stems():
    stems = set()
    if WIKI_DIR.exists():
        for fp in WIKI_DIR.rglob("*.md"):
            stems.add(fp.stem)
    return stems


def bm25_search(query_terms, top_n=5):
    """Lightweight BM25 search — reuse logic from wiki_search."""
    sys.path.insert(0, str(SCRIPT_DIR.parent))
    try:
        from wiki_search import build_index, score as bm25_score
        index = build_index(WIKI_DIR, None, use_wiki=True, use_raw=False)
        scored = [(bm25_score(n, query_terms, query_terms), n) for n in index]
        scored = [(s, n) for s, n in scored if s > 0]
        scored.sort(key=lambda x: -x[0])
        return scored[:top_n]
    except Exception as e:
        return []


def sep(char="─", n=55):
    print(char * n)


def run_audit(file_path):
    path = Path(file_path)
    if not path.exists():
        # Try relative to wiki root
        path = WIKI_ROOT / file_path
    if not path.exists():
        print("Error: File not found: {}".format(file_path))
        sys.exit(1)

    content = read_file(path)
    fm      = extract_frontmatter(content)
    links   = extract_wikilinks(content)
    stems   = get_all_wiki_stems()

    node_id       = path.stem
    thesis        = str(fm.get("thesis", "")).strip()
    tags          = fm.get("tags", [])
    conf          = fm.get("confidence", "?")
    srefs         = fm.get("source_refs", [])
    status        = str(fm.get("status", "")).strip()
    superseded_by = fm.get("superseded_by", None)
    half_life     = fm.get("half_life_years", None)

    VALID_STATUSES  = {"draft", "reviewed", "verified", "stale", "archived", "conflict"}
    LEGACY_STATUSES = {"active": "verified", "deprecated": "archived", "researching": "draft"}

    print()
    sep("═")
    print("CLAIM AUDIT: F.I.T.S.E.R.B.V.L")
    print("Target: {}".format(path.name))
    sep("═")

    # ── F — FIT ──────────────────────────────────────────────────────────────
    print("\n[F] FIT — Related nodes via BM25")
    query_terms = (thesis.lower().split()[:8] if thesis
                   else node_id.lower().replace("_", " ").split())
    results = bm25_search(query_terms)
    if results:
        for sc, n in results:
            if n["id"] != node_id:
                print("  [{:6.1f}] [[{}]] — {}".format(sc, n["id"], n.get("thesis","")[:80]))
    else:
        print("  (no related nodes found — check wiki_search availability)")

    # ── I — INCONSISTENCY ────────────────────────────────────────────────────
    print("\n[I] INCONSISTENCY — Tension candidates")
    tension_keywords = ["however", "but", "contrast", "unlike", "whereas",
                        "mâu thuẫn", "ngược lại", "tuy nhiên", "nhưng"]
    body = content[content.find("---", 3)+3:] if content.startswith("---") else content
    tension_lines = [l.strip() for l in body.splitlines()
                     if any(kw in l.lower() for kw in tension_keywords)]
    if tension_lines:
        for l in tension_lines[:3]:
            print("  ⚠  {}".format(l[:100]))
    else:
        print("  ✓  No explicit contradictions found in body text.")

    # ── T — THESIS ───────────────────────────────────────────────────────────
    print("\n[T] THESIS — Quality check")
    if not thesis:
        print("  ✗  MISSING thesis in frontmatter.")
    elif len(thesis) < 30:
        print("  ⚠  Thesis too short ({} chars): {}".format(len(thesis), thesis))
    else:
        print("  ✓  Thesis present ({} chars)".format(len(thesis)))
        print("     {}".format(thesis[:120]))


    # ── STATUS — Lifecycle check ─────────────────────────────────────────────
    print("\n[STATUS] LIFECYCLE — Node status & half-life")
    if not status:
        print("  ⚠  status not set — default to 'draft'.")
    elif status in LEGACY_STATUSES:
        mapped = LEGACY_STATUSES[status]
        print("  [legacy] status: {} → migrate to '{}'".format(status, mapped))
    elif status not in VALID_STATUSES:
        print("  ✗  Invalid status '{}' — must be one of: {}".format(
            status, ", ".join(sorted(VALID_STATUSES))))
    else:
        icons = {"draft":"[draft]","reviewed":"[reviewed]","verified":"[verified]",
                 "stale":"[stale]","archived":"[archived]","conflict":"[CONFLICT]"}
        print("  {}  status: {}".format(icons.get(status,"?"), status))
        if status in ("stale", "archived") and not superseded_by:
            print("  ⚠  status={} but superseded_by not set.".format(status))
        if status == "conflict":
            print("  ⚠  Node marked CONFLICT — resolve before merge.")
    if half_life is None:
        print("  ⚠  half_life_years not set — search will use default (10y).")
    else:
        hints = {0.1:"market-data", 0.5:"synthesis", 1.0:"regulation/policy", 10:"mechanism/theory"}
        hint = hints.get(float(half_life), "custom")
        print("  ✓  half_life_years: {} ({})".format(half_life, hint))

    # ── S — SOURCES ──────────────────────────────────────────────────────────
    print("\n[S] SOURCES — source_refs check")
    if not srefs:
        print("  ⚠  No source_refs in frontmatter — claim is unanchored.")
    else:
        print("  ✓  {} source ref(s) found:".format(len(srefs)))
        for ref in (srefs if isinstance(srefs, list) else [srefs])[:3]:
            print("     - {}".format(str(ref)[:80]))

    # ── E — EPISTEMIC ────────────────────────────────────────────────────────
    print("\n[E] EPISTEMIC — LLM placeholder detection")
    llm_count = content.count("[LLM]")
    if llm_count > 0:
        print("  ⚠  {} [LLM] placeholder(s) found — needs RAW source verification.".format(llm_count))
    else:
        print("  ✓  No [LLM] placeholders.")

    # ── R — RELATED ──────────────────────────────────────────────────────────
    print("\n[R] RELATED — Wikilinks in this node")
    clean = [l for l in links if not re.search(r'\.pdf|_Ch\d+|_P\d+|trang-', l, re.I)]
    if clean:
        print("  {} link(s): {}".format(len(clean), ", ".join("[[{}]]".format(l) for l in clean[:6])))
        if len(clean) > 6:
            print("  ... and {} more".format(len(clean) - 6))
    else:
        print("  ⚠  No clean wikilinks — node may be isolated.")

    # ── B — BIAS ─────────────────────────────────────────────────────────────
    print("\n[B] BIAS — Source diversity")
    ref_count = len(srefs) if isinstance(srefs, list) else (1 if srefs else 0)
    if ref_count == 0:
        print("  ✗  No sources — fully unverified.")
    elif ref_count == 1:
        print("  ⚠  Single source — potential confirmation bias.")
    else:
        print("  ✓  {} sources — adequate diversity.".format(ref_count))

    # ── V — VALIDATION ───────────────────────────────────────────────────────
    print("\n[V] VALIDATION — Confidence score")
    try:
        c = int(conf)
        bar = "█" * c + "░" * (5 - c)
        label = {1:"very low",2:"low",3:"medium",4:"high",5:"verified"}.get(c,"?")
        print("  confidence: {}/5 [{}] {}".format(c, bar, label))
        if c <= 2:
            print("  ⚠  Low confidence — prioritize for RAW verification.")
    except Exception:
        print("  ⚠  Confidence not set (value: {})".format(conf))

    # ── L — LINKS ────────────────────────────────────────────────────────────
    print("\n[L] LINKS — Broken wikilink detection")
    broken = [l for l in clean if l not in stems]
    if broken:
        print("  ✗  {} broken link(s):".format(len(broken)))
        for b in broken[:5]:
            print("     [[{}]] — node does not exist".format(b))
    else:
        print("  ✓  All {} wikilinks resolve to existing nodes.".format(len(clean)))

    # ── VERDICT ──────────────────────────────────────────────────────────────
    print()
    sep()
    issues = []
    if not thesis:                issues.append("missing thesis")
    if not srefs:                 issues.append("no source_refs")
    if llm_count > 0:             issues.append("{} LLM placeholders".format(llm_count))
    if not status or (status not in VALID_STATUSES and status not in LEGACY_STATUSES): issues.append("status unset/invalid")
    if status == "conflict":      issues.append("status=conflict (unresolved)")
    if status in ("stale","archived") and not superseded_by: issues.append("superseded_by missing")
    if half_life is None:         issues.append("half_life_years unset")
    if broken:                    issues.append("{} broken links".format(len(broken)))
    if ref_count <= 1:            issues.append("single/no source")
    try:
        if int(conf) <= 2:        issues.append("low confidence")
    except Exception:
        issues.append("confidence unset")

    if not issues:
        print("VERDICT: ✓  PASS — Node is well-formed.")
    else:
        print("VERDICT: ⚠  NEEDS WORK — {} issue(s): {}".format(
            len(issues), " | ".join(issues)))
    sep()


def main():
    parser = argparse.ArgumentParser(description="F.I.T.S.E.R.B.V.L Claim Auditor v2.0")
    parser.add_argument("file", help="Path to wiki node or draft file to audit")
    args = parser.parse_args()
    run_audit(args.file)


if __name__ == "__main__":
    main()


