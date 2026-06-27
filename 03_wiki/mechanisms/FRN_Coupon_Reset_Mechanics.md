---
title: FRN Coupon Reset Mechanics
aliases:
- Coupon Reset
- Reset Lag
- In-arrears FRN
- Quoted Margin
- spread
type: mechanism
tags:
- fixed-income
- interest-rates
- settlement
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch18.md
thesis: FRN reset mechanics define the timing and methodology for observing benchmarks,
  utilizing specific lookback lags (T-2 or T-5) and term-rate approximations to ensure
  predictable settlement and continuous accrued interest calculation.
source_refs:
- file: During_Fixed_Income_Ch18.md
  page: 170
- file: During_Fixed_Income_Ch18.md
  page: 172
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The reset schedule of an FRN is its operational heartbeat. Because money markets settle with a lag (typically T+2), the benchmark rate for an accrual period starting today ($T$) must be observed from the past. Alexander Düring bóc tách các ma sát về thời gian này, từ cấu trúc truyền thống đến những giải pháp kỹ thuật phức tạp trong kỷ nguyên hậu LIBOR. [[During_Fixed_Income_Ch18.md#page=170]]

## Mechanism: Timing and Lags

### 1. Standard Reset (In-advance)
- **Formula:** $C_i = R(t_i - 2) + \mu$
- **The T-2 Lag:** Benchmarks are observed 2 business days before the period starts. This allows the bank to finalize the coupon amount and set up settlement before the interest begins to accrue.
- **Quoted Margin ($\mu$):** The fixed credit spread added to the benchmark at issuance. [[During_Fixed_Income_Ch18.md#page=170]]

### 2. In-Arrears Structures
- **Mechanism:** The coupon fixing date is delayed until the *end* of the period (often at the payment date).
- **The Pricing Penalty:** Because the accrual rate is unknown until the very end, it is impossible to calculate **Accrued Interest** for secondary market trades. Consequently, in-arrears FRNs must trade on **Dirty Price**, unlike standard bonds. [[During_Fixed_Income_Ch18.md#page=170]]

## The Post-LIBOR Challenge: Overnight Compounding

Modern FRNs linked to overnight rates (SOFR/€STR) face a structural disadvantage: the final coupon is not known until the last day of the period.

### The $\rho(t)$ Solution
Instead of simple daily compounding (which obscures accrued interest), markets use a term-rate approximation:
- **The Mechanism:** Markets calculate an annualized compound interest $\rho(t)$ from the last payment date to any settlement date $t$.
- **The Lag:** A standard observation lag of **5 business days** (T-5) is used in European markets to enable predictable T+2 settlement while still allowing for defined accrued interest based on the best estimate of the eventual payment. [[During_Fixed_Income_Ch18.md#page=172]]

## Evidence / Source Anchors

- Rationale for the T-2 lag in money market settlement: [[During_Fixed_Income_Ch18.md#page=170]]
- Identification of the Dirty Price requirement for in-arrears structures: [[During_Fixed_Income_Ch18.md#page=170]]
- Formula and logic for the intermediate term rate $\rho(t)$: [[During_Fixed_Income_Ch18.md#page=172]]
- Selection of the 5-day lag for overnight benchmarks: [[During_Fixed_Income_Ch18.md#page=172]]

## Related

- [[Floating_Rate_Notes_FRN]] — The broader instrument category.
- [[LIBOR_Transition_And_Benchmarks]] — The source of the indices $(R)$.
- [[Clean_Vs_Dirty_Price]] — Why the timing of the reset forces a change in pricing convention.
- [[Overnight_Index_Rates_FRN_Compounding]] — Detailed view of the compounding math.
