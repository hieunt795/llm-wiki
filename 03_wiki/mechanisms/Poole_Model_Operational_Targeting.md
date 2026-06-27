---
title: Poole Model (Operational Targeting)
aliases:
- Poole 1970 Model
- Interest Rate vs Money Supply Choice
- Stochastic Target Selection
type: mechanism
tags:
- monetary-policy
- operational-framework
- mathematics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The Poole Model (1970) provides a stochastic framework for central banks to
  choose between interest rate and money supply targets by analyzing which target
  minimizes output volatility in the face of shocks to the goods market (IS) or the
  money market (LM).
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 191
- file: Perry_Central_Bank_Policy_P4.md
  page: 192
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

William Poole (1970) proved that there is no "globally superior" operational target. The optimal choice depends entirely on the **Source of Instability** in the economy. Central banks should target the variable that "shields" the real economy from the most prevalent type of shock.

## Mechanism: The Decision Rule

The model uses a standard IS-LM framework with stochastic error terms:
- **IS Shock ($u$):** Shocks to real demand (investment, consumption).
- **LM Shock ($v$):** Shocks to money demand (financial innovation, velocity shifts).

### 1. When to Target Interest Rates ($r$)
- **Scenario:** The economy is hit primarily by **LM Shocks** (unstable money demand).
- **Logic:** By fixing $r$, the central bank automatically accommodates shifts in $M^d$, preventing them from affecting the real economy.
- **Outcome:** Output volatility is minimized. This explains why most modern central banks (post-financial innovation) target interest rates.

### 2. When to Target Money Supply ($M$)
- **Scenario:** The economy is hit primarily by **IS Shocks** (unstable real demand).
- **Logic:** Fixing $M$ allows the interest rate to act as a "natural stabilizer." For example, if demand spikes, $r$ will naturally rise as people compete for the fixed $M$, thereby dampening the original spike.
- **Outcome:** Output volatility is lower than if the CB had held $r$ constant and "fueled" the demand spike.

## Mathematical Conclusion
Target interest rates if:
$$\sigma^2_v > \sigma^2_u$$
(Volatility of money market shocks exceeds volatility of goods market shocks).

## Evidence / Source Anchors

- Original Poole (1970) contribution on unawareness of shocks: [[Perry_Central_Bank_Policy_P4.md#page=191]]
- Comparison of output variance under $r$ vs. $M$ targets: [[Perry_Central_Bank_Policy_P4.md#page=192]]
- Policy implication for modern interest rate corridors: [[Perry_Central_Bank_Policy_P4.md#page=192]]

## Related

- [[Monetary_Policy_Strategic_Framework]] — The choice of intermediate targets.
- [[Interest_Rate_Corridor_And_Standing_Facilities]] — The modern implementation of interest rate targeting.
- [[Velocity_Of_Money_Instability]] — The primary driver of LM shocks.
