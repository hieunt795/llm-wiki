# -*- coding: utf-8 -*-
"""
count_pages.py - Đếm tổng số trang tất cả PDF trong books/
USAGE: python 05_scripts/count_pages.py
"""
import fitz
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
BOOKS_DIR  = SCRIPT_DIR.parent.parent / "02_sources" / "books"

PAGES_PER_SEC = 0.3  # tốc độ đo được từ central_bank_balance_sheet

results = []
total_pages = 0
errors = []

for pdf in sorted(BOOKS_DIR.rglob("*.pdf")):
    try:
        doc = fitz.open(str(pdf))
        pages = len(doc)
        doc.close()
        total_pages += pages
        rel = pdf.relative_to(BOOKS_DIR)
        results.append((str(rel), pages))
    except Exception as e:
        errors.append((pdf.name, str(e)))

# Print per-book summary (group by folder)
current_folder = None
folder_pages = 0

print(f"{'Pages':>6}  File")
print("-" * 70)

for rel, pages in results:
    folder = rel.split("\\")[0] if "\\" in rel else rel.split("/")[0]
    if folder != current_folder:
        if current_folder and folder_pages > 0:
            est = folder_pages / PAGES_PER_SEC
            mins = int(est // 60); secs = int(est % 60)
            print(f"         → subtotal: {folder_pages} pages, ~{mins}m{secs:02d}s\n")
        current_folder = folder
        folder_pages = 0
        print(f"  [{folder}]")
    print(f"{pages:>6}    {rel}")
    folder_pages += pages

# Last folder
if current_folder and folder_pages > 0:
    est = folder_pages / PAGES_PER_SEC
    mins = int(est // 60); secs = int(est % 60)
    print(f"         → subtotal: {folder_pages} pages, ~{mins}m{secs:02d}s")

# Summary
est_total = total_pages / PAGES_PER_SEC
est_mins  = int(est_total // 60)
est_hours = est_mins // 60
est_mins_rem = est_mins % 60

print("\n" + "=" * 70)
print(f"  Total PDFs  : {len(results)}")
print(f"  Total pages : {total_pages:,}")
print(f"  Speed       : {PAGES_PER_SEC} pages/sec (measured on central_bank_balance_sheet)")
print(f"  Est. time   : ~{est_hours}h {est_mins_rem}m (local CPU)")
print(f"  Est. Colab  : ~{int(est_hours*60*0.15 + est_mins_rem*0.15)}m (T4 GPU, ~7x faster)")

if errors:
    print(f"\n  Errors ({len(errors)}):")
    for name, err in errors:
        print(f"    {name}: {err}")
print("=" * 70)

