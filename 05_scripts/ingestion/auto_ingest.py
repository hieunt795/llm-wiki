# -*- coding: utf-8 -*-
"""
auto_ingest.py - Random Section Sampler & Wiki Node Generator (v1.1)
=====================================================================
Scans raw books -> extracts sections by sub-heading -> checks wiki coverage
-> randomly samples UNCOVERED sections (fair per-book clustering)
-> generates draft wiki nodes in staging area for human review.

PHILOSOPHY:
  - Never write directly to 03_wiki -- always stage first for review
  - Fair clustering: max 1 section per book per run (like raw_scout.py)
  - Coverage-aware: skip sections already represented in wiki
  - Quality floor: minimum content length before generating node
  - Draft format matches canonical Fiscal_Dominance.md template

USAGE:
  python auto_ingest.py                        # sample 3 random uncovered sections
  python auto_ingest.py --n 5                  # sample 5 sections
  python auto_ingest.py --book tuckman         # target specific book (substring match)
  python auto_ingest.py --list-coverage        # show per-book coverage stats
  python auto_ingest.py --dry-run              # show candidates without writing files
  python auto_ingest.py --n 3 --min-depth 2   # only sub-sections (X.Y.Z level)
  python auto_ingest.py --staged               # list current staged nodes
  python auto_ingest.py --accept <name>        # move staged node -> 03_wiki (after review)
  python auto_ingest.py --accept-all           # accept all staged nodes

OUTPUT:
  Draft nodes -> 04_outputs/staged_nodes/[BookSlug]__[SectionSlug].md
  Coverage report -> 04_outputs/staged_nodes/_coverage_report.md (with --list-coverage)
"""

import re
import sys
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import io
import random
import argparse
import yaml
import shutil
from pathlib import Path
from datetime import date
from collections import defaultdict

# Fix Windows terminal encoding (Windows only -- do NOT run on Linux/pipe contexts)
if sys.platform == 'win32':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')

# -- Paths ---------------------------------------------------------------------
SCRIPT_DIR  = Path(__file__).parent
WIKI_ROOT   = SCRIPT_DIR.parent.parent
BOOKS_DIR   = WIKI_ROOT / "02_sources" / "books"
WIKI_DIR    = WIKI_ROOT / "03_wiki"
STAGED_DIR  = WIKI_ROOT / "04_outputs" / "staged_nodes"
LOG_FILE    = WIKI_ROOT / "01_schema" / "log.md"
TODAY       = date.today().isoformat()

# -- Book metadata registry ----------------------------------------------------
# Maps folder name -> (short_name, expert_lens, primary_tags)
BOOK_REGISTRY = {
    "central_policy_Perry":          ("Perry Warjiyo",         "Perry Warjiyo",                    ["central-banking", "monetary-policy"]),
    "fixed_income_during":           ("Alexander Düring",      "Alexander Düring",                  ["fixed-income", "trading", "microstructure"]),
    "tuckman_serrat_fixed_income":   ("Tuckman & Serrat",      "Tuckman & Serrat",                  ["fixed-income", "bond-math", "yield-curve"]),
    "neftci_principles":             ("Neftci",                "Salih Neftci",                      ["financial-engineering", "derivatives"]),
    "howard_corb_swaps":             ("Howard Corb",           "Howard Corb",                       ["derivatives", "interest-rate-swaps"]),
    "choudhry_banking_fixed_income": ("Choudhry",              "Moorad Choudhry",                   ["fixed-income", "ALM", "yield-curve"]),
    "huggins_schaller_relative_value": ("Huggins & Schaller",  "Huggins & Schaller",                ["fixed-income", "relative-value", "spread"]),
    "bindseil_monetary_policy":      ("Bindseil",              "Ulrich Bindseil",                   ["monetary-policy", "central-banking", "liquidity"]),
    "homer_leibowitz_yield_book":    ("Homer & Leibowitz",     "Homer & Leibowitz",                 ["bond-math", "yield-curve", "fixed-income"]),
    "tata_bank_alm":                 ("Tata",                  "Fidelio Tata",                      ["ALM", "banking", "balance-sheet"]),
    "wystup_fx_options":             ("Wystup",                "Uwe Wystup",                        ["fx", "options", "derivatives"]),
    "schofield_fixed_income":        ("Schofield",             "Neil Schofield",                    ["fixed-income", "ALM", "trading"]),
    "watts_wray_mmt_macro":          ("MMT Wray",              "MMT (L. Randall Wray)",             ["MMT", "monetary-policy", "fiscal-policy"]),
    "wilmott_quant_finance":         ("Wilmott",               "Paul Wilmott",                      ["quant-finance", "derivatives", "math"]),
    "weithers_fx_guide":             ("Weithers",              "Weithers",                          ["fx", "forex", "derivatives"]),
    "aci_dealing_certificate":       ("ACI",                   "ACI",                               ["fx", "money-markets", "conventions"]),
    "lipschitz_schadler_macro":      ("Lipschitz & Schadler",  "Lipschitz & Schadler",              ["macroeconomics", "IMF", "EMEs"]),
    "elkenbracht_huizing_alm":       ("Elkenbracht-Huizing",   "Elkenbracht-Huizing",               ["ALM", "banking"]),
    "cargill_central_bank_policy":   ("Cargill",               "Cargill",                           ["central-banking", "monetary-policy"]),
}

