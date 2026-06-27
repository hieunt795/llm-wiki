---
title: Trade Implementation Consistency
aliases:
- Implementation Risk
- Model Error (Trading)
- Sample Bias
- Carry Distortion
type: mechanism
tags:
- trading
- risk-management
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch31.md
thesis: Trade implementation consistency is the rigorous alignment between an analytical
  rationale and the technical execution, identifying four systematic failure points—Model
  Error, Basis Risk, Sample Bias, and Carry Distortion—that invalidate the original
  risk-reward thesis.
source_refs:
- file: During_Fixed_Income_Ch31.md
  page: 345
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The bridge between a "good idea" and a "profitable trade" is often broken by poor implementation. Alexander Düring explains that consistency is the most common operational failure in fixed income. If the instruments selected to express a view carry risks that are not part of the initial analysis, the trade becomes a gamble rather than a calculated risk. [[During_Fixed_Income_Ch31.md#page=345]]

## The 4 Systematic Failure Points

### 1. Model Error (Spline Mismatch)
- **The Process:** A spline model identifies a "cheap" sector on the yield curve.
- **The Error:** A trader buys all bonds in that sector.
- **The Consistency Trap:** If *every* bond in the sector appears cheap to the model, it is a sign that the **model is wrong** (e.g., it doesn't fit the actual curve shape), rather than the bonds being mispriced. A consistent trade targets bonds that are cheap relative to their immediate neighbors *within* a well-fitted model. [[During_Fixed_Income_Ch31.md#page=345]]

### 2. Basis Risk (Instrument Substitution)
- **The Process:** Analysis is performed on cash bonds, but the trade is implemented via Futures to save on transaction costs.
- **The Error:** Failing to check if the [[Futures_Basis_And_Implied_Repo_Rate|Basis]] is at fair value. 
- **The Result:** The performance of the basis may completely counteract the anticipated move in the bonds, rendering the analysis irrelevant. [[During_Fixed_Income_Ch31.md#page=345]]

### 3. Sample Bias (Idiosyncratic Overload)
- **The Process:** A trader concludes that a specific asset class (e.g., AA-rated bank debt) is undervalued.
- **The Error:** Implementing the view by purchasing a **single bond** from a single issuer.
- **The Result:** The trade is now 90% exposed to the specific corporate destiny of that one bank (idiosyncratic risk) and only 10% to the "AA bank debt" thesis. [[During_Fixed_Income_Ch31.md#page=345]]

### 4. Carry Distortion (Risk-Weight Sabotage)
- **The Process:** A spread analysis suggests a certain duration-neutral weight between two assets.
- **The Error:** The trader observes that the neutral weight results in **Negative Carry**. They then arbitrarily "adjust" the weights to achieve positive carry.
- **The Result:** The trade is no longer risk-neutral and no longer reflects the original spread analysis. It is now a directional bet disguised as a spread trade. [[During_Fixed_Income_Ch31.md#page=345]]

## Evidence / Source Anchors

- Identification of consistency as the primary implementation problem in fixed income: [[During_Fixed_Income_Ch31.md#page=345]]
- Analysis of Model Error via sector misidentification: [[During_Fixed_Income_Ch31.md#page=345]]
- Description of Basis Risk when substituting futures for bonds: [[During_Fixed_Income_Ch31.md#page=345]]
- Definition of Sample Bias as an accidental idiosyncratic bet: [[During_Fixed_Income_Ch31.md#page=345]]
- Critique of Carry-driven weight adjustments invalidating rational analysis: [[During_Fixed_Income_Ch31.md#page=345]]

## Related

- [[Trading_Strategy_And_Principles]] — The broader context of consistency.
- [[Yield_Curve_Fitting_Optimization]] — How to prevent Model Error.
- [[Futures_Basis_And_Implied_Repo_Rate]] — The metric to check for Basis Risk.
- [[Yield_Curve_Carry_And_Roll_Down]] — The "lure" that causes Carry Distortion.
