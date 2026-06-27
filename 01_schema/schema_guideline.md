# SCHEMA GUIDELINE v1.0 — Detailed Field-by-Field Tutorial
> Author: Claude | Date: 2026-05-02
> Supplement to `schema.md` v4.0. Use this when building or reviewing nodes.
> Covers: every node type with worked example, every citation pattern, all source_refs cases, multi-source rules, thesis writing guide, anti-patterns.

---

## HOW TO USE THIS DOCUMENT

`schema.md` is the **law** — immutable rules, taxonomy, field specs.
This document is the **tutorial** — walk-throughs, before/after fixes, decision trees.

Read order when creating a new node:
1. schema.md §1 → pick node type
2. This doc §A → full example for that type
3. schema.md §7–§9 → citation + thesis + source_refs rules
4. This doc §B–§D → edge cases and patterns
5. schema.md §10 → run audit checklist before saving

---

## §A. NODE TYPE EXAMPLES (Complete Worked Nodes)

Each example below shows: correct frontmatter + correct body structure + annotations explaining every choice.

---

### A1. `concept` — Primitive building block

**When to use:** The node names an object, category, or taxonomy unit. It does not explain HOW it works (that is `mechanism`) or WHAT the exact definition is (that is `definition`). A `concept` is the anchor — other nodes hang off it.

**Worked example:**

```markdown
---
title: "Duration Risk"
aliases:
  - Interest Rate Duration
  - Rate Sensitivity
type: concept
tags:
  - fixed-income
  - risk
  - duration
status: reviewed
confidence: 3
half_life_years: 10
school: ""
superseded_by: null
superseded_date: null
expert_lens: "Tuckman | Serrat"
provenance: "Tuckman_Serrat_Fixed_Income.md"
thesis: "Duration risk is the sensitivity of a bond's price to parallel shifts in
  the yield curve, where longer-duration instruments suffer larger capital losses
  per unit of rate rise, creating a fundamental trade-off between income and price stability."
source_refs:
  - file: "Tuckman_Serrat_Fixed_Income.md"
    page: 45
created: "2026-05-02"
updated: "2026-05-02"
---

# [[Duration_Risk]]

## Thesis
[RAW-BOOK:Tuckman_Serrat p.45] Duration risk is the sensitivity of a bond's price
to parallel shifts in the yield curve; longer-duration instruments suffer larger
capital losses per unit of rate rise, creating a fundamental trade-off between
yield income and price stability.

## Core Properties
[RAW-BOOK:Tuckman_Serrat p.46] Modified duration measures price sensitivity:
$$\Delta P / P \approx -D_{mod} \cdot \Delta y$$
where $D_{mod}$ = modified duration (years) and $\Delta y$ = yield change.

[LLM-S] Key properties:
- Duration increases with maturity (longer = more sensitive)
- Duration decreases with coupon rate (higher coupon = faster cash return)
- Duration decreases as yield rises (cash flows discounted more heavily)

## Related
- [[DV01]]
- [[Convexity]]
- [[Yield_Curve_Risk]]
- [[Asset_Liability_Management]]
```

**Annotations:**
- `aliases`: include common shorthand used in market conversation
- `expert_lens`: the author(s) whose framing defines this node's perspective — pipe-separated
- `confidence: 3` (WIKI) because the node exists but no RAW page is directly cited in body yet; if you add `[RAW-BOOK:Tuckman_Serrat p.45]` with specific quotes, upgrade to `4`
- `thesis`: concept thesis answers "X is [what] + [key property that distinguishes it]"
- Body H1 uses `[[Node_Stem]]` wikilink — always
- KaTeX for math — `$...$` inline, `$$...$$` block

---

### A2. `mechanism` — How something works

**When to use:** The node explains a transmission process — Input → Condition → Output with intermediate steps. The hallmark is a causal chain, not just a definition.

**Worked example (annotated inline):**

```markdown
---
title: "Interest Rate Transmission Channel"
aliases:
  - Monetary Policy Transmission
  - Rate Pass-Through
type: mechanism
tags:
  - monetary-policy
  - transmission
  - macro
status: verified
confidence: 4
half_life_years: 10
school: ""
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: "Perry_Central_Bank_Policy_P4.md"
thesis: "Central bank policy rate changes propagate to the real economy via five
  sequential channels — money market, bank lending, asset price, exchange rate, and
  expectations — each with distinct lag structures and regime-dependency conditions
  that determine which channel dominates."
source_refs:
  - file: "Perry_Central_Bank_Policy_P4.md"
    page: 112
created: "2026-05-02"
updated: "2026-05-02"
---

# [[Interest_Rate_Transmission_Channel]]

## Thesis
[RAW-BOOK:Perry_Central_Bank_Policy_P4 p.112] Central bank policy rate changes
propagate to the real economy via five sequential channels, each with distinct lag
structures and regime-dependency conditions.

## Transmission Chain
Policy Rate ↑ →[money market, immediate]→ Short-term rates ↑ →[bank repricing, 1–3m]→
  Lending rates ↑ →[credit conditions tight, 3–6m]→ Investment ↓ →[GDP lag 6–18m]→ Inflation ↓

## 1. Money Market Channel (Lag: immediate–1 week)
[RAW-BOOK:Perry p.112] Overnight rate directly sets the floor on interbank rates.
Transmission is near-perfect in systems with reserve corridor (floor/ceiling system).

**Failure condition:** When banks hoard reserves (2008–2009 style), excess reserves
decouple the policy rate from the effective overnight rate.

## 2. Bank Lending Channel (Lag: 1–3 months)
[RAW-BOOK:Perry p.115] Banks reprice loan books as deposit costs rise.
Pass-through is partial in concentrated banking systems where oligopoly pricing dampens competition.

**Condition for strong pass-through:** High interbank competition + low excess reserves.

## 3. Asset Price Channel (Lag: immediate for equities, 3–6m for real estate)
[LLM-S] Higher discount rates → lower present value of future cash flows → equity and
property prices fall → negative wealth effect → consumption declines.

## Worked Example: Fed Hike Cycle 2022–2023
[WEB-2023-08-01:federalreserve.gov] Fed raised 525bp in 16 months.
- Money market: EFFR tracked target within 5bp daily. ✓
- Bank lending: Prime rate followed within 30 days. ✓
- Asset prices: S&P500 fell ~20% in 2022 (partly rate, partly earnings revisions). ✓
- Exchange rate: USD appreciated ~15% on DXY in 2022. ✓

## Failure Conditions / Boundaries
- **Zero Lower Bound:** Policy rate near 0% → money market channel saturated
- **Fiscal Dominance:** Sovereign debt rollover risk forces CB to hold rates low → transmission inverted
- **Dollarized Economy:** Domestic rate changes irrelevant if credit is USD-denominated

## Related
- [[Fiscal_Dominance]]
- [[Zero_Lower_Bound]]
- [[Bank_Lending_Channel]]
- [[Asset_Price_Channel]]
```

