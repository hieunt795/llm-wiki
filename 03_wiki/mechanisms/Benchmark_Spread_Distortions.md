---
title: Benchmark Spread Distortions
aliases:
- Benchmark Jump
- Spline vs Benchmark
- Maturity Extension Noise
type: mechanism
tags:
- yield-curves
- market-infrastructure
- trading
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch32.md
thesis: Benchmark spread distortions—notably 'Benchmark Jumps'—are artificial curve
  shape changes caused by the periodic issuance of new securities that extend the
  maturity anchor of a sector without any underlying change in economic value.
source_refs:
- file: During_Fixed_Income_Ch32.md
  page: 350
- file: During_Fixed_Income_Ch32.md
  page: 351
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Curve trading strategies often rely on "Benchmark Spreads" (e.g., 2Y vs 5Y yields). Alexander Düring warns that these spreads are subject to technical noise that can trigger false trading signals. The most significant of these is the **Benchmark Jump**, a byproduct of how sovereigns manage their debt issuance. [[During_Fixed_Income_Ch32.md#page=350]]

## Mechanism: The Benchmark Jump

1.  **Issuance Timing:** Sovereigns issue new "on-the-run" benchmark bonds periodically.
2.  **Maturity Extension:** A new 5-year bond will have a maturity roughly half a year longer than the old 5-year benchmark at the moment of switch.
3.  **The Jump:** Because the yield curve is typically upward-sloping, the new (longer) bond will naturally have a higher yield.
4.  **The False Signal:** On the day of the switch, the 2Y-5Y spread will appear to "steepen" and the 5Y-10Y spread will appear to "flatten" simply because the 5Y anchor point has moved up the curve. [[During_Fixed_Income_Ch32.md#page=350-351]]

## Strategic Mitigation: Spline Yields

To see through this technical noise, professionals use **Spline Models** (like Nelson-Siegel).
- **The Process:** Instead of using the yield of a specific bond, the analyst uses the yield of a fixed maturity point (e.g., exactly 5.0 years) on a smoothed theoretical curve.
- **The Benefit:** Splines are immune to benchmark jumps because the maturity point $t$ remains constant over time. If a spline spread changes, it reflects a genuine economic shift in the market's consensus view. [[During_Fixed_Income_Ch32.md#page=350]]

## Evidence / Source Anchors

- Analysis of benchmark spreads as subject to technical jumps during bond switches: [[During_Fixed_Income_Ch32.md#page=350]]
- Identification of the German OBL switch (OBL177 to OBL178) on July 25, 2018, as a case study: [[During_Fixed_Income_Ch32.md#page=350-351]]
- Recommendation to use spline yields to filter out maturity-extension noise: [[During_Fixed_Income_Ch32.md#page=350]]
- Comparison of actual benchmark spread jumps vs. stable spline spread behavior (Figure 31.5): [[During_Fixed_Income_Ch32.md#page=351]]

## Related

- [[Yield_Curve_Trading_Strategies]] — Why avoiding these distortions is critical for strategy.
- [[Nelson_Siegel_Spline_Models]] — The primary tool for creating the smoothed benchmark.
- [[On_The_Run_Liquidity_Premium]] — Another distortion linked to benchmark status.
- [[Spline_Spread_Dispersion]] — Measuring how far the benchmarks deviate from the spline.
- [[Preferred_Habitat_Market_Distortions]]
- [[Bid_Ask_Bounce]]
- [[Bond_Futures_Contract_Design]]
- [[Hedge_Based_Pricing_Anchor]]
- [[Indicative_Vs_Firm_Quotes]]
- [[I_Spread_Vs_ASW]]
- [[Liquidity_Hierarchy_Mechanism]]
- [[Mistrade_And_Fat_Finger_Mechanics]]
- [[Order_Flow_FX_Determination]]
- [[TED_Spread_Mechanism]]
- [[Trade_Implementation_Consistency]]
- [[Curve_Hedged_Bond_Spreads]]
- [[Bond_Index_Principles]]
- [[Bond_Relative_Value_Valuation]]
- [[CLOB_Vs_OTC_Execution]]
- [[Credit_Ratings_And_Migration]]
- [[Credit_Risk_Transfer_CRT]]
- [[Dark_Pools]]
