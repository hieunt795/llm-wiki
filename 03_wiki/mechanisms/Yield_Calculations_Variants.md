---
title: Yield Calculations Variants
aliases:
- Bond Yield
- Compound Yield
- Simple Yield
- Running Yield
- Bond-equivalent Yield
- BEY
- Moosmüller Yield
- Lợi suất trái phiếu
type: mechanism
tags:
- fixed-income
- valuation
- mathematics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch17.md
thesis: Bond yield is a standardized measure of return used to collapse a complex
  schedule of cashflows into a single percentage, with various methodologies (Running,
  Simple, Compound) reflecting different assumptions about capital amortization and
  reinvestment.
source_refs:
- file: During_Fixed_Income_Ch17.md
  page: 159
- file: During_Fixed_Income_Ch17.md
  page: 160
- file: During_Fixed_Income_Ch17.md
  page: 161
- file: During_Fixed_Income_Ch17.md
  page: 162
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Yield is the primary language of the bond market, yet it is fundamentally a mathematical "illusion" designed to simplify price discovery. Alexander Düring explains that different yield measures make varying simplifications about the time value of money, with the most sophisticated (Compound Yield) relying on a highly unrealistic assumption: that all interim coupons can be reinvested at the same internal rate of return. [[During_Fixed_Income_Ch17.md#page=159]]

## The Yield Taxonomy

### 1. Running Yield (Lợi suất tức thời)
- **Concept:** The equivalent of a dividend yield for equities.
- **Toán học:** $y = \frac{C}{P}$ (where $C$ is coupon and $P$ is dirty price).
- **Simplification:** Ignores capital gains or losses at maturity. Useful only for immediate income analysis. [[During_Fixed_Income_Ch17.md#page=160]]

### 2. Simple Yield (Trường phái Nhật Bản)
- **Concept:** Incorporates capital amortization in a linear way.
- **Toán học:** $y = \frac{C - \frac{P - 100}{t}}{P}$
- **Simplification:** Assigns the same value to a loss occurring in 1 year as one in 10 years (linear rather than exponential discounting). Standard in the Japanese JGB market. [[During_Fixed_Income_Ch17.md#page=160]]

### 3. Compound Yield (Lợi suất quy chuẩn - IRR)
- **Concept:** The internal rate of return (IRR) of all cashflows.
- **Toán học:** $P = \sum_i \frac{CF_i}{(1+y)^{DCF(t_s, t_i)}}$
- **Moosmüller Yield (German variation):** Treats the stub period (time to first coupon) as a money market instrument (linear discounting) and the rest as compound. [[During_Fixed_Income_Ch17.md#page=160]]

### 4. Bond-Equivalent Yield (BEY - US Standard)
- **Concept:** Translates semi-annual compounding into an annualized figure.
- **Toán học:** $y_B = 2 (\sqrt{1+y} - 1)$
- **Result:** BEY is always slightly lower than the compound yield by an amount of $y^2/4$. [[During_Fixed_Income_Ch17.md#page=161]]

## Critical Critique: The Yield Fallacy

Alexander Düring highlights two structural flaws in the compound yield measure:

1.  **The Reinvestment Paradox:** Yield assumes all coupons are reinvested at rate $y$. In a normal upward-sloping yield curve, short-term reinvestment rates are lower than long-term yields. Thus, an investor holding to maturity and reinvesting coupons will almost always achieve a total return **lower than the quoted yield**. [[During_Fixed_Income_Ch17.md#page=161]]
2.  **The Flat Curve Assumption:** By using a single $y$ for all cashflows, yield implicitly assumes a perfectly flat yield curve. It negates the idea that coupons from different bonds (by the same issuer) should be discounted by different rates based on their specific timing. This leads to the necessity of **Discount Factor Curves**. [[During_Fixed_Income_Ch17.md#page=161-162]]

## Evidence / Source Anchors

- Analysis of Running Yield as a dividend-style measure: [[During_Fixed_Income_Ch17.md#page=160]]
- The Japanese standard of Simple Yield and its linear amortization flaw: [[During_Fixed_Income_Ch17.md#page=160]]
- Mathematical definition of Compound Yield and the Moosmüller variant: [[During_Fixed_Income_Ch17.md#page=160]]
- Proof of the Reinvestment Paradox in non-flat curve environments: [[During_Fixed_Income_Ch17.md#page=161]]
- Criticism of yield's implicit assumption of time-invariance in rates: [[During_Fixed_Income_Ch17.md#page=161-162]]

## Related

- [[Discount_Factors_Theory]] — The "absolute truth" that yield attempts to simplify.
- [[Bond_Cashflow_Structural_Typologies]] — The algorithms that these yields collapse into a single number.
- [[Yield_Curve_Representations]] — The visualization of different yields across maturities.
- [[Bootstrapping_Curve_Construction]] — The process of moving from yields back to discount factors.
