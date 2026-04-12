import pymupdf, os, re

d = r'e:\Wiki Link\01_Raw_Sources\books\fixed_income_during'
files = sorted([f for f in os.listdir(d) if f.endswith('.pdf')], key=lambda x: int(x.split('-')[-1].replace('.pdf','')))
for f in files:
    doc = pymupdf.open(os.path.join(d, f))
    first_text = doc[0].get_text()[:300].replace('\n',' ').strip()
    ch = re.search(r'CHAPTER\s*(\d+)', first_text)
    ch_str = f'Ch.{ch.group(1)}' if ch else '---'
    idx = f.split('-')[-1].replace('.pdf','')
    print(f'File-{idx:>3s} | {len(doc):3d}p | {ch_str:8s} | {first_text[:80]}')
    doc.close()
