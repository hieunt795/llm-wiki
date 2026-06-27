---
title: PCA-Neutral Butterfly Weights
aliases:
- 3-leg PCA Neutrality
- Factor-Neutral Butterfly
- PCA Hedge Weighting
type: mechanism
tags:
- trading-strategies
- yield-curves
- pca
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch37.md
thesis: "PCA-neutral butterfly weighting is a systematic methodology for isolating\
  \ curvature risk by solving a $3 \times 3$ linear system that simultaneously triệt\
  \ tiêu a position's exposure to the first two principal components (Level and Slope)."
source_refs:
- file: During_Fixed_Income_Ch37.md
  page: 394
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The standard butterfly trade aims for duration and slope neutrality. Alexander Düring explains that the most precise way to achieve this is not through maturity-weighting, but through **PCA Neutrality**. By using the empirical factor loadings from a Principal Component Analysis, a trader can ensure that the butterfly is immune to over 95% of aggregate curve variance, leaving a pure bet on the residual Factor 3 (**Curvature**). [[During_Fixed_Income_Ch37.md#page=394]]

## Mechanism: The Matrix Solver

The weights for the three legs (Bullet $N_2$ and Wings $N_1, N_3$) are derived by assuming the state variables $\mu_1$ (Level) and $\mu_2$ (Slope) are the only curve drivers.

### 1. The Sensitivity Identity
The price sensitivity of each bond $i$ to factor $j$ is the product of its [[Bond_Risk_Modified_Duration_And_PVBP|DV01]] ($D_i$) and its PCA factor loading ($f_{j,i}$):
$$\frac{\partial P_i}{\partial \mu_j} = D_i \times f_{j,i}$$

### 2. The 3-Equation System
To solve for a butterfly centered on a 100-unit position in the bullet ($N_2 = \pm 100$), we solve:
$$\begin{pmatrix} 0 & 1 & 0 \\ D_1 f_{1,1} & D_2 f_{1,2} & D_3 f_{1,3} \\ D_1 f_{2,1} & D_2 f_{2,2} & D_3 f_{2,3} \end{pmatrix} \begin{pmatrix} N_1 \\ N_2 \\ N_3 \end{pmatrix} = \begin{pmatrix} \pm 100 \\ 0 \\ 0 \end{pmatrix}$$

- **Equation 2 (Level-Neutral):** Ensures zero P&L from Factor 1 shifts.
- **Equation 3 (Slope-Neutral):** Ensures zero P&L from Factor 2 rotations. [[During_Fixed_Income_Ch37.md#page=394]]

## Strategic Implications: The Residual Bet

Because the trade is neutral to the two factors that explain the vast majority of curve movement, its performance is driven entirely by the **Curvature** (Factor 3).
- **The Alpha:** Profit comes from the "belly" of the curve performing differently than the average of the "wings" in a way that is not correlated with overall rate levels.
- **The Stability:** This trade is far more stable than a simple maturity-weighted butterfly, as the weights are grounded in the actual historical covariance of the specific bond series used. [[During_Fixed_Income_Ch37.md#page=394]]

## Evidence / Source Anchors

- Analysis of the Scalar Product $\mu = y \cdot f$ as the current factor value: [[During_Fixed_Income_Ch37.md#page=394]]
- Identification of the factor loadings as simple constants for the partial derivatives: [[During_Fixed_Income_Ch37.md#page=394]]
- Mathematical formulation of the $3 \times 3$ matrix for PCA-neutral notionals (Equation 36.21): [[During_Fixed_Income_Ch37.md#page=394]]
- Discussion on the sign of the bullet notional reflecting a "rich" or "cheap" view: [[During_Fixed_Income_Ch37.md#page=394]]

## Related

- [[Principal_Component_Analysis_PCA]] — The source of the factor loadings $f_{j,i}$.
- [[Butterfly_Trade_Mechanics]] — The strategy being optimized.
- [[Yield_Curve_Model_Hedges]] — The broader category of model-based risk neutralization.
- [[Yield_Curve_Trading_Strategies]] — Why Factor 3 is the ultimate target of curve relative value.
- [[Curve_Hedged_Bond_Spreads]]
- [[PCA_Yield_Curve_Decomposition]]