# -- Heading detection strategies ----------------------------------------------

# Numbered section: "6.2.1. Title" or "6.2.1 Title" or "1.1 A Unique Instrument"
RE_NUMBERED = re.compile(
    r'^(\d{1,2}\.\d{1,2}(?:\.\d{1,2})?(?:\.\d{1,2})?)[.\s]+([A-Z][^\n]{3,80})$',
    re.MULTILINE
)
# CHAPTER N heading
RE_CHAPTER = re.compile(
    r'^(?:CHAPTER|Chapter)\s+(\d+|[IVXLCDM]+)\s*\n([A-Z][^\n]{3,80})$',
    re.MULTILINE
)
# Markdown H2/H3
RE_MARKDOWN = re.compile(
    r'^(#{2,4})\s+(.+)$',
    re.MULTILINE
)
# Standalone ALL CAPS heading (common in older books)
RE_ALLCAPS = re.compile(
    r'^([A-Z][A-Z\s\-]{8,60})$',
    re.MULTILINE
)


def slugify(text: str) -> str:
    """Convert heading text to wiki-compatible filename slug."""
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '_', text.strip())
    return text[:60]


def read_safe(path: Path, max_bytes: int = 0) -> str:
    """Read file safely, optionally capping at max_bytes to handle huge books."""
    for enc in ['utf-8', 'utf-16', 'latin-1']:
        try:
            if max_bytes:
                with open(path, encoding=enc, errors='ignore') as f:
                    return f.read(max_bytes)
            return path.read_text(encoding=enc, errors='ignore')
        except Exception:
            continue
    return ""


# -- Section Extraction --------------------------------------------------------

