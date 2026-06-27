"""
daily_quest.py — Daily Quest Wrapper (v1.0)
Runs: suggest_ideas.py + find_orphans.py
Legacy wrapper: prefer `python librarian.py daily`.
Usage:
  python daily_quest.py
  python daily_quest.py --suggest   # only run suggest_ideas
  python daily_quest.py --orphans  # only run find_orphans
"""
import sys
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import subprocess
import argparse
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT = SCRIPT_DIR.parent

def run_script(script_name, description):
    """Run a single script"""
    script_path = SCRIPT_DIR / script_name
    
    if not script_path.exists():
        print(f"[ERROR] Script not found: {script_path}")
        return False
    
    print(f"\n{'='*50}")
    print(f"{description}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=60,
            encoding="utf-8",
            errors="replace",
        )
        
        # Print output (limit to 3000 chars)
        output = result.stdout if result.stdout else result.stderr
        print(output[:3000])
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("[ERROR] Script timed out after 60 seconds")
        return False
    except Exception as e:
        print(f"[ERROR] {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Daily Quest - Research Ideas + Orphan Detection")
    parser.add_argument("--suggest", action="store_true", help="Only run suggest_ideas")
    parser.add_argument("--orphans", action="store_true", help="Only run find_orphans")
    
    args = parser.parse_args()
    
    print("""
============================================================
         DAILY QUEST v1.0
   Research Ideas + Orphan Detection
============================================================
""")
    print("LEGACY WRAPPER: prefer `python librarian.py daily`\n")
    
    success = True
    
    if args.suggest:
        success &= run_script("suggest_ideas.py", "[1/2] SUGGEST IDEAS")
    elif args.orphans:
        success &= run_script("find_orphans.py", "[1/1] FIND ORPHANS")
    else:
        success &= run_script("suggest_ideas.py", "[1/2] SUGGEST IDEAS")
        success &= run_script("find_orphans.py", "[2/2] FIND ORPHANS")
    
    print("\n" + "="*50)
    if success:
        print("DONE - All scripts completed")
    else:
        print("DONE - Some scripts had errors")
    print("="*50)

if __name__ == "__main__":
    main()
