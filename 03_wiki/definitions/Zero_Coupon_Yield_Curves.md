---
title: Zero-Coupon Yield Curves
aliases: [Zero rates, Discount factors, Spot curve, Bootstrapping]
type: definition
tags: [fixed-income, yield-curves, valuation, mechanics]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Zero-coupon rates = returns on structures with single cash flow at maturity (no reinvestment risk). Discount factors derived from zero rates. Zero rates extracted from par curve via bootstrapping: sell off interim coupons at known zero rates, solve for remaining coupon-free cash flow. Proper discount rate for each cash flow maturity.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 902-958
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Zero-coupon rate = rate on 2-cash-flow structure (investment today, return at maturity). No reinvestment risk (what you see is what you get). Discount factor = present value of $1 at maturity. Extracted from par curve via bootstrapping: assume par bond, sell interim coupons at known zero rates, solve for terminal cash flow rate. YTM = average of constituent zero rates. Upward-sloping par curve → zero rates exceed par rates.

## Related
- [[Par_Yield_Curve]]
- [[Forward_Yield_Curves]]
- [[Discount_Factor_Mechanics]]
