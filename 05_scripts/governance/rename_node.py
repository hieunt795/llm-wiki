"""
rename_node.py — Safe wiki node renamer
=======================================
Đổi tên một wiki node và tự động heal toàn bộ [[OldName]] → [[NewName]] 
trong tất cả files trong 03_wiki/.

Usage:
  python rename_node.py OldNodeName NewNodeName
  python rename_node.py OldNodeName NewNodeName --dry-run
"""

import sys
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import re
import shutil
import argparse
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT  = SCRIPT_DIR.parent.parent
WIKI_DIR   = WIKI_ROOT / "03_wiki"


def find_node_file(name):
    """Tìm file .md theo stem name trong toàn bộ 03_wiki/."""
    for fp in WIKI_DIR.rglob("*.md"):
        if fp.stem == name:
            return fp
    return None


def heal_links(old_name, new_name, dry_run=False):
    """Search-replace [[OldName]] → [[NewName]] trong toàn bộ wiki."""
    pattern = re.compile(r'\[\[' + re.escape(old_name) + r'(\|[^\]]+)?\]\]')
    changed_files = []

    for fp in WIKI_DIR.rglob("*.md"):
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if old_name not in text:
            continue

        def replace_link(m):
            alias = m.group(1) or ""
            return "[[{}{}]]".format(new_name, alias)

        new_text = pattern.sub(replace_link, text)
        if new_text != text:
            changed_files.append(fp)
            if not dry_run:
                fp.write_text(new_text, encoding="utf-8")

    return changed_files


def main():
    parser = argparse.ArgumentParser(description="Safe wiki node renamer")
    parser.add_argument("old_name", help="Current node stem name (no .md)")
    parser.add_argument("new_name", help="New node stem name (no .md)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without writing")
    args = parser.parse_args()

    old_name = args.old_name.strip()
    new_name = args.new_name.strip()
    dry_run  = args.dry_run

    if old_name == new_name:
        print("ERROR: old and new names are identical.")
        sys.exit(1)

    # 1. Tìm file gốc
    src = find_node_file(old_name)
    if not src:
        print("ERROR: Node '{}' not found in 03_wiki/".format(old_name))
        sys.exit(1)

    dst = src.parent / (new_name + ".md")
    if dst.exists():
        print("ERROR: '{}' already exists at {}".format(new_name, dst))
        sys.exit(1)

    print("\nRENAME NODE")
    print("  {} → {}".format(old_name, new_name))
    print("  File: {} → {}".format(src.name, dst.name))
    if dry_run:
        print("  [DRY RUN — no changes written]\n")

    # 2. Heal links trước khi đổi tên file
    changed = heal_links(old_name, new_name, dry_run=dry_run)
    print("  Wikilinks healed in {} file(s):".format(len(changed)))
    for fp in changed[:8]:
        print("    {}".format(fp.relative_to(WIKI_ROOT)))
    if len(changed) > 8:
        print("    ... and {} more".format(len(changed) - 8))

    # 3. Đổi tên file
    if not dry_run:
        src.rename(dst)
        print("  File renamed: OK")

        # 4. Cập nhật title trong frontmatter nếu khớp với old_name
        try:
            text = dst.read_text(encoding="utf-8")
            updated = re.sub(
                r'^(title:\s*["\']?)' + re.escape(old_name) + r'(["\']?\s*$)',
                r'\g<1>' + new_name + r'\g<2>',
                text, flags=re.MULTILINE
            )
            if updated != text:
                dst.write_text(updated, encoding="utf-8")
                print("  Frontmatter title updated: OK")
        except Exception as e:
            print("  WARNING: could not update frontmatter title: {}".format(e))
    else:
        print("  [DRY RUN] Would rename file and update frontmatter.")

    print("\nDone. Run 'python librarian.py sync' to rebuild graph + index.\n")


if __name__ == "__main__":
    main()

