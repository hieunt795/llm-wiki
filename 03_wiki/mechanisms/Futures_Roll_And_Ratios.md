---
title: Futures Roll and Ratios
aliases:
- Futures Roll
- Calendar Spread
- Roll Ratio
- PVBP-neutral Roll
- Front vs Back Contract
type: mechanism
tags:
- derivatives
- trading
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch29.md
thesis: The futures roll is the periodic transition of risk exposure from the expiring
  (front) contract to the next (back) contract, governed by a roll ratio that ensures
  PVBP-neutrality by accounting for the differing durations of the respective CTD
  bonds.
source_refs:
- file: During_Fixed_Income_Ch29.md
  page: 321
- file: During_Fixed_Income_Ch29.md
  page: 322
- file: During_Fixed_Income_Ch29.md
  page: 324
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The vast majority of bond futures contracts are never delivered. Instead, investors maintain their exposure through **Rolling**. Alexander Düring explains that a roll is not a simple one-for-one exchange. Because the front and back contracts often have different [[Cheapest_To_Deliver_CTD_Mechanism|CTD]] bonds with different durations, the trader must solve for a specific **Roll Ratio** to ensure their total interest rate risk remains constant throughout the transition. [[During_Fixed_Income_Ch29.md#page=321]]

## Mechanism: The Calendar Spread

A roll is executed by trading the **Roll Spread** (Calendar Spread):
$$\text{Roll} = \text{Front Price} - \text{Back Price}$$

### 1. Directionality
- **Backwardation (Positive Roll):** In a normal upward-sloping yield curve, the carry is positive, making the back contract cheaper than the front. This is the global standard for bond futures.
- **Contango (Negative Roll):** Occurs if the back contract's CTD is a significantly more valuable (lower yield) bond than the front contract's CTD, or in rare inverted-curve environments with negative carry. [[During_Fixed_Income_Ch29.md#page=322]]

### 2. The Roll Ratio ($\lambda$)
To maintain a neutral risk profile, the number of contracts in the back ($N_{\text{back}}$) must be adjusted relative to the front ($N_{\text{front}}$):
$$\lambda = \frac{N_{\text{back}}}{N_{\text{front}}} = \frac{PVBP_{\text{front}}}{PVBP_{\text{back}}}$$
- **Typically $\lambda < 1$:** Since the back contract CTD is usually the same or a longer-dated bond than the front CTD, the back contract has a higher PVBP. Therefore, fewer back contracts are needed to hedge the same nominal risk. [[During_Fixed_Income_Ch29.md#page=324]]

## Strategic Implications: Roll Seasonality

Rolling activity creates predictable seasonal spikes in volume and open interest.
- **CTA Behavior:** Commodity Trading Advisors and other specialists typically roll early to avoid the risk of physical delivery.
- **Tracking Progress:** Analysts monitor the share of back-contract open interest to gauge how much of the market's total risk has successfully transitioned. US contracts (CBOT) tend to roll earlier than European (Eurex) ones due to the month-long delivery window in the US. [[During_Fixed_Income_Ch29.md#page=306]]

## Evidence / Source Anchors

- Definition of the futures roll and the calendar spread formula: [[During_Fixed_Income_Ch29.md#page=321]]
- Analysis of Backwardation vs. Contango in roll pricing: [[During_Fixed_Income_Ch29.md#page=322]]
- Mathematical derivation of the PVBP-neutral roll ratio: [[During_Fixed_Income_Ch29.md#page=324]]
- Discussion on why open interest grows despite roll ratios < 1 (issuance of new bonds): [[During_Fixed_Income_Ch29.md#page=324]]
- Comparison of roll timing across CBOT, Eurex, and JPX (Figure 28.4): [[During_Fixed_Income_Ch29.md#page=306]]

## Related

- [[Bond_Futures_Contract_Design]] — The base instrument.
- [[Cheapest_To_Deliver_CTD]] — The primary driver of roll ratio differences.
- [[Present_Value_Of_A_Basis_Point]] — The sensitivity measure being balanced.
- [[Yield_Curve_Carry_And_Roll_Down]] — The economic driver of the roll's backwardation.
