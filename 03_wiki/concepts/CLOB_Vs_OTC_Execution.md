---
title: CLOB vs OTC Execution
aliases:
- Central Limit Order Book
- OTC Execution
- RFQ
- Streaming Pricing
type: mechanism
tags:
- market-structure
- trading
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: extracted from _temp_ch11.md
thesis: The choice between CLOB and OTC execution reflects a trade-off between price
  transparency (high in CLOB) and the management of information leakage and search
  costs (better managed in OTC).
source_refs:
- file: Fixed Income Trading and Risk Management - Alexander Düring
  page: 86
- file: Fixed Income Trading and Risk Management - Alexander Düring
  page: 87
created: '2026-04-13'
updated: '2026-04-18'
---

## Thesis

Execution in financial markets follows two primary paths: matching in a **Central Limit Order Book (CLOB)** or bilateral negotiation in the **OTC** market. CLOBs excel in high-transparency, high-liquidity environments but suffer from information leakage for large trades. OTC execution, often using **Request for Quote (RFQ)** or **Streaming Pricing**, allows for discreet execution of large or illiquid positions by shifting the risk to a market maker.

## Mechanism

### 1. CLOB (Central Limit Order Book)
- **Order Matching:** Orders are matched according to the exchange's rules (e.g., price-time priority). [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=86]]
- **Transparency:** All limit orders in the book are typically visible, which serves as a tool for public price discovery.
- **Risk:** Large orders revealed in a CLOB can alert the market, moving the price against the trader before execution is complete (**information leakage**).

### 2. OTC Execution
- **Bilateral Negotiation:** Involves direct communication between a price taker (client) and a price maker (dealer). [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=87]]
- **RFQ (Request for Quote):** A client asks for a firm quote (bid or ask) for a specific size.
- **Dealer Role:** The dealer provides a price, essentially taking the risk onto their balance sheet to provide immediate execution. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=87]]

### Boundaries / Conditions

- **Product Suitability:** Highly standardized products (like bond futures or blue-chip stocks) are well-suited for CLOBs. Heterogeneous assets (like corporate bonds) are almost exclusively OTC. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=86]]
- **Block Trades:** Many exchanges allow large trades to bypass the CLOB to avoid market impact, effectively mimicking OTC execution within an exchange framework. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=87]]

## Evidence / Source Anchors

- CLOB as the standard model for public exchange trading: [[Fixed_Income_Alexander_During_Ch12.md#page=86]]
- Market makers providing prices only to known clients in the OTC model: [[Fixed_Income_Alexander_During_Ch12.md#page=86]]
- Hybrid models like block trades used to prevent information leakage: [[Fixed_Income_Alexander_During_Ch12.md#page=87]]

## Related

- [[OTC_Vs_Exchange_Trading]] — The structural definitions of these venues.
- [[Dark_Pools]] — Anonymous matching within an exchange framework.
- [[Information_Leakage_In_Trading]] — The primary risk that drives traders toward OTC execution.
