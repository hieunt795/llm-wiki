---
title: CMT and CMS Floaters
aliases:
- CMT Floater
- CMS Floater
- Constant Maturity Treasury
- Constant Maturity Swap
- TEC10
- ISDAfix
type: mechanism
tags:
- fixed-income
- derivatives
- structured-products
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch18.md
thesis: CMT and CMS floaters are structured FRNs where the coupon is linked to a long-term
  interest rate (like 10Y yields) rather than standard short-term benchmarks, introducing
  significant convexity risk and basis risk relative to their hedging instruments.
source_refs:
- file: During_Fixed_Income_Ch18.md
  page: 174
- file: During_Fixed_Income_Ch18.md
  page: 175
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 5510-5589
  section: "Chapter 6.6: Constant-Maturity Products (CMS Swaps, Pricing, Applications)"
created: '2026-04-13'
updated: '2026-05-07'
---

## Thesis

Standard FRNs are "natural" instruments because their coupons track the same short-term rates used to discount them, keeping their prices near Par. **CMT (Constant Maturity Treasury)** and **CMS (Constant Maturity Swap)** floaters break this symmetry. Alexander Düring bóc tách rủi ro của các cấu trúc này: vì coupon phụ thuộc vào lãi suất dài hạn nhưng việc chiết khấu phụ thuộc vào lãi suất ngắn hạn, các trái phiếu này có độ nhạy rủi ro (Convexity) cực kỳ phức tạp. [[During_Fixed_Income_Ch18.md#page=174]]

## Mechanism: Long-Term Indexing

### 1. CMT (Constant Maturity Treasury)
- **Concept:** Coupons are linked to the yield of government bonds at a fixed maturity (e.g., 10 years).
- **Benchmarks:** The French market uses the **TEC10** (Taux de l'Echéance Constante 10 ans), derived from primary dealer quotes. The Japanese market uses recent JGB auction results. [[During_Fixed_Income_Ch18.md#page=174]]

### 2. CMS (Constant Maturity Swap)
- **Concept:** Coupons are linked to the prevailing swap rate for a specific term.
- **Benchmarks:** Formerly known as **ISDAfix**, these are now standardized swap rate fixings provided by entities like ICE (Intercontinental Exchange). [[During_Fixed_Income_Ch18.md#page=174]]

## Strategic Risks

### 1. The Convexity Gap
Unlike standard FRNs, CMT/CMS floaters do not trade at Par on reset dates.
- **Mismatch:** A rise in long-term rates increases the expected future coupons (raising price) but also typically coincides with lower discount factors (lowering price).
- **Result:** These two effects only partially counteract each other, and the **Convexity Adjustment** required for pricing is substantial. [[During_Fixed_Income_Ch18.md#page=175]]

### 2. Basis Risk
Dealers typically hedge CMT positions using CMS structures.
- **The Reason:** Paying or receiving swaps is balance-sheet efficient compared to holding physical bonds and performing repo operations.
- **The Risk:** The hedge is exposed to the **CMS–CMT Spread** (effectively the swap spread of the government bond curve). If this spread widens unexpectedly, the hedge will fail. [[During_Fixed_Income_Ch18.md#page=175]]

## Evidence / Source Anchors

- Definition of CMT and CMS floaters as bonds linked to long-term rates: [[During_Fixed_Income_Ch18.md#page=174]]
- Identification of specific benchmarks (TEC10, ISDAfix): [[During_Fixed_Income_Ch18.md#page=174]]
- Analysis of the convexity mismatch between long-term coupons and short-term discounting: [[During_Fixed_Income_Ch18.md#page=174-175]]
- Rationale for using CMS to hedge CMT and the resulting basis risk: [[During_Fixed_Income_Ch18.md#page=175]]

## Related

- [[Floating_Rate_Notes_FRN]] — The basic structure that CMT/CMS modifies.
- [[Swap_Spread_Basis]] — The risk factor in CMT/CMS hedging.
- [[Convexity_Adjustment_CMS_And_CMT]] — Technical details on the math of the "gap."
- [[Interest_Rate_Swap_Plain_Vanilla]] — The reference instrument for CMS.
