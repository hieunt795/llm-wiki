---
title: Macroeconomic Supply and Demand Shocks
type: mechanism
status: draft
confidence: 4
uncertainty_factors: [Regime-dependent transmission, data reliability in developing contexts]
expert_lens: [Lipschitz & Schadler, L. Randall Wray, Perry Warjiyo]
provenance: [Lipschitz & Schadler Ch2]
half_life_years: 10
tags: [macroeconomics, shocks, national-accounts, transmission]
---

## Thesis
Macroeconomic shocks propagate through the economy via the National Accounts identities, where their final impact on output, prices, and the external balance is determined by the **output gap** and the **composition of absorption** (traded vs. nontraded goods).

## Mechanism (RCL)

### ⓪ CURRENCY GATE
[⊘ skipped: half_life≥10]

### ① REGIME LOCK
The transmission of shocks is highly regime-dependent based on the **Output Gap**:
*   **Slack Regime (Actual < Potential):** Shocks to demand (e.g., aid inflows spent domestically) are absorbed by increased utilization of unemployed labor/capital, leading to higher output with minimal price pressure.
*   **Full Capacity Regime (Actual ≈ Potential):** Shocks to demand lead to "crowding out." Increased spending on nontraded goods bids up domestic prices and wages, reducing export competitiveness and widening the Current Account Deficit (CAD).

### ② CAUSAL CHAIN
[LENSES: Lipschitz & Schadler — Accounting Identity Logic; L. Randall Wray — Resource Constraints; Perry Warjiyo — Developing Country Absorption]

**Shock Transmission Flow:**
Shock (e.g., Aid Inflow) → [Resource Constraint Identity: $I = S_p + S_g + CAD$] → Change in Absorption ($A = C + I + G$).

1.  **Traded Goods Absorption:**
    Aid/Inflow → Spending on Imports → $CAD \uparrow$ (offsetting the inflow) → Real resources transferred without domestic price pressure.
    
2.  **Nontraded Goods Absorption (The "Crowding Out" Mechanism):**
    Aid/Inflow → Spending on Nontraded (e.g., infrastructure) → [IF NO GAP] → Wages/Prices $\uparrow$ → Real Exchange Rate Appreciation → Export Sector $\downarrow$ → $CAD \uparrow$ (effecting the transfer via reduced net exports).

**DENSE — Nontraded Goods Unpacked:**
*   **INTENT:** To model the internal resource constraint where domestic supply cannot be augmented by imports.
*   **MECHANISM:** Inelastic domestic supply (short-run) $\implies$ Excess demand results in price adjustment rather than volume adjustment.
*   **INTERACTIONS:** Connects to **Dutch Disease**; positive shocks to one sector (aid/commodities) penalize the tradable sector (manufacturing) through the wage channel.
*   **BOUNDARY:** Fails if labor is perfectly mobile across borders or if structural reforms shift the potential output frontier ($Y^*$) simultaneously.

### ③ FEEDBACK TOPOLOGY
*   **Reinforcing Loop:** Increased domestic demand $\rightarrow$ higher tax revenues $\rightarrow$ further government spending $\rightarrow$ higher inflation (in a closed or capacity-constrained economy).
*   **Balancing Loop:** Real exchange rate appreciation $\rightarrow$ reduced competitiveness $\rightarrow$ falling exports $\rightarrow$ lower income $\rightarrow$ dampening of the initial demand surge.

### ④ CHANNEL INTERACTION
*   **Fiscal Channel:** Direct impact on $S_g$ and $G$.
*   **External Channel:** Adjustment through the $CAD$.
*   **Monetary Channel:** Interest rate responses to inflationary pressures from nontraded goods prices.

## Worked Example: New Aid Transfer
A low-income country receives a 5% GDP aid transfer.
*   **Scenario A (Traded):** Government buys imported tractors. $G \uparrow$, $M \uparrow$, $CAD$ remains stable relative to the new inflow. No impact on domestic inflation.
*   **Scenario B (Nontraded):** Government hires local workers for roads. If the labor market is tight, wages in the textile export sector rise to compete for labor. Textile exports fall. The "aid" is effectively financed by the decline of the export sector.

## Failure Conditions
*   **Structural Discontinuity:** If a shock (like a pandemic) destroys supply capacity, the "output gap" appears large but is actually zero due to a lower $Y^*$.
*   **Measurement Lag:** Relying on GDP data (lagged) rather than leading indicators (purchasing manager surveys, building permits) leads to pro-cyclical policy errors.

## Related
*   [[Current_Account_Dynamics]]
*   [[Output_Gap_Measurement]]
*   [[Fiscal_Monetary_Policy_Mix]]
*   [[Dutch_Disease_Mechanism]]
