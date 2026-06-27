---
title: Term Risk Premium Mechanics
aliases:
- Term Premium
- Liquidity Risk Premium
- Maturity Premium
- Phần bù rủi ro kỳ hạn
type: mechanism
tags:
- monetary-policy
- valuation
- yield-curve
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch16.md
thesis: The term risk premium is an unobservable spread over expected future short
  rates that compensates lenders for the loss of liquidity and the uncertainty inherent
  in long-term commitments.
source_refs:
- file: During_Fixed_Income_Ch16.md
  page: 136
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Economically, the **Term Risk Premium** represents the price of "giving up options." An overnight investor has the daily option to reinvest their cash elsewhere; a term lender surrenders this option for the duration of the loan. Alexander Düring explains that while this premium is unobservable, its presence is a critical filter for interpreting the shape of the yield curve and central bank expectations. [[During_Fixed_Income_Ch16.md#page=136]]

## Mechanism: The Price of Surrendered Options

The term premium is defined as the difference between the actual market interest rate and the pure expectation of future short rates.

### 1. Growth with Maturity
The term risk premium generally grows as the investment horizon lengthens. The further into the future a cashflow is, the greater the uncertainty regarding inflation, credit quality, and alternative opportunity costs. [[During_Fixed_Income_Ch16.md#page=136]]

### 2. The Unobservable Variable
Because the premium cannot be directly seen on a Bloomberg terminal, it must be modeled. However, most models work on timescales that are too long to be relevant for daily central bank forecasting. In standard short-term analysis, the premium is often "simply ignored," assuming it grows slowly enough over near horizons. [[During_Fixed_Income_Ch16.md#page=136]]

## Strategic Implications: The Flat Curve Paradox

The presence of a term premium creates a fundamental paradox when interpreting the yield curve:

- **The Baseline:** If the market expects rates to stay constant, the yield curve should actually be **upward-sloping** (to reflect the positive term premium).
- **The Paradox:** A **flat yield curve** does not mean the market expects constant rates. It means the market expects **rate cuts** significant enough to perfectly offset the increasing term risk premium.
- **The Inference:** An inverted yield curve represents even more aggressive rate-cut expectations, signaling a severe economic downturn or a significant policy shift. [[During_Fixed_Income_Ch16.md#page=136]]

## Evidence / Source Anchors

- Definition of the term risk premium as compensation for giving up reinvestment options: [[During_Fixed_Income_Ch16.md#page=136]]
- Relationship between premium growth and longer investment horizons: [[During_Fixed_Income_Ch16.md#page=136]]
- Analysis of the flat yield curve as an indicator of rate-cut expectations: [[During_Fixed_Income_Ch16.md#page=136]]
- Discussion on the unobservable nature of the premium and modeling limitations: [[During_Fixed_Income_Ch16.md#page=136]]

## Related

- [[Policy_Rate_Expectations_Extraction]] — The process where term premium must be accounted for or ignored.
- [[Yield_Curve_Representations]] — The visualization where the premium is embedded.
- [[Macaulay_Duration]] — A measure of the time-sensitivity that drives the term premium.
- [[Liquidity_Preference_Theory]] — The underlying economic theory explaining the premium.
- [[Bond_Relative_Value_Valuation]]
- [[Financial_Repression]]
- [[On_The_Run_Liquidity_Premium]]
- [[Price_Yield_Inverse_Relationship]]
- [[Daycount_Conventions]]
- [[Prepayment_Risk_Tranching_And_PACs]]
