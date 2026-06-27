---
title: Real Yield
aliases:
- rho
- Real Interest Rate
- Lợi suất thực
type: definition
tags:
- fixed-income
- inflation
- macroeconomics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch24.md
thesis: Real yield is the interest rate earned on an investment after adjusting for
  the loss of purchasing power, representing the internal rate of return of an instrument's
  real (inflation-adjusted) cashflows.
source_refs:
- file: During_Fixed_Income_Ch24.md
  page: 240
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 6333-6553
  section: "Chapter 8: Inflation-linked bonds"
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

In the nominal bond market, the "yield" is the headline number. In the linker market, the **Real Yield** ($\rho$) is the primary variable. Alexander Düring explains that the most precise way to think about real yield is via the **FX Analogy**: if inflation-linked bonds are bonds denominated in a "purchasing power currency," then the real yield is simply the yield of those bonds in their home currency. It is the rate of return an investor receives in terms of actual baskets of goods. [[During_Fixed_Income_Ch24.md#page=240]]

## Mechanism: Calculation and Interpretation

Real yield is calculated by applying the standard yield equation (IRR) to the **real cashflows** and the **real clean price** of a bond, effectively ignoring the inflation uplift component.

### 1. The Real vs. Nominal Spread
The relationship between real yield ($\rho$) and nominal yield ($r$) is the basis for [[Breakeven_Inflation_Metrics|breakeven inflation]].
- **Expansion:** If nominal yields rise while real yields stay constant, the market is signaling higher inflation expectations.
- **Contraction:** If real yields rise faster than nominal yields, the market is signaling a tightening of real financial conditions (higher cost of capital in purchasing power terms). [[During_Fixed_Income_Ch24.md#page=241]]

### 2. The Multi-Currency Perspective
For a USD-based investor:
- **JGB Yield (Nominal):** Equivalent to the "Real Yield" of a TIPS.
- **UST Yield (Nominal):** The best estimate of the nominal return of that JGB once converted back to inflated cash.
- **The Insight:** Real yield is the return in the "domestic" market of consumption. [[During_Fixed_Income_Ch24.md#page=240]]

## Boundaries / Conditions: The Negative Yield Phenomenon

Real yields can, and frequently do, turn **negative**.
- **The Logic:** A negative real yield means an investor is willing to pay a "storage fee" to ensure they can purchase a nearly-identical basket of goods in the future, reflecting extreme risk aversion or central bank suppression of nominal rates below the inflation rate. [[During_Fixed_Income_Ch24.md#page=244]]

## Evidence / Source Anchors

- Definition of real yield as the IRR of real coupons and real price: [[During_Fixed_Income_Ch24.md#page=240]]
- Use of the FX analogy (USD/JPY example) to explain real yield dynamics: [[During_Fixed_Income_Ch24.md#page=240]]
- Analysis of the link between real yields and breakeven inflation: [[During_Fixed_Income_Ch24.md#page=241]]
- Discussion on the economic significance of negative real yields: [[During_Fixed_Income_Ch24.md#page=244]]

## Related

- [[Inflation_Indexed_Bonds]] — The assets that provide real yields.
- [[Breakeven_Inflation_Metrics]] — The metric that uses real yield as an input.
- [[TIPS_Bond_Structure]] — How real yields are translated into nominal payments.
- [[Real_Short_Rate]] — The short-term equivalent $(\text{Repo} - \text{Inflation})$.
