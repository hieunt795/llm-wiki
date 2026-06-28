"""
auto_synthesis.py — Wisdom-Layer Synthesis Engine (v2.2)
Pipeline: check_staleness -> read_context -> collect -> subgraph -> hubs -> collisions -> clusters -> LLM -> report -> writeback

v2.2 changes:
  - STALENESS DETECTION: so sánh mtime của nodes vs report, cảnh báo nếu stale
  - --check mode: scan tất cả tags, in staleness status mà không chạy synthesis
  - W2 hook: Phase D ingest có thể gọi --check để biết tags nào cần re-run

Usage:
  python auto_synthesis.py "monetary-policy"
  python auto_synthesis.py "fixed-income" --top-hubs 5 --no-llm
  python auto_synthesis.py "central-banking" --model claude-sonnet-4-6
  python auto_synthesis.py "monetary-policy" --no-writeback
  python auto_synthesis.py --check                              # scan staleness toàn bộ tags
  python auto_synthesis.py --check --stale-only                # chỉ hiện tags stale
"""

import sys
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import re
import yaml
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict, Counter

WIKI_ROOT  = Path("03_wiki")
OUTPUT_DIR = Path("04_outputs/research")
HOT_MD     = Path("01_schema/hot.md")
MEMORY_MD  = Path("01_schema/memory.md")
RAW_FILTER = re.compile(r'\.pdf|_Ch\d+|_P\d+|\.md|trang-', re.I)

# ── STALENESS DETECTION ───────────────────────────────────────────────────────

def get_tag_node_mtimes():
    """Quét toàn bộ wiki, trả về {tag: [mtime, ...]} cho mọi tag."""
    tag_mtimes = {}
    for fp in WIKI_ROOT.rglob("*.md"):
        try:
            content = fp.read_text(encoding="utf-8", errors="ignore")
            if not content.startswith("---"):
                continue
            end = content.find("---", 3)
            if end == -1:
                continue
            try:
                fm = yaml.safe_load(content[3:end]) or {}
            except Exception:
                fm = {}
            tags = fm.get("tags", [])
            if isinstance(tags, str):
                tags = [tags]
            tags = [str(t).lower() for t in tags if t]
            mtime = fp.stat().st_mtime
            for tag in tags:
                tag_mtimes.setdefault(tag, []).append(mtime)
        except Exception:
            pass
    return tag_mtimes


def get_existing_reports():
    """Đọc tất cả wisdom reports hiện có, trả về {tag: {file, mtime, date}}."""
    reports = {}
    if not OUTPUT_DIR.exists():
        return reports
    for fp in OUTPUT_DIR.glob("*_wisdom.md"):
        stem = fp.stem  # e.g. "2026-04-26_monetary_policy_wisdom"
        base = stem.split("_wisdom")[0]  # "2026-04-26_monetary_policy"
        if len(base) < 11:
            continue
        tag_part = base[11:].replace("_", "-")  # "monetary-policy"
        reports[tag_part] = {
            "file":  fp.name,
            "path":  fp,
            "mtime": fp.stat().st_mtime,
            "date":  base[:10],
        }
    return reports


def check_staleness(tag, nodes, verbose=True):
    """
    So sánh mtime của nodes trong tag vs wisdom report hiện có.
    Trả về dict: {stale: bool, newer_count: int, report_date: str, report_file: str}
    """
    reports = get_existing_reports()
    if tag not in reports:
        if verbose:
            print("  [STALENESS] No existing report for '{}' — will create fresh.".format(tag))
        return {"stale": False, "newer_count": 0, "report_date": None, "report_file": None}

    report = reports[tag]
    report_mtime = report["mtime"]

    # Đếm nodes mới hơn report (dựa trên file mtime của .md trong wiki)
    newer_nodes = []
    for fp in WIKI_ROOT.rglob("*.md"):
        try:
            content = fp.read_text(encoding="utf-8", errors="ignore")
            if not content.startswith("---"):
                continue
            end = content.find("---", 3)
            if end == -1:
                continue
            try:
                fm = yaml.safe_load(content[3:end]) or {}
            except Exception:
                fm = {}
            tags = fm.get("tags", [])
            if isinstance(tags, str):
                tags = [tags]
            tags = [str(t).lower() for t in tags if t]
            if tag in tags and fp.stat().st_mtime > report_mtime:
                newer_nodes.append(fp.stem)
        except Exception:
            pass

    is_stale = len(newer_nodes) > 0
    if verbose and is_stale:
        print("  ⚠️  [STALE] Report '{}' is outdated.".format(report["file"]))
        print("      {} node(s) added/modified since {}: {}".format(
            len(newer_nodes), report["date"],
            ", ".join(newer_nodes[:5]) + ("..." if len(newer_nodes) > 5 else "")
        ))
        print("      → Re-run to refresh: python auto_synthesis.py \"{}\"".format(tag))
    elif verbose:
        print("  ✓  [FRESH] Report '{}' is up to date.".format(report["file"]))

    return {
        "stale":        is_stale,
        "newer_count":  len(newer_nodes),
        "newer_nodes":  newer_nodes,
        "report_date":  report["date"],
        "report_file":  report["file"],
    }


