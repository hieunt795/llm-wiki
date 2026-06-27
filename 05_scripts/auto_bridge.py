"""
auto_bridge.py — Auto-Link Orphans to Existing Nodes (v2.0)
Usage:
  python auto_bridge.py --dry-run     # show suggestions without applying
  python auto_bridge.py --force     # auto-apply suggestions
  python auto_bridge.py --report      # just show stats, no changes
  python auto_bridge.py --backup     # create backup before --force
"""
import sys
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import re
import yaml
import argparse
import shutil
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT = SCRIPT_DIR.parent
WIKI_DIR = WIKI_ROOT / "03_wiki"
BACKUP_DIR = WIKI_ROOT / ".backup" / "auto_bridge"

def get_all_nodes():
    """Get all wiki nodes with full metadata"""
    nodes = {}
    
    for fp in WIKI_DIR.rglob("*.md"):
        if fp.name.startswith("."):
            continue
        try:
            content = fp.read_text(encoding="utf-8", errors="ignore")
        except:
            continue
        
        # Extract frontmatter
        title = fp.stem
        aliases = []
        tags = []
        
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                try:
                    fm = yaml.safe_load(content[3:end])
                    title = fm.get("title", fp.stem)
                    aliases = fm.get("aliases", [])
                    tags = fm.get("tags", [])
                except:
                    pass
        
        nodes[fp.stem] = {
            "path": fp,
            "title": title,
            "aliases": aliases if isinstance(aliases, list) else [aliases] if aliases else [],
            "tags": tags if isinstance(tags, list) else [tags] if tags else [],
            "content": content
        }
    
    return nodes

def extract_all_links(content, filter_raw=True):
    """Extract all wikilinks, optionally filtering out raw sources"""
    links = re.findall(r"\[\[(.*?)\]\]", content)
    if not filter_raw:
        return links
        
    # Filter out links that look like raw sources (e.g., perry_8_1, Tuckman_Serrat_2022)
    # Typically raw sources have numbers and underscores, or specific keywords
    filtered = []
    for link in links:
        link_clean = link.split("|")[0].split("#")[0].strip().lower()
        # Pattern: contains digits and underscores, or matches known raw naming conventions
        is_raw = bool(re.search(r'_\d+|_ch\d+|raw|trang-', link_clean))
        if not is_raw:
            filtered.append(link)
    return filtered

def find_related_nodes_v2(target_id, target_node, all_nodes):
    """Find related nodes using multiple strategies"""
    target_title = target_node.get("title", "").lower()
    target_words = set(target_title.replace("_", " ").replace("-", " ").split())
    
    # Get aliases/tags safely (handle type variations)
    target_aliases_raw = target_node.get("aliases", [])
    if isinstance(target_aliases_raw, list):
        target_aliases = set(a.lower() if isinstance(a, str) else str(a).lower() for a in target_aliases_raw)
    else:
        target_aliases = set()
    
    target_tags_raw = target_node.get("tags", [])
    if isinstance(target_tags_raw, list):
        target_tags = set(t.lower() if isinstance(t, str) else str(t).lower() for t in target_tags_raw)
    else:
        target_tags = set()
    
    # Stop words to filter
    stop_words = {"the", "a", "an", "of", "and", "or", "in", "to", "for", "vs", "v", "mechanics", "model", "analysis", "concept", "mechanism"}
    target_words = target_words - stop_words
    
    if not target_words:
        target_words = set(target_id.lower().replace("_", " ").replace("-", " ").split())
    
    matches = []
    
    for node_id, node_data in all_nodes.items():
        if node_id == target_id:
            continue
        
        # Skip if already linked
        existing_links = extract_all_links(target_node.get("content", ""))
        if any(node_id in link for link in existing_links):
            continue
        
        other_title = node_data.get("title", "").lower()
        other_words = set(other_title.replace("_", " ").replace("-", " ").split()) - stop_words
        
        # Get other aliases/tags safely
        other_aliases_raw = node_data.get("aliases", [])
        if isinstance(other_aliases_raw, list):
            other_aliases = set(a.lower() if isinstance(a, str) else str(a).lower() for a in other_aliases_raw)
        else:
            other_aliases = set()
        
        other_tags_raw = node_data.get("tags", [])
        if isinstance(other_tags_raw, list):
            other_tags = set(t.lower() if isinstance(t, str) else str(t).lower() for t in other_tags_raw)
        else:
            other_tags = set()
        
        # Strategy 1: Title word overlap
        title_overlap = len(target_words & other_words)
        
        # Strategy 2: Alias overlap
        alias_overlap = len(target_aliases & other_aliases) * 3
        
        # Strategy 3: Tag overlap
        tag_overlap = len(target_tags & other_tags) * 2
        
        # Strategy 4: One word containment
        containment = 0
        for tw in target_words:
            if len(tw) > 3 and tw in other_title:
                containment += 1
        
        # Calculate total score
        score = title_overlap + alias_overlap + tag_overlap + containment
        
        # Only return if score >= 1 AND not self-reference
        if score >= 1 and node_id != target_id:
            matches.append((score, node_id, node_data))
    
    # Sort by score descending, return top 3
    matches.sort(key=lambda x: -x[0])
    return matches[:3]

