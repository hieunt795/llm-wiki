---
title: Yield Curve Trading Strategies
aliases:
- Curve Trading
- Steepener
- Flattener
- Butterfly Trade
- Condor
- Giao dịch đường cong
type: mechanism
tags:
- trading-strategies
- yield-curves
- fixed-income
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch32.md
thesis: Curve trading is the systematic assumption of risk based on anticipated changes
  in the yield curve's geometry (level, slope, or curvature), utilizing multi-legged
  portfolios designed to isolate specific risk factors through duration-neutral weighting.
source_refs:
- file: During_Fixed_Income_Ch32.md
  page: 347
- file: During_Fixed_Income_Ch32.md
  page: 348
- file: During_Fixed_Income_Ch32.md
  page: 349
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 4542-4623
  section: "Chapter 6.1: Trading Terminology and Yield Curve Strategy Framework"
created: '2026-04-18'
updated: '2026-05-07'
---

## Thesis

Yield curve strategies move beyond simple directional bets on interest rates. Alexander Düring explains that these trades are designed to target relative value between different maturity points. A core principle is that any risk position must be analyzed relative to the **Forward Curve**, not the current spot curve, as carry and roll-down are already "baked into" the market pricing. [[During_Fixed_Income_Ch32.md#page=347]]

## Taxonomy of Curve Strategies

| Legs | Name | Objective | Risk Isolation |
| :--- | :--- | :--- | :--- |
| **1** | **Outright** | Directional move in yields. | Exposed to Level shifts (Factor 1). |
| **2** | **Spread (2-leg)** | Change in curve slope. | **Steepener:** Buy short, sell long. **Flattener:** Sell short, buy long. |
| **3** | **Butterfly** | Change in curvature (hump). | **Bullet vs. Wings.** Hedged against Level and Slope. |
| **4** | **Condor** | Change in "spread of spreads". | Compares two different spread sectors (e.g., 2Y-5Y vs. 10Y-30Y). |

[[During_Fixed_Income_Ch32.md#page=347]]

## Mechanism: The $n$-Equation System

To determine the exact notional amount ($N_i$) for each leg of an $n$-legged trade, a trader must solve a system of $n$ equations:

1.  **Equation 1 (Size):** Sets the total risk of the trade (e.g., total $PVBP$ of the long side).
2.  **Equations 2 to $n$ (Hedges):** Each additional leg is used to neutralize the risk factors of lower-order strategies. For example, a 3-leg butterfly uses its 2 extra parameters to be **duration-neutral** (no level risk) and **slope-neutral** (no steepening risk). [[During_Fixed_Income_Ch32.md#page=349]]

## Risk Decomposition Models

To manage curve risk effectively, traders use advanced decomposition models to analyze sensitivities across the term structure.

### 1. Partial ’01s and PV01 (Swap Market Standard)
- **Mechanism:** Decomposes the total **PV01** (Present Value of an ’01) of a swap portfolio into exposures at specific **fitting points** (usually 15-25 points) on the swap curve.
- **Hedging:** Highly intuitive for market makers. Each partial ’01 can be hedged by receiving or paying fixed in a swap whose term matches that specific fitting point.
- **Caveat:** Shifting a single fitting point while holding others constant can create non-local artifacts (e.g., unintended sensitivity in adjacent tenors) if the curve-fitting methodology is not sufficiently robust. [[Tuckman_Serrat_2022.md#page=156]]

### 2. Forward-Bucket ’01s
- **Mechanism:** Shifts "buckets" or segments of the **Forward Curve** (e.g., 1-2Y, 3-5Y, 6-9Y) directly.
- **Interpretability:** Offers a more intuitive view of how changes in the **shape** of the term structure (e.g., a "hump" in the 3-5Y forward rates) affect portfolio value.
- **Comparison:** Unlike Key-rate ’01s, forward-bucket ’01s do not translate directly into liquid hedging instruments but are superior for analyzing structural curve shifts. [[Tuckman_Serrat_2022.md#page=158]]

## Strategic Pitfalls

### 1. Benchmark Jumps
The curve is typically measured using benchmark bonds. When a sovereign issues a new bond (extending the benchmark maturity), the yield spread may "jump" mechanically.
- **The Error:** An analyst sees a spread widening and enters a steepener.
- **The Reality:** It was a technical **Benchmark Jump**, not an economic move. Düring recommends using **Spline Yields** for analysis to avoid this trap. [[During_Fixed_Income_Ch32.md#page=350]]

### 2. Implementation Friction
Curve trades increase in transaction costs with each added leg.
- **The Trade-off:** While higher-order trades (Butterflies/Condors) offer more precise risk isolation, they suffer from lower absolute volatility and higher bid-offer friction, requiring significant informational advantages to be profitable. [[During_Fixed_Income_Ch32.md#page=349]]

## Evidence / Source Anchors

- Definition of curve trading as anticipation of shape changes: [[During_Fixed_Income_Ch32.md#page=347]]
- Systematic table of 1, 2, 3, and 4-legged strategies: [[During_Fixed_Income_Ch32.md#page=347]]
- The logic of $n$ equations for $n$ legs to achieve risk-neutrality: [[During_Fixed_Income_Ch32.md#page=349]]
- Analysis of "Benchmark Jumps" creating artificial curve moves: [[During_Fixed_Income_Ch32.md#page=350]]
- Discussion on the information advantage required for complex strategies: [[During_Fixed_Income_Ch32.md#page=349]]

## Related

- [[PCA_Factor_Interpretation]] — The empirical basis for Level, Slope, and Curvature.
- [[Butterfly_Trade_Mechanics]] — Detailed view of the 3-leg weighting.
- [[Steepener_And_Flattener_Trades]] — Deep dive into 2-leg spread dynamics.
- [[Bond_Carry_And_Forward_Pricing]] — Why forward curves are the baseline for entry.
