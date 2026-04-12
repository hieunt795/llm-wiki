import pymupdf
import sys
import os

def extract_pdf_to_md(pdf_path, output_md):
    doc = pymupdf.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        # sorting blocks vertically
        blocks.sort(key=lambda b: (b[1], b[0]))
        text += f"\n\n--- [PAGE {page_num + 1}] ---\n\n"
        for b in blocks:
            text += b[4] + "\n"
            
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Extracted {len(doc)} pages to {output_md}")
    doc.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        pass
    else:
        extract_pdf_to_md(sys.argv[1], sys.argv[2])