def analyze_graph(nodes):
    """Analyze graph and return statistics"""
    incoming = defaultdict(int)
    outgoing = defaultdict(int)
    link_pattern = re.compile(r"\[\[(.*?)\]\]")
    
    for stem, node_data in nodes.items():
        links = extract_all_links(node_data["content"], filter_raw=True)
        outgoing[stem] = len(links)
        for link in links:
            target = link.split("|")[0].split("#")[0].strip()
            if target in nodes:
                incoming[target] += 1
    
    # FIXED: Check ALL nodes, not just nodes in incoming
    # A node is orphan if NO other node links TO it
    orphans = [stem for stem in nodes if incoming.get(stem, 0) == 0]
    dead_ends = [stem for stem in nodes if outgoing.get(stem, 0) == 0]
    islands = [s for s in orphans if s in dead_ends]
    
    return {
        "total": len(nodes),
        "orphans": orphans,
        "dead_ends": dead_ends,
        "islands": islands
    }

def build_bridge_suggestions_v2(nodes, min_score=1):
    """Build bridge suggestions with improved logic"""
    stats = analyze_graph(nodes)
    orphans = stats["orphans"]
    
    # Only focus on true orphans (no incoming links)
    suggestions = []
    
    for stem in orphans:
        node_data = nodes.get(stem)
        if not node_data:
            continue
        
        related = find_related_nodes_v2(stem, node_data, nodes)
        
        if related:
            suggestions.append({
                "target": stem,
                "target_title": node_data.get("title", stem),
                "suggestions": related[:2]  # Max 2 suggestions per node
            })
    
    return suggestions

def apply_bridges_v2(suggestions, nodes, dry_run=True, create_backup=False):
    """Apply bridge suggestions with backup"""
    count = 0
    applied = []
    
    if create_backup and not dry_run:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = BACKUP_DIR / f"orphans_bridged_{ts}.txt"
        with open(backup_file, "w", encoding="utf-8") as f:
            f.write(f"# Auto-Bridge Applied: {datetime.now()}\n")
            f.write(f"# Total suggestions: {len(suggestions)}\n\n")
            for s in suggestions:
                f.write(f"- {s['target']} -> {[r[1] for r in s['suggestions']]}\n")
        print(f"[Backup saved to: {backup_file}]")
    
    for suggestion in suggestions:
        target = suggestion["target"]
        node_data = nodes.get(target)
        
        if not node_data:
            continue
        
        content = node_data["content"]
        original_content = content
        
        # Check if Related section exists
        if "## Related" not in content:
            content += "\n\n## Related\n\n"
        
        # Add links (filter duplicates)
        new_links = []
        for score, related_id, _ in suggestion["suggestions"]:
            link = f"- [[{related_id}]]\n"
            if link not in content:
                content += link
                new_links.append(related_id)
                count += 1
        
        if not dry_run and new_links:
            try:
                node_data["path"].write_text(content, encoding="utf-8")
                applied.append(target)
            except Exception as e:
                print(f"[ERROR] {target}: {e}")
    
    return count, applied

def show_report(nodes):
    """Display graph analysis report"""
    stats = analyze_graph(nodes)
    
    print("")
    print("============================================================")
    print("           WIKI GRAPH ANALYSIS REPORT")
    print("============================================================")
    print(f"Total Nodes:        {stats['total']}")
    print(f"Orphans (no incoming): {len(stats['orphans'])}")
    print(f"Dead Ends (no outgoing): {len(stats['dead_ends'])}")
    print(f"Islands (both):      {len(stats['islands'])}")
    print("============================================================")
    print("")
    print("[TOP 10 ORPHANS]")
    for i, orphan in enumerate(sorted(stats["orphans"])[:10]):
        print(f"  {i+1}. [[{orphan}]]")
    
    if stats["orphans"]:
        print("")
        print("[Run with --dry-run to see suggestions]")

def main():
    parser = argparse.ArgumentParser(description="Auto-Bridge Orphans v2.0")
    parser.add_argument("--dry-run", action="store_true", help="Show suggestions without applying")
    parser.add_argument("--force", action="store_true", help="Apply suggestions")
    parser.add_argument("--report", action="store_true", help="Show graph analysis only")
    parser.add_argument("--backup", action="store_true", help="Create backup before applying")
    parser.add_argument("--limit", type=int, default=20, help="Limit display (default: 20)")
    
    args = parser.parse_args()
    
    print("\n=== AUTO-BRIDGE ORPHANS v2.0 ===\n")
    
    # Get all nodes
    nodes = get_all_nodes()
    
    if args.report:
        show_report(nodes)
        return
    
    # Build suggestions
    suggestions = build_bridge_suggestions_v2(nodes)
    
    print(f"Found {len(suggestions)} orphan(s) with suggestions\n")
    
    # Display suggestions
    for i, s in enumerate(suggestions[:args.limit]):
        targets = ", ".join([f"[[{r[1]}]]" for r in s["suggestions"]])
        print(f"  [[{s['target']}]] -> {targets}")
    
    if len(suggestions) > args.limit:
        print(f"\n  ... and {len(suggestions) - args.limit} more")
    
    # Apply?
    if args.force and suggestions:
        count, applied = apply_bridges_v2(suggestions, nodes, dry_run=False, create_backup=args.backup)
        print(f"\n[SUCCESS] Applied {count} bridge(s) to {len(applied)} node(s)")
    elif args.dry_run:
        print("\n[Dry Run] No changes made. Use --force to apply.")
    else:
        print("\n[Options]")
        print("  --dry-run   : Preview suggestions")
        print("  --force    : Apply suggestions")
        print("  --report   : Show graph analysis")
        print("  --backup  : Create backup before --force")

if __name__ == "__main__":
    main()