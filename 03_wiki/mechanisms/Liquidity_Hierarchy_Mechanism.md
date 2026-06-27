---
title: Liquidity Hierarchy Mechanism
aliases:
- Pricing Hierarchy
- Market Repricing Chain
- On-the-run Premium
type: mechanism
tags:
- market-infrastructure
- trading
- liquidity
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch12.md
thesis: The market for fixed income instruments is organized as a hierarchy of liquidity,
  where new information is first reflected in the most liquid instruments (the pricing
  anchor) and then propagates to less liquid securities through algorithmic and dealer-driven
  pricing models.
source_refs:
- file: During_Fixed_Income_Ch12.md
  page: 85
- file: During_Fixed_Income_Ch12.md
  page: 86
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Market efficiency does not imply that all prices react to news simultaneously. Instead, all markets have a structural hierarchy of instruments. News affects the "anchors" (the most liquid instruments) first, and the rest of the market reacts through the repricing of these anchors. This hierarchy is self-reinforcing as macroeconomic views are primarily expressed through these highly liquid vehicles. [[During_Fixed_Income_Ch12.md#page=85-86]]

## Mechanism: The Repricing Chain

### 1. The Pricing Anchors (Top Tier)
The instruments that reflect new information (economic data, central bank news) first.
- **In the US:** On-the-run (most recently issued) Treasury securities and Agency mortgage bonds.
- **In Europe and Japan:** Bond futures contracts. [[During_Fixed_Income_Ch12.md#page=85]]

### 2. Algorithmic Propagation (Middle Tier)
Market makers use pricing models that link less liquid instruments (Off-the-run bonds, corporate debt) to the top-tier anchors. 
- **The Calculation:** Price = Output of Hierarchical Model (Anchor price + Spread) + Adjustments for local supply/demand. [[During_Fixed_Income_Ch12.md#page=86]]

### 3. The Opacity Zone (Bottom Tier)
Immediately after a major data release, pricing for less liquid instruments can become opaque. This occurs because market participants are waiting for the pricing anchors to settle on a new equilibrium before they can reliably price the rest of the curve. [[During_Fixed_Income_Ch12.md#page=86]]

## Strategic Consequences

### The On-the-run Premium
The pricing hierarchy can lead to a permanent **Liquidity Premium** for benchmark bonds. 
- **US Treasury Market:** Benchmark bonds often carry a premium because they are the first to be traded on news.
- **Europe/Japan:** This premium is less pronounced for government bonds because bond futures take on the primary role of the pricing anchor. [[During_Fixed_Income_Ch12.md#page=86]]

### Information Leakage and Best Execution
When a large order is shown to multiple dealers (In Competition), information about the trade interest "leaks" to the top-tier market. Dealers will adjust their pricing of the anchors in anticipation of the trade, which can move the price against the client before the trade is even executed. [[During_Fixed_Income_Ch12.md#page=97]]

## Evidence / Source Anchors

- Definition of the hierarchy of instruments and its impact on news pricing: [[During_Fixed_Income_Ch12.md#page=85]]
- Identification of specific anchors (T-bonds vs. Bond Futures): [[During_Fixed_Income_Ch12.md#page=85]]
- Analysis of the self-reinforcing nature of liquidity premiums: [[During_Fixed_Income_Ch12.md#page=86]]
- Discussion on the opacity zone post-data release: [[During_Fixed_Income_Ch12.md#page=86]]

## Related

- [[On_The_Run_Liquidity_Premium]] — The specific manifestation of this hierarchy.
- [[Bond_Futures_Contract_Design]] — Why futures act as anchors in Europe/Japan.
- [[Information_Leakage_In_Trading]] — The risk inherent in the repricing chain.
- [[Market_Maker_Vs_Liquidity_Provider]] — The actors who manage the hierarchical pricing models.
