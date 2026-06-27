---
title: Intraday Overdraft
aliases:
- Intraday Credit
- Daylight Overdraft
- Transaction Ordering Paradox
type: mechanism
tags:
- banking
- liquidity
- payment-systems
- risk-management
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch02.md"
thesis: Intraday overdrafts are temporary central bank credit facilities that provide
  liquidity within RTGS systems to prevent transactional gridlock caused by the specific
  ordering of payment instructions.
source_refs:
- file: Fixed_Income_Alexander_During_Ch02.md
  page: 26
- file: Fixed_Income_Alexander_During_Ch02.md
  page: 27
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

In a Real-Time Gross Settlement ([[RTGS_Systems_Global]]) environment, the sequence in which payments are processed can determine whether a bank remains liquid or defaults on an instruction. Alexander Düring argues that without **Intraday Overdrafts**, banks face a "Game Theory" incentive to delay outgoing payments until they receive incoming ones, which can lead to systemic gridlock. Intraday credit solves this by allowing banks to temporarily dip into negative balances during the payment day.

## Mechanism

The practical necessity of an overdraft is illustrated by the **Transaction Ordering Paradox** (Table 4.2).

### 1. Case Study: Ordering Impact
Imagine a bank with an initial balance of 100 and three pending transactions: a receipt of 100, and two payments of 200 and 50.

| Sequence A (No Overdraft) | Sequence B (Overdraft Required) |
|---|---|
| 1. Starts at 100 | 1. Starts at 100 |
| 2. Receives 100 (Bal: 200) | 2. **Must pay 200** (Bal: -100) -> **Overdraft Needed** |
| 3. Pays 200 (Bal: 0) | 3. Receives 100 (Bal: 0) |
| 4. Pays 50 (Fail) | 4. Pays 50 (Fail) |

In Case B, if the bank is forced to pay before it receives, it requires an intraday overdraft to keep the system moving. Without it, the bank must delay its payment, potentially causing its counterparty (the receiver) to also delay *their* next payment, creating a chain reaction. [[Fixed_Income_Alexander_During_Ch02.md#page=27]]

### 2. Differing Global Philosophies
Central banks take different approaches to this risk:
- **TARGET2 (ECB):** Explicitly allows intraday overdrafts to counterparties. This promotes smoothness but requires the central bank to assume some intraday credit risk.
- **FedWire (USA):** Traditionally restricted or penalized overdrafts. This incentivizes banks to hold higher cash reserve holdings as a substitute for intraday credit.
- **The Trade-off:** In essence, the private sector (US banks) provides the intraday liquidity to itself via reserves, whereas in the Eurozone, the central bank provides it visibly through the system. [[Fixed_Income_Alexander_During_Ch02.md#page=28]]

### Boundaries / Conditions

### 1. End-of-Day Finality
While account balances can be negative during the day, they **must be closed** (returned to at least zero) by the end of the payment day. 
- **Recourse:** If a bank cannot close its negative balance, it must use the central bank's overnight funds-providing facilities (Lombard lending).
- **Sanctions:** Repeatedly failing to close intraday balances is seen as a sign of financial weakness and may lead to central bank sanctions or restricted system access. [[Fixed_Income_Alexander_During_Ch02.md#page=27-28]]

### 2. Monetary Policy Signal Conflict
Providing intraday credit can sometimes conflict with monetary policy signals. If a central bank wants to project a "tight" policy stance, providing "easy" intraday liquidity might be seen as contradictory. This is one reason why FedWire and TARGET2 form different "stable equilibria" with their respective operational frameworks. [[Fixed_Income_Alexander_During_Ch02.md#page=28]]

## Evidence / Source Anchors

- Rationale for overdrafts (robustness against transaction reordering): [[Fixed_Income_Alexander_During_Ch02.md#page=26]]
- Table 4.2 demonstrating the ordering paradox: [[Fixed_Income_Alexander_During_Ch02.md#page=27]]
- Comparison of TARGET2 (with overdraft) and FedWire (without): [[Fixed_Income_Alexander_During_Ch02.md#page=28]]
- Analysis of end-of-day balance requirements and sanctions: [[Fixed_Income_Alexander_During_Ch02.md#page=27-28]]

## Related

- [[RTGS_Systems_Global]] — The payment infrastructure where intraday credit is deployed.
- [[Lender_Of_Last_Resort]] — The function that covers balances that remain negative at the end of the day.
- [[Bank_Deposit_Types]] — The liabilities that these systems are used to transfer.
- [[Reserve_Ratio_Constraint]] — Higher reserve holdings are a substitute for intraday overdrafts.
- [[Herstatt_Risk]] — Overdrafts help mitigate the timing risks that lead to Herstatt-style failures.
