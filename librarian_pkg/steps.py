import re

import yaml

from .shared import STAGED_DIR, WIKI_DIR, run_script


def _last_line(stdout, stderr, fallback=""):
    if stdout and stdout.strip():
        return stdout.strip().splitlines()[-1]
    if stderr:
        return stderr[:80]
    return fallback


def step_build_graph():
    ok_, out, err = run_script("_build_wiki_graph.py")
    return ok_, _last_line(out, err)


def step_gen_index():
    ok_, out, err = run_script("gen_index.py")
    return ok_, _last_line(out, err)


def step_staleness(tag=None):
    args = ["--check"] + (["--stale-only"] if not tag else [tag, "--no-llm", "--no-writeback"])
    ok_, out, err = run_script("auto_synthesis.py", args)
    out = out or ""
    stale = out.count("STALE")
    fresh = out.count("FRESH")
    if tag:
        return True, "checked tag '{}'".format(tag)
    return True, "{} fresh, {} stale".format(fresh, stale)


def step_auto_bridge(dry_run=False):
    args = ["--dry-run"] if dry_run else ["--force", "--backup"]
    ok_, out, err = run_script("auto_bridge.py", args)
    lines = [line for line in out.splitlines() if "orphan" in line.lower() or "bridge" in line.lower() or "Found" in line]
    msg = lines[0][:80] if lines else _last_line(out, err)
    return True, msg


def step_find_orphans():
    ok_, out, err = run_script("find_orphans.py")
    lines = out.strip().splitlines()
    return True, lines[-1][:80] if lines else _last_line(out, err)


def step_suggest_ideas():
    ok_, out, err = run_script("suggest_ideas.py")
    if out:
        for line in out.strip().splitlines()[:20]:
            print("       {}".format(line))
    return True, ""


def step_embed_build(incremental=False):
    args = ["--incremental"] if incremental else ["--build"]
    ok_, out, err = run_script("embed_index.py", args, timeout=None)
    return ok_, _last_line(out, err)


def step_embed_stats():
    ok_, out, err = run_script("embed_index.py", ["--stats"], timeout=30)
    for line in [line for line in out.splitlines() if line.strip()]:
        print("    {}".format(line))
    return ok_, "OK" if ok_ else _last_line(out, err)


def step_missing_thesis():
    missing = []
    if WIKI_DIR.exists():
        for fp in WIKI_DIR.rglob("*.md"):
            try:
                content = fp.read_text(encoding="utf-8", errors="ignore")
                if not content.startswith("---"):
                    continue
                end = content.find("---", 3)
                if end == -1:
                    continue
                fm = yaml.safe_load(content[3:end]) or {}
                thesis = str(fm.get("thesis", "")).strip()
                if len(thesis) < 10:
                    missing.append(fp.stem)
            except Exception:
                pass
    msg = "{} nodes missing thesis".format(len(missing))
    if missing[:3]:
        msg += ": " + ", ".join(missing[:3])
        if len(missing) > 3:
            msg += "..."
    return True, msg


def step_claim_audit(file_path):
    ok_, out, err = run_script("claim_auditor.py", [str(file_path)])
    lines = out.strip().splitlines()
    return ok_, lines[-1][:80] if lines else _last_line(out, err, "done")


def step_inbox_scan():
    ok_, out, err = run_script("inbox_processor.py", ["--scan"])
    if out:
        for line in out.strip().splitlines():
            print("    {}".format(line))
    return ok_, "inbox scanned"


def step_inbox_process(target_book=None):
    if not target_book:
        return False, "target_book required (--process <book>)"
    ok_, out, err = run_script("inbox_processor.py", ["--process", target_book])
    return ok_, _last_line(out, err, "done")


def step_inbox_list_books():
    ok_, out, err = run_script("inbox_processor.py", ["--list-books"])
    if out:
        for line in out.strip().splitlines()[:20]:
            print("    {}".format(line))
    return ok_, "OK"


def step_sync_registry():
    run_script("sync_registry.py")
    return True, "Registry synced"


def count_staged():
    if not STAGED_DIR.exists():
        return 0
    return len([fp for fp in STAGED_DIR.glob("*.md") if not fp.name.startswith("_")])


def count_stale_status():
    count = 0
    if not WIKI_DIR.exists():
        return 0
    for fp in WIKI_DIR.rglob("*.md"):
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            if not text.startswith("---"):
                continue
            end = text.find("---", 3)
            if end == -1:
                continue
            fm = yaml.safe_load(text[3:end]) or {}
            if str(fm.get("status", "")).strip().lower() == "stale":
                count += 1
        except Exception:
            pass
    return count


def count_orphans():
    if not WIKI_DIR.exists():
        return 0
    link_pattern = re.compile(r"\[\[([^\]|#]+)")
    incoming = {}
    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_") or fp.name.startswith("."):
            continue
        incoming[fp.stem] = 0
    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_") or fp.name.startswith("."):
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            for match in link_pattern.finditer(text):
                target = match.group(1).strip()
                if target in incoming and target != fp.stem:
                    incoming[target] += 1
        except Exception:
            pass
    return sum(1 for value in incoming.values() if value == 0)
