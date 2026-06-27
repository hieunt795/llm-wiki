---
title: Value at Risk (VaR)
aliases: [VaR, Value-at-risk, Daily VaR, DVAR]
type: mechanism
tags: [risk-management, market-risk, quantitative-finance]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Value at Risk (VaR) is a forward-looking market risk measure that estimates the maximum loss a position could incur over a given holding period at a specified confidence level, using historical price distributions and probabilities.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 2527-2604
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] VaR answers: "What is my maximum loss at 95% (or 98%) confidence over the next N days?" Unlike instantaneous Greeks/duration measures (how much do I lose if rates move 1bp today), VaR is forward-looking: uses historical price distributions to estimate tail risk. Three main calculation methods: (1) Variance/Covariance — assumes normal distribution, fastest but least flexible. (2) Monte Carlo — simulates many price paths, handles complex derivatives/correlations. (3) Historical Simulation — replays historical market shocks, distribution-free but requires sufficient history. VaR is always conditional on holding period (1-day VaR < 10-day VaR) and confidence level (98% VaR < 95% VaR). Example: Daily VaR at 98% confidence = "potential loss expected to exceed X only ~2 days per 100 business days."

## Methodology: Three Approaches

[RAW-BOOK:5] **(1) Variance/Covariance**: Assumes price returns ~ Normal(μ, σ). Compute portfolio mean return and volatility; apply Normal quantile at desired confidence (e.g., 2.33σ for 99% confidence). Fastest method. Limitation: assumes normality; real distributions have fatter tails. **(2) Monte Carlo Simulation**: Randomly sample from assumed return distribution (e.g., lognormal) to generate many portfolio price paths; compute loss distribution; extract confidence quantile. Flexible—handles path-dependent payoffs, complex correlations, non-linear sensitivities. Limitation: computationally intensive; convergence requires many simulations. **(3) Historical Simulation**: Rank actual historical daily returns; use empirical distribution. Replays past scenarios. Advantage: no distributional assumption (distribution-free). Limitation: requires long history; only as rich as past observed moves; may miss unprecedented shocks.

## Key Limitations

[RAW-BOOK:5] VaR is estimate, not guarantee; confidence level represents average frequency, not upper bound. If 98% 1-day VaR is $1M, losses exceeding $1M expected ~2 times per 100 days, but can happen more frequently during stress. **Holding period assumption**: 1-day VaR assumes position can be unwound/hedged in 24 hours; 10-day assumes 10 business days. Longer holding periods → higher VaR (more time for adverse moves). **Distribution fit**: Variance/Covariance underestimates tail risk if tails are fatter than normal (empirically true). Historical Simulation misses tail events not in historical window.

## Related
- [[Option_Greeks_Risk_Management]] — Instantaneous delta/gamma risk vs forward-looking VaR
- [[DV01_Risk_Management]] — Duration-based instantaneous risk measures
- [[Convexity_Mechanics]] — Non-linear price-yield relationship underlying VaR estimation
- [[VaR_Shock_Feedback_Loop]] — Systemic risk implications of VaR-based risk controls
