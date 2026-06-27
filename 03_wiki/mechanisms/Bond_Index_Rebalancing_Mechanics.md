---
title: Bond Index Rebalancing Mechanics
aliases:
- Index Rebalancing
- Capitalisation Changes
- Rebalancing Lag
- Cân đối lại chỉ số
type: mechanism
tags:
- index
- portfolio-management
- trading
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch35.md
thesis: Index rebalancing is the periodic adjustment of a bond index's constituent
  list and weights to reflect capitalisation changes, utilizing discrete intervals
  (typically monthly) to optimize the trade-off between tracking accuracy and transaction
  costs.
source_refs:
- file: During_Fixed_Income_Ch35.md
  page: 380
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

A bond index universe is never static: new bonds are issued and old bonds mature every day. Alexander Düring explains that while a "perfect" index would adjust daily to reflect these capitalisation changes, the operational reality of **Transaction Costs** makes this impossible for real-world funds. Rebalancing mechanics are therefore designed as a discrete compromise. [[During_Fixed_Income_Ch35.md#page=380]]

## Mechanism: The Discrete Adjustment

Instead of daily changes, indices typically concentrate all adjustments into a single window:

1.  **Rebalancing Frequency:**
    - **Monthly:** The standard for liquid government and corporate bond markets (usually the last day of the month).
    - **Quarterly:** Common for less liquid segments (e.g., small-cap or emerging markets) where frequent trading would be prohibitively expensive. [[During_Fixed_Income_Ch35.md#page=380]]
2.  **Tracking Error Injection:** By "locking" the index for a month, the index provider forces a **Tracking Error** onto any fund that attempts to match the index perfectly. The fund must either trade daily (incurring high costs) or follow the index's monthly jump (incurring model risk). [[During_Fixed_Income_Ch35.md#page=380]]

## Strategic Implications: The Settlement Paradox

Düring identifies a "hidden lie" in global index rebalancing: the **T+0 Assumption**.
- **The Friction:** Different markets have different settlement cycles (e.g., JGBs at T+2, US Treasuries at T+1).
- **The Solution:** Global indices solve this by assuming all markets settle at **T+0**.
- **The Reality:** A fund manager moving capital from Japan to the US based on an index change will find that the cash from the JGB sale arrives one day *after* it is needed to pay for the US Treasury purchase.
- **The Repo Bridge:** In practice, traders must use the [[General_Collateral_Vs_Special|Repo market]] to borrow cash for one or two days to "bridge" this settlement gap, a cost that is rarely reflected in the index returns themselves. [[During_Fixed_Income_Ch35.md#page=380]]

## Evidence / Source Anchors

- Analysis of the tenability of daily rebalancing due to transaction costs: [[During_Fixed_Income_Ch35.md#page=380]]
- Identification of Monthly and Quarterly as the primary rebalancing frequencies: [[During_Fixed_Income_Ch35.md#page=380]]
- Critique of the T+0 settlement assumption in global bond indices: [[During_Fixed_Income_Ch35.md#page=380]]
- Case study of the settlement mismatch between JGB (T+2) and UST (T+1): [[During_Fixed_Income_Ch35.md#page=380]]
- Description of the Repo market as the necessary bridge for cross-border rebalancing: [[During_Fixed_Income_Ch35.md#page=380]]

## Related

- [[Bond_Index_Principles]] — The rules that determine inclusion before rebalancing.
- [[Index_Tracking_And_Replication_Risk]] — How funds implement these periodic jumps.
- [[Repurchase_Agreement_Repo_Market_Structure]] — The tool used to bridge the T+0 paradox.
- [[Macaulay_Duration]] — How rebalancing suddenly alters the risk profile of the benchmark.
