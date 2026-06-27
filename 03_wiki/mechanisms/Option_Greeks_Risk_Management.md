---
title: Option Greeks and Risk Management
aliases: [Greeks, Delta, Gamma, Theta, Vega, Option sensitivities, Option Greeks]
type: mechanism
tags: [derivatives, options, risk-management, quantitative-finance]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: The Greeks decompose option price sensitivity into directional (delta), curvature (gamma), time (theta), and volatility (vega) components. Together they form the toolkit for hedging option portfolios and quantifying how value changes with market conditions. Each Greek measures exposure to a distinct market driver.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 2311-2502
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Greek letters quantify option price sensitivities: (1) **Delta** = slope of premium vs underlying price, ranges [0,1] by moneyness, additive across positions for delta-neutral hedging. (2) **Gamma** = rate of delta change, highest ATM near expiry, determines delta-hedging frequency. (3) **Theta** = time decay per day, negative for buyers (time works against), positive for sellers (earned as "gamma rent"). (4) **Vega** = implied volatility sensitivity; distinct from gamma (realized vol). All Greeks vary with moneyness, time, and implied vol; used to manage multi-dimensional option risk.

## Delta: Directional Exposure

[RAW-BOOK:5] Delta = ∂P/∂S (slope of option premium curve vs underlying). OTM options: delta → 0 (premium insensitive to price). ATM options: delta ≈ 0.5. ITM options: delta → 1 (premium moves almost 1:1 with underlying). Sign convention: long call or short put = +delta (long the underlying); short call or long put = -delta (short the underlying). **Additivity**: delta-neutral position = sum of deltas = 0, hedged against small price moves. **Delta evolution**: changes over time ("delta bleed") and with volatility (higher vol → deltas toward 0.5 for both calls and puts). **Multiple interpretations**: (1) Hedge ratio—how many underlying shares needed to delta-hedge; (2) Directional exposure—whether trader profits on price rise; (3) Probability of exercise—heuristic, not statistical (30-delta ≈ 30% ITM at expiry under geometric Brownian motion).

## Gamma: Curvature and Rehedging

[RAW-BOOK:5] Gamma = ∂Delta/∂S (rate of delta change). Tells how much delta shifts for 1% (or other) underlying move. **Fixed income analogy**: gamma relates to convexity (delta ↔ modified duration, gamma ↔ convexity). **Key property**: gamma requires specifying price move range ("gamma of 0.03 for a 1% move"). Gamma highest when option ATM with little time remaining; lowest for deep ITM/OTM or far-dated options. **Rehedging implication**: high gamma forces frequent delta-hedge adjustments. If trader delta-hedged and underlying moves, delta changes → position becomes unhedged → forced to buy/sell underlying to rehedge, generating transaction costs. Conversely, option seller earns "gamma rent" (theta proceeds) to compensate for rehedging losses.

## Theta: Time Decay

[RAW-BOOK:5] Theta measures premium change per day due to passage of time alone. Decomposes option premium into intrinsic value (moneyness) + time value (decay). **Non-linear decay**: time value amortizes slowly initially, then accelerates as option nears expiry. **Sign by position**: Long call/put → theta < 0 (time works against buyer). Short call/put → theta > 0 (time accrues to seller). **By moneyness**: ITM options decay slowly (most value intrinsic, changes little with time). ATM options lose most value absolutely. OTM options lose most value as percentage. **Theta-gamma tradeoff**: option sellers collect theta but face gamma losses on large underlying moves. Profitability depends on actual volatility realized (gamma P&L) vs theta collected: if realized vol < implied vol, seller profits; if realized vol > implied vol, seller loses.

## Vega: Implied Volatility Sensitivity

[RAW-BOOK:5] Vega = ∂P/∂σ_implied (premium sensitivity to changes in implied volatility, distinct from gamma which is realized vol exposure). **Volatility taxonomy**: (1) Historical volatility—past realized returns. (2) Implied volatility—market's perceived future vol (backed out of option prices, sometimes called "vol surface" when varying by strike/maturity). (3) Forward volatility—vol implied for future period (e.g., 6-month vol in 3 months). (4) Normalized volatility—yield × vol% (fixed income convention; accounts for rate level dependence). **Trading logic**: If trader expects future realized vol < implied vol → sell options (overpriced). If realized vol > implied vol → buy options (underpriced). Vega typically positive for both calls and puts (higher implied vol increases both premiums). Highest ATM, declines far OTM/ITM.

## Greeks Interdependencies

[RAW-BOOK:5] Greeks change dynamically as underlying price moves and time passes. Delta evolves via gamma (gamma × price move ≈ delta change). Theta accrues daily; vega fluctuates with market vol expectations. Gamma-theta tradeoff: short gamma (seller) collects theta but absorbs gamma P&L on price moves. Long gamma (buyer) pays theta but profits from large moves (option becomes more valuable if underlying moves far from strike). High vol environment → high vega exposure, high gamma costs. Low vol environment → low vega, lower rehedging costs, easier to collect theta.

## Related
- [[Option_Pricing_Models]] — BSM model produces Greeks
- [[Convexity_Mechanics]] — Fixed income analogue (duration=delta, convexity=gamma)
- [[DV01_Risk_Management]] — Duration-based hedging parallel
- [[Volatility_Smile_And_Skew]] — Why implied vol varies by strike
