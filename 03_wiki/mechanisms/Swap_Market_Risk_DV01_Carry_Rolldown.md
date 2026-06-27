---
title: Swap Market Risk (DV01, Carry, Roll-Down, Forward-Starting)
aliases: [Swap DV01, Swap convexity, Carry and roll-down, Forward-starting swaps, Interest rate swap risk]
type: mechanism
tags: [derivatives, interest-rate-swaps, risk-management, valuation]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Swap market risk decomposes into fixed-rate bond risk minus FRN risk. DV01 (delta) and convexity (gamma) measure parallel shift sensitivity. Roll-down and carry decompose total P&L. Forward-starting swaps decouple LIBOR setting risk from rate forecasting risk.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 2146-2290
    section: "Chapter 3.5: Swap Market Risk (3.5.1 Spot, 3.5.2 Carry/Rolldown, 3.5.3 DV01 Application, 3.5.4 Forward-Starting)"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **Spot Swap Risk (3.5.1):** Swap = long fixed bond + short FRN. DV01 = value change per 1 bp parallel shift (worked example: 5-year swap DV01 ≈ 3,177 on USD 10m notional). Convexity positive for receive-fixed (buy bond analog). Non-parallel curve moves: only matching-maturity shifts affect NPV. 

**Carry & Roll-Down (3.5.2):** Roll-down = value gain as swap approaches maturity (no curve assumption). Steeper curve → larger roll-down. Carry = fixed leg income - LIBOR cost. Example: receive 6.92% 5-year → 1 year later valued at 6.90% (4-year), profit from roll-down despite no market move.

**DV01 Application (3.5.3):** Duration-neutral spread trades use DV01 ratio hedge. Example: pay fixed 5-year (DV01=3,177), receive fixed 2-year (DV01=2,764) on notional ratio 3,177/2,764=1.1494 to immunize parallel shifts. Steepening profits if 5Y-2Y spread widens. Carry calculation determines break-even LIBOR.

**Forward-Starting Swaps (3.5.4):** Forward-starting DV01 ≠ spot DV01 because unfixed LIBOR has no rate risk. Example: 3-year spot DV01 = 2.727 vs 3-year forward (1y forward) DV01 = 2.596. First LIBOR fixing reduces remaining DV01. Uses: pinpoint favorable forward dates, cleaner roll mechanics, avoid LIBOR-caused position drift, maintain "round" residual maturities.

## Related
- [[Interest_Rate_Swap_IRS]]
- [[Macaulay_Duration]]
- [[DV01_Risk_Management]]
- [[Forward_Yield_Curves]]
- [[Forward_Swap_Relative_Value]]
- [[Credit_Instrument_Market_Risk_PV01_DV01]]
