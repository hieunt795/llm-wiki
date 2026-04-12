"""
_audit_concepts.py — Phase C Audit Tool (v2)
Quét Raw PDF text để tìm các Concept tiềm năng bị bỏ sót.

Cải tiến v2:
  1. Ghép lại các từ bị ngắt dòng do OCR (hyphenation healing).
  2. Bắt thêm pattern: Parenthetical abbreviations (CSD), (DvP), (VM).
  3. Bắt thêm pattern: Capitalized noun phrases (General Collateral, etc.).
  4. Substring matching cải thiện: Word-boundary aware.
  5. Bold/Italic regex mở rộng character class cho /, +, &, ().
  6. Cross-check cả nội dung node files (quét [[wikilinks]] bên trong).
  7. Batch mode: Hỗ trợ chạy nhiều file cùng lúc hoặc dùng wildcard.
  8. Phân loại severity: HIGH (trigger phrase) / MEDIUM (bold/italic) / LOW (capitalized).

Usage:
  python _audit_concepts.py <chapter_file_or_glob> <alias_registry.md> [wiki_dir]

Examples:
  python _audit_concepts.py _temp_ch13.md ../00_Schema/alias_registry.md ../03_Wiki
  python _audit_concepts.py "_temp_ch*.md" ../00_Schema/alias_registry.md ../03_Wiki
"""

import re
import sys
import os
import glob
from collections import Counter


# ─── 1. LOAD KNOWN TERMS ─────────────────────────────────────────────────────

def load_registry(filepath):
    """Parse alias_registry.md and return a set of lowercase known terms."""
    known = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('|') and '---' not in line and 'Canonical' not in line:
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 4:
                        canon = parts[1].strip()
                        if canon and canon != '—':
                            known.add(canon.lower())
                        aliases = parts[2].split(',')
                        for a in aliases:
                            a = a.strip()
                            if a and a != '—':
                                known.add(a.lower())
    except Exception as e:
        print(f"[ERROR] Loading registry: {e}")
    return known


def load_wiki_terms(wiki_dir):
    """Scan existing wiki node files for [[wikilinks]] and filenames, adding them
    to the known-terms pool. This catches concepts that live INSIDE a node
    but don't have their own registry entry."""
    extra = set()
    if not wiki_dir or not os.path.isdir(wiki_dir):
        return extra
    for root, _, files in os.walk(wiki_dir):
        for fname in files:
            if fname.endswith('.md'):
                # The filename itself is a concept (e.g., Repurchase_Agreement.md)
                stem = fname.replace('.md', '').replace('_', ' ').lower()
                extra.add(stem)
                # Scan contents for [[Link_Target]] or [[Link_Target|Display]]
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    links = re.findall(r'\[\[([^\]|]+)', content)
                    for lnk in links:
                        extra.add(lnk.replace('_', ' ').lower().strip())
                except Exception:
                    pass
    return extra


# ─── 2. TEXT PRE-PROCESSING ───────────────────────────────────────────────────

def heal_hyphenation(text):
    """Rejoin words broken across lines by OCR/PDF extraction.
    e.g., 'infla-\\ntion' → 'inflation'
    """
    # Pattern: word fragment + hyphen + newline + continuation (lowercase)
    text = re.sub(r'(\w+)-\r?\n(\w)', lambda m: m.group(1) + m.group(2), text)
    return text


def normalize_whitespace(text):
    """Collapse multiple whitespace/newlines into single spaces for pattern matching,
    but preserve paragraph breaks (double newline)."""
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


# ─── 3. CANDIDATE EXTRACTION ─────────────────────────────────────────────────

