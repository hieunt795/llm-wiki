---
title: Seniority and Subordination
aliases:
- Debt Seniority
- Debt Subordination
- Bail-in
- CoCo Bonds
- Debt Hierarchy
- Structural Subordination
- Phân tầng nợ
type: mechanism
tags:
- credit-risk
- seniority
- banking
- product-structuring
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch25.md
thesis: Seniority and subordination define the cardinal ranking of creditor claims
  against a debtor's assets, utilizing a combination of contractual agreements, statutory
  mandates (like bank bail-ins), and structural time-weighting to dictate the order
  of capital recovery.
source_refs:
- file: During_Fixed_Income_Ch25.md
  page: 256
- file: During_Fixed_Income_Ch25.md
  page: 257
- file: During_Fixed_Income_Ch25.md
  page: 258
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

In a default situation, there are inherently insufficient assets to satisfy all claims. The **Seniority Hierarchy** determines the winners and losers in the competition for remaining value. Alexander Düring explains that subordination is not just a static ranking in a prospectus, but a dynamic and multi-jurisdictional system where legislation can override contracts (Statutory Subordination) and time can act as a silent predator (Time Subordination). [[During_Fixed_Income_Ch25.md#page=256]]

## The Subordination Matrix

### 1. Contractual Subordination (Thỏa thuận)
The most common form, explicitly stated in the debt documentation.
- **The Trade-off:** Investors accept lower seniority in exchange for higher coupon rates.
- **Stability Covenants:** Covenants usually restrict an issuer's ability to issue new debt that is senior to existing claims, ensuring the "cardinal ranking" remains stable over time. [[During_Fixed_Income_Ch25.md#page=256-257]]

### 2. Statutory Subordination (Pháp lý)
Legislation that imposes loss-sharing on specific classes of creditors, often overriding previous contractual expectations.
- **Bank Bail-ins:** Under the EU Bank Resolution Directive (TLAC/MREL), certain bank liabilities (including senior unsecured debt) can be "bailed-in"—meaning they are written down or converted to equity to absorb losses—to prevent taxpayer-funded bailouts. [[During_Fixed_Income_Ch25.md#page=257]]
- **CoCo Bonds (Contingent Convertibles):** Hybrid instruments that automatically convert to equity when a capital threshold (e.g., Tangible Equity Ratio) is breached. Düring notes the **CoCo Paradox**: conversion occurs exactly when the bank's stock price is likely collapsing, causing massive dilution and further panic. [[During_Fixed_Income_Ch25.md#page=258]]

### 3. Structural & Time Subordination
- **Time Subordination:** The risk that creditors paid earlier (short-term debt) drain assets before long-term creditors can claim them. This is mitigated by [[Credit_Risk_Taxonomy|Acceleration]] clauses. [[During_Fixed_Income_Ch25.md#page=256]]
- **ABS Structures:** In Securitization, time subordination is used *beneficially* to improve credit tiering, where principal repayments are directed to senior tranches first to reduce their Weighted Average Life (WAL). [[During_Fixed_Income_Ch25.md#page=256]]

## Strategic Implications: Joint and Several Liability

When multiple entities are liable for the same debt:
- **Several Liability (OR logic):** A default by any one borrower is a default on the instrument. The rating is driven by the **weakest link**.
- **Joint and Several Liability (AND logic):** A default occurs only if *all* borrowers default. The rating is influenced by the **strongest link**, but Düring warns of the **Burden Spillover**: defaulting members increase the financial pressure on the surviving ones, potentially causing a cascade of failures. [[During_Fixed_Income_Ch25.md#page=258]]

## Evidence / Source Anchors

- Analysis of relative seniority as a function of time, contract, and statute: [[During_Fixed_Income_Ch25.md#page=256]]
- Mechanism of PIK (Pay-in-Kind) notes creating contractual time subordination: [[During_Fixed_Income_Ch25.md#page=257]]
- Description of the EU Bail-in regime and its impact on senior unsecured debt: [[During_Fixed_Income_Ch25.md#page=257]]
- Critique of CoCo bond valuation and the equity dilution paradox: [[During_Fixed_Income_Ch25.md#page=258]]
- Boolean logic comparison of Several vs. Joint and Several liability: [[During_Fixed_Income_Ch25.md#page=258]]

## Related

- [[Credit_Risk_Taxonomy]] — The events that trigger this hierarchy.
- [[Managed_Default_Vs_Liquidation]] — The process of enforcing these rankings.
- [[Sovereign_Debt_Risk_Dynamics]] — Why seniority is a "promise" rather than a legal certainty for Chính phủ.
- [[Securitization_And_Asset_Based_Finance_ABF]] — Prime application of structural subordination.
