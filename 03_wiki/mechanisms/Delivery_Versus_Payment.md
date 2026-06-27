---
title: Delivery Versus Payment (DvP)
aliases:
- DvP
- Giao tiền nhận phiếu
type: mechanism
tags:
- market-infrastructure
- settlement
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: extracted from _temp_ch11.md
thesis: DvP is a settlement mechanism where the transfer of securities happens only
  if the corresponding payment occurs simultaneously, eliminating Herstatt (settlement)
  risk.
source_refs:
- file: Fixed Income Trading and Risk Management - Alexander Düring
  page: 99
created: '2026-04-13'
updated: '2026-04-18'
---

## Thesis

To prevent one counterparty from fulfilling their obligation while the other defaults (Herstatt risk), the market uses **Delivery Versus Payment (DvP)**. This is facilitated by a trusted intermediary (usually a GCSD) acting as an escrow agent. DvP ensures that either both sides of the trade are executed or neither is, protecting both the buyer's cash and the seller's securities. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=99]]

## Mechanism

1. **Escrow Logic:** A trusted bank (intermediary) accepts incoming asset transfers from both sides.
2. **Conditional Execution:** The intermediary only executes the transfers if both parties have sufficient assets (cash and securities) in their accounts with that intermediary. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=99]]
3. **Settlement Cycles:** To reduce warehousing costs at the GCSD, DvP in bond markets is often conducted in batches at predefined times rather than on a continuous basis.
4. **Netting Benefit:** Batching allows for the netting of multiple transactions, reducing the total amount of assets that need to be moved. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=99]]

### Boundaries / Conditions

- **Cost of Warehousing:** Maintaining assets at a central intermediary involves costs for all parties.
- **Cross-Currency Risk:** DvP is more complex for transactions in different currencies and locations; the **CLS Bank** was specifically established to manage this for FX. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=99]]

## Evidence / Source Anchors

- Analogy of DvP to real estate escrow accounts: [[Fixed_Income_Alexander_During_Ch12.md#page=99]]
- Role of GCSDs in conducting DvP batches to reduce costs: [[Fixed_Income_Alexander_During_Ch12.md#page=99]]
- CLS Bank as the implementation of DvP for FX: [[Fixed_Income_Alexander_During_Ch12.md#page=99]]

## Related

- [[Herstatt_Risk]] — The specific settlement risk that DvP is designed to eliminate.
- [[Central_Counterparty]] — The entity that often orchestrates the DvP process.
- [[Book_Entry_Securities_System]] — The infrastructure that allows DvP to occur electronically.
