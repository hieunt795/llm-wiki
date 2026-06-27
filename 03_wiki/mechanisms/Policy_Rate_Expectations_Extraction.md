---
title: Policy Rate Expectations Extraction
aliases:
- Policy Path Modeling
- Fitting Policy Expectations
- Implied Policy Probabilities
- Central Bank Action Forecasting
type: mechanism
tags:
- central-banking
- monetary-policy
- valuation
- quantitative-finance
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch16.md
thesis: The extraction of policy rate expectations involves backward-engineering the
  market's yield curve into a projected sequence of overnight rates that align with
  a central bank's specific meeting calendar and historical operational framework.
source_refs:
- file: During_Fixed_Income_Ch16.md
  page: 134
- file: During_Fixed_Income_Ch16.md
  page: 135
- file: During_Fixed_Income_Ch16.md
  page: 136
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Market attention is focused on **Official Rates** (policy rates) because they are the primary tool for influencing money creation. However, market interest rates (like Euribor or 3M Treasuries) do not perfectly mirror policy rates due to credit spreads, turn effects, and risk premia. Alexander Düring explains that to see "through" the market noise, analysts must construct a hypothetical **Overnight Account** that follows a projected policy path and fit it to observed market prices. [[During_Fixed_Income_Ch16.md#page=133-134]]

## Mechanism: The 3-Tier Hierarchy

Reconciling expectations involves a hierarchical model:
1.  **Level 1: The Policy Path:** An assumed sequence of discrete central bank rate changes (e.g., +25bp hikes).
2.  **Level 2: The Overnight (O/N) Account:** A projected path of daily compounded overnight rates, derived from Level 1 but adjusted for timing (e.g., ECB hikes apply only to the next MRO settlement) and market spreads.
3.  **Level 3: Term Rates:** The results of the compounded O/N account are used to build the complete term structure. These are then compared with observed market rates to find the "best fit." [[During_Fixed_Income_Ch13.md#page=134-135]]

## Critical Adjustments

### 1. Discrete Probabilities
Policy changes occur in discrete steps (usually 25bp). Analysts interpret "smooth" implied market changes as probabilities.
- **Example:** A 10bp implied hike in the curve is interpreted as a **40% probability** of a 25bp hike.
- **The Timing Bias:** A 50% probability at two successive meetings often means the market expects *exactly one* hike, but is split on the timing, rather than expecting two hikes. [[During_Fixed_Income_Ch16.md#page=135]]

### 2. Operational Constraints
Policy changes are applied only on days when they *could* actually occur. The model must incorporate the central bank's **meeting calendar**. Otherwise, the solution space becomes too large and unrealistic. [[During_Fixed_Income_Ch16.md#page=135]]

### 3. Noise Stripping (The Basis)
- **Cash vs. Policy Basis:** If the policy rate is a repo rate (ECB) but the market trades unsecured (Euribor), a maturity-dependent credit spread must be subtracted.
- **The Turn Filter:** Technical spikes from the [[Turn_Premium_Mechanism|Turn Premium]] must be removed to prevent them from being misidentified as economic policy shifts. [[During_Fixed_Income_Ch16.md#page=135-136]]

## Evidence / Source Anchors

- Hierarchy of matching policy expectations to market rates (Policy -> O/N -> Term): [[During_Fixed_Income_Ch16.md#page=134-135]]
- Logic of discrete change interpretation and cumulative probability pitfalls: [[During_Fixed_Income_Ch16.md#page=135]]
- Importance of incorporating the meeting calendar into fitting models: [[During_Fixed_Income_Ch16.md#page=135]]
- Identification of the "Basis" problem (ECB repo vs. Euribor unsecured): [[During_Fixed_Income_Ch16.md#page=135]]

## Related

- [[Forward_Rates_Derivation]] — The mathematical engine for Level 3.
- [[Turn_Premium_Mechanism]] — The primary technical noise to be stripped.
- [[Term_Risk_Premium]] — The unobservable spread that complicates long-term extraction.
- [[Yield_Curve_Representations]] — The visual output of this fitting process.
