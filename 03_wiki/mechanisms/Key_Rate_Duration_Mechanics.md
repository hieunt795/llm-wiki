---
title: Key-Rate Duration Mechanics
aliases:
- Key-Rate '01s
- Partial Durations
- Yield Curve Decomposition
- Key-Rate DV01
type: mechanism
tags:
- risk-management
- hedging
- yield-curve
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat"
provenance: Tuckman_Serrat_2022.md
thesis: Key-rate metrics decompose total interest rate risk into sensitivities to
  specific segments of the term structure, allowing for precise hedging against non-parallel
  yield curve shifts (twists and butterflies).
source_refs:
- file: Tuckman_Serrat_2022.md
  page: 137
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Standard DV01 and Duration assume parallel shifts in the yield curve. However, empirical data shows the curve frequently twists (steepens/flattens) or changes curvature. Key-rate '01s and durations solve this by isolating the price impact of a rate change at a specific "key" maturity, while holding other key rates constant. [[Tuckman_Serrat_2022.md#page=148]]

## Mechanism: Key-Rate Shifts

To compute key-rate sensitivities, the framework assumes a set of key rates (e.g., 2yr, 5yr, 10yr, 30yr).
- **Linear Interpolation Assumption:** A shift in a specific key rate (e.g., 20-year) is assumed to decline linearly to zero at the adjacent key rates (10-year and 30-year).
- **Independence:** Each key-rate shift leaves all other key rates unchanged.
- **Summation Property:** The sum of all key-rate durations of a portfolio is equal (or very nearly equal) to its total duration. [[Tuckman_Serrat_2022.md#page=149]]

### Formal Definition
$$DV01_k = -\frac{1}{10,000} \frac{\partial P}{\partial y_k}$$
$$D_k = -\frac{1}{P} \frac{\partial P}{\partial y_k}$$
Where $y_k$ is the $k$-th key rate.

## Application: Asset-Liability Management (ALM)

### Case Study: Pension Fund Hedging (2022)
A pension fund with long-dated liabilities ($140M PV, $232,713 total DV01) uses key-rate decomposition (10yr, 20yr, 30yr, 40yr) to construct a robust hedge:
1.  **Exposure Profile:** The liabilities may show higher sensitivity to the 40yr key rate due to the long-dated nature of pension promises.
2.  **Hedge Construction:** Instead of one single hedge bond, the fund buys a portfolio of bonds (e.g., JNJ 2030, 2040, 2050, 2060) whose combined key-rate DV01s match those of the liabilities.
3.  **Result:** The portfolio is protected against "twists" where, for example, 10yr rates rise while 30yr rates fall. [[Tuckman_Serrat_2022.md#page=153-155]]

## Key-Rate vs. Forward-Bucket '01s
- **Key-Rate '01s:** Translate directly into hedging with liquid on-the-run instruments. Highly intuitive for traders.
- **Forward-Bucket '01s:** Shift individual segments of the forward curve. More interpretable for understanding curve shape changes but less direct for selecting hedging instruments. [[Tuckman_Serrat_2022.md#page=158]]

## Evidence / Source Anchors

- Decomposition of JPM Government Bond Fund duration: [[Tuckman_Serrat_2022.md#page=149]]
- Visual representation of linear key-rate shifts: [[Tuckman_Serrat_2022.md#page=150]]
- System of equations for multi-bond key-rate hedging: [[Tuckman_Serrat_2022.md#page=155]]
- Comparison with Partial PV01s used in swap desks: [[Tuckman_Serrat_2022.md#page=156]]

## Related

- [[Modified_Duration]] — The aggregate sensitivity being decomposed.
- [[Principal_Component_Analysis_PCA]] — An alternative empirical way to decompose curve risk.
- [[Yield_Curve_Trading_Strategies]] — Practical use of key-rate profiles.
