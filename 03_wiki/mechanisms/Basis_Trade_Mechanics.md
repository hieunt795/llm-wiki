---
title: Basis Trade Mechanics
aliases:
- Basis Trade
- Bond vs Future Basis
- Cash vs Futures
- Implied Repo Arbitrage
type: mechanism
tags:
- trading-strategies
- market-infrastructure
- repo
- derivatives
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch33.md
thesis: A basis trade is a duration-neutral strategy that hedges a bond position with
  a futures contract to isolate the basis (mispricing between cash and derivatives
  markets), often benefiting from lower bid-offer spreads than outright bond trading.
source_refs:
- file: During_Fixed_Income_Ch33.md
  page: 364
- file: During_Fixed_Income_Ch33.md
  page: 365
created: '2026-04-13'
updated: '2026-04-21'
---

## Thesis

The bond future and its underlying bond are fundamentally linked by the [[Cheapest_To_Deliver_CTD_Mechanism|delivery]] process. Alexander Düring explains that a **Basis Trade** exploits the temporary decoupling of these two instruments. Because a duration-neutral package of a bond and a future carries zero interest rate risk, it is often tradeable with a lower bid-offer spread, as market makers don't need to charge for directional hedging. [[During_Fixed_Income_Ch33.md#page=364]]

## Mechanism: The Duration-Neutral Package

### 1. Basic Basis Trade (1-to-1)
When the bond is close in maturity to the futures CTD:
- **Hedge Equation:** $N_{\text{bond}} PVBP_{\text{bond}} = -N_{\text{future}} PVBP_{\text{future}}$
- **Objective:** To profit from the convergence of the [[Futures_Basis_And_Implied_Repo_Rate|Basis]] toward zero (or toward the repo rate) as delivery approaches. [[During_Fixed_Income_Ch33.md#page=364]]

### 2. The Butterfly-Hedged Basis (2-to-1)
If the bond and the futures CTD differ significantly in maturity (creating curve risk), a trader uses two different futures contracts to bracket the bond.
- **Hedge Equations:**
    1. $N_{\text{bond}} PVBP_{\text{bond}} = -(N_{\text{future1}} PVBP_{\text{future1}} + N_{\text{future2}} PVBP_{\text{future2}})$
    2. $(m_{\text{bond}} - m_{\text{future1}}) N_{\text{future1}} PVBP_{\text{future1}} = (m_{\text{future2}} - m_{\text{bond}}) N_{\text{future2}} PVBP_{\text{future2}}$
- **The Result:** This ensures that the position is neutral not only to parallel rate shifts (Level) but also to linear changes in the slope (Slope). It places a higher weight on the future that is "closer" on the curve to the bond. [[During_Fixed_Income_Ch33.md#page=365]]

### 3. Bond vs. Swap Basis (The Singapore Case Study)
[RAW] Salih Neftci mô tả một dạng Basis Trade kinh điển (Arb play) được thực hiện tại thị trường Singapore:
- **Strategy:** `Mua Trái phiếu Chính phủ (SGS) + Thực hiện Payer IRS + Funding qua Repo`.
- **Logic:** Nhà đầu tư nhận coupon cố định từ bond và trả coupon cố định qua swap (đã triệt tiêu rủi ro lãi suất). Sau đó dùng Repo để vay tiền mặt mua bond.
- **The Basis Profit:** Lợi nhuận đến từ chênh lệch giữa lãi suất thả nổi nhận được từ Swap (SIBOR) và lãi suất Repo phải trả.
- **Strategic Nuance:** Trader không cá cược vào hướng đi của lãi suất, mà cá cược vào việc **Spread giữa Repo và SIBOR sẽ dãn rộng** (hoặc chí ít không thu hẹp dưới mức 13.5 bp trong ví dụ của Neftci). [[Principles_of_Financial_Engineering_Neftci.md#page=162]]

## Strategic Implications: Execution and Repo

- **Crossing Trades:** In a basis trade, the counterparties often agree to "cross" the appropriate number of futures contracts on the exchange immediately after the cash bond trade is finalized. This ensures the duration-neutrality is locked in simultaneously.
- **Repo Specialness:** The profitability of a basis trade is often determined by the repo rate. If a bond is "Special," the cost of shorting it to execute a "Long Basis" trade (Short Bond, Long Future) may be higher than the basis profit. [[During_Fixed_Income_Ch15.md#page=127]] [[During_Fixed_Income_Ch33.md#page=364]]

## Evidence / Source Anchors

- Definition of Basis trade as hedging bond with futures: [[During_Fixed_Income_Ch33.md#page=364]]
- Mathematical derivation of the 1-to-1 hedge (Equation 32.1): [[During_Fixed_Income_Ch33.md#page=364]]
- Mathematical derivation of the 2-to-1 maturity-weighted hedge (Equation 32.2): [[During_Fixed_Income_Ch33.md#page=365]]
- Analysis of lower bid-offer spreads for DV01-neutral packages: [[During_Fixed_Income_Ch33.md#page=365]]
- Description of the "Crossing" requirement on the futures exchange: [[During_Fixed_Income_Ch33.md#page=365]]
- Case study on Singapore Bond vs Swap play and Repo funding: [[Principles_of_Financial_Engineering_Neftci.md#page=162]]

## Related

- [[Bond_Futures_Contract_Design]] — The derivative leg.
- [[Cheapest_To_Deliver_CTD]] — The anchor for the futures price.
- [[Futures_Basis_And_Implied_Repo_Rate]] — The metrics being traded.
- [[General_Collateral_Vs_Special]] — The primary implementation friction.
