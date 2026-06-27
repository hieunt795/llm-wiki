---
title: Commodities
aliases: []
type: concept
tags: [macro, commodities, financial-engineering]
status: reviewed
confidence: 4
half_life_years: 10
school: 'Practitioner'
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: "Neftci Chapter 7"
thesis: "Commodities represent a tangible asset class characterized by physical constraints—storage costs, heterogeneity, and tangibility—that necessitate specialized financial engineering beyond standard homogeneous asset models."
source_refs: []
created: '2026-04-21'
updated: '2026-04-28'
---

# Commodities

## 1. Thesis & Overview
[RAW][LLM] Commodities represent a tangible asset class that differs fundamentally from traditional financial assets (fixed income, currencies, equities) due to their physical nature. In financial engineering, commodities are used to hedge production/consumption risks and as an investment class via "financialization."

## 2. Unique Characteristics vs. Fixed Income
[RAW] Unlike financial instruments, commodities possess physical constraints that must be modeled in cash flow engineering:

### A. Storage Costs
- **Mechanism:** Holding a physical commodity requires payment for warehousing, insurance, and maintenance.
- **Impact:** These costs create a "carry" drag on spot holdings, directly influencing the relationship between spot and futures prices.
- **Contrast:** Fixed income instruments (e.g., [[Bonds]]) and currencies do not incur significant storage costs.
- **Related Concept:** [[Convenience_Yield]] (The implicit return for holding physical inventory).

### B. Heterogeneity (Grade/Quality)
- **Mechanism:** Commodities are non-homogeneous. Different grades (e.g., Sweet vs. Sour Crude) or geographical locations (e.g., WTI vs. Brent) lead to price differentials.
- **Impact:** Non-homogeneity can limit arbitrage strategies and requires careful standardization in futures contracts.
- **Contrast:** Currencies and standard equity shares are perfectly homogeneous.

### C. Tangibility
- **Mechanism:** Commodities are physical goods.
- **Benefit:** Their physical reality makes them ideal for observing market dynamics like open interest, volume, and the term structure of futures.

### D. Engineering Complexity
- **[RAW][LLM] Comparison:** Financial engineering for commodities is significantly more complex than for homogeneous assets (e.g., [[Currencies]], [[Bonds]]).
- **Factors:** The presence of **Storage Costs**, **Insurance**, and **Quality/Grade Differentials** prevents a simple "one-size-fits-all" pricing model.
- **Impact:** Each commodity requires a specialized contractual equation that accounts for its specific physical basis and delivery location.

## 3. Financialization of Commodities
[RAW] The transition of commodities from purely physical trade to an institutional asset class:
- **Vehicles:** [[Commodity_Swaps]], Futures, and Commodity-linked ETFs.
- **Participants:** Shift from just producers/consumers to include institutional and retail investors.

## 4. Basis Risk in Commodities
[RAW][LLM] In energy and broader commodity markets, the basis is complicated by three factors:
1. **Locational Basis:** Difference between delivery point and physical asset location.
2. **Product/Quality Basis:** Difference between the grade of the underlying and the delivery grade.
3. **Calendar (Spread) Basis:** Time difference between contract maturity and physical delivery needs.

## 5. Failure Conditions
[RAW]
- **Arbitrage Friction:** Physical delivery constraints and non-homogeneity prevent "perfect" arbitrage between markets.
- **Liquidity Imbalance:** Front-month (prompt) contracts are significantly more liquid than back-month contracts, complicating long-term hedging.

─────────────────────────────────────────────
WRITEBACK
> TYPE 2: SPAWN Commodities.md — Ingested from Neftci Ch7, S7.1.
