---
title: Forward-Swap Relative Value Applications
aliases: [Forward swap spread, Forward swap trading, Forward-starting swaps, FRA relationships]
type: mechanism
tags: [derivatives, swaps, relative-value, futures]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Forward-swap relationship applies spot-swap-forward RV triangle concepts to forward-starting swaps. Combine bond futures with forward-starting swaps to trade forward swap spreads using DV01-neutral hedging. Forwards implied from futures prices; compare to forward swap rates to identify relative value.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 3247-3265
    section: "Chapter 4.3: The forward-swap relationship"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **Forward Swap Spread Trade Structure:** (1) Sell bond futures at current price, (2) Receive fixed on forward-starting swap with effective date = futures maturity, final maturity = CTD maturity. **Pricing Logic:** Calculate implied YTM of bond from futures price (forward price of CTD). Compare implied forward yield to forward swap rate → forward swap spread. **Example:** CTD 1.875% Feb 2014, futures Dec 2009 delivery, implied forward YTM 1.872%, forward 5-year swap 2.72% → forward swap spread 84.8 bps. **Execution:** Create DV01-neutral trade to isolate spread exposure from parallel shifts. Unwind when anticipated spread moves.

## Related
- [[Spot_Swap_Relationship]]
- [[Spot_Forward_Relationship]]
- [[Interest_Rate_Swap_IRS]]
- [[Bond_Futures_Pricing_CTD]]
- [[Swap_Market_Risk_DV01_Carry_Rolldown]]
- [[Swap_Spread_Dynamics]]
