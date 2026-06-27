---
title: Operational Framework (Supply Side)
type: mechanism
status: reviewed
confidence: 5
expert_lens:
  - Ulrich Bindseil (Liquidity Management)
  - Knut Wicksell (Natural Rate vs. Market Rate)
  - William Poole (Instrument Choice)
provenance: "[RAW-BOOK: Bindseil (2014)]"
half_life_years: 10
---

## Thesis
The supply side of the operational framework is the central bank's mechanism for steering short-term interest rates toward its operational target. By managing the **Liquidity Deficit** (or surplus) through Open Market Operations (OMOs) and defining the bounds of the money market via **Standing Facilities**, the central bank ensures its policy rate anchors the broader financial system.

## Mechanism (RCL)

### ① REGIME LOCK
The supply mechanism depends on the chosen framework technique (Bindseil's taxonomy):
- **Symmetric Corridor Approach:** The CB sets OMO volume to match the estimated liquidity deficit. Rates fluctuate around the target.
- **Full Allotment (Floor) Regime:** The CB satisfies all demand at a fixed rate (usually the main refinancing rate). The supply of reserves is passive/endogenous.
- **One-Directional Facility:** Rare in modern times (e.g., pre-1914), where the CB only provides liquidity via a standing discount window.

### ② CAUSAL CHAIN
**1. Liquidity Management & OMOs**
Autonomous Factors + Reserve Demand →[Forecasting]→ Net Liquidity Deficit →[OMO Allotment]→ Balanced Reserve Supply.
*   *DENSE Unpack (Intent):* The CB aims to offset exogenous shocks (e.g., banknote outflows) to keep the interbank market "neutral."

**2. Standing Facility Bounds**
Marginal Lending Rate (Ceiling) & Deposit Rate (Floor) →[Arbitrage Channel]→ Interest Rate Corridor.
*   *Mechanism:* If market rates exceed the ceiling, banks borrow from the CB; if they fall below the floor, banks deposit with the CB. This caps volatility.

**3. Steering via Scarcity**
Tightened Allotment →[Scarcity]→ Increased Interbank Competition →[Wicksellian Logic]→ Market Rate converges to Policy Rate.
*   *Boundary:* Effectiveness depends on the **Collateral Framework**. If banks lack eligible collateral, they cannot access the supply.

### ③ FEEDBACK TOPOLOGY
- **Balancing Loop (Full Allotment):** Market rate drops below policy rate → Banks reduce OMO bids or increase deposits → Liquidity drains → Rate rises back.
- **Reinforcing Loop (Stigma):** High ceiling rate + stigma → Banks avoid borrowing from CB → Market rates spike far above target during stress (Failure of the corridor).

### ④ CHANNEL INTERACTION
The supply side interacts with the **Collateral Channel**. Haircuts and eligibility lists determine the "shadow supply" of liquidity. Scarcity of collateral can impede the transmission of the central bank's supply of reserves to the real economy.

## Worked Example: Symmetric Corridor
A central bank targets a 3.00% overnight rate. 
- It sets the Marginal Lending Facility at 3.25% and the Deposit Facility at 2.75%.
- It forecasts a liquidity deficit of $100bn.
- It conducts a weekly OMO providing $100bn.
- If the forecast is correct, the overnight rate trades near 3.00%. If shocks occur (e.g., $10bn extra govt deposits), the market tightens, but is capped at 3.25% by the lending facility.

## Failure Conditions
- **Forecasting Errors:** Large errors in autonomous factors lead to unintended rate volatility in corridor systems.
- **Collateral Scarcity:** Even if the CB is willing to supply reserves, it cannot do so if the banking system has run out of eligible collateral.
- **Broken Arbitrage:** If banks are unwilling to lend to each other (counterparty risk), the supply of reserves at the aggregate level does not prevent rate spikes for individual distressed banks.

## Related
- [[Central_Bank_Reserves_Demand]]
- [[Interest_Rate_Corridor_And_Standing_Facilities]]
- [[OMO_Tender_Mechanics]]
- [[Collateral_Framework_Mechanism]]

---
**Source Reference:** [RAW-BOOK: Bindseil (2014)] Ch 3 & 4.
