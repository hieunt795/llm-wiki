---
title: Reserve Maintenance Period and Averaging Mechanics
aliases: []
type: mechanism
tags: []
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Bindseil
provenance: "bindseil_averaging.md"
thesis: The reserve averaging mechanism provides a buffer against day-to-day autonomous
  factor shocks, stabilizing interest rates through inter-temporal arbitrage.
source_refs:
- file: bindseil_averaging.md
  page: 85
created: '2026-04-26'
updated: '2026-04-26'
---

# [[Reserve_Maintenance_Period_and_Averaging_Mechanics]]

## Thesis
[WIKI] Averaging allows banks to manage liquidity shocks to their reserve holdings across a maintenance period, decoupling daily shocks from immediate market rate volatility. [[Reserve_Maintenance_Period_Averaging#page=85]]

## Mechanism
[RAW] In a reserve maintenance period with averaging, reserve fulfillment is controlled at the end of each day (no-overdraft constraint) and as an average over the period. [[Reserve_Maintenance_Period_Averaging#page=85]]

[RAW] Banks optimize reserve holdings across the period to minimize costs, leading to inter-temporal arbitrage. This ensures the martingale property: the current overnight rate reflects the expected future rate within the period. [[Reserve_Maintenance_Period_Averaging#page=85]]

[LLM] If a bank expects autonomous factors to drain liquidity tomorrow (pushing rates up), it will borrow today to meet its average requirement at a lower cost, thereby equalizing rates across time.

[RAW] In practice, the no-overdraft constraint creates an inherent asymmetry. Banks prefer to backload reserve fulfillment (under-fulfill early, catch up late) to avoid early "lock-in" of fulfillment, which reduces their ability to offset future shocks. [[Reserve_Maintenance_Period_Averaging#page=86]]

[RAW] This asymmetry can cause overnight rates to creep upwards toward the end of the maintenance period. [[Reserve_Maintenance_Period_Averaging#page=86]]

## Evidence / Source Anchors
- [[Reserve_Maintenance_Period_Averaging#page=85]] — Martingale property and averaging mechanics.
- [[Reserve_Maintenance_Period_Averaging#page=86]] — Asymmetry caused by no-overdraft constraints and backloading behavior.

## Related
- [[Central_Bank_Reserves_and_Reserve_Requirements]] — Core definitions.
- [[Autonomous_Factors_and_Liquidity_Supply]] — The shocks that averaging buffers.
- [[Reserve_Ratio]]
- [[Indonesia_ITF_Transition_Period]]
