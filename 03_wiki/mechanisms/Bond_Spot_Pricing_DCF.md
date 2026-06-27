---
title: Bond Spot Pricing (Discounted Cash Flow)
aliases: [Bond valuation, Fair value, Theoretical price, Clean vs. dirty price]
type: mechanism
tags: [fixed-income, valuation, mechanics]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Bond fair value = sum of discounted cash flows (coupons + principal) using appropriate discount rate (YTM, zero-coupon, or par rates). Dirty price includes accrued interest; quoted clean price excludes accrued. Pricing = cash value, market price = what someone pays.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 827-897
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Bond value = PV of cash flows. Dirty price = sum of discounted coupons + principal. Clean price = dirty price - accrued interest (market quotation basis). Fair value vs. market price: if market < fair value = "cheap"; if market > fair value = "rich". YTM assumes constant reinvestment rate (reinvestment risk). Zero-coupon approach values each cash flow separately using zero-coupon discount factors (removes reinvestment assumption).

## Related
- [[Yield_Curve_Types]]
- [[Zero_Coupon_Yield_Curves]]
- [[Par_Yield_Curve]]