def extract_candidates(text_file):
    """Extract concept candidates from the raw chapter text using multiple strategies."""
    try:
        with open(text_file, 'r', encoding='utf-8') as f:
            raw = f.read()
    except Exception as e:
        print(f"[ERROR] Reading {text_file}: {e}")
        return []

    text = heal_hyphenation(raw)
    text_flat = normalize_whitespace(text)  # for multi-word pattern matching

    results = []  # list of (term, severity)

    # ── Strategy 1: Bold text **Term** (MEDIUM) ──
    # Expanded char class:  letters, digits, spaces, hyphens, /, +, &, ', ()
    bolds = re.findall(r'\*\*([A-Za-z0-9\s\-\'/\+\&\(\)\.]+?)\*\*', text)
    for b in bolds:
        results.append((b.strip(), 'MEDIUM'))

    # ── Strategy 2: Italic text *Term* — avoid matching bold (MEDIUM) ──
    italics = re.findall(r'(?<!\*)\*([A-Za-z0-9\s\-\'/\+\&\(\)\.]+?)\*(?!\*)', text)
    for i in italics:
        results.append((i.strip(), 'MEDIUM'))

    # ── Strategy 3: Definition trigger phrases (HIGH) ──
    triggers = [
        r'(?:known|referred to|also called|abbreviated|denoted) as (?:a |an |the )?([A-Za-z0-9][\w\s\-\'/\+\&\(\)]{2,40}?)(?:[,\.\;\:]|\s(?:and|or|which|where|while|but|because|in|is|are|by|for|this))',
        r'(?:called|termed) (?:a |an |the )?([A-Za-z0-9][\w\s\-\'/\+\&\(\)]{2,40}?)(?:[,\.\;\:]|\s(?:and|or|which|where|while|but|because|in|is|are|by|for|this))',
    ]
    for pattern in triggers:
        matches = re.findall(pattern, text_flat, re.IGNORECASE)
        for m in matches:
            results.append((m.strip(), 'HIGH'))

    # ── Strategy 4: Parenthetical abbreviations like (CSD), (DvP), (VM) (HIGH) ──
    parens = re.findall(r'\(([A-Z][A-Za-z0-9]{1,8})\)', text)
    for p in parens:
        results.append((p.strip(), 'HIGH'))

    # ── Strategy 5: Capitalized multi-word noun phrases (LOW) ──
    # Match 2-5 consecutive Capitalized Words (e.g., "General Collateral", "Central Limit Order Book")
    cap_phrases = re.findall(r'\b([A-Z][a-z]+(?:\s[A-Z][a-z]+){1,4})\b', text_flat)
    for cp in cap_phrases:
        results.append((cp.strip(), 'LOW'))

    # ── Cleanup ──
    stop_phrases = {
        'the', 'a', 'an', 'and', 'or', 'in', 'on', 'of', 'for', 'is', 'are', 'to',
        'this', 'that', 'these', 'those', 'it', 'its', 'if', 'but', 'not', 'so',
        'be', 'do', 'as', 'at', 'by', 'we', 'he', 'no', 'up', 'with',
        'strong', 'white', 'buyer', 'seller', 'specifics', 'verb', 'europe',
    }
    # Common structural noise from PDF extraction
    noise_patterns = {
        'page', 'chapter', 'figure', 'table', 'section', 'part', 'note',
        'cash instruments', 'fixed income', 'two', 'preliminaries',
    }
    # Proper nouns / geographic / person names / institutions that are NOT financial concepts
    proper_noun_noise = {
        'united states', 'united kingdom', 'european union', 'the european union',
        'new york', 'hong kong', 'south africa', 'kuala lumpur', 'northern ireland',
        'channel islands', 'in europe', 'in japan', 'in german', 'in yen',
        'for europe', 'for christians', 'as muslim', 'as figure', 'see figure',
        'as ben bernanke', 'ben bernanke', 'karl marx', 'sir toby',
        'sir andrew aguecheek', 'sir isaac newton', 'mr darcy', 'douglas adams',
        'mayer amschel rothschild', 'milton friedman', 'walter bagehot',
        'president nixon', 'president clinton', 'japan governor kuroda',
        'die hard', 'twelfth night', 'pax westphalica', 'the pax westphalica',
        'napoleonic wars', 'years war', 'osaka castle',
        'lehman brothers', 'dekabank', 'state street',
        'the banque', 'the bundesbank', 'the eurosystem', 'the bindseil',
        'the king', 'the latin', 'the glass', 'the german', 'the japanese',
        'the national health service', 'the restaurant', 'as umberto eco',
        'the tokyo tanshi corporation ltd', 'london stock exchange',
        'athens stock exchange', 'the osaka rice exchange',
        'deutsche pfandbriefbank', 'deutsche girozentrale', 'deutsche bundesbank',
        'banques populaires', 'shinkin chukin', 'shoko chukin',
        'knights templar', 'schlesische landschaften', 'austrian landesbank',
        'british bankers', 'european bankers', 'japanese bankers association',
        'federal reserve act', 'federal reserve system', 'federal reserve banks',
        'federal reserve board', 'federal reserve bank system',
        'federal reserve chairman william', 'fed new york',
        'somali shilling', 'hong kong dollar', 'hong kong monetary authority',
        'shanghai banking corporation', 'swedish riksbank',
        'social responsibility', 'introductory statements',
        'cabinet office', 'governing council', 'treasury secretary',
        'world gold council', 'urban consumer price',
        'while euroclear', 'unlike european',
    }
    # Sentence-start words that leak into LOW captures
    sentence_starts = {'the', 'as', 'in', 'for', 'see', 'while', 'because',
                        'between', 'unlike', 'with', 'after', 'before',
                        'when', 'where', 'name', 'time', 'two', 'one',
                        'assets', 'deposit', 'customer', 'bank',
                        'securities', 'swaps', 'recording', 'reporting',
                        'reconciliation', 'confirmation', 'enrichment',
                        'negotiation', 'agencies', 'covered',
                        'anonymity', 'indentifiability',
                       }

    cleaned = []
    seen = set()
    for term, severity in results:
        t = term.strip(' \n\r\t.,:;"\'()[]{}')
        t_lower = t.lower()

        # Skip too short / too long
        if len(t) < 4 or len(t) > 50:
            continue
        # Skip pure stop words
        if t_lower in stop_phrases:
            continue
        # Skip noise
        if t_lower in noise_patterns:
            continue
        # Skip known proper nouns
        if t_lower in proper_noun_noise:
            continue
        # Skip items that are just numbers or page references
        if re.match(r'^[\d\s\.\-]+$', t):
            continue
        # Skip items containing newlines (broken PDF captures)
        if '\n' in t or '\r' in t:
            continue
        # For LOW severity: skip if the first word is a sentence-starter
        if severity == 'LOW':
            first_word = t.split()[0].lower() if t.split() else ''
            if first_word in sentence_starts:
                continue

        # Deduplicate (case-insensitive)
        dedup_key = t_lower
        if dedup_key not in seen:
            seen.add(dedup_key)
            cleaned.append((t, severity))

    return cleaned


