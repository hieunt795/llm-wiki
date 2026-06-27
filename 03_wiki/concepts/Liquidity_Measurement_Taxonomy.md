---
title: Liquidity Measurement Taxonomy
aliases:
- Liquidity Measurement
- Pre-trade indicators
- Post-trade indicators
- Indirect liquidity indicators
- Heisenberg Uncertainty in Finance
- Price vs Volume paradox
- Đo lường thanh khoản
type: mechanism
tags:
- market-infrastructure
- liquidity
- risk-management
- quantitative-finance
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch19.md
thesis: Liquidity measurement is fundamentally constrained by a counterfactual problem
  and a financial 'Heisenberg Uncertainty Principle,' necessitating a multi-layered
  taxonomy of indicators—pre-trade, post-trade, and indirect—to distinguish between
  microscopic breadth and macroscopic depth.
source_refs:
- file: During_Fixed_Income_Ch19.md
  page: 180
- file: During_Fixed_Income_Ch19.md
  page: 181
- file: During_Fixed_Income_Ch19.md
  page: 182
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Measuring the liquidity of an asset is the attempt to solve a **counterfactual problem**: *At what price could a trade take place (when it does not), and what would the price be if a trade had not occurred?* Alexander Düring explains that liquidity is not a static property of an asset but is dependent on the investor and the execution venue. Because of this complexity, no single indicator is sufficient; analysts must use a taxonomy of measures categorized by the information they consume. [[During_Fixed_Income_Ch19.md#page=180]]

## The Financial Heisenberg Uncertainty Principle

The core difficulty in measurement stems from the conflict between **Stock** and **Flow** measures:
- **Price (Stock):** A point-in-time assessment of value.
- **Volume (Flow):** The amount of assets changed hands over time.
- **The Paradox:** To measure flow precisely, one needs a long observation window. However, over that same period, external factors (news, data releases) affect price. It is mathematically impossible to perfectly separate price movements caused by trades (liquidity) from those caused by information (valuation). [[During_Fixed_Income_Ch19.md#page=180]]

## Taxonomy of Indicators

| Category | Typical Measures | Core Weakness / Bias |
| :--- | :--- | :--- |
| **Pre-trade** | Bid–offer spreads, Order book depth, Quote dispersion. | **Advertisement Bias:** Dealers show tight indicative quotes to attract business but may pull them or refuse firm execution when actual trade interest is revealed. [[During_Fixed_Income_Ch19.md#page=181]] |
| **Post-trade** | Trade volumes, Trade impact, Trade sizes, RFQ dispersion. | **Sample Bias:** Only "executable" trades are observed. The trades that *didn't* happen because they were too illiquid are missing from the data. [[During_Fixed_Income_Ch19.md#page=182]] |
| **No-trade (Indirect)** | Spline spread dispersion, Futures dislocation, Repo rates. | **Implementation Friction:** These measure arbitrage opportunities. While they reflect macroscopic depth, they are polluted by the cost of short-selling or financing (repo). [[During_Fixed_Income_Ch19.md#page=181-182]] |

## Strategic Distinction: Breadth vs. Depth

- **Microscopic (Breadth):** Related to single trade instances and dealer competition. Measured well by pre- and post-trade indicators.
- **Macroscopic (Depth):** The market's ability to absorb correlated, non-diversifiable flows. Often only revealed through indirect indicators like **Spline Spread Dispersion**. Lack of depth is usually only observed when it is most needed (e.g., during a crisis). [[During_Fixed_Income_Ch19.md#page=180-181]]

## Evidence / Source Anchors

- Definition of the counterfactual problem in liquidity: [[During_Fixed_Income_Ch19.md#page=180]]
- Analysis of the Stock (Price) vs. Flow (Volume) measurement conflict: [[During_Fixed_Income_Ch19.md#page=180]]
- Comprehensive taxonomy of 3 types of information used for indicators: [[During_Fixed_Income_Ch19.md#page=181]]
- Description of Advertisement Bias in pre-trade indicative quotes: [[During_Fixed_Income_Ch19.md#page=181]]
- Rationale for using indirect measures to gauge macroscopic depth: [[During_Fixed_Income_Ch19.md#page=182-183]]

## Related

- [[Market_Depth_Vs_Breadth]] — Detailed mechanics of risk absorption.
- [[Bid_Ask_Bounce_Mechanism]] — How wide spreads create artificial volatility.
- [[On_The_Run_Liquidity_Premium]] — A price-based indicator of liquidity concentration.
- [[Spline_Spread_Dispersion]] — The primary "No-trade" indicator.
- [[Indicative_Vs_Firm_Quotes]] — The distinction that drives Advertisement Bias.
