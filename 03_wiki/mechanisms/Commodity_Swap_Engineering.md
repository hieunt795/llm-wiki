---
title: Commodity Swap Engineering
aliases:
- Commodity Swap
- Commodity-to-LIBOR Swap
- Fixed-for-Float Commodity Swap
type: mechanism
tags:
- commodities
- swaps
- financial-engineering
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Salih Neftci - Principles of Financial Engineering (2008)
thesis: Hoán đổi hàng hóa là việc tái lập các dòng tiền liên quan đến biến động giá
  hàng hóa thông qua sự kết hợp giữa vị thế hàng hóa giao ngay và một công cụ tài
  trợ (thường là FRN), cho phép các bên trao đổi lợi nhuận tổng thể của hàng hóa lấy
  một lãi suất tham chiếu hoặc một mức giá cố định.
source_refs:
- file: Neftci_Principles.md
  page: 221
created: '2026-04-16'
updated: '2026-04-22'
---

# Commodity Swap Engineering

## 1. Overview
[RAW][LLM] Commodity swap engineering involves the replication of commodity-linked cash flows using a combination of a spot commodity position and a funding instrument (typically a Floating Rate Note). This mechanism allows participants to exchange the total return of a commodity for a money market reference rate (e.g., LIBOR).

## 2. Step-by-Step Engineering (Replication-based)
[RAW] Based on Neftci Section 7.4.1, a commodity swap can be engineered through the "Vertical Addition" of two distinct positions.

### Step 1: Asset Leg (Commodity Investment)
- **Action**: Invest Notional $N$ to purchase $Q$ units of the commodity at spot price $S_0$, where $N = Q \times S_0$.
- **Cash Flows**:
    - $t=0$: Outflow of $-N$.
    - $t_i$: Receive/pay periodic capital gains/losses $\Delta S_{t_i} \times Q$.
    - $t_n$: Receive principal $N$ (liquidation of position).

### Step 2: Funding Leg (Floating Rate Note)
- **Action**: Issue or enter into an $n$-period FRN with notional $N$.
- **Cash Flows**:
    - $t=0$: Inflow of $+N$ (loan proceeds).
    - $t_i$: Pay periodic interest $(L_{t_{i-1}} + \text{spread}) \times \delta \times N$.
    - $t_n$: Outflow of $-N$ (principal repayment).

### Step 3: Vertical Addition (The Swap)
- **Initial Result**: The $+N$ and $-N$ at $t=0$ cancel out, requiring zero initial net investment.
- **Periodic Result**: The counterparty receives the commodity's price performance and pays a floating rate.
- **Final Result**: The principal flows at $t_n$ cancel out.

## 3. Fixed-for-Float Engineering (Commercial Swap)
[RAW] While Section 7.4.1 focuses on replication via LIBOR, the standard commercial "Fixed-for-Float" commodity swap (Section 7.4.2) settles the difference between a negotiated fixed price ($P_{fixed}$) and a realized floating average ($P_{floating}$).

### Engineering Steps:
1.  **Define Notional Volume**: Determine monthly volume ($Q$) and term (e.g., 12 months).
2.  **Define Reference Price**: Select a benchmark (e.g., NYMEX WTI prompt futures settlement).
3.  **Negotiate Fixed Price**: Based on the forward curve, set $P_{fixed}$ such that the initial present value is zero.
4.  **Net Settlement Calculation**:
    - **Producer (Fixed Price Payer)**: Receives $(P_{fixed} - P_{floating}) \times Q$.
    - **Consumer (Floating Price Payer)**: Receives $(P_{floating} - P_{fixed}) \times Q$.
5.  **Cash Flow Example (Oil)**:
    - Fixed: $95/bbl. Realized Average: $85/bbl.
    - Result: Producer receives $10/bbl from dealer (Net payment).

## 4. Transmission Mechanism (ASCII)
[LLM]
  ┌─────────────────────────────────────────────────────────────┐
  │        [COMMODITY LEG]        │        [FUNDING LEG]        │
  │   Assets      │ Liabilities   │     Assets      │ Liabilities│
  │───────────────┼───────────────┼─────────────────┼────────────│
  │ (1) +Commodity│ (1) -Cash (N) ┼───> (1) +Cash   │ (1) +Debt  │
  │ (2) +ΔS_t     │               │                 │ (2) +LIBOR │
  │ (3) +Cash (N) │               │                 │ (3) -Cash  │
  └───────────────────────────────┴─────────────────┴────────────┘
  Net Swap: Receive ΔS_t <───────> Pay LIBOR + Spread

## 4. Key Factors in Engineering
- **Convenience Yield**: Commodity dividends (benefits of physical possession) which reduce the required swap spread.
- **Storage Costs**: Negative carry associated with physical commodities.
- **Supply/Demand Imbalances**: Short-term market dynamics that deviate the swap spread from theoretical parity.

## 5. Failure Conditions
- **Liquidity Squeeze**: Inability to roll the funding leg or liquidate the commodity position without significant slippage.
- **Basis Risk**: Mismatch between the physical commodity held and the reference index used in the swap.
- **Margin/Collateral Calls**: Sharp price moves requiring immediate liquidity to maintain the replication.

─────────────────────────────────────────────
[[Commodity_Futures_Pricing]] | [[LIBOR_Based_Engineering]] | [[Floating_Rate_Notes]]
