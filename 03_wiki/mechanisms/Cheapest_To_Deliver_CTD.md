---
title: Cheapest-to-Deliver (CTD) Mechanism
aliases:
- CTD
- Cheapest-to-deliver
- Deliverable Basket
- CTD Switch
- Trái phiếu rẻ nhất để giao
type: mechanism
tags:
- fixed-income
- derivatives
- trading
- mathematics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Trái phiếu rẻ nhất để giao (CTD) là chứng khoán cụ thể trong rổ tài sản đủ
  điều kiện của một hợp đồng tương lai giúp tối đa hóa lợi nhuận (hoặc tối thiểu hóa
  lỗ) cho vị thế bán (short) trong quá trình giao hàng vật chất; đây là mỏ neo chính
  quyết định giá của hợp đồng tương lai.
source_refs:
- file: During_Fixed_Income_Ch29.md
  page: 310
created: '2026-04-13'
updated: '2026-04-22'
---

## Thesis

Because a bond future allows the seller to deliver *any* bond in the basket, the market assumes the seller will always choose the one that costs them the least. Alexander Düring explains that this bond, the **Cheapest-to-Deliver (CTD)**, is the "true underlying" of the futures contract. Any pricing of the future that decouples from the CTD's forward price will be crushed by **Cash-and-Carry Arbitrage**. [[During_Fixed_Income_Ch29.md#page=310]]

## Mechanism: Identifying the CTD

The CTD is identified by comparing the **Converted Forward Prices** (CFP) of all bonds in the deliverable basket.

### 1. The Decision Metric
- **Gross Basis:** $[ \text{Spot clean price} ] - [ \text{CF} \times \text{Futures price} ]$.
- **Net Basis:** $[ \text{Forward clean price} ] - [ \text{CF} \times \text{Futures price} ]$.
- **The Winner:** The bond with the **lowest (most negative)** net basis is the CTD. In an ideal market, the CTD's net basis should be zero (or slightly positive to account for the quality option). [[During_Fixed_Income_Ch29.md#page=310-311]]

### 2. The Duration Rule (Yield Sensitivity)
The CTD status is highly sensitive to the relationship between market yields $(y)$ and the [[Conversion_Factor_And_Notional_Coupon|Notional Coupon]] $(C)$, which is typically $6\%$.
- **When $y < 6\%$ (Low yields):** The conversion factors over-compensate for long-dated bonds. Therefore, the bond with the **lowest duration** (shortest maturity/highest coupon) tends to become the CTD.
- **When $y > 6\%$ (High yields):** The bond with the **highest duration** (longest maturity/lowest coupon) tends to become the CTD. [[During_Fixed_Income_Ch29.md#page=313]]

## Strategic Implications: The CTD Switch

The CTD is not fixed; it can "switch" if market yields cross the $6\%$ threshold or if idiosyncratic supply issues occur.
- **Quality Option:** Because the short can switch to a new CTD if market conditions change, the futures contract is slightly less valuable than a pure forward on a single bond. This is why the future trades at a discount to the CTD's forward price.
- **Basis Trading:** Traders "buy the basis" (buy bond, sell future) to capture the convergence between the CTD and the contract at delivery. [[During_Fixed_Income_Ch29.md#page=310-315]]

## Evidence / Source Anchors

- Definition of CTD and its role as the convergence anchor: [[During_Fixed_Income_Ch29.md#page=310]]
- Rule for CTD status based on duration and yield vs. notional coupon: [[During_Fixed_Income_Ch29.md#page=313]]
- Analysis of the net basis as the indicator of CTD status: [[During_Fixed_Income_Ch29.md#page=311]]
- Visual representation of converted bond prices under yield shifts (Figure 28.8): [[During_Fixed_Income_Ch29.md#page=313]]
- Use of the basis sheet to identify relative cheapness (Table 28.1): [[During_Fixed_Income_Ch29.md#page=315]]

## Related

- [[Bond_Futures_Contract_Design]] — The instrument that uses CTD.
- [[Conversion_Factor_And_Notional_Coupon]] — The mathematical tools for CTD calculation.
- [[Futures_Quality_Option]] — The value of the right to switch CTDs.
- [[Bond_Carry_And_Forward_Pricing]] — Necessary for calculating the net basis.
- [[Cash_And_Carry_Arbitrage]] — The strategy that enforces CTD pricing.
