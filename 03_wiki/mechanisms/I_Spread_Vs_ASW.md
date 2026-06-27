---
title: I-Spread vs Asset Swap Spread
aliases:
- I-Spread
- Interpolated Spread
- Hedge Quality vs Liquidity
- Quick-and-Dirty Spread
type: mechanism
tags:
- trading-strategies
- market-infrastructure
- liquidity
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch23.md
thesis: The choice between I-spread (Interpolated) and Asset Swap Spread (ASW) represents
  a trade-off between operational liquidity and hedge quality, where I-spread provides
  a high-speed approximation for short-term trades while ASW offers precise, cashflow-matched
  protection.
source_refs:
- file: During_Fixed_Income_Ch23.md
  page: 223
- file: During_Fixed_Income_Ch23.md
  page: 224
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Analysts often use "Spread over Swaps" loosely, but the technical implementation significantly alters risk. Alexander Düring bóc tách sự đánh đổi giữa hai phương pháp: **I-spread** (Interpolated) và **Asset Swap Spread** (ASW). While I-spread is the "Quick-and-Dirty" market standard for speed, ASW is the "Gold Standard" for institutional risk management. [[During_Fixed_Income_Ch23.md#page=223]]

## 1. I-Spread (Interpolated Spread)
Instead of modeling the specific cashflows of a bond, the I-spread compares the bond's yield to a single point interpolated on the swap curve at the exact same maturity date.

- **The Benefit (Liquidity):** Since it uses standard par swaps as reference points, it is extremely fast to calculate and has a lower balance sheet cost for short-term hedges.
- **The Flaw (Hedge Quality):** It ignores the difference in coupon frequencies and payment dates between the bond and the swap. Large curve movements will create a "drift" or mismatch between the bond's value and the I-spread hedge. [[During_Fixed_Income_Ch23.md#page=224]]

## 2. Asset Swap Spread (ASW)
The ASW spread explicitly models every future cashflow of the bond and matches them with a custom-structured swap.

- **The Benefit (Precision):** It provides the highest quality hedge. If an investor holds a bond and enters an ASW, they have virtually eliminated all interest rate risk, including risks from coupon frequency mismatches.
- **The Flaw (Execution):** Because ASW structures are bespoke (not standardized), they are less liquid and more difficult to enter or unwind than standard par swaps. [[During_Fixed_Income_Ch23.md#page=224]]

## Strategic Application: Selection Criteria

| Factor | Preferred Metric | Why? |
| :--- | :--- | :--- |
| **Short-term Trading** | **I-Spread** | Speed of execution and transparency are paramount. |
| **Long-term ALM** | **ASW Spread** | Cumulative mismatches in coupon frequency (e.g., Italian BTPs) become significant over years. |
| **Bespoke Assets** | **ASW Spread** | Required for amortizing or irregular structures where a single yield point doesn't exist. |

[[During_Fixed_Income_Ch23.md#page=224]]

## Evidence / Source Anchors

- Definition of I-spread as a fixed-side interpolated spread: [[During_Fixed_Income_Ch23.md#page=223]]
- Analysis of the trade-off between asset swap precision and interpolated swap liquidity: [[During_Fixed_Income_Ch23.md#page=224]]
- Identification of I-spreads as faster to price with lower balance sheet cost: [[During_Fixed_Income_Ch23.md#page=224]]
- Discussion on the "drift" caused by coupon frequency differences in I-spreads: [[During_Fixed_Income_Ch23.md#page=224]]

## Related

- [[Asset_Swap_Spread_ASW]] — Cơ chế định giá chính xác và hedge dòng tiền.
- [[Yield_Curve_Spreads_Taxonomy]] — Ma trận các loại spread.
- [[Bond_Pricing_Conventions]] — Lý do tại sao sai lệch tần suất coupon lại quan trọng.
- [[Over_The_Counter_OTC_Markets]] — Môi trường vận hành của các giao dịch hoán đổi.