def extract_sections(content: str, source_file: Path) -> list:
    """
    Extract sections from a raw book file.
    Returns list of {heading, depth, number, content_preview, page_ref, line_no}
    """
    sections = []

    # Strategy 1: Numbered sections (most reliable for Perry, Neftci, etc.)
    for match in RE_NUMBERED.finditer(content):
        number  = match.group(1)
        heading = match.group(2).strip()
        depth   = number.count('.')          # 6.1 = depth 1, 6.2.1 = depth 2
        line_no = content[:match.start()].count('\n')

        # Extract content preview (next ~800 chars until next section)
        rest    = content[match.end():]
        next_h  = RE_NUMBERED.search(rest)
        snippet = rest[:next_h.start()] if next_h else rest[:800]
        snippet = re.sub(r'<!--.*?-->', '', snippet).strip()[:600]

        # Skip if too short (title-only, no real content)
        if len(snippet) < 80:
            continue

        sections.append({
            "heading":         heading,
            "number":          number,
            "depth":           depth,
            "content_preview": snippet,
            "source_file":     str(source_file),
            "line_no":         line_no,
        })

    # Strategy 2: Chapter headings (if no numbered sections found)
    if not sections:
        for match in RE_CHAPTER.finditer(content):
            chap_num = match.group(1)
            heading  = match.group(2).strip()
            line_no  = content[:match.start()].count('\n')
            rest     = content[match.end():]
            next_h   = RE_CHAPTER.search(rest)
            snippet  = rest[:next_h.start()] if next_h else rest[:800]
            snippet  = re.sub(r'<!--.*?-->', '', snippet).strip()[:600]
            if len(snippet) < 80:
                continue
            sections.append({
                "heading":         heading,
                "number":          f"Ch.{chap_num}",
                "depth":           0,
                "content_preview": snippet,
                "source_file":     str(source_file),
                "line_no":         line_no,
            })

    # Strategy 3: Markdown headers (fallback)
    if not sections:
        for match in RE_MARKDOWN.finditer(content):
            depth   = len(match.group(1)) - 1
            heading = match.group(2).strip()
            line_no = content[:match.start()].count('\n')
            rest    = content[match.end():]
            next_h  = RE_MARKDOWN.search(rest)
            snippet = rest[:next_h.start()] if next_h else rest[:800]
            snippet = snippet.strip()[:600]
            if len(snippet) < 80:
                continue
            sections.append({
                "heading":         heading,
                "number":          f"H{depth}",
                "depth":           depth,
                "content_preview": snippet,
                "source_file":     str(source_file),
                "line_no":         line_no,
            })

    return sections


# -- Wiki Coverage Check -------------------------------------------------------

def build_wiki_title_set() -> set:
    """Build a set of lowercased wiki node titles and aliases for fast lookup.
    Uses a simple pickle cache (60-min TTL) to avoid re-scanning on every run."""
    import pickle, time
    cache_file = WIKI_ROOT / ".cache" / "ingest_wiki_titles.pkl"
    cache_file.parent.mkdir(exist_ok=True)

    if cache_file.exists():
        age = time.time() - cache_file.stat().st_mtime
        if age < 3600:  # 60-min TTL
            try:
                with open(cache_file, "rb") as f:
                    return pickle.load(f)
            except Exception:
                pass

    titles = set()
    for fp in WIKI_DIR.rglob("*.md"):
        stem = fp.stem.lower().replace('_', ' ')
        titles.add(stem)
        # Fast frontmatter parse -- only read first 600 bytes
        try:
            raw = fp.read_bytes()[:600].decode('utf-8', errors='ignore')
            if raw.startswith('---'):
                end = raw.find('---', 3)
                if end != -1:
                    fm = yaml.safe_load(raw[3:end]) or {}
                    if fm.get('title'):
                        titles.add(str(fm['title']).lower())
                    for alias in (fm.get('aliases') or []):
                        titles.add(str(alias).lower())
        except Exception:
            pass

    try:
        with open(cache_file, "wb") as f:
            pickle.dump(titles, f)
    except Exception:
        pass

    return titles


def is_covered(heading: str, wiki_titles: set, threshold: float = 0.6) -> bool:
    """
    Check if a section heading is already represented in the wiki.
    Uses word overlap scoring (lightweight, no deps).
    """
    heading_words = set(re.findall(r'\b\w{4,}\b', heading.lower()))
    if not heading_words:
        return False

    stop = {'this', 'that', 'with', 'from', 'which', 'their', 'there',
            'these', 'would', 'should', 'could', 'analysis', 'overview',
            'introduction', 'conclusions', 'summary', 'discussion'}
    heading_words -= stop

    if not heading_words:
        return False

    best_score = 0.0
    for title in wiki_titles:
        title_words = set(re.findall(r'\b\w{4,}\b', title)) - stop
        if not title_words:
            continue
        overlap = len(heading_words & title_words)
        score   = overlap / max(len(heading_words), len(title_words))
        if score > best_score:
            best_score = score
        if best_score >= threshold:
            return True

    return best_score >= threshold


