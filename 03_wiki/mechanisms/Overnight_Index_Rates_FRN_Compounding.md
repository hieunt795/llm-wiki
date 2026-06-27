---
title: 'Overnight Index Rates: FRN Compounding'
aliases:
- SOFR Floater
- €STR Floater
- Backward-looking Compounding
- ρ(t)
type: mechanism
tags:
- fixed-income
- interest-rates
- LIBOR-transition
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch18.md
thesis: Modern FRNs linked to overnight benchmarks (like SOFR or €STR) utilize a backward-looking
  compounding mechanism with an intermediate term rate ρ(t) to reconcile daily interest
  volatility with the operational need for predictable accrued interest and T+2 settlement.
source_refs:
- file: During_Fixed_Income_Ch18.md
  page: 172
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The transition from LIBOR (a forward-looking term rate) to overnight benchmarks (backward-looking transaction rates) created a structural problem for FRN settlement. Since the final overnight compounded rate is only known at the very end of a coupon period, investors would normally be unable to calculate **Accrued Interest** for secondary market trades. Alexander Düring bóc tách giải pháp kỹ thuật: sử dụng tỷ suất kỳ hạn giả định và độ trễ quan sát để khôi phục khả năng tính lãi dồn tích. [[During_Fixed_Income_Ch18.md#page=172]]

## Mechanism: The ρ(t) Bridge

Instead of simply compounding the overnight rate $r$ and adding the spread $\mu$ at the end (which would compound the spread as well), modern FRN documentation uses an intermediate term rate $\rho(t)$:

### 1. The Calculation of ρ(t)
$\rho(t)$ is the annualized compound interest between the last coupon payment ($t_0$) and any settlement date ($d$) within the period:
$$\rho(t) = \frac{\prod_{t=t_0}^d [1 + r(t-l) \times DCF(t, t+1)] - 1}{DCF(t_0, d)}$$
- where $l$ is the observation lag (typically 5 business days). [[During_Fixed_Income_Ch18.md#page=172]]

### 2. The Accrued Interest Calculation
Once $\rho(t)$ is calculated, the interim coupon fixing and accrued interest are derived as if they were a standard term rate:
$$\text{Coupon Fixing} = \rho(t) + \mu$$
This ensures that the **Quoted Margin ($\mu$)** is not compounded, keeping it directly comparable to old LIBOR margins. [[During_Fixed_Income_Ch18.md#page=172]]

### 3. The 5-Day Lag Logic
In European markets (€STR), the standard lag $l$ was selected to be **5 business days** rather than the usual T+2.
- **The Reason:** This enables a longer window for T+2 settlement while ensuring that the overnight rates for the settlement cycle are already known, providing a stable "best estimate" of the eventual coupon payment. [[During_Fixed_Income_Ch18.md#page=172]]

## Evidence / Source Anchors

- Analysis of the structural disadvantage of simple overnight compounding for accrued interest: [[During_Fixed_Income_Ch18.md#page=172]]
- Mathematical derivation of the intermediate term rate $\rho(t)$: [[During_Fixed_Income_Ch18.md#page=172]]
- Rationale for not compounding the quoted margin $\mu$: [[During_Fixed_Income_Ch18.md#page=172]]
- Selection of the 5-day lag for €STR-linked FRNs: [[During_Fixed_Income_Ch18.md#page=172]]

## Related

- [[FRN_Coupon_Reset_Mechanics]] — The broader operational framework for these resets.
- [[LIBOR_Transition_And_Benchmarks]] — The source of the new overnight indices.
- [[Floating_Rate_Notes_FRN]] — The underlying instrument structure.
- [[Accrued_Interest_Conventions]] — How $\rho(t)$ enables these conventions to persist.
