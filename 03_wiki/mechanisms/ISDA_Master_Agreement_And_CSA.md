---
title: ISDA Master Agreement and CSA
aliases:
- ISDA
- Master Agreement
- Credit Support Annex
- CSA
- ISDA-CSA
- Standard Settlement Instructions
type: mechanism
tags:
- derivatives
- legal-structure
- risk-management
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch30.md
thesis: The ISDA Master Agreement and its Credit Support Annex (CSA) form the standardized
  legal and collateral architecture for OTC derivatives, enabling bilateral trading
  by mitigating counterparty credit risk through daily mark-to-market margining.
source_refs:
- file: During_Fixed_Income_Ch30.md
  page: 335
- file: During_Fixed_Income_Ch30.md
  page: 336
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Derivatives are fundamentally different from securities because they are not "settled" at the time of trade; they represent an ongoing promise of future payment. Alexander Düring explains that the **ISDA Master Agreement** (from the International Swaps and Derivatives Association) is the "operating system" that allows this promise to be enforceable. By standardizing the thousands of small details (calendars, holidays, netting) into a single document, ISDA reduced the frictional cost of derivatives trading from weeks of negotiation to seconds. [[During_Fixed_Income_Ch30.md#page=335]]

## Mechanism 1: The Master Agreement

The ISDA Master is a singular contract that governs *every* derivative transaction between two parties.
- **The Efficiency:** Parties sign the Master once. Subsequent trades are concluded via a simple "Short-form Confirmation" that references the Master terms.
- **Multitude of Calendars:** Allows for bespoke tailoring. A swap between London and Athens, for instance, will automatically incorporate the combined holiday calendars of both cities to ensure payment dates never fall on a bank holiday. [[During_Fixed_Income_Ch30.md#page=336]]

## Mechanism 2: The Credit Support Annex (CSA)

The CSA is a supplement to the Master Agreement that mandates the daily exchange of collateral to offset mark-to-market changes.

### 1. Daily Margining
If a swap's value moves against a party, they must deposit collateral (cash or bonds) with the counterparty. This ensures that if the losing party defaults, the winning party already holds the assets needed to cover the loss. [[During_Fixed_Income_Ch30.md#page=335]]

### 2. Collateral Types and Preferences
- **Cash CSA:** Preferred by banks for immediate finality and ease of reinvestment.
- **Bond CSA:** Preferred by pension funds and insurance companies, who have large asset pools but limited immediate cash on hand.
- **One-sided CSA:** Historically used by some sovereign treasuries where they receive collateral when in the money but do not post it when out of the money. [[During_Fixed_Income_Ch30.md#page=335-336]]

## Strategic Implications: The Move to Clearing

The bilateral CSA has largely been superseded by **Central Clearing** (CCP) for standard swaps.
- **The Driver (xVA):** Central clearing reduces the [[Valuation_Adjustments_xVA|xVA]] costs associated with bilateral credit risk.
- **Sovereign Transition:** Even sovereigns, who previously resisted posting collateral, are moving towards central clearing to access lower market rates and comply with post-2008 systemic risk mandates. [[During_Fixed_Income_Ch30.md#page=336]]

## Evidence / Source Anchors

- Analysis of ISDA Master Agreement as the foundational operating system for OTC swaps: [[During_Fixed_Income_Ch30.md#page=335]]
- Definition of CSA as a tool for daily mark-to-market collateral protection: [[During_Fixed_Income_Ch30.md#page=335]]
- Comparison of collateral preferences (Cash vs. Bond vs. One-sided CSAs): [[During_Fixed_Income_Ch30.md#page=335-336]]
- Discussion on the role of sovereign CDS as a hedge for dealers against one-sided CSAs: [[During_Fixed_Income_Ch30.md#page=336]]
- Note on the combined holiday calendar logic for international trades: [[During_Fixed_Income_Ch30.md#page=336]]

## Related

- [[Interest_Rate_Swap_Plain_Vanilla]] — The primary instrument governed by ISDA.
- [[Central_Counterparty_CCP]] — The modern alternative to bilateral CSA.
- [[Margining_IM_Vs_VM]] — The specific collateral mechanics defined in the CSA.
- [[Valuation_Adjustments_xVA]] — The cost component that ISDA-CSA frameworks seek to minimize.
