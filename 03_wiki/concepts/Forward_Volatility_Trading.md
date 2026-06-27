---
title: Forward Volatility Trading
aliases:
- Forward Vol
- Forward Implied Volatility
- Forward Vol Trade
type: concept
tags:
- derivatives
- swaptions
- volatility
- pricing
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Howard Corb"
provenance: Howard_Corb_Swaps.md
thesis: A Forward Volatility Trade is a derivative contract that isolates pure implied
  volatility exposure by agreeing to buy or sell a swaption straddle at a future date,
  with the strike set at-the-money forward only at the time of settlement.
source_refs:
- file: Howard_Corb_Swaps.md
  page: 416
- file: Howard_Corb_Swaps.md
  page: 419
- file: Howard_Corb_Swaps.md
  page: 421
- file: Howard_Corb_Swaps.md
  page: 425
created: '2026-04-20'
updated: '2026-04-22'
---

## Thesis

Traditional volatility instruments (like swaption straddles) suffer from "leakage": as rates move, the straddle gains delta and gamma, and as time passes, its maturity profile changes (e.g., 5 into 10 becomes 4 into 10). **Forward Volatility Trading** solves this by fixing the forward price and duration today, but delaying the strike-setting until the settlement date. [[Howard_Corb_Swaps.md#page=416]]

## Structural Mechanism

A forward vol trade is a forward contract on the value of an at-the-money (ATM) straddle.

- **Transaction:** The investor agrees to buy/sell a straddle (e.g., 5-year expiry into 10-year swap) starting in 2 years.
- **Strike Setting:** Unlike a standard forward swaption, the strike is NOT set today. It is set at the **then-prevailing ATM forward rate** on the settlement date (2 years from today).
- **Settlement:** The payout is the difference between the forward price (agreed today) and the actual market price of the ATM straddle at settlement. [[Howard_Corb_Swaps.md#page=419]]

## Heuristic Pricing & Replication

Howard Corb explains that while pricing is model-dependent, it can be heuristically understood via replication:

### 1. Simple Replication
To recreate a "5 into 10 swaption straddle, 2 years forward":
- **Buy:** 7 into 10 ATM straddle today.
- **Sell:** 2 into 10 ATM straddle today.
- **Problem:** The underlying forward rate for a 7 into 10 is different from a 2 into 10, creating a mismatch in the "gray box" duration. [[Howard_Corb_Swaps.md#page=422]]

### 2. Refined Replication (Correlation Bias)
- **Sell:** 2 into 5x15 swaption straddle (a swaption on a forward starting swap).
- **Result:** This matches the forward rate exposure but introduces **Correlation Risk**. The volatility of a forward starting swap depends on the correlation between the constituent spot starting swaps. [[Howard_Corb_Swaps.md#page=423]]

## Key Implementation Risks

- **Rate Bias:** Under the Normal Model, straddle prices are linear in volatility ($\sigma_N$) but also depend on the **Annuity ($A$)**. As rates fall, $A$ increases, potentially raising the straddle price even if volatility is flat.
- **Normal Vol Parameterization:** To achieve "pure" vol exposure, some traders specify a payout in dollars per basis point of normal volatility ($NIV$), stripping out the annuity effect. [[Howard_Corb_Swaps.md#page=425]]
- **Forward vs. Spot Vol:** The forward price depends on the shape of the vol grid. If long-term vol is lower than short-term vol, forward vol will trade at a discount to the current spot price. [[Howard_Corb_Swaps.md#page=424]]

## Related

- [[Swaptions]] — The basic building block.
- [[Bermudan_Swaptions]] — Valuation is implicitly a sequence of forward vol expectations.
- [[Interest_Rate_Option_Models]] — Specifically the Normal (Bachelier) model.
- [[Principal_Component_Analysis_PCA]] — Used to decompose the correlation risks in forward starting swaps.
