---
title: Delivery Versus Payment (DvP)
aliases:
- Settlement Risk
- Herstatt Risk
- Escrow Clearing
type: mechanism
tags:
- market-infrastructure
- systemic-risk
- operations
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch11.md"
thesis: Delivery Versus Payment (DvP) is the foundational clearing architecture engineered
  to entirely eradicate Herstatt (Settlement) Risk, deploying trusted apex intermediaries
  to mathematically lock the exchange of securities and cash into a single, indivisible
  atomic transaction.
source_refs:
- file: Fixed_Income_Alexander_During_Ch11.md
  page: 99
created: '2026-04-16'
updated: '2026-04-16'
---

## Thesis

The paramount vulnerability in any decentralized financial market occurs during the settlement lag. In historical asynchronous markets, if Counterparty A transferred cash to Counterparty B, there existed a terrifying window where Counterparty B could suddenly declare bankruptcy before reciprocating the asset delivery. This structural asymmetry (known formally as **Herstatt Risk** or Settlement Risk) guarantees catastrophic systemic contagion. Modern clearing architectures eradicate this explicitly via **Delivery Versus Payment (DvP)**—a system that functionally binds the dual asset transfers into an indivisible atomic event.

## Mechanism

DvP operates through a trusted central intermediary (usually a Global Central Securities Depository - GCSD).
1. Both the Buyer and the Seller maintain separate ledger accounts at the trusted intermediary.
2. The Seller pipelines the security into the intermediary, and the Buyer pipelines the cash into the intermediary.
3. **The Atomic Execution:** The intermediary functions identically to an escrow provider. It definitively stalls the transaction until both accounts hold the requisite assets. The intermediary then simultaneously flips the ownership registers in a single, perfectly coordinated ledger update.
4. *Failure Condition:* If the Buyer fails to source the cash, the intermediary simply aborts the entire transaction. The security never physically leaves the Seller's custody, ensuring the Seller suffers zero principal loss (only market-movement opportunity cost).

### Boundaries / Conditions

### Cost and Rolling Settlement Cycles
The requirement to hold assets simultaneously at an apex intermediary is extremely expensive and capital-intensive. 

To mitigate the cost of continuous, real-time DvP (which forces dealers to pre-fund massive capital buffers continuously), most bond markets execute DvP inside rigid **Rolling Settlement Cycles** (e.g., $T+2$). During $T+2$, the intermediary aggregates two full days of gross trading flow, perfectly nets offsetting buy/sell obligations across thousands of counterparties, and then conducts a singular enormous batch-clearing event. This shrinks the total capital volume physically required to trigger the DvP cascade to a fraction of the gross notional traded.

## Evidence / Source Anchors

- Definition of Herstatt Risk originating from the catastrophic failure of asynchronous settlement windows: [[Fixed_Income_Alexander_During_Ch11.md#page=99]]
- Definition of the DvP escrow mechanic forcing the atomic, simultaneous transfer of cash and securities via a trusted bank: [[Fixed_Income_Alexander_During_Ch11.md#page=99]]
- The rationale for combining DvP with batch settlement cycles to harness the capital-efficiency of netted obligations: [[Fixed_Income_Alexander_During_Ch11.md#page=99]]

## Related

- [[Global_Note_Dematerialization]] — the physical architecture allowing the GCSD to perform the DvP ledger flip
- [[Real_Time_Gross_Settlement_RTGS]] — the alternative architecture executing continuous rather than batched settlement
- [[Settlement_Fails_And_Fails_Charges]] — what physically happens when the DvP execution aborts due to missing inventory
