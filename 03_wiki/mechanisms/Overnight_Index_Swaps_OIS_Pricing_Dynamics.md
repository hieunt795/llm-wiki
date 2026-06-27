---
title: Overnight Index Swaps (OIS) Pricing Dynamics
aliases:
- OIS Fixed vs Floating
- Compound Overnight Benchmarks
type: mechanism
tags:
- derivatives
- money-markets
- overnight-rates
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch13.md"
thesis: The Overnight Index Swap (OIS) serves as the primary capital bridge linking
  distinct daily overnight interest benchmarks directly into macro term structures,
  functioning mathematically as a pure, collateralized exchange of a fixed forward
  rate against the geometrically compounded aggregate of realizing overnight floating
  rates.
source_refs:
- file: Fixed_Income_Alexander_During_Ch13.md
  page: 119
created: '2026-04-16'
updated: '2026-04-16'
---

## Thesis

Because the global capital markets physically lend extreme volumes of cash on an overnight secured basis, but simultaneously require 3-month and 6-month term rates to price real-world macroeconomics (e.g., mortgage resets, corporate borrowing), a synthetic bridge is mathematically required to connect the two fragmented timescales. This engineered bridge is the **Overnight Index Swap (OIS)**. By trading a locked forward fixed rate against the explicit compounding trajectory of the actual overnight rate, the OIS market seamlessly translates high-frequency, granular overnight volatility into an observable mid-term pricing profile, actively replacing the fraudulent legacy structures of the traditional LIBOR complex.

## Mechanism

### The Swap Architecture
An OIS is fundamentally an interest rate swap. 
- **The Fixed Leg:** One counterparty mathematically dictates a static, fixed interest rate (e.g., $4.25\%$) covering the entire 3-month macro term length.
- **The Floating Leg:** The opposing counterparty commits to paying the exact compounded aggregation of the underlying overnight benchmark rate (e.g., SOFR, $\text{\euro STR}$, TONAR). *Crucially:* This isn't known upfront. The floating payout dynamically realizes day-by-day. Every single night's prevailing rate is multiplied geometrically against the prior day's aggregate, specifically excluding non-business days (weekends).

At the terminal expiry of the 3-month term, the two mathematically derived sums are compressed, absolutely netted out, and only the pure cash difference settles. 

### Quasi-Arbitrage and Term Translation
The primary function of the OIS market is resolving structural arbitrage boundaries. 
There is massive trading volume locked strictly on the spread between the 3M OIS (the swap connecting fixed to compounded overnight) and the 3M Term Rate. Because a trader can theoretically borrow unsecured term cash for 3 months, and instantaneously swap the exposure backwards into chained overnight lending via the OIS, the pricing of the fixed leg of the massive OIS market forms the definitive 'Risk-Free Term Proxy' utilized globally across Yield Curves.

### Boundaries / Conditions

### Lagged Fixings 
A structural limitation of the pure OIS floating leg is that the final compounded payout amount is mathematically unknowable until the absolute final day of the term. To port this structure into physical cash instruments like Corporate Floating Rate Notes (FRNs), standard mechanics utilize explicit Lagging protocols. The interest formula observes the compounding overnight rate over an explicitly lagged prior window (e.g., lagged by exactly 5 periods, solving $l=5$) so the Corporate Treasury actually knows how much explicit cash to provision days before the terminal coupon date.

## Evidence / Source Anchors

- Definition of the Eonia, SOFR, and \euro STR benchmarks expanding the overnight interbank scope beyond unsecured lending: [[Fixed_Income_Alexander_During_Ch13.md#page=119]]
- Establishing the OIS swap mechanic linking a fixed payment with a floating payment precisely corresponding to the *compound interest* applied over the overnight deposit metric: [[Fixed_Income_Alexander_During_Ch13.md#page=120]]
- The explicit forward-starting OIS mechanism and its role replacing structural FRAs in the new benchmark environment: [[Fixed_Income_Alexander_During_Ch13.md#page=120]]

## Related

- [[Forward_Rate_Agreements_FRA_Mechanics]] — the legacy product settling explicitly on beginning-of-term discounting rather than compounding end-of-term overnight metrics
- [[LIBOR_And_Term_Benchmark_Fragility]] — the systemic collapse causing the mass migration into explicit OIS structures
