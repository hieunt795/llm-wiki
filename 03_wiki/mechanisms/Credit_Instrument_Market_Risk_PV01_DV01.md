---
title: Credit Instrument Market Risk (PV01 & DV01)
aliases: [Risky PV01, Credit DV01, Credit duration, CDS delta, Hazard rate, Survival probability]
type: mechanism
tags: [credit-risk, derivatives, fixed-income, risk-management]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Credit risk measurement for CDS requires two risk metrics. Risky PV01 (credit duration) = change in CDS value per 1 bp spread move. Credit DV01 (delta) = change for 1 bp parallel shift in credit curve. Both incorporate survival probability and hazard rate (default probability per period) using zero-coupon swap discounting.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 2045-2123
    section: "Chapter 3.3.6: Market risk of credit instruments"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Two CDS risk metrics for fixed-coupon structures: (1) **Risky PV01** (credit duration) = 1 bp spread impact, (2) **Credit DV01** (delta) = 1 bp parallel curve shift impact. Requires:
- Discount using zero-coupon swap rates (market convention)
- Survival probability = prob of no default to period t
- Hazard rate = prob of default between periods
- Formula: PV01 = Σ[(1 bp) × DF × survival prob] where DF = discount factor
- For on-market CDS (spread = coupon), risky PV01 ≈ credit DV01
- Application: upfront cash adjustment = (spread - coupon) × PV01, mark-to-market = (spread change) × notional × PV01

## Worked Example

5-year CDS, 50 bps spread, 40% recovery → implied 1-year default prob = 50bp/(100%-40%) = 0.8333%. Extends to hazard rates across curve. Risky PV01 calculation in table: undiscounted 1 bp × 5 years = 5 bp → discount for rates (flat 5% swap curve) → discount for survival probs (1% hazard rate) → PV01 ≈ 4.21 bp per 100 notional.

## Related
- [[Credit_Default_Swaps_CDS]]
- [[Credit_Default_Swaps_Schofield]]
- [[Credit_Spread_Pricing]]
- [[Macaulay_Duration]] — Risk-free duration parallel
- [[Forward_Risk_Basis_Risk]]
- [[Counterparty_Credit_Risk]]
