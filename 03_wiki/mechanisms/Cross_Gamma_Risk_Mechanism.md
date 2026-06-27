---
title: Cross-Gamma Risk Mechanism
aliases:
- Cross-Gamma
- Multi-Factor Convexity
- Correlation-Induced Sensitivity
type: mechanism
tags:
- risk-management
- derivatives
- quantitative-finance
- fx
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch36.md
thesis: Cross-gamma risk describes the non-linear change in an instrument's sensitivity
  to one risk factor as a direct result of changes in a separate, independent market
  variable, representing a high-order 'blind spot' in standard risk models.
source_refs:
- file: During_Fixed_Income_Ch36.md
  page: 382
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Standard risk metrics like Gamma measure how the sensitivity to a variable (e.g., interest rates) changes as that same variable moves. Alexander Düring explains that for multi-asset or international portfolios, a more insidious risk exists: **Cross-Gamma**. This represents a second-order derivative across two different variables, where the hedge quality for one risk factor is eroded by the movement of another. [[During_Fixed_Income_Ch36.md#page=382]]

## Mechanism: The Interaction Effect

In a multi-factor world where price $P$ depends on variables $y$ (interest rates) and $z$ (e.g., FX rates), cross-gamma is defined as:
$$\gamma_{\text{cross}} = \frac{\partial^2 P}{\partial y \partial z}$$

### 1. The Foreign Bond Example
Consider a domestic investor holding a bond denominated in a foreign currency.
- **Factor 1 ($y$):** Foreign interest rates.
- **Factor 2 ($z$):** The FX exchange rate.
- **The Interaction:** The absolute domestic-currency sensitivity to foreign rate moves (DV01) is not constant. If the foreign currency appreciates ( $z$ increases), the portfolio's total domestic-currency exposure to those interest rates **increases proportionally**.
- **The Result:** The investor finds themselves "over-hedged" or "under-hedged" on interest rates simply because the currency moved, even if interest rates stayed perfectly still. [[During_Fixed_Income_Ch36.md#page=382]]

### 2. The Inflation Equivalence
Düring notes that holdings in **Inflation-Linked Bonds** are mathematically equivalent to holdings in a foreign currency (the purchasing power unit). While CPI indices change more slowly than FX rates, the cross-gamma logic still applies: your real duration exposure drifts as the nominal price level shifts. [[During_Fixed_Income_Ch36.md#page=382]]

## Strategic Implications: Dynamic Correlation

Standard VaR (Value-at-Risk) models often treat cross-gamma as a constant or ignore it entirely.
- **The Trap:** During market stress, FX and interest rates often move violently and simultaneously. 
- **The Consequence:** Cross-gamma effects can cause hedges to fail exactly when they are most needed, as the "amount" of risk being hedged is itself a moving target. [[During_Fixed_Income_Ch36.md#page=382]]

## Evidence / Source Anchors

- Definition of cross-gamma as a second derivative across two different variables: [[During_Fixed_Income_Ch36.md#page=382]]
- Analysis of the proportional change in portfolio exposure due to FX fluctuations: [[During_Fixed_Income_Ch36.md#page=382]]
- Identification of inflation-linked debt as a cross-gamma-sensitive asset class: [[During_Fixed_Income_Ch36.md#page=382]]
- Distinction between standard gamma ($\frac{\partial^2 P}{\partial y^2}$) and cross-gamma ($\frac{\partial^2 P}{\partial y \partial z}$): [[During_Fixed_Income_Ch36.md#page=382]]

## Related

- [[Risk_Neutral_Portfolios]] — Why cross-gamma makes neutrality hard to maintain.
- [[Inflation_Indexed_Bonds]] — An asset class inherently exposed to cross-gamma.
- [[Convexity_Bias_Mechanism]] — The first-order (single variable) equivalent.
- [[Delta_Gamma_Hedging]] — The trading process that cross-gamma complicates.
- [[Model_Risk_And_Jumps]]
- [[ABS_Tranching_And_Default_Risk]]
- [[Risk_and_Valuation_Adjustments_xVA]]
- [[Cross_Currency_Rates_Synthetics]]
- [[Herstatt_Risk]]
- [[Liquidity_Measurement_Taxonomy]]
