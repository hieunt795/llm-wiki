---
type: mechanism
title: Bond Futures Pricing and Cheapest-to-Deliver
tags: [futures, hedging, ctd, basis, conversion-factors]
source:
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=249]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=259]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=260]]"
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 2608-2813
status: active
created: 2026-04-28
---

# Bond Futures Pricing and Cheapest-to-Deliver (CTD)

## Futures Overview

Futures on government bonds are among the most liquid fixed income products globally, used to hedge interest rate risk and take positions on yield curve changes [extracted].

Unlike **forwards** (bilateral, settled once at maturity), futures contracts embed:
- **Daily settlement** (mark-to-market daily)
- **Delivery options** (short seller chooses which bond to deliver and when)
- **Quality and timing options** affecting the futures contract's value

[extracted]

## Forward Bond Pricing (Baseline)

For a bond forward contract, the arbitrage-free forward price is: [extracted]

$$F = S + \text{Accrued Interest at Settlement} + \text{Financing Cost} - \text{Coupon Income}$$

where all terms are discounted to present value.

**Example:** US Treasury 2.875s of 05/15/2028

Trade date: May 14, 2021
Spot price: 110.77344
Spot settlement: May 17, 2021 (3 days)
Forward settlement: September 30, 2021 (136 days from spot)
Repo rate: 0.015%
Forward price: **109.71221**

[extracted]

## Futures vs. Forwards Difference

Futures prices differ from forwards due to:

1. **Daily settlement:** Futures mark-to-market daily; forwards accumulate value over time
2. **Financing impact:** Daily settlement affects reinvestment of profits/losses
3. **Delivery options:** Short seller can choose which bond to deliver and when

[extracted]

**Key result (Appendix A11.3):**
$$F_{\text{futures}} = F_{\text{forward}} - \text{(small adjustment)}$$

The difference tends to be small, especially for short holding periods and stable rate environments [extracted].

## Delivery Mechanism

US Treasury futures (CBOT 10-year contract, symbol TYU1) specify: [extracted]

- **Deliverable basket:** Multiple Treasury notes with coupons 1.125% to 3.125% and maturities 6.5 to 10 years
- **Conversion factor:** Pre-specified factor for each deliverable bond, standardizing cash flows to par
- **Delivery timing:** Seller has a **wild card option** (right to choose delivery date within contract month)

[extracted]

### Conversion Factor Mechanism

Each deliverable bond has a conversion factor that scales its price to a standardized "par equivalent" [extracted]:

| Coupon | Maturity | Conversion Factor |
|--------|----------|-------------------|
| 2.875% | 05/15/28 | 0.8338 |
| 2.875% | 08/15/28 | 0.8286 |
| 1.250% | 04/30/28 | 0.7474 |
| 3.125% | 11/15/28 | 0.8376 |
| 1.125% | 02/15/31 | 0.6577 |

[extracted]

**Purpose:** Conversion factors normalize differences in coupons and maturities so bonds with different characteristics can be compared [extracted].

## Cheapest-to-Deliver (CTD) Selection

The short seller (holder of the futures contract) will deliver the bond with the lowest cost: [extracted]

$$\text{Cost} = \text{Bond Price} - (\text{Futures Price} \times \text{Conversion Factor})$$

**Example:** If futures price = 133.86 and conversion factor = 0.8338, then:
- Delivered 2.875s: Cost = 110.77344 - (133.86 × 0.8338) = 111.61 [extracted]

The **CTD bond** is the one that minimizes this cost (maximizes profit for the short).

## Basis and Basis Risk

**Basis** = Cash bond price - (Futures price × Conversion factor)

**Basis trading:** Traders lock in the basis by:
1. Buying the cash bond
2. Selling futures
3. Holding until delivery or contract expiration

[extracted]

**Basis risk:** The basis may widen or tighten, creating unexpected P&L:
- If basis widens → short futures loses money (must buy futures back higher)
- If basis tightens → short futures gains money

[extracted]

## Daily Settlement Example

**Position:** Long 1 contract of TYU1 (10-year Treasury futures)

**Mark-to-market from May 10 to May 28, 2021:** [extracted]

| Date | Settlement Price | Daily Change | Daily P&L |
|------|------------------|--------------|-----------|
| 05/10 | 131-24 | — | — |
| 05/11 | 131-19 | −5 ticks | −$156.25 |
| 05/12 | 131-01 | −18 ticks | −$562.50 |
| 05/13 | 131-10 | +9 ticks | +$281.25 |
| 05/14 | 131-17+ | +7.5 ticks | +$234.38 |
| ... | ... | ... | ... |
| 05/28 | 131-30 | +5 ticks | +$156.25 |

[extracted]

**Cumulative from May 10 to May 28:** 6-tick gain = $187.50 profit [extracted]

**Key mechanics:**
- Each tick = 1/32 = $31.25 per contract (for a $100,000 face contract)
- Daily gains/losses are posted to the trader's account
- Margin requirements protect against counterparty default

[extracted]

## Futures vs. Forwards: P&L Realization Pattern

Because of daily settlement: [extracted]

- **Forwards:** Profit/loss realized only at expiration
- **Futures:** Profit/loss realized daily, reinvested at daily spot rates

This timing difference can meaningfully affect returns, especially in volatile rate environments.

## Practical Application: Hedging

A bond portfolio manager uses Treasury futures to hedge interest rate risk: [extracted]

1. Identify portfolio duration: e.g., 5.2 years
2. Calculate futures contract DV01: e.g., $131 per basis point
3. Number of contracts to sell: (Portfolio DV01) / (Futures DV01)
4. Monitor basis between portfolio and deliverable bonds

The futures hedge reduces (but does not eliminate) interest rate risk; basis risk remains [extracted].

## Related Nodes

[[Bond_Spread_Framework]]
[[Yield_to_Maturity_Calculation]]
[[Forward_Bond_Contracts]]
[[Interest_Rate_Risk_Hedging]]
