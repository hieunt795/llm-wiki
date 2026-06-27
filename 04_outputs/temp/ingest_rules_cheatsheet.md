# Ingest Rules — Quick Reference (W2 & W5)

---

## 1. SOURCE ROUTING (Phase 0)

**Determine source type first:**

| Source Type | Label | Workflow | Location |
|-------------|-------|----------|----------|
| Books / textbooks | `[RAW-BOOK]` | **W2** (normal ingest) | `02_sources/books/` |
| Official docs (CB, IMF, BIS) | `[RAW-OFFICIAL]` | **W2** | `02_sources/official_reports/` |
| Academic papers / journals | `[RAW-ACADEMIC]` | **W2** | `02_sources/academic/` |
| Web articles, Substack, press | `[RAW-CLIP]` | **W5** (adversarial audit) | `02_sources/Clipping/` |
| LLM synthesis output (Gemini, ChatGPT) | `[RAW-DR-LLM]` | **W5** | `02_sources/deep-research/` |
| Blog, op-ed, no citations | `[RAW-OPINION]` | **W5** | `02_sources/Clipping/` |
| Unknown / miscellaneous | `[UNVERIFIED]` | **Triage first** | `02_sources/Inbox/` |

---

## 2. W2 WORKFLOW (Primary: Books, Official, Academic)

**4 Phases: A (Pre-flight) → B (Extraction) → C (Merge) → D (Sync)**

### Phase A — Pre-flight (Concept Mapping)
- Convert source to `.md` → `02_sources/`
- Create concept map → `04_outputs/[source]_concept_map.md`
- List key concepts, relationships, wiki gaps

### Phase B — Extraction (Surgical Merge)
**For each concept:**

1. Extract raw text via `exact_extractor.py` or manual section
2. Run `python librarian.py search "<concept>"` — check if node exists
3. **IF node exists:**
   - **Correct content** → UPDATE
     - Append to `source_refs[]`
     - Increase `confidence` if independent [RAW-BOOK/OFFICIAL/ACADEMIC]
     - NEVER replace existing content; augment only
   - **Identical** → SKIP
   - **Contradicts** → CREATE `03_wiki/contradictions/` node (type: contradiction)
     - Link bidirectionally
     - Specify axis: data / mechanism / conclusion
   - **Missing bridge** → ADD wikilink 2-way if related nodes exist

4. **IF node doesn't exist:**
   - SPAWN new node using Mode B template
   - `confidence: 1`, `status: draft` (until ≥2 sources)

### Phase C — Merge & Log
- Create/update node per `schema.md`
- Update `01_schema/log.md` with action type:
  - `[YYYY-MM-DD] SPAWN — NodeName — source [RAW-TYPE]`
  - `[YYYY-MM-DD] UPDATE — NodeName — what added — source`
  - `[YYYY-MM-DD] BRIDGE — NodeA ↔ NodeB — rationale`
  - `[YYYY-MM-DD] CONTRADICTION — NodeA vs NodeB — axis`

### Phase D — Sync
```bash
python librarian.py ingest
# OR manually:
python 05_scripts/_build_wiki_graph.py
python 05_scripts/gen_index.py
python 05_scripts/auto_bridge.py --force --backup
python 05_scripts/auto_synthesis.py --check --stale-only
```

---

## 3. W5 WORKFLOW (Secondary: Clips, LLM Output, Opinion)

**Phases: 0-T (Triage if needed) → A (Pre-flight + Classification) → B (Adversarial Audit) → C (Merge) → D (Sync)**

### Phase 0-T — INBOX TRIAGE (if source is `[UNVERIFIED]`)
1. Read frontmatter + first 50 lines
2. Check: URL? Author? Citations? Style? Date?
3. Assign label (see routing table above)
4. Get user confirmation before moving out of Inbox
5. Proceed to Phase A

### Phase A — Pre-flight + Classification
**A1. Confirm label:**
- Clipping: has `source:` URL + `author` → `[RAW-CLIP]`
- LLM output: no author / synthetic style → `[RAW-DR-LLM]`
- Opinion: URL but no citations in text → `[RAW-OPINION]`

**A2. Concept Map with Risk Flags:**
```
| Claim | Type | Citation? | Risk Flag |
|-------|------|-----------|-----------|
| "X causes Y via Z" | Causal | Y/N | CHECK-CONFLICT |
| "Rate is X%" | Data | Y/N | VERIFY-NUMBER |
| "Framework A means B" | Mechanism | Y/N | CHECK-AGREE |
```

Risk flags: `CHECK-CONFLICT` (check with books), `VERIFY-NUMBER` (verify numbers), `CHECK-AGREE` (check mechanism), `OK` (factual/contextual)

### Phase B — Adversarial Audit (CRITICAL DIFFERENCE FROM W2)
**For each claim with Risk Flag:**

```
→ python librarian.py search "<claim>"
→ Read top-3 wiki results
```

