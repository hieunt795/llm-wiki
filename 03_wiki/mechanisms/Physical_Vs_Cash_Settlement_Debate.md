---
title: Physical vs Cash Settlement Debate
aliases:
- Settlement Finality
- Delivery Mechanism
- Benchmark Manipulation (Futures)
type: mechanism
tags:
- derivatives
- market-infrastructure
- regulation
- fraud
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch29.md
thesis: The debate between physical and cash settlement in bond futures represents
  a choice between assets-linked deterrents to price manipulation (Physical) and simplified
  operational finality prone to reference-rate gaming (Cash).
source_refs:
- file: During_Fixed_Income_Ch29.md
  page: 302
- file: During_Fixed_Income_Ch29.md
  page: 303
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Traditional exchanges (like CBOT and Eurex) primarily utilize **Physical Delivery**, requiring the transfer of actual bonds. Modern contracts and money market futures often prefer **Cash Settlement**, closing out positions with a single cash flow. Alexander Düring explains that while cash settlement is operationally "cleaner," it removes the critical link to physical scarcity that acts as a natural stabilizer against speculative bubbles and manipulation. [[During_Fixed_Income_Ch29.md#page=302]]

## Comparison Matrix

| Feature | Physical Settlement | Cash Settlement |
| :--- | :--- | :--- |
| **Deterrent** | **High:** Manipulators must accept delivery of physical assets at the inflated/deflated price. | **Low:** Participants can "exit" the contract life-cycle cleanly with cash only. |
| **Squeeze Risk** | **Present:** Vulnerable to shortages in the [[Cheapest_To_Deliver_CTD_Mechanism|CTD]] bond. | **Absent:** No physical asset is required, eliminating supply constraints. |
| **Manipulation** | Difficult to manipulate the bond market without massive capital. | **High Risk:** Prone to "gaming" the benchmark fixings (e.g., Libor scandal). |
| **Operational Cost** | **High:** Requires repo financing, custodians, and transfer of title. | **Low:** Simple bank-to-bank electronic transfer of P&L. |

[[During_Fixed_Income_Ch29.md#page=302-303]]

## Strategic Lessons: The Benchmark Trap

Düring argues that the absence of a link to a physical asset (like a deposit with a bank at LIBOR) reduces the hurdles to fraudulent behavior.
- **The Case:** During the financial crisis, traders allegedly manipulated LIBOR fixings to move cash-settled contracts in their favor. 
- **The Deterrent Failure:** Because cash settlement provided a "clean exit," there was no risk of being forced to hold a non-economic asset, making the payoff for successful manipulation much higher relative to the risk. [[During_Fixed_Income_Ch29.md#page=303]]

## Evidence / Source Anchors

- Definition of Physical vs. Cash settlement mechanisms: [[During_Fixed_Income_Ch29.md#page=301]]
- Analysis of physical settlement as a deterrent to price manipulation: [[During_Fixed_Income_Ch29.md#page=302]]
- Description of cash-settled contracts as providing a "clean exit" from the lifecycle: [[During_Fixed_Income_Ch29.md#page=302]]
- Linkage between cash settlement and the incentive to manipulate LIBOR fixings: [[During_Fixed_Income_Ch29.md#page=303]]
- Discussion on the persistence of suboptimal contract designs due to switching costs: [[During_Fixed_Income_Ch29.md#page=303]]

## Related

- [[Bond_Futures_Contract_Design]] — The base instrument categories.
- [[LIBOR_Transition_And_Benchmarks]] — Why modern cash-settled fixings are being policed more heavily.
- [[Bond_Futures_Squeeze_Dynamics]] — The primary risk specific to physical settlement.
- [[OTC_Trade_Lifecycle]] — The settlement process being simplified.
