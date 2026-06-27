# MULTI-SOURCE INGESTION RULES (Evergreen Notes)
## When Multiple Sources Explain the Same Concept Differently

**Governing Philosophy: Evergreen Notes**
> A node = an Evergreen Note. It is concept-oriented, not source-oriented. Multiple sources accumulate into one note over time. The question is always: *"What does the concept say?"* — not *"What did Book1 say?"*

**Problem:** Wiki has node A from Book1. Now Book2, Paper1, Official Doc all discuss A — but with different approaches, emphases, or interpretations. Current rules don't handle this well.

**Goal:** Capture different angles without losing data, flag tension, enhance rather than flatten.

---

## RULE M1: PERSPECTIVE DIVERSITY DETECTION

When ingesting new source on existing concept, **first classify the difference**.

### M1a: Type of Difference Matrix

| Difference Type | Example | Action |
|---|---|---|
| **ANGLE** | Book1: "Carries occur due to interest rate differential" vs Book2: "Carries occur due to basis trade asymmetry" (same phenomenon, different mechanism emphasis) | Expand node with "Dual Mechanism" section |
| **EMPIRICAL EVIDENCE** | Book1: "Data from 1990-2000" vs Paper1: "Data from 2020-2025" (same claim, different time period) | Add "Temporal Evolution" section |
| **PRECONDITION** | Book1: "Carry trade works when market is liquid" vs Official Doc: "Carry trade works when CB rates stay flat ≥2 years" (same effect, different triggers) | Add "Conditional Validity" section |
| **SCOPE** | Book1: "Applies to USD/JPY" vs Paper1: "Applies to all emerging market pairs" (scope difference) | Generalize node, add scoping section |
| **CONTRADICTION** | Book1: "Carry unwinds when rates rise" vs Paper1: "Carry persists even when rates rise if vol stays down" (actual conflict) | Create contradiction node |
| **DETAIL LEVEL** | Book1: "Yen carry is important" (overview) vs Paper1: "Yen carry involves 8 distinct mechanisms in credit/FX/rate space" (deep dive) | Expand "Core Logic" section with granular mechanisms |
| **NORMATIVE VS POSITIVE** | Book1: "Carry should be arbitraged away" (theoretical ideal) vs Practice: "Carry persists due to [frictions]" (real world) | Create separate "Theory vs Practice" section |
| **REGIME DEPENDENCY** | Book1: "Carry trade mechanics (always true)" vs Paper1: "Carry trade only viable in Regime A, fails in Regime B" (same mechanism, different boundary) | Add "Regime Dependency" section |

**RULE M1-STRICT:**
- ❌ Don't assume "same concept" = "same explanation"
- ✅ Classify difference type BEFORE deciding write-back action
- ✅ Read both sources in full before classification

---

## RULE M2: WHEN TO EXPAND vs WHEN TO CONTRADICT

Decision tree for multi-source same-concept scenario.

```
Does New Source Agree with Existing Node's Core Mechanism?

YES, same mechanism but different angle/emphasis?
  → EXPAND (add new section with different perspective label)
  → M2a: Angle expansion
  → M2b: Scope expansion
  → M2c: Evidence temporal expansion
  
YES, same mechanism but adds CONDITIONAL VALIDITY?
  → EXPAND with "Conditional Validity" section
  → M2d: Precondition expansion
  
YES, same mechanism but disagrees on WHEN it applies?
  → EXPAND with "Regime Dependency" or "Boundary Conditions"
  → M2e: Scope/boundary expansion

YES, same claim but different DETAIL LEVEL?
  → EXPAND "Core Logic" to add granular mechanisms
  → M2f: Granularity expansion

NO, contradicts on core mechanism or empirical fact?
  → CREATE CONTRADICTION NODE
  → Axis: mechanism / empirical / precondition
```

**RULE M2-STRICT:**
- ❌ Don't create contradiction node for angle/emphasis differences
- ❌ Don't expand when there's actual mechanism conflict
- ✅ Expand = add labeled section; Contradict = separate node
- ✅ If unsure, expand first; can split into contradiction later

