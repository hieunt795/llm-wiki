---
title: Taylor Rule (Interest Rate Rule)
aliases:
- Taylor 1993 Formula
- Interest Rate Reaction Function
- Feedback Rule for Rates
type: mechanism
tags:
- monetary-policy
- central-banking
- mathematics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The Taylor Rule is a prescriptive guide for central banks to set short-term
  interest rates in response to changes in inflation and economic output, aiming to
  balance the dual goals of price stability and full employment.
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 201
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

Developed by John B. Taylor (1993), this rule moved monetary policy away from the "Black Box" of discretion toward a transparent, feedback-based system. It remains the most widely used benchmark for evaluating whether a central bank's policy stance is "Too Tight" or "Too Loose."

## Mechanism

### 1. The Original Formula
$$i_t = i^* + \pi_t + \alpha(y_t - y^*) + \beta(\pi_t - \pi^*)$$
Where:
- $i_t$: Target nominal policy rate.
- $i^*$: Equilibrium real interest rate (usually assumed to be 2%).
- $\pi_t$: Current inflation rate.
- $y_t - y^*$: Output gap (Actual vs Potential GDP).
- $\pi_t - \pi^*$: Inflation gap (Actual vs Target).
- $\alpha, \beta$: Coefficients (Weights) assigned by the central bank (Original Taylor weights: $\alpha=0.5, \beta=0.5$).

### 2. Research Nuances
- **The Taylor Principle:** $\beta$ must be greater than 0 (effectively making the nominal rate rise by *more* than the increase in inflation) to ensure real interest rates rise and dampen demand.
- **Backward-looking Nature:** The original rule is contemporaneous, meaning it responds to *current* shocks. Critics like Svensson (1997) argue this is inefficient due to transmission lags; hence the development of **Inflation-Forecast-Based (IFB)** rules.

## Boundaries / Conditions

### The Open Economy Modification
For EMEs, the Taylor rule is often augmented with an exchange rate term ($e_t$):
$$i_t = \text{Standard Taylor} + \gamma(e_t - \bar{e})$$
This reflects the "Fear of Floating" and the need to manage capital flow spillovers.

## Evidence / Source Anchors

- Original Taylor (1993) formula and variable definitions: [[Perry_Central_Bank_Policy_P4.md#page=201]]
- Criticism of contemporaneous response vs. policy lags: [[Perry_Central_Bank_Policy_P4.md#page=201]]
- Modification for open economies (Ball, 1997): [[Perry_Central_Bank_Policy_P4.md#page=201]]

## Related

- [[McCallum_Rule_Monetary_Base]] — The quantity-based alternative.
- [[Inflation_Targeting_Framework_ITF]] — The regime that most frequently employs Taylor-like rules.
- [[Central_Bank_Quadratic_Loss_Function]] — The mathematical origin of these weights.
