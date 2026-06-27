---
title: Repo Operations
aliases:
- Lombard Lending
- Repurchase Agreements (Central Bank)
- Reverse Repo
- Collateralised Lending
type: mechanism
tags:
- central-banking
- monetary-policy
- liquidity
- repo
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch08.md
thesis: Repo operations are the modern implementation of collateralized central bank
  lending, where liquidity is provided or absorbed by decoupling the maturity of the
  cash impact from the maturity of the underlying security.
source_refs:
- file: During_Fixed_Income_Ch08.md
  page: 51
- file: During_Fixed_Income_Ch08.md
  page: 52
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

The **Repo** is the workhorse of modern central bank operational frameworks, particularly for the ECB and the Bank of Japan. By utilizing a "Sale and Repurchase" agreement, the central bank can provide or absorb massive amounts of liquidity without assuming the long-term price risk associated with outright [[Open_Market_Operations]]. Alexander Düring explains that this mechanism is the direct technical successor to the historical **Lombard lending**. [[During_Fixed_Income_Ch08.md#page=51]]

## Mechanism

A central bank repo consists of a simultaneous sale of a security for cash and an agreement to repurchase that security at a future date for a specified price.

### 1. From Lombard to Repo
Historically, central banks provided "Lombard loans"—advancing cash against securities physically posted as a pledge. Modern frameworks use the **Repurchase Agreement** structure, which mimics the economic effect of a loan but utilizes the legal efficiency of an outright securities transfer. [[During_Fixed_Income_Ch08.md#page=51]]

### 2. The Decoupling Advantage
Repo operations allow the central bank to provide short-term liquidity (e.g., 7 days) using long-term assets (e.g., a 10-year bond) as collateral.
- **In OMOs:** The liquidity impact is tied to the central bank's discretion to resell the asset.
- **In Repos:** The liquidity impact is fixed at the start. The cash is injected on Day 1 and automatically pulled back when the repo matures. [[During_Fixed_Income_Ch08.md#page=52]]

### 3. Directionality
- **Liquidity Providing (Repo):** The central bank buys the security and provides cash.
- **Liquidity Absorbing (Reverse Repo):** The central bank sells a security and receives cash, effectively "locking up" private bank reserves. [[During_Fixed_Income_Ch08.md#page=52]]

## Boundaries / Conditions: Moral Hazard and Price Risk

### 1. Collateral and Haircuts
Central banks strictly require high-quality collateral to prevent **Moral Hazard**. Lending without security is forbidden as it would allow banks to "socialise" losses. The central bank applies "haircuts" to protect against price volatility of the collateral during the repo period. [[During_Fixed_Income_Ch08.md#page=51]]

### 2. Insulation from Price Risk
Unlike OMOs, the central bank is insulated from the price risk of the underlying security in a repo. Since the repurchase price is fixed at the start, any decline in the market value of the bond during the 7-day period is borne by the commercial bank, not the central bank. [[During_Fixed_Income_Ch08.md#page=52]]

### 3. Liquidity Limits
The decoupling of maturity can only be taken as far as the underlying repo markets are liquid, which typically extends only to horizons of a few months. [[During_Fixed_Income_Ch08.md#page=52]]

## Evidence / Source Anchors

- Definition of repo as modern Lombard lending: [[During_Fixed_Income_Ch08.md#page=51]]
- Explanation of the decoupling of maturity and the fixing of liquidity impact: [[During_Fixed_Income_Ch08.md#page=52]]
- Analysis of collateral necessity and moral hazard: [[During_Fixed_Income_Ch08.md#page=51]]
- Note on the directionality of operations: [[During_Fixed_Income_Ch08.md#page=52]]
- Comparison with OMO price risk: [[During_Fixed_Income_Ch08.md#page=52]]

## Related

- [[Base_Money]] — The asset provided or absorbed via repo.
- [[Open_Market_Operations]] — The "Outright" alternative where ownership is permanent.
- [[Collateral_Haircut]] — The technical protection used in repo.
- [[Repurchase_Agreement_Repo_Market_Structure]] — The broader market version of this mechanism.
- [[Lender_Of_Last_Resort]] — Often implemented via standing repo facilities.
- [[Open_Market_Operations_And_Instruments]]
- [[Central_Bank_Liquidity_Provision_Mechanics]]
