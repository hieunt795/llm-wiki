---
title: Index Tracking and Replication Risk
aliases:
- Passive Investing
- Physical Replication
- Synthetic Replication
- Partial Replication
- Tracking Error
- Cash Drag
type: mechanism
tags:
- index
- portfolio-management
- trading
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch35.md
thesis: Index tracking is the optimization process of replicating a benchmark's performance
  through full, partial, or synthetic asset matching, characterized by the persistent
  'Cash Drag' and 'Replication Risk' inherent in illiquid bond markets.
source_refs:
- file: During_Fixed_Income_Ch35.md
  page: 383
- file: During_Fixed_Income_Ch35.md
  page: 384
- file: During_Fixed_Income_Ch35.md
  page: 388
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Passive investing is based on the assumption that market-weighted portfolios are optimal (Efficient Market Hypothesis). Alexander Düring explains that for bond investors, "passive" is a misnomer. Replicating a bond index is an active and complex optimization problem because many index constituents are illiquid or mathematically inaccessible. The resulting **Tracking Error** is not a failure of management, but a structural feature of the market. [[During_Fixed_Income_Ch35.md#page=383-384]]

## Mechanism: Replication Methodologies

### 1. Physical Replication
- **Full Replication:** Buying every bond in the index at its exact weight. Only feasible for very liquid indices (e.g., the DAX 30 or large-cap US Treasuries). [[During_Fixed_Income_Ch35.md#page=384]]
- **Partial Replication (Sampling):** Using a subset of securities that "spans" the risk factors of the index. This minimizes transaction costs at the expense of adding **Replication Risk** (the risk that the sample deviates from the whole). [[During_Fixed_Income_Ch35.md#page=385]]

### 2. Synthetic Replication
- **Mechanism:** Using Total Return Swaps (TRS) or Futures to receive the index's return without owning the physical bonds.
- **Benefit:** Eliminates the [[#The Cash Drag|Cash Drag]] and the need for physical asset management.
- **Cost:** Introduces **Counterparty Risk** (if the swap provider defaults). [[During_Fixed_Income_Ch35.md#page=384]]

## Strategic Risks

### 1. The Cash Drag (Lực cản tiền mặt)
Passive funds must hold a small percentage of cash to fund daily redemptions.
- **The Problem:** In a normal environment, cash earns the risk-free overnight rate (e.g., €STR), which is typically lower than the yield of a bond index.
- **The Impact:** A fund holding 5% cash against a 5-year bond index will underperform by approximately **2 basis points per year** ($5\% \times 40\text{bp spread}$). This is a deterministic penalty for being a real-world fund. [[During_Fixed_Income_Ch35.md#page=388]]

### 2. Factor Spanning and Optimization
Practitioners use **Lagrangian Optimizers** to find a spanning set of $N$ assets that match $k$ risk factors (e.g., Duration, Convexity, Sector weights).
- **The Identity:** $\sum w_i D^*_i = D^*_m$ (The weighted average duration of the portfolio must match the market duration).
- **The Constraint:** Tracking is an exercise in minimizing the distance between the portfolio and the index while adhering to these factor identities. [[During_Fixed_Income_Ch35.md#page=385-387]]

## Evidence / Source Anchors

- Analysis of full vs. partial vs. synthetic replication strategies: [[During_Fixed_Income_Ch35.md#page=384]]
- Definition of the three-step optimization process for factor analysis and spanning sets: [[During_Fixed_Income_Ch35.md#page=385]]
- Mathematical derivation of the duration-neutral Lagrangian for bond tracking: [[During_Fixed_Income_Ch35.md#page=386-387]]
- Systematic calculation of the 'Cash Drag' penalty for redemption buffers: [[During_Fixed_Income_Ch35.md#page=388]]
- Observation that an index tracker is effectively "Short the Index and Long the tracking assets": [[During_Fixed_Income_Ch38.md#page=405]]

## Related

- [[Bond_Index_Principles]] — The "Triple Mandate" that defines the tracking target.
- [[Bond_Index_Rebalancing_Mechanics]] — The event that forces portfolio re-optimization.
- [[Mean_Variance_Optimisation_Theory]] — The theoretical basis for "optimal" market weights.
- [[Macaulay_Duration]] — The primary factor matched in Step 2 of replication.
