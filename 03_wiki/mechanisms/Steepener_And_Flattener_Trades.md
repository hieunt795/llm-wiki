---
title: Steepener and Flattener Trades
aliases:
- Steepener
- Flattener
- Curve Spread Trade
- Long the Curve
- Short the Curve
type: mechanism
tags:
- trading-strategies
- yield-curves
- monetary-policy
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch32.md
thesis: Steepener and flattener trades are two-legged curve strategies designed to
  profit from changes in the slope of the yield curve, utilizing duration-neutral
  weighting to isolate spread dynamics from parallel interest rate shifts.
source_refs:
- file: During_Fixed_Income_Ch32.md
  page: 350
- file: During_Fixed_Income_Ch32.md
  page: 351
- file: During_Fixed_Income_Ch32.md
  page: 352
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 4564-4622
  section: "Chapter 6.1.2: Steepening and Flattening Trade Examples with Carry Analysis"
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 4811-4978
  section: "Chapter 6.3: Trading the Slope of the Yield Curve (Bonds, Futures, Swaps)"
created: '2026-04-13'
updated: '2026-05-07'
---

## Thesis

The slope of the yield curve is the primary indicator of the market's macroeconomic outlook. Alexander Düring explains that traders use 2-leg spread trades to capture changes in this slope. By neutralizing Level risk (Duration), these strategies allow for specific bets on the central bank's reaction function and the term risk premium. [[During_Fixed_Income_Ch32.md#page=350]]

## Mechanism: The Weighting Logic

A spread trade must be hedged against outright yield movements. For two legs with notionals $N_1$ and $N_2$:

### 1. Duration Neutrality
The primary constraint is that the PVBPs of the two legs must offset each other:
$$N_1 PVBP_1 = -N_2 PVBP_2$$
- **The Calculation:** $N_1 = \frac{R}{PVBP_1}$ and $N_2 = -\frac{R}{PVBP_2}$, where $R$ is the desired total risk amount. [[During_Fixed_Income_Ch32.md#page=351]]

### 2. Strategy Directions
- **Steepener (Long the Curve):** Investor profits if long-term yields rise faster (or fall slower) than short-term yields. 
    - **Position:** Long the short-end bond (Leg 1), Short the long-end bond (Leg 2).
- **Flattener (Short the Curve):** Investor profits if the yield spread narrows.
    - **Position:** Short the short-end bond (Leg 1), Long the long-end bond (Leg 2). [[During_Fixed_Income_Ch32.md#page=350]]

## Strategic Implications: Non-Linearity and Targets

### 1. The Japanese Pivot Case
Düring identifies an interesting non-linear behavior in the JGB market.
- **The Target:** Life insurance companies often have fixed yield targets for their liabilities (e.g., 2%).
- **The Impact:** When JGB yields approach these targets, insurance firms buy aggressively, creating a "floor" for yields. A linear spread trade can suddenly exhibit **option-like payoffs** as yields reach these behavioral pivot points. [[During_Fixed_Income_Ch32.md#page=352]]

### 2. Dynamic Rebalancing
Because PVBP changes over time (declining as maturity approaches), a spread trade must be continuously adjusted.
- **The Risk:** The declination is faster for the shorter-maturity leg.
- **The Fix:** Professionals often execute trades using **Forward PVBP** to align the hedge with the expected holding period. [[During_Fixed_Income_Ch32.md#page=352]]

## Evidence / Source Anchors

- Definition of steepener and flattener objectives: [[During_Fixed_Income_Ch32.md#page=350]]
- Mathematical derivation of the duration-neutral weighting (Equations 31.2 and 31.3): [[During_Fixed_Income_Ch32.md#page=351]]
- Analysis of the "Japanese Pivot" and life insurance yield targets: [[During_Fixed_Income_Ch32.md#page=352]]
- Description of the 'Long the curve' and 'Short the curve' mnemonics: [[During_Fixed_Income_Ch32.md#page=352]]
- Note on the necessity of re-balancing due to PVBP decay: [[During_Fixed_Income_Ch32.md#page=351-352]]

## Related

- [[Yield_Curve_Trading_Strategies]] — The taxonomy where spreads are "Order 2".
- [[Bond_Risk_Modified_Duration_And_PVBP]] — The sensitivity measure used for weighting.
- [[PCA_Factor_Interpretation]] — Factor 2 (Slope) is the target of these trades.
- [[Preferred_Habitat_Market_Distortions]] — Why institutional targets (Japan case) create non-linear payoffs.
