---
title: Bond Pricing and Accrued Interest
aliases:
- Clean Price
- Dirty Price
- Accrued Interest
- Par Price
- Price Quotation
- Thirty-seconds
- Ex-dividend Period
type: convention
tags:
- fixed-income
- trading
- conventions
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch17.md
thesis: Bond pricing conventions bifurcate between the quoted 'Clean Price' and the
  settlement 'Dirty Price', utilizing specialized rounding and fractional rules (like
  US thirty-seconds) to standardize global trading.
source_refs:
- file: During_Fixed_Income_Ch17.md
  page: 151
- file: During_Fixed_Income_Ch17.md
  page: 152
- file: During_Fixed_Income_Ch17.md
  page: 158
- file: During_Fixed_Income_Ch17.md
  page: 159
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

In the bond market, the price you see is rarely the price you pay. To prevent interest rate changes from being masked by daily interest accrual, bonds are quoted on a **Clean Price** basis. However, to settle a trade, the buyer must compensate the seller for the interest earned since the last coupon date, known as **Accrued Interest**. The sum of these two is the **Dirty Price**, which represents the actual cash amount (the invoice amount) exchanged. [[During_Fixed_Income_Ch17.md#page=151]]

## Mechanism: The Price-Yield Dynamic

### 1. Clean vs. Dirty Price
- **Clean Price:** The quoted market price. It remains relatively stable if yields do not change.
- **Accrued Interest:** Calculated as $I = C \times DCF(t_{i-1}, t_s)$, where $C$ is the coupon and $t_s$ is the settlement date.
- **Dirty Price:** Clean Price + Accrued Interest. It exhibits a "saw-tooth" pattern through time, dropping sharply on every coupon payment date. [[During_Fixed_Income_Ch17.md#page=158-159]]

### 2. The US Thirty-Seconds (32nds) Convention
The US Treasury market famously resists decimalization, utilizing binary fractions rooted in the history of physical coins.
- **The Format:** A quote of **99-24** means $99 + 24/32 = 99.75\%$.
- **The Plus (+):** An extra 1/64th. **99-24+** = $99 + 24/32 + 1/64 = 99.765625\%$.
- **Sub-fractions:** Eighths of a thirty-second. **99-245** represents $99 + 24/32 + 5/256 = 99.76953125\%$. [[During_Fixed_Income_Ch17.md#page=152-153]]

### 3. Ex-Dividend Periods
Stemming from the era of paper certificates, some markets (notably the UK) have a period before the coupon payment where the bond trades "ex-dividend."
- **The Process:** If a trade settles during this period, the seller (not the buyer) receives the upcoming coupon.
- **Accrued Interest:** In this case, accrued interest is **negative**, as the buyer will hold the bond for a few days without being entitled to the next interest payment. [[During_Fixed_Income_Ch17.md#page=159]]

## Strategic Implications: Par Yields

The yield that makes a bond's clean price exactly equal to 100 (Par) is the **Par Yield**.
- **The Divergence:** Because accrued interest is calculated linearly while yields are compound, the clean price of a bond trading "at its coupon" will still marginally diverge from Par between coupon dates. This difference is larger for bonds with higher coupons and during leap years. [[During_Fixed_Income_Ch17.md#page=151-152]]

## Evidence / Source Anchors

- Definition of Clean Price, Dirty Price, and Accrued Interest: [[During_Fixed_Income_Ch17.md#page=151]]
- Visual analysis of the saw-tooth pattern of dirty prices: [[During_Fixed_Income_Ch17.md#page=152]]
- Detailed breakdown of the US 1/32nd price convention: [[During_Fixed_Income_Ch17.md#page=152-153]]
- Analysis of the ex-dividend period and negative accrued interest: [[During_Fixed_Income_Ch17.md#page=159]]
- Proof of clean price divergence from par due to linear/compound mismatch: [[During_Fixed_Income_Ch17.md#page=151-152]]

## Related

- [[Yield_Calculations_Variants]] — The mathematical output of these price inputs.
- [[Daycount_Conventions]] — The rules used to calculate the $DCF$ in the accrued interest formula.
- [[Bond_Cashflow_Structural_Typologies]] — How structures (like Zeros) eliminate accrued interest entirely.
- [[Price_Quantization_Noise]] — The impact of minimum price increments (ticks) on market efficiency.
