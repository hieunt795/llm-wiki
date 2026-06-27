---
title: Collateral Transformation and TSLF
aliases:
- Collateral Swap
- Collateral Upgrade
- Term Securities Lending Facility
- TSLF
- Máy giặt tài sản
type: mechanism
tags:
- monetary-policy
- repo
- liquidity
- collateral
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch15.md
thesis: Collateral transformation is a multi-party repo sequence (collateral swap)
  used to upgrade illiquid or lower-quality assets into high-quality liquid assets
  (HQLA) to facilitate interbank funding during periods of market stress.
source_refs:
- file: During_Fixed_Income_Ch15.md
  page: 128
- file: During_Fixed_Income_Ch15.md
  page: 129
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

During financial crises, the primary bottleneck to liquidity is often not a lack of cash, but a lack of **acceptable collateral**. "Pristine" assets (like Treasuries or Bunds) become hoarded, while lower-quality assets (MBS, corporate bonds) are rejected by lenders. Alexander Düring explains that participants use **Collateral Swaps** to bridge this gap, a process that can be either market-driven or central bank-supported. [[During_Fixed_Income_Ch15.md#page=128]]

## Mechanism: The Collateral Swap

A collateral transformation involves a sequence of two or more transactions:
1.  **Party A** (holding low-quality asset X) wants cash from **Party B**.
2.  **Party B** will only accept high-quality asset Y.
3.  **The Swap:** Party A enters a collateral swap with **Party C** (e.g., a large asset manager). Party A gives X and a fee to Party C in exchange for Y.
4.  **The Funding:** Party A now gives Y to Party B to receive cash.
- **The Result:** Asset Y has been "borrowed" to unlock cash that was previously trapped by the illiquidity of asset X. [[During_Fixed_Income_Ch15.md#page=129]]

## Case Study: The Fed's TSLF (2009)

The **Term Securities Lending Facility (TSLF)** was the archetypal central bank implementation of collateral transformation.

- **Objective:** To improve the redistribution of cash between private sector entities during the 2008-2009 freeze.
- **The Operation:** Primary dealers were allowed to borrow US Treasury securities (Y) from the Fed's SOMA portfolio.
- **The Collateral:** In exchange, they posted investment-grade corporate and mortgage bonds (X) to the Fed.
- **The Impact:** By acting as the "ultimate swapper," the Fed increased the aggregate quality of the collateral available for private sector repos, effectively unclogging the interbank funding plumbing. [[During_Fixed_Income_Ch15.md#page=129]]

## Evidence / Source Anchors

- Definition of collateral transformation as a collateral swap for the purpose of upgrading assets: [[During_Fixed_Income_Ch15.md#page=128]]
- Detailed three-party diagram logic for collateral transformation: [[During_Fixed_Income_Ch15.md#page=129]]
- Analysis of the Fed's TSLF as a tool for redistributing cash via collateral upgrades: [[During_Fixed_Income_Ch15.md#page=129]]
- Rationale for large asset managers acting as the private sector supply for collateral swaps (earning lending fees): [[During_Fixed_Income_Ch15.md#page=129]]

## Related

- [[Repurchase_Agreement_Repo_Market_Structure]] — The underlying market for these swaps.
- [[Central_Bank_Collateral_Frameworks]] — The rules that determine what the Fed/ECB will accept in these facilities.
- [[Lender_Of_Last_Resort]] — TSLF is a "Collateral Lender of Last Resort" function.
- [[General_Collateral_Vs_Special]] — Why Party C is willing to lend Y (to capture fees).
