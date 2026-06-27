---
title: Spot-Forward Relationship
aliases: [Cash and carry, Net carry, Forward pricing, Basis]
type: relationship
tags: [fixed-income, derivatives, pricing-relationships]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Forward bond price = spot clean price + net carry. Net carry = borrowing cost - coupon income earned during holding period. Positive carry (coupon > repo rate) lowers forward price. Forward-spot basis narrows to zero by delivery date.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 1257-1331
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Forward bond price = spot price + net carry (financing cost - coupon income). Cash and carry strategy: buy bond, finance via repo, hold to forward date. Positive carry: coupon > repo rate → forward price < spot (income offsets). Negative carry: coupon < repo rate → forward price > spot. Forward/spot basis → 0 by delivery. Forward CDS spread similarly derived: synthetic forward = buy long + sell short protection.

## Worked Example: Bund Forward Pricing

[RAW-BOOK:5] EUR 10m Bund, spot clean price 100.92, coupon 4.00%, YTM 3.88%, 20-day holding period, repo rate 4.25%. Dirty price = clean + accrued ≈ 101.19. Repo financing cost over 20 days: (4.25% × 20 / 360) × 101.19 ≈ 0.024. Coupon income during 20 days ≈ 0.022 (accrued coupon). Net carry = financing cost − coupon income ≈ +0.002 (negative carry). Forward clean price ≈ spot + net carry adjustment ≈ 100.94. Positive carry (coupon income > repo cost) → forward price *below* spot (income reduces capital requirement). Negative carry (repo cost > coupon income) → forward price *above* spot (financing cost accumulates). Forward price always converges to spot at maturity (no net carry left). Basis = forward − spot in basis points; strictly decreases by accrued coupon minus financing costs over holding period.

## Forward CDS Spreads

[RAW-BOOK:5] Forward CDS spread created by synthetic hedging: buying protection for 5Y + selling protection for 10Y creates economic position equivalent to buying 5Y forward protection for 5Y maturity (i.e., 5-year forward starting in 5 years). Formula: breakeven forward spread = (long-dated spread × long maturity − short-dated spread × short maturity) / (long maturity − short maturity). Worked example: 5Y CDS premium 24 bps p.a. (120 bps total), 10Y CDS premium 45 bps p.a. (450 bps total). Protection buyer considering 10Y horizon can either pay 450 bps upfront, or pay 120 bps for 5 years then roll forward. Breakeven forward rate for years 5–10: (450 − 120) / 5 = 66 bps. If trader expects 5Y CDS spread in 5 years to be *less* than 66 bps, buy 5Y protection and roll at maturity (saves cost vs. buying 10Y now). Principle: forward spread = no-arbitrage breakeven preventing advantage from term structure positioning.

## Related
- [[Forward_Yield_Curves]]
- [[Spot_Swap_Relationship]]
- [[Repo_Mechanics]]
- [[Credit_Default_Swaps_Schofield]]
- [[Credit_Spread_Pricing]]
