#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
organize_nodes.py - inspect and organize Wiki Link node folders.

Default mode is report-only. Use --apply to move misplaced nodes and, when
requested, apply mechanical whitespace cleanup.
"""

import argparse
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT = SCRIPT_DIR.parent.parent
WIKI_DIR = WIKI_ROOT / "03_wiki"

TYPE_TO_FOLDER = {
    "concept": "concepts",
    "mechanism": "mechanisms",
    "evidence": "evidence",
    "contradiction": "contradictions",
    "perspective": "perspectives",
    "relationship": "relationships",
    "synthesis": "syntheses",
    "definition": "definitions",
    "convention": "conventions",
    "domain": "domains",
    "glossary": "glossary",
}

REQUIRED_FIELDS = ("title", "type", "status", "confidence", "thesis")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(WIKI_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def split_frontmatter(text: str) -> tuple[dict, str, bool]:
    if not text.startswith("---"):
        return {}, text, False
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text, False
    raw = text[3:end]
    body = text[end + 4 :]
    try:
        return yaml.safe_load(raw) or {}, body, True
    except Exception:
        return {}, body, False


def clean_text(text: str) -> tuple[str, list[str]]:
    original = text
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = text.rstrip() + "\n"

    changes = []
    if text != original:
        if any(line.rstrip() != line for line in original.splitlines()):
            changes.append("trailing whitespace")
        if re.search(r"\n{4,}", original):
            changes.append("excess blank lines")
        if not original.endswith("\n"):
            changes.append("missing final newline")
    return text, changes


def current_wiki_folder(path: Path) -> str | None:
    try:
        parts = path.relative_to(WIKI_DIR).parts
    except ValueError:
        return None
    return parts[0] if len(parts) > 1 else ""


def iter_markdown(root: Path) -> list[Path]:
    return [
        fp
        for fp in sorted(root.rglob("*.md"))
        if not fp.name.startswith(".") and fp.name != "_index.md"
    ]


def inspect_file(fp: Path, duplicate_stems: set[str]) -> dict:
    text = fp.read_text(encoding="utf-8", errors="ignore")
    fm, body, has_valid_fm = split_frontmatter(text)
    cleaned, whitespace_changes = clean_text(text)

    issues = []
    actions = []

    if not has_valid_fm:
        issues.append("missing/invalid frontmatter")
    else:
        missing = [k for k in REQUIRED_FIELDS if not str(fm.get(k, "")).strip()]
        if missing:
            issues.append("missing fields: " + ", ".join(missing))

        thesis = str(fm.get("thesis", "")).strip()
        if len(thesis) < 20:
            issues.append("thin thesis")

        node_type = str(fm.get("type", "")).strip().lower()
        expected_folder = TYPE_TO_FOLDER.get(node_type)
        current_folder = current_wiki_folder(fp)
        if expected_folder and current_folder and current_folder != expected_folder:
            dst = WIKI_DIR / expected_folder / fp.name
            actions.append(("move", dst))
        elif node_type and node_type not in TYPE_TO_FOLDER:
            issues.append("unknown type: " + node_type)

    if whitespace_changes:
        actions.append(("fix_whitespace", cleaned))

    if fp.stem in duplicate_stems:
        issues.append("duplicate stem across wiki folders")

    return {
        "path": fp,
        "issues": issues,
        "actions": actions,
        "frontmatter": fm,
        "body_len": len(body.strip()),
    }


def apply_actions(report: dict, apply: bool, move_nodes: bool, fix_whitespace: bool) -> list[str]:
    fp = report["path"]
    done = []

    for kind, payload in report["actions"]:
        if kind == "fix_whitespace" and fix_whitespace:
            if apply:
                fp.write_text(payload, encoding="utf-8")
                done.append("fixed whitespace")
            else:
                done.append("would fix whitespace")

        if kind == "move" and move_nodes:
            dst = payload
            if dst.exists() and dst.resolve() != fp.resolve():
                done.append("cannot move: target exists " + rel(dst))
                continue
            if apply:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(fp), str(dst))
                done.append("moved -> " + rel(dst))
            else:
                done.append("would move -> " + rel(dst))

    return done


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect and organize Wiki Link node folders.")
    parser.add_argument("--dir", default="03_wiki", help="Directory to inspect (default: 03_wiki)")
    parser.add_argument("--apply", action="store_true", help="Apply moves/fixes. Default is report-only.")
    parser.add_argument("--no-move", action="store_true", help="Do not move misplaced nodes.")
    parser.add_argument("--fix-whitespace", action="store_true", help="Also normalize trailing whitespace/blank lines.")
    parser.add_argument("--limit", type=int, default=80, help="Max detailed rows to print.")
    args = parser.parse_args()

    root = Path(args.dir)
    if not root.is_absolute():
        root = WIKI_ROOT / root
    if not root.exists():
        print("ERROR: directory not found: {}".format(root))
        return 1

    files = iter_markdown(root)
    stems = Counter(fp.stem for fp in iter_markdown(WIKI_DIR))
    duplicate_stems = {stem for stem, count in stems.items() if count > 1}

    print("[organize_nodes] dir={} files={} mode={}".format(
        rel(root), len(files), "APPLY" if args.apply else "DRY-RUN"
    ))

    reports = [inspect_file(fp, duplicate_stems) for fp in files]
    visible_reports = []
    issue_count = 0
    move_count = 0
    whitespace_count = 0

    for rep in reports:
        actions = rep["actions"]
        issue_count += len(rep["issues"])
        has_move = any(kind == "move" for kind, _ in actions)
        has_whitespace = any(kind == "fix_whitespace" for kind, _ in actions)
        move_count += 1 if has_move else 0
        whitespace_count += 1 if has_whitespace else 0
        visible_move = has_move and not args.no_move
        if rep["issues"] or visible_move or (args.fix_whitespace and has_whitespace):
            visible_reports.append(rep)

    for rep in visible_reports[: args.limit]:
        print("\n- {}".format(rel(rep["path"])))
        for issue in rep["issues"]:
            print("  ISSUE: {}".format(issue))
        done = apply_actions(
            rep,
            apply=args.apply,
            move_nodes=not args.no_move,
            fix_whitespace=args.fix_whitespace,
        )
        for item in done:
            print("  ACTION: {}".format(item))

    if len(visible_reports) > args.limit:
        print("\n... {} more files omitted by --limit".format(len(visible_reports) - args.limit))

    print("\nSUMMARY: files={} flagged={} issues={} move_candidates={} whitespace_candidates={}".format(
        len(files), len(visible_reports), issue_count, move_count, whitespace_count
    ))

    if not args.apply:
        print("DRY-RUN: rerun with --apply to write changes.")
    if whitespace_count and not args.fix_whitespace:
        print("NOTE: whitespace candidates are reported but not fixed unless --fix-whitespace is set.")

    return 0


if __name__ == "__main__":
    sys.exit(main())

