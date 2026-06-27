---
title: Nostro Account Settlement Mechanism
aliases:
- Nostro Account
- Correspondent Banking
- Bilateral Interbank Transfer
type: mechanism
tags:
- banking
- payments
- international-finance
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch05.md
thesis: A nostro account ('ours') is a current account held by one bank at another
  bank to facilitate bilateral interbank transfers and cross-border payments without
  the need for a central clearing agent.
source_refs:
- file: During_Fixed_Income_Ch05.md
  page: 23
- file: During_Fixed_Income_Ch05.md
  page: 24
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

Nostro accounts are the cells of the **Correspondent Banking** network. They allow Bank A to offer payment services in a jurisdiction where it has no physical presence by leveraging the balance sheet of Bank B in that region.

## Mechanism: The Transfer Chain (Figure 4.4)

When Customer C (at Bank A) pays Seller S (at Bank B):
1. **Bank A:** Reduces Customer C's deposit (liability) and reduces its **Nostro Account** balance at Bank B (asset). Bank A's balance sheet contracts.
2. **Bank B:** Reduces the Nostro balance of Bank A (liability) and increases Seller S's deposit (liability). Bank B's balance sheet size is unchanged, but its designation of liabilities shifts.

### Creation of Nostro Balances
Nostro balances are **Inside Money** created by Bank B. They can be funded by:
- Bank A taking a loan from Bank B.
- Bank A selling assets/debt to the public and depositing the proceeds at B.
- Reverse customer payments (S paying C).

## Boundaries / Conditions

### 1. Balance Sheet Cost
Nostro accounts consume balance sheet space. Banks must hold sufficient "Idle" funds to cover cumulative daily flows, which incurs an opportunity cost.

### 2. Risk Factors
- **Convertibility Risk:** The risk that Bank B fails and the Nostro balance becomes inaccessible.
- **AML/KYC Risks:** Correspondent banks often make payments without full knowledge of the underlying transaction, potentially facilitating illegal fund flows.

## Evidence / Source Anchors

- Definition of Nostro and its role in cross-border finance: [[During_Fixed_Income_Ch05.md#page=23]]
- Step-by-step impact on four balance sheets (Fig 4.4): [[During_Fixed_Income_Ch05.md#page=24]]
- Disadvantages of idle balances and correspondent banking risks: [[During_Fixed_Income_Ch05.md#page=24]]

## Related

- [[Transfer_Settlement_In_Central_Bank_Money]] — The more efficient centralized alternative.
- [[Multilateral_Netting_Efficiency_Matrix]] — How these flows are reduced.
- [[RTGS_System_Mechanics]] — How these transfers are executed in real-time.
