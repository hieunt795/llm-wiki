---
title: Swap Trade Compression and Recouponing
aliases:
- Trade Compression
- TriOptima
- Swap Novation
- Re-couponing
- Crystallization
- Nén giao dịch
type: mechanism
tags:
- derivatives
- swaps
- risk-management
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch30.md
thesis: Trade compression and recouponing are portfolio optimization techniques used
  to reduce the gross notional volume of outstanding swaps and manage collateral efficiency
  by netting offsetting risk and resetting contract values to market par.
source_refs:
- file: During_Fixed_Income_Ch30.md
  page: 338
- file: During_Fixed_Income_Ch30.md
  page: 339
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The multi-hundred trillion dollar size of the global swap market is partially a mathematical illusion. Alexander Düring explains that because swap users traditionally closed out risk by entering new, offsetting contracts (rather than terminating the original), balance sheets became inflated with redundant trades. **Trade Compression** and **Re-couponing** are the industry's "cleaning" mechanisms to reduce systemic risk and release trapped capital. [[During_Fixed_Income_Ch30.md#page=338]]

## Mechanism 1: Trade Compression (Nén giao dịch)

Compression is a multi-lateral netting process that collapses offsetting risk positions while leaving the net exposure unchanged.

- **The Problem:** Bank A pays fixed to Bank B, who pays fixed to Bank C, who pays fixed back to Bank A. Each trade consumes balance sheet and requires separate settlement.
- **The Solution:** Specialized providers (like **TriOptima**) identify these circular chains and use **Novation** to replace them with a single net contract (or zero contracts if the loop perfectly offsets).
- **The Impact:** Compression reduces the **Gross Notional** volume of the market, making it a more accurate reflection of true systemic risk. [[During_Fixed_Income_Ch30.md#page=338]]

## Mechanism 2: Re-couponing (Làm mới Fair Value)

Re-couponing is the process of resetting a swap's fixed rate to the current market rate to bring its Mark-to-Market (MTM) value back to zero.

### 1. The Capital Drag
When a swap's value moves significantly into the money or out of the money, it requires massive daily **Margin/Collateral** payments. This "traps" liquid cash that could be used elsewhere. [[During_Fixed_Income_Ch30.md#page=338]]

### 2. The Reset Process
- **The Termination:** The existing non-par swap is closed out.
- **The Crystallization:** The party that was "down" on the trade pays a one-time cash lump sum to the other party to settle the remaining valuation. This is known as **crystallizing** the P&L.
- **The Re-issue:** A new swap is immediately entered with the same dates but a new, Par coupon.
- **The Result:** The MTM becomes zero, and the margin accounts are emptied. [[During_Fixed_Income_Ch30.md#page=339]]

## Strategic Implications: Volume Inflation

Düring warns that re-couponing leads to **Reported Volume Inflation**. A single 30-year swap may be re-couponed dozens of times to manage margin efficiency. In trade repositories, this appears as hundreds of billions in "new" activity, even though no new duration risk was created. Re-couponing volume can completely dominate the observed trade universe. [[During_Fixed_Income_Ch30.md#page=339]]

## Evidence / Source Anchors

- Analysis of redundant offsetting swaps inflating the gross notional market size: [[During_Fixed_Income_Ch30.md#page=338]]
- Identification of TriOptima as a key service provider for trade compression: [[During_Fixed_Income_Ch30.md#page=338]]
- Definition of Re-couponing as a restructuring to reduce margin requirements: [[During_Fixed_Income_Ch30.md#page=338]]
- Description of the 'Crystallization' of P&L into cash during re-couponing: [[During_Fixed_Income_Ch30.md#page=339]]
- Discussion on why re-couponing inflates reported transaction volumes: [[During_Fixed_Income_Ch30.md#page=339]]

## Related

- [[Interest_Rate_Swap_Plain_Vanilla]] — The instruments being compressed.
- [[Margining_IM_Vs_VM]] — The collateral requirement that drives the need for re-couponing.
- [[ISDA_Master_Agreement_And_CSA]] — The legal framework governing the novation and termination.
- [[Over_The_Counter_OTC_Markets]] — The Fragmented environment where these redundancies grow.