---

---

## EXPANSION RULES: How Evergreen Notes Grow (M3–M9)

> An Evergreen Note grows by **accumulating angles**, not by replacing content.  
> Each rule below defines one growth pattern. The concept owns the note — sources enrich it.  
> Never start with *"what did this source say?"* — start with *"what does the concept now know?"*

---

## RULE M3: ANGLE EXPANSION (Different Lens, Same Mechanism)

**Scenario:** Book1 says "Carry trades via interest rate spread". Paper1 says "Carry trades via basis trade mechanics".

Both true. Different entry point to same phenomenon.

### M3a: Template for Angle Expansion

**Existing node structure:**
```markdown
## 1. Core Logic
[RAW-BOOK:Book1 p.45] The mechanism is: borrow cheap currency → invest in 
higher-yielding asset → profit from spread.
```

**After new source with different angle:**
```markdown
## 1. Core Logic

### Angle A: Interest Rate Differential (Carry Premium)
[RAW-BOOK:Book1 p.45] Borrow JPY @ 0%, invest USD @ 5% → 500 bps carry.

### Angle B: Basis Trade Mechanics (Cross-Currency Basis)
[RAW-PAPER:Paper1 2024] The same trade viewed through basis lens: USD/JPY 
spot traded vs. cross-currency basis, creating arbitrage opportunity that 
duplicates carry profit but via different accounting.

### Synthesis [LLM-S]
Both angles describe the same economic phenomenon. Angle A emphasizes the 
funding cost perspective; Angle B emphasizes the valuation divergence 
perspective. Practitioners use Angle B (basis) for execution because it 
isolates the true arbitrage opportunity.
```

**RULE M3-STRICT:**
- ✅ Add new subsection under "Core Logic" for new angle
- ✅ Keep old angle intact; don't replace
- ✅ Label each angle with its source
- ✅ Add LLM-S synthesis explaining why both coexist
- ❌ Don't merge angles into one paragraph
- ❌ Don't claim one is "more correct"

---

## RULE M4: SCOPE EXPANSION (Same Mechanism, Different Geography/Asset Class)

**Scenario:** Book1: "Yen carry trade (USD/JPY)" vs Paper1: "Carry trade applies to all emerging market currency pairs".

### M4a: Template for Scope Expansion

**Existing:**
```markdown
## 1. Core Logic
[RAW-BOOK:Book1 p.45] The yen carry trade operates when...
```

**After new source with broader scope:**
```markdown
## 1. Core Logic
[RAW-BOOK:Book1 p.45] **Case 1: Yen Carry (USD/JPY)**
The mechanism is: borrow JPY @ near-0% → invest USD @ 5%.

[RAW-PAPER:Paper1 2024] **Case 2: Generalized Emerging Market Carry**
The same mechanism applies to [BRL, INR, MXN, etc.] when:
  - Funding currency has low policy rate (>200 bps below USD)
  - Receiving currency has illiquid forward market (bid-ask >10 bps)
  - Hedge cost through currency swaps <100 bps
When these conditions hold, carry trade spans all EM pairs, not just JPY.

### Scoping Rule [LLM-S]
Yen carry is the PROTOTYPE case because:
  ✓ JPY has largest negative rate gap (0% vs 5%)
  ✓ JPY/USD spot is most liquid globally (smallest bid-ask)
  → Makes carry visible first in JPY
  
But mechanism is GENERAL to any currency pair with sufficient rate gap 
+ adequate liquidity.
```

**RULE M4-STRICT:**
- ✅ Create subsections for each scope (Case 1, Case 2, etc.)
- ✅ Generalize thesis to reflect both specific + general cases
- ✅ Identify WHY one case is prototype (most liquid, largest gap, etc.)
- ❌ Don't replace "yen carry" with "general emerging market carry"
- ❌ Don't create separate nodes for each currency pair

---

## RULE M5: TEMPORAL EVOLUTION (Same Mechanism, Different Time Periods)

**Scenario:** Book1 (2015): "Yen carry was dominant in 2003-2012" vs Paper1 (2024): "Yen carry re-emerged in 2022-2026".

