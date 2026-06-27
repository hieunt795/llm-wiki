---
title: McCallum Rule (Monetary Base)
aliases:
- McCallum 1988 Rule
- Monetary Growth Rule
- Base Velocity Feedback
type: mechanism
tags:
- monetary-policy
- monetarism
- operational-targets
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The McCallum Rule is an operational guide for monetary policy that targets
  the growth rate of the monetary base, adjusted for changes in the velocity of money
  and deviations of nominal GDP from its target path.
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 200
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

Proposed by Bennett McCallum (1988), this rule serves as the "Quantity-side" counterpart to the Taylor Rule. It is particularly relevant for economies where interest rate transmission is weak or when a central bank wishes to strictly control the "Printing Press" (M0).

## Mechanism

### 1. The Formula
$$\Delta b_t = \Delta x^* - \Delta v^a_t + \lambda(\Delta x^* - \Delta x_{t-1})$$
Where:
- $\Delta b_t$: Target growth of the monetary base (operational target).
- $\Delta x^*$: Target growth of nominal GDP (intermediate target).
- $\Delta v^a_t$: Average growth of base velocity over the past $k$ periods (correction for financial innovation).
- $\Delta x^* - \Delta x_{t-1}$: Nominal GDP gap (cyclical correction).
- $\lambda$: Feedback parameter (how aggressively the CB reacts to GDP deviations).

### 2. Operational Logic
The rule automatically increases the money supply if velocity falls (people are hoarding cash) or if nominal GDP growth is below target, ensuring that the economy has enough "Fuel" to reach its potential.

## Boundaries / Conditions

### The Velocity Instability Problem
The main weakness of the McCallum rule is that in modern financial systems, the **Velocity of Money** ($v$) is highly unstable and difficult to measure in real-time. This makes the $\Delta v^a_t$ term a source of significant noise, leading most central banks to prefer the Taylor (Interest Rate) Rule.

## Evidence / Source Anchors

- Definition of the McCallum Rule and its intuitive formula: [[Perry_Central_Bank_Policy_P4.md#page=200]]
- The role of base velocity in correcting for technological advances: [[Perry_Central_Bank_Policy_P4.md#page=200]]
- Comparison with Taylor Rule and the trend toward interest rates: [[Perry_Central_Bank_Policy_P4.md#page=200]]

## Related

- [[Taylor_Rule_Interest_Rate_Rule]] — The price-side alternative.
- [[Operational_Targets_of_Monetary_Policy]] — Why $b_t$ is chosen.
- [[Nominal_Income_Targeting]] — The strategic framework this rule often supports.
