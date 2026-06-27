---
title: Compounding Mechanics
aliases:
- Compounding
- Lãi kép
- Continuous Compounding
- Annual Effective Rate
- AER
type: mechanism
tags:
- mathematics
- valuation
- interest-rates
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch14.md
thesis: Compounding mechanics describe the process where interest earned on a principal
  is added to the principal for the next accrual period, fundamentally altering the
  total interest cost through exponential rather than linear growth.
source_refs:
- file: During_Fixed_Income_Ch14.md
  page: 116
- file: During_Fixed_Income_Ch14.md
  page: 117
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

While interest rates are typically quoted as annualized figures, the frequency of compounding dictates the true economic cost of a loan. Alexander Düring explains that compounding can lead to surprisingly high effective rates, and in the interbank market, its application is further complicated by the "dead zones" of weekends and holidays. [[During_Fixed_Income_Ch14.md#page=116]]

## Mechanism: From Discrete to Continuous

### 1. The Annual Effective Rate (AER)
To compare different compounding frequencies, the **Annual Effective Rate** ($r_{\text{eff}}$) translates a quoted rate ($r$) into the actual interest paid over one year:
$$r_{\text{eff}} = \left( 1 + \frac{r}{n} \right)^n - 1$$
- **The Power of Frequency:** At 12% annual interest, monthly compounding ($n=12$) generates an AER of 12.68%. [[During_Fixed_Income_Ch14.md#page=116]]

### 2. Continuous Compounding
In interbank lending, which occurs predominantly on an overnight basis, it is useful to consider the limit where $n \to \infty$. This is known as **Continuous Compounding**:
$$r_{\text{eff}} = e^r - 1$$
This model is the basis for most derivative pricing (e.g., Black-Scholes). [[During_Fixed_Income_Ch14.md#page=116]]

## Strategic Dynamics: The Weekend Paradox

In actual interbank lending, compounding is not perfectly continuous because interest cannot be paid or "added to principal" on non-business days.

- **The Logic:** Compounding has no effect on weekends.
- **The Paradox:** For a two-week horizon (14 days), the total interest is not $(1 + r/360)^{14}$, but rather a mix of compounded business days and linearly accrued weekends.
- **Result:** The actual interest paid is slightly *smaller* than what a theoretical continuous model would predict, because the two weekends spanned by the period require linear accrual for 3 days each without compounding. [[During_Fixed_Income_Ch14.md#page=117]]

## Evidence / Source Anchors

- Formula for the Annual Effective Rate (AER) and discrete compounding: [[During_Fixed_Income_Ch14.md#page=116]]
- Mathematical derivation of continuous compounding ($e^r - 1$): [[During_Fixed_Income_Ch14.md#page=116]]
- Analysis of the "Weekend Effect" on interbank compounding: [[During_Fixed_Income_Ch14.md#page=117]]
- Proof of lower total interest due to linear accrual over holidays/weekends: [[During_Fixed_Income_Ch14.md#page=117]]

## Related

- [[Discount_Factors_Theory]] — Compounding is the bridge between a term rate and its discount factor.
- [[Overnight_Index_Rates_FRN_Compounding]] — Modern application in SOFR/€STR based instruments.
- [[Daycount_Conventions]] — Determines the fraction used within the compounding formula.