### M5a: Template for Temporal Expansion

**Existing:**
```markdown
## 2. Worked Example
[RAW-BOOK:Book1 p.156] 2003-2004: Japan intervened ¥35T over 15 months
```

**After new source with new time period:**
```markdown
## 2. Worked Example

### Episode 1: The Original Yen Carry (2003-2007)
[RAW-BOOK:Book1 p.156] Japan spent ¥35T to defend weak yen. Global carry 
traders borrowed ¥ at 0%, invested in AUD/NZD/USD, earning 300-400 bps. 
Duration: 4 years. Unwound during 2008 GFC.

### Episode 2: Post-Crisis Carry (2010-2019)
[RAW-ACADEMIC:Smith2020] Carry re-emerged after rates bottomed in 2010 but 
with lower leverage and shorter duration due to regulatory changes (Dodd-Frank).

### Episode 3: The New Yen Carry (2022-2026)
[RAW-PAPER:Paper1 2024] Re-emergence driven by Fed tightening (5% vs BOJ 0%), 
creating 500 bps gap. Scale larger than Episode 1 but with different structure:
  - More algorithmic hedging
  - More presence in emerging markets (not just JPY)
  - Faster unwinding cycles (weeks, not years)

### Evolution Analysis [LLM-S]
The mechanism (exploit rate differential) is CONSTANT. But:
  - Structural funding costs have fallen (market deepened)
  - Regulatory constraints changed (higher capital requirements)
  - Unwinding speed increased (more algorithmic execution)
→ Same mechanism, different RISK PROFILE across episodes
```

**RULE M5-STRICT:**
- ✅ Create subsections per episode with date ranges
- ✅ Highlight what's SAME (mechanism) vs DIFFERENT (structure, speed, scale)
- ✅ Add "Evolution Analysis" explaining why mechanics change
- ❌ Don't assume "old data outdated"; data from different regimes both valid
- ❌ Don't merge episodes; keep temporal separation explicit

---

## RULE M6: PRECONDITION EXPANSION (Same Effect, Different Triggers)

**Scenario:** Book1: "Carry works when rates stable" vs Official Doc: "Carry viable when CB committed to flat rates ≥2 years".

### M6a: Template for Precondition Expansion

**Existing:**
```markdown
## Failure Conditions
[RAW-BOOK:Book1 p.200] Carry trades unwind when rates rise sharply.
```

**After new source with granular preconditions:**
```markdown
## Conditional Validity

### Precondition Set 1: Rate Stability (Book1 framework)
[RAW-BOOK:Book1 p.200] Carry trades exist when rates are expected stable.
Trigger unwinding: rates rise sharply.

### Precondition Set 2: Central Bank Forward Guidance (Official framework)
[RAW-OFFICIAL:BOJ 2024] Carry trades sustained by CB commitment.
Specific condition: BOJ maintained 0% rate guidance ≥2 years forward.
Trigger unwinding: CB signals imminent rate hike OR removes forward guidance.

### Precondition Set 3: Market Liquidity (Paper framework)
[RAW-PAPER:Paper1 2024] Carry trades collapse when funding liquidity dries.
Specific condition: JPY Libor spread vs SOFR <50 bps (market functioning).
Trigger unwinding: spread widens >100 bps (market stress).

### Precondition Map [LLM-S]
| Precondition | Source | Test | Failure Signal |
|---|---|---|---|
| Rate stability | Book1 | Rates stay in band | Sharp move outside band |
| CB commitment | BOJ | Forward guidance ≥2y | Guidance withdrawn |
| Funding liquidity | Paper1 | Libor-SOFR <50bps | Spread >100bps |

All three preconditions can be true simultaneously (carry viable) or fail 
independently (carry at risk). Most recent unwinding (May 2026 yen intervention) 
suggests Precondition 2 (CB guidance) is MOST critical.
```

**RULE M6-STRICT:**
- ✅ Create Precondition Set subsections for each source's trigger conditions
- ✅ Create a Precondition Map table showing test / signal for each
- ✅ Highlight which precondition is MOST critical (data-driven, not opinion)
- ❌ Don't claim one precondition is "correct" without evidence
- ❌ Don't assume one source's precondition subsumes others

