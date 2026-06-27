---
title: 'Mortgage Prepayment Metrics: SMM and CPR'
aliases:
- SMM
- CPR
- Prepayment Speed
- Single Monthly Mortality
- Constant Prepayment Rate
- PSA Benchmark
type: mechanism
tags:
- mortgages
- quantitative-finance
- valuation
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch28.md
thesis: Prepayment metrics translate complex borrower behavior into standardized mathematical
  speeds (SMM and CPR), utilizing logistic mortality models to project future cashflows
  for RMBS valuation.
source_refs:
- file: During_Fixed_Income_Ch28.md
  page: 292
- file: During_Fixed_Income_Ch28.md
  page: 293
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

To value an RMBS, one must estimate the "mortality" of the underlying mortgages at every future payment date. Alexander Düring explains that these speeds are expressed through two primary variables—SMM and CPR—and modeled using statistical functions that bridge the gap between individual borrower decisions and aggregate pool behavior. [[During_Fixed_Income_Ch28.md#page=292]]

## The Core Metrics

### 1. SMM (Single Monthly Mortality)
The percentage of the remaining principal that is prepaid in a given month.
- **Concept:** It is the "hazard rate" of the mortgage pool.
- **Interpretation:** An SMM of 1% means that 1% of the principal available at the start of the month (after scheduled payments) was repaid early. [[During_Fixed_Income_Ch28.md#page=292]]

### 2. CPR (Constant Prepayment Rate)
The annualized version of SMM, assuming the monthly speed remains constant for a year.
- **Formula:** $CPR = 1 - (1 - SMM)^{f}$
- where $f$ is the payment frequency (e.g., $f=12$ for monthly). [[During_Fixed_Income_Ch28.md#page=292]]

## Mechanism: The Logistic Mortality Model

Practitioners use statistical functions to project future SMM based on the refinancing incentive $(s)$.

### 1. The Logistic Function
Düring utilizes a four-parameter logistic function to model mortality:
$$p_k = b_k + (1 - m) \frac{\exp((s-c)/w)}{1 + \exp((s-c)/w)}$$

### 2. Parameter Interpretation
- **$b_k$ (Baseline):** The attrition rate from non-economic factors (moves, deaths).
- **$c$ (Centre):** The level of saving (e.g., 6%) where half of the interest-rate-sensitive borrowers prepay.
- **$w$ (Width):** The uncertainty interval; a narrow $w$ implies a very sensitive "step-like" reaction to rates.
- **$m$ (Saturation):** The share of borrowers who are assumed to never refinance regardless of incentive. [[During_Fixed_Income_Ch28.md#page=293]]

## The PSA (Public Securities Association) Benchmark

While not explicitly detailed in the formulas, the market uses the **PSA Model** as a standardized yardstick.
- **100 PSA:** Assumes CPR starts at 0.2% in month 1, increases by 0.2% each month until month 30, and then remains constant at 6.0% for the life of the pool.
- **Usage:** Prepayment speeds are quoted as a multiple of this benchmark (e.g., "150 PSA"). [[During_Fixed_Income_Ch28.md#page=292]]

## Evidence / Source Anchors

- Definition of Single Monthly Mortality (SMM) and the annualized CPR formula: [[During_Fixed_Income_Ch28.md#page=292]]
- Analysis of the logistic function for modeling aggregate borrower decisions: [[During_Fixed_Income_Ch28.md#page=293]]
- Parameterization of the mortality model (Baseline, Centre, Width, Saturation): [[During_Fixed_Income_Ch28.md#page=293]]
- Visualization of the mortality model as a function of the mortgage-treasury spread (Figure 27.2): [[During_Fixed_Income_Ch28.md#page=294]]
- Discussion on the smoothness benefit of logistic functions for scenario analysis: [[During_Fixed_Income_Ch28.md#page=294]]

## Related

- [[Mortgage_Prepayment_Drivers]] — The economic qualitative inputs for the $s$ variable.
- [[Residential_Mortgage_Backed_Securities_RMBS]] — The instrument being valued.
- [[Negative_Convexity_In_MBS]] — The result of high SMM at low interest rates.
- [[Weighted_Average_Life_WAL]] — The primary summary statistic derived from these speeds.
