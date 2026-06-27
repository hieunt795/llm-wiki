# -*- coding: utf-8 -*-
"""
debug_page.py - In tọa độ thực tế của các blocks trên 1 trang PDF
USAGE:
  python 05_scripts/debug_page.py --pdf 02_sources/books/central_bank_balance_sheet/Central_Bank_Balance_Sheet.pdf --page 9
"""
import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT  = SCRIPT_DIR.parent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf",  type=str, required=True)
    parser.add_argument("--page", type=int, default=1, help="Page number (1-based)")
    args = parser.parse_args()

    import fitz
    pdf_path = Path(args.pdf)
    if not pdf_path.is_absolute():
        pdf_path = WIKI_ROOT / pdf_path

    doc = fitz.open(str(pdf_path))
    page = doc[args.page - 1]
    blocks = page.get_text("blocks")

    print(f"Page {args.page} — size: {page.rect.width:.0f} x {page.rect.height:.0f}")
    print(f"Gutter zone: {page.rect.width*0.25:.0f} — {page.rect.width*0.75:.0f}")
    print(f"{'#':<3} {'x0':>5} {'y0':>5} {'x1':>5} {'y1':>5} {'cx':>5}  text")
    print("-" * 90)

    text_blocks = [(b[0], b[1], b[2], b[3], b[4]) for b in blocks if b[6] == 0 and b[4].strip()]
    for i, b in enumerate(text_blocks):
        cx = (b[0] + b[2]) / 2
        snippet = b[4].replace('\n', ' ').strip()[:55]
        print(f"{i:<3} {b[0]:>5.0f} {b[1]:>5.0f} {b[2]:>5.0f} {b[3]:>5.0f} {cx:>5.0f}  {snippet}")

    doc.close()

if __name__ == "__main__":
    main()