# -- Book Scanner --------------------------------------------------------------

def scan_book(book_dir: Path) -> list:
    """Scan all .md files in a book directory and return all sections.
    Uses a persistent index cache to avoid re-scanning large files."""
    import pickle, time, hashlib

    book_slug  = book_dir.name
    meta       = BOOK_REGISTRY.get(book_slug, (book_slug, book_slug, ["finance"]))
    cache_dir  = WIKI_ROOT / ".cache" / "ingest_sections"
    cache_dir.mkdir(parents=True, exist_ok=True)

    all_sections = []

    for md_file in sorted(book_dir.glob("*.md")):
        if md_file.stat().st_size < 500:
            continue

        # Cache key: file path + mtime
        mtime     = int(md_file.stat().st_mtime)
        cache_key = hashlib.md5(f"{md_file}{mtime}".encode()).hexdigest()
        cache_f   = cache_dir / f"{cache_key}.pkl"

        # Load from cache if available
        if cache_f.exists():
            try:
                with open(cache_f, "rb") as f:
                    sections = pickle.load(f)
                all_sections.extend(sections)
                continue
            except Exception:
                pass

        # Read file -- cap at 300KB for very large files to keep speed reasonable
        # (300KB ~~ 100 pages, more than enough for section detection)
        file_size = md_file.stat().st_size
        max_bytes = 300_000 if file_size > 500_000 else 0
        content   = read_safe(md_file, max_bytes=max_bytes)

        if not content or len(content) < 500:
            continue

        sections = extract_sections(content, md_file)
        for s in sections:
            s["book_slug"]   = book_slug
            s["book_name"]   = meta[0]
            s["expert_lens"] = meta[1]
            s["base_tags"]   = meta[2]

        # Save to cache
        try:
            with open(cache_f, "wb") as f:
                pickle.dump(sections, f)
        except Exception:
            pass

        all_sections.extend(sections)

    return all_sections


# -- Draft Node Generator ------------------------------------------------------

def infer_node_type(heading: str, content: str) -> str:
    """Infer node type from heading keywords."""
    h = heading.lower()
    if any(w in h for w in ['mechanism', 'process', 'how', 'transmission', 'operation', 'function']):
        return 'mechanism'
    if any(w in h for w in ['definition', 'concept', 'what is', 'overview', 'introduction']):
        return 'definition'
    if any(w in h for w in ['convention', 'standard', 'rule', 'practice', 'market convention']):
        return 'convention'
    if any(w in h for w in ['evidence', 'empirical', 'case study', 'study', 'data']):
        return 'evidence'
    if any(w in h for w in ['debate', 'vs', 'versus', 'argument', 'criticism']):
        return 'perspective'
    return 'mechanism'  # default: most wiki nodes are mechanisms


