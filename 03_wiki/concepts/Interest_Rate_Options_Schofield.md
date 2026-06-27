---
title: Interest Rate Options
aliases: [Caps, Floors, Swaptions, Caplets, Floorlets]
type: concept
tags: [derivatives, interest-rate-risk, fixed-income, options]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Interest rate options (caps, floors, swaptions) are strips of OTC calls/puts on forward rates or swap entries. Caps protect borrowers against LIBOR rises; swaptions give optionality on swap entry with non-linear payoff profile.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 730-766
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Cap structures = strip of call options on forward rates (protects against LIBOR rises). Floor structures = strip of put options (protects against LIBOR falls). Swaptions = options on swap entry (payer = pay fixed if rates rise; receiver = receive fixed if rates fall). Cash settlement on swaptions quoted as option maturity × swap tenor (e.g., 1y × 5y).

## Related
- [[Vanilla_Options_Schofield]]
- [[Interest_Rate_Swap_IRS]]
- [[Caps_And_Floors]]
