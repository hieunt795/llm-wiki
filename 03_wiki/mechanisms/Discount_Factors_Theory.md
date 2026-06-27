---
title: Discount Factors Theory
aliases:
- Df(t)
- Discount Factor
- Present Value Arbitrage
- Theoretical Discount Factor
- Chiết khấu
type: mechanism
tags:
- quantitative-finance
- valuation
- interest-rates
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch14.md
thesis: The Discount Factor, $Df(t)$, is the fundamental unit of fixed income valuation,
  representing the present value of a single unit of currency delivered at a future
  time $t$, integrating inflation, credit risk, interest rate risk, and liquidity
  preference into a singular mathematical anchor.
source_refs:
- file: During_Fixed_Income_Ch14.md
  page: 112
- file: During_Fixed_Income_Ch14.md
  page: 113
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Modern fixed income mathematics strips away the subjective noise of "interest rates" (which are dependent on daycount conventions and compounding rules) and reduces all valuation to the absolute truth of cash: The **Discount Factor**, $Df(t)$. Every other metric—from yield to maturity to option Greeks—is built on top of this foundation. Economically, the discount factor represents the market's collective "punishment" of future value relative to immediate cash in hand. [[During_Fixed_Income_Ch14.md#page=112]]

## Mechanism: The Drivers of Value Decay

A discount factor $Df(t) < 1.0$ (in normal positive-rate environments) reflects four distinct friction points:
1.  **Inflation:** The future unit of currency will purchase fewer goods than today.
2.  **Credit Risk:** The danger that the counterparty making the promise to pay will default before time $t$.
3.  **Interest Rate Risk:** The opportunity cost of locking in a rate today when better lending terms might be available tomorrow.
4.  **Liquidity Preference:** The biological and structural preference for immediate "cash in hand" over a deferred claim. [[During_Fixed_Income_Ch14.md#page=112]]

## The Uniqueness Principle (Arbitrage Theory)

In a frictionless market, for any given time $t$, there is exactly one $Df(t)$ for each issuer and instrument type. If two different discount factors existed ($Df'(t) > Df''(t)$), a riskless profit could be harvested:
1.  **Sell (Short)** 100 units of the "expensive" instrument ($Df'$). You receive $100 \times Df'(t)$ today and accept a liability to pay 100 at time $t$.
2.  **Buy (Long)** 100 units of the "cheap" instrument ($Df''$). You pay only $100 \times Df''(t)$.
3.  **Profit:** You pocket the difference $(100 \times (Df' - Df''))$ immediately. At time $t$, the long position perfectly funds the short liability. [[During_Fixed_Income_Ch14.md#page=113]]

## Boundaries / Conditions: Real-World Friction

In practice, multiple discount factors for comparable cashflows can persist because the arbitrage above is often impossible to execute:
- **Repo Scarcity:** To sell an instrument short, one must be able to borrow it. If the repo market is illiquid or the "Special" rate is too high, the transaction cost exceeds the arbitrage profit.
- **Indivisibility:** Bond cashflows (coupons) are often bundled together. It may be impossible to separate an individual payment at time $t$ to trade it against a standalone money market instrument.
- **Maturity Distance:** If $t$ is very far in the future, the small mathematical difference between discount factors may not justify the multi-decade capital commitment required to exploit it. [[During_Fixed_Income_Ch14.md#page=113]]

## Evidence / Source Anchors

- Definition of the Discount Factor and its four economic components: [[During_Fixed_Income_Ch14.md#page=112]]
- Proof of discount factor uniqueness via riskless arbitrage: [[During_Fixed_Income_Ch14.md#page=113]]
- Analysis of why unique discount factors fail in practice (Repo, Indivisibility): [[During_Fixed_Income_Ch14.md#page=113]]

## Related

- [[Daycount_Conventions]] — The rules used to translate $Df(t)$ back into human-readable interest rates.
- [[Yield_Curve_Construction_Bootstrapping]] — The algorithmic process of extracting $Df(t)$ from market prices.
- [[Repurchase_Agreement_Mechanism]] — The primary mechanism that facilitates (or blocks) discount factor arbitrage.
- [[Compounding_Mechanics]] — The mathematical link between $Df(t)$ and interest rates over multiple periods.
