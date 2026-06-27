---
title: "Reserve Averaging and Martingale Property of Overnight Rates"
aliases: [Averaging Mechanism, Multi-day Averaging Period, Reserve Maintenance Averaging, Overnight Rate Martingale, Martingale Property]
type: mechanism
tags: [monetary-operations, reserve-requirements, interest-rate-volatility]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "Multi-day reserve averaging allows banks to tolerate within-period liquidity shocks; under averaging, overnight rate follows martingale property (expected future rate = current rate)."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 66
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Reserve averaging mechanism permits banks to maintain reserve balances below required level on individual days, provided average across maintenance period meets requirement; this stabilizes overnight rate through martingale property.

## 1. Core Logic / Mechanism

[RAW] **Averaging Framework** (Bindseil p.66, sec 5.2):
- Reserve maintenance period: $T$ days (e.g., $T = 3$ for ECB)
- Requirement: Daily snapshots previously → **Now**: Average across $T$ days
- Bank flexibility: If day 1 reserve balance = 80% of required, can catch up on day 2 or 3

[LLM] **Mechanic Flow**:

Day 1: Deposit shock $d_1$ (negative = outflow)
- Bank reserve: $R_1 = \text{Target} - d_1$
- CB does NOT intervene (tolerance within averaging period)
- Overnight rate: $r_1^{ON}$ reflects liquidity conditions

Day 2: Deposit shock $d_2$
- Bank reserve: $R_2 = R_1 + d_2$
- Bank evaluates: Is average $\frac{R_1 + R_2}{2} \geq \text{Required}$?

Day 3: Final day
- Bank reserve: $R_3 = R_2 + d_3$
- Bank ensures: $\frac{R_1 + R_2 + R_3}{3} = \text{Required}$ (exactly or surplus)

[RAW] **Martingale Property** (Bindseil p.66, sec 5.2):
Under averaging with no systematic trend in shocks, overnight rate satisfies:
$$E[r_t^{ON} | \mathcal{F}_{t-1}] = r_{t-1}^{ON}$$

**Intuition**: 
- If today's rate is 1.2%, bank has no reason to expect tomorrow's rate to be systematically higher or lower
- Since banks can defer today's liquidity adjustment to later in period, they're indifferent between borrowing today at 1.2% vs. borrowing tomorrow at expected 1.2%
- This indifference implies no expected drift → martingale

[LLM] **Stabilization Mechanism**:
- **Without averaging**: Each day must balance, shock $d_1$ causes rate spike on day 1 if CB doesn't inject
- **With averaging**: Bank can absorb $d_1$ internally, borrow less from CB on day 1, repay more on days 2-3
- **Result**: CB operations needed are spread across period → smoother path for overnight rate volatility

## 2. Worked Example

[LLM] **Three-Day Period with Shocks**:

Target daily reserve: 100

**Day 1**:
- Shock: $d_1 = -20$ (deposit withdrawal)
- Reserve at end of day: $R_1 = 100 - 20 = 80$
- Average to date: $\bar{R} = 80$ (below required)
- Bank's position: Can manage if shocks reverse later
- Overnight rate: Tight ($r_1 = 1.5\%$) due to aggregate deficit, but not catastrophic

**Day 2**:
- Shock: $d_2 = +15$ (deposits inflow)
- Reserve: $R_2 = 80 + 15 = 95$
- Average: $\bar{R} = \frac{80 + 95}{2} = 87.5$ (still short)
- Bank: Must catch up on day 3
- Overnight rate: $r_2 = 1.45\%$ (slightly easier)

**Day 3**:
- Shock: $d_3 = +35$ (large inflow, end-period settlement)
- Reserve: $R_3 = 95 + 35 = 130$
- Final average: $\bar{R} = \frac{80 + 95 + 130}{3} = 101.67$ (compliant)
- Overnight rate: $r_3 = 1.30\%$ (eases significantly)

**Martingale Check**: At start of day 1, expected rate on day 2 ≈ day 1 rate (no systematic drift expected). This holds only if shocks are random (mean-zero).

## 3. Failure Conditions / Boundaries

- **Systematic Drift**: If shocks are not mean-zero (e.g., continuing deposit outflows), martingale breaks → expected rate drifts downward (or upward)
- **End-of-Period Crunch**: If all shocks cluster in final days, CB may face sudden large borrowing demand on final day → rate spike
- **Collateral Constraints**: Averaging provides NO relief if banks hit collateral limit before period end (see [[Collateral_Constraints_In_Monetary_Operations]])
- **Counterparty Risk**: If bank faces rolling-over term funding, averaging doesn't help (only overnight averages)
- **Procyclicality**: In stress, averaging can concentrate demand into final days when spreads widen most (amplifying volatility)

## 4. Mathematical Foundation

[LLM] **Formal Martingale Condition**:

Under averaging, if bank has $N$ days remaining in period and current reserve deficit = $x$:
- Bank borrowing demand on day $t$ = $\frac{x}{N-t+1}$ (linear repayment path)
- Overnight rate on day $t$ reflects aggregate borrowing demand
- If all banks follow same logic and shocks are i.i.d., overnight rate $r_t^{ON}$ is martingale

Proof sketch: $E[r_{t+1}^{ON} - r_t^{ON} | r_t^{ON}] = 0$ because both deficit and shock are symmetric

## Related
- [[Reserve_Requirements_As_Monetary_Control_Instruments]]
- [[Interest_Rate_Corridor_And_Standing_Facilities]]
- [[Overnight_Index_Swaps_OIS_Pricing_Dynamics]]
- [[Interbank_Money_Market_Mechanism]]
- [[Liquidity_Management_Operations]]
