---
title: LSOC Mechanism
aliases:
- Legally Separated Operationally Commingled
- LSOC
- Customer Margin Protection
type: concept
tags:
- risk-management
- legal-framework
- clearing-and-settlement
status: verified
confidence: 5
half_life_years: 20
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat"
provenance: Tuckman_Serrat_2022_Ch13.md
thesis: LSOC is a regulatory framework for cleared swaps that protects non-defaulting customers by ensuring their collateral is legally segregated from the collateral of other customers, even if operationally mixed at the clearing member level.
source_refs:
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 341-342
created: '2026-04-29'
updated: '2026-04-29'
---

## Mechanism: Protection vs. Efficiency

**LSOC (Legally Separated Operationally Commingled)** balances the need for operational efficiency with the requirement for robust customer protection in the Interest Rate Swap (IRS) market.

- **Legally Separated:** If a clearing member (dealer) defaults with an obligation to the CCP, the CCP **cannot** legally use the margin of the member's non-defaulting customers to cover the member's own default or the default of other customers.
- **Operationally Commingled:** For efficiency, the margin from multiple customers is mixed in a single account at the CCP.

## Contrast: The Futures Market (Fellow Customer Risk)
LSOC differs significantly from the treatment of customers in the futures market:
- **Futures Market:** If a Futures Commission Merchant (FCM) defaults, bankruptcy proceedings could make non-defaulting customer margin available to the clearinghouse.
- **Fellow Customer Risk:** This is the risk that a customer loses their collateral due to the default of another customer at the same firm. LSOC is designed specifically to eliminate this risk for cleared swaps.

## Strategic Implications
LSOC increases the creditworthiness of cleared swaps for institutional clients (pension funds, etc.) but increases the complexity of default management for the CCP, as it cannot simply grab the entire customer pool of collateral.

## Related
- [[Central_Counterparty_CCP]] — The entity holding the commingled margin.
- [[Agency_Vs_Principal_Clearing_Models]] — The context in which clients access CCPs.
- [[Bilateral_vs_Cleared_Swaps]] — The clearing structure where LSOC applies.
