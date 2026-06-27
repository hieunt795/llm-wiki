---
title: Forward Yield Curves
aliases: [Forward rates, Forward curve, Forward-starting rates]
type: definition
tags: [fixed-income, yield-curves, derivatives, mechanics]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Forward rate = interest rate for future period, determined today (no arbitrage basis). Derived from zero-coupon rates via hedging formula: forward rate breakeven neutralizes excess profit/loss from borrowing short vs. lending long. Often misunderstood as forecast (it is not—it's objective calculation, not expectation).
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 959-1091
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Forward rate = rate locked in today for future period. Derived from no-arbitrage: if borrowing 6mo @ 5.59% and lending 3mo @ 5.50%, 3-6mo forward rate = breakeven preventing profit. Formula: forward = [(1+rate_long)/(1+rate_short)]^power - 1. Forward ≠ forecast. Empirically, forwards are poor predictors of future spots. Used as breakeven benchmarks for relative value decisions.

## Related
- [[Zero_Coupon_Yield_Curves]]
- [[Par_Yield_Curve]]
- [[Spot_Forward_Relationship]]
