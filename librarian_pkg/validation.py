import re
from datetime import datetime

import yaml

from .shared import WIKI_DIR, WIKI_ROOT


def validate_frontmatter_vs_schema():
    issues = []
    schema_dir = WIKI_ROOT / "01_schema" / "registry"
    if not schema_dir.exists() or not WIKI_DIR.exists():
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
        except Exception as exc:
            issues.append("{}  — error: {}".format(fp.relative_to(WIKI_ROOT), str(exc)[:40]))

    return len(issues) == 0, issues


def validate_broken_wikilinks():
    broken = []
    if not WIKI_DIR.exists():
        return True, []

    valid_nodes = {fp.stem for fp in WIKI_DIR.rglob("*.md") if not fp.name.startswith("_")}
    link_pattern = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]*)?(?:#[^\]]*)?\]\]")

    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("_"):
            continue
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            for match in link_pattern.finditer(text):
                target = match.group(1).strip()
                if "/" in target:
                    target = target.split("/", 1)[1]
                if target not in valid_nodes:
                    broken.append("{}  →  [[{}]] (not found)".format(fp.relative_to(WIKI_ROOT), target))
        except Exception:
            pass

    return len(broken) == 0, broken


def validate_orphan_refs():
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
                if not (sources_dir / ref).exists():
                    orphans.append("{}  →  source_ref '{}' not found".format(fp.relative_to(WIKI_ROOT), ref))
        except Exception:
            pass

    return len(orphans) == 0, orphans


def append_log_entry(pipeline_name, status, summary=""):
    log_path = WIKI_ROOT / "01_schema" / "log.md"
    if not log_path.exists():
        log_path.write_text(
            "# Librarian Execution Log\n\n| Timestamp | Pipeline | Status | Summary |\n|-----------|----------|--------|---------|\n",
            encoding="utf-8",
        )
    log_content = log_path.read_text(encoding="utf-8")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    summary = summary.replace("|", "\\|")[:80]
    log_content += "\n| {} | {} | {} | {} |".format(timestamp, pipeline_name, status, summary)
    log_path.write_text(log_content, encoding="utf-8")


def process_writeback_queue():
    queue_path = WIKI_ROOT / "01_schema" / "writeback_queue.md"
    if not queue_path.exists():
        return True, 0

    applied = 0
    for block in queue_path.read_text(encoding="utf-8").split("---"):
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
                key, _, value = line.partition(":")
                updates[key.strip()] = value.strip().strip('"')
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
            if not content.startswith("---"):
                continue
            end = content.find("---", 3)
            if end == -1:
                continue
            fm = yaml.safe_load(content[3:end]) or {}
            for key, value in updates.items():
                fm[key] = value

            new_fm = "---\n"
            for key, value in fm.items():
                if isinstance(value, list):
                    new_fm += "{}:\n".format(key)
                    for item in value:
                        new_fm += "  - {}\n".format(item)
                else:
                    new_fm += "{}: {}\n".format(key, value)
            new_fm += "---\n"

            node_path.write_text(new_fm + content[end + 4 :], encoding="utf-8")
            applied += 1
        except Exception:
            pass

    queue_path.write_text(
        "# Writeback Queue\n\nProcessed at {}.\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        encoding="utf-8",
    )
    return True, applied