**Annotations:**
- `Transmission Chain` section is mandatory for `mechanism` nodes (schema.md §3.2)
- Arrow notation: `X →[condition]→ Y` — always state the condition in brackets
- `Worked Example` section: must include quantified data when available
- `Failure Conditions` section: prevents overreach — states where the mechanism breaks

---

### A3. `definition` — Precise boundary-setting

**When to use:** The node answers "X là gì?" with expert-level precision — properties, boundary conditions, variants. Not a transmission chain; a careful enumeration of what X is and is NOT.

**Worked example:**

```markdown
---
title: "High Quality Liquid Assets"
aliases:
  - HQLA
  - Level 1 Assets
  - Level 2 Assets
type: definition
tags:
  - liquidity
  - regulatory
  - basel
  - lcr
status: verified
confidence: 4
half_life_years: 1
school: ""
superseded_by: null
superseded_date: null
expert_lens: "BIS Basel Committee"
provenance: "BIS_Basel3_LCR_2013.md"
thesis: "HQLA are assets that can be converted into cash quickly with minimal loss
  of value under stress; Basel III defines two tiers with strict eligibility criteria
  — Level 1 (0% haircut, unlimited) and Level 2 (15–50% haircut, capped at 40% of
  total HQLA stock) — where the tiering is designed to prevent regulatory arbitrage
  into illiquid instruments."
source_refs:
  - file: "BIS_Basel3_LCR_2013.md"
    page: 14
created: "2026-05-02"
updated: "2026-05-02"
---

# [[High_Quality_Liquid_Assets]]

## Thesis
[RAW-OFFICIAL:BIS_Basel3_LCR_2013 p.14] HQLA are assets that can be converted into
cash quickly with minimal loss of value under stress. Basel III creates a two-tier
structure with haircuts and caps to prevent regulatory arbitrage.

## 1. Level 1 HQLA (0% haircut, unlimited)
[RAW-OFFICIAL:BIS_Basel3 p.15]
- Central bank reserves (excess reserves eligible)
- Sovereign bonds (0% RWA under Basel II standardized)
- Central bank-issued securities
- IMF, BIS, ECB-issued claims

**What is NOT Level 1:** Corporate bonds regardless of rating, equity, most covered bonds.

## 2. Level 2 HQLA (haircut applies, cap at 40% total HQLA)

### Level 2A (15% haircut, cap at 40%)
[RAW-OFFICIAL:BIS_Basel3 p.16]
- Sovereign/PSE bonds (20% RWA under standardized)
- High-rated non-financial corporate bonds (AA– minimum)
- High-rated covered bonds (AA– minimum)

### Level 2B (25–50% haircut, cap at 15%)
[RAW-OFFICIAL:BIS_Basel3 p.17]
- RMBS (25% haircut, subject to national discretion)
- Lower-rated corporate bonds (A+ to BBB–)
- Exchange-traded equities in main indices (50% haircut)

## Boundaries — What disqualifies an asset
[RAW-OFFICIAL:BIS_Basel3 p.14]
- **Issued by a financial institution** → excluded (wrong-way risk)
- **Has encumbrance** → pledged collateral is not free liquid
- **Not tradeable** → must be tradeable on a recognised exchange or OTC market

## Related
- [[Liquidity_Coverage_Ratio]]
- [[Net_Stable_Funding_Ratio]]
- [[Asset_Encumbrance_Problem]]
```

**Annotations:**
- `definition` thesis answers "X is [precise boundary] where [key distinguishing property holds]"
- Use `## Boundaries — What X is NOT` subsection — critical for definitions
- `half_life_years: 1` because regulatory rules change; HQLA eligibility lists get updated
- `status: verified` because RAW-OFFICIAL source exists

---

### A4. `relationship` — Interaction between nodes

**When to use:** The node describes how two or more concepts interact — hierarchy, trade-off, amplification, or dependency. It is NOT a mechanism (no transmission chain) and not a definition (no boundary-setting for one concept).

**Worked example:**

