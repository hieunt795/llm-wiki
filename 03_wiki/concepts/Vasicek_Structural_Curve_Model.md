---
title: Vasicek Structural Curve Model
aliases:
- Vasicek Spline
- Mean-reverting Short Rate Model
- Structural Curve Model
type: mechanism
tags:
- quantitative-finance
- stochastic-calculus
- yield-curves
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch20.md
thesis: The Vasicek model is a structural curve representation that derives the entire
  term structure from a single mean-reverting stochastic process of the short rate,
  providing a closed-form solution for discount factors based on long-term volatility
  and reversion speed.
source_refs:
- file: During_Fixed_Income_Ch20.md
  page: 200
- file: During_Fixed_Income_Ch20.md
  page: 201
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Unlike parametric models (like Nelson-Siegel) which are purely descriptive, **Structural Models** like Vasicek attempt to ground the curve's shape in the physics of interest rate evolution. Alexander Düring explains that the "beauty" of the Vasicek model lies in its mathematical parsimony: the entire curve shape is determined by the volatility $(\sigma)$ and mean-reversion strength $(k)$ of the short-term rate. [[During_Fixed_Income_Ch20.md#page=200]]

## Mechanism: The Stochastic Process

The evolution of the short rate $(r_t)$ is modeled as a Wiener process with mean reversion:
$$dr_t = k(\theta - r_t)dt + \sigma dW_t$$
- **$k$:** The speed at which rates return to the mean.
- **$\theta$:** The long-term mean level of interest rates.
- **$\sigma$:** The volatility of the short rate. [[During_Fixed_Income_Ch20.md#page=200]]

### The Closed-form Solution
Vasicek allows for a direct calculation of the Discount Factor ($Df$) without numerical integration:
$$Df(t) = B(t) e^{-r_0 A(t)}$$
- where $A(t)$ and $B(t)$ are functions of the model parameters. This makes the model extremely efficient for high-frequency calibration. [[During_Fixed_Income_Ch20.md#page=200]]

## Critical Critique: The Volatility Disconnect

A theoretical structural model should imply a volatility that matches market-traded options. However, Düring's empirical analysis reveals a massive disconnect:

1.  **The Evidence:** A scatter plot of the $\sigma$ parameter from a Vasicek spline (fitted to US Treasuries) against the CBOE VXTYN index (market-traded Treasury volatility) shows an $R^2$ of **less than 0.1**.
2.  **The Inference:** It is extremely difficult to achieve a self-consistent calibration of interest rates and volatility in a structural model. The "volatility" needed to fit the static shape of the yield curve is not the same as the "volatility" expected by option traders. [[During_Fixed_Income_Ch20.md#page=201-202]]

## Evidence / Source Anchors

- Mathematical formula for the Vasicek short-rate process and closed-form Df: [[During_Fixed_Income_Ch20.md#page=200]]
- Interpretation of parameters $k$ (reversion speed) and $\sigma$ (volatility): [[During_Fixed_Income_Ch20.md#page=200]]
- Sensitivity analysis of zero rates to bumps in Vasicek parameters (Figure 19.5): [[During_Fixed_Income_Ch20.md#page=201]]
- Empirical proof of the low correlation ($R^2 < 0.1$) between model-implied and market-traded volatility: [[During_Fixed_Income_Ch20.md#page=201-202]]

## Related

- [[Yield_Curve_Representations]] — The context of structural models.
- [[Stochastic_Calculus_Fundamentals]] — The basis for the Wiener process $dW_t$.
- [[CBOE_VXTYN_Volatility_Index]] — The market benchmark that refutes simple structural fitting.
- [[Black_Scholes_Option_Pricing]] — The alternative model for extracting "market" volatility.
- [[Bootstrapping_Curve_Construction]]
- [[Nelson_Siegel_Svensson_Curve_Models]]
