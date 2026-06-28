import os
import random
import re
import pathlib
import argparse
import sys
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from collections import defaultdict

def read_file_safe(file_path):
    try:
        try:
            return file_path.read_text(encoding='utf-8', errors='ignore')
        except UnicodeDecodeError:
            return file_path.read_text(encoding='utf-16', errors='ignore')
    except:
        return ""

def get_source_clusters():
    raw_dir = pathlib.Path('02_sources')
    all_files = list(raw_dir.rglob('*.md'))
    
    clusters = defaultdict(list)
    
    for f in all_files:
        # Xác định "ID" của nguồn
        # Nếu nằm trong thư mục con của 'books', ID là tên thư mục đó (cụm sách)
        # Nếu là file lẻ trong Clipping hoặc deep-research, ID là tên file
        parts = f.relative_to(raw_dir).parts
        if len(parts) > 1 and parts[0] == 'books':
            cluster_id = f"BOOK: {parts[1]}"
        else:
            cluster_id = f"FILE: {f.name}"
            
        clusters[cluster_id].append(f)
    
    return clusters

def scout_words(num=20):
    clusters = get_source_clusters()
    if not clusters:
        print("Error: No .md files found.")
        return

    cluster_ids = list(clusters.keys())
    selected_words = []
    stop_words = {'the', 'this', 'that', 'with', 'from', 'which', 'their', 'there', 'these', 'would', 'should', 'could', 'because', 'however'}
    
    attempts = 0
    while len(selected_words) < num and attempts < num * 20:
        attempts += 1
        # BƯỚC 1: Chọn cụm nguồn ngẫu nhiên (Mỗi quyển sách/bài báo có 1 phiếu bầu)
        cid = random.choice(cluster_ids)
        # BƯỚC 2: Chọn 1 file ngẫu nhiên trong cụm đó
        f = random.choice(clusters[cid])
        
        content = read_file_safe(f)
        words = re.findall(r'\b[A-Za-z]{7,25}\b', content)
        valid_words = [w for w in words if w.lower() not in stop_words]
        
        if valid_words:
            word = random.choice(valid_words)
            # Hiển thị tên cụm thay vì tên file lẻ để người dùng biết nguồn gốc
            selected_words.append((cid, word))
    
    print(f"\n=== RAW SCOUT v4.0: {len(selected_words)} RANDOM TERMS (Fair Clustering) ===")
    for i, (src, word) in enumerate(selected_words, 1):
        print(f"{i:2d}. {word:25s} [Source: {src}]")

def scout_lines(num=10):
    clusters = get_source_clusters()
    if not clusters:
        print("Error: No .md files found.")
        return

    cluster_ids = list(clusters.keys())
    selected_lines = []
    attempts = 0
    
    while len(selected_lines) < num and attempts < num * 20:
        attempts += 1
        cid = random.choice(cluster_ids)
        f = random.choice(clusters[cid])
        
        content = read_file_safe(f)
        lines = [l.strip() for l in content.splitlines() if len(l.strip()) > 90 and not l.startswith('#') and not l.startswith('!')]
        
        if lines:
            line = random.choice(lines)
            selected_lines.append((cid, line))
        
    print(f"\n=== RAW SCOUT v4.0: {len(selected_lines)} RANDOM LINES (Fair Clustering) ===")
    for i, (src, line) in enumerate(selected_lines, 1):
        display_line = (line[:120] + '...') if len(line) > 120 else line
        print(f"{i:2d}. [{src}]")
        print(f"    > {display_line}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Raw Scout v4.0 - Fair clustering random inspiration")
    parser.add_argument("--mode", choices=['words', 'lines'], default='lines', help="Choose to scout words or lines")
    parser.add_argument("--n", type=int, default=10, help="Number of items to return")
    args = parser.parse_args()
    
    if args.mode == 'words':
        scout_words(args.n if args.n != 10 else 20)
    else:
        scout_lines(args.n)
