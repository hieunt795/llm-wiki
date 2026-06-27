---
title: Sovereign ASW Valuation Framework
aliases: [Sovereign bond ASW analysis, Cheap-rich sovereign analysis, Z-score bond valuation, Government curve vs swap curve benchmarks, Carry and roll-down decomposition]
type: mechanism
tags: [fixed-income, sovereigns, relative-value, asset-swaps, valuation]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Sovereign bond relative value expressed via asset swap spreads to LIBOR, isolating credit from interest rate risk. Three benchmarks available (government/swap/EONIA curves); cheap-rich identification uses Z-scores vs 3M average, supplemented by carry/roll-down decomposition and market segmentation factors.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 4258-4302
    section: "Chapter 5.4.1: Determining the appropriate benchmark"
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 4297-4325
    section: "Chapter 5.4.2: Term structure of asset swap spreads"
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 4325-4405
    section: "Chapter 5.4.3: Assessing value in sovereign bonds"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **Three Popular Benchmarks:**
1. **Government yield curve** - intuitive but subjective (which bonds form the curve?)
2. **Swap curve** - objective and observable, increasingly standard
3. **EONIA (Euro Overnight Index Average) curves** - post-2010 crisis alternative when LIBOR funding became difficult; reflects true cost of interbank borrowing

Post-2010 financial crisis: EONIA adoption increased as LIBOR-based financing became unreliable. Banks unable to borrow at LIBOR for longer maturities; swap rates fell below government bond rates → many analysts use EONIA as 'cheap-rich' benchmark.

**Term Structure Analysis:** Plot par/par ASW spreads for entire bond population against maturity. Fit curve through observations. Bonds above fitted curve = trading cheap; below = trading rich. AAA-rated sovereign issuers show different credit perception: 2003-2008 spreads converged (ignored individual risks), 2008-2009 crisis spreads diverged by ~150 bps as market reassessed default risk.

**Cheap-Rich Identification Methodology:**

1. **Z-Score Analysis:** Measures deviation from 3-month average spread.
   - Z = (current spread - 3M average) / (1 standard deviation)
   - Negative = trading rich to 3M average (even if cheap to fitted curve)
   - Positive = trading cheap to 3M average
   - Implies mean reversion belief: spread will revert to historical average

2. **Spread Comparison:** Assess bond's spread relative to peers of similar maturity.

3. **Market Segmentation Factors:**
   - Shorter-dated EUR sovereigns expensive: collateral preference for Central Bank operations
   - Money market funds hold short-dated bonds: regulatory/liquidity constraints
   - Illiquidity or 'on special' repo status increases valuation
   - Deliverable bonds (futures) richened due to hedging demand

4. **Carry & Roll-Down Decomposition:** For 3-month horizon:
   - **Carry** (column 13): Coupon income
   - **Roll-Down** (column 14-15): P&L from bond rolling down curve due to curve steepness
   - Steep curves (2009 case): favorable roll-down as longer bonds roll to shorter maturities
   - Analyst could select asset with most favorable carry + roll-down combination

**Execution Strategies:**

- **If bond trading rich:** Non-leveraged accounts execute curve trades (sell rich, buy cheap peer). Leveraged accounts reverse-asset-swap (sell bond short, receive fixed on swap, unwind when spread reverts).
- **If bond trading cheap:** Non-leveraged focus on cash market trades; leveraged accounts use derivatives.

## Related
- [[Asset_Swap_Spread_ASW]]
- [[Asset_Swap_Structure]]
- [[Relative_Value_Applied_To_Sovereigns]]
- [[Relative_Value_Framework]]
- [[Relative_Value_Triangle]]
- [[Forward_ASW_And_Inflation_Swaps]]
