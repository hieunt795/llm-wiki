#!/usr/bin/env python3
"""
librarian.py — Wiki Link Librarian (v2.0)
==========================================
Single entry point cho toàn bộ Wiki Link pipeline.

WHAT'S NEW in v2.0:
  - pipeline `batch`   : chạy nhiều pipeline liên tiếp trong một lệnh
  - pipeline `review`  : UI rõ ràng cho staged nodes (list / accept / accept-all)
  - pipeline `status`  : hiển thị staged count, stale count, orphan count
  - bug fix: `--threshold` cho deepdive giờ pass xuống script đúng
  - bug fix: `cleanup` alias tự động bật --fix-whitespace --no-move
  - `staleness` thêm --threshold override
  - `search` thêm --export để lưu kết quả ra file

DESIGN PRINCIPLES:
  - Mỗi pipeline là một chuỗi Steps có tên rõ ràng
  - --skip step1,step2  : bỏ qua các bước cụ thể
  - --only step1        : chỉ chạy bước đó
  - Mọi step đều report kết quả (OK / SKIP / FAIL)
  - Expand: thêm pipeline mới = thêm 1 dict vào PIPELINES

USAGE:
  python librarian.py sync
  python librarian.py health
  python librarian.py daily
  python librarian.py ingest
  python librarian.py stage --dry-run
  python librarian.py review
  python librarian.py review accept <node_name>
  python librarian.py extract --book perry --skip-existing
  python librarian.py scout --mode lines --n 10
  python librarian.py section --dir 02_sources/books/foo --heading "1.1" --out 04_outputs/temp/foo.md
  python librarian.py wisdom <tag> [--no-llm]
  python librarian.py audit <file>
  python librarian.py search <query> [--deep] [--export path]
  python librarian.py status
  python librarian.py sync --skip gen_index
  python librarian.py health --only staleness
  python librarian.py batch sync,health
  python librarian.py batch daily,wisdom monetary-policy
  python librarian.py staleness --threshold 1.0
  python librarian.py organize --dir 03_wiki/concepts --limit 8
  python librarian.py cleanup --dir 03_wiki/mechanisms --apply
"""

import sys
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import os
import argparse
import subprocess
import yaml
import re
import math
import random
from pathlib import Path
from datetime import datetime
from collections import Counter

# ── PATHS ─────────────────────────────────────────────────────────────────────
WIKI_ROOT   = Path(__file__).parent
SCRIPTS_DIR = WIKI_ROOT / "05_scripts"
WIKI_DIR    = WIKI_ROOT / "03_wiki"
OUTPUT_DIR  = WIKI_ROOT / "04_outputs" / "research"
STAGED_DIR  = WIKI_ROOT / "04_outputs" / "staged_nodes"
HOT_MD      = WIKI_ROOT / "01_schema" / "hot.md"
MEMORY_MD   = WIKI_ROOT / "01_schema" / "memory.md"

# ── ANSI COLORS ───────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"

def ok(msg):    print("  {}[OK]{} {}".format(GREEN, RESET, msg))
def skip(msg):  print("  {}[SKIP]{} {}".format(YELLOW, RESET, msg))
def fail(msg):  print("  {}[FAIL]{} {}".format(RED, RESET, msg))
def info(msg):  print("  {}[INFO]{} {}".format(CYAN, RESET, msg))
def header(msg): print("\n{}{}{}".format(BOLD, msg, RESET))


# ── STEP RUNNER ───────────────────────────────────────────────────────────────

def run_script(script_name, args=None, timeout=120):
    """Chạy một script trong SCRIPTS_DIR. Trả về (success, stdout, stderr)."""
    script_path = SCRIPTS_DIR / script_name
    if not script_path.exists():
        return False, "", "Script not found: {}".format(script_path)
    cmd = [sys.executable, str(script_path)] + (args or [])
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=timeout, encoding="utf-8", errors="replace",
                           cwd=str(WIKI_ROOT))
        return r.returncode == 0, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Timeout after {}s".format(timeout)
    except Exception as e:
        return False, "", str(e)


class StepRunner:
    """
    Chạy một pipeline gồm nhiều steps.
    skip_set: set of step names to skip
    only_set: nếu non-empty, chỉ chạy steps trong set này
    """
    def __init__(self, skip_set=None, only_set=None):
        self.skip_set = skip_set or set()
        self.only_set = only_set or set()
        self.results = []  # [(step_name, status, msg)]

    def should_run(self, name):
        if name in self.skip_set:
            return False
        if self.only_set and name not in self.only_set:
            return False
        return True

    def step(self, name, fn):
        """Chạy một step. fn() trả về (success: bool, message: str)."""
        if not self.should_run(name):
            skip(name)
            self.results.append((name, "SKIP", ""))
            return True  # skip = không fail pipeline

        print("  [ .. ] {}".format(name), end="\r")
        try:
            success, msg = fn()
        except Exception as e:
            success, msg = False, str(e)

        if success:
            ok("{:<35} {}".format(name, msg))
            self.results.append((name, "OK", msg))
        else:
            fail("{:<35} {}".format(name, msg))
            self.results.append((name, "FAIL", msg))
        return success

    def summary(self):
        total  = len(self.results)
        n_ok   = sum(1 for _, s, _ in self.results if s == "OK")
        n_skip = sum(1 for _, s, _ in self.results if s == "SKIP")
        n_fail = sum(1 for _, s, _ in self.results if s == "FAIL")
        print("\n  ─── Summary: {}/{} OK | {} skipped | {} failed ───".format(
            n_ok, total - n_skip, n_skip, n_fail))


# ── STEP IMPLEMENTATIONS ──────────────────────────────────────────────────────

def step_build_graph():
    ok_, out, err = run_script("_build_wiki_graph.py")
    msg = out.strip().splitlines()[-1] if out.strip() else (err[:80] if err else "")
    return ok_, msg

def step_gen_index():
    ok_, out, err = run_script("gen_index.py")
    msg = out.strip().splitlines()[-1] if out.strip() else (err[:80] if err else "")
    return ok_, msg

def step_staleness(tag=None):
    args = ["--check"] + (["--stale-only"] if not tag else [tag, "--no-llm", "--no-writeback"])
    ok_, out, err = run_script("auto_synthesis.py", args)
    out = out or ""
    stale = out.count("STALE")
    fresh = out.count("FRESH")
    if tag:
        msg = "checked tag '{}'".format(tag)
    else:
        msg = "{} fresh, {} stale".format(fresh, stale)
    return True, msg

def step_auto_bridge(dry_run=False):
    args = ["--dry-run"] if dry_run else ["--force", "--backup"]
    ok_, out, err = run_script("auto_bridge.py", args)
    lines = [l for l in out.splitlines() if "orphan" in l.lower() or "bridge" in l.lower() or "Found" in l]
    msg = lines[0][:80] if lines else (out.strip().splitlines()[-1][:80] if out.strip() else "")
    return True, msg

def step_find_orphans():
    ok_, out, err = run_script("find_orphans.py")
    lines = out.strip().splitlines()
    msg = lines[-1][:80] if lines else ""
    return True, msg

def step_suggest_ideas():
    ok_, out, err = run_script("suggest_ideas.py")
    if out:
        for line in out.strip().splitlines()[:20]:
            print("       {}".format(line))
    return True, ""

def step_embed_build(incremental=False):
    """Rebuild FAISS embedding index."""
    args = ["--incremental"] if incremental else ["--build"]
    ok_, out, err = run_script("embed_index.py", args, timeout=None)
    msg = out.strip().splitlines()[-1] if out.strip() else (err[:80] if err else "")
    return ok_, msg

def step_embed_stats():
    """Print embedding index statistics."""
    ok_, out, err = run_script("embed_index.py", ["--stats"], timeout=30)
    lines = [l for l in out.splitlines() if l.strip()]
    if lines:
        for line in lines:
            print("    {}".format(line))
    return ok_, "OK" if ok_ else (err[:80] if err else "")

def step_missing_thesis():
    """Scan wiki nodes thiếu thesis field."""
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


def step_embed_build(incremental=False):
    """Rebuild FAISS embedding index."""
    args = ["--incremental"] if incremental else ["--build"]
    ok_, out, err = run_script("embed_index.py", args, timeout=None)
    msg = out.strip().splitlines()[-1] if out.strip() else (err[:80] if err else "")
    return ok_, msg

