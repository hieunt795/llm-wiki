---
title: "ABS Tranching and Default Risk"
aliases:
  - Tranching
  - Waterfall Priority
  - Equity Tranche
  - Mezzanine Tranche
  - Senior Tranche
  - Asset Pool Risk
  - Tranche Subordination
type: mechanism
tags:
  - abs
  - securitisation
  - risk-management
  - derivatives
status: reviewed
confidence: 4
half_life_years: 10
expert_lens: "Alexander Düring"
provenance: "Alexander Düring - Fixed Income Trading and Risk Management (2021)"
created: '2026-04-13'
updated: '2026-04-28'
thesis: "Tranching là cơ chế phân tách rủi ro của một ABS, tạo ra một hệ cấu trúc vốn (Waterfall) phân tầng giúp biến đổi một rổ tài sản rủi ro thành các lớp chứng khoán có hồ sơ lợi nhuận-rủi ro khác biệt, tương đương với các vị thế quyền chọn (Call/Straddle/Put) trên chất lượng tín dụng của rổ tài sản gốc."
source_refs:
  - file: "During_Fixed_Income_Ch27.md"
    page: 286
---

## Thesis

Because an SPV has no natural assets of its own, the credit risk of an ABS is derived entirely from the underlying asset pool. Alexander Düring explains that **Tranching** is the core strategy used to manage this risk. Instead of all investors sharing losses equally, the cashflows are prioritized into a **Waterfall**, allowing the creation of high-rated "Senior" debt from lower-rated collateral by sacrificing the more junior "Equity" and "Mezzanine" tranches. [[During_Fixed_Income_Ch27.md#page=286]]

## Mechanism: The Option-Theoretic Analogy

Düring identifies a powerful way to understand the risk profile of different tranches using lăng kính phái sinh:

### 1. Equity Tranche (First Loss)
- **Concept:** Absorbs all initial losses in the pool (the "Expected Loss").
- **Option Term:** A **Long Call Option** on the credit quality of the asset pool. It has the highest potential return but is designed to be wiped out if losses exceed the initial expectation. [[During_Fixed_Income_Ch27.md#page=286-287]]

### 2. Mezzanine Tranche
- **Concept:** Protects the senior tranches from "unexpected" losses.
- **Option Term:** A **Short Straddle**. It has the highest return volatility because its payoff is extremely sensitive to changes in the uncertainty (standard deviation) of the loss distribution. [[During_Fixed_Income_Ch27.md#page=287]]

### 3. Senior Tranche
- **Concept:** Protected by the subordination of the junior tranches. It is the last resort for loss absorption.
- **Option Term:** A **Far-out-of-the-money Short Put**. It behaves like risk-free debt under normal conditions but faces sharp "cliff-edge" risks during systemic crises. [[During_Fixed_Income_Ch27.md#page=287]]

## The Enforcement Gap

A critical difference between ABS and standard lending is the **legal status of investors**.
- **No Direct Standing:** Investors in ABS tranches have no legal basis on which to pursue individual defaulted borrowers in the pool.
- **Servicer Agency:** All recovery pressure is delegated to the **Servicer**. Bondholders are passive recipients of the servicer's efforts. If the servicer is inefficient or fails, the default risk of the pool effectively increases regardless of the asset quality. [[During_Fixed_Income_Ch27.md#page=286]]

## Evidence / Source Anchors

- Definition of Tranching as the issuance of multiple bond series with a priority waterfall: [[During_Fixed_Income_Ch27.md#page=286]]
- Mapping of tranches to specific option payoff profiles (Call/Straddle/Put): [[During_Fixed_Income_Ch27.md#page=287]]
- Analysis of the Equity tranche absorbing expected losses vs. Mezzanine absorbing uncertainty: [[During_Fixed_Income_Ch27.md#page=286-287]]
- Description of the legal barrier preventing ABS investors from pursuing defaulted borrowers directly: [[During_Fixed_Income_Ch27.md#page=286]]
- Schematic of the standard tranche structure (Figure 26.1): [[During_Fixed_Income_Ch27.md#page=287]]

## Related

- [[Securitization_And_Asset_Based_Finance_ABF]] — The broader structure.
- [[Special_Purpose_Vehicle_SPV_Architecture]] — The environment where the waterfall is implemented.
- [[Prepayment_Risk_Tranching_And_PACs]] — How timing risk is similarly partitioned.
- [[ABS_Servicer_Risk]] — The operational counterparty risk tied to enforcement.