---

## RULE M7: REGIME DEPENDENCY (Same Mechanism, Different Validity Boundaries)

**Scenario:** Book1: "Carry trade mechanics (timeless theory)" vs Paper1: "Carry trade only viable in Low-Volatility Regime, breaks in High-Vol Regime".

### M7a: Template for Regime Dependency

**Existing:**
```markdown
## Core Logic
[RAW-BOOK:Book1 p.45] Carry trade = borrow cheap, lend expensive.
```

**After new source with regime dependency:**
```markdown
## Core Logic + Regime Dependency

### Mechanism (Regime-Independent)
[RAW-BOOK:Book1 p.45] The arbitrage opportunity: borrow JPY @ 0%, 
invest USD @ 5%.

### Regime A: Low-Volatility Regime (Mechanism Works)
[RAW-PAPER:Paper1 2024] When realized volatility <10% annualized:
  - Carry trade profitable
  - Unwind time: weeks to months
  - Leverage: 10-50x
  - Typical duration: sustained 2-3 years
  
[Example] 2010-2019 period: volatility averaged 8%, carry sustained.

### Regime B: High-Volatility Regime (Mechanism Breaks)
[RAW-PAPER:Paper1 2024] When realized volatility >20% annualized:
  - Carry trade becomes liability (hedging costs >400 bps)
  - Unwind time: days to hours
  - Leverage forced lower: 2-5x
  - Typical duration: unwound in 2-4 weeks
  
[Example] 2008 GFC (vol 80%+), March 2020 (vol 60%+): carry collapsed.

### Regime Boundary [LLM-S]
The mechanism is valid in both regimes. But PROFITABILITY and RISK 
depend critically on volatility regime:
  - Low Vol: Carry profitable (spread > hedge cost)
  - High Vol: Carry unprofitable (hedge cost > spread)
  
Therefore, same mechanism, DIFFERENT OUTCOME across regimes.
```

**RULE M7-STRICT:**
- ✅ Separate "Mechanism" (always true) from "Regime A/B" (outcome differs)
- ✅ Provide historical examples of each regime
- ✅ Identify BOUNDARY VARIABLE that triggers regime switch (volatility, rate move, etc.)
- ❌ Don't say mechanism "doesn't work" in High-Vol regime; say outcome differs
- ❌ Don't assume regime switches are rare; identify historical frequency

---

## RULE M8: DETAIL LEVEL EXPANSION (Overview vs Deep Dive)

**Scenario:** Book1 (overview): "Yen carry trades involve interest rate differential" vs Paper1 (deep dive): "Yen carry trades operate through 8 distinct sub-mechanisms: funding cost, basis, volatility smile, convexity, jump risk, financing-rate vol correlation, market microstructure, regulatory arbitrage".

### M8a: Template for Granular Mechanism Expansion

**Existing:**
```markdown
## 1. Core Logic
[RAW-BOOK:Book1 p.45] The mechanism is interest rate differential.
```

**After granular source:**
```markdown
## 1. Core Logic

### Level 1: High-Level Mechanism (Book1, overview)
[RAW-BOOK:Book1 p.45] Borrow JPY @ 0% → Invest USD @ 5% → 500 bps spread.

### Level 2: Granular Decomposition (Paper1, deep dive)
[RAW-PAPER:Paper1 2024] The 500 bps spread decomposes into:

| Sub-Mechanism | Basis Points | Driver | Duration |
|---|---|---|---|
| **1. Funding Cost** | 450 | Policy rate differential | Persistent |
| **2. Basis (CCS)** | 30 | USD/JPY tenor basis | Persistent |
| **3. Volatility Smile** | 15 | Implied vs realized vol | 3-month cycles |
| **4. Convexity** | 5 | Duration convexity hedge cost | Persistent |
| **5. Jump Risk** | 8 | Tail risk premium | Event-driven |
| **6. Financing-Rate Vol** | 12 | BOJ rate path uncertainty | 12-month cycles |
| **7. Microstructure** | 5 | Bid-ask in spot/FX swap | Persistent |
| **8. Regulatory Arbitrage** | 2-3 | Basel/FRTB incentive | Policy-dependent |
| **TOTAL** | 527 | | |

### Integration Analysis [LLM-S]
Book1 gives the ESSENTIAL mechanism (500 bps carry). Paper1 breaks down 
WHERE each bp comes from. Both correct at different detail levels.
- Level 1 (Book1) sufficient for understanding carry EXISTENCE
- Level 2 (Paper1) necessary for:
  - Predicting when carry becomes unprofitable (e.g., if vol doubles, loss 30 bps)
  - Identifying which factors drove recent unwinding
  - Hedging specific risks
```