```markdown
---
title: "Duration-Convexity Trade-off"
aliases:
  - Convexity vs Duration
  - Curvature Risk vs Sensitivity
type: relationship
tags:
  - fixed-income
  - duration
  - convexity
  - risk-management
status: reviewed
confidence: 3
half_life_years: 10
school: ""
superseded_by: null
superseded_date: null
expert_lens: "Tuckman | Serrat"
provenance: "Tuckman_Serrat_Fixed_Income.md"
thesis: "Duration and convexity describe the first and second derivatives of price
  with respect to yield; convexity creates an asymmetric payoff (gains > losses for
  equal yield moves) whose benefit is offset by the premium investors pay via lower
  yield, creating a fundamental tension in portfolio construction between earning
  carry and owning optionality."
source_refs:
  - file: "Tuckman_Serrat_Fixed_Income.md"
    page: 78
created: "2026-05-02"
updated: "2026-05-02"
---

# [[Duration-Convexity_Trade-off]]

## Thesis
[RAW-BOOK:Tuckman_Serrat p.78] Duration measures linear price sensitivity; convexity
captures the curvature. Positive convexity creates asymmetric payoff (bigger gains
than losses for equal yield moves) but investors pay for it via reduced carry.

## The Core Tension
| Property | Duration | Convexity |
|---|---|---|
| Measures | First derivative (slope) | Second derivative (curvature) |
| Effect | Linear price change | Asymmetric payoff |
| Cost | N/A (intrinsic) | Paid via yield give-up |
| Benefit | Yield income | Downside protection |

[LLM-S] Portfolio managers who "buy convexity" (long options, callable bonds with
high convexity) accept lower running yield in exchange for asymmetric return profile.
This is a regime-conditional trade: in low-vol regimes, convexity premium is wasted;
in high-vol regimes, convexity earns back its cost.

## Interaction Mechanics
[RAW-BOOK:Tuckman_Serrat p.79]
Price approximation to second order:
$$\Delta P / P \approx -D_{mod} \cdot \Delta y + \frac{1}{2} C \cdot (\Delta y)^2$$
Where $C$ is convexity (always positive for non-callable bonds).

**Key interaction:** For large yield moves, convexity term dominates the duration
term — a 300bp move in rates makes convexity more important than duration in PnL attribution.

## Related
- [[Duration_Risk]]
- [[Convexity]]
- [[Mortgage_Backed_Securities]] (negative convexity example)
- [[Interest_Rate_Options]]
```

**Annotations:**
- `relationship` thesis answers "[A] and [B] interact via [mechanism] creating [tension/amplification]"
- Tables work well for side-by-side comparisons
- State the regime condition: when does each side dominate?

---

### A5. `perspective` — Author/institution's specific view

**When to use:** The node captures a SPECIFIC VIEW held by a named author, school, or institution. It is NOT a neutral definition. It should state the claim, who holds it, and what the alternative is.

**Worked example:**

```markdown
---
title: "Warjiyo on Integrated Policy Framework"
aliases:
  - IPF Thesis
  - 4-Tool Policy Framework
type: perspective
tags:
  - monetary-policy
  - macro-prudential
  - central-banking
status: verified
confidence: 4
half_life_years: 1
school: "Institutional"
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: "Perry_Central_Bank_Policy_P1.md"
thesis: "Perry Warjiyo argues that post-GFC central banks must deploy four coordinated
  tools — interest rate, exchange rate intervention, macro-prudential policy, and
  capital flow management — as a unified framework, rejecting the pre-GFC doctrine
  that price stability alone suffices for financial stability."
source_refs:
  - file: "Perry_Central_Bank_Policy_P1.md"
    page: 5
created: "2026-05-02"
updated: "2026-05-02"
---

# [[Warjiyo_on_Integrated_Policy_Framework]]

## Author / Source
[RAW-BOOK:Perry_Central_Bank_Policy_P1 p.5] Perry Warjiyo — Governor, Bank Indonesia;
Co-author with Solikin M. Juhro. "Central Bank Policy: Theory and Practice" (2019).
Institutional school — draws on EM central bank experience.

## Claim
[RAW-BOOK:Perry p.5] The four-tool Integrated Policy Framework (IPF) asserts:
1. **Interest rate** → price stability, demand management
2. **Exchange rate intervention** → external stability, imported inflation control
3. **Macro-prudential policy** → systemic risk, credit cycle management
4. **Capital flow management** → buffer against sudden stops and hot money

[RAW-BOOK:Perry p.6] "No single tool can achieve both price and financial stability
simultaneously — the Tinbergen Principle requires one instrument per target."

## Counter-argument
[WIKI] The pre-GFC Jackson Hole Consensus (Greenspan/Bernanke) held that interest
rates alone suffice: macro-prudential tools distort capital allocation and create
regulatory arbitrage. See [[Lean_Vs_Clean_Monetary_Debate]].

[LLM-S] IMF (2012 "Rethinking Macroeconomic Policy") partially endorsed IPF for
EMs but maintained that AEs with deep capital markets should rely primarily on
conventional monetary policy.

## Regime conditions for IPF validity
[LLM-S] Warjiyo's framework is most defensible when:
- Domestic banking sector dominates credit creation (shallow capital markets)
- Exchange rate pass-through to CPI is high (>0.3 coefficient)
- Capital flows are volatile relative to domestic asset markets

## Related
- [[Lean_Vs_Clean_Monetary_Debate]]
- [[Macro_Prudential_Policy]]
- [[Tinbergen_Principle]]
- [[Capital_Flow_Management]]
```