def step_embed_stats():
    """Print embedding index statistics."""
    ok_, out, err = run_script("embed_index.py", ["--stats"], timeout=30)
    lines = [l for l in out.splitlines() if l.strip()]
    if lines:
        for line in lines:
            print("    {}".format(line))
    return ok_, "OK" if ok_ else (err[:80] if err else "")

def step_claim_audit(file_path):
    ok_, out, err = run_script("claim_auditor.py", [str(file_path)])
    lines = out.strip().splitlines()
    msg = lines[-1][:80] if lines else (err[:80] if err else "done")
    return ok_, msg


def step_inbox_scan():
    """Scan inbox folder and report file counts + auto-classify suggestions."""
    ok_, out, err = run_script("inbox_processor.py", ["--scan"])
    if out:
        for line in out.strip().splitlines():
            print("    {}".format(line))
    return ok_, "inbox scanned"

def step_inbox_process(target_book=None):
    """Process inbox files: extract, move to specified book folder."""
    if not target_book:
        return False, "target_book required (--process <book>)"
    args = ["--process", target_book]
    ok_, out, err = run_script("inbox_processor.py", args)
    msg = out.strip().splitlines()[-1] if out.strip() else (err[:80] if err else "done")
    return ok_, msg

def step_inbox_list_books():
    """List known book folders for classification."""
    ok_, out, err = run_script("inbox_processor.py", ["--list-books"])
    if out:
        for line in out.strip().splitlines()[:20]:
            print("    {}".format(line))
    return ok_, "OK"

# ── HELPER: quick wiki stats ───────────────────────────────────────────────────

def _count_staged() -> int:
    if not STAGED_DIR.exists():
        return 0
    return len([f for f in STAGED_DIR.glob("*.md") if not f.name.startswith("_")])

def _count_stale_status() -> int:
    """Nodes với status: stale trong frontmatter."""
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

def _count_orphans() -> int:
    """Nhanh: đếm nodes không có incoming wikilink."""
    if not WIKI_DIR.exists():
        return 0
    link_pattern = re.compile(r"\[\[([^\]|#]+)")
    nodes = {}
    incoming = {}
    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_") or fp.name.startswith("."):
            continue
        nodes[fp.stem] = fp
        incoming[fp.stem] = 0
    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_") or fp.name.startswith("."):
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            for m in link_pattern.finditer(text):
                target = m.group(1).strip()
                if target in incoming and target != fp.stem:
                    incoming[target] += 1
        except Exception:
            pass
    return sum(1 for c in incoming.values() if c == 0)


# ── VALIDATE & LOGGING HELPERS ────────────────────────────────────────────────

def validate_frontmatter_vs_schema() -> tuple:
    """
    Check mỗi wiki node's frontmatter vs registry_<type>.md schema.
    Trả về (ok: bool, issues: list of str).
    """
    issues = []
    schema_dir = WIKI_ROOT / "01_schema" / "registry"

    if not schema_dir.exists():
        return True, []  # skip nếu không có registry

    # Load schema definitions từ registry/*.md
    type_schemas = {}
    for schema_file in schema_dir.glob("registry_*.md"):
        type_name = schema_file.stem.replace("registry_", "")
        try:
            content = schema_file.read_text(encoding="utf-8", errors="ignore")
            # Rất đơn giản: tìm frontmatter requirements từ schema file
            # Chi tiết hơn sẽ cần YAML parser, nhưng đây là sketch
            type_schemas[type_name] = content
        except Exception:
            pass

    # Check wiki nodes
    if not WIKI_DIR.exists():
        return True, []

    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_"):
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            if not text.startswith("---"):
                issues.append("{}  — missing frontmatter".format(fp.relative_to(WIKI_ROOT)))
                continue
            end = text.find("---", 3)
            if end == -1:
                issues.append("{}  — malformed frontmatter".format(fp.relative_to(WIKI_ROOT)))
                continue
            fm = yaml.safe_load(text[3:end]) or {}

            # Check required fields (simplistic)
            node_type = fm.get("type", "unknown")
            if not fm.get("title"):
                issues.append("{}  — missing title".format(fp.relative_to(WIKI_ROOT)))
            if not fm.get("thesis") and len(text) > 1000:
                issues.append("{}  — long node missing thesis".format(fp.relative_to(WIKI_ROOT)))
        except Exception as e:
            issues.append("{}  — error: {}".format(fp.relative_to(WIKI_ROOT), str(e)[:40]))

    return len(issues) == 0, issues