**RULE M8-STRICT:**
- ✅ Create separate subsections for Level 1 (high) and Level 2 (granular)
- ✅ Use table to show decomposition when adding granular source
- ✅ Explain when each level is appropriate (understanding vs. execution)
- ❌ Don't replace Level 1 with Level 2; keep both
- ❌ Don't assume granular source is "more correct"; it's just more detailed

---

## RULE M9: NORMATIVE vs POSITIVE (Theory vs Practice)

**Scenario:** Book1 (theory): "Carry trades should be arbitraged away in efficient markets" vs Practice: "Carry trades persist for years despite being obvious".

### M9a: Template for Theory vs Practice

**Existing:**
```markdown
## Core Logic
[RAW-BOOK:Book1 p.45] Arbitrage efficiency suggests carry should disappear.
```

**After practice-based source:**
```markdown
## Core Logic + Reality Gap

### Theoretical Prediction (Book1: Efficient Markets)
[RAW-BOOK:Book1 p.45] If markets are efficient, carry trades should be 
arbitraged away. Any rate differential >transaction costs indicates market 
inefficiency.

### Empirical Reality (Papers 1-3: Actual Data)
[RAW-PAPER:Paper1 2024] Carry trades persisted continuously:
  - 2003-2007: 4 years with 300+ bps spread
  - 2010-2019: 9 years with 150+ bps spread (lower due to regulatory constraints)
  - 2022-2026: 4+ years with 450+ bps spread
  
Persistence timeline: ~17+ years across three episodes.

### Reconciliation: Why Theory ≠ Practice [LLM-S]
Theory assumes:
  ✗ Infinite capital available for arbitrage
  ✗ Zero transaction costs
  ✗ No regulatory constraints
  ✗ Perfect information
  ✗ No tail risk

Reality includes:
  ✓ Limited capital (leverage constraints)
  ✓ Transaction costs: 50-100 bps round-trip
  ✓ Regulatory constraints: Basel III, Dodd-Frank (reduced leverage)
  ✓ Information asymmetry: tail risk underpriced
  ✓ Carry trades ARE the arbitrage — they don't "disappear"; they become structural

**Corrected Model [LLM-S]:**
Carry trades are NOT market inefficiencies to arbitrage away.
They ARE the mechanism through which rate differentials get exploited.
The mechanism persists because arbitrage capital is constrained, not because 
markets are inefficient.
```

**RULE M9-STRICT:**
- ✅ Create "Theory" and "Reality" subsections
- ✅ List specific assumptions of theory, reality violations explicitly
- ✅ Add "Reconciliation" section explaining the gap
- ✅ Update thesis of node if theory-practice gap is LARGE
- ❌ Don't claim "theory is wrong"; say "theory assumes conditions not met"
- ❌ Don't ignore empirical contradiction; flag it prominently

---

## RULE M10: WHAT TO DO WHEN SOURCES CONTRADICT ON DETAILS

**Scenario:** Book1 says "Yen carry unwinds when rates rise" vs Paper1 says "Yen carry persists even when rates rise if vol stays low".

### M10a: Decision Tree for Detail Contradiction

