---
title: Floating Rate Notes (FRN)
aliases:
- FRN
- Variable-rate note
- Floater
- Trái phiếu lãi suất thả nổi
type: definition
tags:
- fixed-income
- interest-rates
- banking
- product-structuring
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch18.md
thesis: Floating Rate Notes (FRNs) are debt instruments where the coupon is reset
  periodically according to a reference index plus a fixed spread, fundamentally serving
  as an interest-rate risk hedge for institutions whose liabilities track short-term
  market rates.
source_refs:
- file: During_Fixed_Income_Ch18.md
  page: 169
- file: During_Fixed_Income_Ch18.md
  page: 170
- file: During_Fixed_Income_Ch18.md
  page: 171
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The defining characteristic of an FRN is its variable coupon function $C = f(\text{index})$. While a standard fixed-rate bond has a constant coupon, the FRN resets it—usually at the start of each interest period—to match a benchmark (like LIBOR, SOFR, or €STR) plus a constant **Quoted Margin ($\mu$)**. Alexander Düring explains that this feature makes FRNs a "natural" asset for the treasuries of retail banks, as their liability side (deposits) is also linked to fluctuating short-term rates. [[During_Fixed_Income_Ch18.md#page=169-170]]

## Mechanism: The Par Value Property

The most powerful mathematical feature of a standard FRN is its price stability.

### 1. The Pull-to-Par on Reset
At the beginning of each coupon period, right after the coupon is reset, the value of an FRN should theoretically return to **Par (100)**.
- **Proof:** The present value at reset is $P = \frac{100 + C \times DCF}{1 + r \times DCF}$.
- **Equality:** If the Quoted Margin ($\mu$) is exactly equal to the credit risk spread of the issuer at that time, then $C = r$. The numerator and denominator cancel each other out, yielding $P=100$.
- **Induction:** This logic applies recursively from the last reset back to the first. An FRN "washes away" market interest rate risk at every reset date. [[During_Fixed_Income_Ch18.md#page=171]]

### 2. Engineering Perspective: Vertical Addition of Zeros
[RAW] Neftci cung cấp một cách nhìn khác về cấu trúc FRN:
- **The Construction:** Một FRN kỳ hạn $n$ kỳ thực chất là sự cộng dồn theo chiều dọc của $n$ khoản vay LIBOR kỳ hạn (số 0 tài chính).
- **Mathematical Value:** Vì mỗi khoản vay thành phần $V_i$ có giá trị bằng 0 tại reset date, tổng giá trị của FRN cũng bằng 0 (khi xét phần chênh lệch so với mệnh giá):
$$\text{Value}_t[FRN] = V^1_t + V^2_t + \dots + V^n_t = 0$$
- **Insight:** Cách tiếp cận này giải thích tại sao FRN LIBOR-flat không có rủi ro lãi suất (volatility = 0) tại các điểm reset.

### Between Resets
Price fluctuations occur only when market rates move *between* reset dates (creating a temporary mismatch between the fixed coupon and current rates) or if the issuer's credit risk $(\mu)$ changes. [[During_Fixed_Income_Ch18.md#page=171-172]]

## Strategic Functions: The Banking Match

- **Liability Hedging:** Retail deposits are "sticky" but sensitive to interbank rates. By holding FRNs, a bank ensures that its interest income increases exactly when its deposit funding costs rise, protecting the Net Interest Margin (NIM). [[During_Fixed_Income_Ch18.md#page=169]]
- **Liquidity:** For retail investors, FRNs serve as a more liquid alternative to bank term deposits, as they can be sold in the secondary market at any time without maturity penalties. [[During_Fixed_Income_Ch18.md#page=170]]

## Evidence / Source Anchors

- Strategic role of FRNs in banking treasury operations: [[During_Fixed_Income_Ch18.md#page=169]]
- Mathematical proof of the Par Value Property via induction: [[During_Fixed_Income_Ch18.md#page=171]]
- Analysis of price stability vs. credit risk and central bank surprises: [[During_Fixed_Income_Ch18.md#page=171-172]]
- Comparison with term deposits for retail investors: [[During_Fixed_Income_Ch18.md#page=170]]

## Related

- [[FRN_Coupon_Reset_Mechanics]] — Details on T-2 lags and In-arrears structures.
- [[Discount_Margin_Mechanism]] — How to value FRNs when they don't trade at Par.
- [[CMS_And_CMT_Floaters]] — Structured variants that break the Par Value Property.
- [[FRN_Implicit_Coupon_Floor]] — Why coupons rarely turn negative.
- [[Overnight_Index_Rates_FRN_Compounding]] — Modern implementation in post-Libor markets.
