# STRICT RULES FOR RAW SOURCE INGEST

**Version:** 1.1 (2026-05-06)  
**Status:** MANDATORY — All ingest must comply with these rules or fail audit.

**Governing Philosophy: Evergreen Notes**
> Every wiki node is an **Evergreen Note** — concept-oriented, not source-oriented. A node represents *what is known about a concept*, accumulated from all sources over time. It is never a summary of one source. Sources enrich the node; the node belongs to the concept.

---

## RULE 0: PRE-INGEST CONCEPT CHECK (Mandatory First Step)

**Before creating any new node, search the wiki for existing coverage.**

**Workflow:**
1. **Search wiki:** `python librarian.py search "<concept>"` OR `grep -r "concept-name" 03_wiki/`
2. **Analyze results:**
   - **Exact match found:** UPDATE existing node (append source_refs, enrich content)
   - **Related coverage found:** CREATE cross-reference link, check for conflicts
   - **Conflict detected:** CREATE contradiction node (per Rule 9), never overwrite
   - **No match found:** Proceed to ingest as new node

**Common Search Targets:**
- Title (exact): e.g., "Credit Default Swaps"
- Aliases: e.g., "CDS", "credit insurance"
- Concept variants: e.g., "Interest Rate Swap", "IRS", "fixed-for-floating"

**RULE 0-STRICT:**
- ❌ Never create duplicate node without checking aliases + title variations
- ❌ Never overwrite existing content when updating; append to source_refs[] instead
- ✅ Always perform search BEFORE creating node
- ✅ If dual coverage justified (complementary lenses): add bidirectional cross-references
- ✅ Log conflict resolution in `01_schema/log.md`

---

## RULE 1: SOURCE ROUTING (Zero Exceptions)

**First step:** Determine source type. No ingest begins without classification.

| Source Type | Required Label | Folder | Workflow | Trust Level |
|-------------|---|---|---|---|
| Published textbook (author + publisher clear) | `[RAW-BOOK]` | `02_sources/books/` | W2 | ⭐⭐⭐⭐⭐ |
| Official document (CB, IMF, BIS, government) | `[RAW-OFFICIAL]` | `02_sources/official_reports/` | W2 | ⭐⭐⭐⭐⭐ |
| Peer-reviewed journal or working paper | `[RAW-ACADEMIC]` | `02_sources/academic/` | W2 | ⭐⭐⭐⭐⭐ |
| Web article, Substack, financial press (dated, author clear) | `[RAW-CLIP]` | `02_sources/Clipping/` | W5 | ⭐⭐⭐ |
| LLM synthesis output (Gemini, ChatGPT, no clear author) | `[RAW-DR-LLM]` | `02_sources/deep-research/` | W5 | ⭐⭐ |
| Blog, op-ed, commentary (no citations) | `[RAW-OPINION]` | `02_sources/Clipping/` | W5 | ⭐⭐ |
| Unknown origin or no metadata | `[UNVERIFIED]` | `02_sources/Inbox/` | **MUST TRIAGE FIRST** | ⚠️ |

