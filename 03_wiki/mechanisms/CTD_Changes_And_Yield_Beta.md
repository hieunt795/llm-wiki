---
title: CTD Changes & Yield Beta
aliases: [Cheapest to deliver switching, CTD dynamics, Yield beta, CTD option value, Conversion factor effects]
type: mechanism
tags: [fixed-income, futures, derivatives, relative-value]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: CTD selection depends on yield levels and curve shape. Rule of thumb: yields below notional → shortest maturity/lowest DV01 is CTD; yields above notional → highest DV01 is CTD. Conversion factor formula creates optionality. Yield beta measures relative yield movements between deliverable bonds.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 2813-2889
    section: "Chapter 4.1.3-4.1.4: Changes in CTD, Yield beta"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **CTD Selection:** Conversion factor formula creates unequal delivery economics depending on yield curve. Rule of thumb: (1) yields < notional coupon → CTD = shortest maturity + lowest DV01 (minimal price appreciation); (2) yields = notional → both bonds equally cheap (maximum optionality); (3) yields > notional → CTD = highest DV01 (larger price depreciation). **CTD Switching:** Plona formula calculates yield change needed for another bond to become CTD: ΔYield = [(FDP_N / CF_N) - (FDP_CTD / CF_CTD)] / (DV01_N - DV01_CTD). Example: 3.50% July 2019 becomes CTD if yields rise 1.51%.

**Futures Price Properties:** Futures tracks whichever bond is CTD (lowest converted forward price). Displays negative convexity (delivery option worth more at-the-money). Short seller holds optionality (right to choose delivery bond), so futures prices slightly below fair value to reflect this option value.

**CTD Change Drivers:** (1) Absolute yield level, (2) Yield curve slope (if bond cheapens relative to basket), (3) New bonds/notes added to deliverable basket.

**Yield Curve Movement Effects:** Bull steepening (short rates fall more) → delays CTD switch. Bear flattening (short rates rise more) → accelerates CTD switch from longer to shorter-dated bonds.

**Yield Beta:** Measures relative yield movement: amount bond's yield changes for 1 bp change in reference bond. Can modify DV01-based CTD forecasts using yield beta to account for non-parallel curve moves.

## Related
- [[Bond_Futures_Pricing_CTD]]
- [[Bond_Futures_Contract_Design]]
- [[Basis_Trading_Mechanics_And_Options]]
