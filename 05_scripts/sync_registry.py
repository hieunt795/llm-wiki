import yaml
from pathlib import Path

def sync_registry():
    """Tự động gom alias từ Wiki và giữ nguyên cấu trúc thủ công."""
    wiki_dir = Path("03_wiki")
    syn_path = Path("01_schema/registry/synonyms.yml")
    
    # 1. Thu thập từ wiki
    wiki_syns = {}
    for md_file in wiki_dir.rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8", errors="ignore")
            if text.startswith("---"):
                end = text.find("---", 3)
                if end != -1:
                    fm = yaml.safe_load(text[3:end]) or {}
                    if fm.get("aliases"):
                        base = fm.get("title", md_file.stem).lower()
                        aliases = fm.get("aliases")
                        if isinstance(aliases, str): aliases = [aliases]
                        wiki_syns[base] = set(a.lower() for a in aliases)
        except: continue

    # 2. Merge với file hiện tại
    if syn_path.exists():
        with open(syn_path, "r", encoding="utf-8") as f:
            existing = yaml.safe_load(f) or {}
            for entry in existing.get("synonyms", []):
                if entry:
                    base = entry[0].lower()
                    existing_aliases = set(a.lower() for a in entry[1:])
                    wiki_syns[base] = wiki_syns.get(base, set()) | existing_aliases

    # 3. Ghi lại
    final_syns = [[k] + sorted(list(v)) for k, v in wiki_syns.items()]
    with open(syn_path, "w", encoding="utf-8") as f:
        yaml.dump({"synonyms": sorted(final_syns)}, f, allow_unicode=True, default_flow_style=False)
    print("Registry synced.")

if __name__ == "__main__":
    sync_registry()
