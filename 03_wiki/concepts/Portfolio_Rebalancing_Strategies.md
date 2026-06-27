---
title: Portfolio Rebalancing Strategies
aliases:
- Rebalancing
- Constant Asset Allocation
- Trend-Following
- Mean Reversion
- Reinvestment Logic
- Tái cân đối danh mục
type: mechanism
tags:
- portfolio-management
- risk-management
- behavioral-finance
- trading-strategies
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch39.md
thesis: Portfolio rebalancing is the systematic adjustment of asset weights to maintain
  a risk profile or exploit return patterns, characterized by an implicit assumption
  about the autocorrelation structure of asset returns.
source_refs:
- file: During_Fixed_Income_Ch39.md
  page: 403
- file: During_Fixed_Income_Ch39.md
  page: 404
- file: During_Fixed_Income_Ch39.md
  page: 406
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Performance is an ambiguous concept until the rebalancing strategy is defined. Alexander Düring demonstrates that the future value of a portfolio depends heavily on how gains are reinvested. Rebalancing is not just an administrative task; it is an expression of an investor's belief in market efficiency and the persistence of trends. [[During_Fixed_Income_Ch39.md#page=403]]

## Taxonomy of Rebalancing Archetypes

| Strategy | Rule | Implicit Assumption |
| :--- | :--- | :--- |
| **No Reallocation** | Buy-and-hold; reinvest gains in the same asset. | Past performance predicts future success (Momentum). |
| **Constant Allocation** | Periodically sell winners and buy losers to restore fixed weights. | **Passive Mean Reversion**: Assets that out-performed will likely revert to mean. |
| **Trend-Following** | Aggressively overweight assets that have performed well. | **Positive Autocorrelation**: A trend will likely continue. |
| **Mean Reversion** | Underweight assets that have performed well in anticipation of a dip. | **Negative Autocorrelation**: Price spikes are temporary and will reverse. |

[[During_Fixed_Income_Ch39.md#page=404-406]]

## Strategic Implications: The Failure of Invariance

### 1. The Time-Invariance Trap
The "No Reallocation" (Buy-and-hold) strategy is not time-invariant.
- **The Problem:** The weight of each asset depends on its performance since inception.
- **The Paradox:** Two investors who buy the same assets but start at different times will eventually hold completely different risk exposures, making the strategy non-standardizable for institutional risk management. [[During_Fixed_Income_Ch39.md#page=404]]

### 2. The Autocorrelation Mirror
Düring proves that "Supposedly passive" strategies (like constant weighting) actually take an active stance on market physics:
- A trader who cuts losses and lets profits run is following a strategy halfway between **No Reallocation** and **Constant Allocation**.
- Success depends entirely on whether the market's true autocorrelation matches the chosen rebalancing frequency. [[During_Fixed_Income_Ch39.md#page=403]]

### 3. The Cross-Currency Collision
In global portfolios, rebalancing can lead to contradictory actions:
- If the USD appreciates, a European fund must **sell** US equities to restore its Euro-denominated weight.
- Simultaneously, a US fund may **buy** those same equities because their local dollar price is unchanged or lower.
- **The Insight:** Both actions are "correct" under their respective rebalancing mandates, illustrating that the "optimal" trade depends on the home currency of the investor. [[During_Fixed_Income_Ch39.md#page=406]]

## Evidence / Source Anchors

- Mathematical proof of 3 different terminal values for the same 2-asset portfolio based on reinvestment strategy: [[During_Fixed_Income_Ch39.md#page=403]]
- Analysis of 'No Reallocation' as a bet on the rationality of market valuations: [[During_Fixed_Income_Ch39.md#page=404]]
- Identification of Constant Asset Allocation as a 'selling the best and buying the worst' approach: [[During_Fixed_Income_Ch39.md#page=406]]
- Description of the Cross-Currency rebalancing paradox: [[During_Fixed_Income_Ch39.md#page=406]]
- Definition of Trend-following as a passive strategy that relies on others' decisions: [[During_Fixed_Income_Ch39.md#page=406]]

## Related

- [[Index_Tracking_And_Replication_Risk]] — Rebalancing to match a benchmark.
- [[Statistical_Arbitrage_And_Smart_Beta]] — The automated version of Mean Reversion/Trend Following.
- [[Trend_Following_Vs_Mean_Reversion_Simulations]] — Quantitative proof of strategy performance.
- [[Cross_Currency_Rebalancing_Paradox]] — Detailed view of the currency conflict.
