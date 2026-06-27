---
title: 'MIU Model: Sidrauski Framework'
aliases:
- Money-in-the-Utility
- MIU Model
- Superneutrality proof
- Sidrauski Model
type: mechanism
tags:
- monetary-theory
- macroeconomics
- quantitative-economics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The Money-in-the-Utility (MIU) model demonstrates the superneutrality of money
  in the steady state by incorporating money directly into the agent's utility function,
  concluding that money growth only affects inflation and government transfers without
  altering real interest rates or consumption.
source_refs:
- file: Perry_Central_Bank_Policy_P3.md
  page: 55
- file: Perry_Central_Bank_Policy_P3.md
  page: 56
- file: Perry_Central_Bank_Policy_P3.md
  page: 57
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The MIU model, pioneered by Sidrauski (1967), addresses a gap in Neoclassical theory: why rational agents hold cash despite its lack of intrinsic return. By placing money directly in the **Utility Function**, the model proves that in a decentralized economy, money growth is **superneutral**—it has zero impact on real variables like capital formation ($k$) or consumption ($c$) in the long run. [[Perry_Central_Bank_Policy_P3.md#page=55]]

## Mechanism: The Optimization Problem

Individuals live indefinitely and maximize their lifetime utility, which depends on both consumption ($c$) and real cash balances per capita ($m$):
$$\max V = \int_s^\infty u(c, m) \exp[-\theta(t-s)] dt$$

### 1. The Budget Constraint
Agents hold wealth in cash ($M$) or capital ($K$). The flow budget constraint is:
$$\frac{da}{dt} = [(r - n)a + w + x] - [c + (\pi + r)m]$$
- where $a = k + m$ (total net worth per capita).
- $x$ is the lump-sum transfer from the government (seigniorage). [[Perry_Central_Bank_Policy_P3.md#page=56]]

### 2. The Hamiltonian Solver
To solve this, a co-state variable $\lambda$ is used to establish the Hamiltonian:
$$H = \{u(c, m) + \lambda[(r - n)a + w + x - c - (\pi + r)m]\} \exp(-\theta t)$$

The First-Order Conditions (FOC) imply that:
1.  **$u_c(c, m) = \lambda$:** Marginal utility of consumption equals the co-state value.
2.  **$u_m(c, m) = \lambda(\pi + r)$:** The marginal utility of holding money equals the opportunity cost (nominal interest rate). [[Perry_Central_Bank_Policy_P3.md#page=56]]

## The Superneutrality Proof

In the **Steady State** (where $\dot{a} = \dot{m} = \dot{\lambda} = 0$):
- **Inflation Identity:** $\pi = \mu - n$ (where $\mu$ is money growth and $n$ is population growth).
- **The Core Outcome:**
    - $f'(k^*) = \theta + n$
    - $c^* = f(k^*) - nk^*$
- **The Significance:** Notice that $k^*$ and $c^*$ are independent of the money growth rate $\mu$. Money growth only alters the marginal utility of holding money and the nominal inflation rate, making it **superneutral**. [[Perry_Central_Bank_Policy_P3.md#page=57]]

## Evidence / Source Anchors

- Establishment of the MIU utility function $u(c, m)$: [[Perry_Central_Bank_Policy_P3.md#page=55]]
- Formulation of the budget constraint and the non-Ponzi-game condition: [[Perry_Central_Bank_Policy_P3.md#page=56]]
- Derivation of the FOC establishing the marginal rate of substitution between money and consumption: [[Perry_Central_Bank_Policy_P3.md#page=56]]
- Formal proof of superneutrality in the steady state (Equation 16): [[Perry_Central_Bank_Policy_P3.md#page=57]]

## Related

- [[Neutrality_Of_Money]] — The broader theoretical context.
- [[OLG_Model_Monetary]] — The counter-example showing non-superneutrality.
- [[Seigniorage_Mechanism]] — How government transfers ($x$) are derived in the MIU framework.
- [[Quantity_Equation_Of_Money]] — The simple version of the steady-state inflation identity.