```
Sources disagree on detail (not core mechanism)?

Disagreement about:
  ✓ Timing (when does X occur?)     → Temporal/regime expansion
  ✓ Magnitude (how much?)            → Empirical expansion
  ✓ Trigger (what causes unwinding?) → Precondition expansion
  ✓ Boundary (when does rule break?) → Regime dependency expansion

All valid simultaneously or different time periods?
  → Expand with temporal/regime sections
  
One clearly more recent than other?
  → Flag older view as potentially stale
  → Add recency note: "[RAW-PAPER: 2024 data supersedes Book1 2003]"
  
One is theory, one is practice?
  → Create Theory vs Practice section
  
Truly incompatible (one = true, one = false)?
  → Create CONTRADICTION node
  → Specify empirical test to resolve
```

**RULE M10-STRICT:**
- ❌ Don't assume more recent source is "more correct"
- ❌ Don't assume academic source beats practitioner source
- ✅ Flag when data is from different time periods (EP1 vs EP2)
- ✅ Note when newer source provides new evidence (doesn't invalidate old)
- ✅ If empirically testable (e.g., "carry unwinds when rates rise"), find test data
- ✅ If untestable (philosophical), note both views as valid perspectives

---

## RULE M11: MISSING DATA DETECTION (What to Search For)

When you notice a multi-source scenario, search wiki for these SPECIFIC ANGLES:

### M11a: Standard Angles to Always Check

After adding a new source to existing node, automatically search for these patterns:

| Angle | Search Pattern | Why |
|---|---|---|
| **Temporal episodes** | `"[concept] 2003 OR 2008 OR 2020"` | Different time periods often have different mechanisms |
| **Geographic scope** | `"[concept] JPY OR EM OR EM carry"` | Mechanism may be prototype (JPY) vs general (all EM) |
| **Preconditions** | `"[concept] when OR if OR condition"` | Different sources often have different triggers |
| **Regime dependency** | `"[concept] volatile OR liquidity OR stress"` | High/low vol regimes often flip mechanism |
| **Theory vs practice** | `"[concept] should OR efficient OR persist"` | Distinguish what "should" happen vs what actually happens |
| **Granular mechanisms** | `"[concept] decompose OR component OR sub"` | High-level overview may need detail expansion |
| **Contradiction** | `"[concept] contradict OR conflict OR debate"` | Check if contradiction node already exists |
| **Boundary conditions** | `"[concept] when it fails OR breaks OR limits"` | Failure conditions often encode preconditions |
| **Historical evolution** | `"[concept] before 2010 OR 2015 OR evolved"` | Structure may have changed over decades |
| **Practitioner view** | `"[concept] trading OR market OR real world"` | Practitioners often catch gaps in theory |

### M11b: Automated Search Protocol

**When ingesting new source on existing concept:**
```
Step 1: Read new source completely
Step 2: Run these searches:
  a) python librarian.py search "[concept] 200X OR 201X OR 202X" --deep
  b) python librarian.py search "[concept] episode OR cycle OR phase" 
  c) python librarian.py search "[concept] when OR condition OR trigger"
  d) python librarian.py search "[concept] regime OR volatile OR stress"
  e) python librarian.py search "[concept] theory vs practice OR should persist"
Step 3: Review top-3 results for each search
Step 4: Classify results by angle (temporal, precondition, regime, etc.)
Step 5: Update node with expansion matching identified angles
```

**RULE M11-STRICT:**
- ✅ Always run 5 searches minimum when adding new source to existing node
- ✅ Document which angles you found (and which you didn't)
- ❌ Don't assume current node covers all angles
- ❌ Don't skip "Theory vs Practice" search even if seems obvious

---

## RULE M12: HOW TO ORGANIZE EXPANDED NODE (Hierarchy)

When a node grows to have multiple angles, use this hierarchy:

```markdown
# [[Concept_Name]]

## Thesis
[Single sentence capturing essence + multiplicity]

## 1. Core Logic (Always First)
[RAW-BOOK:Source1] High-level mechanism. ≤3 sentences.

## 2. Worked Example (Always Second)
[Multiple sub-examples if different time periods/geographies]

## 3. Expansions (Variable, add as needed)
  
  ### 3a. Temporal Evolution / Episodes
  [If concept changed over decades]
  
  ### 3b. Scope Generalization
  [If concept is prototype case of broader class]
  
  ### 3c. Precondition Mapping
  [If different sources identify different triggers]
  
  ### 3d. Regime Dependency
  [If mechanism outcome depends on market regime]
  
  ### 3e. Granular Mechanisms (Detail Expansion)
  [If concept decomposes into sub-mechanisms]
  
  ### 3f. Theory vs Practice
  [If theoretical prediction ≠ empirical reality]
  
  ### 3g. Angle Comparison
  [If multiple valid entry points to same mechanism]

## 4. Failure Conditions
[When does this concept break?]

## 5. Source Evolution Summary [LLM-S]
[Table showing evolution of understanding across sources]

## Related
[[Cross-references]]
```

**RULE M12-STRICT:**
- ✅ Always keep Core Logic + Worked Example as first two sections
- ✅ Add Expansions (3a-3g) only if evidence-based
- ✅ Create Source Evolution Summary table at end (when ≥3 sources)
- ❌ Don't create subsections without evidence (no "Potential Preconditions")
- ❌ Don't nest subsections >2 levels deep

---

## RULE M13: SOURCE EVOLUTION SUMMARY TABLE

When node has ≥3 sources covering same concept, create this table:

```markdown
## Source Evolution Summary

| Dimension | Book1 (2003) | Paper1 (2020) | Paper2 (2024) | Consensus |
|-----------|---|---|---|---|
| **Core mechanism** | Rate differential | Rate differential + basis | Rate + vol + FV correlation | Rate differential is primary |
| **Geographic scope** | JPY/USD only | JPY/USD + AUD/NZD | All EM pairs | Generalizable mechanism |
| **Duration viable** | 4 years | 9 years | 2-4 weeks (faster) | Regime-dependent |
| **Trigger unwinding** | Rates spike | Hedge costs rise | Vol spike + guidance change | Multi-trigger (regime-dependent) |
| **Precondition** | Rate stable | Rate stable + liquidity | CB committed to flat rates | Most critical: CB guidance |
| **Viability in high vol** | Not discussed | Breaks down | Becomes unprofitable | Regime-dependent |
| **Theory vs practice** | Theory (efficient markets) | Reality (persistent) | Reality (now ≥17 years) | Large theory-practice gap |
```

**RULE M13-STRICT:**
- ✅ Create 1 row per dimension (mechanism, scope, duration, etc.)
- ✅ Show evolution across sources chronologically
- ✅ Final column = consensus or "no consensus"
- ❌ Don't list every detail; list only main dimensions
- ❌ Don't create this table if <3 sources (premature)

---

## RULE M14: CONFIDENCE RECALCULATION (Multi-Source Dynamics)

When you add new source to existing concept, **recalculate confidence**.

**Old rule:** Confidence = source composition (1–5 scale).

**New rule:** When ≥2 sources agree on CORE mechanism but differ on DETAILS:
- ✓ Core mechanism confidence INCREASES (now multi-sourced)
- ✗ Detail-level claims keep original confidence until verified

### M14a: Example

**Node before M1-M13 expansion:**
```yaml
confidence: 4  # Single [RAW-BOOK]
source_refs:
  - file: "Book1_Ch8.md"
    page: 45
```

**Node after adding Paper1 + Paper2:**
```yaml
confidence: 5  # Three independent sources agree on core mechanism
source_refs:
  - file: "Book1_Ch8.md"
    page: 45
  - file: "Paper1_2020_Carry.md"
    page: 12
  - file: "Paper2_2024_Carry.md"
    page: 156
```

**But for specific detail claims:**
```markdown
[RAW-BOOK] Unwind trigger is rate spike. (confidence: 4)
[RAW-PAPER:Paper1] Unwind trigger is hedge cost. (confidence: 4)
[RAW-PAPER:Paper2] Unwind trigger is vol + guidance. (confidence: 4)

[LLM-S] Synthesis: all three triggers valid in different regimes. 
Consensus incomplete. (confidence: 3)
```

**RULE M14-STRICT:**
- ✅ Increase confidence when multiple independent sources confirm core mechanism
- ❌ Don't increase confidence if sources only agree on surface description
- ✅ Keep detail-claims at original confidence unless independent verification
- ✅ Distinguish "core mechanism confidence" from "detail-claim confidence"

---

## RULE M15: WHEN TO SPLIT A NODE (Don't Let Nodes Get Too Complex)

If multi-source expansion creates >2000 words or >10 subsections, **consider splitting**.

### M15a: Split Criteria

| Trigger | Action |
|---|---|
| Node >2000 words | Consider splitting |
| >8 subsections | Probably should split |
| >3 distinct angles (e.g., theory vs practice + temporal + regime) | Split |
| Core mechanism + detail decomposition both substantial | Split |
| Concept is BOTH mechanism AND domain-specific instance | Split |

### M15b: Split Pattern

**Before split:**
```
- Carry Trade Mechanics (core mechanism + JPY details + EM details + history)
```

**After split:**
```
- Carry Trade Mechanisms (core, theory vs practice, granular decomposition)
- Yen Carry Trade Episodes (JPY-specific, temporal, regime)
- Emerging Market Carry Trade Characteristics (scope, preconditions)
```

**RULE M15-STRICT:**
- ✅ Split when node has conflicting organizational logics (e.g., temporal + geographic)
- ✅ Keep core mechanism node as hub, reference from specialty nodes
- ❌ Don't split just because node is long; combine related angles
- ❌ Don't split until you have ≥3 independent sources

---

## QUICK REFERENCE: M-RULES DECISION TREE

```
New source on existing concept?

Same core mechanism?
  YES → Different ANGLE?
    YES → M3: Angle expansion (subsection)
    NO → Continue below
  
  Different SCOPE?
    YES → M4: Scope expansion (subsection)
    NO → Continue
  
  Different TIME PERIOD?
    YES → M5: Temporal expansion (episode subsection)
    NO → Continue
  
  Different PRECONDITIONS?
    YES → M6: Precondition map (table)
    NO → Continue
  
  Different REGIME VALIDITY?
    YES → M7: Regime dependency (subsection)
    NO → Continue
  
  Different DETAIL LEVEL?
    YES → M8: Granular decomposition (subsection)
    NO → Continue
  
  THEORY vs PRACTICE gap?
    YES → M9: Theory vs practice (subsection)
    NO → Continue
  
  Minor detail contradiction?
    YES → M10: Document both views (expanded text)
    NO → UPDATE source_refs only

DIFFERENT core mechanism?
  → M2: Evaluate as CONTRADICTION vs EXPANSION
  → If truly contradicts: Create contradiction node (M2)
  → If complements: Expand (M3-M9)
```

---

## ENFORCEMENT

When ingesting multi-source concept:

1. **Mandatory searches** (M11) — Run 5+ searches for different angles
2. **Classify difference** (M1) — Don't assume "same concept"
3. **Expand strategically** (M2-M9) — Add labeled subsections, don't replace
4. **Create source evolution table** (M13) — When ≥3 sources
5. **Recalculate confidence** (M14) — Increase when consensus on core
6. **Split if complex** (M15) — >2000 words or >8 subsections
7. **Log every expansion** — Update log.md with what angle added + source

---

## EXAMPLE: Yen Carry Trade Node After M-Rules

**Before:** Simple mechanism description (200 words, 1 source)

**After M-Rules applied:**
- Core Logic (M1-M2)
- Worked Examples with temporal episodes (M5)
- Scope expansion from JPY to all EM (M4)
- Precondition map: 3 different trigger sets (M6)
- Regime dependency: Low-vol vs High-vol outcomes (M7)
- Detail decomposition: 8 sub-mechanisms (M8)
- Theory vs Practice reconciliation (M9)
- Source evolution table with 4 sources (M13)

**Result:** ~1500 words, 9 subsections, confidence 5, multiple angles captured

**Without M-Rules:** Would have either (a) lost nuance by oversimplifying, or (b) created confusing sprawl by dumping all sources together.

**With M-Rules:** Clear structure, multiple valid angles preserved, no data loss.
