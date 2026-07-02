---
title: Delegation of Authority Theory (Conservative Agent)
aliases:
- Theory of Central Bank Delegation
- Optimal Conservatism Model
- Rogoff Delegation Formula
type: mechanism
tags:
- central-banking
- governance
- monetary-theory
- math
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The delegation of authority theory states that a society can maximize its
  intertemporal welfare by delegating monetary policy to an independent agent who
  is more inflation-averse (conservative) than the public itself, effectively neutralizing
  inflation bias.
source_refs:
- file: Perry_Central_Bank_Policy_P5.md
  page: 328
- file: Perry_Central_Bank_Policy_P5.md
  page: 330
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

Kenneth Rogoff (1985) provided the mathematical proof that "Humans are the best commitment device." Since binding mathematical rules (like a k-percent rule) are often too brittle for reality, delegating power to a **Conservative Central Banker** achieves the same low inflation result while allowing for some flexibility during crises.

## Mechanism: The Optimization Problem

### 1. The Preference Mismatch
- **Public Loss Function ($L$):** Weights inflation ($\pi^2$) and output gap $(y - y^*)^2$ with parameter $b$.
- **Agent's Loss Function ($\hat{L}$):** Weights the same variables but with parameter $\hat{b}$.
- **Delegation Goal:** The public (policymaker) chooses an agent such that $0 < \hat{b} < b$.

### 2. The Social Welfare Solution
The public chooses the agent's conservatism $\hat{b}$ to minimize its own expected loss:
$$\min_{\hat{b}} E(L(b, \hat{b})) = (a\hat{b}y^*)^2 + \left( \frac{a\hat{b}}{1+a^2\hat{b}} \right)^2 \sigma_\epsilon^2 + b \left( \frac{1}{1+a^2\hat{b}} \right)^2 \sigma_\epsilon^2 + by^{*2}$$
Where:
- $a\hat{b}y^*$: Inflation bias (smaller with a conservative agent).
- $\sigma_\epsilon^2$: Variance of supply shocks.

### 3. The Trade-off
A smaller $\hat{b}$ (more conservative) leads to:
1. **Lower and more stable inflation** (benefit).
2. **Higher output volatility** (cost), because the conservative agent is less willing to use inflation to buffer shocks.

## Mathematical Conclusion
The optimal $\hat{b}$ is strictly less than $b$. This means society should *always* prefer a central banker who cares more about inflation than the average citizen does.

## Evidence / Source Anchors

- Formal derivation of the delegation model: [[Perry_Central_Bank_Policy_P5.md#page=328]]
- Mathematical proof of the $0 < \hat{b} < b$ condition: [[Perry_Central_Bank_Policy_P5.md#page=330]]
- Figure 11.1: Graphical representation of output stabilization preference: [[Perry_Central_Bank_Policy_P5.md#page=331]]

## Related

- [[Conservative_Central_Banker_Paradigm]] — The conceptual version.
- [[Barro_Gordon_Model]] — The problem this theory solves.
- [[Strict_vs_Flexible_Inflation_Targeting]] — The operational weight of $\hat{b}$.
- [[Quantity_Theory_Of_Money_MV_PY]]
- [[ECB_Institutional_Architecture]]
- [[Central_Bank_Independence_Framework]]
- [[Monetary_Policy_Nominal_Anchors_Matrix]]
- [[Rupiah_Stability_Dual_Dimension]]
- [[Baseline_ITF_Macroeconomic_Model]]
- [[Board_of_Governors_Decision_Making]]
- [[Central_Bank_Accountability_And_Transparency_Framework]]
- [[Central_Bank_Accountability_Characteristics]]
- [[Central_Bank_Credibility_Mechanisms]]
- [[Central_Bank_Independence_and_Accountability_Framework]]
- [[Democratic_Accountability_Theory]]
- [[Dimensions_of_Central_Bank_Independence]]
- [[Fed_Put_Theory]]
- [[Real_Bills_Doctrine_Mechanism]]
- [[Accountability_Independence_Trade_off]]
- [[Central_Bank_Political_Economy_Dynamics]]
- [[Quantity_Theory_Money_Demand_Velocity]]
