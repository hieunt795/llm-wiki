---
title: RTGS Systems Global Reference
aliases:
- Real-Time Gross Settlement
- RTGS
- TARGET2
- FedWire
- BOJ-NET
- CHAPS
type: evidence
tags:
- banking
- payment-systems
- central-banking
- infrastructure
status: verified
confidence: 5
half_life_years: 1
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Các hệ thống Quyết toán Tổng tức thời (RTGS) đại diện cho đỉnh cao của hạ
  tầng thanh toán liên ngân hàng, nơi mọi giao dịch được quyết toán riêng lẻ và ngay
  lập tức bằng tiền ngân hàng trung ương, loại bỏ hoàn toàn rủi ro tín dụng đối tác.
source_refs:
- file: Fixed_Income_Alexander_During_Ch02.md
  page: 25
created: '2026-04-18'
updated: '2026-04-22'
---

## Thesis

The evolution of modern finance is a history of reducing "Settlement Risk." While netting systems (like [[Interbank_Netting]]) increase liquidity efficiency, they leave banks exposed to each other's credit for the duration of the netting cycle. **RTGS Systems** solve this by merging the payment processing function with the central bank's ledger. A deposit at a central bank *is* money; thus, an RTGS transfer is economically identical to a physical handover of legal tender, achieving absolute finality in near real-time.

## Evidence / Source Anchors

The larger central banks operate the following mission-critical RTGS platforms:

| Central Bank | System Name | Access and Participation |
|---|---|---|
| **Federal Reserve (USA)** | **FedWire** | Fed member banks, depositary institutions, foreign branches. |
| **ECB (Eurozone)** | **TARGET2** | Eurosystem counterparties (Monetary Financial Institutions - MFIs). |
| **Bank of Japan (JP)** | **BOJ-NET** | Banks, securities firms, money market brokers. |
| **Bank of England (UK)** | **RTGS / CHAPS** | Banks, building societies, investment firms, CCPs. |
| **PBoC (China)** | **HVPS** | Banks and PBoC branches. |

[extracted] [[Fixed_Income_Alexander_During_Ch02.md#page=26]] (Table 4.1)

### The Functional Difference
The essential difference between an RTGS system and a private clearing bank (like a money-centre bank) is the nature of the settlement asset:
- **Central Bank RTGS:** Settles in **Central Bank Money** (Sovereign Liability). Finality is immediate and carries no credit risk (excluding currency devaluation).
- **Private Clearing Bank:** Settles in **Inside Money** (Commercial Liability). Participants assume "Convertibility Risk"—the risk that the clearing bank fails and the balances become inaccessible. [[Fixed_Income_Alexander_During_Ch02.md#page=26]]

## Mechanism

Transfers between current accounts at a central bank are viewed as **Gross Transfers**. To enable the efficient use of these deposits, systems often incorporate secondary mechanisms:

1. **Real-Time Instruction:** Instructions are executed as they arrive, provided the sender has a sufficient balance or credit limit.
2. **Immediate Finality:** Once the central bank debits Account A and credits Account B, the transfer is non-reversible and the "obligor" has successfully changed from Bank A's private ledger to the central bank's ledger. [[Fixed_Income_Alexander_During_Ch02.md#page=26]]

### Boundaries / Conditions

### The Efficiency Trade-off
RTGS systems are highly liquidity-intensive. Because every payment is settled gross, banks must maintain large positive balances at the central bank. To prevent "gridlock" where no one can pay because everyone is waiting for an incoming payment, many RTGS systems (like TARGET2) offer **Intraday Overdrafts**. [[Fixed_Income_Alexander_During_Ch02.md#page=26]]

## Evidence / Source Anchors

- Definition of RTGS as the merger of payment processing and central bank functions: [[Fixed_Income_Alexander_During_Ch02.md#page=25-26]]
- Table 4.1 taxonomy of global systems (FedWire, TARGET2, etc.): [[Fixed_Income_Alexander_During_Ch02.md#page=26]]
- Analysis of "Immediate Finality" in central bank money: [[Fixed_Income_Alexander_During_Ch02.md#page=26]]
- Discussion on the cost/interest distribution of clearing banks vs central banks: [[Fixed_Income_Alexander_During_Ch02.md#page=26]]

## Related

- [[Interbank_Netting]] — The "Net" alternative to the "Gross" RTGS model.
- [[Intraday_Overdraft]] — The technical mechanism used to provide liquidity within RTGS systems.
- [[Inside_Vs_Outside_Money]] — RTGS transfers are the movement of "Outside Money."
- [[Herstatt_Risk]] — The systemic failure that RTGS systems were specifically designed to prevent.
- [[Central_Bank_Definition]] — The institutional entity that operates these critical infrastructures.
