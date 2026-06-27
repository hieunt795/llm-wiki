---
title: Expectations Hypothesis in Yield Curves
aliases:
- Expectations Theory
- Taylor Rule in Curve Analysis
- Macro-Economic Shock Transmission
- Impulse-Response Curve Effects
type: mechanism
tags:
- monetary-policy
- macroeconomics
- central-banking
- yield-curves
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch21.md
thesis: The expectations hypothesis asserts that long-term interest rates are the
  geometric average of expected future short-term rates, serving as the primary channel
  through which macroeconomic data surprises and central bank reaction functions are
  priced into the yield curve.
source_refs:
- file: During_Fixed_Income_Ch21.md
  page: 206
- file: During_Fixed_Income_Ch21.md
  page: 207
- file: During_Fixed_Income_Ch21.md
  page: 208
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The expectations hypothesis provides the intellectual bridge between the economy and the bond market. Alexander Düring explains that market interest rates should reflect the projected path of central bank policy rates. However, he highlights a critical paradox: while economic models (like the Taylor Rule) suggest that data shocks should primarily affect the curve's slope, real-world data often results in nearly parallel shifts, suggesting that investors assign extreme persistence to even minor economic surprises. [[During_Fixed_Income_Ch21.md#page=206-207]]

## Mechanism: Translating Shocks to Curves

### 1. The Taylor Rule Framework
Analysts use the **Taylor Rule** to project the central bank's reaction function:
$$r = p + 0.5y + 0.5(p - 2) + 2$$
- where $p$ is inflation and $y$ is the output gap. Surprises in these variables force a reassessment of the target rate $r$. [[During_Fixed_Income_Ch21.md#page=206]]

### 2. Impulse-Response Persistence
Using a VAR (Vector Autoregression) model, Düring identifies two distinct shock profiles:
- **GDP Shock:** Typically less persistent. It primarily drives changes in the **Front-end Steepness** (e.g., the 2Y–5Y spread) as rates are expected to return to mean relatively quickly.
- **Inflation Shock:** Historically much more persistent. It leads to rate adjustments all along the curve. However, the high [[Present_Value_Of_A_Basis_Point|PVBP]] of long-term bonds acts as a dampener, reducing the absolute par rate move required to reflect these expectations. [[During_Fixed_Income_Ch21.md#page=207]]

### 3. The Credibility Filter
The persistence of an inflation shock is inversely related to central bank credibility. A credible inflation-targeter should reverse price shocks within 12–18 months. Düring's analysis of US data across decades (Figure 20.3) shows that the market's perception of shock persistence has changed significantly over time, meaning **investors must update their models as frequently as their data inputs**. [[During_Fixed_Income_Ch21.md#page=208]]

## Strategic Implications: The Parallel Shift Mystery

Standard expectations theory fails to explain why daily yield curve moves are predominantly **parallel**.
- **The Explanation:** This suggests that current data shocks are perceived to affect not just near-term policy, but the long-term equilibrium level of the natural rate ($r^*$). Factors like shifting demographics or structural productivity changes are "baked into" every daily data release by market participants. [[During_Fixed_Income_Ch21.md#page=208]]

## Evidence / Source Anchors

- Application of the Taylor Rule and VAR impulse-response functions to curve analysis: [[During_Fixed_Income_Ch21.md#page=206-207]]
- Analysis of GDP shocks affecting steepness vs. inflation shocks affecting the whole curve: [[During_Fixed_Income_Ch21.md#page=207]]
- Paradox of parallel curve shifts despite mean-reverting economic data: [[During_Fixed_Income_Ch21.md#page=207-208]]
- Discussion on central bank credibility as a driver of shock persistence: [[During_Fixed_Income_Ch21.md#page=208]]
- Identification of "over-shooting commitments" as a complication for Taylor Rule fitting: [[During_Fixed_Income_Ch21.md#page=208]]

## Related

- [[Yield_Curve_Drivers_Taxonomy]] — The broader context (Driver #1).
- [[Policy_Rate_Expectations_Extraction]] — The technical process of fitting these views.
- [[Taylor_Rule_Monetary_Policy]] — Deep dive into the reaction function.
- [[Wicksellian_Natural_Interest_Rate]] — The long-term target of the expectations path.