**Annotations:**
- `school` field is mandatory for perspective nodes — see schema.md §6 for valid values
- `## Author / Source` section must appear first — who holds this view and where stated
- `## Counter-argument` is mandatory — no perspective without its opposition
- `thesis` must identify author explicitly: "[Author] argues that..."

---

### A6. `evidence` — Quantified case study

**When to use:** The node presents empirical data, a historical case, or a quantified observation. Minimal theory — maximum specificity. Numbers, dates, outcomes.

**Key rule:** Evidence nodes exist to back mechanisms and relationships. Link back to the mechanism the evidence supports.

**Worked example:**

```markdown
---
title: "LCR Procyclicality Crisis 2020"
aliases:
  - LCR Buffer Drawdown March 2020
  - Covid LCR Stress
type: evidence
tags:
  - lcr
  - liquidity
  - regulatory
  - covid
  - procyclicality
status: verified
confidence: 4
half_life_years: 1
school: ""
superseded_by: null
superseded_date: null
expert_lens: "BIS"
provenance: "BIS_Working_Paper_2020.md"
thesis: "During the March 2020 Covid shock, global bank LCR ratios fell sharply as
  off-balance-sheet credit facilities were drawn, confirming the procyclicality
  hypothesis: LCR creates a cliff-effect incentive where banks resist ratio drawdown,
  causing them to hoard liquidity rather than extend credit precisely when most needed."
source_refs:
  - file: "BIS_Working_Paper_2020.md"
    page: 8
created: "2026-05-02"
updated: "2026-05-02"
---

# [[LCR_Procyclicality_Crisis_2020]]

## Evidence Overview
[RAW-OFFICIAL:BIS_Working_Paper_2020 p.8] March 2020: Global banks drew down
undrawn revolving credit facilities at unprecedented speed as corporates sought
liquidity buffers. Aggregate HQLA consumption exceeded Basel's 30-day stress scenario
parameters in several jurisdictions within 2 weeks.

## Quantified Findings
[RAW-OFFICIAL:BIS_WP_2020 p.9]
- European large banks: average LCR fell from 145% (Feb 2020) to 128% (Mar 2020) — 17pp in 30 days
- US G-SIBs: LCR stable (excess buffer) but credit line drawdowns peaked at 3× historical monthly average
- BIS estimate: $140bn in undrawn revolving facilities drawn in March 2020 alone

## The Cliff-Effect Observation
[RAW-OFFICIAL:BIS_WP_2020 p.11] Banks with LCR near 105% (just above the 100% minimum)
showed statistically significant reduction in new loan origination during the stress
period, while banks with LCR >130% continued lending normally.

**Mechanism confirmed:** [[LCR_Procyclicality_Mechanism]] — banks near LCR floor hoard
liquidity rather than lending, amplifying credit contraction in stress.

## Policy Response
[WEB-2020-03-20:bankofengland.co.uk] BoE, ECB, FRB all issued guidance permitting
banks to operate below LCR minimum "temporarily" to encourage continued lending.
Effective: banks used buffer once regulators communicated tolerance.

## Related
- [[Liquidity_Coverage_Ratio]]
- [[LCR_Procyclicality_Mechanism]]
- [[Asset_Fire_Sales_Mechanism]]
- [[HQLA_Market_Impact]]
```

**Annotations:**
- `evidence` thesis answers "[Quantified claim] observed [where/when], consistent with [mechanism]"
- Always link to the mechanism the evidence supports/contradicts
- Date specificity is critical — `March 2020`, not just `2020`
- `half_life_years: 1` for market data / case studies that may be superseded by newer evidence

---

### A7. `contradiction` — Unresolved conflict between sources

**When to use:** Two or more authoritative sources make incompatible claims about the same phenomenon, AND the conflict cannot be resolved by "different conditions/regimes" without additional analysis. A contradiction node holds the tension explicitly rather than forcing a false resolution.

**Worked example:**

```markdown
---
title: "QE Effectiveness Debate"
aliases:
  - Does QE Work
  - Portfolio Rebalancing vs Signalling QE
type: contradiction
tags:
  - qe
  - monetary-policy
  - central-banking
  - effectiveness
status: verified
confidence: 5
half_life_years: 1
school: ""
superseded_by: null
superseded_date: null
expert_lens: "Bernanke | Borio"
provenance: "Perry_Central_Bank_Policy_P4.md"
thesis: "The effectiveness of QE is actively contested: portfolio rebalancing theory
  (Bernanke/Fed) claims QE lowers long yields via scarcity and wealth effects, while
  the BIS/Borio view argues QE primarily works through signalling and forward guidance,
  with the asset purchase mechanism being secondary and potentially distortionary."
source_refs:
  - file: "Perry_Central_Bank_Policy_P4.md"
    page: 167
  - file: "BIS_Annual_Report_2019.md"
    page: 45
created: "2026-05-02"
updated: "2026-05-02"
---

# [[QE_Effectiveness_Debate]]

## Claim A — Portfolio Rebalancing (Bernanke / Fed view)
[RAW-OFFICIAL:FederalReserve_Bernanke2010] QE works via portfolio rebalancing:
1. Fed purchases long-term Treasuries/MBS → scarcity effect pushes investors into riskier assets
2. Lower risk-free rates → compressed risk premia across asset classes
3. Wealth effect from higher asset prices → consumption stimulus
4. Exchange rate depreciation → export boost

**Empirical support cited:** 10Y UST fell ~100bp during QE1 announcement window.

## Claim B — Signalling Dominance (BIS / Borio view)
[RAW-OFFICIAL:BIS_Annual_Report_2019 p.45] QE primarily works through forward
guidance and commitment to low rates, NOT the asset purchase volume:
1. The "portfolio rebalancing" channel is weak because investors simply reinvest
   at similar risk levels (duration for duration)
2. The empirical yield compression observed in QE is attributable to the accompanying
   forward guidance ("rates low until unemployment falls")
3. Asset purchases may cause financial stability risks (search for yield, zombie firms)
   that offset the demand stimulus

**Empirical challenge:** BoJ QE 2013 — yields rose despite massive purchases
(see [[BoJ_QE_2013_Case_Study]]). ECB PSPP: transmission was heterogeneous across EZ members.

## Resolution Status
REGIME-DEPENDENT:
- In a credibly independent central bank with high financial market depth → portfolio
  rebalancing may be non-trivial but signalling dominates (event study evidence)
- In a context of policy rate at ZLB + high fiscal dominance risk → signalling
  channel becomes unstable as credibility is questioned
- In shallow/illiquid bond markets → pure scarcity mechanism may dominate

**Not RESOLVED** — the relative contribution remains empirically contested as of 2024.

## Related
- [[Quantitative_Easing]]
- [[Portfolio_Rebalancing_Channel]]
- [[Forward_Guidance]]
- [[BoJ_QE_2013_Case_Study]]
- [[Fiscal_Dominance]]
```

