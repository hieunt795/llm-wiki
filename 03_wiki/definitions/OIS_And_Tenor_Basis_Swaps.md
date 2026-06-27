---
title: OIS and Tenor Basis Swaps
aliases:
- OIS Discounting
- Tenor Basis
- Basis Swap
type: mechanism
tags:
- derivatives
- swaps
- benchmarks
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Fixed_Income_Alexander_During_Ch29.md
thesis: OIS Discounting is the modern market standard where all future swap cash flows
  are discounted using the risk-free overnight rate (e.g., €STR, SOFR) rather than
  the term LIBOR rate, reflecting the collateralised nature of the interbank market.
source_refs:
- file: Fixed_Income_Alexander_During_Ch29.md
  page: 324
- file: Fixed_Income_Alexander_During_Ch29.md
  page: 325
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

Post-2008, the "one-curve" world collapsed. Markets now distinguish between the **projection curve** (the rate being received/paid) and the **discount curve** (the risk-free rate used for PV). The spread between different indices is traded via **Basis Swaps**.

## Mechanism

### 1. OIS (Overnight Index Swap)
A swap where one party pays a fixed rate and the other pays a compounded overnight rate (e.g., EONIA/€STR).
- **Risk-Free Proxy:** OIS rates are considered the closest proxy to a risk-free rate because they involve no term credit risk (only overnight risk).
- **Discounting:** All swap valuations (including LIBOR-linked swaps) now use the OIS curve for discounting to reflect that the trades are collateralised daily at the overnight rate.

### 2. Tenor Basis Swaps
A swap where two floating rates of different tenors are exchanged (e.g., 3M LIBOR vs. 6M LIBOR).
- **Tenor Basis:** The spread between these rates exists because 6M lending carries more credit and liquidity risk than two consecutive 3M loans.
- **Pricing:** The market quotes the spread added to one of the legs (usually the shorter tenor) to make the swap's PV equal to zero.

### Boundaries / Conditions

### Multi-Curve Framework
A modern valuation system must simultaneously maintain:
- **The OIS Curve:** For discounting.
- **LIBOR/Term Curves (3M, 6M, etc.):** For projecting floating leg cash flows.
The spread between these curves (the **LOIS spread**) is a key indicator of systemic banking stress.

## Evidence / Source Anchors

- Transition to OIS discounting and collateralisation: [[Fixed_Income_Alexander_During_Ch29.md#page=324]]
- Definition of tenor basis swaps (e.g., 3M vs 6M): [[Fixed_Income_Alexander_During_Ch29.md#page=325]]
- The role of basis swaps in managing bank asset-liability mismatches: [[Fixed_Income_Alexander_During_Ch17.md#page=170]]

## Related

- [[Interest_Rate_Swap_Plain_Vanilla]] — The base swap instrument.
- [[Interest_Rate_Benchmarks]] — €STR, SOFR, and the LIBOR transition.
- [[Central_Counterparty_CCP_Clearing_Waterfall]] — Why swaps are now low-risk "cleared" instruments.
- [[Credit_Default_Swaps_CDS]]
- [[Basis_Trade_Mechanics]]
- [[Cross_Currency_Basis]]
- [[Futures_Basis_And_Implied_Repo_Rate]]
