---
title: Optimal Width of the Corridor
aliases:
- Độ rộng tối ưu của hành lang lãi suất
- Corridor width trade-offs
type: mechanism
tags:
- monetary-policy
- interest-rate-corridor
- market-turnover
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Ulrich Bindseil
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: The optimal corridor width balances the trade-off between interest rate stability
  (narrow corridor) and interbank market turnover/discipline (wide corridor), accounting
  for transaction costs and central bank risk-taking.
source_refs:
- file: Bindseil_Monetary_Policy_Operations.md
  page: 73
created: '2026-04-26'
updated: '2026-04-26'
chapter: 6
---

# [[Optimal_Width_of_the_Corridor]]

## Thesis
[WIKI] Central banks must decide how wide the spread between the borrowing and deposit rates should be. A narrow corridor ensures low volatility but suppresses the interbank market, while a wide corridor encourages trading but increases rate volatility.

## Mechanism: The Fundamental Trade-offs

### 1. Interest Rate Control vs. Interbank Turnover
[RAW] A very narrow corridor would probably be very effective in steering the overnight interest rate, but at the same time the Riksbank would take over much of the risk distribution that is currently done on the overnight market. [[Bindseil_Monetary_Policy_Operations.md#page=74]]

[LLM] If the corridor is zero (borrowing rate = deposit rate), banks have no incentive to trade with each other because the central bank provides a costless substitute for the interbank market.

### 2. Market Discipline and Signaling
[RAW] Any corridor would need to allow for credit tiering, since widening credit spreads are an important signal of potential financial stress. [[Bindseil_Monetary_Policy_Operations.md#page=74]]

[LLM] A wide corridor forces banks to "test their name" in the commercial credit market. The rates at which they trade reveal information about their perceived creditworthiness, which the central bank can use as a signal.

### 3. Transaction Costs ($C_{MM}$)
[RAW] If there is a cost $C_{MM}$ associated with transacting in the market, the average volume of interbank trading will depend both on $C_{MM}$ and on the width of the standing facilities corridor. [[Bindseil_Monetary_Policy_Operations.md#page=76]]

[LLM] Banks will only trade if the difference in their marginal valuation of reserves exceeds the transaction cost. A wider corridor increases the "penalty" for using the central bank, thus making interbank trading more attractive even when transaction costs are present.

## Analytical Model (Bindseil & Jablecki)
[RAW] Wider standing facilities corridors are associated with greater interbank trading volumes and greater volatility of the overnight interest rate. In view of the concavity of the turnover function, and the convexity of the variance function, it seems plausible that a central bank... will prefer an interior value. [[Bindseil_Monetary_Policy_Operations.md#page=80]]

[LLM]
- **Turnover function:** Increases rapidly at first, then flattens as the corridor widens.
- **Variance function:** Rate volatility increases exponentially as the corridor widens.
- **Optimal Point:** Usually found where the marginal gain in turnover no longer justifies the marginal increase in volatility.

## Evidence / Source Anchors
- [[Bindseil_Monetary_Policy_Operations.md#page=73]] — Introduction to the optimal width problem.
- [[Bindseil_Monetary_Policy_Operations.md#page=74]] — Trade-offs identified by BoC, Riksbank, and BoE.
- [[Bindseil_Monetary_Policy_Operations.md#page=80]] — Simulation results on turnover vs. volatility.

## Related
- [[Symmetric_Corridor_Approach]]
- [[Interbank_Market_Discipline]]
- [[Central_Bank_Balance_Sheet_Length]]
- [[Symmetric_Corridor_Framework_Bindseil]]
- [[Asymmetric_Lending_Corridor]]
- [[Full_Allotment_OMO_Mechanics]]
- [[Interest_Rate_Corridor_And_Standing_Facilities]]
- [[2026-04-26_monetary_policy_synthesis]]
- [[Financial_Deepening]]
- [[Standing_Facilities_Optimal_Width_In_Symmetric_Corridor]]
- [[Financial_Repression]]
- [[Fiscal_Dominance]]
- [[Inflation_Targeting_Economic_Performance_Evaluation]]
