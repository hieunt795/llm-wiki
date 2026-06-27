---
title: Volatility Smile, Skew & Surface
aliases: [Volatility smile, Volatility skew, Volatility surface, Implied volatility moneyness, Term structure of volatility]
type: concept
tags: [derivatives, options, volatility, risk-management]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Black-Scholes assumes constant implied volatility across strikes (moneyness) and maturities. Empirically, vol varies by both. Smile = OTM/ITM higher vol than ATM (FX). Skew = asymmetric smile (equity: downside skew). Driven by fat tails in distribution, hedging costs (gamma), and supply/demand imbalances.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 2503-2526
    section: "Chapter 3.6.5: Smiles, skews and surfaces"
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 5496-5509
    section: "Chapter 6.5: Volatility, Curvature and Skew (Curve-Skew Relationship)"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **Volatility Smile:** OTM & ITM options priced higher implied vol than ATM. Classic pattern in FX markets. **Volatility Skew:** Asymmetric smile (lopsided). Equity index skew: OTM puts (ITM calls) higher vol than ATM, OTM calls (ITM puts) lower vol. **Volatility Surface:** Combines moneyness dependence with maturity (term structure) of vol. Practitioners use terms interchangeably.

**Three Explanations for Non-Constant Volatility:**
1. **Fat Tails:** Extreme events more frequent than lognormal distribution predicts → OTM options more valuable
2. **Hedging Costs (De Weert):** After market crash, OTM puts become ATM, gamma exposure rises, delta-hedging losses increase → traders price OTM puts higher initially as cushion
3. **Supply/Demand:** If market expected to rally, traders buy OTM calls (vol ↑) and sell OTM puts (vol ↓) → skew to upside

**Evolution:** Smile/skew becomes more pronounced over time as gamma risk increases for short-dated ATM options.

## Related
- [[Option_Greeks_Risk_Management]]
- [[Option_Pricing_Models]]
- [[Implied_Volatility]]