# ─── 4. MATCHING AGAINST KNOWN TERMS ─────────────────────────────────────────

def is_known(term, known_set):
    """Check if a candidate term is already covered by the registry or wiki nodes.
    Uses word-boundary-aware substring matching to reduce false negatives."""
    t = term.lower().strip()

    # Direct exact match
    if t in known_set:
        return True

    # Word-boundary aware: check if any known term contains this term as a
    # complete word sequence, or vice versa.
    t_words = set(t.split())
    for k in known_set:
        if len(k) < 4:
            continue
        # Bidirectional containment with word-boundary awareness
        k_words = set(k.split())
        # If the candidate's words are a subset of a known term's words (or vice versa)
        # AND they share at least one non-trivial word
        shared = t_words & k_words
        trivial = {'of', 'the', 'a', 'an', 'and', 'in', 'vs', 'or', 'for', 'as', 'at', 'by'}
        non_trivial_shared = shared - trivial
        if non_trivial_shared:
            # At least 50% of the candidate's non-trivial words are shared
            t_non_trivial = t_words - trivial
            if t_non_trivial and len(non_trivial_shared) / len(t_non_trivial) >= 0.5:
                return True

    return False


# ─── 5. REPORT ────────────────────────────────────────────────────────────────

SEVERITY_ORDER = {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}
SEVERITY_ICON = {'HIGH': '🔴', 'MEDIUM': '🟡', 'LOW': '⚪'}


def run_audit(ch_file, reg_file, wiki_dir=None):
    """Run the full audit pipeline on a single chapter file."""
    basename = os.path.basename(ch_file)
    print(f"\n{'='*60}")
    print(f"  AUDIT: {basename}")
    print(f"{'='*60}")

    # Build known-terms pool
    known = load_registry(reg_file)
    if wiki_dir:
        known |= load_wiki_terms(wiki_dir)

    # Extract & filter
    candidates = extract_candidates(ch_file)
    if not candidates:
        print("  ✅ No structural candidates found (possibly non-textual chapter).\n")
        return 0

    # Check each candidate
    missing = []
    for term, severity in candidates:
        if not is_known(term, known):
            missing.append((term, severity))

    # Sort by severity then alphabetically
    missing.sort(key=lambda x: (SEVERITY_ORDER.get(x[1], 9), x[0].lower()))

    if not missing:
        print("  ✅ All highlighted concepts are accounted for in the Registry + Wiki!\n")
        return 0

    print(f"  ⚠️  {len(missing)} potential gaps detected:\n")
    print(f"  {'Severity':<10} {'Candidate Term':<40} {'Source'}")
    print(f"  {'─'*10} {'─'*40} {'─'*20}")
    for term, sev in missing:
        icon = SEVERITY_ICON.get(sev, '?')
        source_hint = ''
        if sev == 'HIGH':
            source_hint = 'trigger phrase / abbreviation'
        elif sev == 'MEDIUM':
            source_hint = 'bold / italic'
        else:
            source_hint = 'capitalized phrase'
        print(f"  {icon} {sev:<7}  {term:<40} {source_hint}")

    print()
    return len(missing)


# ─── 6. MAIN ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python _audit_concepts.py <ch_file_or_glob> <alias_registry.md> [wiki_dir]")
        print("  ch_file_or_glob:   Path to _temp_chNN.md, or a glob like \"_temp_ch*.md\"")
        print("  alias_registry.md: Path to 00_Schema/alias_registry.md")
        print("  wiki_dir:          (Optional) Path to 03_Wiki/ for cross-referencing node files")
        sys.exit(1)

    ch_pattern = sys.argv[1]
    reg_path = sys.argv[2]
    wiki_path = sys.argv[3] if len(sys.argv) > 3 else None

    # Resolve glob
    files = sorted(glob.glob(ch_pattern))
    if not files:
        # Maybe it's a literal path
        if os.path.isfile(ch_pattern):
            files = [ch_pattern]
        else:
            print(f"[ERROR] No files found matching: {ch_pattern}")
            sys.exit(1)

    total_gaps = 0
    for f in files:
        total_gaps += run_audit(f, reg_path, wiki_path)

    print(f"\n{'='*60}")
    print(f"  SUMMARY: {len(files)} chapters audited, {total_gaps} total gaps found.")
    print(f"{'='*60}\n")
