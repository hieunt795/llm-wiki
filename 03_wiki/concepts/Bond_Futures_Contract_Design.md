---
title: Bond Futures Contract Design
aliases:
- Bond Futures
- Physical Settlement
- Cash-Settled Futures
- EDSP
- Invoice Price
- Open Interest Inflation
- Hợp đồng tương lai trái phiếu
type: mechanism
tags:
- fixed-income
- derivatives
- trading
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch29.md
thesis: Bond futures are exchange-traded derivative contracts that standardize the
  forward trading of fixed-income instruments, utilizing distinct settlement architectures—Physical
  (deterrent-based) or Cash (finality-based)—to bridge the gap between speculative
  liquidity and the underlying cash market.
source_refs:
- file: During_Fixed_Income_Ch29.md
  page: 1
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 2608-2982
  page: 301
- file: During_Fixed_Income_Ch29.md
  page: 302
- file: During_Fixed_Income_Ch29.md
  page: 303
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Bond futures solve the liquidity fragmentation of the physical bond market by concentrating trading into a few standardized quarterly expiries. Alexander Düring explains that the "crucial link" between the contract and the underlying market is the convergence of values at delivery. The choice of settlement mechanism (Physical vs. Cash) represents a fundamental trade-off between price manipulation deterrents and operational simplicity. [[During_Fixed_Income_Ch29.md#page=301]]

## Mechanism 1: Physical Settlement (Giao nhận vật lý)

The global standard for sovereign bond futures (US Treasuries, Bunds, JGBs).
- **The Process:** The seller (short) delivers a physical bond from a defined basket to the buyer (long).
- **The Invoice Price:** The actual cash paid for the delivered bond is:
$$\text{Invoice Price} = (\text{Futures Price} \times \text{Conversion Factor}) + \text{Accrued Interest}$$
- **The Deterrent:** Physical delivery prevents extreme price manipulation. If a long trader artificially pushes prices up, shorts will deliver the CTD bond at that inflated price, leaving the long holding a physical asset at a loss. [[During_Fixed_Income_Ch29.md#page=301-302]]

## Mechanism 2: Cash Settlement (Thanh toán chênh lệch)

Common in Australia and for money market rates (LIBOR/SOFR futures).
- **The Process:** Positions are closed out via a cash payment based on an **EDSP (Exchange-Determined Settlement Price)**.
- **The Risk:** Unlike physical settlement, there is no "link" to a tangible asset at delivery. This "clean exit" reduces hurdles for traders to manipulate the underlying reference benchmarks (e.g., LIBOR fixings) on the day of expiry. [[During_Fixed_Income_Ch29.md#page=301-303]]

## Market Dynamics: Open Interest vs. Volume

Exchanges use two primary metrics for liquidity:
1.  **Volume:** The number of contracts traded in a given period.
2.  **Open Interest (OI):** The total number of outstanding long (or short) positions.

### The Open Interest Inflation Paradox
Düring warns that OI figures are not comparable across exchanges due to clearing rules:
- **US Model (Agency):** Automatically nets long and short positions of the same user. OI reflects true net risk.
- **European Model (Principal):** Does not have end-user visibility and may permit simultaneous long and short positions in the same account. This **inflates OI figures**, making the market appear more active than the underlying economic risk suggests. [[During_Fixed_Income_Ch29.md#page=303-304]]

## Evidence / Source Anchors

- Definition of the Invoice Price formula and conversion factors: [[During_Fixed_Income_Ch29.md#page=301]]
- Analysis of physical settlement as a deterrent to price manipulation: [[During_Fixed_Income_Ch29.md#page=302]]
- Critique of cash-settled contracts and the lesson of the LIBOR crisis: [[During_Fixed_Income_Ch29.md#page=303]]
- Explanation of Open Interest inflation under the Principal Clearing model (Eurex): [[During_Fixed_Income_Ch29.md#page=303]]
- Identification of 90% of US RMBS trading as forward TBA, contrasting with bond futures: [[During_Fixed_Income_Ch28.md#page=289]]

## Related

- [[Cheapest_To_Deliver_CTD]] — How the delivered bond is selected.
- [[Conversion_Factor_And_Notional_Coupon]] — The math used to equalize the basket.
- [[Futures_Roll_And_Ratios]] — How positions transition between expiries.
- [[Bond_Futures_Squeeze_Dynamics]] — The risk of delivery failure in physical contracts.
- [[Agency_Vs_Principal_Clearing_Models]] — The structural cause of OI inflation.
