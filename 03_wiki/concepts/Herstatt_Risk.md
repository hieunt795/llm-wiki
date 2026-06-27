---
title: Herstatt Risk
aliases:
- Settlement Risk
- Principal Risk
- Cross-Currency Settlement Risk
type: definition
tags:
- market-infrastructure
- settlement
- history
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch12.md
thesis: Herstatt risk is the danger that one counterparty to a transaction will deliver
  its asset but not receive the counter-asset because the other party defaults in
  the interval between the two legs of the trade.
source_refs:
- file: During_Fixed_Income_Ch12.md
  page: 99
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Herstatt risk represents the most fundamental danger in settlement: the lack of simultaneity. Named after a catastrophic failure in 1974, it remains a primary concern for cross-currency and cross-border transactions where payments occur in different time zones. The elimination of this risk was the primary driver behind modern settlement architectures like **Delivery versus Payment (DvP)** and the **Continuous Linked Settlement (CLS)** bank. [[During_Fixed_Income_Ch12.md#page=99]]

## The Historical Origin: Herstatt Bank (1974)

On June 26, 1974, German regulators ordered the insolvency of the Herstatt Bank.
- **The Event:** The bank was forced to suspend operations at 3:30 PM (German time) after it had received Deutsche Marks from several counterparties in Europe.
- **The Failure:** Because of the time zone difference, it was still morning in New York. Herstatt's American counterparties were expecting to receive their US Dollars later that day. Herstatt defaulted before the US leg of the trades could be settled.
- **The Impact:** Counterparties faced an immediate outflow of assets with no chance of recovery, leading to a freeze in the global interbank market. It took over 30 years to fully resolve the resulting legal claims. [[During_Fixed_Income_Ch12.md#page=99]]

## Mechanism: Settlement Asymmetry

In a bygone era, instructions were given independently:
1.  **Party A** (Seller) instructs their bank to deliver a security.
2.  **Party B** (Buyer) instructs their bank to deliver cash.
3.  **The Risk:** If Party B defaults after receiving the security but before delivering the cash, Party A becomes an unsecured creditor, losing the principal value of the asset. [[During_Fixed_Income_Ch12.md#page=99]]

## Modern Mitigation

### 1. Delivery versus Payment (DvP)
A process where a trusted intermediary (GCSD) accepts incoming transfers but only executes them if **both parties** have the necessary assets available. It acts as an escrow service, ensuring "simultaneity" even if the transfers are technically separate. [[During_Fixed_Income_Ch12.md#page=99]]

### 2. CLS Bank (Continuous Linked Settlement)
Specifically designed for the FX market to eliminate Herstatt risk in cross-currency trades by linking the two legs of a transaction across different central bank settlement systems. [[During_Fixed_Income_Ch12.md#page=99]]

## Evidence / Source Anchors

- Definition of Herstatt risk as settlement risk: [[During_Fixed_Income_Ch12.md#page=99]]
- Historical account of the 1974 Herstatt Bank failure and the 30-year resolution: [[During_Fixed_Income_Ch12.md#page=99]]
- Analysis of settlement risk as an outflow of assets without receipt of counter-assets: [[During_Fixed_Income_Ch12.md#page=99]]
- Role of DvP and CLS Bank in mitigating principal risk: [[During_Fixed_Income_Ch12.md#page=99]]

## Related

- [[Delivery_Versus_Payment]] — The technical implementation of "vắc-xin" against Herstatt risk.
- [[OTC_Trade_Lifecycle]] — The process that culminates in settlement.
- [[Herstatt_Risk_Case_Study]] — Further details on systemic impact.
- [[GCSD_Global_Central_Securities_Depository]] — The entities that implement DvP.
