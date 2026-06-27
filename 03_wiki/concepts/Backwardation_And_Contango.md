---
title: Backwardation and Contango
aliases:
- Futures Curve Shapes
- Normal Backwardation
- Inverted Market
type: definition
tags:
- futures
- commodities
- term-structure
- basis
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: "Neftci_Principles.md"
thesis: The term structure of futures prices is determined by the net balance between
  the cost of carry (interest and storage) and the convenience yield (benefit of physical
  possession), reflecting market expectations of supply-demand dynamics and risk premia.
source_refs:
- file: Neftci_Principles.md
  page: 215
created: '2026-05-23'
updated: '2026-05-23'
---

## Thesis

Backwardation and Contango describe the slope of the futures term structure. While contango is the theoretical "baseline" for storable assets due to the cost of carry, backwardation emerges when the immediate scarcity of the underlying asset (convenience yield) or structural hedging demand overrides storage costs.

## Definitions

### 1. Backwardation (Inverted Market)
[WIKI] A market condition where the price for forward delivery is **below** the current spot price ($F_{t,T} < S_t$).
- **Curve Shape:** Downward sloping.
- **Basis:** Positive (Basis = Spot - Futures).
- **Market Signal:** Typically indicates current supply shortages or high demand for immediate delivery.

### 2. Contango
[WIKI] A market condition where the price for forward delivery is **above** the current spot price ($F_{t,T} > S_t$).
- **Curve Shape:** Upward sloping.
- **Basis:** Negative.
- **Market Signal:** Indicates a well-supplied market where futures prices reflect the "cost of carry" (interest + storage + insurance).

---

## Visual Representations

### Term Structure Curves
```
  Price ($)                            Price ($)
    ^                                    ^
    │ S (Spot)                           │       / F (Futures)
    │  \                                 │      /
    │   \                                │     /
    │    \ F (Futures)                   │    /
    │     \                              │   /
    │      \                             │ S (Spot)
    └───────────────> Time               └───────────────> Time
      BACKWARDATION                         CONTANGO
```

---

## Economic Rationale & Mechanisms

### 1. Spot-Futures Parity (Cost of Carry)
[RAW] The theoretical price of a futures contract is governed by the replication cost:
$$F_{t,0} = S_{t,0} (1 + r\delta) + q_{t,0}(T - t_0)$$
Where:
- $r$: Interest rate (financing cost).
- $q$: Storage and insurance costs.
- $\delta$: Day count fraction.

### 2. Convenience Yield ($cy$)
[RAW] To explain backwardation, a "placeholder" variable is introduced to represent the intangible benefit of holding the physical commodity:
$$F_{t,0} = S_{t,0} (1 + r\delta) + q_{t,0}(T - t_0) - cy$$
- If $cy > (r + q)$, the curve flips into **Backwardation**.
- **High $cy$:** Occurs in commodities like crude oil when refiners fear stockouts or when physical supply is tight.

### 3. Normal Backwardation Theory
[LLM] Proposed by Keynes and Hicks, this theory focuses on the relationship between the futures price ($F$) and the **expected future spot price** ($E[S_T]$):
- **Premise:** Hedgers (producers) are natural sellers of futures. To entice speculators to take the long side of the trade, producers must sell at a discount to the expected future spot price.
- **Formula:** $F < E[S_T]$.
- **Risk Premium:** The difference $E[S_T] - F$ represents the risk premium paid by hedgers to speculators.
- *Note:* In this theory, the futures price "normally" rises toward the spot price as maturity approaches.

---

## Transmission Flow: Supply Shock to Backwardation
[LLM]
```
[Supply Shortage] ───> [Physical Scarcity] ───> [↑ Convenience Yield]
                                                       │
                                                       v
[Backwardation] <─── [F < S] <─── [Benefit of Spot > Cost of Carry]
```

---

## Failure Conditions
- **Arbitrage Limits:** In contango, [[Cash_And_Carry_Arbitrage]] (buy spot, sell futures, store) provides a ceiling on how high $F$ can go relative to $S$.
- **Non-Storability:** For assets like electricity, the cost of carry model fails as $q \to \infty$, making the curve purely driven by expectations and $cy$.

---
WRITEBACK
> TYPE 2: SPAWN Backwardation_And_Contango.md — New fundamental node for futures term structure mechanics.