def extract_thesis_candidate(content: str) -> str:
    """
    Extract first substantive sentence as thesis candidate.
    Falls back to [NEEDS THESIS] if content is too fragmented.
    """
    # Clean PDF artifacts and page markers
    clean = re.sub(r'<!--.*?-->', '', content)
    clean = re.sub(r'\(cid:\d+\)', '', clean)
    clean = re.sub(r'[-=]{3,}', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', clean)
    for sent in sentences:
        sent = sent.strip()
        # Good thesis: >40 chars, starts with capital, no page numbers
        if (len(sent) > 40
                and sent[0].isupper()
                and not re.match(r'^\d', sent)
                and not re.search(r'copyright|wiley|published|isbn', sent.lower())):
            return sent[:300]

    return "[NEEDS THESIS -- review and write 1-sentence core claim]"


def generate_draft_node(section: dict) -> str:
    """Generate a draft wiki node matching the canonical Fiscal_Dominance.md format."""
    heading      = section["heading"]
    number       = section["number"]
    content      = section["content_preview"]
    book_name    = section["book_name"]
    expert_lens  = section["expert_lens"]
    base_tags    = section["base_tags"]
    source_file  = Path(section["source_file"])
    node_type    = infer_node_type(heading, content)
    thesis       = extract_thesis_candidate(content)
    title_slug   = slugify(heading)

    # Build tags -- combine base + type
    tags = list(base_tags)
    if node_type not in tags:
        tags.append(node_type)

    # Infer chapter number from section number (e.g. "6.2.1" -> 6)
    chapter_num = number.split('.')[0] if re.match(r'^\d', number) else None

    # Build frontmatter dict -- order matches canonical template
    frontmatter = {
        "title":       heading,
        "aliases":     [heading],
        "type":        node_type,
        "tags":        tags,
        "status":      "draft",
        "confidence":  1,
        "expert_lens": expert_lens,
        "thesis":      thesis,
        "provenance":  "extracted",
        "source_refs": [{"file": source_file.name, "page": number}],
        "created":     TODAY,
        "updated":     TODAY,
    }
    if chapter_num:
        frontmatter["chapter"] = int(chapter_num)

    fm_str = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False,
                       sort_keys=False).strip()

    # Clean raw content for embedding
    clean_content = re.sub(r'<!--.*?-->', '', content)
    clean_content = re.sub(r'\(cid:\d+\)', ' ', clean_content)
    clean_content = re.sub(r'\s+', ' ', clean_content).strip()

    # Body section label depends on type
    core_section = "## Definition" if node_type == "definition" else "## Mechanism"

    node = f"""---
{fm_str}
---

# [[{title_slug}]]

> STAGED -- auto_ingest v1.1. Review before `--accept`.
> Source: `{source_file.name}` section {number}

## Thesis

[extracted] {thesis}

## Raw Content Extract

[RAW] From **{book_name}** ({number}):

> {clean_content}

{core_section}

[NEEDS CONTENT -- expand from Raw Content above using P3_mechanistic.md claim structure]

```
Claim:         [X] -> [Y]
Mechanism:     A -> B -> C
Can:           [condition A], [condition B]
Du:            [A] + [B] + [C]
Source:        [RAW] {source_file.name} section {number}
```

## Worked Example

[NEEDS EXAMPLE -- add quantitative illustration with real numbers]

## Evidence / Source Anchors

- [[{source_file.name}#page={number}]] -- {heading}

## Related

[NEEDS LINKS -- add wikilinks after review]
"""
    return node


# -- Coverage Report -----------------------------------------------------------

def generate_coverage_report(all_sections: list, wiki_titles: set) -> str:
    """Generate a markdown coverage report per book."""
    by_book = defaultdict(list)
    for s in all_sections:
        by_book[s["book_slug"]].append(s)

    lines = [f"# Ingest Coverage Report\n_Generated: {TODAY}_\n"]
    lines.append("| Book | Total Sections | Covered | Uncovered | Coverage % |")
    lines.append("|------|---------------|---------|-----------|------------|")

    total_all, covered_all = 0, 0
    for book_slug, sections in sorted(by_book.items()):
        covered   = sum(1 for s in sections if is_covered(s["heading"], wiki_titles))
        total     = len(sections)
        pct       = f"{100*covered//total}%" if total else "N/A"
        uncovered = total - covered
        book_name = BOOK_REGISTRY.get(book_slug, (book_slug,))[0]
        lines.append(f"| {book_name} | {total} | {covered} | {uncovered} | {pct} |")
        total_all   += total
        covered_all += covered

    overall_pct = f"{100*covered_all//total_all}%" if total_all else "N/A"
    lines.append(f"| **TOTAL** | **{total_all}** | **{covered_all}** | **{total_all-covered_all}** | **{overall_pct}** |")

    lines.append("\n## Top Uncovered Sections (by Book)\n")
    for book_slug, sections in sorted(by_book.items()):
        uncovered = [s for s in sections if not is_covered(s["heading"], wiki_titles)]
        if not uncovered:
            continue
        book_name = BOOK_REGISTRY.get(book_slug, (book_slug,))[0]
        lines.append(f"\n### {book_name} ({len(uncovered)} uncovered)")
        for s in uncovered[:5]:
            lines.append(f"- [{s['number']}] **{s['heading']}**")
        if len(uncovered) > 5:
            lines.append(f"- _...and {len(uncovered)-5} more_")

    return "\n".join(lines)


