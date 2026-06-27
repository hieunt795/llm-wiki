# -*- coding: utf-8 -*-
"""
cleanup_books.py - Dọn dẹp folder 02_sources/books
====================================================
Thực hiện:
  1. Xóa .md duplicate (giữ bản khớp tên PDF với frontmatter chuẩn)
  2. Xóa _original PDFs
  3. Move Bondistan_Tourist_Guide vào subfolder riêng

USAGE:
  cd "E:\\Wiki Link"
  python 05_scripts/cleanup_books.py --dry-run   # Preview trước
  python 05_scripts/cleanup_books.py              # Thực thi thật
"""

import sys
import shutil
import argparse
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT  = SCRIPT_DIR.parent
BOOKS_DIR  = WIKI_ROOT / "02_sources" / "books"

def log(msg): print(msg, flush=True)

def delete(path: Path, dry_run: bool):
    if not path.exists():
        log(f"  [SKIP]  not found: {path.relative_to(WIKI_ROOT)}")
        return
    if dry_run:
        log(f"  [DRY DELETE] {path.relative_to(WIKI_ROOT)}")
    else:
        path.unlink()
        log(f"  [DELETED]    {path.relative_to(WIKI_ROOT)}")

def move(src: Path, dst: Path, dry_run: bool):
    if not src.exists():
        log(f"  [SKIP]  not found: {src.relative_to(WIKI_ROOT)}")
        return
    if dry_run:
        log(f"  [DRY MOVE] {src.relative_to(WIKI_ROOT)} -> {dst.relative_to(WIKI_ROOT)}")
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        log(f"  [MOVED]    {src.relative_to(WIKI_ROOT)} -> {dst.relative_to(WIKI_ROOT)}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Preview only, no changes")
    args = parser.parse_args()
    dry = args.dry_run

    if dry:
        log("=== DRY RUN — no files will be changed ===\n")
    else:
        log("=== CLEANUP books/ — executing changes ===\n")

    # ── 1. Delete duplicate .md ────────────────────────────────────────────────
    log("--- Step 1: Delete duplicate .md files ---")

    # neftci: keep Neftci_Principles_of_Financial_Engineering.md (matches PDF)
    neftci = BOOKS_DIR / "neftci_principles"
    delete(neftci / "Neftci_Principles.md", dry)
    delete(neftci / "Principles_of_Financial_Engineering_Neftci.md", dry)
    log(f"  [KEEP]  neftci_principles/Neftci_Principles_of_Financial_Engineering.md")

    # howard_corb: keep Howard_Corb_Interest_Rate_Swaps.md (matches PDF)
    howard = BOOKS_DIR / "howard_corb_swaps"
    delete(howard / "Howard_Corb_Swaps.md", dry)
    log(f"  [KEEP]  howard_corb_swaps/Howard_Corb_Interest_Rate_Swaps.md")

    # tuckman: keep Tuckman_Serrat_Fixed_Income_2022.md (matches PDF)
    tuckman = BOOKS_DIR / "tuckman_serrat_fixed_income"
    delete(tuckman / "Tuckman_Serrat_2022.md", dry)
    log(f"  [KEEP]  tuckman_serrat_fixed_income/Tuckman_Serrat_Fixed_Income_2022.md")

    # ── 2. Delete _original PDFs ───────────────────────────────────────────────
    log("\n--- Step 2: Delete _original PDFs ---")
    delete(BOOKS_DIR / "central_bank_balance_sheet" / "understanding_CB_balance_sheet_original.pdf", dry)
    delete(BOOKS_DIR / "imf_wb_govt_bond_markets" / "IMF_Developing_GB_Market_original.pdf", dry)
    delete(BOOKS_DIR / "duffie_bpea_payments_2026" / "duffie_bpea_payments_original.pdf", dry)

    # ── 3. Move Bondistan into subfolder ──────────────────────────────────────
    log("\n--- Step 3: Move Bondistan_Tourist_Guide into subfolder ---")
    bondistan_dir = BOOKS_DIR / "bondistan_tourist_guide"
    move(BOOKS_DIR / "Bondistan_Tourist_Guide.pdf", bondistan_dir / "Bondistan_Tourist_Guide.pdf", dry)
    move(BOOKS_DIR / "Bondistan_Tourist_Guide.md",  bondistan_dir / "Bondistan_Tourist_Guide.md",  dry)

    # ── Summary ───────────────────────────────────────────────────────────────
    log("\n=== Summary ===")
    log(f"  Deleted .md duplicates : 3 files (Neftci x2, Howard_Corb x1, Tuckman x1 = 4 total)")
    log(f"  Deleted _original PDFs : 3 files")
    log(f"  Moved Bondistan        : 2 files -> bondistan_tourist_guide/")
    if dry:
        log("\n  [DRY RUN] Run without --dry-run to apply changes.")
    else:
        log("\n  Done! Run: python 05_scripts/extract_pdf.py --all --force  (to re-extract)")


if __name__ == "__main__":
    main()
