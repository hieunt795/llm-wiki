---
title: Bootstrapping Curve Construction
aliases:
- Bootstrapping
- Bootlacing
- Recursive Yield Stripping
- Lột vỏ đường cong
type: mechanism
tags:
- quantitative-finance
- yield-curves
- valuation
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch20.md
thesis: Bootstrapping is a recursive algorithm used to extract discount factors and
  zero rates from a sequence of par instruments, systematically stripping away coupon
  payments using previously solved values to uncover the pure time-value of money.
source_refs:
- file: During_Fixed_Income_Ch20.md
  page: 193
- file: During_Fixed_Income_Ch20.md
  page: 194
- file: During_Fixed_Income_Ch20.md
  page: 195
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Par rates (like swap rates or bond yields) are mathematically "polluted" by periodic coupons, which create reinvestment risk. Alexander Düring explains that **Bootstrapping** is the essential market-based tool to "un-pollute" these rates. By treating each maturity point as a dependent extension of the points that precede it, bootstrapping creates a set of discount factors that reprice all market instruments exactly. [[During_Fixed_Income_Ch20.md#page=193]]

## Mechanism: The Recursive Algorithm

The process involves progressively stripping coupon instruments into zero-coupon equivalents:

1.  **Step 1 (The Anchor):** For a 1-year instrument, the coupon is its only payment (assuming annual). The 1Y Discount Factor ($Df_1$) is simply:
$$Df_1 = \frac{1}{1 + p_1}$$
- where $p_1$ is the 1Y par rate. [[During_Fixed_Income_Ch20.md#page=193]]

2.  **Step 2 (Recursive Stripping):** A 2-year par bond pays a coupon at Year 1 (which we now know how to discount) and Par + Coupon at Year 2. To keep the price at Par (1.0):
$$1 = (p_2 \times Df_1) + ((1 + p_2) \times Df_2)$$
Solving for the unknown $Df_2$:
$$Df_2 = \frac{1 - (p_2 \times Df_1)}{1 + p_2}$$
[[During_Fixed_Income_Ch20.md#page=194]]

3.  **General Form:** For any year $i$:
$$Df_i = \frac{1 - p_i \sum_{j=1}^{i-1} Df_j}{1 + p_i}$$
This iterative nature is colloquially known as **"Bootlacing"** because each new "lace" (maturity point) relies on the support of the previous ones. [[During_Fixed_Income_Ch20.md#page=194-195]]

## Reverse Bootstrapping

Occasionally, analysts need to decompose a given payment obligation (like an annuity) into a portfolio of par instruments.
- **Direction:** Unlike standard bootstrapping, this starts at the longest maturity point and progresses toward the shortest.
- **Use Case:** Translating a fixed cashflow liability into a portfolio of par swaps for hedging purposes. [[During_Fixed_Income_Ch20.md#page=195]]

## Evidence / Source Anchors

- Definition of bootstrapping as stripping coupon instruments into zero instruments: [[During_Fixed_Income_Ch20.md#page=193]]
- Detailed table of the bootstrapping algorithm for a 10Y swap curve: [[During_Fixed_Income_Ch20.md#page=194]] (Table 19.1)
- General mathematical formula for recursive discount factor extraction: [[During_Fixed_Income_Ch20.md#page=194]]
- Visualization of the "Bootlacing" process: [[During_Fixed_Income_Ch20.md#page=195]] (Figure 19.2)
- Analysis of Reverse Bootstrapping starting from longest maturities: [[During_Fixed_Income_Ch20.md#page=195-196]]

## Related

- [[Yield_Curve_Representations]] — The output of the bootstrapping process.
- [[Discount_Factors_Theory]] — The theoretical targets being solved for.
- [[Cash_Stub_Rate]] — The " भौतिक grounding" needed before Step 1.
- [[Interest_Rate_Swap_Plain_Vanilla]] — The primary par instruments used for bootstrapping.