**Annotations:**
- `contradiction` MUST have both claims labeled with their sources
- `## Resolution Status` is mandatory — must state: UNRESOLVED / RESOLVED / REGIME-DEPENDENT
- Both sources should appear in `source_refs`
- `confidence: 5` is appropriate when both claims are well-sourced — the contradiction itself is well-documented
- Do NOT collapse the contradiction into a "synthesis" — that would be premature

---

### A8. `synthesis` — Wisdom run output

**When to use:** Output from `python librarian.py wisdom <tag>`. Do NOT write synthesis nodes manually.

If you must create one manually (e.g., a research session produced a new cross-tag insight):

```markdown
---
title: "Liquidity-Solvency Confusion Synthesis"
aliases:
  - Misdiagnosis of Solvency as Liquidity
type: synthesis
tags:
  - liquidity
  - solvency
  - central-banking
  - synthesis
status: reviewed
confidence: 2
half_life_years: 0.5
school: ""
superseded_by: null
superseded_date: null
expert_lens: ""
provenance: "wisdom-run-2026-05-02"
thesis: "Canonical synthesis: across fixed-income, monetary policy, and crisis management
  literature, the persistent tension between liquidity and solvency frameworks — where
  LOLR intervention requires solvency judgment — is the central unresolved problem
  of modern financial stability architecture."
source_refs: []
created: "2026-05-02"
updated: "2026-05-02"
---
```

**Annotations:**
- `confidence: 2` maximum for manual synthesis (no direct RAW backing)
- `half_life_years: 0.5` — synthesis is derived, stales as inputs evolve
- `source_refs: []` is acceptable — this is a cross-node insight, not a citation
- Add `provenance: "wisdom-run-YYYY-MM-DD"` to track origin

---

### A9. `domain` — Geographic or market context

**When to use:** Country-level, market-level, or regulatory-regime-level context. Defines the operating environment that conditions how mechanisms behave in that context.

```markdown
---
title: "Vietnam Bond Market"
aliases:
  - VN Bond Market
  - SBV Monetary System
type: domain
tags:
  - vietnam
  - emerging-market
  - bond-market
  - sbv
status: reviewed
confidence: 3
half_life_years: 3
school: ""
superseded_by: null
superseded_date: null
expert_lens: "SBV | IMF"
provenance: "IMF_Vietnam_2023.md"
thesis: "Vietnam's domestic bond market is bank-dominated and shallow by regional
  standards, with VGBs concentrated in commercial bank holdings (>75%), creating
  structural rollover dependency on banking system liquidity that amplifies the
  transmission of SBV reserve requirement and open market operations to sovereign
  funding costs."
source_refs:
  - file: "IMF_Vietnam_2023.md"
    page: 22
created: "2026-05-02"
updated: "2026-05-02"
---
```

**Annotations:**
- `half_life_years: 3` — domain conditions change (regulations, market development) but not as fast as market data
- Thesis should identify the STRUCTURAL FEATURE that makes this domain distinct from the generic mechanism

---

### A10. `glossary` — Quick reference / terminology aggregation

**When to use:** The node aggregates multiple related terms that do NOT each warrant their own node. A glossary node should NOT be the primary location for any major concept — it is a reference shortcut.

```markdown
---
title: "Fixed Income Daycount Glossary"
aliases:
  - Daycount Conventions Reference
  - ACT/360 ACT/365
type: glossary
tags:
  - fixed-income
  - convention
  - daycount
status: verified
confidence: 4
half_life_years: 10
school: ""
superseded_by: null
superseded_date: null
expert_lens: "ISDA"
provenance: "ISDA_2006_Definitions.md"
thesis: "Daycount conventions determine how interest accrues between payment dates;
  the choice of convention affects the bond's carry calculation and is regime-specific
  — money markets use ACT/360, government bonds use ACT/ACT or 30/360,
  with the difference creating basis risk in cross-market hedges."
source_refs:
  - file: "ISDA_2006_Definitions.md"
    page: 4
created: "2026-05-02"
updated: "2026-05-02"
---

# [[Fixed_Income_Daycount_Glossary]]

## Quick Reference Table
| Convention | Used In | Formula |
|---|---|---|
| ACT/ACT | Govt bonds (US, EUR) | Actual days / actual days in coupon period |
| ACT/360 | Money market (LIBOR, EURIBOR) | Actual days / 360 |
| ACT/365 (Fixed) | GBP bonds, some EM | Actual days / 365 |
| 30/360 | USD corporate bonds | Assumes 30-day months / 360 |
| 30E/360 | EUR covered bonds | European variant of 30/360 |

[RAW-OFFICIAL:ISDA_2006 p.4] ISDA definitions govern all OTC derivative daycount.
Mismatch between bond (ACT/ACT) and hedge (ACT/360) creates daycount basis.
```