def scan_all_staleness(stale_only=False):
    """--check mode: scan tất cả tags có report, in staleness status."""
    print("\n[auto_synthesis] Staleness Scan — all wisdom reports")
    print("=" * 55)
    reports = get_existing_reports()
    tag_mtimes = get_tag_node_mtimes()

    if not reports:
        print("  No wisdom reports found in {}.".format(OUTPUT_DIR))
        return

    stale_tags = []
    for tag, report in sorted(reports.items()):
        node_mtimes = tag_mtimes.get(tag, [])
        newer = [m for m in node_mtimes if m > report["mtime"]]
        total = len(node_mtimes)
        is_stale = len(newer) > 0

        if stale_only and not is_stale:
            continue

        status = "⚠️  STALE  ({:2d} new)".format(len(newer)) if is_stale else "✓  FRESH "
        print("  [{}] {:30s} | {:3d} nodes | {}".format(
            status, tag, total, report["date"]))
        if is_stale:
            stale_tags.append(tag)

    print("=" * 55)
    if stale_tags:
        print("\n  Re-run commands:")
        for tag in stale_tags:
            print("    python auto_synthesis.py \"{}\" --no-llm".format(tag))
    else:
        print("\n  All reports are up to date.")




# ── 0. CONTEXT: READ hot.md + memory.md ──────────────────────────────────────

def read_session_context():
    """Đọc hot.md và memory.md, trả về dict context để inject vào LLM prompt."""
    ctx = {
        "current_focus": "",
        "god_nodes": [],
        "user_preferences": "",
        "active_debt": "",
    }

    # Đọc hot.md
    if HOT_MD.exists():
        hot = HOT_MD.read_text(encoding="utf-8", errors="ignore")
        # God Nodes Cache
        m = re.search(r'## 0\. Graph God Nodes Cache.*?\n(.*?)(?=\n## |\Z)', hot, re.DOTALL)
        if m:
            ctx["god_nodes"] = re.findall(r'`([^`]+)`', m.group(1))
        # Current session context (section 1)
        m = re.search(r'## 1\. Current Session Context.*?\n(.*?)(?=\n## |\Z)', hot, re.DOTALL)
        if m:
            ctx["current_focus"] = m.group(1).strip()[:600]

    # Đọc memory.md
    if MEMORY_MD.exists():
        mem = MEMORY_MD.read_text(encoding="utf-8", errors="ignore")
        # User Preferences
        m = re.search(r'## 1\. User Preferences\n(.*?)(?=\n## |\Z)', mem, re.DOTALL)
        if m:
            ctx["user_preferences"] = m.group(1).strip()[:400]
        # Active Debt
        m = re.search(r'## 4\. Active Debt\n(.*?)(?=\n---|\Z)', mem, re.DOTALL)
        if m:
            ctx["active_debt"] = m.group(1).strip()[:300]

    return ctx


# ── 1. COLLECT ────────────────────────────────────────────────────────────────

def extract_snippet(text, max_chars=800):
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            text = text[end + 3:].strip()
    lines, chars = [], 0
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("---"):
            continue
        lines.append(s)
        chars += len(s)
        if chars >= max_chars:
            break
    snippet = " ".join(lines)
    return snippet[:max_chars] + ("..." if len(snippet) > max_chars else "")


