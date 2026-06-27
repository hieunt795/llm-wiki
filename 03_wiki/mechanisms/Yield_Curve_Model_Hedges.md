---
title: Yield Curve Model Hedges
aliases:
- Model-Based Hedging
- State Variable Hedging
- Numerical Bumping
- Risk Neutralization (Model)
type: mechanism
tags:
- hedging
- yield-curves
- quantitative-finance
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch37.md
thesis: Model-based hedging neutralizes a portfolio against the specific state variables
  of a yield curve model, utilizing a system of partial derivatives to ensure that
  small changes in the model's parameters result in zero net change in portfolio value.
source_refs:
- file: During_Fixed_Income_Ch37.md
  page: 392
- file: During_Fixed_Income_Ch37.md
  page: 393
- file: During_Fixed_Income_Ch37.md
  page: 394
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Once a term structure has been captured in a model (like Nelson-Siegel or Vasicek), that model dictates the only possible ways the curve can move. Alexander Düring explains that a "model-implied hedge" is superior to simple duration because it accounts for the unique curvature of the model. However, he warns that a good hedging model must prioritize explaining **daily price changes** ($\Delta P$) over the best absolute yield fit. [[During_Fixed_Income_Ch37.md#page=392]]

## Mechanism: The State Variable Solver

Assume a bond's model price $P$ depends on a set of $k$ time-dependent state variables $\mu$ (e.g., Level, Slope, Hump).

### 1. The Neutrality Condition
To make the portfolio value independent of the model's state variables, the sum of partial derivatives across all assets $i$ must vanish for every variable $j$:
$$\sum_{i} N_i \frac{\partial P_i}{\partial \mu_j} = 0 \quad \forall j = 1 \dots k$$
- **The Rule:** A portfolio of at least $k$ hedge instruments is necessary to completely neutralize a $k$-factor model. [[During_Fixed_Income_Ch37.md#page=393]]

### 2. Numerical Bumping
In many structural models, a closed-form formula for the derivative $\frac{\partial P}{\partial \mu}$ does not exist. 
- **The Process:** Analysts calculate **Numerical Derivatives**. They "bump" (manually increase) each model parameter by a tiny amount (e.g., 0.1bp), record the price change for every instrument, and then solve the linear system using these observed sensitivities. [[During_Fixed_Income_Ch37.md#page=393]]

## Strategic Application: PCA-Neutral Butterfly

A trader given a bond position ($N_B$) can use a 2-factor PCA model to solve for two hedge notionals ($N_1, N_2$) by solving a $3 \times 3$ matrix:
$$\begin{pmatrix} 1 & 0 & 0 \\ \frac{\partial P_B}{\partial \mu_1} & \frac{\partial P_1}{\partial \mu_1} & \frac{\partial P_2}{\partial \mu_1} \\ \frac{\partial P_B}{\partial \mu_2} & \frac{\partial P_1}{\partial \mu_2} & \frac{\partial P_2}{\partial \mu_2} \end{pmatrix} \begin{pmatrix} N_B \\ N_1 \\ N_2 \end{pmatrix} = \begin{pmatrix} \text{Position Size} \\ 0 \\ 0 \end{pmatrix}$$
- This creates a position that is immune to Level and Slope shifts of the curve, isolating only the residual (Curvature) risk. [[During_Fixed_Income_Ch37.md#page=393-394]]

## Evidence / Source Anchors

- Analysis of model-based hedging as an attempt to explanatory price movements: [[During_Fixed_Income_Ch37.md#page=392]]
- Mathematical derivation of the multi-factor neutrality equations: [[During_Fixed_Income_Ch37.md#page=393]]
- Identification of Numerical Bumping as the requirement for structural model sensitivities: [[During_Fixed_Income_Ch37.md#page=393]]
- Formulation of the $k+1$ system for neutralizing a fixed bond position (Equation 36.18): [[During_Fixed_Income_Ch37.md#page=393]]
- Application of PCA factor loadings to derive risk-neutral butterfly weights: [[During_Fixed_Income_Ch37.md#page=394]]

## Related

- [[Principal_Component_Analysis_PCA]] — The source of the factors $(\mu)$.
- [[Butterfly_Trade_Mechanics]] — The primary strategy using these weights.
- [[Duration_Neutral_Hedges]] — The simpler, model-agnostic version.
- [[Nelson_Siegel_Spline_Models]] — The most common model used for state variable hedging.