def validate_broken_wikilinks() -> tuple:
    """
    Scan toàn bộ wiki nodes cho [[link]] references.
    Kiểm tra nếu target node tồn tại.
    Trả về (ok: bool, broken_links: list of str).
    """
    broken = []
    if not WIKI_DIR.exists():
        return True, []

    # Build set of valid node names
    valid_nodes = set()
    for fp in WIKI_DIR.rglob("*.md"):
        if not fp.name.startswith("_"):
            valid_nodes.add(fp.stem)

    # Also check aliases from registry
    link_pattern = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]*)?(?:#[^\]]*)?\]\]")

    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_"):
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            for m in link_pattern.finditer(text):
                target = m.group(1).strip()
                # Remove book prefix nếu format "book/node"
                if "/" in target:
                    target = target.split("/", 1)[1]
                if target not in valid_nodes:
                    broken.append("{}  →  [[{}]] (not found)".format(
                        fp.relative_to(WIKI_ROOT), target))
        except Exception:
            pass

    return len(broken) == 0, broken


def validate_orphan_refs() -> tuple:
    """
    Check source_ref fields trong wiki nodes.
    Ensure referenced files tồn tại.
    """
    orphans = []
    if not WIKI_DIR.exists():
        return True, []

    sources_dir = WIKI_ROOT / "02_sources"

    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_"):
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            if not text.startswith("---"):
                continue
            end = text.find("---", 3)
            if end == -1:
                continue
            fm = yaml.safe_load(text[3:end]) or {}

            source_refs = fm.get("source_ref", [])
            if isinstance(source_refs, str):
                source_refs = [source_refs]

            for ref in source_refs:
                if not ref:
                    continue
                # Format: "book_name/chapter.md" hoặc "book/chap/sec.md"
                ref_path = sources_dir / ref
                if not ref_path.exists():
                    orphans.append("{}  →  source_ref '{}' not found".format(
                        fp.relative_to(WIKI_ROOT), ref))
        except Exception:
            pass

    return len(orphans) == 0, orphans


def append_log_entry(pipeline_name: str, status: str, summary: str = "") -> None:
    """
    Append một row vào log.md markdown table.
    Format: | timestamp | pipeline | status | summary |
    """
    log_path = WIKI_ROOT / "01_schema" / "log.md"

    # Ensure log.md exists với header
    if not log_path.exists():
        header_text = """# Librarian Execution Log

| Timestamp | Pipeline | Status | Summary |
|-----------|----------|--------|---------|
"""
        log_path.write_text(header_text, encoding="utf-8")

    # Read current log
    log_content = log_path.read_text(encoding="utf-8")

    # Append new entry
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Escape pipes in summary
    summary = summary.replace("|", "\\|")[:80]
    new_row = "| {} | {} | {} | {} |".format(timestamp, pipeline_name, status, summary)

    log_content += "\n" + new_row
    log_path.write_text(log_content, encoding="utf-8")


def process_writeback_queue() -> tuple:
    """
    Read 01_schema/writeback_queue.md, parse entries, apply updates.
    Format: each entry is a YAML block with node_name + frontmatter fields to update.
    After applying, clear the queue.
    """
    queue_path = WIKI_ROOT / "01_schema" / "writeback_queue.md"
    if not queue_path.exists():
        return True, 0

    queue_text = queue_path.read_text(encoding="utf-8")
    entries = []

    # Very simple parser: split by "---" blocks
    blocks = queue_text.split("---")
    applied = 0

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.splitlines()
        if not lines:
            continue

        # First line should be node_name
        node_name = lines[0].strip()
        if not node_name or node_name.startswith("#"):
            continue

        # Rest are YAML key: value pairs
        updates = {}
        for line in lines[1:]:
            if ":" in line and not line.startswith(" "):
                k, _, v = line.partition(":")
                updates[k.strip()] = v.strip().strip('"')

        if not updates:
            continue

        # Find and update node
        node_path = None
        if WIKI_DIR.exists():
            for fp in WIKI_DIR.rglob("{}.md".format(node_name)):
                if not fp.name.startswith("_"):
                    node_path = fp
                    break

        if not node_path:
            continue

        # Update frontmatter
        try:
            content = node_path.read_text(encoding="utf-8", errors="ignore")
            if content.startswith("---"):
                end = content.find("---", 3)
                if end != -1:
                    fm_text = content[3:end]
                    fm = yaml.safe_load(fm_text) or {}

                    # Apply updates
                    for k, v in updates.items():
                        fm[k] = v

                    # Rebuild frontmatter
                    new_fm = "---\n"
                    for k, v in fm.items():
                        if isinstance(v, list):
                            new_fm += "{}:\n".format(k)
                            for item in v:
                                new_fm += "  - {}\n".format(item)
                        else:
                            new_fm += "{}: {}\n".format(k, v)
                    new_fm += "---\n"

                    # Write back
                    new_content = new_fm + content[end+4:]
                    node_path.write_text(new_content, encoding="utf-8")
                    applied += 1
        except Exception:
            pass

    # Clear queue
    queue_path.write_text("# Writeback Queue\n\nProcessed at {}.\n".format(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")), encoding="utf-8")

    return True, applied



# ── VALIDATE & LOGGING HELPERS ────────────────────────────────────────────────

def validate_frontmatter_vs_schema():
    """Check each wiki node's frontmatter vs registry."""
    issues = []
    schema_dir = WIKI_ROOT / "01_schema" / "registry"
    if not schema_dir.exists():
        return True, []
    
    if not WIKI_DIR.exists():
        return True, []

    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_"):
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            if not text.startswith("---"):
                issues.append("{}  — missing frontmatter".format(fp.relative_to(WIKI_ROOT)))
                continue
            end = text.find("---", 3)
            if end == -1:
                issues.append("{}  — malformed frontmatter".format(fp.relative_to(WIKI_ROOT)))
                continue
            fm = yaml.safe_load(text[3:end]) or {}
            if not fm.get("title"):
                issues.append("{}  — missing title".format(fp.relative_to(WIKI_ROOT)))
            if not fm.get("thesis") and len(text) > 1000:
                issues.append("{}  — long node missing thesis".format(fp.relative_to(WIKI_ROOT)))
        except Exception as e:
            issues.append("{}  — error: {}".format(fp.relative_to(WIKI_ROOT), str(e)[:40]))

    return len(issues) == 0, issues


def validate_broken_wikilinks():
    """Check for broken [[wikilinks]]."""
    broken = []
    if not WIKI_DIR.exists():
        return True, []

    valid_nodes = set()
    for fp in WIKI_DIR.rglob("*.md"):
        if not fp.name.startswith("_"):
            valid_nodes.add(fp.stem)

    link_pattern = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]*)?(?:#[^\]]*)?\]\]")

    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_"):
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            for m in link_pattern.finditer(text):
                target = m.group(1).strip()
                if "/" in target:
                    target = target.split("/", 1)[1]
                if target not in valid_nodes:
                    broken.append("{}  →  [[{}]] (not found)".format(
                        fp.relative_to(WIKI_ROOT), target))
        except Exception:
            pass

    return len(broken) == 0, broken


def validate_orphan_refs():
    """Check source_ref fields exist."""
    orphans = []
    if not WIKI_DIR.exists():
        return True, []

    sources_dir = WIKI_ROOT / "02_sources"

    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_"):
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            if not text.startswith("---"):
                continue
            end = text.find("---", 3)
            if end == -1:
                continue
            fm = yaml.safe_load(text[3:end]) or {}

            source_refs = fm.get("source_ref", [])
            if isinstance(source_refs, str):
                source_refs = [source_refs]

            for ref in source_refs:
                if not ref:
                    continue
                ref_path = sources_dir / ref
                if not ref_path.exists():
                    orphans.append("{}  →  source_ref '{}' not found".format(
                        fp.relative_to(WIKI_ROOT), ref))
        except Exception:
            pass

    return len(orphans) == 0, orphans


def append_log_entry(pipeline_name, status, summary=""):
    """Append to log.md markdown table."""
    log_path = WIKI_ROOT / "01_schema" / "log.md"

    if not log_path.exists():
        header_text = """# Librarian Execution Log

| Timestamp | Pipeline | Status | Summary |
|-----------|----------|--------|---------|
"""
        log_path.write_text(header_text, encoding="utf-8")

    log_content = log_path.read_text(encoding="utf-8")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary = summary.replace("|", "\\|")[:80]
    new_row = "| {} | {} | {} | {} |".format(timestamp, pipeline_name, status, summary)

    log_content += "\n" + new_row
    log_path.write_text(log_content, encoding="utf-8")


def process_writeback_queue():
    """Process writeback_queue.md."""
    queue_path = WIKI_ROOT / "01_schema" / "writeback_queue.md"
    if not queue_path.exists():
        return True, 0

    queue_text = queue_path.read_text(encoding="utf-8")
    blocks = queue_text.split("---")
    applied = 0

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.splitlines()
        if not lines:
            continue

        node_name = lines[0].strip()
        if not node_name or node_name.startswith("#"):
            continue

        updates = {}
        for line in lines[1:]:
            if ":" in line and not line.startswith(" "):
                k, _, v = line.partition(":")
                updates[k.strip()] = v.strip().strip('"')

        if not updates:
            continue

        node_path = None
        if WIKI_DIR.exists():
            for fp in WIKI_DIR.rglob("{}.md".format(node_name)):
                if not fp.name.startswith("_"):
                    node_path = fp
                    break

        if not node_path:
            continue

        try:
            content = node_path.read_text(encoding="utf-8", errors="ignore")
            if content.startswith("---"):
                end = content.find("---", 3)
                if end != -1:
                    fm_text = content[3:end]
                    fm = yaml.safe_load(fm_text) or {}

                    for k, v in updates.items():
                        fm[k] = v

                    new_fm = "---\n"
                    for k, v in fm.items():
                        if isinstance(v, list):
                            new_fm += "{}:\n".format(k)
                            for item in v:
                                new_fm += "  - {}\n".format(item)
                        else:
                            new_fm += "{}: {}\n".format(k, v)
                    new_fm += "---\n"

                    new_content = new_fm + content[end+4:]
                    node_path.write_text(new_content, encoding="utf-8")
                    applied += 1
        except Exception:
            pass

    queue_path.write_text("# Writeback Queue\n\nProcessed at {}.\n".format(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")), encoding="utf-8")

    return True, applied


# ── PIPELINES ─────────────────────────────────────────────────────────────────

def step_sync_registry():
    ok_, out, err = run_script("sync_registry.py")
    return True, "Registry synced"

def pipeline_sync(runner):
    """Phase D: build graph → gen index → sync registry → staleness check."""
    header("PIPELINE: sync")
    runner.step("build_graph",    step_build_graph)
    runner.step("gen_index",      step_gen_index)
    runner.step("sync_registry",  step_sync_registry)
    runner.step("staleness",      step_staleness)
    runner.summary()

def pipeline_ingest(runner):
    """Post-ingest sync: build graph → gen index → auto_bridge → staleness."""
    header("PIPELINE: ingest (post-ingest sync)")
    info("Run Phase A–C manually first (exact_extractor → wiki audit → SPAWN/EXPAND)")
    runner.step("build_graph",    step_build_graph)
    runner.step("gen_index",      step_gen_index)
    runner.step("auto_bridge",    lambda: step_auto_bridge(dry_run=False))
    runner.step("staleness",      step_staleness)
    runner.summary()

def pipeline_health(runner):
    """Health check: orphans → missing thesis → staleness → bounties."""
    header("PIPELINE: health")
    runner.step("find_orphans",   step_find_orphans)
    runner.step("missing_thesis", step_missing_thesis)
    runner.step("staleness",      step_staleness)
    runner.step("suggest_ideas",  step_suggest_ideas)
    runner.summary()

def pipeline_daily(runner):
    """Daily workflow: suggest → orphans → staleness → random walk."""
    header("PIPELINE: daily")
    runner.step("suggest_ideas",  step_suggest_ideas)
    runner.step("find_orphans",   step_find_orphans)
    runner.step("staleness",      step_staleness)
    runner.step("missing_thesis", step_missing_thesis)
    runner.summary()

def pipeline_wisdom(runner, tag, no_llm=False, model="claude-sonnet-4-6"):
    """Wisdom synthesis cho một tag."""
    header("PIPELINE: wisdom [{}]".format(tag))
    runner.step("staleness_check", lambda: step_staleness(tag=None))

    def _synthesis():
        args = [tag]
        if no_llm:
            args.append("--no-llm")
        else:
            args += ["--model", model]
        ok_, out, err = run_script("auto_synthesis.py", args, timeout=180)
        out = out or ""
        lines = [l for l in out.splitlines() if "Report saved" in l or "Nodes:" in l]
        msg = lines[-1][:100] if lines else (err[:80] if err else "")
        return ok_, msg

    runner.step("auto_synthesis", _synthesis)
    runner.summary()

def pipeline_audit(runner, file_path):
    """Claim audit trên một file."""
    header("PIPELINE: audit [{}]".format(file_path))
    runner.step("claim_audit", lambda: step_claim_audit(file_path))
    runner.summary()

def pipeline_search(runner, query, deep=False, semantic=False, top=8,
                    no_raw=False, no_wiki=False, raw_only=False,
                    no_semantic=False, filter_type=None, min_confidence=0,
                    export=None):
    """Search pipeline:
      default  → wiki_search RRF(keyword+semantic)
      --no-semantic → wiki_search keyword-only
      --semantic → semantic_search only (meaning-based)
      --deep   → hybrid_search heatmap + semantic support
      --export <path> → lưu kết quả ra file
    """
    mode = "[SEMANTIC]" if semantic else "[DEEP+SEMANTIC]" if deep else ""
    header("PIPELINE: search ['{}'] {}".format(query, mode))

    def _search():
        output_lines = []
        use_raw_only = raw_only or no_wiki

        wiki_args = [query, "--top", str(top), "--show-related"]
        if no_raw:
            wiki_args.append("--no-raw")
        if use_raw_only:
            wiki_args.append("--no-wiki")
        if no_semantic:
            wiki_args.append("--no-semantic")
        if filter_type:
            wiki_args += ["--type", filter_type]
        if min_confidence:
            wiki_args += ["--min-confidence", str(min_confidence)]

        semantic_args = [query, "--top", str(top)]
        if no_raw:
            semantic_args.append("--wiki-only")
        if use_raw_only:
            semantic_args.append("--raw-only")

        hybrid_args = [query, "--top", str(top)]
        if use_raw_only:
            hybrid_args.append("--raw-only")
        if no_raw:
            hybrid_args.append("--no-raw")

        if semantic and not deep:
            ok_, out, err = run_script("semantic_search.py", semantic_args, timeout=90)
            if out:
                output_lines += out.strip().splitlines()[:50]

        elif deep:
            ok_, out, err = run_script("hybrid_search.py", hybrid_args, timeout=90)
            if out:
                output_lines += ["=== HYBRID SEARCH ==="]
                output_lines += out.strip().splitlines()[:45]

            ok2_, out2, err2 = run_script("semantic_search.py", semantic_args, timeout=90)
            if out2:
                output_lines += ["", "=== SEMANTIC SEARCH ==="]
                output_lines += out2.strip().splitlines()[:35]

        else:
            ok_, out, err = run_script("wiki_search.py", wiki_args, timeout=90)
            if out:
                output_lines += out.strip().splitlines()[:70]

        if output_lines:
            print()
            for line in output_lines:
                print("    {}".format(line))

        # ── Export ────────────────────────────────────────────────────────────
        if export and output_lines:
            export_path = Path(export)
            if not export_path.is_absolute():
                export_path = WIKI_ROOT / export_path
            export_path.parent.mkdir(parents=True, exist_ok=True)
            with open(export_path, "w", encoding="utf-8") as fh:
                fh.write("# Search: {}\n".format(query))
                fh.write("_Generated: {}_\n\n".format(
                    datetime.now().strftime("%Y-%m-%d %H:%M")))
                fh.write("\n".join(output_lines))
                fh.write("\n")
            info("Exported → {}".format(export_path))

        return True, "search complete"

    runner.step("search", _search)
    runner.summary()


def pipeline_staleness(runner, auto_mark=False, threshold_multiplier=None):
    """Auto-detect và optionally mark stale nodes dựa trên half_life_years.
    threshold_multiplier: override hệ số (default ln(2)*1.5 ≈ 1.04)
    """
    mode = " [AUTO-MARK]" if auto_mark else " [REPORT ONLY]"
    header("PIPELINE: staleness{}".format(mode))

    def _staleness():
        WIKI_DIR_P = Path("03_wiki")
        now = datetime.now().timestamp()
        stale_nodes = []
        updated_nodes = []
        _mult = threshold_multiplier if threshold_multiplier is not None else math.log(2) * 1.5

        for fp in WIKI_DIR_P.rglob("*.md"):
            if fp.name.startswith("_") or fp.name.startswith("."):
                continue
            try:
                text = fp.read_text(encoding="utf-8", errors="ignore")
                if not text.startswith("---"):
                    continue
                end = text.find("---", 3)
                if end == -1:
                    continue
                try:
                    fm = yaml.safe_load(text[3:end]) or {}
                except Exception:
                    fm = {}
                hl = fm.get("half_life_years")
                status = fm.get("status", "")
                if not hl or status in ("archived", "stale"):
                    continue
                mtime = fp.stat().st_mtime
                age_years = (now - mtime) / (365.25 * 86400)
                threshold = float(hl) * _mult
                if age_years > threshold:
                    stale_nodes.append((fp, fm, age_years, hl))
                    if auto_mark:
                        new_text = text.replace(
                            "status: {}".format(status),
                            "status: stale"
                        )
                        if new_text != text:
                            fp.write_text(new_text, encoding="utf-8")
                            updated_nodes.append(fp.stem)
            except Exception:
                pass

        print("    Stale nodes detected: {}".format(len(stale_nodes)))
        for fp, fm, age, hl in stale_nodes[:10]:
            print("    ⚠  [{:.1f}y / hl={:.1f}] {}".format(age, hl, fp.stem))
        if len(stale_nodes) > 10:
            print("    ... ({} more)".format(len(stale_nodes) - 10))
        if auto_mark and updated_nodes:
            print("    ✓  Marked stale: {}".format(len(updated_nodes)))

        return True, "{} stale, {} marked".format(len(stale_nodes), len(updated_nodes))

    runner.step("staleness_scan", _staleness)
    runner.summary()


def pipeline_deepdive(runner, query, threshold=2):
    """Deep Research: Detect → Drill → Draft."""
    header("PIPELINE: deepdive ['{}'] threshold={}".format(query, threshold))

    def _deepdive():
        # BUG FIX v2.0: pass --threshold xuống script
        args = [query, "--threshold", str(threshold)]
        ok_, out, err = run_script("deepdive_search.py", args, timeout=180)
        out = out or ""
        summary = next((l for l in out.splitlines() if "SUMMARY:" in l), "")
        for line in out.splitlines():
            if any(x in line for x in ["DETECT", "DRILL", "DRAFT", "SUMMARY", "thin", "→"]):
                print("    {}".format(line))
        return ok_, summary[:100] if summary else "done"

    runner.step("deepdive", _deepdive)
    runner.summary()


def pipeline_rename(runner, old_name, new_name, dry_run=False):
    """Rename a wiki node safely: heal links then rename file."""
    mode = " [DRY RUN]" if dry_run else ""
    header("PIPELINE: rename [{}] → [{}]{}".format(old_name, new_name, mode))
    args = [old_name, new_name]
    if dry_run:
        args.append("--dry-run")

    def _rename():
        ok_, out, err = run_script("rename_node.py", args)
        out = out or ""
        if out:
            for line in out.strip().splitlines():
                print("    {}".format(line))
        return ok_, "OK" if ok_ else (err[:80] if err else "FAILED")

    runner.step("rename_node", _rename)

    if not dry_run:
        runner.step("sync_graph",  lambda: step_build_graph())
        runner.step("sync_index",  lambda: step_gen_index())

    runner.summary()


def pipeline_stage(runner, args):
    """Auto ingest staging workflow wrapper."""
    header("PIPELINE: stage")
    cmd_args = []
    if args.n is not None:
        cmd_args += ["--n", str(args.n)]
    if args.book:
        cmd_args += ["--book", args.book]
    if args.min_depth is not None:
        cmd_args += ["--min-depth", str(args.min_depth)]
    if args.dry_run:
        cmd_args.append("--dry-run")
    if args.list_coverage:
        cmd_args.append("--list-coverage")
    if args.staged:
        cmd_args.append("--staged")
    if args.accept:
        cmd_args += ["--accept", args.accept]
    if args.accept_all:
        cmd_args.append("--accept-all")

    def _stage():
        ok_, out, err = run_script("auto_ingest.py", cmd_args, timeout=180)
        out = out or ""
        for line in out.strip().splitlines()[:80]:
            print("    {}".format(line))
        if err:
            for line in err.strip().splitlines()[:20]:
                print("    {}".format(line))
        return ok_, "OK" if ok_ else (err[:80] if err else "FAILED")

    runner.step("auto_ingest", _stage)
    runner.summary()


def pipeline_review(runner, action=None, target=None):
    """Review staged nodes: list / accept <name> / accept-all."""
    header("PIPELINE: review")

    if not STAGED_DIR.exists():
        info("No staged_nodes directory found.")
        runner.summary()
        return

    staged = sorted([f for f in STAGED_DIR.glob("*.md") if not f.name.startswith("_")])

    if action == "accept-all":
        def _accept_all():
            ok_, out, err = run_script("auto_ingest.py", ["--accept-all"], timeout=120)
            out = out or ""
            for line in out.strip().splitlines()[:60]:
                print("    {}".format(line))
            return ok_, "OK" if ok_ else (err[:80] if err else "FAILED")
        runner.step("accept_all", _accept_all)
        if True:
            runner.step("sync_graph", step_build_graph)
            runner.step("sync_index", step_gen_index)
        runner.summary()
        return

    if action == "accept" and target:
        def _accept():
            ok_, out, err = run_script("auto_ingest.py", ["--accept", target], timeout=120)
            out = out or ""
            for line in out.strip().splitlines()[:40]:
                print("    {}".format(line))
            return ok_, "OK" if ok_ else (err[:80] if err else "FAILED")
        runner.step("accept_node", _accept)
        runner.step("sync_graph", step_build_graph)
        runner.step("sync_index", step_gen_index)
        runner.summary()
        return

    # Default: list staged nodes với tóm tắt frontmatter
    def _list_staged():
        if not staged:
            print("    (no staged nodes)")
            return True, "0 staged"

        print()
        for i, fp in enumerate(staged, 1):
            try:
                text = fp.read_text(encoding="utf-8", errors="ignore")
                fm = {}
                if text.startswith("---"):
                    end = text.find("---", 3)
                    if end != -1:
                        try:
                            fm = yaml.safe_load(text[3:end]) or {}
                        except Exception:
                            pass
                title  = fm.get("title", fp.stem)
                typ    = fm.get("type", "?")
                tags   = fm.get("tags", [])
                thesis = str(fm.get("thesis", "")).strip()[:80]
                tag_str = ", ".join(str(t) for t in tags[:4]) if tags else "—"
                print("  {}[{}]{} {}{}{}".format(BOLD, i, RESET, CYAN, title, RESET))
                print("       type={} | tags={}".format(typ, tag_str))
                if thesis:
                    print("       thesis: {}{}{}".format(DIM, thesis, RESET))
                print("       file: {}".format(fp.name))
            except Exception as e:
                print("  [{}] {} — error reading: {}".format(i, fp.name, e))

        print()
        print("  To accept: python librarian.py review accept <filename_substring>")
        print("  To accept all: python librarian.py review accept-all")
        return True, "{} staged nodes".format(len(staged))

    runner.step("list_staged", _list_staged)
    runner.summary()


def pipeline_extract(runner, args):
    """PDF extraction wrapper."""
    header("PIPELINE: extract")
    cmd_args = []
    if args.book:
        cmd_args += ["--book", args.book]
    if args.file:
        cmd_args += ["--file", args.file]
    if args.all:
        cmd_args.append("--all")
    if args.dry_run:
        cmd_args.append("--dry-run")
    if args.skip_existing:
        cmd_args.append("--skip-existing")

    def _extract():
        ok_, out, err = run_script("extract_pdf.py", cmd_args, timeout=180)
        text = out or err or ""
        for line in text.strip().splitlines()[:80]:
            print("    {}".format(line))
        return ok_, "OK" if ok_ else (err[:80] if err else "FAILED")

    runner.step("extract_pdf", _extract)
    runner.summary()


def pipeline_scout(runner, args):
    """Random raw source discovery wrapper."""
    header("PIPELINE: scout")
    cmd_args = []
    if args.mode:
        cmd_args += ["--mode", args.mode]
    if args.n is not None:
        cmd_args += ["--n", str(args.n)]

    def _scout():
        ok_, out, err = run_script("raw_scout.py", cmd_args, timeout=60)
        text = out or err or ""
        for line in text.strip().splitlines()[:80]:
            print("    {}".format(line))
        return ok_, "OK" if ok_ else (err[:80] if err else "FAILED")

    runner.step("raw_scout", _scout)
    runner.summary()


def pipeline_section(runner, args):
    """Exact extractor wrapper."""
    header("PIPELINE: section")
    cmd_args = ["--dir", args.dir, "--heading", args.heading, "--out", args.out]

    def _section():
        ok_, out, err = run_script("exact_extractor.py", cmd_args, timeout=90)
        text = out or err or ""
        for line in text.strip().splitlines()[:40]:
            print("    {}".format(line))
        return ok_, "OK" if ok_ else (err[:80] if err else "FAILED")

    runner.step("exact_extractor", _section)
    runner.summary()


def pipeline_organize(runner, args, force_cleanup_mode=False):
    """Inspect and organize node folders.
    force_cleanup_mode: True khi alias 'cleanup' được dùng
      → auto bật --fix-whitespace + --no-move
    """
    header("PIPELINE: {}".format("cleanup" if force_cleanup_mode else "organize"))
    cmd_args = []
    if args.dir:
        cmd_args += ["--dir", args.dir]

    # cleanup alias: default --fix-whitespace --no-move
    fix_ws  = args.fix_whitespace or force_cleanup_mode
    no_move = args.no_move        or force_cleanup_mode

    if args.apply and not args.dry_run:
        cmd_args.append("--apply")
    if no_move:
        cmd_args.append("--no-move")
    if fix_ws:
        cmd_args.append("--fix-whitespace")
    if args.limit is not None:
        cmd_args += ["--limit", str(args.limit)]

    def _organize():
        ok_, out, err = run_script("organize_nodes.py", cmd_args, timeout=120)
        text = out or err or ""
        for line in text.strip().splitlines()[:120]:
            print("    {}".format(line))
        return ok_, "OK" if ok_ else (err[:80] if err else "FAILED")

    runner.step("organize_nodes", _organize)
    if args.apply and not args.dry_run:
        runner.step("sync_graph", lambda: step_build_graph())
        runner.step("sync_index", lambda: step_gen_index())
    runner.summary()


def pipeline_embed(runner, args):
    """Manage semantic embedding index (FAISS)."""
    mode = "[INCREMENTAL]" if args.incremental else ""
    header("PIPELINE: embed {}".format(mode))

    if args.stats:
        # Just print stats
        runner.step("embed_stats", step_embed_stats)
        runner.summary()
        return

    if args.watch:
        # Run build first, then watch
        runner.step("embed_build", lambda: step_embed_build(incremental=args.incremental))
        runner.summary()
        print("\n  [INFO] Entering watch mode (Ctrl+C to stop)...")
        try:
            ok_, out, err = run_script("embed_index.py", ["--watch"], timeout=None)
        except KeyboardInterrupt:
            print("\n  [INFO] Watch stopped.")
        return

    # Default: build or incremental
    runner.step("embed_build", lambda: step_embed_build(incremental=args.incremental))
    runner.summary()


def pipeline_inbox(runner, args):
    """Process inbox: scan → list files → user selects folder → extract + move."""
    header("PIPELINE: inbox")

    if args.list_books:
        runner.step("list_books", lambda: step_inbox_list_books())
        runner.summary()
        return

    if args.process:
        runner.step("process", lambda: step_inbox_process(target_book=args.process))
        runner.step("sync_graph", lambda: step_build_graph())
        runner.step("sync_index", lambda: step_gen_index())
        runner.summary()
        return

    # Default: scan only (user must manually choose folder)
    runner.step("scan_inbox", step_inbox_scan)
    runner.summary()


def pipeline_validate(runner):
    """Validate wiki schema, wikilinks, and references."""
    header("PIPELINE: validate")

    def _validate_frontmatter():
        ok, issues = validate_frontmatter_vs_schema()
        if issues:
            for issue in issues[:10]:
                print("    {}".format(issue))
            if len(issues) > 10:
                print("    ... {} more issues".format(len(issues) - 10))
        msg = "0 issues" if ok else "{} issues found".format(len(issues))
        return ok, msg

    def _validate_wikilinks():
        ok, broken = validate_broken_wikilinks()
        if broken:
            for link in broken[:10]:
                print("    {}".format(link))
            if len(broken) > 10:
                print("    ... {} more broken links".format(len(broken) - 10))
        msg = "OK" if ok else "{} broken links".format(len(broken))
        return ok, msg

    def _validate_orphan_refs():
        ok, orphans = validate_orphan_refs()
        if orphans:
            for orphan in orphans[:10]:
                print("    {}".format(orphan))
            if len(orphans) > 10:
                print("    ... {} more orphan refs".format(len(orphans) - 10))
        msg = "OK" if ok else "{} orphan refs".format(len(orphans))
        return ok, msg

    runner.step("schema_check", _validate_frontmatter)
    runner.step("wikilink_check", _validate_wikilinks)
    runner.step("orphan_ref_check", _validate_orphan_refs)
    runner.summary()


def pipeline_writeback(runner):
    """Process writeback_queue.md: apply frontmatter updates & clear queue."""
    header("PIPELINE: writeback")

    def _process_queue():
        ok, applied = process_writeback_queue()
        msg = "{} nodes updated".format(applied)
        return ok, msg

    runner.step("process_queue", _process_queue)
    runner.step("sync_graph", lambda: step_build_graph())
    runner.step("sync_index", lambda: step_gen_index())
    runner.summary()


def pipeline_batch(runner, pipelines_str, args, extra_target=None):
    """Chạy nhiều pipelines liên tiếp.
    pipelines_str: comma-separated list, e.g. "sync,health" hoặc "daily,wisdom"
    extra_target: truyền vào cho wisdom tag, deepdive query, v.v.
    """
    names = [p.strip() for p in pipelines_str.split(",") if p.strip()]
    header("PIPELINE: batch [{}]".format(" → ".join(names)))

    SIMPLE = {
        "sync":     lambda: pipeline_sync(StepRunner()),
        "ingest":   lambda: pipeline_ingest(StepRunner()),
        "health":   lambda: pipeline_health(StepRunner()),
        "daily":    lambda: pipeline_daily(StepRunner()),
        "staleness":lambda: pipeline_staleness(StepRunner()),
        "review":   lambda: pipeline_review(StepRunner()),
        "validate": lambda: pipeline_validate(StepRunner()),
        "writeback":lambda: pipeline_writeback(StepRunner()),
    }

    for name in names:
        print()
        if name in SIMPLE:
            SIMPLE[name]()
        elif name == "wisdom":
            tag = extra_target
            if not tag:
                fail("batch wisdom: tag required (e.g. batch daily,wisdom monetary-policy)")
                continue
            pipeline_wisdom(StepRunner(), tag, no_llm=args.no_llm, model=args.model)
        elif name == "deepdive":
            query = extra_target
            if not query:
                fail("batch deepdive: query required")
                continue
            pipeline_deepdive(StepRunner(), query, threshold=args.threshold)
        elif name == "embed":
            pipeline_embed(StepRunner(), args)
        elif name in ("organize", "cleanup"):
            pipeline_organize(StepRunner(), args, force_cleanup_mode=(name == "cleanup"))
        else:
            fail("batch: unknown pipeline '{}'".format(name))

    print("\n{}batch done: [{}]{}".format(BOLD, " → ".join(names), RESET))


# ── HELP DATA ─────────────────────────────────────────────────────────────────

PIPELINE_HELP = {
    "sync": {
        "desc":    "Đồng bộ graph + index sau bất kỳ thay đổi nào trong wiki.",
        "when":    "Sau khi sửa node, đổi tên file, hoặc thêm wikilink thủ công.",
        "steps": [
            ("build_graph",  "Inject wiki nodes & edges vào graph.json"),
            ("gen_index",    "Tái tạo index.md và các sub-index theo loại node"),
            ("staleness",    "Kiểm tra wisdom reports nào đã bị lỗi thời"),
        ],
        "examples": [
            "python librarian.py sync",
            "python librarian.py sync --skip gen_index",
            "python librarian.py sync --only staleness",
        ],
    },
    "ingest": {
        "desc":    "Post-ingest sync sau khi hoàn tất Phase A–C của W2.",
        "when":    "Sau khi SPAWN/EXPAND node mới từ raw source.",
        "steps": [
            ("build_graph",  "Inject nodes & edges mới vào graph.json"),
            ("gen_index",    "Tái tạo index"),
            ("auto_bridge",  "Tự động link orphan nodes vào graph (--force --backup)"),
            ("staleness",    "Báo cáo tags bị stale cần re-run wisdom"),
        ],
        "examples": [
            "python librarian.py ingest",
            "python librarian.py ingest --skip auto_bridge",
        ],
    },
    "health": {
        "desc":    "Kiểm tra toàn bộ sức khỏe của wiki graph.",
        "when":    "Định kỳ hoặc trước khi bắt đầu ingest topic mới.",
        "steps": [
            ("find_orphans",   "Tìm nodes không có incoming link nào"),
            ("missing_thesis", "Tìm nodes thiếu thesis trong frontmatter"),
            ("staleness",      "Wisdom reports nào đã lỗi thời"),
            ("suggest_ideas",  "Bounty nodes + synthesis alerts + random walk"),
        ],
        "examples": [
            "python librarian.py health",
            "python librarian.py health --only missing_thesis,staleness",
            "python librarian.py health --skip suggest_ideas",
        ],
    },
    "daily": {
        "desc":    "Workflow hằng ngày: gợi ý việc cần làm hôm nay.",
        "when":    "Đầu mỗi session làm việc với wiki.",
        "steps": [
            ("suggest_ideas",  "Bounty nodes, synthesis alerts, random walk"),
            ("find_orphans",   "Orphan nodes cần được bridge"),
            ("staleness",      "Wisdom reports cần refresh"),
            ("missing_thesis", "Nodes cần bổ sung thesis"),
        ],
        "examples": [
            "python librarian.py daily",
            "python librarian.py daily --only suggest_ideas",
        ],
    },
    "wisdom": {
        "desc":    "Chạy Wisdom Synthesis cho một tag — Hub Map + Tension Pairs + LLM essay.",
        "when":    "Trước khi ingest topic mới (baseline) hoặc sau khi ingest (so sánh).",
        "steps": [
            ("staleness_check", "Kiểm tra report cũ có tồn tại và còn fresh không"),
            ("auto_synthesis",  "Collect → subgraph → hubs → collisions → clusters → report"),
        ],
        "examples": [
            "python librarian.py wisdom monetary-policy --no-llm",
            "python librarian.py wisdom fixed-income",
            "python librarian.py wisdom central-banking --model claude-sonnet-4-6",
        ],
    },
    "audit": {
        "desc":    "Chạy F.I.T.S.E.R.B.V.L audit trên một wiki node hoặc draft.",
        "when":    "Trước khi merge node mới, hoặc khi nghi ngờ chất lượng của một node.",
        "steps": [
            ("claim_audit", "F-I-T-S-E-R-B-V-L: 9 bước kiểm tra chất lượng node"),
        ],
        "examples": [
            "python librarian.py audit 03_wiki/mechanisms/Fiscal_Dominance.md",
            "python librarian.py audit 03_wiki/concepts/Barro_Gordon_Model.md",
        ],
    },
    "search": {
        "desc":    "Tìm kiếm trong wiki + raw sources.",
        "when":    "Khi cần tìm khái niệm trước khi SPAWN node hoặc trong khi viết.",
        "steps": [
            ("search", "wiki_search RRF mặc định; semantic-only hoặc hybrid heatmap khi cần"),
        ],
        "examples": [
            "python librarian.py search 'fiscal dominance' --top 8",
            "python librarian.py search 'interest rate transmission' --semantic --no-raw",
            "python librarian.py search 'repo market liquidity stress' --deep --raw-only --top 3",
            "python librarian.py search 'monetary policy' --export 04_outputs/temp/mp_search.md",
        ],
    },
    "deepdive": {
        "desc":    "Deep Research: Detect thin wiki nodes → Drill raw sources → Draft expansion proposal.",
        "when":    "Khi wiki node có confidence thấp, [LLM] placeholders, hoặc thiếu source_refs.",
        "steps": [
            ("detect", "wiki_search → đánh giá confidence/[LLM]/source_refs của top results"),
            ("drill",  "hybrid_search trên Raw Sources nếu wiki coverage thin"),
            ("draft",  "Tạo expansion proposal với RAW citations vào 04_outputs/drafts/"),
        ],
        "examples": [
            "python librarian.py deepdive 'taralac facility mechanics'",
            "python librarian.py deepdive 'interest rate corridor' --threshold 3",
        ],
    },
    "staleness": {
        "desc": "Auto-detect nodes quá half_life → report hoặc mark status:stale",
        "when": "Khi cần rà soát node đã quá hạn tri thức hoặc muốn tự động gắn cờ stale.",
        "steps": [("staleness_scan", "Quét toàn bộ 03_wiki theo half_life_years")],
        "examples": [
            "python librarian.py staleness",
            "python librarian.py staleness --auto-mark",
            "python librarian.py staleness --threshold 1.0   # stricter",
        ],
    },
    "rename": {
        "desc":    "Đổi tên wiki node an toàn: heal [[OldName]] → [[NewName]] rồi rename file + sync.",
        "when":    "Khi cần rename node sau ingest, tránh broken wikilinks.",
        "steps": [
            ("rename_node", "Search-replace wikilinks + rename file + update frontmatter title"),
            ("sync_graph",  "Rebuild graph.json với tên mới"),
            ("sync_index",  "Rebuild index.md + _index.md"),
        ],
        "examples": [
            "python librarian.py rename OldName NewName",
            "python librarian.py rename 'Old Name' 'New Name'",
            "python librarian.py rename OldName NewName --dry-run",
        ],
    },
    "status": {
        "desc":    "System overview: node count, staged nodes, stale flags, orphan count, scripts, reports.",
        "when":    "Đầu session hoặc khi cần nắm nhanh trạng thái hệ thống.",
        "steps": [
            ("status", "In thống kê hệ thống + danh sách pipelines"),
        ],
        "examples": [
            "python librarian.py status",
            "python librarian.py          # mặc định = status",
        ],
    },
    "stage": {
        "desc": "Staging ingest từ raw books: sample uncovered sections, review staged nodes, accept vào wiki.",
        "when": "Khi muốn bán tự động hóa W2 ingest thay vì làm thủ công từng section.",
        "steps": [
            ("auto_ingest", "scan books -> coverage -> stage drafts -> optionally accept reviewed drafts"),
        ],
        "examples": [
            "python librarian.py stage --dry-run",
            "python librarian.py stage --list-coverage",
            "python librarian.py stage --staged",
            "python librarian.py stage --accept Bindseil__Some_Heading",
        ],
    },
    "review": {
        "desc": "Xem và accept staged nodes — UI rõ ràng hơn stage --staged/--accept.",
        "when": "Sau khi chạy stage, trước khi merge nodes vào 03_wiki chính thức.",
        "steps": [
            ("list_staged",  "Liệt kê staged nodes với frontmatter tóm tắt"),
            ("accept_node",  "Accept node cụ thể → 03_wiki + sync"),
            ("accept_all",   "Accept tất cả nodes → 03_wiki + sync"),
        ],
        "examples": [
            "python librarian.py review",
            "python librarian.py review accept Bindseil__Some_Heading",
            "python librarian.py review accept-all",
        ],
    },
    "extract": {
        "desc": "Extract PDF sang Markdown trong 02_sources/books.",
        "when": "Khi vừa thêm PDF raw source mới hoặc cần backfill file .md cho pipeline ingest/search.",
        "steps": [
            ("extract_pdf", "pdf -> markdown alongside source files"),
        ],
        "examples": [
            "python librarian.py extract --book perry --skip-existing",
            "python librarian.py extract --file 02_sources/books/foo/bar.pdf --dry-run",
            "python librarian.py extract --all --dry-run",
        ],
    },
    "scout": {
        "desc": "Random discovery trên raw sources để tìm idea hoặc spot coverage gaps.",
        "when": "Khi cần seed ý tưởng nghiên cứu hoặc random walk ngoài wiki graph.",
        "steps": [
            ("raw_scout", "sample lines or terms from clustered raw sources"),
        ],
        "examples": [
            "python librarian.py scout --mode lines --n 10",
            "python librarian.py scout --mode words --n 20",
        ],
    },
    "section": {
        "desc": "Surgical extraction một section cụ thể từ book markdown.",
        "when": "Khi cần raw passage đầy đủ để viết node hoặc audit claim sâu hơn.",
        "steps": [
            ("exact_extractor", "extract matching chapter/section block into output file"),
        ],
        "examples": [
            'python librarian.py section --dir 02_sources/books/bindseil_monetary_policy --heading "1.1 Key Concepts" --out 04_outputs/temp/bindseil_1_1.md',
        ],
    },
    "organize": {
        "desc": "Dọn dẹp và sắp xếp node trong thư mục: report schema gaps, misplaced types, duplicates, whitespace.",
        "when": "Khi một folder wiki lộn xộn, node nằm sai taxonomy folder, hoặc cần review trước khi sync/ingest tiếp.",
        "steps": [
            ("organize_nodes", "scan folder -> propose moves/fixes; default dry-run"),
            ("sync_graph", "rebuild graph after applied moves"),
            ("sync_index", "rebuild generated indexes after applied moves"),
        ],
        "examples": [
            "python librarian.py organize --dir 03_wiki/concepts",
            "python librarian.py organize --dir 03_wiki --limit 40",
            "python librarian.py organize --dir 03_wiki/concepts --apply",
        ],
    },
    "cleanup": {
        "desc": "Dọn whitespace cơ học trong folder (trailing spaces, blank lines, final newline). Không move node.",
        "when": "Sau khi ingest hàng loạt hoặc khi node có trailing whitespace nhìn xấu trong diff.",
        "steps": [
            ("organize_nodes", "scan + fix whitespace only (no moves)"),
        ],
        "examples": [
            "python librarian.py cleanup --dir 03_wiki/mechanisms",
            "python librarian.py cleanup --dir 03_wiki/concepts --apply",
            "python librarian.py cleanup --dir 03_wiki --apply --limit 50",
        ],
    },
    "batch": {
        "desc": "Chạy nhiều pipelines liên tiếp trong một lệnh.",
        "when": "Khi muốn kết hợp nhiều bước mà không cần mở nhiều terminal.",
        "steps": [
            ("pipeline_N", "Mỗi pipeline trong list chạy tuần tự với StepRunner riêng"),
        ],
        "examples": [
            "python librarian.py batch sync,health",
            "python librarian.py batch daily,wisdom monetary-policy",
            "python librarian.py batch ingest,staleness",
            "python librarian.py batch organize,sync --dir 03_wiki/concepts --apply",
        ],
    },
    "inbox": {
        "desc": "Process inbox: scan files → user manually selects folder → extract + move.",
        "when": "Khi add tài liệu mới vào 02_sources/inbox/, cần extract + organize cho ingest.",
        "steps": [
            ("scan_inbox", "Scan inbox files (no auto-classify, user chooses folder)"),
            ("process",    "Extract + move inbox files to specified book folder"),
            ("sync_graph", "Rebuild graph after moving files"),
            ("sync_index", "Rebuild indexes after moving files"),
        ],
        "examples": [
            "python librarian.py inbox                     # default = scan",
            "python librarian.py inbox --list-books        # show available folders",
            "python librarian.py inbox --process bindseil  # move inbox files → 02_sources/bindseil/",
            "python librarian.py inbox --process clipping  # move inbox files → 02_sources/clipping/",
        ],
    },
}


def pipeline_help(target=None):
    """Help system: overview hoặc chi tiết một pipeline."""
    if target and target in PIPELINE_HELP:
        p = PIPELINE_HELP[target]
        header("HELP: {}".format(target.upper()))
        print("\n  {}Description:{} {}".format(BOLD, RESET, p["desc"]))
        print("  {}When to use:{} {}".format(BOLD, RESET, p["when"]))
        print("\n  {}Steps:{}".format(BOLD, RESET))
        for step_name, step_desc in p["steps"]:
            print("    {:22s} {}".format(step_name, step_desc))
        print("\n  {}Examples:{}".format(BOLD, RESET))
        for ex in p["examples"]:
            print("    {}".format(ex))
        print()
    else:
        header("LIBRARIAN v2.0 — Pipeline Reference")
        print()
        all_pipes = [
            "status", "inbox", "sync", "ingest", "health", "daily",
            "wisdom", "audit", "search", "deepdive",
            "rename", "staleness", "stage", "review",
            "extract", "scout", "section",
            "organize", "cleanup", "batch",
        ]
        for name in all_pipes:
            if name not in PIPELINE_HELP:
                continue
            p = PIPELINE_HELP[name]
            print("  {}{:<10s}{}  {}".format(BOLD, name, RESET, p["desc"]))
            for ex in p.get("examples", [])[:1]:
                print("              {}{}{}".format(DIM, ex, RESET))
            print()
        print("  Tip: python librarian.py help <pipeline>  → chi tiết từng pipeline")
        print()


# ── STATUS PIPELINE ───────────────────────────────────────────────────────────

def pipeline_status():
    """System overview — v2.0: thêm staged count, stale flag count, orphan estimate."""
    header("WIKI LINK — System Status  (librarian v2.0)")
    wiki_dir     = WIKI_ROOT / "03_wiki"
    scripts_dir  = SCRIPTS_DIR
    reports_dir  = WIKI_ROOT / "04_outputs" / "research"

    node_count   = len(list(wiki_dir.rglob("*.md"))) if wiki_dir.exists() else 0
    script_count = len(list(scripts_dir.glob("*.py"))) if scripts_dir.exists() else 0
    report_count = len(list(reports_dir.glob("*.md"))) if reports_dir.exists() else 0

    staged_count = _count_staged()
    stale_count  = _count_stale_status()
    orphan_count = _count_orphans()

    print()
    print("  Wiki nodes      : {}".format(node_count))
    print("  Scripts         : {}".format(script_count))
    print("  Wisdom reports  : {}".format(report_count))
    print("  Staged (pending): {}{}{}".format(
        YELLOW if staged_count else GREEN, staged_count, RESET))
    print("  Status=stale    : {}{}{}".format(
        YELLOW if stale_count else GREEN, stale_count, RESET))
    print("  Orphans         : {}{}{}".format(
        RED if orphan_count else GREEN, orphan_count, RESET))
    print()

def main():
    parser = argparse.ArgumentParser(
        prog="librarian.py",
        description="Wiki Link Librarian v2.0 — single entry point for all pipelines.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("command", nargs="?", default="status",
                        help="Pipeline to run (default: status)")
    parser.add_argument("targets", nargs="*",
                        help="Positional args for the pipeline (query, tag, file, …)")

    # StepRunner control
    parser.add_argument("--skip",  default="",
                        help="Comma-separated step names to skip")
    parser.add_argument("--only",  default="",
                        help="Comma-separated step names to run exclusively")

    # search
    parser.add_argument("--top",            type=int,  default=8)
    parser.add_argument("--deep",           action="store_true")
    parser.add_argument("--semantic",       action="store_true")
    parser.add_argument("--no-raw",         action="store_true")
    parser.add_argument("--no-wiki",        action="store_true")
    parser.add_argument("--raw-only",       action="store_true")
    parser.add_argument("--no-semantic",    action="store_true")
    parser.add_argument("--type",           dest="filter_type", default=None)
    parser.add_argument("--min-confidence", type=int, default=0)
    parser.add_argument("--export",         default=None)

    # staleness / deepdive threshold
    parser.add_argument("--auto-mark",      action="store_true")
    parser.add_argument("--threshold",      type=float, default=None)

    # wisdom
    parser.add_argument("--no-llm",         action="store_true")
    parser.add_argument("--model",          default="claude-sonnet-4-6")

    # rename / general
    parser.add_argument("--dry-run",        action="store_true")

    # stage
    parser.add_argument("--n",              type=int, default=None)
    parser.add_argument("--book",           default=None)
    parser.add_argument("--min-depth",      type=int, default=None)
    parser.add_argument("--list-coverage",  action="store_true")
    parser.add_argument("--staged",         action="store_true")
    parser.add_argument("--accept",         default=None)
    parser.add_argument("--accept-all",     action="store_true")

    # extract
    parser.add_argument("--file",           default=None)
    parser.add_argument("--all",            action="store_true")
    parser.add_argument("--skip-existing",  action="store_true")

    # scout
    parser.add_argument("--mode",           default=None)

    # section
    parser.add_argument("--dir",            default=None)
    parser.add_argument("--heading",        default=None)
    parser.add_argument("--out",            default=None)

    # organize / cleanup
    parser.add_argument("--apply",          action="store_true")
    parser.add_argument("--no-move",        action="store_true")
    parser.add_argument("--fix-whitespace", action="store_true")
    parser.add_argument("--limit",          type=int, default=None)

    # embed
    parser.add_argument("--stats",          action="store_true")
    parser.add_argument("--watch",          action="store_true")
    parser.add_argument("--incremental",    action="store_true", help="Incremental embed (only new/changed files)")

    # inbox
    parser.add_argument("--scan",           action="store_true", help="Scan inbox files (default)")
    parser.add_argument("--process",        default=None,        help="Process inbox → <book|clipping> folder (manual classify)")
    parser.add_argument("--list-books",     action="store_true", help="List known book folders")

    args = parser.parse_args()

    skip_set = set(s.strip() for s in args.skip.split(",") if s.strip())
    only_set = set(s.strip() for s in args.only.split(",") if s.strip())

    def make_runner():
        return StepRunner(skip_set=skip_set, only_set=only_set)

    cmd     = args.command.lower()
    targets = args.targets

    if cmd == "status":
        pipeline_status()

    elif cmd == "sync":
        pipeline_sync(make_runner())

    elif cmd == "ingest":
        pipeline_ingest(make_runner())

    elif cmd == "health":
        pipeline_health(make_runner())

    elif cmd == "daily":
        pipeline_daily(make_runner())

    elif cmd == "wisdom":
        tag = targets[0] if targets else None
        if not tag:
            fail("wisdom: <tag> required  (e.g. python librarian.py wisdom monetary-policy)")
            sys.exit(1)
        pipeline_wisdom(make_runner(), tag, no_llm=args.no_llm, model=args.model)

    elif cmd == "audit":
        file_path = targets[0] if targets else None
        if not file_path:
            fail("audit: <file> required  (e.g. python librarian.py audit 03_wiki/mechanisms/Foo.md)")
            sys.exit(1)
        pipeline_audit(make_runner(), file_path)

    elif cmd == "search":
        query = " ".join(targets) if targets else None
        if not query:
            fail("search: <query> required  (e.g. python librarian.py search 'fiscal dominance')")
            sys.exit(1)
        pipeline_search(
            make_runner(), query,
            deep=args.deep,
            semantic=args.semantic,
            top=args.top,
            no_raw=args.no_raw,
            no_wiki=args.no_wiki,
            raw_only=args.raw_only,
            no_semantic=args.no_semantic,
            filter_type=args.filter_type,
            min_confidence=args.min_confidence,
            export=args.export,
        )

    elif cmd == "deepdive":
        query = " ".join(targets) if targets else None
        if not query:
            fail("deepdive: <query> required  (e.g. python librarian.py deepdive 'repo mechanics')")
            sys.exit(1)
        threshold = int(args.threshold) if args.threshold is not None else 2
        pipeline_deepdive(make_runner(), query, threshold=threshold)

    elif cmd == "rename":
        if len(targets) < 2:
            fail("rename: <old_name> <new_name> required")
            sys.exit(1)
        pipeline_rename(make_runner(), targets[0], targets[1], dry_run=args.dry_run)

    elif cmd == "staleness":
        pipeline_staleness(make_runner(), auto_mark=args.auto_mark,
                           threshold_multiplier=args.threshold)

    elif cmd == "stage":
        pipeline_stage(make_runner(), args)

    elif cmd == "review":
        action = targets[0] if targets else None
        target = targets[1] if len(targets) > 1 else None
        pipeline_review(make_runner(), action=action, target=target)

    elif cmd == "extract":
        pipeline_extract(make_runner(), args)

    elif cmd == "scout":
        pipeline_scout(make_runner(), args)

    elif cmd == "section":
        pipeline_section(make_runner(), args)

    elif cmd in ("organize", "cleanup"):
        pipeline_organize(make_runner(), args, force_cleanup_mode=(cmd == "cleanup"))

    elif cmd == "inbox":
        pipeline_inbox(make_runner(), args)

    elif cmd == "embed":
        pipeline_embed(make_runner(), args)

    elif cmd == "validate":
        pipeline_validate(make_runner())

    elif cmd == "writeback":
        pipeline_writeback(make_runner())

    elif cmd == "batch":
        pipelines_str = targets[0] if targets else ""
        extra_target  = targets[1] if len(targets) > 1 else None
        if not pipelines_str:
            fail("batch: <pipelines> required  (e.g. python librarian.py batch sync,health)")
            sys.exit(1)
        pipeline_batch(make_runner(), pipelines_str, args, extra_target=extra_target)

    elif cmd in ("help",):
        target = targets[0] if targets else None
        pipeline_help(target)

    else:
        fail("Unknown command: '{}'.  Run: python librarian.py help".format(cmd))
        sys.exit(1)


if __name__ == "__main__":
    main()