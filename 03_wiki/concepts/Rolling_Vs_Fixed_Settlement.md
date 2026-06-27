---
title: Rolling vs Fixed Settlement
aliases:
- T+2
- T+0
- Nguồn gốc Backwardation
- Rolling Settlement
- Fixed Settlement
type: definition
tags:
- market-infrastructure
- settlement
- conventions
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: extracted from _temp_ch11.md
thesis: Modern markets use rolling settlement (e.g., T+2) where settlement occurs
  a set number of business days after the trade, whereas historic markets used fixed
  dates for all transactions within a period.
source_refs:
- file: Fixed Income Trading and Risk Management - Alexander Düring
  page: 100
created: '2026-04-13'
updated: '2026-04-18'
---

## Thesis

The time between **trade date** (valuation date) and **settlement date** (value date) is defined by market convention. Historically, markets used **fixed settlement**, where all trades from a period were settled on a single predetermined date. Modern electronic markets have shifted to **rolling settlement** (most commonly T+2), which reduces credit risk by shortening the exposure window between agreement and exchange. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=100]]

## Definition

### 1. Rolling Settlement (Standard)
- **Mechanism:** The settlement date is calculated as a fixed number of business days after the trade date ($T+n$).
- **Value Date vs. Effective Date:** [RAW] Neftci phân biệt: **Value Date** là ngày tiền thực sự chuyển giao; **Effective Date** là ngày các điều khoản logic của hợp đồng (như Swap) bắt đầu có hiệu lực.
- **Specific Asset Conventions (Neftci):**
    - **US Treasuries:** $T+1$ (Regular way) hoặc $T+0$ (Cash settlement).
    - **Corporate/International Bonds:** $T+3$.
    - **Commercial Paper (CP):** $T+0$ (Same day).
    - **Euromarket Deposits:** $T+2$.
    - **Foreign Exchange (FX):** $T+2$ (thường gọi là "Spot Date").
    - **US Stocks:** $T+3$ (Standard pre-2014).

### 2. Regulatory Update: Shortened Settlement Cycle (SSC)
- **Rationale:** [RAW] Sau GFC, DTCC và các cơ quan quản lý đẩy mạnh việc chuyển từ $T+3$ sang $T+2$ (và hướng tới $T+1$).
- **Objectives:** Giảm thiểu rủi ro đối tác (counterparty risk), giảm tính chu kỳ (procyclicality), và giải phóng vốn ký quỹ (margin capital) nhanh hơn cho các thành viên bù trừ.

### 3. Fixed Settlement (Historical)
- **Mechanism:** All transactions executed within a specific period (e.g., 60 days) were settled on one specific day.
- **Legacy Terminology:** When parties in a fixed market agreed to settle on the *following* fixed date instead of the upcoming one, the trade was said to be **backwarded**. This term survives in the futures market as **backwardation**. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=100]]. For modern market dynamics, see [[Backwardation_And_Contango]].

### Boundaries / Conditions

- **Credit Risk vs. Error Cost:** Shorter settlement periods reduce the window for counterparty default but increase the cost and likelihood of fails due to insufficient time for manual reconciliation of human errors. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=100]]
- **Custom Dates:** While T+2 is the convention, parties can bilaterally agree to earlier or later settlement.

## Evidence / Source Anchors

- Market convention of T+2 for bonds/FX: [[Fixed_Income_Alexander_During_Ch12.md#page=100]]
- Historical origin of the term "backwardation" from fixed settlement: [[Fixed_Income_Alexander_During_Ch12.md#page=100]]
- Trade-off between credit risk and operational error in shortening settlement cycles: [[Fixed_Income_Alexander_During_Ch12.md#page=100]]

## Related

- [[OTC_Trade_Lifecycle]] — The process that must be completed before the settlement date.
- [[Delivery_Versus_Payment]] — The mechanism used on the settlement date.
- [[Settlement_Fails_And_Cures]] — Consequences of missing the settlement deadline.
- [[Settlement_Fails_And_Incentives]]
- [[Herstatt_Risk]]
