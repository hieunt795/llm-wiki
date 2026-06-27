---
title: Central Bank Reserves Demand
type: mechanism
status: reviewed
confidence: 5
expert_lens:
  - Ulrich Bindseil (Monetary Operations)
  - Walter Bagehot (Money Market Instability)
  - Henry Thornton (Bank Rate Theory)
provenance: "[RAW-BOOK: Bindseil (2014)]"
half_life_years: 10
---

## Thesis
The demand for central bank reserves (bank sight deposits with the central bank) is the anchor of monetary policy implementation. It is structurally determined by reserve requirements and the banking system's need for "working balances" to facilitate payments. In the short term, this demand is characterized by extreme interest rate inelasticity, necessitating active central bank intervention to stabilize rates.

## Mechanism (RCL)

### ① REGIME LOCK
The nature of reserve demand shifts based on the operational regime:
- **Corridor Regime:** Demand is dominated by **Reserve Requirements** (if binding) or **Working Balances** (if requirements are low/zero). The central bank targets a specific scarcity level.
- **Floor Regime (Excess Liquidity):** Demand becomes perfectly elastic at the deposit facility rate as banks hold vast excess reserves.
- **Crisis Regime:** Demand is driven by **Precautionary Liquidity** (hoarding) due to interbank market breakdown.

### ② CAUSAL CHAIN
**1. Structural Demand Formation**
Reserve Requirements →[Averaging Provision]→ Intertemporal Arbitrage →[Martingale Property]→ Stabilized Overnight Rates.
*   *Confounder:* If the averaging period is too short, volatility spikes at period end.

**2. Payment System Need (Working Balances)**
Intraday Payment Volatility →[Uncertainty]→ Precautionary Buffer Demand →[Inelasticity]→ Scarcity.
*   *Confounder:* Efficient Real-Time Gross Settlement (RTGS) systems reduce the level of working balances needed.

**3. Interest Rate Elasticity (The Bagehot Constraint)**
Urgent Payment Obligations →[Necessity]→ Vertical Demand Curve →[Fixed Supply]→ Extreme Rate Volatility.
*   *Mechanism:* As Bagehot (1873) noted, a slight deficiency in quantity leads to wild fluctuations because banks *must* find reserves to meet acceptances.

### ③ FEEDBACK TOPOLOGY
- **Reinforcing Loop (Hoarding):** Perceived scarcity → Increased precautionary demand → Higher interbank rates → Further scarcity fears (Crisis mode).
- **Balancing Loop (Averaging):** Rate above expected future average → Banks use reserves today, plan to hold more later → Current rate falls back toward the expected average.

### ④ CHANNEL INTERACTION
The interaction between **Autonomous Factors** (banknotes, government deposits) and **Demand** determines the **Liquidity Deficit**. A larger deficit increases central bank "leadership" in the money market by making banks dependent on refinancing.

## Worked Example: The Martingale Property
In a reserve maintenance period of 30 days with averaging, if the market expects the central bank to raise rates in 10 days, the demand for reserves *today* will spike. Banks try to fulfill their average requirement early while it is cheaper. This pulls the current overnight rate up toward the future expected rate immediately, even before the policy change.

## Failure Conditions
- **Technical Breakdown:** If payment systems fail, demand for working balances becomes infinite (or limited only by collateral).
- **Zero Lower Bound (ZLB):** At the ZLB, the opportunity cost of holding reserves vanishes, making demand potentially satiable but decoupling it from traditional interest rate steering.

## Related
- [[Operational_Framework_Supply_Side]]
- [[Interest_Rate_Corridor_And_Standing_Facilities]]
- [[Liquidity_Deficit_Mechanism]]
- [[Reserve_Requirements_Averaging]]

---
**Source Reference:** [RAW-BOOK: Bindseil (2014)] Ch 2 & 3.
