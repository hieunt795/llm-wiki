---
title: Soft Bullet and Conditional Pass-Through
aliases:
- Soft Bullet
- Conditional Pass-Through
- CPT
- Maturity Extension Clause
- Rating Arbitrage (Covered Bonds)
type: mechanism
tags:
- covered-bonds
- risk-management
- product-structuring
- credit-rating
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch26.md
thesis: Soft bullet and conditional pass-through structures are maturity extension
  mechanisms in covered bonds designed to mitigate issuer liquidity risk and defend
  credit ratings by shifting the timing risk of redemption from the bank to the investor.
source_refs:
- file: During_Fixed_Income_Ch26.md
  page: 277
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The 2008 financial crisis exposed a critical vulnerability in covered bonds: while the assets in the cover pool might be safe, they are often illiquid. If a bank defaults, the pool administrator may struggle to sell mortgages fast enough to meet a large "bullet" principal repayment. Alexander Düring explains that banks responded by creating **Soft Bullet** and **Conditional Pass-Through (CPT)** structures. These should be recognized as a form of **Rating Arbitrage**: by "softening" the issuer's obligation to pay on time, they artificially improve credit metrics while creating significant cashflow uncertainty for investors. [[During_Fixed_Income_Ch26.md#page=277]]

## Mechanism: The Timing Pivot

### 1. Soft Bullet Bonds
- **Mechanism:** The bond has a scheduled maturity date. However, if the issuer (or the pool) cannot fund the redemption, the maturity is automatically extended—typically by one year.
- **The Buffer:** This gives the administrator extra time to liquidate assets or find alternative funding without triggering a terminal default of the bond structure. [[During_Fixed_Income_Ch26.md#page=277]]

### 2. Conditional Pass-Through (CPT)
- **Mechanism:** A more extreme version where the entire redemption schedule becomes "conditional." 
- **The Trigger:** If the issuing bank defaults and the cover pool cannot meet the original bullet, the bond converts into a pass-through instrument.
- **The Result:** Investors receive principal payments only as and when the underlying mortgages are repaid or sold. This can extend the maturity by several years (e.g., +5 to 30 years). [[During_Fixed_Income_Ch26.md#page=277]]

## Strategic Implications: Rating Arbitrage

Düring argues that these features are primarily designed to satisfy **Rating Agency** criteria.
- **Default Definition:** Rating agencies typically define default as a failure to pay interest or principal *on the legal due date*. By making the maturity date "conditional," the bank ensures it technically hasn't defaulted even if it misses the originally intended payment.
- **The Cost:** For investors, these features transform a predictable fixed-income instrument into a **Liquidity Risk** product. Investors must demand higher yields to compensate for the "uncertainty about future cash flow timing." [[During_Fixed_Income_Ch26.md#page=277]]

## Evidence / Source Anchors

- Identification of Soft Bullet and CPT as post-crisis innovations for managing cashflow mismatches: [[During_Fixed_Income_Ch26.md#page=277]]
- Analysis of these structures as forms of "Credit Rating Arbitrage": [[During_Fixed_Income_Ch26.md#page=277]]
- Description of the maturity extension mechanics (conditional on incoming cashflows): [[During_Fixed_Income_Ch26.md#page=277]]
- Discussion on the resulting investor uncertainty regarding cashflow timing: [[During_Fixed_Income_Ch26.md#page=277]]

## Related

- [[Covered_Bonds]] — The instrument that embeds these features.
- [[Liquidity_Risk_Management]] — The bank-side driver for these structures.
- [[Macaulay_Duration]] — How maturity extensions violently alter the risk profile.
- [[Securitization_And_Asset_Based_Finance_ABF]] — The origin of the pass-through logic.
- [[Bond_Clauses_And_Covenants]]
- [[Cover_Pool_And_Overcollateralisation]]
- [[Exchange_Rate_Pass_Through]]
- [[Bid_Ask_Bounce]]
- [[Bond_Index_Principles]]
- [[Dynamic_Replication_Methods]]
- [[Herstatt_Risk]]
- [[Liquidity_Measurement_Taxonomy]]
- [[Margining]]
- [[Market_Depth_Vs_Breadth]]
- [[Mean_Variance_Optimisation_Theory]]
- [[Model_Risk_And_Jumps]]
- [[Mortgage_Prepayment_Drivers]]
- [[Negative_Convexity]]
- [[FRN_Market_Risk_Duration]]
- [[LSOC_Mechanism]]
- [[Margin_Procyclicality]]
- [[Portfolio_Rebalancing_Strategies]]
- [[Portfolio_Volatility_MultiFactor]]
- [[Yield_Curve_Trading_Strategies]]
- [[Agency_Vs_Principal_Clearing_Models]]
- [[Bank_Deposit_Types]]
- [[Bond_Cashflow_Structural_Typologies]]
- [[Floating_Rate_Notes_FRN]]
- [[Merchant_Banking_Origin]]
- [[Risk_Weighted_Assets]]
- [[Systemic_Risk_Taxonomy]]
- [[ABS_Tranching_And_Default_Risk]]
- [[asset_encumbrance_and_lgd]]
- [[Banking_Separation_And_Ring_Fencing]]
