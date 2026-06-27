---
title: Yield Curve Fitting Optimization
aliases:
- Curve Fitting
- DV01 Trick
- DV01 Weighted Fitting
- Outlier Removal
- Minimum Square Error Fitting
- Tối ưu hóa đường cong
type: mechanism
tags:
- quantitative-finance
- yield-curves
- mathematics
- optimization
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch20.md
thesis: Yield curve fitting is the optimization process of finding model parameters
  that minimize price errors, utilizing the 'DV01 trick' to transform non-linear yield
  searches into high-speed linear price approximations and outlier removal to ensure
  data integrity.
source_refs:
- file: During_Fixed_Income_Ch20.md
  page: 203
- file: During_Fixed_Income_Ch20.md
  page: 204
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Fitting a parametric curve to market data is a computationally intensive task. While economists often prefer to minimize errors in **Yield** space (as yields are intuitive), Alexander Düring explains that traders and practitioners use **Price** space with a specific weighting to achieve extreme computational speed without sacrificing accuracy. This process is further refined through iterative **Outlier Removal** to strip away polluted data. [[During_Fixed_Income_Ch20.md#page=203]]

## Mechanism: The DV01 Optimization Trick

### 1. The Standard Error Term (Slow)
The most common theoretical approach is to minimize the sum of squared yield errors:
$$E = \sum (y_i - y_{model,i})^2$$
- **The Problem:** Calculating $y_{model}$ from a bond price requires a non-linear root search for every bond in every iteration. This is very slow for large datasets. [[During_Fixed_Income_Ch20.md#page=203]]

### 2. The Weighted Price Term (Fast)
Since yield changes are well-approximated by $\Delta y = \Delta P / DV01$ for small changes, the error term can be rewritten as:
$$E = \sum \frac{1}{DV01_i^2} (P_i - P_{model,i})^2$$
- **The Benefit:** $P_{model}$ is a linear function of the discount factors (which are direct outputs of the model).
- **The Speed:** This approximation is **several orders of magnitude faster** than yield-based fitting, as it avoids millions of root-search operations. [[During_Fixed_Income_Ch20.md#page=203-204]]

## Data Integrity: Outlier Removal

Even with a perfect model, noisy market data (polluted prices, incorrect bond static data, or call options not marked in the system) will distort the curve.

### 1. The Iterative Pruning
1.  Fit the curve to the full sample.
2.  Evaluate the **Spline Spread** for each bond.
3.  Remove bonds that are more than a certain number of standard deviations away from the implied yield.
4.  Re-fit the curve to the stable sample. [[During_Fixed_Income_Ch20.md#page=204]]

### 2. The Systematic Removal Problem
Düring warns against blindly removing bonds with "distorted" prices, such as CTDs (Cheapest-to-deliver) or newly issued benchmarks.
- **The Conflict:** These bonds carry systematic **Repo or Liquidity Premia**. Removing them makes the curve "cleaner" but less representative of the actual liquid market. 
- **The Recommendation:** The "true" discount curve lies somewhere between the liquid benchmarks and the illiquid off-the-runs. Equal weighting of all bonds in the sample usually produces a more robust result than aggressive exclusion. [[During_Fixed_Income_Ch20.md#page=204]]

## Evidence / Source Anchors

- Formula for yield-based error minimization: [[During_Fixed_Income_Ch20.md#page=203]]
- Mathematical derivation of the DV01-weighted price error approximation: [[During_Fixed_Income_Ch20.md#page=203]]
- Analysis of computational speed-up using price-space optimization: [[During_Fixed_Income_Ch20.md#page=204]]
- Description of iterative outlier removal techniques: [[During_Fixed_Income_Ch20.md#page=204]]
- Critique of removing benchmark bonds due to liquidity/repo distortions: [[During_Fixed_Income_Ch20.md#page=204]]

## Related

- [[Yield_Curve_Representations]] — What is being fitted.
- [[Bond_Risk_Modified_Duration_And_PVBP]] — Definition of the $DV01$ weighting factor.
- [[Discount_Factors_Theory]] — The linear building blocks of $P_{model}$.
- [[Spline_Spread_Dispersion]] — The metric used to identify outliers.
