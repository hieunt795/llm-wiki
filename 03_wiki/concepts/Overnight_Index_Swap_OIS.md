---
title: Overnight Index Swap (OIS)
aliases:
- OIS
- Overnight index swap
- SONIA swap
- EONIA swap
type: concept
tags:
- derivatives
- interest-rate-risk
- fixed-income
- swap-mechanics
- overnight-rates
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: An OIS is an interest rate swap where the floating leg equals the average of an overnight index (SONIA/EONIA) rather than tenor LIBOR. Enables banks to synthetically transform fixed deposit funding into overnight-indexed exposure, with annual compounding for maturities exceeding one year.
source_refs:
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 650-659
  section: Overnight index swap
created: '2026-05-07'
updated: '2026-05-07'
---

## Thesis

An OIS is an IRS variant where the floating leg is set to the average of an overnight index (SONIA in GBP, EONIA in EUR) rather than tenor LIBOR. This enables funding transformation: a bank accepting fixed-rate deposits can swap into overnight-index exposure, converting liability structure without changing absolute spread.

---

## 1. Structure: Overnight Index vs. Tenor LIBOR

### A. Core Distinction from Vanilla IRS
[RAW-BOOK:5] An overnight index swap (OIS) differs from standard interest rate swaps in the **floating leg specification**:
- **Vanilla IRS floating leg:** Fixed to a tenor rate (3M LIBOR, 6M LIBOR, etc.)
- **OIS floating leg:** Equal to the **average of an overnight index** such as:
  - SONIA (Sterling Overnight Index Average, GBP)
  - EONIA (Euro OverNight Index Average, EUR)

[RAW-BOOK:5] The fixed leg of the swap is set at a level ensuring the transaction constitutes an "equitable exchange of cash flows."

---

## 2. Application: Funding Transformation

### A. Bank Liability Transformation
[RAW-BOOK:5] One simple application: A bank has agreed to take money on deposit at a **fixed rate**. Using an OIS, the bank can **transform the nature of their interest rate risk**:

1. Bank accepts fixed-rate deposit from customer
2. Bank enters OIS: **receives fixed rate** | **pays overnight index rate**
3. Assuming the two fixed rates are equal (on-market), they net to zero
4. **Net result:** Bank has acquired funds and is paying the overnight index rate

### B. Economic Mechanics
[RAW-BOOK:5] By entering the OIS as a receiver of fixed, the bank:
- **Eliminates its fixed-rate liability** (the deposit's fixed coupon is offset by OIS fixed receipt)
- **Converts liability to overnight-indexed funding** (must now pay overnight rate on a compounded basis)

This provides flexibility in managing liability funding structures and hedging duration exposure.

---

## 3. Settlement & Payment Conventions

### A. Maturity-Dependent Settlement
[RAW-BOOK:5] OIS settlement follows different conventions by maturity:

- **OIS with maturity < 1 year:** Fixed versus compounded floating payments exchanged at maturity (single settlement date)
- **OIS with maturity ≥ 1 year:** Payments exchanged annually

[RAW-BOOK:5] This convention reflects the compounding nature of overnight rates; longer-dated OIS break payments into annual buckets to manage operational simplicity.

### B. Compounding Mechanics
[RAW-BOOK:5] For overnight-index floaters, the coupon is computed by compounding the daily overnight rates over the accrual period, not by simple interest. This is fundamental to OIS valuation and requires careful handling in pricing models.

---

## 4. OIS vs. Tenor Basis in Modern Markets

[RAW-BOOK:5] The emergence of OIS as a primary risk-transfer tool reflects:
- **Reduced LIBOR volumes** and increased reliance on secured overnight funding rates
- **Central bank operational corridors** (e.g., Fed funds rate, SONIA) serving as anchors
- **Transition from LIBOR to overnight indices** in many jurisdictions (e.g., SOFR in USD, SONIA in GBP post-2021)

OIS pricing typically reflects **lower credit spread** than tenor LIBOR swaps because overnight secured rates embed lower counterparty risk.

---

## Evidence / Source Anchors
- OIS definition and overnight index specification (SONIA/EONIA): [[Schofield_Trading_Fixed_Income_2011.md#page=650-652]]
- Bank liability transformation application: [[Schofield_Trading_Fixed_Income_2011.md#page=654]]
- Settlement by maturity (< 1 year at maturity, ≥ 1 year annually): [[Schofield_Trading_Fixed_Income_2011.md#page=654]]

---

## Related
- [[Interest_Rate_Swap_IRS]]
- [[LIBOR_Floating_Rate_Mechanics]]
- [[SONIA_Sterling_Overnight_Index]]
- [[EONIA_Euro_Overnight_Index]]
- [[Funding_Transformation_Mechanics]]
- [[Swap_Market_Basis_Trades]]