def collect_nodes(target_tag):
    nodes = {}
    for fp in WIKI_ROOT.rglob("*.md"):
        try:
            content = fp.read_text(encoding="utf-8", errors="ignore")
            if not content.startswith("---"):
                continue
            end = content.find("---", 3)
            if end == -1:
                continue
            try:
                fm = yaml.safe_load(content[3:end]) or {}
            except Exception:
                fm = {}
            tags = fm.get("tags", [])
            if isinstance(tags, str):
                tags = [tags]
            tags = [str(t).lower() for t in tags if t]
            if target_tag not in tags:
                continue

            # Skip synthesis nodes to avoid recursive recursion and repetition
            if fm.get("type") == "synthesis":
                continue

            raw_links = re.findall(r'\[\[([^\]|#]+)', content)
            clean_links = [
                l.strip() for l in raw_links
                if not RAW_FILTER.search(l) and len(l.strip()) > 3
            ]
            thesis = str(fm.get("thesis", "")).strip()
            nodes[fp.stem] = {
                "id":           fp.stem,
                "title":        fm.get("title", fp.stem),
                "thesis":       thesis,
                "has_thesis":   len(thesis) > 10,
                "tags":         tags,
                "confidence":   fm.get("confidence", 0),
                "links":        clean_links,
                "snippet":      extract_snippet(content),
                "path":         str(fp.relative_to(WIKI_ROOT.parent)),
            }
        except Exception:
            pass
    return nodes


# ── 2. SUBGRAPH ───────────────────────────────────────────────────────────────

def build_subgraph(nodes):
    node_ids = set(nodes.keys())
    edges = defaultdict(list)
    for nid, data in nodes.items():
        for link in data["links"]:
            if link in node_ids and link != nid:
                edges[nid].append(link)
    return dict(edges)


# ── 3. HUBS ───────────────────────────────────────────────────────────────────

def rank_hubs(nodes, edges, top_n=8):
    in_deg  = Counter()
    out_deg = Counter()
    for src, targets in edges.items():
        out_deg[src] += len(targets)
        for tgt in targets:
            in_deg[tgt] += 1
    scores = {nid: in_deg.get(nid, 0) * 2 + out_deg.get(nid, 0) for nid in nodes}
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    return [(s, nid) for nid, s in ranked if s > 0][:top_n]


# ── 4. COLLISION DETECTION ────────────────────────────────────────────────────

def find_collisions(edges):
    seen, pairs = set(), []
    for a, a_links in edges.items():
        for b in a_links:
            if b in edges and a in edges[b]:
                key = tuple(sorted([a, b]))
                if key not in seen:
                    seen.add(key)
                    pairs.append((a, b))
    return pairs


# ── 5. CLUSTERS ───────────────────────────────────────────────────────────────

def find_clusters(nodes, edges, hubs):
    hub_ids = {nid for _, nid in hubs}
    clusters = defaultdict(list)
    for nid, data in nodes.items():
        if nid in hub_ids:
            continue
        hub_hits = Counter(l for l in data["links"] if l in hub_ids)
        if hub_hits:
            best_hub = hub_hits.most_common(1)[0][0]
            clusters[best_hub].append(nid)
    return dict(clusters)


# ── 6. LLM SYNTHESIS ─────────────────────────────────────────────────────────

PROMPT_TMPL = """You are a Quant Macro Analyst operating inside the Wiki Link knowledge system.

## SESSION CONTEXT (from hot.md)
Current Focus:
{current_focus}

God Nodes (graph-wide hubs, always relevant):
{god_nodes_block}

## USER PREFERENCES (from memory.md)
{user_preferences}

## ANALYSIS TARGET — Tag: "{tag}"

HUB NODES (most central in this tag's subgraph):
{hubs_block}

TENSION PAIRS (bidirectional links — possible conflict or complementarity):
{collisions_block}

## TASK — Write a WISDOM SYNTHESIS (4-6 paragraphs, dense prose, no bullet points):
1. Core tension or organizing question connecting the hub nodes. How do they relate to the God Nodes above?
2. For each major tension pair: under what CONDITIONS does mechanism A dominate B? Causal chain A -> B -> C.
3. Failure condition: when does the entire cluster break down simultaneously?
4. One open question the wiki has not yet answered — frame as a potential new node to create.

Rules: technical prose, causal language (->), cite nodes as [[Node_Name]], no platitudes.
Match the dominant language of the thesis content (Vietnamese or English)."""


