---
title: Nominal Rigidity Models (Fischer & Taylor)
aliases:
- Staggered Wages Model
- Fischer-Taylor Model
- Wage-Price Mechanism
- Nominal Rigidity
type: mechanism
tags:
- neo-keynesian
- macroeconomics
- monetary-transmission
- expectations
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: Nominal rigidity models demonstrate that money is non-neutral in the short
  run because wages and prices are set in advance through staggered contracts, creating
  persistence (inertia) in output response to monetary shocks even under rational
  expectations.
source_refs:
- file: Perry_Central_Bank_Policy_P3.md
  page: 60
- file: Perry_Central_Bank_Policy_P3.md
  page: 61
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

The Fischer (1977) and Taylor (1980) models provide the Neo-Keynesian rebuttal to the Neoclassical "Island" model. They prove that **rational expectations alone do not guarantee money neutrality**. If institutional rigidities (like staggered labor contracts) exist, monetary policy can effectively influence real output in the short run by altering real wages before contracts can be renegotiated. [[Perry_Central_Bank_Policy_P3.md#page=60]]

---

## 1. Fischer (1977): Unanticipated Shocks

Fischer focuses on the timing of information. Nominal wages ($w$) are set at the beginning of a period based on the available information ($t-1$):
$$w = E[p | t-1]$$

- **The Mechanism:** Prices are assumed flexible, but nominal wages are rigid for one period.
- **The Result:** Output ($y$) becomes a function of **unanticipated** money and demand shocks:
$$y = \frac{1}{2} [(m - E[m|t-1]) + (u - E[u|t-1])]$$
- **Implication:** The central bank can stabilize output because it possesses more "current" information than the workers who are locked into their $t-1$ contracts. [[Perry_Central_Bank_Policy_P3.md#page=60]]

---

## 2. Taylor (1980): Staggered Wage Setting

Taylor introduces **Staggering**: the workforce is divided into cohorts that renegotiate at different times.

### The Overlapping Mechanism
In each period, only half of the labor force sets a new wage for the next two periods.
- **Weighted Average Price:** $p = \frac{1}{2}(w + w_{-1})$.
- **The Wage Equation:**
$$w = \frac{1}{2}[p + E(p_{+1}|-1)] + \frac{1}{2}a[E(y|-1) + E(y_{+1}|-1)]$$
- **Relative Wages:** Workers do not just look at prices; they look at the wages of the other cohort ($w_{-1}$). This creates a social and institutional "anchor" that prevents rapid adjustments. [[Perry_Central_Bank_Policy_P3.md#page=61]]

### Real Money Persistence ($k$)
If money follows a random walk, the solution implies a dynamic influence:
$$w = kw_{-1} + (1-k)m_{-1}$$
- **The Parameter $k$:** $k = \frac{1 - a^{1/2}}{1 + a^{1/2}}$
- **The Sensitivity $a$:** Reflects how much the labor market (output gap) affects wages.
- **The Persistence Paradox:** A smaller $a$ (less sensitive labor market) leads to $k \to 1$. This means the influence of a monetary shock today **echoes exponentially** through the economy for many periods, rather than being a one-off shock. [[Perry_Central_Bank_Policy_P3.md#page=61]]

---

## Evidence / Source Anchors

- Fischer's derivation of output as a function of unanticipated disturbances: [[Perry_Central_Bank_Policy_P3.md#page=60]]
- Taylor's staggered wage-setting model (Equation 25): [[Perry_Central_Bank_Policy_P3.md#page=60]]
- Mathematical proof of persistence $k$ being inversely related to labor market sensitivity $a$: [[Perry_Central_Bank_Policy_P3.md#page=61]]
- Analysis of output gradually returning to equilibrium following an exponential decline: [[Perry_Central_Bank_Policy_P3.md#page=61]]

## Related

- [[Neutrality_Of_Money]] — The long-term state that these models eventually reach.
- [[Lucas_Aggregate_Supply_Function]] — The Neoclassical alternative based on information islanding.
- [[Monetary_Transmission_Mechanism]] — How these rigidities create the "Lag" in policy effects.
- [[Inside_Vs_Outside_Money]] — Why bank-credit cycles amplify these nominal rigidities.
