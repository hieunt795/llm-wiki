---
title: PAC vs. Sequential Tranches
aliases:
- Planned Amortisation Certificates
- PAC Bonds
- Sequential Pay Structure
type: mechanism
tags:
- structured-finance
- MBS
- tranching
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Fixed_Income_Alexander_During_Ch27.md
thesis: Tranching in RMBS redistributes prepayment risk among different classes of
  investors through Sequential Pay structures (managing time-subordination) or Planned
  Amortisation Certificates (managing prepayment volatility).
source_refs:
- file: Fixed_Income_Alexander_During_Ch27.md
  page: 299
- file: Fixed_Income_Alexander_During_Ch27.md
  page: 300
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

The unpredictable cash flows of a mortgage pool are unappealing to many institutional investors. Structural engineering via **Collateralised Mortgage Obligations (CMOs)** allows the creation of tranches with stable, bond-like schedules by diverting prepayment volatility to specialized "support" tranches.

## Mechanism

### 1. Sequential Pay
Principal repayments (both scheduled and prepayments) are directed to one tranche at a time.
- **Mechanism:** Tranche A receives all principal until it is retired, then Tranche B, and so on.
- **Investor Impact:** Senior tranches have a shorter, more predictable life (time-subordination) while junior tranches provide longer exposure.

### 2. Planned Amortisation Certificates (PAC)
The most sophisticated prepayment-risk management structure.
- **Mechanism:** A PAC tranche is guaranteed a fixed principal repayment schedule as long as the actual prepayment rate (CPR) stays within a predefined range (the **PAC Band**, e.g., 100-300 PSA).
- **Support Tranches:** Volatility is absorbed by **Support (or Companion) Tranches**. If prepayments are too fast, the surplus goes to the support tranche. If too slow, the support tranche's principal is diverted to keep the PAC on schedule.
- **Risk:** If prepayments fall outside the band for a prolonged period, the PAC "breaks" and starts behaving like a sequential tranche.

### Boundaries / Conditions

### Contraction vs. Extension Risk
- **Contraction Risk:** Rates fall, prepayments speed up, and the bond's life shortens just when reinvestment rates are low.
- **Extension Risk:** Rates rise, prepayments slow down, and the bond's life extends just when the investor could earn higher rates elsewhere.
PAC tranches effectively eliminate these risks within their bands.

## Evidence / Source Anchors

- Sequential pay and time-subordination: [[Fixed_Income_Alexander_During_Ch27.md#page=299]]
- PAC mechanics and the PAC Band: [[Fixed_Income_Alexander_During_Ch27.md#page=300]]
- The role of support tranches in protecting PAC stability: [[Fixed_Income_Alexander_During_Ch27.md#page=300]]

## Related

- [[Mortgage_Prepayment_Drivers]] — The underlying risk being managed.
- [[Residential_Mortgage_Backed_Securities_RMBS]] — The asset class.
- [[Securitization_And_Asset_Based_Finance_ABF]] — The broader structural framework.
- [[Prepayment_Risk_Tranching_And_PACs]]
- [[Credit_Risk_Transfer_CRT]]
- [[Structured_Notes]]
- [[Inverse_Floater]]
- [[Free_Banking_Vs_Central_Banking]]
- [[Lean_Vs_Clean_Monetary_Debate]]
- [[Narrow_Banking_Vs_Positive_Money]]
- [[Rules_Vs_Discretion_Debate]]
- [[Administered_Prices_Vs_Volatile_Food]]
- [[Agency_Vs_Principal_Clearing_Models]]
- [[Bilateral_Contracts_Vs_Securities]]
- [[Cyclical_vs_Structural_Stability_Policy]]
- [[CLO_Tranche_Structure_And_Loss_Allocation]]
- [[Operational_Targeting_Price_Vs_Quantity]]
