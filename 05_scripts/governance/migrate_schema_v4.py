#!/usr/bin/env python3
"""
migrate_schema_v4.py
Normalize legacy 03_wiki frontmatter into the current schema used by the repo.

This is a deterministic migration:
- adds missing frontmatter when absent
- maps legacy statuses/confidence labels
- infers type from folder when absent
- adds half_life_years, superseded_by, superseded_date, aliases, tags, source_refs
- preserves existing body content
"""

from __future__ import annotations

import re
import sys
import io
from pathlib import Path
from datetime import datetime
from collections import OrderedDict
import yaml

if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT = SCRIPT_DIR.parent.parent
WIKI_DIR = WIKI_ROOT / "03_wiki"

FOLDER_TYPE_MAP = {
    "concepts": "concept",
    "definitions": "definition",
    "mechanisms": "mechanism",
    "relationships": "relationship",
    "conventions": "convention",
    "perspectives": "perspective",
    "evidence": "evidence",
    "domains": "domain",
    "glossary": "glossary",
    "contradictions": "contradiction",
    "syntheses": "synthesis",
}

STATUS_MAP = {
    "active": "verified",
    "deprecated": "archived",
    "researching": "draft",
}

CONFIDENCE_MAP = {
    "low": 2,
    "medium": 3,
    "high": 4,
    "very low": 1,
    "very_low": 1,
    "verified": 5,
}

HALF_LIFE_BY_TYPE = {
    "mechanism": 10,
    "definition": 10,
    "concept": 10,
    "relationship": 10,
    "convention": 10,
    "perspective": 5,
    "evidence": 1,
    "domain": 1,
    "glossary": 10,
    "contradiction": 1,
    "synthesis": 0.5,
}


def split_frontmatter(text: str):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm_text = text[4:end] if text.startswith("---\n") else text[3:end]
            body = text[end + 4 :].lstrip("\r\n")
            return fm_text, body
    return None, text


def safe_load_fm(fm_text: str):
    if not fm_text:
        return {}
    try:
        data = yaml.safe_load(fm_text) or {}
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def first_heading_or_stem(fp: Path, body: str) -> str:
    m = re.search(r"^#\s+(.+?)\s*$", body, flags=re.MULTILINE)
    if m:
        return m.group(1).strip()
    return fp.stem.replace("_", " ")


def extract_thesis(body: str) -> str:
    lines = body.splitlines()
    in_thesis = False
    collected = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^##\s+Thesis\b", stripped, flags=re.IGNORECASE):
            in_thesis = True
            continue
        if in_thesis and re.match(r"^##\s+", stripped):
            break
        if in_thesis:
            if stripped and not stripped.startswith(("#", "-", ">", "|")):
                collected.append(stripped)
    if collected:
        return " ".join(collected)[:300].strip()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(("#", ">", "-", "|", "```", "---")):
            continue
        return stripped[:300].strip()
    return "TODO: add thesis"


def normalize_confidence(value):
    if value is None or value == "":
        return 1
    if isinstance(value, int):
        return max(1, min(5, value))
    sval = str(value).strip().lower()
    if sval.isdigit():
        return max(1, min(5, int(sval)))
    return CONFIDENCE_MAP.get(sval, 1)


def normalize_status(value):
    if value is None:
        return "draft"
    sval = str(value).strip()
    if not sval:
        return "draft"
    if sval.lower() in {"none", "null", "nan"}:
        return "draft"
    return STATUS_MAP.get(sval, sval)


def normalize_date(value, fallback_ts: float) -> str:
    if value:
        sval = str(value).strip()
        m = re.match(r"^(\d{4})-(\d{1,2})-(\d{1,2})$", sval)
        if m:
            return f"{int(m.group(1)):04d}-{int(m.group(2)):02d}-{int(m.group(3)):02d}"
    return datetime.fromtimestamp(fallback_ts).strftime("%Y-%m-%d")


def normalize_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def normalize_source_refs(value):
    if not value:
        return []
    if isinstance(value, list):
        return value
    return []


def build_frontmatter(fp: Path, fm: dict, body: str) -> OrderedDict:
    node_type = fm.get("type") or FOLDER_TYPE_MAP.get(fp.parent.name, "concept")
    if node_type in {"document", "note", "article"}:
        node_type = FOLDER_TYPE_MAP.get(fp.parent.name, "concept")
    title = str(fm.get("title") or first_heading_or_stem(fp, body)).strip()
    thesis = str(fm.get("thesis") or "").strip() or extract_thesis(body)
    status = normalize_status(fm.get("status"))
    confidence = normalize_confidence(fm.get("confidence"))
    mtime = fp.stat().st_mtime

    new = OrderedDict()
    new["title"] = title
    new["aliases"] = normalize_list(fm.get("aliases"))
    new["type"] = node_type
    new["tags"] = normalize_list(fm.get("tags"))
    new["status"] = status
    new["confidence"] = confidence
    new["half_life_years"] = fm.get("half_life_years", HALF_LIFE_BY_TYPE.get(node_type, 10))
    new["school"] = fm.get("school", "") if node_type == "perspective" else fm.get("school", "")
    new["superseded_by"] = fm.get("superseded_by", None)
    new["superseded_date"] = fm.get("superseded_date", None)
    if "expert_lens" in fm:
        new["expert_lens"] = fm.get("expert_lens", "")
    else:
        new["expert_lens"] = ""
    new["provenance"] = fm.get("provenance", "legacy_migrated")
    new["thesis"] = thesis
    new["source_refs"] = normalize_source_refs(fm.get("source_refs"))
    new["created"] = normalize_date(fm.get("created"), mtime)
    new["updated"] = normalize_date(fm.get("updated"), mtime)

    passthrough_keys = [
        "chapter", "region", "standard", "author", "source", "related_hubs",
        "node_count", "tension_count",
    ]
    for key in passthrough_keys:
        if key in fm and key not in new:
            new[key] = fm[key]
    return new


def dump_frontmatter(data: OrderedDict) -> str:
    return yaml.safe_dump(dict(data), allow_unicode=True, sort_keys=False).strip()


def migrate_file(fp: Path) -> bool:
    text = fp.read_text(encoding="utf-8", errors="ignore")
    fm_text, body = split_frontmatter(text)
    fm = safe_load_fm(fm_text) if fm_text is not None else {}
    new_fm = build_frontmatter(fp, fm, body)
    new_text = "---\n" + dump_frontmatter(new_fm) + "\n---\n\n" + body.lstrip("\r\n")
    if new_text != text:
        fp.write_text(new_text, encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    total = 0
    for fp in sorted(WIKI_DIR.rglob("*.md")):
        if fp.name.startswith("_"):
            continue
        total += 1
        if migrate_file(fp):
            changed += 1
            print(f"[UPDATED] {fp.relative_to(WIKI_ROOT)}")
    print(f"\nDone. Updated {changed}/{total} files.")


if __name__ == "__main__":
    main()

