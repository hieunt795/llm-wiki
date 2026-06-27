---
title: Settlement Fails and Incentives
aliases:
- Settlement Fail
- Fail to Deliver
- Buy-in Procedure
- Fails Charge
- CSDR
type: mechanism
tags:
- market-infrastructure
- settlement
- repo
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch12.md
thesis: A settlement fail—the failure of a seller to deliver a security—triggers a
  complex set of economic incentives and disciplinary measures that vary significantly
  depending on the prevailing interest rate environment.
source_refs:
- file: During_Fixed_Income_Ch12.md
  page: 95
- file: During_Fixed_Income_Ch12.md
  page: 96
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

In the principle of *dictum meum pactum* (my word is my bond), a settlement fail is a serious violation, technically an event of default. However, due to clerical errors and liquidity frictions, "fails" are common and usually managed through economic penalties rather than legal action. The core mechanism for discouraging fails is to ensure the failing party suffers an economic loss greater than the cost of obtaining the security. [[During_Fixed_Income_Ch12.md#page=95]]

## Mechanism: The Economic Incentive of a Fail

When a fail occurs, the economic status of the trade stands still. This creates an implicit loan:
- **The Process:** The seller keeps the security, but the buyer keeps the cash.
- **The Result:** The seller effectively borrows cash from the buyer at **0% interest**.
- **The Disincentive:** In a high-interest-rate environment, losing the ability to earn interest on the expected cash is a significant penalty. [[During_Fixed_Income_Ch12.md#page=95]]

### The Failure of the 0% Penalty
This basic disincentive fails in two scenarios:
1. **Low/Negative Interest Rates:** If rates are 0% or negative, the seller suffers no loss (or even gains) by failing to deliver.
2. **Special Collateral:** If a bond is trading "Special" (e.g., at -5% repo rate), a seller would rather fail and "borrow" the security at 0% than pay the market rate to source it. [[During_Fixed_Income_Ch12.md#page=95]]

## Disciplinary Measures

To counter these failures, markets have introduced explicit penalties:

### 1. Fails Charges
- **US Market:** A flat 3% fee (introduced in 2009) for failing to deliver Treasuries.
- **European Market:** Charges that reflect the actual cost of sourcing the security. [[During_Fixed_Income_Ch12.md#page=95]]

### 2. Mandatory Buy-ins
- **Mechanism:** The buyer (or a clearing agent) buys the security in the open market and charges the cost to the failing seller.
- **Regulation:** Under the EU's **Central Securities Depositories Regulation (CSDR)**, buy-ins became mandatory for fails lasting beyond a certain period. [[During_Fixed_Income_Ch12.md#page=96]]

### 3. Curing Facilities
- **Fails Mitigation Lending:** CSDs automatically borrow the security from a pool to settle the trade (at a high cost).
- **Dollar Rolls/Coupon Swaps:** Used in the US MBS market to manage production delays. [[During_Fixed_Income_Ch12.md#page=95-96]]

## Evidence / Source Anchors

- Analysis of the implicit 0% interest loan created by a fail: [[During_Fixed_Income_Ch12.md#page=95]]
- Rationale for fails charges in low-rate or special collateral environments: [[During_Fixed_Income_Ch12.md#page=95]]
- Introduction of the flat 3% fee in the US market: [[During_Fixed_Income_Ch12.md#page=95]]
- Description of mandatory buy-ins and the CSDR framework: [[During_Fixed_Income_Ch12.md#page=96]]
- Types of facilities to "cure" a fail (Lending, Rolls, Swaps): [[During_Fixed_Income_Ch12.md#page=95-96]]

## Related

- [[Repurchase_Agreement_Mechanism]] — Most fails originate from clerical errors in repo financing.
- [[General_Collateral_Vs_Special]] — Why "Specials" create an incentive to fail.
- [[Delivery_Versus_Payment]] — The mechanism that protects the buyer's cash during a fail.
- [[OTC_Trade_Lifecycle]] — Where a fail occurs (Step 11).
