---
title: TIPS Bond Structure
aliases:
- Capital-Indexed Bonds
- Real Coupon Mechanism
- TIPS Structure
- Index Ratio
- Inflation Lag
- Inflation Interpolation
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
expert_lens: "Alexander Düring | Neil Schofield"
provenance: During_Fixed_Income_Ch24.md, Schofield_Trading_Fixed_Income_2011.md
thesis: The TIPS (Capital-Indexed) structure maintains constant purchasing power by
  scaling every nominal cashflow—both coupons and principal—by an index ratio derived
  from lagged and interpolated CPI data (the Canadian Model).
source_refs:
- file: During_Fixed_Income_Ch24.md
  page: 230
- file: During_Fixed_Income_Ch24.md
  page: 231
- file: During_Fixed_Income_Ch24.md
  page: 233
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 53
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 54
created: '2026-04-13'
updated: '2026-04-22'
---

## Thesis

The TIPS structure (Treasury Inflation-Protected Securities), also known as **Capital-Indexed**, is the global standard for sovereign inflation-linked debt. Alexander Düring explains that by adjusting the "Capital" (the Notional) rather than just the interest rate, the bond returns the loss of purchasing power to the investor as a lump sum at maturity. This creates a "real" instrument where the coupon rate remains constant in purchasing power units. [[During_Fixed_Income_Ch24.md#page=230-231]]

## Mechanism: The Index Ratio ($R_t$)

The fundamental scaling factor for every cashflow is the **Index Ratio**:
$$R_t = \frac{I_t}{I_0}$$
- **$I_t$ (Reference Index):** The interpolated CPI level for settlement date $t$.
- **$I_0$ (Base Index):** The reference index at the bond's issuance. [[During_Fixed_Income_Ch24.md#page=230]]

### 1. Nominal Cashflow Calculation
The actual cash amount paid to the investor is:
$$\text{Nominal Cashflow} = \text{Real Cashflow} \times R_t$$
- **Coupons:** TIPS pay lower coupon rates than nominal bonds because the inflation compensation is returned via the principal uplift.
- **Principal:** Redeemed at $\text{Par} \times R_{\text{maturity}}$. [[During_Fixed_Income_Ch24.md#page=230]]

### 2. The Reference Index $I_t$: Lag and Interpolation
Daily CPI readings do not exist. To provide a daily $I_t$, markets use:
- **Inflation Lag:** A fixed period (e.g., 3 months in the US and Europe) before the settlement date to allow for CPI publication.
- **Linear Interpolation (The Canadian Model):** $I_t$ is linearly interpolated between the two closest published monthly values. Schofield notes that this specific interpolation method is widely known as the **Canadian Model**, which is the global standard and was adopted by the UK for bonds issued after 2005. [[Schofield_Trading_Fixed_Income_2011.md#page=53]]
  
  The formula for calculating the interpolated index on a specific settlement day $t$ in month $m$ is:
  $$Index = CPI_{m-3} + \frac{t-1}{D} \times (CPI_{m-2} - CPI_{m-3})$$
  Where $D$ is the number of days in month $m$. [[Schofield_Trading_Fixed_Income_2011.md#page=53]]

## Technical Nuances: Rebasing and Floors

### 1. The Deflation Floor
Most modern TIPS structures include a floor: at maturity, the investor receives the maximum of (Par) or $(\text{Par} \times R_{\text{maturity}})$. This ensures that even in prolonged deflation, the nominal principal is never lost. Schofield notes that the UK, Canada, and Japan are exceptions that historically did not impose deflation floors. [[During_Fixed_Income_Ch24.md#page=230]] [[Schofield_Trading_Fixed_Income_2011.md#page=54]]

### 2. Index Rebasing (Chaining)
When statistics offices change index weights and reset the level (e.g., Base-2010 to Base-2015), existing bonds must be transitioned.
- **The Process:** The old and new indices are **chained** using the ratio of their averages over the transition year.
- **The Result:** Historical index ratios $(R_t)$ remain mathematically unchanged, preventing a discrete jump in bond prices during a rebasing. [[During_Fixed_Income_Ch24.md#page=233]]

## Market Quoting Convention (Fractional Pricing & Invoice Calculation)

While the bond returns are based on inflation, the secondary market abstracts inflation out of the trading screen to allow traders to focus purely on the **Real Yield**. [WEB] [Nguồn: TIPS Watch](https://tipswatch.com)

### 1. Fractional Quoting (32nds)
In the US market, TIPS are quoted using the **Real Price** expressed in 32nds of a point. A quote of `98-16` on a trading screen does not equal 98.16%; it means $98 + \frac{16}{32}$, or `98.50%` of the unadjusted par value. This quote is entirely immune to the current CPI.

### 2. The Invoice Price Calculation
When a trade is executed, the clearing system calculates the actual cash exchanged (the Invoice or Settlement Price) by multiplying the quoted Real Price by the Index Ratio.
- **Example:** If an investor buys $\$100,000$ face value of TIPS at a quoted Real Price of `98-16` (`98.50%`), and the current Index Ratio ($R_t$) is `1.05240`.
- **Calculation:** $98.50\% \times 1.05240 = 103.6614\%$.
- **Actual Cash Paid:** $\$103,661.40$ (excluding accrued interest).
This creates a common "failure condition" for retail investors who may be surprised that the cash deducted from their account is significantly higher than the quoted price times the original par value, due to the accumulated inflation principal uplift. [[Schofield_Trading_Fixed_Income_2011.md#page=53]]

## Evidence / Source Anchors

- Definition of the Index Ratio and the nominal cashflow scaling formula: [[During_Fixed_Income_Ch24.md#page=230]]
- Analysis of the 3-month inflation lag and linear interpolation requirement: [[During_Fixed_Income_Ch24.md#page=230]]
- Comparison of capital-indexed (TIPS) vs. interest-indexed (FRN) structures: [[During_Fixed_Income_Ch24.md#page=231]]
- Description of index chaining mechanics during quinquennial revisions (Japanese case study): [[During_Fixed_Income_Ch24.md#page=233]]
- Calculation of the invoice price using real clean price scaled by $R_t$: [[During_Fixed_Income_Ch24.md#page=232]]
- Description of the Canadian Model for index interpolation, formulas, and absence of deflation floors in certain jurisdictions: [[Schofield_Trading_Fixed_Income_2011.md#page=53-54]]

## Related

- [[Inflation_Indexed_Bonds]] — The broader asset class.
- [[Interest_Indexed_Bonds]] — The alternative floating-coupon structure.
- [[Inflation_Seasonality_And_Pricing]] — Why the interpolation lag creates valuation "noise."
- [[Breakeven_Inflation_Metrics]] — How $R_t$ is used to derive market expectations.
