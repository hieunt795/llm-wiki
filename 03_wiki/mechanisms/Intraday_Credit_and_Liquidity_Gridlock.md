---
title: Intraday Credit and Liquidity Gridlock
aliases:
- Intraday Overdraft
- Settlement Gridlock
- Transaction Ordering Risk
type: mechanism
tags:
- payments
- risk-management
- central-banking
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch05.md
thesis: Intraday credit is a facility provided by central banks allowing participants
  to temporarily overdraw their settlement accounts during a payment day, preventing
  liquidity gridlocks caused by mismatched transaction timing.
source_refs:
- file: During_Fixed_Income_Ch05.md
  page: 26
- file: During_Fixed_Income_Ch05.md
  page: 27
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

Without intraday credit, every payment participant has a rational incentive to **delay outgoing payments** and **accelerate incoming flows**. If all participants act this way, the payment system enters a **Liquidity Gridlock**, where no transactions move because everyone is waiting for funds from someone else.

## Mechanism: Transaction Ordering (Table 4.2)

The need for an overdraft is often determined purely by the **ordering** of transactions rather than the net balance. 

| Time | Action (Case A) | Balance | Action (Case B) | Balance |
|---|---|---|---|---|
| 06:00 | Initial Balance | 100 | Initial Balance | 100 |
| 09:23 | **Pay Out 200** | **-50 (Overdraft)** | Receive 100 | 200 |
| 10:01 | Receive 100 | 50 | **Pay Out 200** | **0 (No Overdraft)** |

In Case A, the participant requires an intraday overdraft to complete the 09:23 transaction. In Case B, simply by waiting for an incoming payment, they avoid the overdraft.

### Systematic Solutions
- **Central Bank Overdrafts:** Systems like **TARGET2** provide intraday overdrafts (usually collateralized) to ensure the economy's "plumbing" never stops.
- **Private Reserve Substitution:** Systems like **FedWire** (without automatic overdraft) encourage banks to hold higher cash reserve balances as a private buffer, essentially moving the liquidity provision from the CB to the private sector.

## Boundaries / Conditions: End-of-Day Finality
Intraday credit must be closed by the end of the trading day. Any remaining negative balance must be covered via:
- Regular funding operations.
- **Marginal Lending Facility** (Ceiling of the corridor).
- Interbank borrowing.

## Evidence / Source Anchors

- Example of transaction ordering effect on cash balances (Table 4.2): [[During_Fixed_Income_Ch05.md#page=26]]
- Definition of liquidity gridlock risk in payment systems: [[During_Fixed_Income_Ch05.md#page=26]]
- Contrast between TARGET2 and FedWire operational equilibriums: [[During_Fixed_Income_Ch05.md#page=28]]

## Related

- [[Payment_System_Stability_Mechanics]] — The broader mandate.
- [[Multilateral_Netting_Efficiency_Matrix]] — How the total need for credit is reduced.
- [[Lender_Of_Last_Resort_Mechanism]] — The next level of credit support.
