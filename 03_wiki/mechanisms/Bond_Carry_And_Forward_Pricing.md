---
title: Bond Carry and Forward Pricing
aliases:
- Carry
- Bond Carry
- Carry and Roll Down
- Forward Bond Pricing
- Lợi nhuận nắm giữ
type: mechanism
tags:
- fixed-income
- trading
- mathematics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch17.md
thesis: Bond carry is the income generated from holding a long bond position funded
  at the prevailing repo rate, mathematically defined by the spread between the spot
  price and the implied forward price.
source_refs:
- file: During_Fixed_Income_Ch17.md
  page: 167
- file: During_Fixed_Income_Ch17.md
  page: 168
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Carry is the primary driver of returns in a stable interest rate environment. It measures the net benefit of "carrying" an asset on the balance sheet, accounting for the income it generates (coupons) minus the cost to finance it (repo). Alexander Düring emphasizes that carry is fundamentally a **forward-looking** measure: it is the profit an investor earns if interest rates and the yield curve remain perfectly unchanged. [[During_Fixed_Income_Ch17.md#page=167]]

## Mechanism: The No-Arbitrage Forward Price

To calculate carry, one must first determine the **Forward Price** ($P_f$) of the bond for a future settlement date $t_f$.

### 1. No Interim Coupon
If no coupon is paid between today ($t_0$) and the forward date ($t_f$):
$$P_f = P_0 (1 + r DCF(t_0, t_f))$$
- where $r$ is the financing rate (typically the [[General_Collateral_Vs_Special|Repo Rate]]). [[During_Fixed_Income_Ch17.md#page=167]]

### 2. Including Interim Coupons
If a coupon $C$ is paid at time $t_i$, it must be subtracted from the forward price because the forward buyer will not receive it. The coupon is reinvested at the repo rate until $t_f$:
$$P_f = \frac{P_0}{Df(t_0, t_f)} - C \frac{Df(t_i, t_f)}{Df(t_0, t_f)}$$
[[During_Fixed_Income_Ch17.md#page=168]]

## The Definition of Carry

The carry earned over the period is the difference between the current price and the price at which you are "forced" to sell in the future by the math of financing:

### 1. In Price Terms
$$\text{Carry} = \text{Spot Price} - \text{Forward Price}$$
- **Paradox of Zeros:** Zero-coupon bonds exhibit **negative carry** in price terms because their spot price is always lower than their par-converging forward price. [[During_Fixed_Income_Ch17.md#page=167]]

### 2. In Yield Terms (US Standard)
$$\text{Carry} = \text{Forward Yield} - \text{Spot Yield}$$

### 3. The Carry Approximation
For practical purposes, carry can be approximated by de-annualizing the spread between the bond yield and the repo rate over the holding period:
$$\text{Carry} \approx (y - r) \times \frac{\text{Holding Days}}{360}$$
Düring notes that this approximation works surprisingly well, especially when using **Simple Yield** rather than Compound Yield. [[During_Fixed_Income_Ch17.md#page=168]]

## Evidence / Source Anchors

- Definition of carry as coupon income minus financing cost: [[During_Fixed_Income_Ch17.md#page=167]]
- Mathematical derivation of forward bond prices via repo-based discount factors: [[During_Fixed_Income_Ch17.md#page=167]]
- Analysis of the negative carry paradox for zero-coupon bonds: [[During_Fixed_Income_Ch17.md#page=167]]
- The exact formula for forward pricing with interim coupon reinvestment: [[During_Fixed_Income_Ch17.md#page=168]]
- Comparison of carry approximation quality across yield measures: [[During_Fixed_Income_Ch17.md#page=168]]

## Related

- [[Repurchase_Agreement_Repo_Market_Structure]] — The source of the financing rate $r$.
- [[Yield_Calculations_Variants]] — Why Simple Yield is often better for carry approximations.
- [[Bond_Roll_Down]] — The secondary component of static returns (moving down the curve).
- [[Zero_Coupon_Bond_Pricing]] — Detailed view of the pull-to-par effect.