def run_llm_synthesis(tag, hubs, collisions, nodes, model, ctx):
    hubs_block = "\n".join(
        "- [[{}]] (score={}): {}".format(nid, s, nodes[nid]["thesis"][:200])
        for s, nid in hubs
    )
    collision_lines = []
    for a, b in collisions[:10]:
        ta = nodes[a]["thesis"][:120] if a in nodes else ""
        tb = nodes[b]["thesis"][:120] if b in nodes else ""
        collision_lines.append("- [[{}]] <-> [[{}]]\n  A: {}\n  B: {}".format(a, b, ta, tb))
    collisions_block = "\n".join(collision_lines) if collision_lines else "(none)"

    god_nodes_block = "\n".join("- {}".format(n) for n in ctx.get("god_nodes", []))

    prompt = PROMPT_TMPL.format(
        tag=tag,
        current_focus=ctx.get("current_focus", "(not available)"),
        god_nodes_block=god_nodes_block or "(none cached)",
        user_preferences=ctx.get("user_preferences", "(not available)"),
        hubs_block=hubs_block,
        collisions_block=collisions_block,
    )

    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", model],
            capture_output=True, text=True, timeout=120, encoding="utf-8"
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        return "[LLM call failed: {}]".format(result.stderr[:300])
    except FileNotFoundError:
        return "[claude CLI not found — run with --no-llm to skip]"
    except subprocess.TimeoutExpired:
        return "[LLM timed out after 120s]"
    except Exception as e:
        return "[LLM error: {}]".format(e)


# ── 7. REPORT ─────────────────────────────────────────────────────────────────

def generate_report(tag, nodes, hubs, collisions, clusters, wisdom_text, ctx):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    L = []

    L.append("# Wisdom Synthesis: {}".format(tag.upper()))
    L.append("**Generated:** {}  |  **Nodes:** {}  |  **Hubs:** {}  |  **Tensions:** {}".format(
        now, len(nodes), len(hubs), len(collisions)))
    L.append("")

    # Session context snapshot
    L.append("## 0. Session Context Snapshot\n")
    L.append("> God Nodes active: {}\n".format(", ".join(ctx.get("god_nodes", [])) or "none"))

    L.append("## I. Cross-Node Synthesis (Wisdom Layer)\n")
    L.append(wisdom_text)
    L.append("")

    L.append("## II. Hub Map (God Nodes of this tag)\n")
    L.append("| Rank | Node | Score | Thesis |")
    L.append("|------|------|-------|--------|")
    for i, (score, nid) in enumerate(hubs, 1):
        thesis = nodes[nid]["thesis"][:120].replace("|", "|")
        L.append("| {} | [[{}]] | {} | {} |".format(i, nid, score, thesis))
    L.append("")

    L.append("## III. Tension Pairs\n")
    if collisions:
        for a, b in collisions:
            ta = nodes[a]["thesis"][:100] if a in nodes else "?"
            tb = nodes[b]["thesis"][:100] if b in nodes else "?"
            L.append("**[[{}]] <-> [[{}]]**".format(a, b))
            L.append("> A: {}".format(ta))
            L.append("> B: {}".format(tb))
            L.append("")
    else:
        L.append("_No bidirectional pairs detected._\n")

    L.append("## IV. Cluster Map\n")
    for hub_id, members in sorted(clusters.items(), key=lambda x: -len(x[1])):
        L.append("### Cluster: [[{}]] ({} satellites)".format(hub_id, len(members)))
        for m in sorted(members):
            thesis = nodes[m]["thesis"][:80] if m in nodes else ""
            L.append("- [[{}]] — {}".format(m, thesis))
        L.append("")

    L.append("## V. Node Index\n")
    sorted_nodes = sorted(
        nodes.values(),
        key=lambda x: (-(x["confidence"] if isinstance(x["confidence"], int) else 0), x["title"])
    )
    for node in sorted_nodes:
        missing = " ⚠️ NO THESIS" if not node["has_thesis"] else ""
        L.append("### [[{}]] | {}{}".format(node["id"], node["title"], missing))
        L.append("- **Confidence:** {}  |  **Path:** `{}`".format(node["confidence"], node["path"]))
        L.append("> {}\n".format(node["thesis"] if node["thesis"] else "_thesis missing_"))

    return "\n".join(L)


# ── 8. WRITEBACK ─────────────────────────────────────────────────────────────

