---
title: Quantity Equation of Money
aliases:
- MV=PY
- Equation of Exchange
- Quantity Theory of Money
type: mechanism
tags:
- economics
- macroeconomics
- monetary-policy
- mathematics
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch01.md"
thesis: The quantity equation ($MV=PY$) is a fundamental accounting identity expressing
  that the total volume of money payments in an economy must equal the nominal value
  of goods and services exchanged.
source_refs:
- file: Fixed_Income_Alexander_During_Ch01.md
  page: 43
- file: Fixed_Income_Alexander_During_Ch01.md
  page: 44
- file: Fixed_Income_Alexander_During_Ch01.md
  page: 45
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

While simple in appearance, the quantity equation represents the mathematical bridge between abstract monetary units and the real economy. Alexander Düring argues that while central banks use this identity to guide policy, the unobservable nature of its variables (particularly velocity) makes it more of a theoretical framework than a practical steering wheel. The equation reveals the four-layer hierarchy through which central banks attempt to control the price level of consumer goods.

## Mechanism

The basic quantity equation is expressed as:
$$MV = PY$$

Where:
- $M$: The **Money Stock** (broad definitions like M2 or M3).
- $V$: The **Velocity of Money** (the frequency with which a unit of money is used).
- $P$: The **Price Level**.
- $Y$: The **Total Volume of Traded Goods** (a proxy for Real GDP). [[Fixed_Income_Alexander_During_Ch01.md#page=43]]

### 1. The Total Differential
To understand how changes in these variables impact inflation ($dP$), Düring takes the total differential of the equation:

$$dP = \frac{M}{Y}dV + \frac{V}{Y}dM - \frac{MV}{Y^2}dY$$

This reveals that higher prices ($dP > 0$) can be obtained through three primary channels:
- **Velocity Increase ($dV > 0$):** People spend money faster.
- **Money Stock Increase ($dM > 0$):** The central bank or commercial banks create more money.
- **Output Decrease ($dY < 0$):** The supply of real goods shrinks. [[Fixed_Income_Alexander_During_Ch01.md#page=43]]

### 2. The Control Hierarchy
Central banks influence the price level ($P$) through a four-step transmission mechanism:

1. **Quantity (I):** Open market operations adjust central bank reserves.
2. **Price (II):** This influences interest rates on central bank money.
3. **Quantity (III):** Interest rates influence the demand for broad money ($M$).
4. **Price (IV):** Broad money supply eventually impacts the price level ($P$) of goods.

This process operates with a **long and variable lag**, typically estimated at 12–18 months. [[Fixed_Income_Alexander_During_Ch01.md#page=44]]

### Boundaries / Conditions

### 1. The Velocity Breakdown
The term $dV$ is generally considered unsuitable for monetary policy because it is impossible to control.
- **Hoarding:** If households hoard cash, a change in $M$ is simply offset by an opposing change in $V$, leaving $P$ unchanged.
- **Loss of Faith:** If the public loses faith in the currency ($V \to 0$), the central bank loses all control over the price level ($dP/dM \to 0$) as society resorts to barter or **Dollarization**. [[Fixed_Income_Alexander_During_Ch01.md#page=45]]

### 2. The Observability Problem
Düring critiques the equation as "somewhat of a fiction" because:
- $M$ has multiple competing definitions (M0–M3).
- $V$ is unobservable and can only be defined by rearranging the equation ($V = PY/M$).
- Consequently, the equation is often a circular definition rather than an empirical guideline. [[Fixed_Income_Alexander_During_Ch01.md#page=44]]

## Evidence / Source Anchors

- Definition of $MV=PY$ and its variables: [[Fixed_Income_Alexander_During_Ch01.md#page=43]]
- Derivation of the total differential equation (6.2): [[Fixed_Income_Alexander_During_Ch01.md#page=43]]
- Description of the four-layer control hierarchy: [[Fixed_Income_Alexander_During_Ch01.md#page=44]]
- Analysis of the 12-18 month transmission lag: [[Fixed_Income_Alexander_During_Ch01.md#page=44]]
- Discussion on the breakdown of $V$ and dollarization: [[Fixed_Income_Alexander_During_Ch01.md#page=45]]

## Related

- [[Monetarist_Vs_Keynesian_Monetary_Views]] — The debate over which term in the differential ($dM$ or $dY$) is paramount.
- [[Bank_Money_Creation]] — The process that determines the $M$ variable.
- [[Monetary_Policy_Targeting]] — The frameworks used to choose the desired $dP$.
- [[Liquidity_Preference_Theory]] — Explains the fluctuations in $V$ mentioned here.
- [[Inside_Vs_Outside_Money]] — $M$ consists mostly of "Inside Money" which the central bank only influences indirectly.
