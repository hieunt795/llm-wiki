---
title: Cover Pool and Overcollateralisation
aliases:
- Cover Pool
- Overcollateralisation
- OC
- Asset Encumbrance
- Substitute Collateral
- Registrar
type: mechanism
tags:
- covered-bonds
- risk-management
- banking
- collateral
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Danh mục tài sản đảm bảo (Cover Pool) là động lực cốt lõi cho tính an toàn
  của trái phiếu bao phủ (covered bond), sử dụng cơ chế dư thừa tài sản đảm bảo (OC)
  làm vùng đệm chống lại sự sụt giảm giá trị tài sản, đồng thời tạo ra sự đánh đổi
  chiến lược cho tổ chức phát hành giữa việc tăng cường tín dụng và chi phí thế chấp
  tài sản đối với các chủ nợ không có bảo đảm.
source_refs:
- file: During_Fixed_Income_Ch26.md
  page: 277
created: '2026-04-13'
updated: '2026-04-22'
---

## Thesis

A covered bond is only as strong as its **Cover Pool**. Alexander Düring explains that this pool is not a static set of assets but a dynamically managed "capital centre" where the issuer is legally obligated to maintain both quality and quantity. The presence of **Overcollateralisation (OC)** provides a safety margin, but it introduces a systemic risk known as **Asset Encumbrance**, which can undermine the stability of the bank's other creditors. [[During_Fixed_Income_Ch26.md#page=277-278]]

## Mechanism: Managing the Pool

### 1. The Role of the Registrar
Every cover pool is monitored by an independent **Registrar** or trustee.
- **The Mandate:** To ensure that the volume of cover assets always suffices to cover the outstanding bonds and that the asset quality satisfies statutory standards.
- **Asset Substitution:** If an asset in the pool (e.g., a mortgage) falls into arrears, the issuer must remove it and replace it with a performing loan immediately. [[During_Fixed_Income_Ch26.md#page=277-278]]

### 2. Overcollateralisation (OC)
OC is the excess of cover assets over the nominal value of outstanding bonds.
- **Minimum OC:** Defined by law (statutory minimum).
- **Economic OC:** Issuers routinely exceed the minimum to satisfy rating agency requirements for AAA ratings.
- **The Funding Paradox:** OC is by definition funded by liabilities *other* than covered bonds (e.g., senior unsecured debt or equity), which carries a higher interest cost. [[During_Fixed_Income_Ch26.md#page=277]]

### 3. Substitute Collateral
To manage short-term cashflow mismatches (e.g., monthly mortgage payments vs. annual bond coupons), issuers use **Substitute Collateral**.
- **The Logic:** Highly liquid assets (cash or government bonds) held in the pool until they are needed for bond servicing. [[During_Fixed_Income_Ch26.md#page=277]]

## Strategic Implications: Asset Encumbrance

Asset encumbrance is the "dark side" of covered bonds.
- **The Conflict:** By pledging its best assets (and significant OC) to covered bond holders, the bank leaves fewer high-quality assets available for other creditors.
- **The Result:** In a default, recovery values for depositors and senior unsecured bondholders are significantly lower.
- **The Limit:** Regulators in some jurisdictions (notably the UK and US) severely restrict the volume of covered bond issuance to prevent excessive encumbrance from destabilizing the general banking system. [[During_Fixed_Income_Ch26.md#page=278]]

## Evidence / Source Anchors

- Definition of the cover pool as a segregated pool of assets on the issuer's balance sheet: [[During_Fixed_Income_Ch26.md#page=272]]
- Analysis of the Registrar's responsibility for asset substitution and quality maintenance: [[During_Fixed_Income_Ch26.md#page=277-278]]
- Identification of Asset Encumbrance as a risk to unsecured creditors and depositors: [[During_Fixed_Income_Ch26.md#page=278]]
- Visual representation of the balance sheet structure of a covered bond issuer (Figure 25.3): [[During_Fixed_Income_Ch26.md#page=278]]
- Discussion on the economic optimization of OC levels vs. funding costs: [[During_Fixed_Income_Ch26.md#page=278]]

## Related

- [[Covered_Bonds]] — The instrument that utilizes this mechanism.
- [[Seniority_And_Subordination]] — Why asset encumbrance matters for unsecured rankings.
- [[LTV_Ratio_In_Mortgage_Lending]] — The primary metric for cover asset quality.
- [[Margining_IM_Vs_VM]] — A parallel mechanism for collateralizing derivative exposures.
- [[Covered_Bonds_Mechanism]]
- [[Agency_Vs_Principal_Clearing_Models]]
