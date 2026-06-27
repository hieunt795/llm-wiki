---
title: Spline Spread Dispersion
aliases:
- Spline Dispersion
- Yield Curve Noise
- Fitting Error Indicator
- Indirect Liquidity Indicator
type: mechanism
tags:
- liquidity
- quantitative-finance
- yield-curve
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch19.md
thesis: Spline spread dispersion measures the aggregate deviation of individual bond
  prices from a theoretical smooth yield curve, serving as a powerful indirect indicator
  of macroscopic market liquidity and the confidence of arbitrageurs.
source_refs:
- file: During_Fixed_Income_Ch19.md
  page: 181
- file: During_Fixed_Income_Ch19.md
  page: 183
- file: During_Fixed_Income_Ch19.md
  page: 184
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

A liquid market is mathematically "smooth." In theory, bonds from the same issuer should not trade at prices that allow for obvious arbitrage. Alexander Düring explains that **Spline Spread Dispersion** captures the degree to which market participants are *unable* or *unwilling* to trade against mispricings. It is a "No-trade" indicator: it reflects the cost of trades that are **not being done**, rather than the ones that are. [[During_Fixed_Income_Ch19.md#page=181-182]]

## Mechanism: The Model-to-Market Gap

The dispersion is calculated through a three-step quantitative process:

1.  **Spline Fitting:** A fair-value model (typically a **Nelson-Siegel** or **Svensson** spline) is fitted to the entire universe of an issuer's bonds.
2.  **Residual Calculation:** The absolute yield deviation (spread) of each individual bond from this theoretical curve is measured.
3.  **Aggregation:** The average absolute deviation is plotted over time. [[During_Fixed_Income_Ch19.md#page=183]]

### The Arbitrage Signal
- **Low Dispersion:** Means the market is deep and arbitrageurs are efficiently "policing" the curve, buying cheap bonds and selling expensive ones until all fit the smooth spline.
- **High Dispersion:** Suggests that funding costs (repo), capital constraints, or fear of volatility prevent arbitrageurs from closing the gaps. A high dispersion is a clear signal of **macroscopic illiquidity**. [[During_Fixed_Income_Ch19.md#page=181]]

## Strategic Implications: Divergence Analysis

Düring identifies a critical divergence in 2015/16:
- **Microscopic Stability:** Bid-ask spreads (micro-liquidity) showed no significant deterioration.
- **Macroscopic Stress:** Spline dispersion spiked significantly during the same period.
- **The Insight:** This divergence was likely caused by the **Dodd-Frank Act** and other regulations that restricted dealer balance sheet commitment. Dealers were still competing for client trades (good breadth), but they were no longer willing to warehouse the idiosyncratic risks needed to keep the curve smooth (poor depth). [[During_Fixed_Income_Ch19.md#page=184]]

## Evidence / Source Anchors

- Definition of spline dispersion as a measure of potential arbitrage opportunities: [[During_Fixed_Income_Ch19.md#page=181]]
- Description of the Nelson-Siegel spline fitting process to calculate fair value: [[During_Fixed_Income_Ch19.md#page=183]]
- Analysis of the 2015/16 divergence between bid-ask spreads and spline dispersion: [[During_Fixed_Income_Ch19.md#page=184]]
- Discussion on how indirect indicators measure the cost of trades not performed: [[During_Fixed_Income_Ch19.md#page=183]]

## Related

- [[Liquidity_Measurement_Taxonomy]] — The category of indicators (No-trade) to which this belongs.
- [[Market_Depth_Vs_Breadth]] — Dispersion is the primary measure of depth.
- [[Nelson_Siegel_Spline_Models]] — The mathematical engine for the fair-value curve.
- [[Repurchase_Agreement_Repo_Market_Structure]] — High repo rates are often the friction that prevents dispersion from being closed.
