---
title: "One-Directional Standing Facility Implementation"
aliases: [One-Way Standing Facility, Asymmetric Corridor, Unidirectional Lending Window, Discount Window Only, Standing Facility Ceiling]
type: mechanism
tags: [monetary-operations, standing-facilities, interest-rate-corridor]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "One-directional standing facility provides only liquidity provision (lending) at fixed rate, establishing a ceiling for overnight rate but no floor, allowing rate to fall to near-zero in liquidity surplus."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 51
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
One-directional (asymmetric) standing facility-based implementation uses only a lending window at fixed rate to constrain short-term rates; this approach leaves rates unbounded on downside when banks have excess liquidity.

## 1. Core Logic / Mechanism

[RAW] **Asymmetric Framework** (Bindseil p.51, sec 4.1):
Central bank provides:
- **Lending facility** at rate $r_L$ (upper bound/ceiling for overnight rate)
- **NO deposit facility** (no floor; no rate floor protection)

**Rate Control Logic**:
- If overnight rate $r^{ON}$ rises above $r_L$: Banks can arbitrage by borrowing from CB at $r_L$ instead → rate cannot exceed $r_L$
- If overnight rate $r^{ON}$ falls below zero: No floor → banks may hold excess reserves at zero yield rather than lend in interbank market

[LLM] **Transmission Mechanism**:
$$\text{If } r^{ON} > r_L \text{ → Arbitrage pulls } r^{ON} \rightarrow r_L$$
$$\text{If } r^{ON} < 0 \text{ → No arbitrage constraint; } r^{ON} \text{ may be pulled down by excess liquidity}$$

This creates an **implicit ceiling** but no explicit **floor**. In liquidity surplus periods, rates can drift toward zero or become negative (if CB allows negative deposits).

[RAW] **Historical Manifestation** (Bindseil references):
- **German Reichsbank** (pre-WWI): Pure rediscount facility; no deposit facility
- **Federal Reserve 2013**: De facto one-directional post-QE (lending window available, but near-zero deposit rates provide minimal floor)

## 2. Worked Example

[LLM] **Normal Liquidity Day**:
- CB sets lending facility rate $r_L = 1.5\%$
- Demand for liquidity exists; banks must borrow to meet reserve targets
- Overnight rate: $r^{ON} = 1.45\%$ (banks prefer cheaper interbank market to CB lending)

[LLM] **Liquidity Stress Day**:
- Large deposit inflow to banking system
- Banks accumulate excess reserves (no investment opportunity at 0% deposit rate)
- Overnight rate: $r^{ON} = 0.00\%$ (cannot go negative without deposit facility)
- Banks are indifferent between holding excess reserves at 0% or lending at 0%
- Volatility risk: Rate spikes when shock reverses (sudden withdrawal) → banks need borrowing facility urgently

[LLM] **Crisis Scenario**:
If deposit flight occurs:
- Overnight rate could spike above $r_L = 1.5\%$ momentarily (until banks recognize standing facility)
- If information frictions or stigma prevent facility use, rate can spike well above $r_L$ (see [[Collateral_Scarcity_And_Effective_Term_Funding_Costs]])

## 3. Failure Conditions / Boundaries

- **Rate Floor Missing**: Without deposit facility, rates can become excessively low, reducing incentive for banks to actively manage liquidity
- **Stigma in Crisis**: Banks may avoid borrowing facility due to signaling effect (market interprets CB borrowing as distress)
- **Volatility Asymmetry**: Rate can spike sharply on demand shocks but drift gradually downward on supply shocks
- **QE Incompatibility**: In quantitative easing phase (excess reserves system-wide), one-directional facility becomes increasingly irrelevant; floor becomes only binding constraint
- **Negative Rate Transmission**: If CB tries to implement negative rates, one-directional facility cannot steer them below zero (no floor below zero)

## 4. Alternative Approaches

Bindseil identifies two superior symmetric alternatives (Chapters 4.2-4.3):
1. **Symmetric Corridor with CB-Determined OMO Volume**: CB sets both facility rates and OMO size
2. **Full Allotment OMOs within Corridor**: CB sets corridor rates; banks determine OMO demand at fixed (often zero) spread

Both provide both ceiling (lending facility) and floor (deposit facility) for overnight rate control.

## Related
- [[Interest_Rate_Corridor_And_Standing_Facilities]]
- [[Standing_Facilities_Optimal_Width_In_Symmetric_Corridor]]
- [[Open_Market_Operations_And_Instruments]]
- [[Overnight_Index_Swaps_OIS_Pricing_Dynamics]]
- [[Collateral_Scarcity_And_Effective_Term_Funding_Costs]]
