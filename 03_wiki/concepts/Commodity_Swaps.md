---
title: Commodity Swaps
aliases: []
type: concept
tags: []
status: draft
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: "Neftci Chapter 7"
thesis: '[WIKI][LLM] A commodity swap is a contractual agreement where counterparties
  exchange cash flows based on the price of an underlying commodity. The most common
  form is a **Fixed-for-Floating Swap**, allowing producers and consumers to hedge
  against price volatility.'
source_refs: []
created: '2026-04-21'
updated: '2026-04-28'
---

# Commodity Swaps

## 1. Thesis & Overview
[WIKI][LLM] A commodity swap is a contractual agreement where counterparties exchange cash flows based on the price of an underlying commodity. The most common form is a **Fixed-for-Floating Swap**, allowing producers and consumers to hedge against price volatility.

## 2. Engineering Mechanism (Fixed-for-Float)
[RAW][LLM] Commodity swaps can be engineered by combining a commodity investment with a money market reference rate (FRN). For a detailed breakdown of the replication process, see [[Commodity_Swap_Engineering]].

## 3. Arbitrage-Free Valuation Principles
[RAW][LLM] The valuation of commodity swaps is anchored in the **No-Arbitrage condition**, where the fair swap price is determined by the present value of expected future cash flows.

### A. Fundamental Pricing Rule
At inception ($t=0$), the swap rate ($P_{fixed}$) is set so that the Present Value (PV) of the fixed and floating legs are equal:
$$PV(\text{Fixed Leg}) = PV(\text{Floating Leg})$$
$$\sum_{i=1}^{n} P_{fixed} \times N \times D(t_i) = \sum_{i=1}^{n} E[S_{avg,i}] \times N \times D(t_i)$$
Where:
- $N$: Notional volume.
- $D(t_i)$: Discount factor for settlement date $t_i$.
- $E[S_{avg,i}]$: Expected average price for period $i$, derived from the **Commodity Forward Curve**.

### B. Swap Curve Construction (Weighted Average)
[RAW] Commodity swaps often settle based on the average price of the **prompt futures contract** during a month. Since futures contracts roll mid-month, the fair swap price for a given month is a weighted average of two successive futures maturities.

**Formula:**
$$P_{swap, month} = P_{fut,1} \times w_1 + P_{fut,2} \times w_2$$

**Weighting Logic:**
Weights represent the proportion of business days each contract is the "prompt" contract during the pricing window:
- $w_1 = \frac{\text{Days Until Roll Date}}{\text{Total Business Days}}$
- $w_2 = \frac{\text{Days After Roll Date}}{\text{Total Business Days}}$

**Worked Example: Oil Prompt Month Swap (Jan 2013)**
- **Prompt Contract #1 (Feb 13)**: $88.40 (11 days)
- **Prompt Contract #2 (Mar 13)**: $88.92 (12 days)
- **Total Business Days**: 23
- **Weights**: $w_1 = 11/23 \approx 48\%$, $w_2 = 12/23 \approx 52\%$
- **Fair Swap Price**: $(88.40 \times 0.48) + (88.92 \times 0.52) = 88.65$
*> Note: Neftci Table 7.5 contains a labeling discrepancy where it swaps the weights in the text calculation vs. the table headers.*

### C. Mark-to-Market (MtM) Valuation
[RAW] The mark-to-market value of a commodity swap is calculated by discounting the remaining future cash flows using updated forward prices.
$$V_t = \sum_{i=k}^{n} (E_t[S_{avg,i}] - P_{fixed}) \times N \times D(t, t_i)$$
- **MtM Gain**: If the forward curve shifts upward ($E_t[S_{avg}] > P_{fixed}$), the fixed-price payer (swap buyer) gains.
- **MtM Loss**: If the forward curve shifts downward, the fixed-price payer loses.

## 4. Real-World Complications & Arbitrage
[RAW] Unlike financial assets, [[Commodities]] involve physical constraints that affect pricing:
- **Storage & Heterogeneity**: As discussed in [[Commodities]], physical storage costs and grade differences (heterogeneity) must be accounted for in the forward price.
- **Seasonality**: Demand peaks (e.g., iron ore in May/September) affect liquidity and curve shape.
- **Settlement Differences**: Physical (e.g., Dalian DCE) vs. Financial (e.g., Singapore SGX).
- **Onshore/Offshore Arbitrage**: Mismatch between domestic curves (contango) and international curves (backwardation) creates "three-way arbitrage" opportunities (Futures vs. Physical Onshore vs. International Swap).
- **Currency & Margin Risk**: In cross-exchange arbitrage (e.g., RMB-denominated DCE vs. USD-denominated SGX), traders cannot offset margins. A sharp price move can cause a margin call on one exchange even if the overall position is profitable.

## 5. Specialized Variations & Use Cases
- **Crack Spread Swap**: Used by refiners to hedge the margin between refined products and crude oil. Refiner pays floating refined product price and receives floating crude price + fixed margin.
- **Commodity-Linked Interest Rate Swap**: Hybrid where LIBOR is exchanged for a rate linked to commodity prices (e.g., fixed rate declines as oil price rises).
- **Japanese Oil Markets**: Companies use swaps to hedge the exposure between light-oil products (long in Singapore) and heavy-oil products (long in Japan due to refinery overcapacity). This "paper balance" market is often settled in cash.

─────────────────────────────────────────────
WRITEBACK
> TYPE 1: EXPAND Commodity_Swaps.md — Added Section 7.4 details (Japanese oil hedging, currency/margin risk, T-Shape mechanism).
