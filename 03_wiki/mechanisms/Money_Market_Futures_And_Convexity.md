---
title: Money Market Futures and Convexity
aliases:
- IMM Dates
- Tick
- Money Market Futures
- Convexity Adjustment (Futures)
- Convexity Bias
- Eurodollar Future
- Euribor Future
- Short Sterling
type: mechanism
tags:
- fixed-income
- derivatives
- quantitative-finance
- trading
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch14.md
thesis: Money market futures are exchange-traded contracts for hedging short-term
  interest rates, characterized by standardized IMM delivery dates and a significant
  convexity bias created by the daily variation margin mechanism.
source_refs:
- file: During_Fixed_Income_Ch14.md
  page: 121
- file: During_Fixed_Income_Ch14.md
  page: 122
- file: During_Fixed_Income_Ch14.md
  page: 124
- file: During_Fixed_Income_Ch14.md
  page: 125
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

While simple in concept (hedging 3-month interest rates), **Money Market Futures** are mathematically distinct from their bilateral equivalent, the Forward Rate Agreement (FRA). Alexander Düring highlights that the mandatory daily margining of futures introduces a path-dependency that results in a permanent price wedge known as **Convexity Adjustment**. This bias ensures that futures-implied rates are not unbiased estimates of future spot rates. [[During_Fixed_Income_Ch14.md#page=121-124]]

## Mechanism: Standardization and Identification

### 1. IMM Dates and Ticks
Futures contracts expire on the third Wednesday of March, June, September, and December (the **IMM Days**). 
- **The Tick:** The minimum discrete price move (e.g., 0.005 or 0.5bp). 
- **The Value:** For a standard USD 1 million contract, one tick is worth approximately **$12.50**. [[During_Fixed_Income_Ch14.md#page=122]]

### 2. The Color-Coded Strip
Traders identify contracts expiring in successive years using a specific color-coding system:
- **White (Year 1):** The next four quarterly expiries.
- **Red, Green, Blue (Years 2-4):** Mnemonic: RGB monitor makes up white light.
- **Gold, Purple, Orange, etc.:** Expiries extending further out (up to 10 years in the US). [[During_Fixed_Income_Ch14.md#page=122]]

## The Convexity Bias (Gamma)

The price of a money market future is linear: $P = 100 - r$. Therefore, its theoretical second derivative with respect to interest rates is zero ($\frac{\partial^2 F}{\partial r^2} = 0$). However, a simple deposit has positive convexity. [[During_Fixed_Income_Ch14.md#page=124]]

### The Margining Effect
In reality, the requirement to post **Variation Margin** creates convexity:
- **Rate Rise:** The value of a long future position falls. The trader must post margin and must fund this cash at the **new, higher rate**.
- **Rate Fall:** The trader receives margin but can only reinvest it at the **new, lower rate**.
- **Result:** Volatility systematically hurts the trader, who is "borrowing at the highs and investing at the lows." [[During_Fixed_Income_Ch14.md#page=124]]

### The Adjustment Formula
To compensate for this cost, the futures implied rate ($r_f$) must be higher than the actual expected forward rate ($r_{FRA}$):
$$\Delta r = -\frac{1}{2} \sigma^2 t^2$$
- where $\sigma$ is interest rate volatility and $t$ is the time to expiry.
- **Strategic Impact:** The adjustment increases **quadratically** with time. It is small for near-term contracts but massive for the "Gold" or "Purple" years in the US dollar strip. [[During_Fixed_Income_Ch14.md#page=125]]

## Evidence / Source Anchors

- Definition of money market futures and the IMM standard: [[During_Fixed_Income_Ch14.md#page=121]]
- Table of expiry month codes and the color-coded strip logic: [[During_Fixed_Income_Ch14.md#page=122-123]]
- Mathematical proof of the convexity bias created by margining: [[During_Fixed_Income_Ch14.md#page=124]]
- The quadratic convexity adjustment formula ($\frac{1}{2} \sigma^2 t^2$): [[During_Fixed_Income_Ch14.md#page=125]]
- Analysis of how margining transforms a linear contract into a convex one: [[During_Fixed_Income_Ch14.md#page=124-125]]

## Related

- [[Margining_IM_Vs_VM]] — The mechanism that creates the convexity bias.
- [[Yield_Curve_Representations]] — Where these futures-implied rates are plotted.
- [[Convexity_Adjustment_CMS_And_CMT]] — Parallel adjustments in longer-dated derivatives.
- [[Discount_Factors_Theory]] — Futures prices must be "de-convexed" before building discount curves.
