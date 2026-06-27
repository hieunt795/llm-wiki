---
title: Cash Stub Rate
aliases:
- Stub Rate
- Curve Anchor
- Cash Stub
type: mechanism
tags:
- money-market
- valuation
- yield-curve
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch16.md
thesis: The cash stub rate is the spot interest rate for the immediate period from
  today until the start of the first liquid forward-starting contract, serving as
  the foundational anchor for building the entire term structure.
source_refs:
- file: During_Fixed_Income_Ch16.md
  page: 132
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

When constructing a yield curve from derivatives (like the Libor futures strip), a mathematical gap exists between the current date ($t_0$) and the start date of the first contract ($t_1$). This gap is filled by the **Cash Stub Rate**. Alexander Düring explains that while the rest of the curve is built from forward-looking derivatives, the stub rate must be taken from the actual spot deposit or repo market. [[During_Fixed_Income_Ch16.md#page=132]]

## Mechanism: The Recursive Extension

The term structure of money market rates is built recursively starting from the anchor:

1.  **The Anchor:** The Stub Rate $r(t_0, t_1)$ is observed from liquid overnight or short-dated cash markets.
2.  **The First Extension:** The first futures-implied rate $r(t_1, t_2)$ is combined with the stub using the recursive relationship:
$$(1 + r(t_0, t_2)DCF(t_0, t_2)) = (1 + r(t_0, t_1)DCF(t_0, t_1)) \times (1 + r(t_1, t_2)DCF(t_1, t_2))$$
3.  **The Chain:** This process is repeated for the 2nd, 3rd, and 4th quarterly contracts (the Libor strip) to build the spot curve out to the desired maturity. [[During_Fixed_Income_Ch16.md#page=132-133]]

## Strategic Implications: Convexity and Fitting

Before the futures-implied forward rates can be added to the chain, they must undergo a **Convexity Adjustment** (following $\Delta r = -\frac{1}{2} \sigma^2 t^2$). Without this adjustment, the spot curve would be systematically biased upwards. The cash stub provides the "physical grounding" for these derivative-based projections. [[During_Fixed_Income_Ch16.md#page=132]]

## Evidence / Source Anchors

- Definition of the cash stub as the rate until the start of the first Libor contract: [[During_Fixed_Income_Ch16.md#page=132]]
- Description of the recursive term structure building process: [[During_Fixed_Income_Ch16.md#page=132-133]]
- Visual representation of the Libor strip relationship with spot rates: [[During_Fixed_Income_Ch16.md#page=133]]
- Link between the stub rate and the necessity of convexity adjustments: [[During_Fixed_Income_Ch16.md#page=132]]

## Related

- [[Forward_Rates_Derivation]] — The mathematical engine for the recursive chain.
- [[Yield_Curve_Construction_Bootstrapping]] — The broader process of which the cash stub is Step 1.
- [[Money_Market_Futures_And_Convexity]] — The source of the forward rates that the stub anchors.
