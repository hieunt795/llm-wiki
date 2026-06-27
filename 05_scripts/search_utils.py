import yaml
import re
from pathlib import Path

# Resolve WIKI_ROOT from script location — works regardless of CWD
_SCRIPT_DIR = Path(__file__).parent
_WIKI_ROOT   = _SCRIPT_DIR.parent
_DEFAULT_SYNONYMS_PATH    = _WIKI_ROOT / "01_schema" / "registry" / "synonyms.yml"
_DEFAULT_ROUTER_RULES_PATH = _WIKI_ROOT / "01_schema" / "registry" / "router_rules.yml"


def load_synonyms(registry_path: Path = None) -> dict:
    """Tải từ điển đồng nghĩa từ file YAML."""
    if registry_path is None:
        registry_path = _DEFAULT_SYNONYMS_PATH
    if not registry_path.exists():
        return {}
    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            syn_map = {}
            for syn_list in data.get("synonyms", []):
                if not syn_list:
                    continue
                base_term = syn_list[0].lower()
                for alias in syn_list:
                    syn_map[alias.lower()] = base_term
            return syn_map
    except Exception:
        return {}


def expand_query(query_terms: list, syn_map: dict) -> list:
    """Mở rộng query term bằng các synonym."""
    expanded = set(query_terms)
    for term in query_terms:
        if term.lower() in syn_map:
            expanded.add(syn_map[term.lower()])
        for alias, base in syn_map.items():
            if base == term.lower():
                expanded.add(alias)
    return list(expanded)


def route_query(query: str, rules_path: Path = None) -> dict:
    """Định tuyến truy vấn dựa trên từ khóa."""
    if rules_path is None:
        rules_path = _DEFAULT_ROUTER_RULES_PATH
    default_route = {"sources": ["both"], "boost": ["title"], "escalation": False}
    if not rules_path.exists():
        return default_route
    try:
        with open(rules_path, "r", encoding="utf-8") as f:
            rules_data = yaml.safe_load(f).get("rules", {})
        q_lower = query.lower()
        for category, config in rules_data.items():
            if any(k in q_lower for k in config.get("keywords", [])):
                return config
        return default_route
    except Exception:
        return default_route

def highlight_snippet(text: str, terms: list[str], max_chars: int = 150) -> str:
    """Highlight terms within a text snippet."""
    if not terms:
        return text[:max_chars] + "..."
    
    # Tìm đoạn snippet chứa từ khóa
    snippet = text
    for t in terms:
        idx = text.lower().find(t.lower())
        if idx != -1:
            start = max(0, idx - 40)
            end = min(len(text), idx + 60)
            snippet = text[start:end]
            break
            
    # Highlight
    for t in terms:
        if len(t) < 2: continue
        pattern = re.compile(f"({re.escape(t)})", re.IGNORECASE)
        snippet = pattern.sub(r"**\1**", snippet)
        
    return "..." + snippet + "..."
