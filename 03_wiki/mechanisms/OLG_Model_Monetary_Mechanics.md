---
title: 'OLG Model: Monetary Mechanics'
aliases:
- Overlapping Generations Model
- Non-superneutrality proof
- Samuelson Consumption-Loan Model
- OLG Model
type: mechanism
tags:
- monetary-theory
- macroeconomics
- general-equilibrium
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The Overlapping Generations (OLG) model demonstrates the non-superneutrality
  of money by showing how money supply growth redistributes wealth between young and
  old generations, thereby altering real economic variables and resource allocation
  in the steady state.
source_refs:
- file: Perry_Central_Bank_Policy_P3.md
  page: 53
- file: Perry_Central_Bank_Policy_P3.md
  page: 54
- file: Perry_Central_Bank_Policy_P3.md
  page: 55
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

The OLG model, based on Samuelson (1958), is a fundamental tool for analyzing the non-neutrality of money through a demographic lens. Unlike infinite-horizon models (like MIU), the OLG structure creates a natural conflict of interest between generations. Perry Warjiyo explains that in this framework, money supply growth is **not superneutral** because the way new money is injected (the distribution effect) fundamentally changes the allocation of consumption between the young and the old. [[Perry_Central_Bank_Policy_P3.md#page=53-55]]

## Mechanism: The Two-Period Lifecycle

The model assumes discrete time where individuals live for exactly two periods: **Young** (period $t$) and **Old** (period $t+1$).

### 1. The Maximization Problem
The utility of an individual born in $t$ is $u(c_{1t}, c_{2t+1})$. 
- **Young:** Each young person receives one unit of an endowment ($1$) but consumes only $c_{1t}$. The remainder is saved in the form of money ($Md$).
- **Old:** In the second period, they receive zero endowment but consume $c_{2t+1}$ by exchanging their saved money for goods.
- **Constraint:** $P_t(1 - c_{1t}) = Md$ and $P_{t+1} c_{2t+1} = \Delta M + Md$ (where $\Delta M$ is the government transfer). [[Perry_Central_Bank_Policy_P3.md#page=54]]

### 2. Money as a Transfer Machine
If money supply grows at rate $\mu$, the inflation rate in the steady state will be $\pi = \mu - n$ (where $n$ is population growth).
- **The Distribution Effect:** Because additional new money is typically distributed to the "old" generation, a change in $\mu$ alters the real rate at which money can be accumulated and transferred. 
- **Non-Superneutrality:** This redistribution means that a continuous change in the *growth rate* of money supply ($\mu$) has real effects on consumption levels and resource allocation, effectively proving that money is **not superneutral** in an OLG world. [[Perry_Central_Bank_Policy_P3.md#page=55]]

---

## Strategic Implications: The Walras' Law Link
In the OLG steady state, prices experience a change at a rate where the supply of money expands at the same pace as demand ($g=n$). Deflation must equal the population growth rate to maintain par equilibrium if money stock is constant. When the government intervenes with monetary growth, it effectively uses the OLG structure to tax one generation for the benefit of another (the "Seigniorage" link). [[Perry_Central_Bank_Policy_P3.md#page=54]]

## Evidence / Source Anchors

- Definition of the OLG model based on the Samuelson consumption-loan model: [[Perry_Central_Bank_Policy_P3.md#page=53]]
- Mathematical derivation of the first-order condition for money demand (Equation 6): [[Perry_Central_Bank_Policy_P3.md#page=55]]
- Proof that inflation/deflation must align with population growth in steady state ($g=n$): [[Perry_Central_Bank_Policy_P3.md#page=54]]
- Analysis of how additional money distributed to the old generation breaks superneutrality: [[Perry_Central_Bank_Policy_P3.md#page=55]]

## Related

- [[Neutrality_Of_Money]] — The broader debate OLG seeks to address.
- [[MIU_Model_Sidrauski_Framework]] — The opposing model showing superneutrality.
- [[Inside_Vs_Outside_Money]] — Why the generation gap creates a demand for Outside Money.
- [[Seigniorage_Mechanism]] — How the government captures the generation-transfer value.
- [[OLG_Model_Monetary_Analysis]]
- [[Monetarist_Vs_Keynesian_Monetary_Views]]
