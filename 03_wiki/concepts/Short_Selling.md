---
title: Short-Selling
aliases: []
type: concept
tags: []
status: draft
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: legacy_migrated
thesis: '[WIKI][LLM] **Short-selling** is a core investment technique involving the
  sale of a security that is not owned by the seller, with the intent of buying it
  back later at a lower price. It serves as a fundamental mechanism for **Absolute
  Return** strategies and provides a "hedge" against downward mar'
source_refs: []
created: '2026-04-21'
updated: '2026-04-21'
---

# Short-Selling

## 1. Thesis & Overview
[WIKI][LLM] **Short-selling** is a core investment technique involving the sale of a security that is not owned by the seller, with the intent of buying it back later at a lower price. It serves as a fundamental mechanism for **Absolute Return** strategies and provides a "hedge" against downward market trends.

## 2. Mechanism & Transmission
[RAW][LLM] The process typically involves:
1.  **Borrowing**: The seller borrows the security from a lender, facilitated by a **Prime Broker (PB)**.
2.  **Sale**: The security is sold in the open market, generating cash proceeds.
3.  **Repurchase (Covering)**: The seller buys the security back at a future date to return it to the lender.

### Transmission Flow: Profiting from Price Declines
  [Price: 100] ─── (1) Sell ───> [Cash: +100]
                                    │
  [Price: 80]  <── (2) Buy  ─── [Cash: -80]
                                    │
  ──────────────────────────────────┼──────────
  [Profit] ──────────────────────> [+20]

[RAW] **The Prime Broker Advantage**: Short selling an asset requires borrowing it. Prime brokers’ securities lending divisions have better information on this, allowing hedge funds to find borrowable assets efficiently.
[LLM] The PB's role is critical for liquidity in shorting; they consolidate information on available inventory from various institutional lenders (pension funds, insurance companies), reducing the search cost for the hedge fund.

## 3. Role in Hedge Fund Mandates
[RAW]
- **Original "Hedge"**: Provided a way to protect portfolios during bear markets, leading to the term "hedge fund". See [[Hedge_Fund_Industry]].
- **Absolute Return**: Allows funds to generate positive returns even when benchmarks are down.
- **Construction Leverage**: Proceeds from short-selling can be used to fund long positions, creating a self-financing or levered structure.

## 4. Convergence with Traditional Funds
[RAW] Increasingly adopted by **40 Act funds** (US) and **absolute return UCITS** (EU) to offer hedge-like returns to retail investors.

## 5. Failure Conditions
[LLM]
- **Short Squeeze**: Rapid price increases forcing short-sellers to buy back at high prices to limit losses, further driving up the price.
- **Recall Risk**: The lender may recall the borrowed security at an inconvenient time.
- **Unlimited Loss Potential**: Unlike long positions (limited to 0), there is no theoretical ceiling on how high a price can go.

─────────────────────────────────────────────
WRITEBACK
> TYPE 2: SPAWN Short_Selling.md — Initial node from Neftci Ch7.
