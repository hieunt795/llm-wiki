---
title: Trend Following vs Mean Reversion Simulations
aliases:
- Dynamic Asset Allocation (Simulations)
- Strategy Sensitivity k
- Mean Reversion Speed
- Performance under Covariance
type: evidence
tags:
- quantitative-finance
- trading-strategies
- statistics
status: verified
confidence: 5
half_life_years: 1
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch39.md
thesis: Quantitative simulations demonstrate that the optimal asset allocation strategy
  is a function of the market's underlying mean-reversion speed and covariance structure,
  where trend-following outperforms during periods of weak mean-reversion and negative
  asset correlation.
source_refs:
- file: During_Fixed_Income_Ch39.md
  page: 407
- file: During_Fixed_Income_Ch39.md
  page: 408
- file: During_Fixed_Income_Ch39.md
  page: 409
created: '2026-04-13'
updated: '2026-04-20'
---

## Overview

Because real-world probability distributions have time-varying parameters that obscure strategy performance, Alexander Düring utilizes a controlled simulation environment. By applying four distinct allocation strategies to three hypothetical assets (matching Bonds, Equities, and Cash), he quantifies the impact of autocorrelation on terminal portfolio value. [[During_Fixed_Income_Ch39.md#page=407]]

## Mechanism: The Stochastic Process

The simulated returns $r_t$ follow a discrete-time mean-reverting process:
$$r_t = \lambda m + (1 - \lambda) r_{t-1} + w_t$$
- **$\lambda$ (Reversion Speed):** High $\lambda$ favors Mean Reversion strategies.
- **$w_t$:** Stochastic innovation with zero mean and constant covariance $M$.
- **$m$ (Expected Return):** Defined proportional to variance (CAPM-consistent). [[During_Fixed_Income_Ch39.md#page=407]]

## The Strategy Sensitivity Parameter ($k$)

Düring models the active strategies using a common sensitivity factor $k$ to adjust weights $w_i$:

### 1. Mean Reversion Logic
$$w'_{i,t} = w_{i,t-1} - k(r_{i,t-1} - m_i)$$
- Decreases weight in assets that out-performed their average ($m_i$) in the previous period. [[During_Fixed_Income_Ch39.md#page=407]]

### 2. Trend Following Logic
$$w'_{i,t} = w_{i,t-1} + k(r_{i,t-1} - m_i)$$
- Increases weight in out-performers, betting on positive autocorrelation. [[During_Fixed_Income_Ch39.md#page=408]]

## Findings: Performance Attribution

### 1. The Covariance Multiplier
Simulation results (Figure 38.2) show that the performance gap between strategies is amplified by the **Covariance Structure**.
- **Negative Covariance:** Asset allocation decisions are most decisive. The ability to switch from a losing asset to an independent winning asset creates the highest alpha.
- **Positive Covariance:** Assets behave as partial substitutes, reducing the benefit of active rebalancing. [[During_Fixed_Income_Ch39.md#page=408-409]]

### 2. The Reversion Speed Threshold
- **Weak Mean Reversion ($\lambda$ is low):** Trend-following consistently pays off and outperforms all other strategies.
- **Strong Mean Reversion:** The contrarian approach (Mean Reversion) dominates, and trend-followers are punished by "buying the highs." [[During_Fixed_Income_Ch39.md#page=408]]

## Evidence / Source Anchors

- Definition of the discrete-time mean-reverting return process (Equation 38.1): [[During_Fixed_Income_Ch39.md#page=407]]
- Analysis of the proportional relationship between expected return and variance (CAPM logic): [[During_Fixed_Income_Ch39.md#page=407]]
- Mathematical formulation of the weight adjustment formulas using parameter $k$: [[During_Fixed_Income_Ch39.md#page=407-408]]
- Comparison of strategy performance paths under 4 different settings of reversion and covariance (Figure 38.2): [[During_Fixed_Income_Ch39.md#page=409]]

## Related

- [[Portfolio_Rebalancing_Strategies]] — The taxonomy of the strategies tested.
- [[Mean_Variance_Optimisation_Theory]] — The static starting point for these dynamic tests.
- [[Statistical_Arbitrage_And_Smart_Beta]] — Real-world implementations of the simulated logics.
- [[Autocorrelation_Mechanics_In_Finance]] — The statistical phenomenon being exploited.
