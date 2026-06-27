---
title: Index Aggregation for Optimisation
aliases:
- Subindex Mapping
- Covariance Proxy Mapping
- Bucket-based Optimisation
- Maturity Bucket Mapping
type: mechanism
tags:
- portfolio-management
- quantitative-finance
- yield-curves
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch38.md
thesis: Index aggregation is a dimension-reduction technique that solves the 'aging'
  problem of bond covariance matrices by mapping individual securities to standardized
  sub-index maturity buckets, ensuring stationary risk inputs for portfolio optimisation.
source_refs:
- file: During_Fixed_Income_Ch38.md
  page: 401
- file: During_Fixed_Income_Ch38.md
  page: 402
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Traditional mean-variance optimisation fails when applied to individual bonds because a bond's risk profile (duration) is non-stationary—it decays as the instrument ages. Alexander Düring explains that the "standard solution" is to abstract away from individual bonds. By using **Index Aggregation**, portfolio managers can treat a 5-year bond not as an idiosyncratic asset, but as a realization of a generic, stationary maturity bucket. [[During_Fixed_Income_Ch38.md#page=401]]

## Mechanism: Sub-Index Mapping

The optimization problem is restructured to use high-level "Asset Classes" rather than ISINs.

### 1. Defining the Buckets
Analysts use sub-indices published by providers (e.g., Bloomberg/iBoxx) that segment the market by maturity and rating:
- **Example:** iBoxx Euro Corporate A 3–5Y.
- **The Stationary Property:** These indices are rebalanced monthly. As a bond in the index "ages" past the 3-year floor, it is replaced by a newer 5-year bond. This ensures the index's duration and variance remain relatively constant over time. [[During_Fixed_Income_Ch38.md#page=401]]

### 2. The Factor Equation
The return $r_i$ of an individual bond is decomposed into a class-level factor and an idiosyncratic error:
$$r_i(t) = \beta_i f_k(t) + \epsilon_i(t)$$
- **$f_k$:** The return of the sub-index bucket.
- **$\epsilon_i$:** The specific risk of the issuer (ignored for high-level macro allocation). [[During_Fixed_Income_Ch38.md#page=401-402]]

### 3. Numerical Stability
By reducing the number of variables from thousands of bonds to 10-20 buckets, the covariance matrix $V$ becomes much smaller and easier to invert. This eliminates the "numerical instability" that plagues large-scale Markowitz solvers. [[During_Fixed_Income_Ch38.md#page=401]]

## Strategic Implications: The Map back to Reality

Once the optimal weights for the **Buckets** are found, the manager maps them back to individual assets:
- **Rule of Thumb:** Within each bucket, assets are held in their natural **Market Capitalisation** weights.
- **Credit Caveat:** Düring warns that for credit-heavy portfolios, a higher number of factors is needed (Factor Decomposition) because industry-specific or issuer-specific idiosyncratic risks $(\epsilon)$ are too large to be ignored. [[During_Fixed_Income_Ch38.md#page=402]]

## Evidence / Source Anchors

- Analysis of the finite lifetime of fixed income securities making individual bond covariance meaningless: [[During_Fixed_Income_Ch38.md#page=401]]
- Description of the 'Standard Solution' via abstraction to bond indices: [[During_Fixed_Income_Ch38.md#page=401]]
- Mathematical derivation of the factor-based return model (Equation 37.11): [[During_Fixed_Income_Ch401.md#page=401]]
- Identification of sub-index mapping as a tool for numerical stability in matrix inversion: [[During_Fixed_Income_Ch38.md#page=401]]
- Comparison of factor requirements between liquid bond markets (low factors) and equity/credit markets (high factors): [[During_Fixed_Income_Ch38.md#page=402]]

## Related

- [[Mean_Variance_Optimisation_Theory]] — The engine that uses these aggregated inputs.
- [[Bond_Index_Rebalancing_Mechanics]] — How the sub-index maintains its stationary property.
- [[Principal_Component_Analysis_PCA]] — An alternative way to extract the factors $f_k$.
- [[Portfolio_Risk_Budgeting_And_Optimization]] — How the resulting bucket weights are rationed.
