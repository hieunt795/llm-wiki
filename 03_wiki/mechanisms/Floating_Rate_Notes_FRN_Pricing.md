---
title: Floating-Rate Notes (FRN) Pricing
aliases: [FRN discount margin, FRN valuation, Quoted margin, Discount margin]
type: mechanism
tags: [fixed-income, valuation, floating-rate]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: FRN pricing uses discount margin (yield to maturity of the note). Assumes all future LIBOR coupons = par swap rate of same maturity. Discount margin = quoted margin + capital gain spread. FRN insensitive to interest rate changes (both short- and long-term); primarily sensitive to credit spread changes.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 360-369
    section: "Chapter 1.2.2: FRN fundamentals"
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 1128-1177
    section: "Chapter 2.3.5: FRN pricing"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] FRN can't use YTM (future coupons unknown). Priced on discount margin basis: assume future LIBOR = par swap rate, add quoted margin to get numerator. Use swap rate in denominator. Discount margin = quoted margin + capital gain amortized. FRN insensitive to rate moves (floating coupon + fixed spread hedge interest-rate risk). Sensitive to issuer credit (discount margin rises if credit worsens). Asset swap = FRN synthetic.

## Related
- [[Interest_Rate_Swap_IRS]]
- [[Asset_Swap_Structure]]
- [[Credit_Spread_Pricing]]