---

### A11. `convention` — Market operational standard

**When to use:** A rule, standard, or operational norm that governs market practice — settlement rules, ISDA standards, CCP margin rules. Different from `definition` (which explains a concept) or `mechanism` (which explains a process).

```markdown
---
title: "T+2 Bond Settlement Convention"
aliases:
  - Standard Settlement Period
  - Securities Settlement Cycle
type: convention
tags:
  - fixed-income
  - settlement
  - operations
  - convention
status: verified
confidence: 5
half_life_years: 1
school: ""
superseded_by: null
superseded_date: null
expert_lens: "ICMA | ISDA"
provenance: "ICMA_Settlement_Rules.md"
thesis: "The T+2 settlement convention creates a 2-business-day gap between trade
  execution and cash/securities exchange, generating counterparty credit exposure
  during the settlement window and creating replacement risk that CCP clearing partially
  mitigates but does not eliminate for bilateral trades."
source_refs:
  - file: "ICMA_Settlement_Rules.md"
    page: 1
created: "2026-05-02"
updated: "2026-05-02"
---
```

---

## §B. CITATION PATTERNS — All Cases

### B1. Single clean RAW source
```markdown
[RAW-BOOK:Tuckman_Serrat p.45] The DV01 of a bond equals...
```

### B2. Single official source
```markdown
[RAW-OFFICIAL:BIS_Basel3_2017 §31] The LCR minimum is 100% from January 2019.
```

### B3. Single web source (ephemeral)
```markdown
[WEB-2026-04-30:bloomberg.com] The Fed held rates at 4.25–4.50% at the May 2026 meeting.
```

### B4. Two sources agree on the same claim — CORROBORATION
**Format:** `[SRC1 | SRC2]` inline, or two separate citations in adjacent sentences.

```markdown
# Option A — stacked inline (preferred for direct agreement)
[RAW-BOOK:Perry p.115 | RAW-BOOK:Bindseil p.43] The bank lending channel operates
with a 1–3 month lag in transmission from policy rate to retail loan rates.

# Option B — sequential (preferred when each adds a nuance)
[RAW-BOOK:Perry p.115] Bank lending rate transmission has 1–3 month lag.
[RAW-BOOK:Bindseil p.43] Confirms lag structure; adds that concentration
in the banking system reduces pass-through to 60% of the policy rate move.
```

**Confidence implication:** Two independent RAW sources agreeing → confidence = 5.

### B5. Two sources agree on mechanism, disagree on magnitude — PARTIAL CONFLICT
```markdown
[RAW-BOOK:Perry p.115] Bank lending channel lag: 1–3 months in EM context.
[RAW-ACADEMIC:Mishkin2007 p.22] Lag estimated at 3–6 months for US banking system.

[LLM-S] The disagreement likely reflects structural differences: EM banks reprice
faster (shorter fixed-rate loan terms) vs US banks with longer-duration loan books.
```

**Confidence implication:** Keep confidence at 4 (single clean backing per claim); add a `contradiction` node if the magnitude difference is material.

### B6. LLM synthesis from cited sources
```markdown
[RAW-BOOK:Perry p.112] Policy rate → money market rate.
[RAW-BOOK:Bindseil p.43] Money market rate → interbank rate.
[LLM-S] Therefore, a 25bp hike transmits to LIBOR panel rates within 1–2 days,
  with the overnight rate as the instantaneous anchor.
```

**Rule:** `[LLM-S]` is ONLY valid when the preceding sentences contain RAW citations whose logic supports the synthesis. Do not use `[LLM-S]` as a standalone claim.

### B7. Placeholder — not yet sourced
```markdown
[LLM] The duration of the transmission lag depends on the degree of banking system
  concentration. Confidence: 1. Source needed: BIS or CB research paper.
```

**Rule:** Every `[LLM]` placeholder MUST include an explicit note that it is unsourced. This triggers `deepdive_search` to flag the node as `thin`.

### B8. Web source flagged for ingest
```markdown
[WEB-2026-04-15:imf.org] Vietnam's current account surplus narrowed to 2.1% of GDP
  in Q1 2026 per IMF Article IV consultation.  [INGEST CANDIDATE]
```

**Rule:** Add `[INGEST CANDIDATE]` to any WEB source with durable analytical value.

### B9. Multi-source citation with conflict — CREATE CONTRADICTION NODE
```markdown
[RAW-BOOK:SourceA p.22] X causes Y.
[RAW-BOOK:SourceB p.45] X does NOT cause Y; observed correlation is spurious.

→ See [[SourceA_SourceB_Contradiction]] for resolution analysis.
```

**Rule:** When two RAW sources directly contradict on a factual claim (not regime-dependent), do NOT embed the resolution in the node. Spawn a `contradiction` node and link.

---

## §C. MULTI-SOURCE CITATION — 9 CASES DECISION TREE

When you have two sources about the same claim, determine which case applies:

```
Q1: Do both sources address the SAME specific claim?
  → NO → Cite separately, no stacking. They are about different things.
  → YES → proceed to Q2

Q2: Do they agree on the claim?
  → YES → [SRC1 | SRC2] stacked. Confidence = 5 if both RAW.
  → NO → proceed to Q3

Q3: Do they disagree on mechanism or on magnitude/degree?
  → MAGNITUDE → cite both, add [LLM-S] reconciliation note. Confidence = 4.
  → MECHANISM → spawn CONTRADICTION node. Link with "→ See [[Node]]". Confidence = 3.

Q4 (for disagreement cases): Is the disagreement regime-dependent?
  → YES → Add "Condition: [X holds when ...]" resolution. Status = REGIME-DEPENDENT.
  → NO → Status = UNRESOLVED. Do not force a resolution.
```

Full 9-case matrix:

| Case | Description | Citation format | Confidence |
|---|---|---|---|
| 1 | Both RAW, agree exactly | `[SRC1 \| SRC2]` | 5 |
| 2 | RAW + WIKI, agree | `[RAW-X \| WIKI]` | 4 |
| 3 | RAW + WEB, agree | `[RAW-X \| WEB-date]` | 4 |
| 4 | Both RAW, agree on mechanism, differ on magnitude | Two sequential citations + [LLM-S] reconciliation | 4 |
| 5 | Both RAW, contradict on mechanism | Spawn CONTRADICTION node | 3 |
| 6 | RAW contradicts WIKI (internal) | Note conflict, flag WIKI node for update | 3 |
| 7 | RAW contradicts WEB | Trust RAW; flag WEB as `[INGEST CANDIDATE]` if WEB is more recent | 4 |
| 8 | LLM-S synthesises multiple RAW | `[LLM-S]` only after preceding RAW citations | 2–3 |
| 9 | Same source, different pages, different claims | Two separate citations; NOT stacked | (depends) |

**Confidence is always the WEAKEST LINK:** `[RAW \| LLM]` → confidence 1, not 4.

---

## §D. THESIS WRITING GUIDE

### D1. The thesis field does THREE jobs
1. **Search anchor** — wikisearch.py weights thesis ×4 in BM25. Bad thesis = bad findability.
2. **Graphify label** — graph.json uses thesis for node description in graph visualization.
3. **Quality gate** — claim_auditor.py checks that thesis contains ≥1 condition and mechanism marker.

### D2. The formula
```
thesis = [under CONDITION] + [ACTOR] + [operates via MECHANISM] + [producing OUTCOME]
```

Not all four are required, but mechanism is always required. Condition should be present whenever the claim is not universally true.

### D3. Anti-patterns with fixes

**Anti-pattern 1: Restating the title**
```yaml
# title: "Yield Curve Inversion"
# BAD
thesis: "Yield curve inversion occurs when short-term yields exceed long-term yields."
# GOOD
thesis: "Yield curve inversion occurs when central bank tightening raises short-term
  rates above long-term expectations; historically precedes recessions by 12–18 months
  in the US because it signals market expectation of future rate cuts to address
  growth weakness."
```

**Anti-pattern 2: Too abstract**
```yaml
# BAD
thesis: "Monetary policy affects the economy through various transmission channels."
# GOOD
thesis: "Central bank policy rate changes transmit to real activity via five channels
  — money market, bank lending, asset price, exchange rate, expectations — with
  lags ranging from immediate (money market) to 12–18 months (GDP impact)."
```

**Anti-pattern 3: Too long / multiple claims**
```yaml
# BAD (87 words, two independent claims)
thesis: "The LCR forces banks to hold 100% liquid assets. At the same time, banks
  try to minimize the amount of HQLA they hold because HQLA earns lower returns.
  This creates a conflict between regulatory requirements and profit maximization.
  During crises, banks near the LCR floor reduce lending to preserve their buffer,
  which amplifies credit contraction and creates systemic risk."
# GOOD (split into thesis + mechanism body)
thesis: "The LCR minimum creates a cliff-effect incentive where banks near the 100%
  floor hoard liquidity rather than lend, amplifying credit contraction during stress
  because buffer drawdown signals weakness to counterparties and regulators."
```

**Anti-pattern 4: Missing the condition (always-true claims)**
```yaml
# BAD
thesis: "When the central bank raises rates, borrowing costs increase."
# GOOD
thesis: "Central bank rate hikes increase borrowing costs only when the bank lending
  channel is intact — i.e., banks are not capital-constrained and deposit competition
  is sufficient to pass through policy rate moves to lending rates."
```

### D4. Language rule
- **English preferred** for thesis field — ensures graphify node labels are readable cross-context
- **Bilingual OK** for perspective nodes only: `"EN / VI"` format
- **Vietnamese only** for evidence nodes from Vietnamese sources (SBV, VCBS, SSI reports) where the original language adds precision

---

## §E. SOURCE_REFS GUIDE — Every Case

### E1. Book source (paginated)
```yaml
source_refs:
  - file: "Tuckman_Serrat_Fixed_Income.md"
    page: 45
```
- `file` = the `.md` file in `02_sources/books/` (basename, not full path)
- `page` = integer (the original book page, not the .md line number)

### E2. Book source with section reference
```yaml
source_refs:
  - file: "Perry_Central_Bank_Policy_P4.md"
    page: "§4.3"
```
- When page number is unclear but section is known, use section string

### E3. Multi-chapter source (same book, multiple chapters ingested as separate files)
```yaml
source_refs:
  - file: "Perry_Central_Bank_Policy_P1.md"
    page: 5
  - file: "Perry_Central_Bank_Policy_P4.md"
    page: 112
```
- Two entries for two different chapters/files — do NOT merge into one

