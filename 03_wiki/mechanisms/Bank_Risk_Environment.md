---
title: Bank Risk Environment (Treasury Perspective)
aliases:
- Treasury Risk Management
- Banking Risks
- Treasury Risk Framework
- Môi trường rủi ro ngân hàng
type: domain
tags:
- risk-management
- treasury
- ALM
- liquidity
- credit-risk
status: verified
confidence: 5
half_life_years: 1
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: ACI_Dealing_Certificate_Mastering.md
thesis: A comprehensive framework for identifying and managing market, credit, and
  liquidity risks within a bank's treasury, focused on protecting capital and ensuring
  regulatory compliance (Basel). / Một khung khổ toàn diện để xác định và quản lý
  các rủi ro thị trường, tín dụng và thanh khoản trong bộ phận nguồn vốn ngân hàng,
  tập trung vào bảo vệ vốn và đảm bảo tuân thủ quy định (Basel).
source_refs:
- file: ACI_Dealing_Certificate_Mastering.md
  page: 293
created: '2026-04-24'
updated: '2026-04-24'
---

# Bank Risk Environment (Treasury Perspective)

## Thesis
A comprehensive framework for identifying and managing market, credit, and liquidity risks within a bank's treasury, focused on protecting capital and ensuring regulatory compliance (Basel). / Một khung khổ toàn diện để xác định và quản lý các rủi ro thị trường, tín dụng và thanh khoản trong bộ phận nguồn vốn ngân hàng, tập trung vào bảo vệ vốn và đảm bảo tuân thủ quy định (Basel)."


In the Treasury context, risk management is about identifying, measuring, and mitigating exposures arising from the bank's balance sheet activities and market-making operations.

## 1. Core Risk Categories

### 1.1. Market Risk
The risk that a position's value changes due to movements in market rates (interest rates or FX rates).
*   **Interest Rate Risk**: Arises from mismatched maturity positions (Gaps).
    *   *Short Position*: Overlent (Interest rates rise -> Loss).
    *   *Long Position*: Overborrowed (Interest rates fall -> Loss).
*   **Foreign Exchange Risk**:
    *   **Transaction Risk**: Arises from specific trades/commercial invoices.
    *   **Translation Risk**: Arises from revaluing assets/liabilities for financial reporting.
    *   **Economic Risk**: Competitive risk due to structural currency shifts.

### 1.2. Liquidity Risk
The risk that the bank cannot meet its obligations or fund its assets at a reasonable cost.
*   **Prudential Liquidity**: Minimum reserve requirements (MRR) set by central banks (often non-interest bearing).
*   **Funding Liquidity Risk**: The risk that a funding deposit cannot be replaced in the market when it matures.

### 1.3. Credit Risk (Counterparty Risk)
The risk of loss due to a counterparty's default.
*   **Lending Risk**: 100% of the unsecured amount advanced.
*   **Market Replacement Risk**: The cost of replacing a failed derivative contract (FRA, Swap, etc.) at current (unfavourable) market rates.
*   **Delivery Risk (Herstatt Risk)**: The risk of paying out one currency without receiving the other in an FX settlement.

## 2. Risk Mitigation & Limits
Treasury uses a hierarchical limit structure to control exposures:

| Limit Type | Purpose |
| :--- | :--- |
| **Counterparty Limit** | Controls maximum credit exposure to a specific name. |
| **Intra-day Limit** | Restricts the maximum open position allowed *during* the trading day. |
| **Overnight Limit** | Restricts the open position carried *after* hours (linked to capital/reserves). |
| **Stop-Loss Limit** | Mandates closing a position once a specific loss threshold is hit. |
| **Forward Gap Limit** | Restricts the size of maturity mismatches (interest rate risk). |

## 3. Specialized Risk Concepts

### 3.1. Settlement Risk Mitigation
*   **Netting**: Bilateral or multi-lateral agreements (e.g., CLS) to settle only the net difference, drastically reducing delivery risk.
*   **RTGS (Real Time Gross Settlement)**: Immediate and final settlement of payments to eliminate systemic risk.

### 3.2. Basis Risk
The risk that the price of a hedging instrument (e.g., Futures) does not move in perfect correlation with the underlying instrument being hedged.

### 3.3. Market Replacement Cost
Calculated via **Mark-to-Market (MtM)**. A positive MtM represents a credit risk to the counterparty (they owe us); a negative MtM represents no current credit risk to the bank (we owe them).


## Related

- [[Bank_Deposit_Types]]
- [[Rehypothecation_Mechanism_And_Risks]]
