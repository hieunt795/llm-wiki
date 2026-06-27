---
title: Option Pricing Models
aliases: [Black-Scholes-Merton, BSM, Binomial option pricing, Monte Carlo option pricing, Put-call parity, Option valuation]
type: mechanism
tags: [derivatives, options, quantitative-finance, pricing]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Option pricing fundamentally rests on replication: if you can hedge an option's payoff using the underlying asset and cash, then option premium = cost of replication. Three main methods link option value to underlying market movements: closed-form Black-Scholes-Merton for European options, binomial trees for discrete evolution, Monte Carlo for high-dimensional paths. Put-call parity enforces no-arbitrage linkage between calls and puts.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 1513-1885
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Option premium = present value of expected payoff under risk-neutral probability distribution. Black-Scholes-Merton (BSM) closed-form: fair value function of five parameters (spot, strike, time, rate, volatility). Core insight: volatility (standard deviation of returns) drives time value; extreme price movements become more likely under higher vol. Binomial model: recursively value option at each node by computing expected payoff discounted at risk-free rate, using replication to establish delta hedge. Monte Carlo: simulate many underlying price paths under risk-neutral dynamics, average payoff across paths, discount back. Put-call parity: C - P = S - K×DF (call premium - put premium = spot - discounted strike), ensures no-arbitrage between calls and puts on same underlying.

## Core Principle: Replication

[RAW-BOOK:5] Option hedging = creating replicating portfolio using underlying and cash that matches option payoff at maturity. If payoff_up = $5 when price rises, payoff_down = $0 when falls, option premium must equal cost of delta-hedging portfolio: buy Δ shares + borrow cash such that portfolio value matches both outcomes. Delta = (payoff_up - payoff_down) / (price_up - price_down). Principle: "If you can hedge it, you can price it" — option value = replication cost, independent of actual probability distribution (depends only on risk-free rate and volatility).

## 2.7.1 Black-Scholes-Merton: Intuitive Approach

[RAW-BOOK:5] Normal distribution framework: option premium depends on forward price (mean), volatility σ (standard deviation), time to maturity T. Key concepts: (1) **Intrinsic value** = max(S - K, 0) for call (immediate exercise value); (2) **Time value** = premium - intrinsic (value from uncertainty over T). Intrinsic value always ≥ 0 (can't lose money by exercising immediately). Time value highest at-the-money (maximum uncertainty of exercise). Worked example: crude oil call, strike $50, spot $50, T=1yr, σ=10%, r=5%. One standard deviation ≈ $3.32, so 68.3% probability price lands in [$46.68, $53.32]. BSM shortcut formula: C ≈ 0.4 × σ × √T × DF × S (0.4 factor approximates normal distribution quantiles). Result: $1.8966 ≈ 3.79% of strike.

## 2.7.2 Binomial Pricing

[RAW-BOOK:5] Assume discrete up/down movements at each period. Start with current price, specify up-factor u and down-factor d (derived from volatility). At each node, compute option payoff. Work backward: option value at prior node = [p × payoff_up + (1-p) × payoff_down] / (1+r), where p = risk-neutral probability = (1+r-d)/(u-d) (NOT actual market probability). Delta = (C_up - C_down)/(S_up - S_down). Recursion continues until present value computed at spot. Advantage: handles American-style early exercise (check at each node if early exercise > continuation value). Many periods approximate lognormal distribution, converging to BSM.

## 2.7.3 Monte Carlo Simulation

[RAW-BOOK:5] Simulate many price paths using log-normal dynamics: ln(S_T) ~ N(ln(S_0) + (r - σ²/2)T, σ²T). For each simulated path, compute option payoff at maturity. Average all payoffs to get expected value. Discount back at risk-free rate to present. Advantage: handles path-dependent payoffs (Asian options, barrier payoffs, multi-dimensional underlying correlation). Limitations: computationally intensive; convergence requires large number of paths; American early exercise challenging (needs regression or optimization).

## 2.7.4 Put-Call Parity

[RAW-BOOK:5] European call and put with same strike K, maturity T, underlying S satisfy: C - P = S - K/(1+r)^T. Intuition: long call + short put = synthetic forward (replicates obligation to buy at K). Forward price = S - PV(K), so call premium - put premium must equal this. Rearranged: C = P + S - K/(1+r)^T. Arbitrage if violated: buy underpriced side, sell overpriced side, lock in risk-free profit via replication. No-arbitrage condition links all option contracts on same underlying.

## Related
- [[Interest_Rate_Options_Schofield]]
- [[Exotic_Options_Schofield]]
- [[Caps_And_Floors]]
- [[Volatility_Smile_And_Skew]]