**RULE 1-STRICT:**
- ❌ Never skip routing. Unknown sources go to Inbox, do NOT ingest directly.
- ❌ Never mix source types (e.g., don't label academic paper as [RAW-CLIP]).
- ✅ When in doubt about classification, triage to Inbox first.

---

## RULE 2: FRONTMATTER COMPLETENESS (All Fields Non-Negotiable)

Every node MUST have ALL 13 frontmatter fields. No omissions.

```yaml
---
title:              # REQUIRED — exact match filename stem
aliases:            # REQUIRED — list, can be [] but never null
type:               # REQUIRED — one of: concept/definition/mechanism/relationship/convention/perspective/evidence/domain/glossary/contradiction/synthesis
tags:               # REQUIRED — ≥1 tag, lowercase-hyphenated
status:             # REQUIRED — draft/reviewed/verified/stale/archived/conflict
confidence:         # REQUIRED — integer 1–5 (see scale below)
half_life_years:    # REQUIRED — number matching content type (see scale below)
school:             # REQUIRED — perspective-specific OR "" (empty string)
superseded_by:      # REQUIRED — null OR "NodeName" (never missing)
superseded_date:    # REQUIRED — null OR "YYYY-MM-DD" (never missing)
expert_lens:        # REQUIRED — pipe-separated OR "" (empty string, never null)
provenance:         # REQUIRED — short source description
thesis:             # REQUIRED — 1 sentence, 20–60 words, condition + mechanism
source_refs:        # REQUIRED — list [] (never null, never [""])
created:            # REQUIRED — "YYYY-MM-DD"
updated:            # REQUIRED — "YYYY-MM-DD" (update on every write)
---
```

**RULE 2-STRICT:**
- ❌ `null` is FORBIDDEN in lists. Use `[]` for empty.
- ❌ `""` (empty string) is FORBIDDEN where list expected. Use `[]`.
- ❌ Missing fields = fail pre-publish audit.
- ✅ Every field present, even if empty string or `null` (where allowed).

---

## RULE 3: CONFIDENCE SCALING (No Estimation)

Confidence is determined ONLY by source composition. Not by author opinion.

| Score | Definition | Valid source config | Raw Requirement |
|---|---|---|---|
| 1 | Very low | [LLM] only, no RAW | source_refs: [] |
| 2 | Low | [LLM] + partial RAW OR [WIKI] cross-ref only | source_refs: [] OR 1 RAW-CLIP |
| 3 | Medium | [WIKI] internal cross-references | source_refs: [] (internal only) |
| 4 | High | ≥1 RAW-BOOK / RAW-OFFICIAL / RAW-ACADEMIC | source_refs: ≥1 RAW entry |
| 5 | Verified | ≥2 INDEPENDENT RAW sources agree | source_refs: ≥2 RAW entries, MUST cite both |

**RULE 3-STRICT:**
- ❌ Confidence 4+ requires RAW backing. No exceptions.
- ❌ [RAW-CLIP] alone cannot reach confidence 4 (only 3 max).
- ❌ [RAW-DR-LLM] alone cannot reach confidence 4.
- ❌ Multiple citations of SAME source (e.g., Tuckman pages 45 + 110) = counts as 1 source, not 2.
- ✅ If confidence ≥ 4: source_refs MUST list ≥1 RAW file with page number.

---

## RULE 4: HALF-LIFE ASSIGNMENT (Mechanism-Based)

Half-life is **not** subjective. Determined by content type.

| Content Type | half_life_years | Examples |
|---|---|---|
| Mechanism / Theory | 10 | Transmission channels, pricing models, framework theory |
| Regulatory / Policy | 1 | Basel III, ISDA standards, CB policy frameworks (change annually) |
| Market Data / Rates | 0.1 | Specific interest rates, prices, spreads (stale within weeks) |
| Synthesis / Wisdom | 0.5 | Wisdom run outputs, derived insights (re-run when inputs change) |
| Domain Context | 3 | Country macro profiles, institutional structure |

**RULE 4-STRICT:**
- ❌ Never use 2, 5, 7, or any other value. Only use table above.
- ❌ Personal judgment overrides forbidden. Use content type first.
- ✅ When unclear, default to broader type: Mechanism (10) > Domain (3) > Synthesis (0.5).

---

## RULE 5: THESIS STANDARD (Non-Negotiable)

Thesis is the most critical field. It drives search ranking (×4 weight) and graphify labeling.

**Format Requirements:**
- ✅ **Exactly 1 sentence** (no periods in middle, no bullet points)
- ✅ **20–60 words** (minimum 20, maximum 60)
- ✅ **Contains mechanism, not just description** (verb = "operates", "forces", "causes"; not "is", "describes")
- ✅ **Includes ≥1 condition** (if, when, under, during, as, when)
- ✅ **Different from title** (thesis = core claim, title = label)
- ✅ **English preferred** (bilingual: "EN / VI" acceptable for perspectives only)

**Examples:**

❌ **BAD** — Too short, no mechanism
```
thesis: "Repo is a sale + repurchase agreement."
```

❌ **BAD** — Description, not mechanism
```
thesis: "The LCR is a regulatory ratio requiring banks to hold high-quality liquid assets."
```

❌ **BAD** — No condition
```
thesis: "Carry trades unwind when volatility spikes."
```

✅ **GOOD** — Condition + mechanism + effect
```
thesis: "When volatility exceeds historical bands, yen carry trades unwind as hedging costs rise, forcing speculators to close short-yen positions and triggering yen appreciation."
```

✅ **GOOD** — Transmission chain visible
```
thesis: "Under fiscal dominance, sovereign refinancing needs force central banks to suppress long-term yields via QE, creating financial repression that erodes real returns and incentivizes search-for-yield behavior among investors."
```

**RULE 5-STRICT:**
- ❌ Vague words forbidden: "many", "several", "often", "some", "depends on multiple factors" (without specifics)
- ❌ No conjunctions joining two separate claims (no "X and Y both occur")
- ❌ Thesis <20 words = fail audit
- ❌ Thesis >60 words = fail audit
- ✅ Run thesis through claim auditor before publish

---

## RULE 6: SOURCE_REFS FORMAT (Machine-Read)

`source_refs` is parsed by `wiki_search.py` and `claim_auditor.py`. Format must be exact.

**Correct format:**
```yaml
source_refs:
  - file: "Perry_Warjiyo_Central_Bank_Policy_Ch4.md"
    page: 156
  - file: "Tuckman_Serrat_Fixed_Income_2022.md"
    page: "§10.3"
```

**Format rules:**
- ✅ `file:` ALWAYS the **exact basename** of a file in `02_sources/` (any subdirectory)
- ✅ `page:` integer OR string (e.g., "§10.3", "Ch4.1")
- ✅ Empty list: `source_refs: []` (valid for draft nodes with confidence ≤ 2)
- ❌ `null` — NEVER valid. Use `[]` instead.
- ❌ Bare string: `source_refs: ["Filename.md"]` — INVALID
- ❌ Missing `file:` key: `source_refs: [{page: 45}]` — INVALID
- ❌ `page: 0` — use omit page entirely (not page: 0)
- ❌ `page: null` — use omit page entirely

**Common errors:**
```yaml
# ❌ BAD — null
source_refs: null

# ❌ BAD — bare string
source_refs: ["Filename.md"]

# ❌ BAD — page without file
source_refs:
  - page: 45

# ✅ GOOD — empty draft
source_refs: []

# ✅ GOOD — with page
source_refs:
  - file: "Bindseil_Monetary_Policy_Ch8.md"
    page: 112
```

**RULE 6-STRICT:**
- ❌ File basename must exactly match filename in `02_sources/`. No typos.
- ❌ If file doesn't exist in `02_sources/`, ingest fails immediately.
- ✅ Verify file exists before writing node.

---

## RULE 7: CITATION LABELS IN BODY TEXT

Every claim in body text MUST be labeled. No unlabeled claims.

**Label hierarchy (trust order):**
```
[RAW-BOOK:SourceName p.X]        ← Trust level 5
[RAW-OFFICIAL:SourceName]        ← Trust level 5
[RAW-ACADEMIC:AuthorYYYY]        ← Trust level 5
[RAW-CLIP:source]                ← Trust level 3
[RAW-DR:SourceName]              ← Trust level 2
[WIKI]                           ← Trust level 3 (cross-ref)
[WEB-YYYY-MM-DD:url]             ← Trust level 2 (ephemeral)
[LLM]                            ← Trust level 1 (unverified)
[LLM-S]                          ← Trust level 1 (synthesis)
```

**RULE 7-STRICT:**
- ❌ Claim without label = fail audit
- ❌ Unlabeled numbers = immediate rejection
- ❌ [LLM] placeholder without explicit "Placeholder — mechanism not yet sourced" note = fail
- ✅ Every sentence/paragraph starts with label
- ✅ [WEB] MUST include date: [WEB-YYYY-MM-DD:url]

**Examples:**
```markdown
# BAD — no label
"The DV01 of a bond equals the negative of the first derivative of price with respect to yield."

# GOOD — labeled
[RAW-BOOK:Tuckman_Serrat p.45] The DV01 of a bond equals the negative 
of the first derivative of price with respect to yield.

# BAD — [LLM] without note
[LLM] Fiscal dominance occurs when...

# GOOD — [LLM] with note
[LLM] Placeholder — mechanism not yet sourced from RAW. Confidence: 1.
Fiscal dominance occurs when...
```

---

## RULE 8: FORBIDDEN PATTERNS (Will Fail Audit)

These patterns indicate vague thinking. Do NOT use.

❌ **"ảnh hưởng nhiều kênh" (affects many channels)**  
→ MUST specify channels

❌ **"phụ thuộc vào nhiều yếu tố" (depends on many factors)**  
→ MUST list factors and conditions

❌ **"thường hoạt động theo..." (typically operates)**  
→ MUST define when it applies, when it doesn't

❌ **"có thể tăng/giảm" (can increase/decrease)**  
→ MUST specify direction and condition

❌ **Claim without source label**  
→ MUST add [...] prefix

❌ **Multiple independent claims in one sentence**  
→ MUST split into separate sentences with separate labels

---

## RULE 9: CONFLICT HANDLING (Zero Tolerance for Overwrites)

When new source contradicts existing node: CREATE CONTRADICTION NODE. Never overwrite.

**Decision tree:**

```
New source AGREES with existing node?
  → UPDATE source_refs[] (append, don't replace)
  → NO confidence bump if source is [RAW-CLIP] or [RAW-DR-LLM]
  → Confidence bump if source is [RAW-BOOK] + independent

New source CONTRADICTS existing node?
  → SPAWN 03_wiki/contradictions/NodeName.md
  → type: contradiction
  → Link bidirectionally
  → Specify axis: data / mechanism / conclusion
  → DO NOT merge contradicting claim into original node

New source is in NEW TERRITORY (no existing node)?
  → SPAWN new node in appropriate folder
  → confidence: 1 (single non-RAW-BOOK source)
  → status: draft
  → Add to Active Debt: "Verify [[NodeName]] against RAW-BOOK"
```

**RULE 9-STRICT:**
- ❌ Never merge contradicting claim into existing node
- ❌ Never replace old source data with new source
- ✅ Always create contradiction node when conflict detected
- ✅ Archive old node only if NEW source has ≥2 independent RAW backing

---

## RULE 10: WRITE-BACK ACTIONS (Limited to 5 Per Session)

After Phase B extraction, choose exactly ONE action per concept.

| Action | Trigger | Log Format |
|--------|---------|---|
| **SPAWN** | Node doesn't exist | `[YYYY-MM-DD] SPAWN — NodeName — source [RAW-TYPE]` |
| **UPDATE** | Node exists + new source confirms + no contradiction | `[YYYY-MM-DD] UPDATE — NodeName — what added — source` |
| **BRIDGE** | Two nodes exist but missing wikilink | `[YYYY-MM-DD] BRIDGE — NodeA ↔ NodeB — rationale` |
| **CONFLICT** | New source contradicts existing node | `[YYYY-MM-DD] CONTRADICTION — NodeA vs NodeB — axis` |
| **SYNTHESIS** | Output from wisdom run | `[YYYY-MM-DD] SYNTHESIS — tag — result` |

**RULE 10-STRICT:**
- ❌ Max 5 write-back actions per session (prevent drift)
- ❌ Never perform both UPDATE and SPAWN on same concept in same session
- ✅ Log EVERY action in `01_schema/log.md`
- ✅ Run `python librarian.py sync` after each session to rebuild graph + indexes

---

## RULE 11: W5 SPECIFIC (Secondary Sources: Clips, LLM Output)

W5 sources must pass ADVERSARIAL AUDIT before any write-back.

**Before ingesting any [RAW-CLIP] or [RAW-DR-LLM] claim:**

1. **Search wiki:**  
   `python librarian.py search "<claim>"`

2. **Audit result:**
   - AGREE with wiki node? → UPDATE source_refs[], NO confidence bump
   - CONFLICT with wiki node? → CREATE contradiction node, do NOT merge
   - NEW territory? → SPAWN with confidence 1, mark as [RAW-CLIP — unverified]

3. **Special rule for [RAW-DR-LLM] numbers:**
   - ✅ If LLM cites source: find original citation, verify URL alive
   - ❌ If LLM doesn't cite: label `[LLM-E — unverified]`, do NOT cite directly

**RULE 11-STRICT:**
- ❌ Never bump confidence on W5 source confirmation
- ❌ Never cite unverified LLM numbers
- ✅ Always perform adversarial audit before W5 write-back
- ✅ Use contradiction node for W5 conflicts, never merge

---

## RULE 12: PRE-PUBLISH AUDIT CHECKLIST

Before any node is published, run this checklist. Fail any item = do not publish.

```
FRONTMATTER:
  [ ] Title matches filename stem exactly
  [ ] All 13 mandatory fields present (no missing)
  [ ] No null values in lists (use [])
  [ ] confidence: integer 1–5
  [ ] status: valid value (draft/reviewed/verified/stale/archived/conflict)
  [ ] half_life_years: one of {10, 3, 1, 0.5, 0.1}
  [ ] thesis: 20–60 words, condition + mechanism, differs from title
  [ ] source_refs: list (not null), each item has 'file' key
  [ ] If confidence ≥4: source_refs has ≥1 RAW entry

BODY:
  [ ] H1 heading = # [[Node_Stem]]
  [ ] Every claim has [...] citation label
  [ ] No forbidden vague patterns
  [ ] Related section has ≥1 wikilink
  [ ] All source_refs files exist in 02_sources/
  [ ] No unlabeled numbers or data
  [ ] [LLM] placeholders have explicit "not yet sourced" note

METADATA:
  [ ] updated: field = today's date
  [ ] Log entry added to 01_schema/log.md with action type
  [ ] Node type appropriate for content
  [ ] Tags are lowercase-hyphenated
```

**RULE 12-STRICT:**
- ❌ Fail audit if ANY checklist item unchecked
- ✅ Run audit via: `python librarian.py audit 03_wiki/path/NodeName.md`
- ✅ Fix all issues before merging

---

## RULE 13: VERSION PERSISTENCE (Never Erase Context)

The wiki accumulates knowledge. Never erase it.

**When new source augments existing node:**
- ✅ Append to Worked Example section with new source label
- ✅ Append to source_refs[]
- ❌ Do NOT delete old content
- ❌ Do NOT replace old example with newer one

**Example of persistence:**

```markdown
## 2. Worked Example

[RAW-BOOK:Tuckman_Serrat p.45] Example 1: Bond DV01 calculation.
The 5-year TNOTE has duration 4.2 years...

[RAW-CLIP:Bloomberg_2026-05-01] Example 2: Recent market data.
On May 1, 2026, the 5-year yield was 4.25% with DV01 = $42.30...

[LLM-S] Both examples demonstrate that DV01 increases with duration
and decreases with coupon rate.
```

---

## QUICK REFERENCE: ENFORCEMENT

| Violation | Consequence |
|-----------|-------------|
| **Skipping pre-ingest check (Rule 0)** | **Ingest FAIL — must search wiki first** |
| Creating duplicate without searching | Ingest FAIL — node must be verified unique |
| Overwriting existing node | Audit fail, must create contradiction node |
| Missing frontmatter field | Node fails audit, cannot publish |
| confidence ≥4 without RAW source | Audit fail, automatic downgrade to confidence 3 |
| Thesis <20 or >60 words | Audit fail |
| Unlabeled claim | Audit fail |
| source_refs: null | Audit fail |
| >5 write-backs per session | Rollback last 2–3 actions |
| [RAW-CLIP] without adversarial audit | W5 audit fail |

---

## SUMMARY: THE STRICT PIPELINE

0. **PRE-INGEST CHECK** → Search wiki first, verify concept doesn't exist
1. **SOURCE ROUTING** → Classify, never skip
2. **FRONTMATTER** → All 13 fields, no omissions
3. **CONFIDENCE** → Determined by source only
4. **HALF-LIFE** → Matched to content type
5. **THESIS** → 1 sentence, 20–60 words, mechanism
6. **SOURCE_REFS** → Exact format, file must exist
7. **BODY LABELS** → Every claim labeled
8. **CONFLICT** → Create contradiction node, never overwrite
9. **W5 AUDIT** → Adversarial check before write-back
10. **PRE-PUBLISH** → Run checklist, fail any item = no publish
11. **LOGGING** → Every action in log.md
12. **SYNC** → Rebuild graph after session

**Non-negotiable: If ANY rule violated, ingest fails.**
