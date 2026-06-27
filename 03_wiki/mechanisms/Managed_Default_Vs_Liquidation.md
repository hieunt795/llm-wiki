---
title: Managed Default vs Liquidation
aliases:
- Managed Default
- Wind-down
- Reorganization
- Bankruptcy Stay
- Chapter 11 vs Chapter 7
- Consent Solicitation
- Exchange Offer
type: mechanism
tags:
- credit-risk
- restructuring
- bankruptcy
- legal-structure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch25.md
thesis: 'The resolution of defaulted debt is a choice between preservation and destruction:
  ''Managed Default'' aims to maximize recovery by restructuring the borrower as a
  going concern, while ''Liquidation'' realize assets at a discount to terminate the
  entity''s existence.'
source_refs:
- file: During_Fixed_Income_Ch25.md
  page: 260
- file: During_Fixed_Income_Ch25.md
  page: 262
- file: During_Fixed_Income_Ch25.md
  page: 263
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

When a default occurs, creditors face a critical decision: wind down the debtor immediately or allow continued operations under a new capital structure. Alexander Düring explains that the choice is driven by **Recovery Maximization**. Because companies often possess intangible assets (brand, relationships) that only have value as a "going concern," a managed default is usually the preferred outcome for large corporate and sovereign borrowers. [[During_Fixed_Income_Ch25.md#page=260]]

## Mechanism 1: Managed Default (Reorganization)

Managed default is a non-antagonistic resolution involving a temporary **Stay** (suspension of liquidation proceedings).

- **Objective:** Eventual recovery of the debtor's business so it can service reduced or rescheduled liabilities.
- **US Bankruptcy Code Archetypes:**
    - **Chapter 11:** Reorganization for private companies.
    - **Chapter 9:** Reorganization for municipalities.
- **Debtor-in-Possession (DIP):** During reorganization, the debtor can often incur new debt to cover working capital. These new lenders are granted super-seniority to incentivize liquidity provision to the distressed entity. [[During_Fixed_Income_Ch25.md#page=260-263]]

## Mechanism 2: Wind-down (Liquidation)

The final stage of existence where there is no realistic prospect of business recovery.

- **Process:** Selling all remaining assets and distributing proceeds to creditors according to [[Seniority_And_Subordination|seniority]].
- **Fire-sale Discounts:** Assets in liquidation often sell at substantial discounts because they are specialized (hard to integrate for buyers) and the process is expedited.
- **Timeline:** Can take decades for complex entities (e.g., the Herstatt Bank wind-down lasted from 1974 to 2006). [[During_Fixed_Income_Ch25.md#page=263]]

## Pre-Default Strategic Tools: Voluntary Exchanges

Issuers often attempt to avoid formal default proceedings through two mechanisms:

### 1. Consent Solicitation
The issuer asks bondholders to voluntarily accept changes to the terms (e.g., relaxing a covenant) to prevent a technical default from becoming a payment failure. [[During_Fixed_Income_Ch25.md#page=262]]

### 2. Exchange Offers
The issuer proposes swapping existing bonds for new ones with different terms (lower coupon, longer maturity). 
- **Game Theory:** These are prime examples of game theory. If a majority agrees, the liquidity of the original bonds collapses, effectively forcing "Holdout" investors to comply or hold a useless asset.
- **Rating Impact:** If the exchange results in a material reduction in the economic value of the bond, rating agencies will treat it as a **Distressed Exchange** (effectively a default). [[During_Fixed_Income_Ch25.md#page=262-263]]

## Evidence / Source Anchors

- Analysis of the incentive for managed default to preserve going-concern value: [[During_Fixed_Income_Ch25.md#page=255-256]]
- Contrast between US Chapter 11 (Managed) and Chapter 7 (Liquidation): [[During_Fixed_Income_Ch25.md#page=260]]
- Description of the 'Stay' and DIP financing protections: [[During_Fixed_Income_Ch25.md#page=263]]
- Mechanism of Consent Solicitations and Distressed Exchange Offers: [[During_Fixed_Income_Ch25.md#page=262]]
- Historical case study of the 32-year Herstatt Bank wind-down: [[During_Fixed_Income_Ch25.md#page=263]]

## Related

- [[Credit_Risk_Taxonomy]] — The events that lead to this resolution process.
- [[Seniority_And_Subordination]] — The rules of distribution within the process.
- [[Collective_Action_Clause_CAC]] — The legal tool that streamlines managed defaults.
- [[Herstatt_Risk]] — The systemic danger that originated from a messy wind-down.
