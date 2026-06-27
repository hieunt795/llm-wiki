---
title: Bond Valuation Principles
aliases:
- Clean vs. Dirty Price
- Yield to Maturity (YTM)
- Bond Pricing Formula
type: mechanism
tags:
- bonds
- valuation
- mathematics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Fixed_Income_Alexander_During_Ch16.md
thesis: Bond valuation is the process of discounting future cash flows (coupons and
  principal) to their present value, fundamentally bifurcated into Clean Price (market
  quote) and Dirty Price (actual invoice amount).
source_refs:
- file: Fixed_Income_Alexander_During_Ch16.md
  page: 138
- file: Fixed_Income_Alexander_During_Ch16.md
  page: 151
- file: Fixed_Income_Alexander_During_Ch16.md
  page: 159
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

The valuation of a bond is mathematically a time-value-of-money problem. Because bonds trade between coupon dates, the market uses the **Clean Price** to avoid "saw-tooth" price volatility caused by accruing interest, while the **Dirty Price** represents the actual cash economic exchange.

## Mechanism

### 1. The Pricing Formula (Compound Yield)
The dirty price ($P$) is the sum of the present values of all future cash flows ($Cf_i$), discounted at the compound yield ($y$):
$$P = \sum_{i} \frac{Cf_i}{(1 + y)^{DCF(t_s, t_i)}}$$
Where:
- $t_s$: Settlement date.
- $t_i$: Payment date of cash flow $i$.
- $DCF$: Daycount fraction according to market convention.

### 2. Clean vs. Dirty Price
- **Dirty Price:** The actual invoice amount paid by the buyer to the seller. Includes the market value of the bond plus interest accrued since the last coupon.
- **Clean Price:** The market quotation. It is calculated as:
$$\text{Clean Price} = \text{Dirty Price} - \text{Accrued Interest}$$
- **Accrued Interest ($I$):** Calculated as a linear interpolation:
$$I = C \times DCF(t_{i-1}, t_s)$$
Where $C$ is the annual coupon and $t_{i-1}$ is the previous coupon date.

### Yield Measures

| Yield Type | Calculation / Definition | Context |
|---|---|---|
| **Running Yield** | $y = C / P$ | Simplest measure, equivalent to dividend yield. |
| **Simple Yield** | $y = \frac{C - (P-100)/t}{P}$ | Standard convention in the Japanese market; amortizes capital gains/losses linearly. |
| **Compound Yield** | Internal Rate of Return (IRR) | The "scientific" standard; assumes reinvestment at the same rate. |
| **Par Yield** | The yield where Clean Price = Par (100) | Used as a benchmark for new issuances. |

### Boundaries / Conditions

### The Thirty-Seconds Convention (US Market)
While most markets use decimal increments (0.001%), the US Treasury market uses 1/32nds.
- Example: `99-24` means $99 + 24/32 = 99.75\%$.
- A `+` suffix adds 1/64th (e.g., `99-24+` = $99.765625\%$).

## Evidence / Source Anchors

- Definition of Clean vs. Dirty Price and "saw-tooth" pattern: [[Fixed_Income_Alexander_During_Ch16.md#page=151]]
- Compound yield formula and IRR: [[Fixed_Income_Alexander_During_Ch16.md#page=160]]
- US price quotation in 32nds: [[Fixed_Income_Alexander_During_Ch16.md#page=152]]

## Related

- [[Daycount_Conventions]] — The rules governing $DCF$ calculations.
- [[Interest_Rate_Risk_Duration_Convexity]] — Sensitivity of these prices to yield changes.
- [[Amortising_Bond_Mechanics]] — Valuation when the principal is not a "bullet" repayment.
