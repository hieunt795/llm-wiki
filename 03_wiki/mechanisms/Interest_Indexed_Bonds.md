---
title: Interest-Indexed Bonds
aliases:
- Pay-as-you-go Linkers
- Floating Rate Inflation Linkers
- BTP Italia Structure
type: mechanism
tags:
- fixed-income
- inflation
- bond-mechanics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch24.md
thesis: Interest-indexed bonds are inflation-linked instruments that utilize a floating-rate
  coupon structure (Inflation + Spread) while maintaining a constant nominal principal,
  serving as a simpler but more carry-sensitive alternative to capital-indexed TIPS.
source_refs:
- file: During_Fixed_Income_Ch24.md
  page: 231
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

While the majority of sovereign linkers use the capital-indexed (TIPS) structure, corporate issuers and specific retail programs (like Italy's **BTP Italia**) often prefer the **Interest-Indexed** (Pay-as-you-go) model. Alexander Düring explains that this structure simplifies settlement and provides higher immediate cash income (carry) at the cost of sacrificing principal protection against inflation. [[During_Fixed_Income_Ch24.md#page=231]]

## Mechanism: Pay-as-you-go

Unlike TIPS, where inflation is "hidden" in the growing principal, interest-indexed bonds pay out inflation as it happens:

1.  **Principal:** Constant and typically repaid at Par (100). No index ratio is applied to the notional.
2.  **Coupons:** Calculated as a floating rate.
    - **Formula:** $\text{Coupon} = \text{Inflation Rate} + \text{Fixed Spread}$
3.  **Timing:** The inflation rate is determined at the start of each interest period based on the most recent CPI readings. [[During_Fixed_Income_Ch24.md#page=231]]

## Strategic Trade-offs

### 1. The Carry Advantage
Because the inflation compensation is paid out periodically, interest-indexed bonds have much higher coupon rates than TIPS. This makes them attractive to retail investors and income-focused funds who prioritize immediate cashflow over long-term principal growth. [[During_Fixed_Income_Ch24.md#page=231]]

### 2. The Inflation Risk Profile
- **TIPS:** Investor is protected against cumulative inflation over the life of the bond.
- **Interest-Indexed:** Investor is exposed to the path of inflation. Since the coupon is set at the start of the period, the investor faces **inflation risk** within the period itself (if inflation spikes after the coupon is set but before it is paid). [[During_Fixed_Income_Ch24.md#page=231]]

### 3. Valuation Parity
Düring notes that given a term structure of inflation expectations, it is possible to calculate a theoretical "equivalence" between TIPS and Interest-indexed bonds. However, their risk characteristics (Duration and Convexity) are fundamentally different due to the timing of the cashflows. [[During_Fixed_Income_Ch24.md#page=231]]

## Evidence / Source Anchors

- Contrast between capital-indexed (TIPS) and interest-indexed (FRN-style) bond structures: [[During_Fixed_Income_Ch24.md#page=231]]
- Identification of the BTP Italia as a prominent example of interest-indexed debt: [[During_Fixed_Income_Ch24.md#page=231]]
- Analysis of higher coupon payments in pay-as-you-go structures: [[During_Fixed_Income_Ch24.md#page=231]]
- Discussion on the simplicity of par principal repayment: [[During_Fixed_Income_Ch24.md#page=231]]

## Related

- [[TIPS_Bond_Structure]] — The competing capital-indexed model.
- [[Floating_Rate_Notes_FRN]] — The underlying technical framework for interest-indexed bonds.
- [[Inflation_Indexed_Bonds]] — The broader category.
- [[Breakeven_Inflation_Metrics]] — Used to compare the two structures.
