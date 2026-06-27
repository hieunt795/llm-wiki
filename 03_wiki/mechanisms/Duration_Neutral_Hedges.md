---
title: Duration-Neutral Hedges
aliases:
- DV01-Neutral Hedge
- Duration Match
- Risk-Neutral Weighting
- Phòng vệ theo thời lượng
type: mechanism
tags:
- risk-management
- hedging
- duration
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch37.md
thesis: A duration-neutral hedge is the foundational strategy for neutralizing interest
  rate risk by offsetting the dollar-value price change of an existing position with
  an equal and opposite move in a hedge instrument, assuming a single yield factor
  explains the entire curve movement.
source_refs:
- file: During_Fixed_Income_Ch37.md
  page: 390
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

The simplest form of hedging assumes that if you know the sensitivity of a bond to interest rates (its DV01), you can neutralize it by taking an opposite position in another bond or future. Alexander Düring explains that while mathematically elegant ($N_2 = -N_1 D_1/D_2$), this model is fundamentally fragile because it relies on the **"Single Variable" assumption**—the idea that the same $dy$ shift applies to both instruments. [[During_Fixed_Income_Ch37.md#page=390]]

## Mechanism: The Two Perspective Paradigms

While the math is identical, different market actors manage duration neutrality using different units:

### 1. The Trader's Perspective (Nominal Focus)
- **Metric:** DV01 ($D$) — the dollar value change for 1bp shift.
- **Equation:** $N_1 D_1 = -N_2 D_2$
- **Logic:** Trading desks operate on nominal blocks and P&L limits. DV01 is the most direct translation of market moves into cash gain/loss. [[During_Fixed_Income_Ch37.md#page=390]]

### 2. The Fund Manager's Perspective (Market Value Focus)
- **Metric:** Modified Duration ($D^*$) — the percentage change for 1% shift.
- **Equation:** $M_1 D^*_1 = -M_2 D^*_2$
- **Logic:** Real money managers are measured by their return on Assets Under Management (AUM). Their "nominal" amount is the total market value ($M$) of their portfolio. [[During_Fixed_Income_Ch37.md#page=390]]

## Boundaries / Conditions: The Breaking Points

The duration-neutral hedge fails in two primary scenarios:

### 1. The Maturity Gap
If Bond 1 is a 2-year bond and Bond 2 is a 30-year bond, a single $dy$ shift is unrealistic. The curve almost never moves in a perfectly parallel way across such a wide spectrum (Level risk vs. Slope risk). [[During_Fixed_Income_Ch37.md#page=390]]

### 2. The Cross-Market Gap
If a trader attempts to hedge a US Treasury with a German Bund, the duration neutrality provides zero protection against changes in the **US-German Spread**. In these cases, the hedge is merely a bet on the spread rather than an interest rate insurance. [[During_Fixed_Income_Ch37.md#page=390]]

### 3. Stability Drift
Sensitivities ($D$ and $D^*$) are not constant. They decay as the bond ages (Theta) and as interest rates move (Convexity). A duration-neutral portfolio must be **actively rebalanced** to preserve its neutrality. [[During_Fixed_Income_Ch36.md#page=382]]

## Evidence / Source Anchors

- Mathematical derivation of the hedge condition for two bonds (Equation 36.2): [[During_Fixed_Income_Ch37.md#page=390]]
- Identification of the dichotomy between Trader (Nominal) and Fund Manager (Market Value) mental models: [[During_Fixed_Income_Ch37.md#page=390]]
- Critique of the 'dy as a non-indexed variable' assumption (Single Variable flaw): [[During_Fixed_Income_Ch37.md#page=390]]
- Analysis of hedge failure across disparate maturities and markets: [[During_Fixed_Income_Ch37.md#page=390]]

## Related

- [[Regression_Vs_PCA_Hedges]] — How to fix the Single Variable flaw using correlation.
- [[Yield_Curve_Model_Hedges]] — Hedging across the entire term structure.
- [[Bond_Risk_Modified_Duration_And_PVBP]] — The sensitivity inputs for these formulas.
- [[Risk_Neutral_Portfolios]] — The multi-factor goal of duration matching.
