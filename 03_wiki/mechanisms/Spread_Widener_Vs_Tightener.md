---
title: Spread Widener vs Tightener
aliases:
- Spread Widener
- Spread Tightener
- Underweight vs Overweight (Bonds)
- Relative Value Expressing
type: mechanism
tags:
- trading-strategies
- valuation
- portfolio-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch33.md
thesis: Spread wideners and tighteners are the primary directional modes for expressing
  relative value views, where a widener bets on a bond's underperformance relative
  to a curve, and a tightener bets on its outperformance.
source_refs:
- file: During_Fixed_Income_Ch33.md
  page: 363
- file: During_Fixed_Income_Ch33.md
  page: 364
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Relative value analysis identified via spline spreads or ASW spreads is implemented through two fundamental positioning archetypes. Alexander Düring explains that the nomenclature can be confusing in global markets where spreads can be negative (e.g., bonds trading below the swap curve). To maintain consistency, professional desks link the term "Widener" to a short bond position and "Tightener" to a long bond position, regardless of the absolute spread level. [[During_Fixed_Income_Ch33.md#page=363]]

## 1. Spread Tightener (Cược thu hẹp spread)
- **Market View:** The bond is "cheap" (high yield/positive spline spread) and its yield will decline toward the benchmark.
- **Positioning:** Long the bond and **Pay the Curve** (Short the benchmark/swap).
- **In Index Tracking:** This is expressed as an **Overweight** position relative to the bond's weight in the benchmark index. [[During_Fixed_Income_Ch33.md#page=364]]

## 2. Spread Widener (Cược dãn rộng spread)
- **Market View:** The bond is "rich" (low yield/negative spline spread) and its yield will rise faster (or fall slower) than the benchmark.
- **Positioning:** Short the bond and **Receive the Curve** (Long the benchmark/swap).
- **In Index Tracking:** This is expressed as an **Underweight** position relative to the benchmark index. [[During_Fixed_Income_Ch33.md#page=363-364]]

## Mechanism: Curve Expression

Unlike swaps, a "curve" cannot be traded directly. Traders express the benchmark leg of these trades using:
- **Asset Swaps:** For corporate or high-grade bank debt.
- **Interpolated Swaps (I-spread):** For speed and lower transaction costs.
- **Butterfly/Spread Overlay:** If the bond and the curve benchmark have a duration mismatch, the trader embeds the view in a multi-legged position to neutralize slope risk. [[During_Fixed_Income_Ch33.md#page=364]]

## Evidence / Source Anchors

- Definition of spread widener (Selling bond, receiving curve): [[During_Fixed_Income_Ch33.md#page=363]]
- Analysis of nomenclature consistency in positive and negative spread environments: [[During_Fixed_Income_Ch33.md#page=364]]
- Description of the 'Overweight' and 'Underweight' equivalents for index trackers: [[During_Fixed_Income_Ch33.md#page=364]]
- Identification of Asset Swaps as the default instrument for express spread views: [[During_Fixed_Income_Ch33.md#page=363]]
- Schematic of spread widener payoff profiles (Figure 32.1): [[During_Fixed_Income_Ch33.md#page=363]]

## Related

- [[Bond_Relative_Value_Valuation]] — The analysis that generates these trades.
- [[Asset_Swap_Spread_ASW]] — The primary implementation vehicle.
- [[I_Spread_Vs_ASW]] — The trade-off in execution choice.
- [[Bond_Index_Principles]] — The context for Overweight/Underweight strategies.