# -- Main ----------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="auto_ingest.py v1.1 -- Random Section Sampler")
    parser.add_argument("--n",             type=int, default=3,    help="Number of sections to sample (default: 3)")
    parser.add_argument("--book",          type=str, default=None, help="Filter by book name (substring match)")
    parser.add_argument("--min-depth",     type=int, default=1,    help="Min section depth: 1=X.Y, 2=X.Y.Z (default: 1)")
    parser.add_argument("--dry-run",       action="store_true",    help="Show candidates without writing files")
    parser.add_argument("--list-coverage", action="store_true",    help="Show per-book coverage report")
    parser.add_argument("--staged",        action="store_true",    help="List current staged nodes")
    parser.add_argument("--accept",        type=str, default=None, help="Accept staged node by filename (move to 03_wiki)")
    parser.add_argument("--accept-all",    action="store_true",    help="Accept ALL staged nodes (use with caution)")
    args = parser.parse_args()

    STAGED_DIR.mkdir(parents=True, exist_ok=True)

    # -- List staged nodes -----------------------------------------------------
    if args.staged:
        staged = list(STAGED_DIR.glob("*.md"))
        staged = [f for f in staged if not f.name.startswith('_')]
        if not staged:
            print("No staged nodes. Run without --staged to generate some.", flush=True)
            return
        print(f"\n{'='*55}", flush=True)
        print(f"  STAGED NODES ({len(staged)} pending review)", flush=True)
        print(f"{'='*55}", flush=True)
        for f in sorted(staged):
            print(f"  -> {f.name}", flush=True)
        print(f"\nReview files in: {STAGED_DIR}", flush=True)
        print("Use --accept <filename> or --accept-all to promote to 03_wiki", flush=True)
        return

    # -- Accept staged nodes ---------------------------------------------------
    if args.accept or args.accept_all:
        staged = list(STAGED_DIR.glob("*.md"))
        staged = [f for f in staged if not f.name.startswith('_')]
        if args.accept:
            staged = [f for f in staged if args.accept in f.name]

        if not staged:
            print("No matching staged nodes found.", flush=True)
            return

        accepted = 0
        for f in staged:
            try:
                text = f.read_text(encoding='utf-8')
                fm   = {}
                if text.startswith('---'):
                    end = text.find('---', 3)
                    if end != -1:
                        fm = yaml.safe_load(text[3:end]) or {}
                node_type = fm.get('type', 'mechanisms')
                type_map  = {
                    'definition': 'definitions', 'mechanism': 'mechanisms',
                    'convention': 'conventions', 'perspective': 'perspectives',
                    'evidence':   'evidence',    'contradiction': 'contradictions',
                }
                folder = type_map.get(node_type, 'mechanisms')
                target_dir = WIKI_DIR / folder
                target_dir.mkdir(exist_ok=True)
                title  = fm.get('title', f.stem)
                target = target_dir / f"{slugify(title)}.md"
                shutil.copy2(f, target)
                f.unlink()
                print(f"  Accepted: {f.name} -> 03_wiki/{folder}/{target.name}", flush=True)
                accepted += 1

                # Log
                with open(LOG_FILE, 'a', encoding='utf-8') as log:
                    log.write(f"\n[{TODAY}] SPAWN (from staged) -- {slugify(title)} -- accepted from auto_ingest")
            except Exception as e:
                print(f"  Error accepting {f.name}: {e}", flush=True)

        print(f"\nAccepted {accepted} node(s) into 03_wiki.", flush=True)
        return

    # -- Scan all books --------------------------------------------------------
    print(f"\n{'='*55}", flush=True)
    print(f"  AUTO INGEST v1.1 -- Scanning books...", flush=True)
    print(f"{'='*55}", flush=True)

    all_sections = []
    book_dirs    = sorted(BOOKS_DIR.iterdir()) if BOOKS_DIR.exists() else []

    for book_dir in book_dirs:
        if not book_dir.is_dir():
            continue
        if args.book and args.book.lower() not in book_dir.name.lower():
            continue
        sections = scan_book(book_dir)
        all_sections.extend(sections)
        if sections:
            print(f"  {book_dir.name}: {len(sections)} sections found", file=sys.stderr, flush=True)

    if not all_sections:
        print("No sections found. Check --book filter or books directory.", flush=True)
        return

    print(f"\n  Total sections scanned: {len(all_sections)}", file=sys.stderr, flush=True)

    # -- Coverage report -------------------------------------------------------
    print("  Building wiki coverage index...", file=sys.stderr, flush=True)
    wiki_titles = build_wiki_title_set()

    if args.list_coverage:
        report = generate_coverage_report(all_sections, wiki_titles)
        report_path = STAGED_DIR / "_coverage_report.md"
        report_path.write_text(report, encoding='utf-8')
        print(report, flush=True)
        print(f"\nReport saved: {report_path}", flush=True)
        return

    # -- Filter: depth + uncovered ---------------------------------------------
    candidates = [
        s for s in all_sections
        if s["depth"] >= args.min_depth
        and not is_covered(s["heading"], wiki_titles)
    ]

    if not candidates:
        print("\nAll sections at this depth are already covered in wiki!", flush=True)
        return

    print(f"  Uncovered candidates: {len(candidates)}", file=sys.stderr, flush=True)

    # -- Fair clustering: max 1 per book per run -------------------------------
    by_book = defaultdict(list)
    for s in candidates:
        by_book[s["book_slug"]].append(s)

    # Shuffle within each book, then pick 1 per book
    pool = []
    for book_slug, sections in by_book.items():
        random.shuffle(sections)
        pool.append(sections[0])  # 1 representative per book

    # Shuffle pool and pick N
    random.shuffle(pool)
    selected = pool[:args.n]

    # -- Output ----------------------------------------------------------------
    print(f"\n{'='*55}", flush=True)
    print(f"  SELECTED {len(selected)} SECTION(S) FOR INGEST", flush=True)
    print(f"{'='*55}\n", flush=True)

    for i, section in enumerate(selected, 1):
        print(f"#{i} [{section['book_name']}] {section['number']} -- {section['heading']}", flush=True)
        print(f"   Source: {Path(section['source_file']).name}", flush=True)
        print(f"   Depth:  {section['depth']} | Type: {infer_node_type(section['heading'], section['content_preview'])}", flush=True)
        print(f"   Preview: {section['content_preview'][:120].strip()}...", flush=True)
        print(flush=True)

        if not args.dry_run:
            draft    = generate_draft_node(section)
            filename = f"{section['book_slug']}__{slugify(section['heading'])}.md"
            out_path = STAGED_DIR / filename
            out_path.write_text(draft, encoding='utf-8')
            print(f"   Staged: {out_path.name}\n", flush=True)

    if args.dry_run:
        print("[DRY RUN] No files written. Remove --dry-run to generate staged nodes.", flush=True)
    else:
        print(f"{'='*55}", flush=True)
        print(f"  {len(selected)} node(s) staged at:", flush=True)
        print(f"  {STAGED_DIR}", flush=True)
        print(f"\n  Next steps:", flush=True)
        print(f"  1. Review staged files -- edit thesis, add mechanism, add Related links", flush=True)
        print(f"  2. python auto_ingest.py --staged          (list pending)", flush=True)
        print(f"  3. python auto_ingest.py --accept <name>   (promote to 03_wiki)", flush=True)
        print(f"{'='*55}", flush=True)


if __name__ == "__main__":
    main()

