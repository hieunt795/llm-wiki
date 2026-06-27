import sys
from pathlib import Path
import re
import argparse

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT = SCRIPT_DIR.parent / "03_wiki"
LINK_PATTERN = re.compile(r"\[\[(.*?)\]\]")

def extract_wikilinks(text):
    links = []
    for match in LINK_PATTERN.finditer(text):
        link_target = match.group(1).split("|")[0].split("#")[0].strip()
        links.append(link_target)
    return links

def main():
    if not WIKI_ROOT.exists():
        print(f"Error: {WIKI_ROOT} not found.")
        sys.exit(1)

    nodes = {} # stem -> filepath
    incoming_counts = {} # stem -> count
    outgoing_counts = {} # stem -> count

    # Initialize
    for filepath in WIKI_ROOT.rglob("*.md"):
        if filepath.name.startswith("_") or filepath.name.startswith("."):
            continue
        stem = filepath.stem
        nodes[stem] = filepath
        incoming_counts[stem] = 0
        outgoing_counts[stem] = 0

    # Scan
    for filepath in WIKI_ROOT.rglob("*.md"):
        if filepath.name.startswith("_") or filepath.name.startswith("."):
            continue
        stem = filepath.stem
        try:
            text = filepath.read_text(encoding="utf-8", errors="ignore")
            links = extract_wikilinks(text)
            
            for link in links:
                if link != stem: # ignore self-links
                    outgoing_counts[stem] += 1
                    if link in incoming_counts:
                        incoming_counts[link] += 1
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    # Analyze
    orphans = [stem for stem, count in incoming_counts.items() if count == 0]
    dead_ends = [stem for stem, count in outgoing_counts.items() if count == 0]

    print("="*60)
    print(f"WIKI GRAPH AUDIT: {len(nodes)} total nodes")
    print("="*60)
    
    print(f"\n[ORPHANS] Nodes with NO incoming links ({len(orphans)}):")
    print("These nodes are isolated. No other document points to them.")
    for stem in sorted(orphans):
        print(f"  - {stem}  ({nodes[stem].relative_to(WIKI_ROOT)})")

    print(f"\n[DEAD ENDS] Nodes with NO outgoing links ({len(dead_ends)}):")
    print("These nodes do not connect to any other concepts in the wiki.")
    for stem in sorted(dead_ends):
        print(f"  - {stem}  ({nodes[stem].relative_to(WIKI_ROOT)})")
        
    print("\nRecommendation: Create [[wikilinks]] to connect these nodes to the broader graph.")

if __name__ == "__main__":
    main()