### E4. Clipping or article (no page)
```yaml
source_refs:
  - file: "Are_high_UK_yields_good_or_bad.md"
```
- Omit `page` entirely — do NOT write `page: null` or `page: 0`

### E5. Web source (not in 02_sources — ephemeral)
```yaml
# WEB sources do NOT go in source_refs
# They are cited inline only: [WEB-2026-04-30:ft.com]
# source_refs is for files in 02_sources/ only
source_refs: []
```

### E6. Draft node — no source yet
```yaml
source_refs: []
# confidence must be ≤2
# status: draft
```

### E7. Multiple books corroborating (confidence 5)
```yaml
source_refs:
  - file: "Bindseil_LOLR.md"
    page: 167
  - file: "Perry_Central_Bank_Policy_P4.md"
    page: 142
# confidence: 5 — two independent RAW sources
```

### Common errors checklist
```yaml
# ERROR 1: null instead of []
source_refs: null           ← FAIL — use []

# ERROR 2: bare string
source_refs:
  - "Perry_Central_Bank.md" ← FAIL — must be dict with 'file' key

# ERROR 3: full path instead of basename
source_refs:
  - file: "02_sources/books/Perry_Central_Bank.md"  ← FAIL — basename only

# ERROR 4: page: null when page is unknown
source_refs:
  - file: "Perry.md"
    page: null              ← FAIL — omit page key entirely

# ERROR 5: wrong file (file not in 02_sources/)
source_refs:
  - file: "03_wiki/mechanisms/Some_Node.md"  ← FAIL — must be in 02_sources/
```

---

## §F. FULL PRE-PUBLISH CHECKLIST (Annotated)

```
[ ] 1. title matches filename stem
        "Duration Risk" → Duration_Risk.md  ✓
        "Duration Risk" → duration-risk.md  ✗ (wrong case convention)

[ ] 2. All mandatory frontmatter fields present and non-null
        Every field in schema.md §2 must exist. Missing = FAIL.
        Fields that accept null: superseded_by, superseded_date only.

[ ] 3. type is in valid taxonomy list
        One of: concept / definition / mechanism / relationship / convention /
        perspective / evidence / domain / glossary / contradiction / synthesis

[ ] 4. confidence integer 1–5
        Not float, not "high", not null. Integer only.

[ ] 5. status is a valid value
        draft / reviewed / verified / stale / archived / conflict

[ ] 6. half_life_years matches content type
        10 = mechanism/theory, 1 = regulatory, 0.1 = market data,
        0.5 = synthesis, 3 = domain. Don't default to 10 for everything.

[ ] 7. thesis: ≥20 words, ≤60 words, contains condition + mechanism
        Fail patterns: "X is when Y" (no mechanism), "X affects Y" (no condition)

[ ] 8. source_refs: list (not null), each item has 'file' key
        [] is valid for drafts. null is never valid.

[ ] 9. If confidence ≥ 4: source_refs has ≥1 entry
        confidence:4 + source_refs:[] = CONTRADICTION → fix one or the other

[ ] 10. All body claims have [...] citation label
         Scan body for sentences without [RAW/WIKI/WEB/LLM] prefix.
         Exception: section headers and Related wikilinks.

[ ] 11. No forbidden vague patterns
         Search body for: "nhiều yếu tố", "phụ thuộc vào", "thường hoạt động",
         "ảnh hưởng nhiều", "qua nhiều kênh" — each must be replaced with
         specific conditions and mechanisms.

[ ] 12. H1 heading = # [[Node_Stem]]
         [[Node_Stem]] = filename without .md, underscores preserved

[ ] 13. Related section has ≥1 wikilink
         Exception: truly isolated new concept (rare). Add related nodes as
         graph fills in, but flag with [[?]] if unknown.

[ ] 14. updated field = today's date
         Always update this on every write — even minor edits.

[ ] 15. log.md entry added
         One line per change: "YYYY-MM-DD | NodeName | writeback-type | reason"
         Writeback types: UPDATE / REPLACE / BRIDGE / CONTRADICTION /
         SPAWN / SYNTHESIS / PERSPECTIVE
```

---

## §G. QUICK REFERENCE — Type → Thesis template

| Type | Thesis template |
|---|---|
| `concept` | "[X] is [definition] + [key distinguishing property]" |
| `mechanism` | "Under [condition], [actor] operates via [transmission] → [outcome]" |
| `definition` | "[X] is precisely [boundary] where [distinguishing property holds]; [common confusion] does NOT qualify" |
| `relationship` | "[A] and [B] interact via [mechanism]; [regime condition] determines which dominates" |
| `perspective` | "[Author] argues [X] because [reasoning], contrasting with [mainstream/alternative view]" |
| `evidence` | "[Quantified claim] observed [where + when], [consistent with / challenging] [[Mechanism_Node]]" |
| `contradiction` | "The [X] debate pits [Claim A] against [Claim B]; [UNRESOLVED / REGIME-DEPENDENT: condition]" |
| `synthesis` | "Canonical synthesis of [domain]: key tension [X vs Y]; implication for [practice/theory]" |
| `domain` | "[Country/market] exhibits [structural feature] that [conditions how mechanisms behave differently vs baseline]" |
| `glossary` | "[Terms] are related conventions governing [domain]; choice affects [calculation/instrument/risk]" |
| `convention` | "The [convention] creates [operational constraint] that generates [risk/basis/exposure] in [context]" |
