---
title: Interbank Netting
aliases:
- Multilateral Netting
- Bilateral Netting
- Payment Clearing
type: mechanism
tags:
- banking
- settlement
- systems
- operational-risk
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch02.md"
thesis: Interbank netting is a cooperative mechanism that reduces the volume of interbank
  credit and physical settlement required by offsetting reciprocal payment obligations
  into a single net receivable or payable.
source_refs:
- file: Fixed_Income_Alexander_During_Ch02.md
  page: 22
- file: Fixed_Income_Alexander_During_Ch02.md
  page: 23
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

The expansion of [[Bank_Money_Creation]] across multiple banks creates a massive volume of interbank payment obligations. Because deposits carry bank-specific credit risk, a transfer from Bank A to Bank B requires Bank A to provide an asset that Bank B accepts (usually central bank money). To prevent the economy from seizing up due to the limited supply of this settlement asset, banks utilize **Netting** to cancel out as many offsetting flows as possible, significantly increasing systemic efficiency while introducing new temporal risks.

## Mechanism

Netting is a joint benefit for participating banks, even those who otherwise compete fiercely for customers.

### 1. Bilateral Netting
The simplest form involving two banks (A and B).
- **Process:** Banks A and B calculate the total flow sent from A to B and from B to A over a specific period. 
- **The Offset:** Only the positive difference (the net amount) is actually transferred in central bank money. This reduces the "Interbank Credit" that would otherwise be required if every single transaction were settled gross. [[Fixed_Income_Alexander_During_Ch02.md#page=22]]

### 2. Multilateral Netting
Higher efficiency is achieved by including all banks in a network.
- **The Matrix:** A matrix of flows is established ($f_{AB}, f_{BA}, f_{AC}$, etc.). 
- **The Calculation:** 
  - **Gross Due to A ($I_A$):** The sum of all inflows from all other banks.
  - **Gross Due from A ($O_A$):** The sum of all outflows to all other banks.
  - **Net Position:** $I_A - O_A$.
- **Systemic Rule:** The sum of all net positions in a closed system must add up to zero. [[Fixed_Income_Alexander_During_Ch02.md#page=22-23]]

### 3. Historical Implementation
Historically, this was performed physically. Clerks from different banks would place paper cheques on a large central table subdivided like the netting matrix. Today, this is done digitally via central clearing houses or money-centre banks. [[Fixed_Income_Alexander_During_Ch02.md#page=22]]

### Boundaries / Conditions

### 1. The Efficiency vs. Risk Trade-off
- **Efficiency:** Netting is more effective over longer periods (e.g., 24 hours) as more offsetting flows accumulate.
- **Risk:** A longer netting period allows larger "unsettled" imbalances to build up. If a bank fails *during* the netting period but *before* the final settlement, the entire system faces the risk of unwinding, which can cause systemic collapse. [[Fixed_Income_Alexander_During_Ch02.md#page=23]]

### 2. Change of Obligor
Netting effectively facilitates a change of obligor. A customer at Bank A paying a seller at Bank B asks Bank B to accept the credit risk of Bank A. Netting reduces the amount of this specific interbank credit that must be extended. [[Fixed_Income_Alexander_During_Ch02.md#page=22]]

## Evidence / Source Anchors

- Definition of interbank credit reduction via netting: [[Fixed_Income_Alexander_During_Ch02.md#page=22]]
- Description of the Multilateral Netting Matrix (Figure 4.3): [[Fixed_Income_Alexander_During_Ch02.md#page=23]]
- Historical note on physical cheque netting tables: [[Fixed_Income_Alexander_During_Ch02.md#page=22]]
- Analysis of the netting period risk/efficiency trade-off: [[Fixed_Income_Alexander_During_Ch02.md#page=23]]

## Related

- [[Bank_Money_Creation]] — The process that generates the payment obligations being netted.
- [[Nostro_Account]] — The bilateral account used to execute the results of netting.
- [[RTGS_Systems_Global]] — The "Gross" alternative to netting, where every transaction is settled immediately without offsetting.
- [[Central_Counterparty]] — The institutional entity that usually manages multilateral netting today.
- [[Herstatt_Risk]] — The specific systemic risk that arises when netting or settlement fails between time zones.
- [[Inside_Vs_Outside_Money]] — Netting is the process of minimizing the use of "Outside Money" to settle "Inside Money" transfers.
