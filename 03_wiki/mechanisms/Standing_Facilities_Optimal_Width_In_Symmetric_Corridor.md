---
title: "Standing Facilities Optimal Width in Symmetric Corridor"
aliases: [Corridor Width Optimization, Standing Facility Spread, Standing Facility Rate Spread, Optimal Corridor Width, Symmetric Corridor Design]
type: mechanism
tags: [monetary-operations, standing-facilities, interest-rate-corridor]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "Optimal corridor width balances reduced rate volatility (wider corridor) against excessive interbank trading costs (narrower corridor); typical range is 50-100 bps."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 73
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Symmetric corridor width (standing facility spread) should be set to minimize sum of expected interbank transaction costs and overnight rate volatility, accounting for central bank operational costs.

## 1. Core Logic / Mechanism

[RAW] **Framework** (Bindseil p.73, sec 6.2):
Corridor: $[\text{Deposit Facility Rate} = i^* - s, \text{Lending Facility Rate} = i^* + s]$
- $i^*$ = policy midpoint rate (target)
- $s$ = half-width (spread divided by 2)
- Symmetric: both sides equidistant from target

[LLM] **Optimization Trade-off**:

**Narrow Corridor** (small $s$, e.g., 25 bps):
- **Advantage**: Overnight rate $r^{ON}$ stays tightly anchored near $i^*$
- **Disadvantage**: Banks face severe rate wedge; must actively arbitrage corridor
  - Borrowing from neighbor at $r^{ON} + \epsilon$ is essentially same cost as CB lending at $i^* + s$
  - Induces high interbank trading volume to minimize rate variance
  - High transaction costs (bid-ask spreads, search frictions)

**Wide Corridor** (large $s$, e.g., 200 bps):
- **Advantage**: Banks can tolerate $r^{ON}$ swings; interbank trading less compulsive
  - Lower transaction costs; banks can hold excess reserves at deposit facility rate safely
- **Disadvantage**: $r^{ON}$ volatility increases sharply
  - On tight liquidity days: $r^{ON} \approx i^* + s$ (ceiling)
  - On easy liquidity days: $r^{ON} \approx i^* - s$ (floor)
  - Policy transmission uncertainty increases

[LLM] **Optimization Condition**:
$$\text{Optimal } s^* = \arg\min_s \left[ \sigma(r^{ON}) + \text{Transaction Costs} + \text{CB Implementation Cost} \right]$$

Where:
- $\sigma(r^{ON})$ = volatility of overnight rate (rises with $s$)
- Transaction Costs = function of interbank trading volume (falls with $s$)
- CB Implementation Cost = operational burden of frequent OMOs (minimal, not binding)

## 2. Worked Example

[LLM] **Scenario: Comparing 50 bps vs. 150 bps Corridor**

**Market Conditions**:
- Policy rate: 2.00% ($i^*$)
- Daily liquidity shock volatility: $\sigma_{\text{shock}} = 10$ basis points

**50 bps Corridor** ($i^* - 0.25\% = 1.75\%$ deposit, $i^* + 0.25\% = 2.25\%$ lending):
- Interbank overnight rate: Oscillates tightly in $[1.76\%, 2.24\%]$
- Standard deviation observed: $\sigma = 8$ bps (highly anchored)
- Required interbank transactions (to stay near target): HIGH
  - Bank A borrows from Bank B at $r^{ON} = 2.02\%$ multiple times daily
  - Bid-ask spread: 5 bps; transaction cost per trade: ~2 bps
  - Daily interbank trades per bank: 3-5 trades
  - System-wide transaction cost: ~30-50 million EUR daily

**150 bps Corridor** ($i^* - 0.75\% = 1.25\%$ deposit, $i^* + 0.75\% = 2.75\%$ lending):
- Interbank overnight rate: Can float more freely
- Standard deviation observed: $\sigma = 25$ bps (wider swings)
- Interbank transactions: LOW (banks tolerate 25 bps variance)
  - Banks borrow less actively; hold excess reserves at 1.25% facility deposit rate
  - Interbank trades per bank: 0-1 trades daily
  - System-wide transaction cost: ~5-10 million EUR daily

**Trade-off**: 
- Narrow corridor reduces rate uncertainty but costs 20-40 million EUR/day in transaction costs
- Wide corridor saves transaction costs but increases policy transmission uncertainty
- **Bindseil Finding**: Optimal width typically 50-100 bps (European practice: 50 bps, Fed: 100-200 bps historically)

## 3. Failure Conditions / Boundaries

- **Zero Lower Bound (ZLB)**: Cannot implement negative corridor around zero midpoint (deposit facility rate would become positive penalty)
- **Stigma Effects**: Narrow corridor may increase stigma cost (market interprets frequent CB borrowing as distress) → actual effective corridor widens
- **Heterogeneous Banks**: Small, risky banks excluded from standing facilities face wider effective corridor (may not have access to deposit facility) → corridor optimization invalid for them
- **Liquidity Crisis**: In stress, standing facilities become irrelevant (banks hit collateral constraints before rate ceiling) → optimal width calculation breaks down
- **Interbank Market Shutdown**: If interbank market freezes (2008 crisis), transaction cost advantage of narrow corridor disappears → wide corridor effectively costless

## 4. TARALAC Variant

[RAW] **"Target Rate—Limited Access" (TARALAC) Facility** (Bindseil p.80, sec 6.3):
- Modified standing facility: deposits at target rate $i^*$, borrowing at $i^* + s$
- Effect: Asymmetric corridor, tighter floor (deposit facility = target), loose ceiling
- Purpose: Reduce excess reserve accumulation (banks less eager to deposit at penalty rate)
- Trade-off: Introduces asymmetry; ceiling no longer constrains when liquidity is tight

## Related
- [[Interest_Rate_Corridor_And_Standing_Facilities]]
- [[One_Directional_Standing_Facility_Implementation]]
- [[Open_Market_Operations_And_Instruments]]
- [[Interbank_Money_Market_Mechanism]]
- [[Standing_Facilities_Types_And_History]]
