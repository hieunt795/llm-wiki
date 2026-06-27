---
title: OTC vs Exchange Trading
aliases:
- Public Exchange
- Over-the-counter
- Thị trường phi tập trung
type: definition
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
thesis: 'Financial markets operate between two structural extremes: public exchanges
  using central limit order books (CLOBs) and over-the-counter (OTC) markets based
  on bilateral relationships with market makers.'
source_refs:
- file: Fixed Income Trading and Risk Management - Alexander Düring
  page: 86
- file: Fixed Income Trading and Risk Management - Alexander Düring
  page: 87
created: '2026-04-13'
updated: '2026-04-18'
---

## Thesis

Modern trading venues range from public exchanges, which match orders anonymously through a **central limit order book (CLOB)**, to over-the-counter (OTC) markets, where **market makers** provide liquidity on a bilateral basis. While exchanges offer transparency and intermediation, OTC markets rely on established relationships to manage risks and execute large or complex trades. In practice, many venues employ hybrid models to balance price discovery and execution efficiency.

## Definition

### 1. Public Exchange (CLOB)
- **Mechanism:** Operates on the basis of a public order book where members place limit orders. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=86]]
- **Intermediation:** The exchange acts as a central counterparty, meaning participants face the exchange rather than each other.
- **Dark Pools:** Some exchanges allow "dark pools" where orders are matched without being made public, primarily to prevent information leakage. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=86]]

### 2. Over-the-counter (OTC) Market
- **Mechanism:** Market makers advertise their willingness to trade certain instruments on a bilateral basis. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=86]]
- **Relationships:** Dealers typically provide prices only to known clients to manage credit and informational risks.
- **Quotes:** Trading involves requesting firm or indicative prices (one-way or two-way). [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=86-87]]

### Boundaries / Conditions

- **Hybrid Models:** Most exchanges permit **block trades** to be negotiated outside the order book and reported later. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=87]]
- **Liquidity Provision:** In OTC markets, issuers may incentivize investment banks to act as market makers in their bonds to facilitate price discovery. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=87]]

## Evidence / Source Anchors

- Distinction between CLOB and OTC based on order matching vs bilateral negotiation: [[Fixed_Income_Alexander_During_Ch12.md#page=86]]
- Role of market makers in providing advertised prices to known clients: [[Fixed_Income_Alexander_During_Ch12.md#page=86]]
- Implementation of block trades and dark pools within exchange structures: [[Fixed_Income_Alexander_During_Ch12.md#page=86-87]]

## Related

- [[CLOB_Vs_OTC_Execution]] — Detailed comparison of execution mechanisms.
- [[Central_Counterparty]] — The role of the exchange/clearing house as intermediary.
- [[OTC_Trade_Lifecycle]] — The sequence of steps in an OTC transaction.
