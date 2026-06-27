---
title: Convenience Yield
aliases:
- cy
- Lợi suất tiện ích
type: concept
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: "Neftci_Principles.md"
thesis: Convenience yield is the non-monetary benefit (premium) of holding physical
  inventory over a futures contract, primarily driven by stockout avoidance and supply
  scarcity.
source_refs:
- file: Neftci_Principles.md
  page: 1
created: '2026-04-16'
updated: '2026-04-16'
---

# Convenience Yield

## 1. Definition & Core Thesis
[RAW][LLM] **Convenience Yield (cy)** is the premium a consumer is willing to pay for the ability to consume a commodity now rather than at some future date. It represents the implicit return on holding physical inventory, which provides operational flexibility and mitigates the risk of supply disruptions.

In financial engineering, it is often treated as an "abstract placeholder" to reconcile the observed spot-futures price relationship when markets are in **backwardation** ($F < S$).

## 2. Transmission Mechanism: Scarcity & Inventory
[RAW] The magnitude of the convenience yield is inversely related to inventory levels (scarcity):
- **Low Inventory (Scarcity):** Leads to a high $cy$. Consumers fear stockouts and are willing to pay a high premium for spot delivery.
- **High Inventory (Balance):** Leads to a low or zero $cy$. The "convenience" of holding physical stock is minimized when supply is abundant.

### The Stockout Insurance Mechanism
- **Process:** Holding physical inventory acts as an insurance policy against the high cost of production shutdowns (e.g., a refinery closing due to lack of crude).
- **Cost-Benefit:** The premium paid for spot delivery ($cy$) is often justified by the massive opportunity cost of a factory stoppage.

## 3. Mathematical Representation
[RAW] In the cost-of-carry model, the convenience yield reduces the net cost of holding the commodity:

$$F_{t_0} = (1 + r_{t_0} \delta) [S_{t_0} + q_{t_0}(T - t_0) - cy]$$

Where:
- $F_{t_0}$: Futures price.
- $S_{t_0}$: Spot price.
- $r_{t_0} \delta$: Interest rate over the interval.
- $q_{t_0}(T - t_0)$: Storage costs over the interval.
- $cy$: Convenience yield.

> **Condition for Backwardation:** If $cy > r + q$, the term structure slopes downward.

## 4. Examples & Industry Lens
[RAW]
- **Crude Oil:** Refiners face extremely high costs if they run out of feedstock. Consequently, crude oil often exhibits a high convenience yield, particularly during geopolitical tensions or supply chain shocks.
- **Base Metals:** Aluminum, copper, and zinc markets frequently move into backwardation when LME (London Metal Exchange) inventories drop below critical thresholds.

## 5. Failure Conditions & Limitations
[RAW][LLM]
- **Abstract Nature:** Because $cy$ is not directly observable (unlike $r$ or $q$), it is often calculated as a residual. This means it may absorb market noise, model errors, or temporary liquidity squeezes that aren't strictly "convenience-driven."
- **Non-homogeneity:** If the physical commodity is not easily transportable or varies in grade, the $cy$ may vary significantly across different delivery locations.

─────────────────────────────────────────────
WRITEBACK
> TYPE 2: SPAWN Convenience_Yield.md — Extracted from Neftci Ch7, S7.3.3.