**IF claim agrees with wiki node:**
- Mark: AGREE
- When ingesting: EXPAND source_refs[], DON'T increase confidence
- (Clips/LLM don't get confidence bumps even if confirmed)

**IF claim conflicts with wiki node:**
- Mark: CONFLICT
- DON'T merge into existing node
- Route to Phase C-CONFLICT

**IF claim is new territory:**
- Mark: NEW-TERRITORY
- Route to Phase C-NEW (lower starting confidence)

**IF claim is opinion/perspective:**
- Route to Phase C-PERSPECTIVE

**Special [RAW-DR-LLM] check:**
- Find original citations in text
- If cited: treat as [WEB], verify URL is alive
- If not cited: label as `[LLM-E — unverified]`, don't cite directly

### Phase C — Merge (4 branches)

**C-AGREE: Confirms wiki (no conflict)**
- UPDATE: Add to `source_refs[]` (don't replace)
- NO confidence increase
- Add interesting examples/analogies to ## Worked Example section
- Log: `[YYYY-MM-DD] UPDATE — NodeName — added clip source — [RAW-CLIP]`

**C-CONFLICT: Contradicts wiki**
- Check: Is clip newer than book?
  - YES → Mark old node with `⚠️ [STALE SIGNAL]` + `[INGEST CANDIDATE]`
  - NO → Add note: "Contradicted by [clip] — older/unverified source"
- NEVER replace book data with clip data
- For mechanism/conclusion conflicts: SPAWN `03_wiki/contradictions/` node
- Log: `[YYYY-MM-DD] CONTRADICTION — NodeA vs NodeB — axis`

**C-NEW: Opens new territory**
- SPAWN node in appropriate folder (mechanisms/ / definitions/ / etc.)
- `confidence: 1`, `status: draft`
- Mark thesis: `[RAW-CLIP — not yet verified against books]`
- Log: `[YYYY-MM-DD] SPAWN — NodeName — source [RAW-CLIP]`
- Add to Active Debt: "Verify [[NodeName]] against RAW-BOOK"

**C-PERSPECTIVE: Opinion/analyst view**
- SPAWN `03_wiki/perspectives/` node
- `type: perspective`, `confidence: 2`
- Use attributed language: "Selon [Author], X parce que Y"
- Link to related mechanism nodes

### Phase D — Sync
```bash
python librarian.py ingest
```

---

## 4. KEY RULES

### Confidence Increment
- **W2 sources** (books/official/academic): confidence ↑ when independent corroboration
- **W5 sources** (clips/LLM): confidence does NOT increase; must verify with books first

### Writebacks
- **Max 3 writebacks per session** (to avoid drift)
- Always check for conflicts before merging

### Conflicting Claims
- NEVER merge into existing node if conflicting
- ALWAYS spawn `03_wiki/contradictions/` node instead
- Specify axis: data / mechanism / conclusion

### Unverified Numbers
- [RAW-CLIP] with numbers → verify source
- [RAW-DR-LLM] with numbers → find original citation or mark `[LLM-E — unverified]`
- Don't cite unverified numbers directly

### Bridge & Related Links
- After ingest, check if new node should link to existing concepts
- Add 2-way wikilinks
- Rebuild graph: `python librarian.py sync`

---

## 5. W2 vs W5 QUICK COMPARISON

| Feature | W2 Books | W5 Clips/LLM |
|---------|----------|-------------|
| Confidence bump when confirmed? | ✅ Yes | ❌ No |
| Numbers cited directly? | ✅ Yes | ❌ Verify first |
| Conflict → merge into node? | ❌ Create contradiction | ❌ Create contradiction |
| Starting confidence (new territory) | 1 (↑ with RAW) | 1 (must verify with books) |
| Mechanism claims → trust level | High | Medium (need corroboration) |
| Adversarial audit required? | ❌ No | ✅ Yes, always |

---

## 6. EXECUTION CHECKLIST

**When ingesting a new source:**

- [ ] Phase 0: Determine source type & label
- [ ] Phase A: Create concept map with risk flags (W5 only)
- [ ] Phase B: Extract content, search each concept
  - [ ] If node exists: UPDATE / SKIP / CONFLICT / BRIDGE?
  - [ ] If node doesn't exist: SPAWN
- [ ] Phase C: Write node(s) per schema.md, log action in `01_schema/log.md`
- [ ] Phase D: Run `python librarian.py ingest` (or manual sync)
- [ ] Verify: `python librarian.py status` shows node count increase
- [ ] Update memory.md if: new high-value source found, confidence patterns emerge, or conflict axis discovered

---

## 7. COMMON PITFALLS

❌ **Merging conflicting claims into existing node** → Create contradiction node instead  
❌ **Bumping confidence on W5 confirmation** → W5 sources don't increase confidence  
❌ **Citing LLM numbers without verification** → Mark as `[LLM-E — unverified]` first  
❌ **Skipping adversarial audit for clips** → W5 requires audit before merge  
❌ **Forgetting to log action** → Always update `01_schema/log.md`  
❌ **Replacing old content** → UPDATE/AUGMENT only; never replace with new source  
❌ **Not creating bidirectional links** → Always add Related section with 2-way wikilinks  

---

## 8. SAVING TO MEMORY

Once ingest rule nuances emerge or patterns are discovered, save to:
```
C:\Users\ASUS\.claude\projects\E--Wiki-Link\memory\
```

Example memory entries:
- "W5 contradictions about rate transmission mechanisms—check vs UMM framework"
- "Clips from Substack often have exaggerated CDS spreads—always verify vs CB data"
- "DR-LLM outputs on emerging markets confidence: start at 1, require ≥2 book sources to increment"
