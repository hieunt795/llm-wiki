---
title: Market Depth vs Breadth
aliases:
- Market Depth
- Market Breadth
- Macroscopic Liquidity
- Microscopic Liquidity
- Độ rộng và độ sâu thị trường
type: mechanism
tags:
- market-infrastructure
- liquidity
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch19.md
thesis: The distinction between market breadth (microscopic) and depth (macroscopic)
  defines the market's resilience, differentiating between the ability to execute
  single isolated trades and the capacity to absorb large-scale correlated flows during
  periods of systemic stress.
source_refs:
- file: During_Fixed_Income_Ch19.md
  page: 180
- file: During_Fixed_Income_Ch19.md
  page: 181
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Analysts often confuse competitive dealer pricing with resilient market capacity. Alexander Düring bóc tách sự phân rã này thành hai chiều kích: **Market Breadth** (Độ rộng) và **Market Depth** (Độ sâu). Understanding this difference is critical for risk managers, as traditional liquidity indicators often only measure breadth, leaving the market blind to the "disconcerting" disappearance of depth during a crisis. [[During_Fixed_Income_Ch19.md#page=180-181]]

## 1. Market Breadth (Microscopic Liquidity)
- **Concept:** The ability to execute a single, isolated transaction at or near the current market price.
- **Drivers:** Dealer competition, the number of market makers, and the willingness of non-bank dealers to provide quotes.
- **Observation:** Easily seen through pre-trade (bid-ask spreads) and post-trade (executed volumes) indicators.
- **The Catch:** Breadth tells you nothing about what happens if *everyone* wants to trade in the same direction at once. [[During_Fixed_Income_Ch19.md#page=180]]

## 2. Market Depth (Macroscopic Liquidity)
- **Concept:** The aggregate risk-absorption capacity of the market to handle correlated, non-diversifiable flows.
- **Drivers:** Total balance sheet capacity of all liquidity providers (including non-dealers) and their willingness to hold positions in the face of volatility.
- **The Paradox:** Lack of depth is often invisible during normal times when flows are diversifiable. It only reveals itself when investors attempt to exit a subset of securities simultaneously.
- **The Disconcerting Truth:** Macroscopic liquidity cannot be measured by simply scaling up microscopic indicators. [[During_Fixed_Income_Ch19.md#page=181]]

## Strategic Implications: Risk Absorption

### The Warehouse Problem
Market making requires "warehousing" securities until an offsetting client is found. Depth is determined by how much "warehouse space" (balance sheet) dealers can commit. If volatility increases, the capital cost of warehousing rises, causing a sudden contraction in market depth even if breadth (number of dealers) appears unchanged. [[During_Fixed_Income_Ch19.md#page=177]]

### Search Cost vs. Price Impact
- **Exchanges:** Reduce search costs by concentrating participants in a Central Limit Order Book (CLOB). They provide high transparency but suffer from immediate **Information Leakage**.
- **OTC Markets:** Market makers eliminate the search problem by acting as willing counterparties, but they charge for this "Warehouse" service via the bid-offer spread. [[During_Fixed_Income_Ch19.md#page=177-178]]

## Evidence / Source Anchors

- Schematic distinction between Microscopic (Breadth) and Macroscopic (Depth): [[During_Fixed_Income_Ch19.md#page=180]]
- Identification of balance sheet capacity and risk absorption as the drivers of depth: [[During_Fixed_Income_Ch19.md#page=181]]
- Analysis of correlated flows as the primary test of market depth: [[During_Fixed_Income_Ch19.md#page=181]]
- Discussion on the transparency vs. information leakage trade-off between exchanges and OTC: [[During_Fixed_Income_Ch19.md#page=178]]

## Related

- [[Liquidity_Measurement_Taxonomy]] — How to measure these two dimensions.
- [[Information_Leakage_In_Trading]] — The primary cost of exchange-based breadth.
- [[Bid_Ask_Bounce_Mechanism]] — How a lack of breadth creates volatility.
- [[Inventory_Risk_Management]] — The dealer-side driver of market depth.
