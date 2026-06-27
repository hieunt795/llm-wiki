---
title: Discounting
aliases:
- Bill Discounting
- Rediscounting
- Origin of the Discount
type: mechanism
tags:
- banking
- credit
- history
- monetary-policy
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch02.md"
thesis: Discounting is the foundational process of bank credit where a lender purchases
  a future payment obligation (like a bill of exchange) for an immediate cash payment
  that is lower than the obligation's face value.
source_refs:
- file: Fixed_Income_Alexander_During_Ch02.md
  page: 30
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

Discounting is one of the oldest forms of banking and the etymological origin of the word **"Discount"** in finance. It represents the transformation of a commercial obligation (which lacks legal tender status) into immediate, liquid cash. Alexander Düring explains that this mechanism is not only a commercial tool but a primary lever through which central banks historically injected liquidity into the entire financial system.

## Mechanism

The process of discounting involves a trade-off between certain present value and uncertain future value.

### 1. The Commercial Discount
A trader who holds an accepted **Bill of Exchange** (payable in, say, 90 days) can sell that bill to a banker.
- **The Payment:** The banker pays an immediate cash amount that is lower than the face value of the bill.
- **The Profit:** The difference between the face value and the cash paid is the banker's return for the risk and the time-value of the money.
- **The Formula:** The ratio between the two is the **Discount Factor**.
$$\text{Discount Factor} = \frac{\text{Cash Payment}}{\text{Face Value}}$$
[[Fixed_Income_Alexander_During_Ch02.md#page=30]]

### 2. Rediscounting
A bank that has already discounted a bill may find itself needing liquidity. It can re-sell that same bill to another bank (or the central bank). This is known as **Rediscounting**.
- **Systemic Role:** Historically, this was the primary way central banks provided liquidity to the market. By standing ready to rediscount bills from commercial banks, the central bank acted as the ultimate liquidity provider. [[Fixed_Income_Alexander_During_Ch02.md#page=30]]

### Boundaries / Conditions

### 1. Motive for Discounting
The primary motivation for a trader to accept a discount (and thus lose some value) is the **legal tender problem**. A merchant cannot force their suppliers to accept a bill of exchange as payment for debts. By discounting the bill with a bank, the merchant converts a "non-legal tender" asset into "legal tender" cash (or bank deposits) that is universally accepted. [[Fixed_Income_Alexander_During_Ch02.md#page=30]]

### 2. Risk Assumption
When a banker discounts a bill, they assume the credit risk of the drawer. To protect themselves, they often require the bill to be a **Banker's Acceptance** or rely on the redress rights provided by the previous endorsers. [[Fixed_Income_Alexander_During_Ch02.md#page=29-30]]

## Evidence / Source Anchors

- Definition of discounting as one of the oldest forms of bank credit: [[Fixed_Income_Alexander_During_Ch02.md#page=30]]
- Equation (4.2) for the Discount Factor: [[Fixed_Income_Alexander_During_Ch02.md#page=30]]
- Explanation of rediscounting and its role in central bank operations: [[Fixed_Income_Alexander_During_Ch02.md#page=30]]
- Discussion on converting non-legal tender bills into legal tender: [[Fixed_Income_Alexander_During_Ch02.md#page=30]]

## Related

- [[Bills_Of_Exchange]] — The primary asset being discounted.
- [[Trade_Credit]] — The commercial origin of the obligations that require discounting.
- [[Bank_Money_Creation]] — Discounting is a primary event that triggers the creation of a new bank deposit.
- [[Liquidity_Operations]] — Modern central bank operations (like Repo) are the spiritual and technical successors to historical rediscounting.
- [[Yield_Curve_Representations]] — Where the "Discount Factor" ($Df(t)$) is used as a fundamental building block for curve construction.
