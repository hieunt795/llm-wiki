---
title: Inflation Forecast Targeting (IFT)
aliases:
- IFT
- Svensson IFT Framework
- Forecast as Intermediate Target
type: mechanism
tags:
- monetary-policy
- forecasting
- ITF
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: Inflation Forecast Targeting (IFT) is a strategic implementation of ITF where
  the central bank's own internal inflation forecast serves as the intermediate target,
  recognizing that policy actions take 6-8 quarters to impact actual prices.
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 232
- file: Perry_Central_Bank_Policy_P4.md
  page: 233
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

Lars Svensson (1997) argued that because of the **"Long and Variable Lags"** of monetary policy, targeting *current* inflation is "like driving a car by looking only at the rearview mirror." In IFT, the central bank adjusts the policy rate until its *forecasted* inflation at the policy horizon (usually 2 years) equals the target.

## Mechanism: The Targeting Rule

Using a forward-looking model, the central bank sets the interest rate $i_t$ such that:
$$E_t[\pi_{t+k}] = \pi^*$$
Where $k$ is the transmission lag.

### The Role of Output Stabilization ($\lambda$)
If the central bank also cares about output ($\lambda > 0$), the First-Order Condition (FOC) changes to:
$$E_t[\pi_{t+2}] - \pi^* = -\frac{\lambda}{\delta \alpha k} E_t[x_{t+1}]$$
- **Logic:** The central bank will only allow inflation to deviate from the target if it helps close a large output gap.
- **Speed of Adjustment:** A higher $\lambda$ means the central bank will return inflation to the target more slowly to avoid a massive recession (**Gradualism**).

## Operational Implications
- **Transparency:** The central bank must publish its **Inflation Report** and fan charts to show the public the "Target" it is actually aiming for.
- **Accountability:** The bank is judged not by today's inflation, but by whether its past forecasts were reasonable and if its actions were consistent with those forecasts.

## Evidence / Source Anchors

- Svensson (1997) concept of inflation forecast as a target: [[Perry_Central_Bank_Policy_P4.md#page=232]]
- Mathematical proof of optimal policy rule under IFT: [[Perry_Central_Bank_Policy_P4.md#page=233]]
- The advantage of enhancing credibility by focusing on expectations: [[Perry_Central_Bank_Policy_P4.md#page=234]]

## Related

- [[Baseline_ITF_Macroeconomic_Model]] — The model used for the forecast.
- [[Monetary_Policy_Implementation_Lags]] — The reason why IFT is necessary.
- [[Forward_Guidance_Strategic_Implementation]] — A tool used to communicate the forecast.
