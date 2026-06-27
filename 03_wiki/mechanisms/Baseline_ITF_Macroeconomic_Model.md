---
title: Baseline ITF Macroeconomic Model
aliases:
- New Keynesian Three-Equation Model
- Modern Macroeconomic Consensus
- NKPC-IS-Taylor Framework
type: mechanism
tags:
- monetary-theory
- ITF
- macroeconomics
- math
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: Mô hình ITF nền tảng bao gồm ba phương trình cốt lõi—Cung tổng thể (NKPC),
  Cầu tổng thể (IS) và Quy tắc chính sách (Policy Rule)—cung cấp một khung phân tích
  vi mô về cách chính sách tiền tệ ổn định lạm phát và sản lượng.
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 230
created: '2026-04-18'
updated: '2026-04-22'
---

## Thesis

Developed by Clarida, Gali, and Gertler (1999) and Woodford (1997), this model represents the "New Neoclassical Synthesis." It proves that a central bank can anchor the entire economy by managing a single short-term interest rate, provided it influences public expectations correctly.

## The Three-Equation System

### 1. New Keynesian Phillips Curve (NKPC) - Supply Side
$$\pi_t = \beta E_t \pi_{t+1} + \alpha x_t + \epsilon_t$$
- **Logic:** Current inflation ($\pi_t$) is driven by future expectations and the output gap ($x_t$).
- **Implication:** If the central bank is credible, it can lower inflation by merely changing expectations, without causing a recession.

### 2. The IS Curve - Demand Side
$$x_t = E_t x_{t+1} - \delta(i_t - E_t \pi_{t+1}) + u_t$$
- **Logic:** The output gap depends on future expected output and the **Real Interest Rate** ($i_t - E_t \pi_{t+1}$).
- **Implication:** Monetary policy transmission works by altering the intertemporal substitution of consumption.

### 3. The Interest-Based Policy Rule
$$i_t = \phi_\pi \pi_t + \phi_x x_t + \phi_i i_{t-1} + v_t$$
- **The Taylor Principle:** For the system to be stable, $\phi_\pi$ must be $> 1$. If the central bank raises rates by less than the inflation spike, real rates fall, fueling more inflation (**Indeterminacy**).

## Optimal Policy Weights
The central bank minimizes a loss function where $\lambda$ represents the weight on output stability:
$$L = \frac{1}{2} [(\pi_t - \pi^*)^2 + \lambda x_t^2]$$
- **Strict ITF:** $\lambda = 0$ (Inflation Nutters).
- **Flexible ITF:** $\lambda > 0$ (Modern consensus, e.g., Bank Indonesia).

## Evidence / Source Anchors

- Generic three-equation system for modern macro thinking: [[Perry_Central_Bank_Policy_P4.md#page=230]]
- The problem of indeterminacy and the Taylor principle: [[Perry_Central_Bank_Policy_P4.md#page=231]]
- Distinction between Strict and Flexible ITF based on $\lambda$: [[Perry_Central_Bank_Policy_P4.md#page=231]]

## Related

- [[Inflation_Targeting_Framework_ITF]] — The strategic context.
- [[Taylor_Rule_Interest_Rate_Rule]] — The explicit version of Equation 3.
- [[Monetary_Policy_Transmission_Mechanism_MPTM]] — How these equations interact in reality.
