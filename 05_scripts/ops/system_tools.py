"""
system_tools.py — Wiki Link System Commands (v1.1)
Legacy wrapper: prefer `python librarian.py ...` commands.
Usage:
  python system_tools.py --help-cmd       Show all commands
  python system_tools.py --status        System status
  python system_tools.py --daily         Daily quest (suggest + orphans)
  python system_tools.py --audit [file]   Run FITSERBVL audit
"""
import sys
if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
import argparse
from pathlib import Path

# Dynamic path resolution
SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT = SCRIPT_DIR.parent.parent
WIKI_DIR = WIKI_ROOT / "03_wiki"
OUTPUTS_DIR = WIKI_ROOT / "04_outputs"

def show_help():
    help_text = """
============================================================
WIKI LINK SYSTEM COMMANDS v3.8 (Atomic Knowledge Engine)
============================================================

Prefer `python librarian.py help` for the canonical entry point.

[1] SEARCH & DISCOVERY:
  python 05_scripts/wiki_search.py "query" [--top N] [--show-related]
  python 05_scripts/wiki_search.py "query" --type concept|mechanism|relationship
  python 05_scripts/wiki_search.py "query" --no-raw     # wiki only
  python 05_scripts/wiki_search.py "query" --no-wiki    # raw only

[2] GRAPH & INDEX:
  python 05_scripts/gen_index.py          # Rebuild index.md
  python 05_scripts/_build_wiki_graph.py  # Sync to graph.json
  python 05_scripts/find_orphans.py       # Find unlinked nodes

[3] RESEARCH:
  python 05_scripts/suggest_ideas.py      # Bounty/Synthesis ideas
  python 05_scripts/auto_synthesis.py [tag] # Merge nodes by tag
  python 05_scripts/claim_auditor.py [file] # FITSERBVL audit

[4] INGEST:
  python 05_scripts/extract_pdf.py [pdf_path] # PDF -> Markdown
  System.md Phase A-D: Ingest workflow

[5] DAILY WORKFLOW:
  python 05_scripts/system_tools.py --daily # suggest + orphans

============================================================
"""
    print(help_text)

def show_status():
    print(f"""
============================================================
WIKI LINK STATUS
============================================================
Root:     {WIKI_ROOT}
Wiki:     {WIKI_DIR}
Scripts:  {SCRIPT_DIR}
Outputs:  {OUTPUTS_DIR}

 [Quick Commands]
1. Search:      python librarian.py search "concept"
2. Index:       python 05_scripts/gen_index.py
3. Graph:       python 05_scripts/_build_wiki_graph.py
4. Orphans:     python 05_scripts/find_orphans.py
5. Ideas:       python 05_scripts/suggest_ideas.py
============================================================
""")

def daily_quest():
    """Run daily quest: suggest_ideas + find_orphans"""
    import subprocess
    
    print("\n=== DAILY QUEST ===\n")
    
    # Run suggest_ideas
    print("[1/2] Running suggest_ideas.py...")
    result1 = subprocess.run(
        [sys.executable, str(SCRIPT_DIR.parent / "suggest_ideas.py")],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    print(result1.stdout[:2000] if result1.stdout else result1.stderr[:1000])
    
    print("\n[2/2] Running find_orphans.py...")
    result2 = subprocess.run(
        [sys.executable, str(SCRIPT_DIR.parent / "find_orphans.py")],
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    print(result2.stdout[:2000] if result2.stdout else result2.stderr[:1000])
    
    print("\n=== DONE ===")

def main():
    parser = argparse.ArgumentParser(description="Wiki Link System Tools")
    parser.add_argument("--help-cmd", action="store_true", help="Show all commands")
    parser.add_argument("--status", action="store_true", help="System status")
    parser.add_argument("--daily", action="store_true", help="Daily quest")
    parser.add_argument("--audit", nargs="?", metavar="FILE", help="Run FITSERBVL audit")
    
    args = parser.parse_args()
    
    if args.help_cmd:
        show_help()
    elif args.status:
        show_status()
    elif args.daily:
        daily_quest()
    elif args.audit:
        from wiki_search import build_index, score
        import yaml
        
        path = Path(args.audit)
        if not path.exists():
            print(f"Error: File {path} not found.")
            return
            
        print(f"\n{'='*50}")
        print(f"AUDIT: F.I.T.S.E.R.B.V.L on {path.name}")
        print(f"{'='*50}\n")
        
        # Read content
        content = path.read_text(encoding="utf-8", errors="ignore")
        
        # Extract thesis from frontmatter
        fm = {}
        if content.startswith("---"):
            end = content.find("---", 3)
            if end != -1:
                try:
                    fm = yaml.safe_load(content[3:end]) or {}
                except:
                    pass
        
        thesis = str(fm.get("thesis", "")).strip()
        print(f"Thesis: {thesis[:200]}...")

        # Find related nodes
        print("\n[Related Nodes via wiki_search]:")
        index = build_index(WIKI_DIR, None, use_wiki=True, use_raw=False)
        query = thesis.lower().split()[:10] if thesis else path.stem.lower().replace("_", " ").split()
        matches = [(score(n, query, query), n) for n in index]
        matches = [m for m in matches if m[0] > 0]
        matches.sort(key=lambda x: -x[0])
        
        if matches[:3]:
            for m in matches[:3]:
                print(f"  - [[{m[1]['id']}]] (score: {m[0]})")
        else:
            print("  - No related nodes found")
        
        print(f"\n{'='*50}")
    else:
        show_help()

if __name__ == "__main__":
    main()



