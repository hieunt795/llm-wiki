---
title: Negative Convexity in MBS
aliases:
- Negative Convexity
- Convexity Trap
- Price-Yield Hump
- Extension Risk
- Contraction Risk
- Lồi âm
type: mechanism
tags:
- fixed-income
- rmbs
- risk-management
- quantitative-finance
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch28.md
thesis: Negative convexity is a structural risk profile in prepayable debt where a
  security's duration extends as interest rates rise and contracts as interest rates
  fall, creating a non-linear 'hump' in the price-yield relationship that mandates
  aggressive dynamic hedging.
source_refs:
- file: During_Fixed_Income_Ch28.md
  page: 297
- file: During_Fixed_Income_Ch28.md
  page: 298
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Standard bonds have **Positive Convexity**: they gain value faster when rates fall than they lose value when rates rise. **Mortgage-Backed Securities (MBS)** exhibit the opposite behavior. Alexander Düring explains that this is because the investor has effectively sold a "Short Call Option" to the borrower. This negative convexity manifests as a "hump" on the price chart, where the asset's duration behaves as a "silent predator," moving against the investor in both directions. [[During_Fixed_Income_Ch28.md#page=297-298]]

## Mechanism: The Duration Seesaw

Negative convexity is driven by the dynamic change in the **Weighted Average Life (WAL)** of the mortgage pool:

### 1. Contraction Risk (When Rates Fall)
- **The Behavior:** Borrowers refinance their mortgages to capture lower rates.
- **The Impact:** Prepayments surge, and the high-coupon MBS is repaid early.
- **The Result:** The duration of the MBS collapses. The investor is forced to reinvest the returned principal at the new, lower market rates. The price of the MBS "caps out" because the upside is truncated by redemptions at Par. [[During_Fixed_Income_Ch28.md#page=297]]

### 2. Extension Risk (When Rates Rise)
- **The Behavior:** Borrowers stop refinancing because their existing coupon is lower than current market rates.
- **The Impact:** Prepayments dry up, and the low-coupon MBS remains outstanding for much longer than expected.
- **The Result:** The duration of the MBS extends. The investor is "trapped" in a low-yielding asset while market rates move higher, causing the price to fall much faster than a standard bond. [[During_Fixed_Income_Ch28.md#page=297]]

## Strategic Implications: The Hedging Feedback Loop

MBS hedgers (banks and GSEs) must maintain a stable duration. To do this, they must perform **Dynamic Hedging**:
1.  **Rates Fall:** MBS duration shrinks. Hedgers must **Sell Treasuries** to restore their portfolio duration.
2.  **Rates Rise:** MBS duration extends. Hedgers must **Buy Treasuries** to reduce risk.
3.  **The Trigger:** This activity creates a self-accelerating feedback loop. Large-scale buying or selling of Treasuries by mortgage hedgers can cause "Convexity Shocks" that violently push yields further in the same direction. [[During_Fixed_Income_Ch28.md#page=297-298]]

## Evidence / Source Anchors

- Analysis of rising duration for rising yields as the definition of negative convexity: [[During_Fixed_Income_Ch28.md#page=297]]
- Description of the "Price-Yield Hump" where RMBS initially gains value as rates rise: [[During_Fixed_Income_Ch28.md#page=297]]
- Identification of "Contraction Risk" and "Extension Risk" as the two faces of negative convexity: [[During_Fixed_Income_Ch28.md#page=297]]
- Analysis of the "Short Option" position held by MBS investors against ordinary households: [[During_Fixed_Income_Ch28.md#page=298]]
- Linkage between mortgage convexity hedging and Treasury market liquidity: [[During_Fixed_Income_Ch28.md#page=298]]

## Related

- [[Residential_Mortgage_Backed_Securities_RMBS]] — The primary source of this risk.
- [[Mortgage_Prepayment_Drivers]] — The behavioral factors that trigger the seesaw.
- [[Preferred_Habitat_Market_Distortions]] — Why RMBS hedgers create tranches of demand in Treasuries.
- [[Macaulay_Duration]] — The metric that becomes unstable in negatively convex instruments.