def writeback_hot(tag, nodes, hubs, collisions, out_file):
    """WRITE END: cập nhật hot.md theo W4 protocol."""
    if not HOT_MD.exists():
        print("  [writeback] hot.md not found, skipping.")
        return

    hot = HOT_MD.read_text(encoding="utf-8", errors="ignore")
    date_str = datetime.now().strftime("%Y-%m-%d")
    top_hub_names = [nid for _, nid in hubs[:3]]

    # Inject vào ## 1. Current Session Context
    entry = (
        "- **Wisdom Run [{date}]:** tag=`{tag}` → "
        "{n_nodes} nodes, {n_tension} tensions, top hubs: {hubs}"
    ).format(
        date=date_str,
        tag=tag,
        n_nodes=len(nodes),
        n_tension=len(collisions),
        hubs=", ".join(top_hub_names),
    )

    # Thêm entry vào cuối section 1
    if "## 1. Current Session Context" in hot:
        hot = hot.replace(
            "\n## 2. Active Focus Nodes",
            "\n- {}\n## 2. Active Focus Nodes".format(entry)
        )

    # Thêm report vào ## 2. Active Focus Nodes (nếu chưa có)
    report_entry = "- `{}` — Wisdom report: {}".format(out_file, tag)
    if str(out_file) not in hot:
        hot = hot.replace(
            "\n## 3. Key Transmission Chains",
            "\n{}\n## 3. Key Transmission Chains".format(report_entry)
        )

    HOT_MD.write_text(hot, encoding="utf-8")
    print("  [writeback] hot.md updated.")


def writeback_memory_debt(nodes, tag):
    """W4 Commit: nodes thiếu thesis → ghi vào memory.md § Active Debt."""
    missing = [nid for nid, d in nodes.items() if not d["has_thesis"]]
    if not missing or not MEMORY_MD.exists():
        return

    mem = MEMORY_MD.read_text(encoding="utf-8", errors="ignore")
    date_str = datetime.now().strftime("%Y-%m-%d")

    new_items = []
    for nid in missing:
        debt_line = "- [ ] Fix missing thesis: `{}` (tag: {}, detected {})".format(
            nid, tag, date_str)
        # Chỉ thêm nếu chưa có trong file
        if nid not in mem:
            new_items.append(debt_line)

    if not new_items:
        return

    # Append vào cuối § Active Debt, trước dòng ---
    insert_block = "\n".join(new_items)
    if "## 4. Active Debt" in mem:
        mem = re.sub(
            r'(## 4\. Active Debt\n.*?)(\n---|\Z)',
            lambda m: m.group(1) + "\n" + insert_block + m.group(2),
            mem, flags=re.DOTALL
        )
        MEMORY_MD.write_text(mem, encoding="utf-8")
        print("  [writeback] memory.md: {} missing-thesis items added to Active Debt.".format(len(new_items)))


# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Wisdom-Layer Synthesis Engine v2.2")
    parser.add_argument("tag",           nargs="?", default=None, help="Tag to synthesize (e.g. 'monetary-policy')")
    parser.add_argument("--top-hubs",    type=int, default=8,  help="Hub nodes to rank (default: 8)")
    parser.add_argument("--no-llm",      action="store_true",  help="Skip LLM synthesis")
    parser.add_argument("--no-writeback",action="store_true",  help="Skip hot.md + memory.md writeback")
    parser.add_argument("--model",       default="claude-sonnet-4-6", help="Claude model")
    parser.add_argument("--check",       action="store_true",  help="Scan staleness of all wisdom reports")
    parser.add_argument("--stale-only",  action="store_true",  help="With --check: only show stale tags")
    args = parser.parse_args()

    if not WIKI_ROOT.exists():
        print("Error: 03_wiki not found. Run from wiki root.")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # --check mode: scan all reports, no synthesis
    if args.check:
        scan_all_staleness(stale_only=args.stale_only)
        sys.exit(0)

    if not args.tag:
        parser.print_help()
        sys.exit(1)

    tag = args.tag.lower()

    print("\n[auto_synthesis v2.2] Tag: '{}'".format(tag))

    # STALENESS CHECK
    # (chạy sơ bộ trước khi collect để cảnh báo nếu report cũ)
    # nodes chưa có ở đây, dùng file-level check thay thế
    _ = check_staleness(tag, {}, verbose=True)

    # READ START
    print("  [0/6] Reading session context (hot.md + memory.md)...")
    ctx = read_session_context()
    print("        -> God nodes: {}".format(ctx["god_nodes"][:3]))
    print("        -> Preferences loaded: {}".format(bool(ctx["user_preferences"])))

    print("  [1/6] Collecting nodes...")
    nodes = collect_nodes(tag)
    if not nodes:
        print("  No nodes found with tag '{}'.".format(tag))
        sys.exit(0)
    missing_thesis = [nid for nid, d in nodes.items() if not d["has_thesis"]]
    print("        -> {} nodes ({} missing thesis)".format(len(nodes), len(missing_thesis)))

    print("  [2/6] Building subgraph...")
    edges = build_subgraph(nodes)
    total_edges = sum(len(v) for v in edges.values())
    print("        -> {} nodes with links, {} internal edges".format(len(edges), total_edges))

    print("  [3/6] Ranking hubs...")
    hubs = rank_hubs(nodes, edges, top_n=args.top_hubs)
    print("        -> Top hubs: {}".format([nid for _, nid in hubs[:4]]))

    print("  [4/6] Detecting tension pairs...")
    collisions = find_collisions(edges)
    print("        -> {} bidirectional pairs".format(len(collisions)))

    clusters = find_clusters(nodes, edges, hubs)

    if args.no_llm:
        wisdom_text = "_[LLM synthesis skipped — run without --no-llm to enable]_"
        print("  [5/6] LLM synthesis skipped.")
    else:
        print("  [5/6] Running LLM synthesis (model: {})...".format(args.model))
        wisdom_text = run_llm_synthesis(tag, hubs, collisions, nodes, args.model, ctx)
        ok = not wisdom_text.startswith("[")
        print("        -> {}".format("OK" if ok else "FAILED"))

    report = generate_report(tag, nodes, hubs, collisions, clusters, wisdom_text, ctx)
    date_str = datetime.now().strftime("%Y-%m-%d")
    out_file = OUTPUT_DIR / "{}_{}_wisdom.md".format(date_str, tag.replace("-", "_"))
    out_file.write_text(report, encoding="utf-8")

    # WRITE END
    print("  [6/6] Writeback...")
    if args.no_writeback:
        print("        -> skipped (--no-writeback)")
    else:
        writeback_hot(tag, nodes, hubs, collisions, out_file)
        writeback_memory_debt(nodes, tag)

    # Archive synthesis node vào 03_wiki/syntheses/
    if not args.no_writeback:
        syn_node = archive_synthesis_node(tag, nodes, hubs, collisions, out_file, date_str)
        print("        -> Synthesis node: {}".format(syn_node.name))

    print("\n  Report saved: {}".format(out_file))
    print("  Nodes: {}  |  Hubs: {}  |  Tensions: {}  |  Clusters: {}  |  Missing thesis: {}".format(
        len(nodes), len(hubs), len(collisions), len(clusters), len(missing_thesis)))




