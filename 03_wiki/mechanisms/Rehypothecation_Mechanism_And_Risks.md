---
title: Rehypothecation Mechanism and Risks
aliases:
- Rehypothecation
- Collateral Reuse
- Collateral Chaining
- Tái thế chấp
type: mechanism
tags:
- money-market
- repo
- liquidity
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch15.md
thesis: Rehypothecation is the reuse of collateral received in a repo transaction
  for a subsequent trade, creating a complex 'collateral chain' that increases market
  liquidity but introduces significant operational risk and potential systemic freezes.
source_refs:
- file: During_Fixed_Income_Ch15.md
  page: 130
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Collateral is the lifeblood of the modern financial system. **Rehypothecation** allows a single security to support multiple transactions as it moves through the interbank market. Alexander Düring explains that while this process is vital for market efficiency, it creates opaque, interconnected dependencies where the failure of one distant participant can freeze the assets of counterparties who are not even aware of their existence. [[During_Fixed_Income_Ch15.md#page=130]]

## Mechanism: The Collateral Chain

A rehypothecation chain is formed when Party B, having received collateral from Party A in a repo, uses that same collateral for another repo with Party D, and so on.

### 1. Liquidity Multiplication
Rehypothecation increases the effective "velocity" of collateral. A single JGB or Treasury bond can potentially back five or six different cash loans simultaneously. This lowers the aggregate cost of funding for the entire market. [[During_Fixed_Income_Ch15.md#page=130]]

### 2. The Chain Paradox
An entity can be the third link in one chain (started at A) but the second link in another (started at C). Because collateral is fungible, it is often impossible for the original owners (A and C) to know how many links exist in their specific security's chain or who the terminal holders are. [[During_Fixed_Income_Ch15.md#page=130]]

## Strategic Risks: The Liquidity Freeze

The primary risk of rehypothecation is not credit risk (as the trades are collateralized) but **Operational/Liquidity Risk**.

- **The Failure Logic:** If Party F at the end of a chain fails to return the security on time, Party E cannot return it to Party D. The failure propagates all the way back to the start of the chain.
- **Systemic Fragility:** In a crisis, the inability to "unlock" collateral from a defaulted chain causes a **Liquidity Freeze**. Participants find themselves solvent but unable to fulfill their own delivery obligations, creating a self-accelerating cycle of settlement fails. [[During_Fixed_Income_Ch15.md#page=130]]

## Boundaries / Conditions: Regulatory Caps
Due to the risks observed in 2008 (notably the Lehman Brothers collapse), regulators now seek to limit the length of rehypothecation chains. However, tracking these chains requires massive data processing because beneficial ownership is often masked by the dematerialized book-entry system. [[During_Fixed_Income_Ch14.md#page=130]]

## Evidence / Source Anchors

- Definition of rehypothecation as the reuse of collateral: [[During_Fixed_Income_Ch15.md#page=130]]
- Analysis of how a single failure (e.g., Party F) propagates back through the chain (domino effect): [[During_Fixed_Income_Ch15.md#page=130]]
- Discussion on the opacity of chains and the difficulty for original suppliers (A and C) to track their assets: [[During_Fixed_Income_Ch15.md#page=130]]
- Identification of rehypothecation risk as a liquidity freeze rather than simple credit default: [[During_Fixed_Income_Ch15.md#page=130]]

## Related

- [[Repurchase_Agreement_Repo_Market_Structure]] — The market that enables rehypothecation.
- [[Settlement_Fails_And_Incentives]] — The consequence of a break in the rehypothecation chain.
- [[Global_Note_Dematerialization]] — The technical system that masks the beneficial ownership tracking.
- [[Collateral_Transformation_And_TSLF]] — Upgrading collateral to make it eligible for more chains.
