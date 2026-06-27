---
title: Inflation-Linked Bond Trading Strategies
aliases: [Linker trading, Breakeven inflation, Real yield curves, RPI swaps, CPI bonds, Inflation curve steepening]
type: mechanism
tags: [fixed-income, inflation, trading-strategies, derivatives, breakeven]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Inflation-linked bond trading combines identifying value in breakeven inflation curves (cheap-rich analysis, forward rate analysis, butterflies) with market risk management (real duration, yield beta) and consideration of liquidity effects and seasonality in CPI.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 6333-6553
    section: "Chapter 8: Inflation-Linked Bond Trading and Valuation Strategies"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

### 8.1: Market Participants

[RAW-BOOK:5] **Inflation Receivers:** Pension funds/insurers with index-linked liabilities, organizations with index-linked wage costs, industries with CPI-linked raw material contracts, inflation hedgers

**Inflation Payers:** Companies with inflation-linked revenues (utilities), retailers, property companies with CPI-linked rents, project finance entities

**Intermediaries:** Investment banks, hedge funds

### 8.2: Term Structure & Liquidity Effects

[RAW-BOOK:5] **Fisher Equation:** Nominal yield = Real yield + Inflation expectations + Risk premium

**Key Insight:** Observed breakeven (Nominal - Real) may diverge from true inflation expectations due to:
- **Inflation risk premium:** Compensation for unexpected inflation
- **Liquidity discount:** Premium demanded for less-liquid inflation-linked bonds

**Practical Example:** 1Y nominal 0.64%, real -2.58% implies 3.22% breakeven; yet inflation swaps quoted 4.40%. Difference reflects liquidity premium (~1.2%) embedded in less-liquid bond spreads vs more-liquid swap spreads.

### 8.3: Seasonality

[RAW-BOOK:5] CPI exhibits predictable seasonal patterns (energy costs peak summer, clothing discounts Nov-Jan). Non-seasonally-adjusted (NSA) indices show systematic monthly variations. Affects trading returns since bonds/swaps typically reference NSA indices.

### 8.4: Identifying Value in Linkers

[RAW-BOOK:5] Three approaches (same as fixed income):
1. **Cheap-Rich Analysis:** Plot breakevens vs fitted curve. Account for seasonality effects.
2. **Forward Rate Analysis:** Zero-coupon breakeven swap rates + real rate swaps. Look for smooth term structure (dislocations = potential mispricing).
3. **Butterfly Trades:** 5-10-10 or other maturity combinations on bonds or swaps (spot or forward).

Also applies **Asset Swap Spreads** for linkers (converts inflation exposure to synthetic floating for relative value).

### 8.5: Trading Strategies

[RAW-BOOK:5] **Real Duration:** Standard duration applied to inflation-linked bonds measuring sensitivity to real yield changes. Typically higher than nominal duration for equivalent maturity.

**Yield Beta:** Expected change in real yield for given change in nominal yield. Beta = Real Duration / Nominal Duration. Enables risk-weighted trades between linker and nominal bonds. Unstable (depends on measurement period, sample selection, frequency).

**Market Risk Decomposition:** 
- Level risk (parallel shifts in real yield curve)
- Slope risk (curve steepening/flattening)
- Carry risk (time-decay benefits)
- Roll-down risk (curve shape migration)

## Related
- [[Inflation_Linked_Bond_Pricing]]
- [[Yield_Curve_Structure_And_Mechanics]]
- [[Forward_Yield_Curves]]
- [[Carry_And_Rolldown_Analysis]]
- [[Interest_Rate_Swap_IRS]]
- [[Forward_ASW_And_Inflation_Swaps]]
- [[Breakeven_Inflation_Metrics]]
