---
title: Bond Cashflow Structural Typologies
aliases:
- Bullet vs Amortizing Bonds
- Zero-Coupon Bonds and STRIPS
- Perpetual Consols
- Bond Cashflow Anatomy
- Trái phiếu trả gốc cuối kỳ
- Trái phiếu trả góp
type: definition
tags:
- fixed-income
- product-structuring
- cashflow-mechanics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch17.md
thesis: The intrinsic valuation of a bond is dictated by its deterministic cashflow
  architecture—ranging from periodic 'Bullet' structures to 'Amortizing Annuities'
  and 'Perpetuals'—where the timing of principal repayment fundamentally alters the
  instrument's sensitivity to interest rate volatility.
source_refs:
- file: During_Fixed_Income_Ch17.md
  page: 138
- file: During_Fixed_Income_Ch17.md
  page: 139
- file: During_Fixed_Income_Ch17.md
  page: 140
- file: During_Fixed_Income_Ch17.md
  page: 141
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

At its core, a bond is a legal envelope encapsulating a predefined algorithm of future cashflows. Alexander Düring emphasizes that from an economic point of view, the cashflow structure is the most important feature because it determines the valuation approach used to price and hedge the security. While cashflows are mathematically fungible in the absence of default, they carry distinct legal statuses in insolvency: claims on principal and accrued interest take precedence over future, non-accrued coupons. [[During_Fixed_Income_Ch17.md#page=137-138]]

## Typology of Cashflow Algorithms

### 1. Bullet Bonds (Trái phiếu trả gốc cuối kỳ)
The global standard for government and corporate debt.
- **Mechanism:** Periodic coupon payments at regular intervals (annual, semi-annual, etc.) with 100% of the principal repaid at the final maturity date.
- **Accrual Adjustments:** Often feature "Long first coupon" or "Short first coupon" periods if the time between issuance and the first payment deviates from the standard interval. [[During_Fixed_Income_Ch17.md#page=139]]

### 2. Zero-Coupon Bonds (Zeros)
Pure discount instruments paying no periodic interest.
- **Mechanism:** Issued deeply below Par; the investor's return is the capital gain as the price rolls up to 100 at maturity.
- **STRIPS:** (Separate Trading of Registered Interest and Principal of Securities). Created by physically or mathematically stripping coupons from a bullet bond and trading them as standalone zeros.
- **Paradox:** A 0% coupon bond is *not* a Zero. A 0% bond retains its original coupon frequency (e.g., semi-annual) for yield calculation purposes, whereas a true Zero has no natural frequency. [[During_Fixed_Income_Ch17.md#page=139-140]]

### 3. Amortizing Annuities (Trái phiếu trả góp)
Standard for mortgages and specialized debt (e.g., Icelandic HFF bonds).
- **Mechanism:** Fixed total payments ($P$) that mix principal and interest.
- **Toán học:** $P = N_0 \frac{r}{1-(1+r)^{-n}}$
- **Back-loading:** At higher interest rates, the repayment of principal is mathematically pushed towards the end of the bond's life (back-loaded). At $r=0$, the annuity is simply equal installments of principal. [[During_Fixed_Income_Ch17.md#page=141-142]]

### 4. Perpetuals (Consols)
Infinite-maturity annuities with no scheduled principal repayment.
- **Mechanism:** Pays coupons forever. Redemption only occurs via issuer buy-backs or "Call" options.
- **History:** UK Consols (Consolidated Loans) were the archetypal perpetuals. Historically used to circumvent usury laws because the lack of a repayment date made them legally resemble equity partnerships. [[During_Fixed_Income_Ch17.md#page=140-141]]

## Evidence / Source Anchors

- Establishing the legal precedence of principal/accrued interest over future coupons: [[During_Fixed_Income_Ch17.md#page=138]]
- Definition of Long/Short first coupon periods: [[During_Fixed_Income_Ch17.md#page=139]]
- Distinction between true Zeros and 0% coupon bonds: [[During_Fixed_Income_Ch17.md#page=140]]
- Derivation of the amortizing annuity formula and the back-loading effect: [[During_Fixed_Income_Ch17.md#page=141]]
- Historical link between perpetuals and usury laws: [[During_Fixed_Income_Ch17.md#page=141]]

## Related

- [[Yield_Calculations_Variants]] — How different structures require different return measures.
- [[Bond_Risk_Modified_Duration_And_PVBP]] — Why Zeros have the highest relative interest rate risk.
- [[Clean_Vs_Dirty_Price]] — The impact of regular coupon payments on quoted prices.
- [[Amortizing_Mortgage_Mechanics]] — Direct consumer application of the annuity typology.
