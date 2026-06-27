---
title: Option Directional & Volatility Trading Strategies
aliases: [Option strategy matrix, Bull spreads, Bear spreads, Vertical spreads, Straddles, Option Greeks trading]
type: mechanism
tags: [derivatives, options, volatility, trading-strategies]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Option strategies organized by two dimensions: directional view (rising/neutral/falling) and volatility view (rising/neutral/falling). Vertical spreads (bull/bear calls/puts) limit both profit and loss. Volatility strategies (straddles) profit from realized volatility changes. Greeks help evaluate strategy payoff profile and risk sensitivities.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 3267-3419
    section: "Chapter 4.4.1: Expressing views on market direction and volatility"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **Trading Matrix Framework:** Strategies mapped to (direction view) × (volatility view) grid. **Building Blocks:** (1) Buy underlying (delta+, vega-neutral), (2) Sell underlying (delta-, vega-neutral), (3) Buy call (delta+, vega+), (4) Buy put (delta-, vega+), (5) Sell call (delta-, vega-), (6) Sell put (delta+, vega-).

**Vertical Spreads (Bull/Bear):** Limited profit/loss structures for directional bets.
- **Bull Spread:** Buy lower-strike, sell higher-strike (calls or puts). Greeks: mildly delta+, vega-neutral, gamma-neutral initially. Lower premium cost than outright.
- **Bear Spread:** Sell lower-strike, buy higher-strike. Greeks: mildly delta-, vega-neutral, gamma-neutral. Credit strategies have better risk/reward than debit but higher max loss at expiry.

**Greeks Evolution:** Vertical spreads near-neutral in gamma/vega initially; deltas converge to zero for large price moves. Time decay (theta) activates near expiry, sign depends on which side dominates.

**Volatility Strategies:** Straddle = buy/sell call + put at same strike/maturity. Quoted as mid-vol bid-offer (e.g., 10.5%-10.7%). Buy straddle profits from vol increase; sell profits from vol decrease. Mixes intrinsic + time value sensitivity.

**Strategy Selection Tradeoffs:** 
- Outright: unlimited P&L, high upfront cost
- Bull/Bear spreads: limited P&L, lower premium, effective for bounded views
- Premium-receiving spreads: worse at-expiry ratio, better cost

## Related
- [[Option_Greeks_Risk_Management]]
- [[Option_Pricing_Models]]
- [[Volatility_Smile_Skew_Surface]]
- [[Forward_Volatility_Trading]]
- [[Hedge_Fund_Strategies]]