def archive_synthesis_node(tag, nodes, hubs, collisions, out_file, date_str):
    """
    Tạo wiki node tóm tắt trong 03_wiki/syntheses/<date>_<tag>_synthesis.md
    Để wisdom report vào graph, searchable, và compounding.
    """
    syntheses_dir = WIKI_ROOT / "syntheses"
    syntheses_dir.mkdir(parents=True, exist_ok=True)

    node_id   = "{}_{}_{}_synthesis".format(date_str.replace("-",""), tag.replace("-","_"), "wisdom")
    node_file = syntheses_dir / "{}_{}_synthesis.md".format(date_str, tag.replace("-","_"))

    top_hubs = [nid for _, nid in hubs[:5]] if hubs else []
    top_tensions = [
        "[[{}]] ↔ [[{}]]".format(a, b)
        for a, b in collisions[:3]
    ] if collisions else []
    tag_list = [tag, "synthesis", "wisdom-layer"]

    fm = """---
title: "Wisdom Synthesis: {tag} ({date})"
type: synthesis
tags: {tags}
status: verified
confidence: 4
half_life_years: 0.5
thesis: "Wisdom synthesis of {n} nodes tagged [{tag}]: top hubs {hubs_str}, {nt} tension pairs identified."
source_refs:
  - file: "{report_file}"
    page: "full"
created: {date}
updated: {date}
---
""".format(
        tag=tag, date=date_str,
        tags=str(tag_list),
        n=len(nodes),
        hubs_str=", ".join(top_hubs[:3]) if top_hubs else "none",
        nt=len(collisions),
        report_file=out_file.name,
    )

    hub_links  = "\n".join("- [[{}]]".format(h) for h in top_hubs)
    tens_links = "\n".join("- {}".format(t) for t in top_tensions)

    body = """## Thesis
Wisdom synthesis of {n} nodes tagged `{tag}` as of {date}.

## Top Hubs
{hubs}

## Key Tensions
{tensions}

## Related
- [Full report]({report})
""".format(
        n=len(nodes), tag=tag, date=date_str,
        hubs=hub_links or "_(none)_",
        tensions=tens_links or "_(none)_",
        report=str(out_file),
    )

    node_file.write_text(fm + body, encoding="utf-8")
    return node_file

if __name__ == "__main__":
    main()
