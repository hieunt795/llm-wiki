---
title: Bond Trading Simplicity Principle
aliases:
- Simplicity in Trading
- Over-engineered Strategy Risk
- Execution Friction
type: mechanism
tags:
- trading
- risk-management
- behavioral-finance
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch33.md
thesis: The simplicity principle asserts that the robustness of a trading strategy
  is inversely proportional to its technical complexity, emphasizing that over-engineered
  strategies suffer from excessive re-adjustment costs and blurred performance attribution.
source_refs:
- file: During_Fixed_Income_Ch33.md
  page: 367
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

In the high-stakes world of institutional bond trading, there is a constant temptation to build increasingly complex multi-asset portfolios. Alexander Düring argues that **Simplicity is a virtue**. While a 6-legged trade might perfectly neutralize every known risk on a spreadsheet, the operational reality of managing such a position often leads to a decay in performance. [[During_Fixed_Income_Ch33.md#page=367]]

## Mechanism: The Complexity Decay

Over-engineered strategies suffer from three systematic drains on P&L:

### 1. Re-adjustment Friction
Fixed income instruments have finite lifetimes. Their durations and PVBPs decay every day.
- **The Problem:** A complex 6-legged trade requires constant re-balancing to maintain neutrality.
- **The Cost:** Each re-balancing involves crossing a bid-offer spread. In a multi-leg trade, these costs accumulate geometrically, often eating a significant portion of the projected "relative value" profit. [[During_Fixed_Income_Ch33.md#page=367]]

### 2. Performance Attribution Blur
When a trade involves many parts, it becomes difficult to identify *why* it is making or losing money.
- **The Noise:** Is the profit coming from the core thesis, or from a temporary mispricing in one of the hedge legs?
- **The Consequence:** Without clear attribution, the trader cannot make rational decisions about whether to increase the position or cut the loss. [[During_Fixed_Income_Ch33.md#page=367]]

### 3. Model Dependency
Complex trades rely on sophisticated models (like PCA or Splines) to determine weights.
- **The Risk:** If the model's assumptions fail (e.g., correlations break down during a crisis), the "neutral" hedge can suddenly become a source of massive directional risk. Simple trades are less sensitive to these model failures. [[During_Fixed_Income_Ch33.md#page=367]]

## Evidence / Source Anchors

- Analysis of simplicity as a fundamental requirement for active trading: [[During_Fixed_Income_Ch33.md#page=367]]
- Warning against over-engineered strategies with too many moving parts: [[During_Fixed_Income_Ch33.md#page=367]]
- Description of the 'blurring' of performance attribution in complex trades: [[During_Fixed_Income_Ch33.md#page=367]]
- Discussion on the excessive re-adjustment needs of complex portfolios: [[During_Fixed_Income_Ch33.md#page=367]]

## Related

- [[Trading_Strategy_And_Principles]] — The broader context (Pillar #4: Consistency).
- [[Trade_Implementation_Consistency]] — Detailed view of implementation failures.
- [[Yield_Curve_Trading_Strategies]] — Where the temptation for complexity (Order 4+ trades) is highest.
- [[Principal_Component_Analysis_PCA]] — The tool often used to justify (or over-complicate) curve trades.
