---
title: Prepayment Risk Tranching and PACs
aliases:
- Planned Amortisation Certificates
- PACs
- Prepayment Tranching
- Duration Protection
- Tranching thanh toán sớm
type: convention
tags:
- abs
- rmbs
- fixed-income
- conventions
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch27.md
thesis: Prepayment risk tranching is a structural methodology that partitions the
  timing uncertainty of cashflows into distinct bond classes, utilizing Planned Amortisation
  Certificates (PACs) to provide duration certainty to senior investors by diverting
  cashflow volatility to support tranches.
source_refs:
- file: During_Fixed_Income_Ch27.md
  page: 287
- file: During_Fixed_Income_Ch27.md
  page: 288
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

While standard tranching addresses credit risk, **Prepayment Risk Tranching** addresses the uncertainty of time. Alexander Düring explains that most ABS do not have bullet repayment schedules; they amortize as the underlying loans are repaid. For institutional investors (like pension funds) who require specific duration targets, the unpredictability of these repayments is a major risk. **PACs (Planned Amortisation Certificates)** were designed to solve this by creating a synthetic "bullet-like" experience within an amortizing pool. [[During_Fixed_Income_Ch27.md#page=287-288]]

## Mechanism: The Duration Sluice

In a standard amortizing structure, principal is distributed to tranches as it is received. Prepayment tranching introduces a non-proportional ruleset:

### 1. PAC Tranches (The Protected Class)
- **Mechanism:** A PAC bond follows a pre-defined amortization schedule. As long as the underlying pool's prepayment speed stays within a specified range (the **PAC Band**), the bondholder receives exactly the planned principal amount.
- **The Benefit:** Provides high duration certainty, making the ABS behave more like a standard bullet bond. [[During_Fixed_Income_Ch27.md#page=288]]

### 2. Support (Companion) Tranches
- **Mechanism:** To protect the PAC, these tranches act as a buffer.
- **In High Prepayment:** If the pool pays back too fast, the excess principal is diverted to the support tranches first, "filling" them up before it can affect the PAC.
- **In Low Prepayment:** If the pool pays back slowly, the support tranches give up their share of principal to ensure the PAC schedule is met.
- **The Cost:** Support tranches inherit extreme duration volatility. If prepayments surge, their duration collapses (Contraction risk). If prepayments stall, their duration extends massively (Extension risk). [[During_Fixed_Income_Ch28.md#page=288]]

## Strategic Implications: The Complexity Premium

Düring warns that more complex tranching structures—while suiting specific investor needs—require more sophisticated valuation models.
- **The Liquidity Drain:** Creating bespoke duration tranches can make the individual bond lines less liquid.
- **Model Uncertainty:** Investors demand higher risk premia to compensate for the uncertainty about the appropriate parameters for these prepayment models. Often, a more straightforward structure results in a lower overall funding cost for the originator. [[During_Fixed_Income_Ch27.md#page=288]]

## Evidence / Source Anchors

- Definition of PACs as tranches protected from prepayments via planned amortization: [[During_Fixed_Income_Ch27.md#page=288]]
- Analysis of prepayment risk being distributed like default risk within the structure: [[During_Fixed_Income_Ch27.md#page=288]]
- Description of the trade-off between tailored seniority and higher complexity-driven spreads: [[During_Fixed_Income_Ch27.md#page=288]]
- Contrast between bullet repayment bonds and amortizing ABS structures: [[During_Fixed_Income_Ch27.md#page=287]]

## Related

- [[ABS_Tranching_And_Default_Risk]] — The parallel credit-risk version of this mechanism.
- [[Residential_Mortgage_Backed_Securities_RMBS]] — The primary asset class using PACs.
- [[Macaulay_Duration]] — The metric PACs are designed to stabilize.
- [[Mortgage_Prepayment_Drivers]] — The economic factors that create the risk being tranched.
