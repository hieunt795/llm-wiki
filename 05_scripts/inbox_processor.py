#!/usr/bin/env python3
"""
inbox_processor.py — Process inbox files: detect, classify, extract, stage
=========================================================================
Monitors 02_sources/inbox/ for new files (PDF, docx, txt, epub).
Classifies files into book folders (bindseil/, perry/, corb/, etc.).
Extracts markdown from PDFs.
Stages extracted sections for review + ingest.

USAGE:
  python 05_scripts/inbox_processor.py --scan              # List inbox files (with suggestions)
  python 05_scripts/inbox_processor.py --process <book>    # Process files → <book> folder
  python 05_scripts/inbox_processor.py --auto              # Auto-classify + extract all
  python 05_scripts/inbox_processor.py --help              # Show classification rules
"""

import sys
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import os
import re
import argparse
import subprocess
import json
from pathlib import Path
from datetime import datetime
from collections import Counter

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT = SCRIPT_DIR.parent
INBOX_DIR = WIKI_ROOT / "02_sources" / "inbox"
RAW_DIR = WIKI_ROOT / "02_sources"
CONFIG_PATH = WIKI_ROOT / ".cache" / "inbox_config.json"

# Known book folders + author keywords (for auto-classify)
BOOK_FOLDERS = {
    "bindseil": ["bindseil", "monetary policy"],
    "perry": ["perry", "monetary macroeconomics"],
    "corb": ["corb", "central banking"],
    "schofield": ["schofield", "monetary transmission"],
    "choudhry": ["choudhry", "bond market", "fixed income"],
    "tuckman": ["tuckman", "fixed income"],
    "wilmott": ["wilmott", "derivatives", "financial engineering"],
    "singh": ["singh", "repo", "collateral", "liquidity"],
    "homer_liebowitz": ["homer", "liebowitz", "bond portfolio", "duration"],
    "during": ["during", "fixed income during"],
}

def _detect_file_type(path: Path) -> str:
    """Detect file type. Returns: pdf, docx, txt, epub, md, unknown"""
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return "pdf"
    elif suffix in (".docx", ".doc"):
        return "docx"
    elif suffix in (".txt", ".text"):
        return "txt"
    elif suffix == ".epub":
        return "epub"
    elif suffix == ".md":
        return "md"
    return "unknown"

def _is_clipping(filename: str) -> bool:
    """Detect if filename contains 'clip' marker."""
    filename_lower = filename.lower()
    clipping_keywords = ["_clip", "-clip", "_excerpt", "_snippet"]
    for keyword in clipping_keywords:
        if keyword in filename_lower:
            return True
    return False

def _list_inbox_files(verbose=True) -> dict:
    """Scan inbox folder. Return: {file_type: [files]}"""
    if not INBOX_DIR.exists():
        if verbose:
            print(f"  Inbox not found: {INBOX_DIR}")
        return {}

    files_by_type = {}
    for fp in sorted(INBOX_DIR.glob("*")):
        if fp.is_file() and not fp.name.startswith("."):
            ftype = _detect_file_type(fp)
            if ftype == "unknown":
                continue
            if ftype not in files_by_type:
                files_by_type[ftype] = []
            files_by_type[ftype].append(fp)

    if verbose:
        if not files_by_type:
            print("  [Inbox empty]")
        else:
            total = sum(len(v) for v in files_by_type.values())
            print(f"  Found {total} files in inbox:")
            for ftype, files in sorted(files_by_type.items()):
                print(f"    {ftype}: {len(files)} file(s)")
                for fp in files:
                    print(f"      {fp.name}")
            print()
            print("  Use: python librarian.py inbox --process <book|clipping>")
            print("  Or:  python librarian.py inbox --list-books")

    return files_by_type

def step_scan_inbox():
    """Scan and report inbox contents."""
    files = _list_inbox_files(verbose=True)
    total = sum(len(v) for v in files.values())
    return True, f"{total} files ready for processing"

