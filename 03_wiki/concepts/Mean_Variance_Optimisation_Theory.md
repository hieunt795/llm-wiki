---
title: Mean-Variance Optimisation Theory
aliases:
- Modern Portfolio Theory
- MPT
- Efficient Frontier
- Markowitz Bullet
- Utility Function Optimization
- Tối ưu hóa Trung bình - Phương sai
type: mechanism
tags:
- portfolio-management
- quantitative-finance
- risk-management
- statistics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch38.md
thesis: Mean-variance optimisation is a single-period mathematical framework that
  balances expected returns against uncertainty (variance), utilizing a utility function
  to identify dominant portfolios along an efficient frontier while facing fundamental
  limitations in non-stationary fixed income environments.
source_refs:
- file: During_Fixed_Income_Ch38.md
  page: 395
- file: During_Fixed_Income_Ch38.md
  page: 398
- file: During_Fixed_Income_Ch38.md
  page: 399
- file: During_Fixed_Income_Ch38.md
  page: 401
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

For a single investment period with normally distributed returns, a portfolio is described entirely by two parameters: the expected return ($\mu$) and the uncertainty around that return (variance $\sigma^2$). Alexander Düring explains that while this Markowitz framework provides the foundation for all modern asset management, its application to fixed income is uniquely compromised by the finite lifetime of bonds and the structural evolution of market correlations. [[During_Fixed_Income_Ch38.md#page=395]]

## Mechanism: The Optimisation Engine

The objective is to maximize the investor's **Utility ($U$)**, defined as the expected return minus a penalty for risk:
$$U = \boldsymbol{\mu} w - \lambda w^T V w$$
- **$\lambda$ (Risk Aversion):** The trade-off parameter. A higher $\lambda$ means the investor demands more return for every unit of added variance.
- **The Solver:** By differentiating $U$ with respect to weights $w$, we find the optimal allocation:
$$w = \frac{1}{2\lambda} V^{-1} \boldsymbol{\mu}$$
- **The Numerical Trap:** Solving this requires inverting the covariance matrix $V$. For large numbers of assets, this process is numerically unstable and highly sensitive to small errors in the input data. [[During_Fixed_Income_Ch38.md#page=398-401]]

## Critical Limitations: The Convergence Paradox

Düring identifies three "epistemological hurdles" that prevent a naive implementation:

### 1. The Multi-Universe Problem
Mean and variance are statistics that determine random numbers but do not dictate them.
- **The Result:** Actual portfolio returns only converge to the model's predictions over extremely long periods.
- **The Paradox:** In the real world, an investor exists in only one realization of history. They cannot justify a current loss by pointing to an "average" across multiple alternative universes where they made money. [[During_Fixed_Income_Ch38.md#page=399-400]]

### 2. Bond Aging (The Non-Stationary V)
Unlike equities, which have indefinite lives, bonds decay.
- **The Problem:** As a bond approaches maturity, its duration shrinks, and its sensitivity to interest rates declines.
- **The Failure:** A historical covariance matrix ($V$) based on the last 5 years is **meaningless** for predicting the future of a bond that is 5 years older today. Fixed income risk is intrinsically non-stationary. [[During_Fixed_Income_Ch38.md#page=400-401]]

### 3. Correlation Convergence in Crisis
The model assumes stable correlations. Düring warns that during systemic shocks (e.g., 9/11 or 2020), correlations often "spike to 1," causing all diversified asset classes to collapse simultaneously, rendering the "Efficient Frontier" an illusion. [[During_Fixed_Income_Ch38.md#page=396]]

## Evidence / Source Anchors

- Mathematical definition of the utility-maximizing portfolio solver: [[During_Fixed_Income_Ch38.md#page=398-399]]
- Simulation-based proof of the slow convergence of sample mean and variance (Figure 37.2): [[During_Fixed_Income_Ch39.md#page=399]]
- Analysis of the "Numerical Instability" caused by inverting large covariance matrices: [[During_Fixed_Income_Ch38.md#page=401]]
- Comparison of risk-return distributions under positive and negative correlations: [[During_Fixed_Income_Ch38.md#page=395-396]]
- Critique of the 50-year irrelevance of initial ratings in Corporate vs. Sovereign contexts: [[During_Fixed_Income_Ch25.md#page=269]]

## Related

- [[Efficient_Frontier_And_CML]] — The geometric output of this theory.
- [[Index_Aggregation_For_Optimisation]] — How to fix the "aging" problem using sub-indices.
- [[Principal_Component_Analysis_PCA]] — A primary tool for dimension reduction.
- [[Portfolio_Risk_Budgeting_And_Optimization]] — The strategic rationing of capital.
- [[Statistical_Arbitrage_And_Smart_Beta]] — The automated application of these views.
