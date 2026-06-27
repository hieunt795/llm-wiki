---
title: Taralac (Target Rate Limited Access) Facility
aliases:
- Taralac Facility
- Target-Rate Limited-Access
type: mechanism
tags:
- monetary-policy
- central-banking
- standing-facilities
- interest-rate-steering
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Bindseil
provenance: "bindseil_target_rate.md"
thesis: The Taralac facility stabilizes overnight interest rates at the central bank's
  target rate by acting as a limited-access buffer, substituting the averaging function
  of reserve requirements while maintaining interbank market activity.
source_refs:
- file: bindseil_target_rate.md
  page: 80-83
created: '2026-04-26'
updated: '2026-04-26'
chapter: 6
---

# [[Taralac_Facility_Mechanics]]

## Thesis
[WIKI/LLM] The Taralac (Target Rate Limited Access) facility is a specialized standing facility designed to anchor market rates to the policy target. Unlike unlimited penalty facilities, Taralac access is capped to ensure that banks still have incentives to trade in the interbank market, effectively managing the trade-off between rate stability and market turnover.

## Mechanism

### 1. Conceptual Framework
[RAW] Taralac substitutes the averaging function of reserve requirements. It can be integrated into a standard symmetric corridor framework through one or two limited-access facilities at the target rate. [[bindseil_target_rate.md#page=80]]

### 2. Operational Logic (One-Directional Variant)
[RAW] There would be only one facility, at the target rate, say a borrowing facility. In order to ensure that the limited access facility anchors the overnight rate, the daily liquidity deficit should require ex ante an aggregate half-use of the standing facilities’ limit. [[bindseil_target_rate.md#page=81]]

*   **Mathematical Condition:** [RAW] The central bank provides through open market operations the amount of reserves such that the expected use of the Taralac facility at day end is one-half of the limit ($\psi$). [[bindseil_target_rate.md#page=82]]
*   **Signaling Alignment:** [LLM] By centering the liquidity distribution around the half-capacity of the Taralac facility at the target rate ($i^*$), the central bank ensures the interbank rate ($i$) defaults to $i^*$.

### 3. The Trade-off: Stability vs. Turnover
[RAW] The larger the capacity of the Taralac facility ($\psi$), the more stable the overnight rate will be. However, activity in the interbank overnight trading also depends on the capacity... the higher the capacity, the lower will be the incentive of banks to trade in the market. [[bindseil_target_rate.md#page=82]]

[RAW] The whole idea of limiting the access to a facility at the target rate reflects that such a limit supports the interbank market. [[bindseil_target_rate.md#page=82]]

## Worked Example
[LLM] **Calibrating Taralac Capacity:**
1.  **Parameters:** Target rate ($i^*$) = 0.5%; Corridor = [0%, 1.0%]; Taralac capacity ($\psi$) = €2bn.
2.  **OMO Goal:** Central bank forecasts a liquidity deficit. It conducts an OMO to leave the market "short" by €1bn (exactly $\psi/2$).
3.  **Result:**
    *   If the aggregate shock is 0, banks borrow €1bn from Taralac at 0.5%.
    *   The interbank rate stays at 0.5% because there is a 50% probability of needing more (at 1.0% penalty) and a 50% probability of having excess (at 0% deposit).
4.  **Conclusion:** The rate is anchored at 0.5% despite shocks, as long as shocks do not exceed $\pm\psi/2$.

## Failure Conditions
[LLM]
1.  **Excessive Capacity ($\psi \to \infty$):** [RAW] Eliminates the incentive for interbank trading, making the central bank the sole counterparty (market cannibalization). [[bindseil_target_rate.md#page=82]]
2.  **Insufficient Capacity:** If $\psi$ is too small relative to autonomous factor volatility, the rate will frequently hit the corridor boundaries, increasing volatility.
3.  **Asymmetric Shocks:** If the distribution of liquidity shocks is not symmetric, the "half-use" rule fails to anchor the rate exactly at $i^*$.

## Evidence / Source Anchors
- [[bindseil_target_rate.md#page=80]] — Introduction of the Taralac concept and its role relative to reserve requirements.
- [[bindseil_target_rate.md#page=81]] — Mathematical derivation of the interbank rate in a Taralac framework (Equation 6.3/6.4).
- [[bindseil_target_rate.md#page=82]] — Analysis of the stability-turnover trade-off and simulation results (Table 6.1).

## Related
- [[Interest_Rate_Corridor]]
- [[Reserve_Requirement_Averaging]]
- [[Interbank_Market_Activity]]
