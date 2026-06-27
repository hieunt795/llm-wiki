---
title: Danish Balance Principle and Mortgage Delivery
aliases:
- Danish Covered Bonds
- Pass-Through Delivery Refinancing
- Balance Principle
- Danish Mortgage System
type: convention
tags:
- market-infrastructure
- european-finance
- bonds
- mortgage-market
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch26.md
thesis: The Danish covered bond market utilizes a strict 'Balance Principle' to link
  individual mortgages 1-to-1 with funding bonds, granting retail borrowers a unique
  'Delivery Option' to cancel debt by purchasing their own bonds at market discounts.
source_refs:
- file: During_Fixed_Income_Ch26.md
  page: 279
- file: During_Fixed_Income_Ch26.md
  page: 280
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The Danish covered bond market is one of the oldest and most structurally sophisticated in the world. Its core distinguishing feature is the **Balance Principle**, which creates an absolute economic linkage between a homeowner's mortgage and the bonds that refinance it. Alexander Düring explains that this transparency democratizes institutional yield curve mechanics, effectively turning the Danish bank into a mere administrative pass-through proxy for capital market lending. [[During_Fixed_Income_Ch26.md#page=279]]

## Mechanism: The 1-to-1 Linkage

When a Danish borrower takes out a mortgage, the funding bank issues an exactly identical amount of specific covered bonds matched to that loan's terms (coupon and duration).

### 1. The Delivery Right (Prepayment Arbitrage)
Because the bond pricing mirrors the mortgage pricing, a Danish borrower is granted an explicit legal right to execute financial arbitrage.
- **Scenario:** Interest rates rise, and the market price of the $5\%$ fixed Danish covered bond crashes to **80 cents on the dollar**.
- **The Trade:** The borrower buys the required face value of these bonds on the secondary market for 80 cents and "delivers" them to the bank.
- **The Result:** The bank accepts the bonds at **Par (100)** and cancels the mortgage. The borrower has effectively generated equity for themselves by trading against yield curve shifts. [[During_Fixed_Income_Ch26.md#page=279]]

### 2. Traditional Par Prepayment
Conversely, if interest rates fall and the covered bond surges above Par (e.g., 110 cents):
- **The Execution:** The borrower ignores the expensive secondary bond market and simply repays the physical mortgage at **Par (100)** using the standard prepayment option.
- **The Hedge:** The bank, in turn, partially "calls" the outstanding covered bonds at Par, passing the prepayment through to the bondholders. [[During_Fixed_Income_Ch26.md#page=279-280]]

## Strategic Implications: Market Fragmentation

This intense alignment creates extreme transparency but leads to massive **Market Fragmentation**.
- **Fragmentation:** Because bonds match specific discrete mortgage tranches, the Danish market generates thousands of individually customized bond lines rather than a few large benchmark series.
- **Price Discovery:** Despite the fragmentation, Danish regulators enforce high price transparency for these OTC trades to ensure retail borrowers can accurately value their delivery options. [[During_Fixed_Income_Ch26.md#page=279]]

## Evidence / Source Anchors

- Definition of the Balance Principle as the close relationship between underlying mortgages and refinancing bonds: [[During_Fixed_Income_Ch26.md#page=279]]
- Analysis of the "Delivery" process as a full or partial cancellation of mortgage debt via bond purchase: [[During_Fixed_Income_Ch26.md#page=279]]
- Comparison of the opposing effects of delivery (during rising rates) and par prepayment (during falling rates): [[During_Fixed_Income_Ch26.md#page=280]]
- Identification of "Flexlån" (variable rate contracts) and their implementation via bond auctions: [[During_Fixed_Income_Ch26.md#page=280]]
- Discussion on the resulting market fragmentation vs. price transparency: [[During_Fixed_Income_Ch26.md#page=279]]

## Related

- [[Covered_Bonds]] — The broader asset class to which this model belongs.
- [[Yield_Curve_Carry_And_Roll_Down]] — The trajectory dynamics utilized by the delivery option.
- [[Floating_Rate_Notes_FRN]] — Technical basis for Flexlån variable structures.
- [[Macaulay_Duration]] — Why rising rates create the discount used in delivery.
