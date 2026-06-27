---
title: Inflation-Linked Bond Pricing
aliases: [Index-linked bonds, Linkers, Real yield, Canadian model, Index ratio]
type: mechanism
tags: [fixed-income, inflation, valuation, mechanics]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Linker pricing (Canadian model): real coupon and principal uplifted by index ratio (CPI_settlement / CPI_issue). Discounted at real yield (not nominal). Bond insensitive to inflation changes (what matters = real yields). Deflation floor on principal (except UK/Canada/Japan).
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 1178-1240
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 6333-6553
    section: "Chapter 8: Inflation-linked bonds and trading"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Linker = real coupons + principal uplifted by CPI index ratio. Index ratio = CPI(settlement) / CPI(issue), with 3-month lag and interpolation. Priced using real discount rate, not nominal. Change in inflation has zero effect on linker value (CPI uplift offsets); sensitive only to real yield changes. Most countries have deflation floor (principal won't fall below 100) except UK/Canada/Japan.

## Related
- [[Bond_Spot_Pricing_DCF]]
- [[Inflation_Risk_Premium]]
- [[Real_Yield]]
