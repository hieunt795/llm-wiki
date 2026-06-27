---
title: Settlement Fails and Cures
aliases:
- Settlement Fail
- Buy-ins
- Partial fail
- Fails charges
- Thất tín giao nhận
type: mechanism
tags:
- market-infrastructure
- settlement
- operations
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: extracted from _temp_ch11.md
thesis: A settlement fail occurs when a seller cannot deliver the required security
  on the agreed date; cures involve borrow/lend facilities, cash-and-carry extensions,
  or mandatory buy-ins.
source_refs:
- file: Fixed Income Trading and Risk Management - Alexander Düring
  page: 95
- file: Fixed Income Trading and Risk Management - Alexander Düring
  page: 96
created: '2026-04-13'
updated: '2026-04-18'
---

## Thesis

Settlement fails are a significant operational risk in bond markets, effectively turning an outright trade into an unintended 0% repo borrowing of the security. Fails are discouraged through economic penalties (**fails charges**) and bilateral relationships. Cures range from automatic lending facilities provided by CSDs to the more drastic and costly **buy-in** procedure. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=95-96]]

## Mechanism

### 1. The Nature of a Fail
- A seller fails to deliver securities to the buyer. This is technically an event of default, but rarely declared as such. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=95]]
- **Partial Fail:** The seller delivers only a portion of the transacted amount.

### 2. Disincentives and Charges
- **0% Repo Logic:** Traditionally, a fail meant the seller loses interest on the cash they didn't receive, effectively borrowing the security at 0%. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=95]]
- **Fails Charges:** In low or negative interest rate environments, a 0% rate is not a disincentive. Markets have introduced flat fees (e.g., 3% in the US) or actual cost-of-fail charges in Europe. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=95]]

### 3. Cures (Ways to Resolve a Fail)
- **Fails Mitigation Lending:** Automated facilities by CSDs to borrow for delivery (expensive). [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=95]]
- **Bilateral Repos:** O/N or T/N repos with non-standard settlement to source the bond quickly. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=96]]
- **Buy-ins:** The buyer (or clearer) buys the security in the open market and charges the failing counterparty. Mandatory under EU CSDR for long-term fails. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=96]]
- **Dollar Rolls/Coupon Swaps:** Specific to US mortgage TBA markets. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=96]]

### Boundaries / Conditions

- **Settlement Discipline:** Fails contradict the core principle of *dictum meum pactum*. High fail rates can lead to a loss of counterparty relationships. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=96]]
- **Repo Linkage:** Many fails are caused by a chain reaction: a market maker sells a bond but fails to receive it back from a repo counterparty in time. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=95]]

## Evidence / Source Anchors

- US Treasury market 3% fails charge introduction (May 2009): [[Fixed_Income_Alexander_During_Ch12.md#page=95]]
- Mandatory buy-ins under EU CSDR (as of 1 Feb 2021): [[Fixed_Income_Alexander_During_Ch12.md#page=96]]
- Economic logic of 0% repo for failing sellers: [[Fixed_Income_Alexander_During_Ch12.md#page=95]]

## Related

- [[OTC_Trade_Lifecycle]] — The process where fails are detected (Step 7).
- [[Repurchase_Agreement]] — The primary tool used to source bonds to prevent or cure fails.
- [[Delivery_Versus_Payment]] — The mechanism that protects the buyer from paying cash for a failing delivery.
