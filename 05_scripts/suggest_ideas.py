import sys
import yaml
import random
import io
from pathlib import Path

# Fix Windows terminal UTF-8 encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT = SCRIPT_DIR.parent / "03_wiki"
RESEARCH_ROOT = SCRIPT_DIR.parent / "04_outputs/research"

def extract_frontmatter(file_path: Path) -> dict:
    try:
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        if text.startswith("---"):
            end = text.find("---", 3)
            if end != -1:
                return yaml.safe_load(text[3:end]) or {}
    except Exception:
        pass
    return {}

def main():
    if not WIKI_ROOT.exists():
        print(f"Error: {WIKI_ROOT} not found.")
        sys.exit(1)

    nodes = []
    low_confidence = []
    tag_map = {} # tag -> list of node stems
    
    for filepath in WIKI_ROOT.rglob("*.md"):
        fm = extract_frontmatter(filepath)
        stem = filepath.stem
        nodes.append(stem)
        
        # Check Confidence
        conf = fm.get("confidence", 5)
        try:
            conf = int(conf)
        except:
            conf = 5
            
        # Check if text contains [LLM]
        try:
            content = filepath.read_text(encoding="utf-8", errors="ignore")
            if "[LLM]" in content or conf <= 2:
                low_confidence.append(stem)
        except:
            pass
            
        # Build Tag Map
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        tags = [str(t).lower() for t in tags if t]
        
        for t in tags:
            if t not in tag_map:
                tag_map[t] = []
            tag_map[t].append(stem)

    print("="*60)
    print("🧠 ATOMIC KNOWLEDGE ENGINE - DAILY QUEST BOARD")
    print("="*60)

    # 1. Bounties (Low Confidence)
    print("\n🕵️‍♂️ [MISSION 1: RESEARCH BOUNTY]")
    if low_confidence:
        sample = random.sample(low_confidence, min(3, len(low_confidence)))
        print(f"System detected {len(low_confidence)} nodes requiring Raw Source verification ([LLM] placeholders or low confidence).")
        print("Suggested targets for today:")
        for s in sample:
            print(f"  👉 {s}")
    else:
        print("  All current nodes are fully verified. Excellent work!")

    # 2. Synthesis Alerts
    print("\n📚 [MISSION 2: SYNTHESIS ALERTS]")
    synthesis_targets = []
    for tag, items in tag_map.items():
        if len(items) >= 5: # Threshold for synthesis
            # Check if synthesis exists
            syn_files = list(RESEARCH_ROOT.glob(f"*{tag}*synthesis*.md"))
            if not syn_files:
                synthesis_targets.append((tag, len(items)))
    
    if synthesis_targets:
        synthesis_targets.sort(key=lambda x: x[1], reverse=True)
        top_targets = synthesis_targets[:2]
        print(f"Found {len(synthesis_targets)} mature concept clusters lacking a Synthesis Report.")
        for tag, count in top_targets:
            print(f"  👉 Tag '{tag}' has {count} nodes. Run: python 05_scripts/auto_synthesis.py \"{tag}\"")
    else:
        print("  No mature clusters require synthesis right now.")

    # 3. Random Walk
    print("\n🎲 [MISSION 3: RANDOM WALK]")
    if nodes:
        random_node = random.choice(nodes)
        print(f"  👉 Review a random concept today: [[{random_node}]]")
        
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
