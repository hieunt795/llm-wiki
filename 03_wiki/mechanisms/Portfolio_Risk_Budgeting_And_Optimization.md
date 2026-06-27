---
title: Portfolio Risk Budgeting and Optimization
aliases:
- Risk Budgeting
- Mean-Variance Optimization
- Black-Litterman
- Rebalancing
- Risk Rationing
type: mechanism
tags:
- portfolio-management
- risk-management
- mathematics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch31.md
thesis: Portfolio risk budgeting is the systematic rationing of risk capital across
  multiple trades, utilizing optimization models while acknowledging the fundamental
  failure of mean-variance assumptions in the face of non-normal return distributions
  and diverse trade horizons.
source_refs:
- file: During_Fixed_Income_Ch31.md
  page: 346
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Few reasonable traders commit all available capital to a single trade. Instead, multiple trades compete for a fixed **Risk Capital Budget**. Alexander Düring explains that while mathematical models like **Mean-Variance Optimization** (Markowitz) and **Black-Litterman** exist to assist this process, they suffer from deep epistemological flaws when applied to the multi-dimensional complexity of fixed income trading. [[During_Fixed_Income_Ch31.md#page=346]]

## The Optimization Bottleneck

Standard portfolio optimization relies on two primary inputs: **Expected Returns (Mean)** and **Correlations (Variance/Covariance)**.

### 1. The Horizon Mismatch
Mean-variance optimization is typically a **single-period** approach. In a bond portfolio, different trades (e.g., a 2Y swap spread vs. a 30Y curve flattener) have vastly different expected horizons. Reconciling these into a single optimization window is mathematically and operationally hostile. [[During_Fixed_Income_Ch31.md#page=346]]

### 2. The Non-Normality Problem
Complex trading strategies (notably those involving [[Negative_Convexity_In_MBS|Negative Convexity]] or credit risk) exhibit strongly non-normal return distributions. Mean and variance are insufficient to describe the "Fat-tail" risk profiles of these instruments. [[During_Fixed_Income_Ch31.md#page=346]]

### 3. The Dynamic Estimation Gap
Trading decisions are often based on the assumption that recent trends will revert or that a structural change is imminent. This implies that the trader is explicitly betting that **past correlations and means will NOT hold**. Using historical variance to budget risk for a trade that bets against history is a fundamental contradiction in logic. [[During_Fixed_Income_Ch31.md#page=346]]

## Strategic Application: Risk Rationing

Given these flaws, practitioners use models as a guide but rely on **Risk Rationing**:
- **Diversification:** Ensuring that trades compensating each other's inherent risks are grouped correctly.
- **PVBP Alignment:** Ensuring that the nominal amount committed to each trade reflects its "dollar value of risk" ($DV01$) rather than just its principal value. [[During_Fixed_Income_Ch31.md#page=346]]

## Evidence / Source Anchors

- Analysis of risk rationing as a competition for a finite capital budget: [[During_Fixed_Income_Ch31.md#page=346]]
- Critique of Mean-Variance Optimization as a single-period model: [[During_Fixed_Income_Ch31.md#page=346]]
- Identification of non-normal return distributions in complex fixed income trades: [[During_Fixed_Income_Ch31.md#page=346]]
- Discussion on the logical conflict between StatArb views and historical variance inputs: [[During_Fixed_Income_Ch31.md#page=346]]

## Related

- [[Trading_Strategy_And_Principles]] — The source of the individual trades.
- [[Bond_Risk_Modified_Duration_And_PVBP]] — The primary metric for risk rationing ($DV01$).
- [[Statistical_Arbitrage_And_Smart_Beta]] — Why rebalancing is often based on mean-reversion views.
- [[Value_At_Risk_VaR]] — The standard (but flawed) metric for budgeting risk capital.
