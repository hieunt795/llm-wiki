---
title: Swap Spread Dynamics
aliases: [Swap spread, IRS spread, Spread trading, Negative spreads]
type: mechanism
tags: [derivatives, swaps, relative-value, credit]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Swap spreads (IRS rate minus sovereign yield) represent the credit/liquidity premium of the banking sector relative to government. They fluctuate based on credit conditions, curve shape, rate expectations, and supply/demand of government bonds. Trading swaps spreads isolates exposure to these factors.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 3142-3247
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Swap spread = (IRS swap rate) - (government benchmark yield), expressed in basis points. Represents credit/liquidity premium of LIBOR panel banks relative to sovereign government. Spread exists because swaps are contingent on 3m LIBOR (bank credit risk), while sovereigns carry sovereign risk. Factors affecting spreads: (1) relative credit strength (govs vs banks); (2) gov bond supply; (3) banking sector creditworthiness (flight-to-quality episodes); (4) curve shape (steep → receive fixed less attractive → spreads narrow); (5) absolute rate level (rising rates → borrowers pay fixed → spreads widen). Negative spreads empirically occur (e.g., May 2009) when market perceives banking system healthier over 3m horizons than government over bond maturity (but caution: swap default risk is only 3m forward, sovereign risk is life-of-bond).

## Key Drivers of Spread Changes

[RAW-BOOK:5] **(1) Government Bond Supply/Demand**: Increase in gov bond issuance → yields rise → if swap rates unchanged, spreads fall (tighter). Gov debt buybacks → yields fall → spreads widen (looser). **(2) Banking Sector Credit Perceptions**: Concerns over bank creditworthiness → flight-to-quality (buy govs, avoid LIBOR exposure) → gov yields down, LIBOR/swap rates up (via increased demand for fixed payers) → spreads widen. Confidence in banks → more LIBOR issuance → spreads narrow. **(3) Swaps Curve Shape**: Steep curve → receiving longer fixed attractive (high expected rolldown) → demand to receive long fixed → supply-demand imbalance → long swap rates fall relative to short, spread narrows. Flat/inverted curve → floating borrowers prefer to pay fixed and receive LIBOR → swap rates rise, spreads widen. **(4) Absolute Rate Direction**: Rising rate environment → borrowers hedge via pay-fixed swaps → swap rates increase → spreads widen. Falling rates → spreads narrow. **(5) Relative Credit Strength**: Government budget deficits + private sector deleveraging → banks look stronger relative to govs → spreads narrow. Government surplus + private borrowing → spreads widen.

## Trading Swap Spreads: Constructing Relative Value Trades

[RAW-BOOK:5] Trader expects swap spreads to tighten (narrow). Constructs: (1) Buy government bond (go long sovereign yield), (2) Sell interest rate swap (go long the spread = short LIBOR risk). If spreads narrow, both legs profit—bond price appreciates + spread compresses. Reverse for expecting spreads to widen. Risk: spread might move against expectation despite correct directional rate view. Hedging: use DV01 matching between bond and swap to isolate spread risk from parallel yield curve moves.

## Negative Swap Spreads

[RAW-BOOK:5] Negative spreads occur when swap rates < sovereign yields. Market interpretation: banking system perceived as better credit than government over the 3-month LIBOR reset horizon, even though government credit is evaluated over longer maturity. Example: -30y swap spread in 2009 meant 3m banking risk < 30y sovereign risk—possible but reflects asymmetric temporal risk comparison (3m forward vs life-of-bond). Caution: negative spreads may also reflect supply/demand dislocations (e.g., regulatory constraints forcing banks to hold govs, reducing LIBOR demand).

## Related
- [[Basis_Swap_Spreads_Valuation]] — Tenor basis (3m vs 6m LIBOR spreads)
- [[Asset_Swap_Spread_ASW]] — Bond + pay-fixed IRS = FRN equivalent; ASW spread differs from swap spread
- [[Interest_Rate_Swap_IRS]] — Foundational swap mechanics
- [[Spot_Swap_Relationship]] — Swap valuation via bond decomposition (PV fixed legs = PV floating legs)
