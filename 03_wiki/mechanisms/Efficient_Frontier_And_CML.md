---
title: Efficient Frontier and CML
aliases:
- Efficient Frontier
- Capital Markets Line
- CML
- Market Portfolio
- Dominance (Finance)
type: mechanism
tags:
- portfolio-management
- quantitative-finance
- economic-theory
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch38.md
thesis: The Efficient Frontier and Capital Markets Line (CML) represent the geometric
  limits of risk-return optimization, identifying the 'Market Portfolio' as the unique
  point of maximum efficiency in a frictionless world.
source_refs:
- file: During_Fixed_Income_Ch38.md
  page: 396
- file: During_Fixed_Income_Ch38.md
  page: 397
- file: During_Fixed_Income_Ch38.md
  page: 398
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

In the geometry of portfolio risk and return, investors seek "dominance": a portfolio is dominant if it has higher returns for the same risk, or lower risk for the same return. Alexander Düring explains that the **Efficient Frontier** and the **CML** define the boundary of these choices. However, he warns that the traditional interpretation of these lines relies on the **Efficient Market Hypothesis (EMH)**—a "sleight of hand" that assumes markets are already at equilibrium without explaining how they got there. [[During_Fixed_Income_Ch38.md#page=396-397]]

## Mechanism: The Geometric Bounds

### 1. The Efficient Frontier (Markowitz Bullet)
- **Concept:** The convex hull of all possible asset combinations.
- **Selection:** Investors should only choose portfolios on the **upper part** of this hull, as these are the only ones that are not dominated by another set of weights. [[During_Fixed_Income_Ch38.md#page=396]]

### 2. The Capital Markets Line (CML)
- **Mechanism:** A line drawn from the risk-free rate ($V=0$) that is tangential to the efficient frontier.
- **The Market Portfolio:** The point of tangency. 
- **The Optimization:** Every point on the CML represents a combination of the risk-free asset and the market portfolio. Because the CML is above the frontier, it "dominates" all other possible allocations. [[During_Fixed_Income_Ch38.md#page=397]]

## Strategic Implications: The Friction Failure

The CML and the optimality of the "Market Portfolio" (holding all assets at market weight) rely on the **Miller–Modigliani Theorem**. Düring bóc tách những rào cản thực tế làm sụp đổ mô hình này:

1.  **Tax and Friction Costs:** In the real world, few investors can access every global market at the same cost. High taxes or transaction costs in specific sectors force investors to skew away from the "Market Portfolio."
2.  **Borrowing Constraints:** The CML assumes investors can borrow at the risk-free rate to leverage their market exposure. In reality, retail and many institutional investors face much higher borrowing costs or regulatory bans on leverage. [[During_Fixed_Income_Ch38.md#page=397-398]]
3.  **The Information Loop:** If every investor follows the CML and holds only the market portfolio, mis-priced assets would never correct. The rise of passive investing may paradoxically increase the returns available to **Active Investors** who provide the informational grease that makes the EMH "appear" to work. [[During_Fixed_Income_Ch38.md#page=384]]

## Evidence / Source Anchors

- Definition of portfolio dominance in the risk-variance coordinate system: [[During_Fixed_Income_Ch38.md#page=396]]
- Analysis of the CML as the tangent through the riskless asset: [[During_Fixed_Income_Ch38.md#page=397]]
- Description of the 'Market Portfolio' as independent of individual risk preferences: [[During_Fixed_Income_Ch38.md#page=397]]
- Critique of the EMH as being "silent" on how information is incorporated into prices: [[During_Fixed_Income_Ch38.md#page=384]]
- Identification of taxes and friction as the primary breakers of Miller-Modigliani optimality: [[During_Fixed_Income_Ch38.md#page=397-398]]

## Related

- [[Mean_Variance_Optimisation_Theory]] — The underlying engine.
- [[Index_Tracking_And_Replication_Risk]] — The practical implementation of the "Market Portfolio."
- [[Preferred_Habitat_Market_Distortions]] — Why different investors choose different spots on the CML.
- [[Market_Portfolio_Paradox]] — Why "holding everything" is a risk in bonds.
