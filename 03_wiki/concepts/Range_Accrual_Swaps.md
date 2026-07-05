---
title: Range Accrual Swaps
aliases: [Range accrual, Corridor swap, Callable range accrual, Contingent coupon]
type: concept
tags: [derivatives, structured-products, exotic-swaps, fixed-income]
status: draft
confidence: 3
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Range accrual swaps are structured products that pay coupons contingent on an underlying index staying within predefined bounds. Coupons accrue only when conditions are met, introducing exposure to volatility and tail risk while potentially reducing borrowing costs for issuers.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 5590-5650
    section: "Chapter 6.7: Structured Products - Range Accruals"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] A callable range accrual swap (also called range/corridor swaps) is a structured product that pays investors a coupon which only accrues if an agreed index meets a predefined condition. Coupons are multiplied by an accrual factor n/N, where n = number of observation days the index remained within the range and N = total observation days. The structure is typically sold either as an OTC swap or packaged as a bond.

**Key Features:**
- **Contingent Coupon:** Only accrues when underlying rate stays within defined band
- **Accrual Factor:** n/N (daily observations) determines what fraction of coupon is paid
- **Issuer Motivation:** Reduces borrowing costs by embedding short volatility position
- **Investor Motivation:** Higher yields in exchange for accepting contingency risk

**Common Underlying Indices:** LIBOR, swap rates, government bond yields, foreign exchange rates

**Risk Profile:** Investors profit when implied volatility is lower than realized volatility (short vega position). If realized vol spikes above expected, accrual factor drops and expected coupon income reduced.

## Related
- [[Exotic_Swaps_Varieties]]
- [[Volatility_Smile_Skew_Surface]]
- [[CMT_And_CMS_Floaters]]
- [[Interest_Rate_Swap_IRS]]
- [[Credit_Default_Swaps_CDS]]
- [[Credit_Default_Swaps_Schofield]]
- [[Forward_ASW_And_Inflation_Swaps]]
- [[Asset_Swap_Structure]]
- [[Barrier_Options]]
- [[Binary_Options_Digital]]
- [[Bond_Futures_Contract_Design]]
- [[Caps_And_Floors]]
- [[Exotic_Options_Schofield]]
- [[Interest_Rate_Options_Schofield]]
