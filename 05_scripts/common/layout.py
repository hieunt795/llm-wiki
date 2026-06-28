from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = MODULE_DIR.parent
WIKI_ROOT = SCRIPTS_ROOT.parent
WIKI_DIR = WIKI_ROOT / '03_wiki'
RAW_DIR = WIKI_ROOT / '02_sources'
OUTPUTS_DIR = WIKI_ROOT / '04_outputs'
CACHE_DIR = WIKI_ROOT / '.cache'

