---
title: Forward Risk & Basis Risk
aliases: [Forward position risk, Basis risk, Carry risk, Repo risk, Credit curve risk]
type: mechanism
tags: [derivatives, fixed-income, credit-risk, risk-management]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Forward price = spot + net carry. Forward risk arises from spot price changes and/or net carry changes. For bonds, net carry = repo cost - coupon. Long forward loses if curve steepens (short rates fall relative to long). For credit, forward CDS risk driven by credit curve shape.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 2124-2144
    section: "Chapter 3.4: Forward Risk (Fixed income 3.4.1, Credit 3.4.2)"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Forward price formula: Forward = Spot + net carry. Risk sources: (1) Spot price changes, (2) Net carry changes. **Fixed income:** Net carry = repo borrowing cost - fixed coupon income. Repo rate decrease → forward price down → long position loss. Long forward position exposed to curve shape (short end = repo, long end = bond price). Long forward loses if curve steepens. **Credit:** Forward-starting CDS replicated as long-dated protection - short-dated protection. Forward protection risk depends on credit curve shape. Buying forward protection loses if credit curve flattens.

## Related
- [[Spot_Forward_Relationship]]
- [[Repurchase_Agreement_Mechanism]]
- [[Bond_Spot_Pricing_DCF]]
- [[Credit_Default_Swaps_CDS]]
- [[Credit_Instrument_Market_Risk_PV01_DV01]]
- [[Convexity_Adjustment_Futures_Vs_Forward]]
