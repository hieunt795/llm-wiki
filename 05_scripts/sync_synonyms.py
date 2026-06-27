import yaml
from pathlib import Path
from collections import defaultdict

def extract_all_aliases():
    wiki_dir = Path("03_wiki")
    registry_path = Path("01_schema/registry/synonyms.yml")
    syn_map = defaultdict(set)
    
    # 1. Quét tất cả các file md trong wiki
    for md_file in wiki_dir.rglob("*.md"):
        try:
            text = md_file.read_text(encoding="utf-8", errors="ignore")
            if text.startswith("---"):
                end = text.find("---", 3)
                if end != -1:
                    fm = yaml.safe_load(text[3:end]) or {}
                    aliases = fm.get("aliases")
                    title = fm.get("title", md_file.stem)
                    
                    if aliases:
                        if isinstance(aliases, str): aliases = [aliases]
                        # Base term là title hoặc filename
                        base = title.strip()
                        for a in aliases:
                            if a: syn_map[base.lower()].add(a.strip())
        except Exception:
            continue
            
    # 2. Cập nhật vào YAML
    new_synonyms = []
    for base, aliases in syn_map.items():
        entry = [base] + sorted(list(aliases))
        new_synonyms.append(entry)
        
    with open(registry_path, "w", encoding="utf-8") as f:
        yaml.dump({"synonyms": new_synonyms}, f, allow_unicode=True, default_flow_style=False)
    print(f"Extracted {len(new_synonyms)} base terms with aliases.")

if __name__ == "__main__":
    extract_all_aliases()
