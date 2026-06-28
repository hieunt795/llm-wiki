import re
import os
from pathlib import Path
import argparse

# Refined regex for Perry's book
RE_CHAPTER = re.compile(r'^Chapter\s+(\d+)$', re.IGNORECASE)
RE_SECTION = re.compile(r'^(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?)\.?\s+[A-Z]')

def extract_from_file(file_path, target_num, target_is_chapter, target_full):
    content = file_path.read_text(encoding='utf-8')
    lines = content.splitlines()
    
    blocks = []
    current_block = []
    in_target = False
    
    for i, line in enumerate(lines):
        line_s = line.strip()
        if not line_s:
            if in_target: current_block.append(line)
            continue
        
        line_lower = line_s.lower()
        is_ch = RE_CHAPTER.match(line_s)
        is_sec = RE_SECTION.match(line_s)
        
        if is_sec and ('doi:' in line_lower or len(line_s) > 100):
            is_sec = None
            
        current_num = ""
        if is_ch: current_num = is_ch.group(1)
        elif is_sec: current_num = is_sec.group(1)

        # START condition
        if not in_target:
            found_start = False
            if target_is_chapter:
                if is_ch and current_num == target_num: found_start = True
            else:
                if is_sec and current_num == target_num: found_start = True
                elif target_full in line_lower and (is_ch or is_sec): found_start = True
            
            if found_start:
                in_target = True
                current_block = [line]
                continue
        
        # END condition
        if in_target:
            if is_ch or is_sec:
                if target_is_chapter and is_ch and current_num != target_num:
                    blocks.append("\n".join(current_block))
                    in_target = False
                    current_block = []
                elif not target_is_chapter and (is_ch or (is_sec and current_num != target_num)):
                    blocks.append("\n".join(current_block))
                    in_target = False
                    current_block = []
            
            if in_target:
                current_block.append(line)
                
    if in_target and current_block:
        blocks.append("\n".join(current_block))
        
    return blocks

def extract_section(book_dir, target_heading):
    book_path = Path(book_dir)
    md_files = sorted(list(book_path.glob("*.md")))
    
    target = target_heading.strip().lower()
    target_num = ""
    target_is_chapter = "chapter" in target
    
    if target_is_chapter:
        m = re.search(r'chapter\s+(\d+)', target)
        if m: target_num = m.group(1)
    else:
        m = re.search(r'(\d+\.\d+(?:\.\d+)?)', target)
        if m: target_num = m.group(1)

    all_blocks = []
    for f in md_files:
        blocks = extract_from_file(f, target_num, target_is_chapter, target)
        all_blocks.extend(blocks)
    
    if not all_blocks:
        return None
    
    # Heuristic: The block with the most text is likely the actual content, not the TOC entry
    best_block = max(all_blocks, key=len)
    return best_block

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=True)
    parser.add_argument("--heading", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    
    text = extract_section(args.dir, args.heading)
    if text:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text, encoding='utf-8')
        print(f"Extracted: {args.heading} -> {args.out} ({len(text)} chars)")
    else:
        print(f"FAILED to find heading: {args.heading}")

if __name__ == "__main__":
    main()
