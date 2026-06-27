---
title: Forward ASW and Inflation-Linked Asset Swaps
aliases: [Forward asset swap spread, Forward-starting asset swap, Inflation asset swap, Real yield synthesis, Forward financing spreads]
type: mechanism
tags: [fixed-income, asset-swaps, derivatives, inflation, repo]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Forward ASW = today's ASW spread for a given maturity starting at future date; accounts for repo financing costs that spot ASW ignores. Forward spreads equal when market has arbitraged away financing advantage. Inflation asset swaps apply same par/proceeds structures to inflation-linked bonds, creating synthetic nominal floating exposure.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 4406-4458
    section: "Chapter 5.4.4: Forward asset swap spreads"
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 4459-4490
    section: "Chapter 5.4.5: Inflation-linked asset swaps"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **Forward ASW Spread Definition:** Spread to LIBOR for an asset swap with a specific maturity starting at a future date. Example: spot ASW for 10-year = 10 bp; forward 10-year ASW starting 3 months out = 12 bp. Investor executing spot transaction with 3-month horizon loses money when ASW moves beyond forward spread (12 bp).

**Motivation:** Different bonds finance at different repo rates. Two bonds with same spot ASW spread but different repo rates have different true financing costs. Larger ASW spread ≠ better investment if bond trades 'on special' in repo (financing cheaper but market has already priced this advantage).

**Forward ASW Formula (Tonge 2001):**
- Accounts for: spot ASW, bond price, repo rate, time to forward date
- Forward ASW = break-even spread accounting for interim cash flows and financing costs

**Arbitrage Mechanics:**
Two zero-coupon bonds (price=10, same maturity, same credit) with equal spot ASW but different repo rates:
- Bond A: repo 0%
- Bond B: repo 1%

Strategy: Buy A (repo out at 0%), sell B (repo in at 1%), receive fixed on swaps → 1% annualized gain with no duration mismatch. Market arbitrages this until **forward ASW spreads equalize**. Forward spreads therefore serve as objective, repo-adjusted valuation framework.

**Forward as Breakeven:** Forward ASW = threshold level where position begins to lose money. Higher forward ASW = more protection; bond can widen by larger spread before losses occur.

**Calculation Depth:** How far forward? As far as repo market supports active trades. If bond only 'special' for 1 month but not 3 months, forward ASW won't show cheapness on 3-month basis.

---

## Inflation-Linked Asset Swaps

[RAW-BOOK:5] **Structure:** Similar to nominal ASW but inflation-linked bond + inflation swap = synthetic nominal floating-rate note (investor inflation-neutral).

**Two Variants:**
1. **Par/Par** (European standard): Investor buys inflation-linked bond at par regardless of market price; enters inflation swap with fixed real yield + inflation adjustment; receives LIBOR ± spread; at maturity pays full inflation-uplifted redemption, receives par back.

2. **Proceeds/Market Value** (UK/US standard): Swap cash flows and timing mirror actual bond cash flows; no par adjustment structure.

**Pricing Challenge:** Must estimate future inflation values (from zero-coupon inflation swaps) to set fixed swap cash flows.

**Case Study — 2008 Crisis Divergence:**
French nominal 5.75% 2032 vs inflation-linked 3.15% 2032:
- December 2007: ASW spreads nearly equal
- Q3 2008: spreads diverged → peak 72 bps in October 2008

**Drivers of Divergence:**
- Investors sold inflation-linked holdings, switched to nominal bonds (perceived greater liquidity)
- Banks unwound inflation-swap hedges for balance sheet management
- Mark-to-market losses on existing inflation ASWs triggered unwinding cascade
- Depressed inflation-linked bond prices → higher nominal ASW spreads compared to nominal bonds

**Lesson:** Inflation and nominal ASW spreads can diverge significantly during crises due to liquidity and hedging flows, not fundamental credit differences.

## Related
- [[Asset_Swap_Spread_ASW]]
- [[Asset_Swap_Structure]]
- [[Sovereign_ASW_Valuation_Framework]]
- [[Inflation_Linked_Bond_Pricing]]
- [[Interest_Rate_Swap_IRS]]
- [[Spot_Swap_Relationship]]