def step_process_inbox(target_book: str | None = None):
    """
    Process inbox files:
    - Extract PDFs → markdown
    - Move/classify files to book folders

    target_book: required, move all files to this book folder (or 'clipping')
    """
    if not target_book:
        print("ERROR: --process requires a target folder (book or clipping)")
        print("Use: python librarian.py inbox --process <book|clipping>")
        print("Or:  python librarian.py inbox --list-books")
        return False, "target_book required"

    files = _list_inbox_files(verbose=False)
    if not files:
        return True, "Inbox empty"

    processed = []
    errors = []

    for ftype, file_list in files.items():
        for fp in file_list:
            dest_book = target_book

            dest_folder = RAW_DIR / dest_book
            dest_folder.mkdir(exist_ok=True)

            # Process based on file type
            if ftype == "pdf":
                # Extract PDF → markdown
                dest_md = dest_folder / (fp.stem + ".md")
                if dest_md.exists():
                    errors.append(f"{fp.name}: {dest_md.name} already exists, skipped")
                    continue

                # Call extract_pdf.py
                try:
                    result = subprocess.run(
                        [sys.executable, str(SCRIPT_DIR / "extract_pdf.py"),
                         "--file", str(fp), "--output", str(dest_md)],
                        capture_output=True, text=True, timeout=120
                    )
                    if result.returncode == 0:
                        fp.unlink()  # delete from inbox after success
                        processed.append(f"{fp.name} → {dest_book}/{dest_md.name}")
                    else:
                        errors.append(f"{fp.name}: extraction failed")
                except Exception as e:
                    errors.append(f"{fp.name}: {str(e)[:60]}")

            elif ftype == "md":
                # Move markdown directly
                dest_md = dest_folder / fp.name
                if dest_md.exists():
                    errors.append(f"{fp.name}: already exists in {dest_book}, skipped")
                    continue
                try:
                    fp.rename(dest_md)
                    processed.append(f"{fp.name} → {dest_book}/{fp.name}")
                except Exception as e:
                    errors.append(f"{fp.name}: move failed ({str(e)[:40]})")

            else:
                # docx, txt, epub — not yet supported
                errors.append(f"{fp.name}: {ftype} format not yet supported")

    msg = f"Processed {len(processed)}"
    if errors:
        msg += f" | {len(errors)} errors"

    if processed:
        print()
        for p in processed:
            print(f"    {p}")
    if errors:
        print()
        for e in errors[:10]:
            print(f"    [WARN] {e}")
        if len(errors) > 10:
            print(f"    ... ({len(errors) - 10} more errors)")

    return True, msg

def main():
    parser = argparse.ArgumentParser(
        description="inbox_processor.py — manage inbox, classify, extract, stage"
    )
    parser.add_argument("--scan",    action="store_true", help="List inbox files with suggestions")
    parser.add_argument("--process", default=None,       help="Process inbox → <book> folder")
    parser.add_argument("--auto",    action="store_true", help="Auto-classify + process all")
    parser.add_argument("--list-books", action="store_true", help="Show known book folders")
    parser.add_argument("--help-classify", action="store_true", help="Show classification rules")

    args = parser.parse_args()

    if args.list_books:
        print("Known book folders (for classification):")
        for book in sorted(BOOK_FOLDERS.keys()):
            print(f"  {book}")
        return

    if args.help_classify:
        print("Classification rules (by filename keyword):")
        for book, keywords in sorted(BOOK_FOLDERS.items()):
            print(f"  {book}: {', '.join(keywords)}")
        print("\nUse: python librarian.py inbox --process <book>  (manual classify)")
        print("Or:  python librarian.py inbox --auto           (auto-classify by keywords)")
        return

    if args.scan:
        step_scan_inbox()
    elif args.process:
        step_process_inbox(target_book=args.process, auto_classify=False)
    elif args.auto:
        step_process_inbox(target_book=None, auto_classify=True)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
