---
title: Central Bank Quadratic Loss Function
aliases:
- Macroeconomic Welfare Function
- CB Loss Function
- Price-Output Trade-off Formula
type: mechanism
tags:
- monetary-policy
- mathematics
- optimization
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: Mục tiêu của ngân hàng trung ương được biểu diễn một cách toán học dưới dạng
  hàm tổn thất bậc hai, trong đó mục tiêu là tối thiểu hóa tổng có trọng số bình phương
  các độ lệch của lạm phát so với mục tiêu và sản lượng so với mức tiềm năng.
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 162
created: '2026-04-18'
updated: '2026-04-22'
---

## Thesis

The loss function is the operational translation of "Public Welfare." By using a quadratic form, the model penalizes large deviations more heavily than small ones and treats positive and negative errors (over-shooting vs under-shooting) as equally harmful.

## Mechanism

### 1. The Standard Inflation-Output Loss Function
$$L = \frac{1}{2} [\omega_p(\pi_t - \pi^*)^2 + \omega_y(y_t - y^*)^2]$$
Where:
- $\pi_t - \pi^*$: Inflation gap (Actual vs Target).
- $y_t - y^*$: Output gap (Actual vs Potential).
- $\omega_p, \omega_y$: Policy weights (Preferences) for price stability vs growth.

### 2. The Nominal Income Target Alternative
$$L = \frac{1}{2} [(\pi_t + \Delta y_t) - (\pi + \Delta y)^*]^2$$
This function targets the sum of inflation and real growth, providing more flexibility during supply-side shocks.

## Decision Analysis: Response to Shocks

- **Demand Shocks:** Both price and nominal income targeting lead to the same optimal response (stabilize both).
- **Supply Shocks:** A conflict arises.
    - Strict price targeting ignores output loss, potentially causing a deep recession.
    - Nominal income targeting allows for a "compromise," accepting slightly higher inflation to prevent a collapse in output.

## Evidence / Source Anchors

- Mathematical formulation of the quadratic loss function: [[Perry_Central_Bank_Policy_P4.md#page=162]]
- Analysis of weights ($\omega$) reflecting policy preferences: [[Perry_Central_Bank_Policy_P4.md#page=163]]
- Comparison of targeting strategies under supply shocks: [[Perry_Central_Bank_Policy_P4.md#page=164]]

## Related

- [[Inflation_Targeting_Framework_ITF]] — The regime that uses function (1).
- [[Monetary_Policy_Strategic_Framework]] — The broader context.
- [[Sacrifice_Ratio_Mechanics]] — The cost of minimizing this loss function too aggressively.
