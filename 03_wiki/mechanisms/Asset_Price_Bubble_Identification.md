---
title: Asset Price Bubble Identification
aliases:
- Growing Bubbles
- Fundamental Price Deviation
- Property Price Bubble Indicator
type: mechanism
tags:
- asset-prices
- bubbles
- systemic-risk
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: An asset price bubble occurs when the market price significantly and persistently
  exceeds the fundamental price derived from discounted expected returns, serving
  as a primary leading indicator of systemic financial crises.
source_refs:
- file: Perry_Central_Bank_Policy_P6.md
  page: 440
- file: Perry_Central_Bank_Policy_P6.md
  page: 441
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

Why do bubbles exist if markets are efficient? Perry Warjiyo notes that in reality, bubbles are often **Growing Bubbles** driven by herding and cheap credit. For a central bank, the challenge is not just identifying the bubble but determining when the "Misalignment" becomes a threat to FSS.

## Mechanism: The Pricing Gap

The market price ($P_t$) is decomposed into:
$$P_t = P^*_t + f(x)$$
Where:
- $P^*_t = \sum_{i=0}^{\infty} E \left[ \frac{R_{t+i}}{(1+r)^i} \right]$ is the fundamental price (NPV of returns).
- $f(x)$ is the **Market Deviation** or the "Bubble Component."

### Characteristics of Bubbles
- **Random Walk vs. Exponential:** In an efficient market, $f(x)$ is a random error with zero mean. In a bubble, $f(x)$ becomes non-zero and often grows exponentially as more speculators enter the market.
- **Sector Concentration:** Experience shows that **Property Bubbles** are far more dangerous than stock market bubbles because property is heavily used as bank collateral.

## Case Study: 2008 GFC vs. 1997 Asian Crisis
- **GFC:** Driven by a US housing bubble facilitated by securitization (MBS) and excessive risk-taking.
- **Asian Crisis:** Driven by property price bubbles combined with weak banking regulation in Thailand and Indonesia.
- **Counter-example:** Hong Kong and Singapore survived the 1997 property burst due to strong **Microprudential** regulation.

## Evidence / Source Anchors

- Mathematical definition of bubble deviation $f(x)$: [[Perry_Central_Bank_Policy_P6.md#page=440]]
- Identification of property bubbles as the best predictor of crisis: [[Perry_Central_Bank_Policy_P6.md#page=441]]
- Comparison of resilience across Asian banking systems: [[Perry_Central_Bank_Policy_P6.md#page=442]]

## Related

- [[Macro-Financial_Linkages]] — Why bubbles spill over to the real economy.
- [[Financial_Procyclicality_Mechanism]] — How bubbles amplify cycles.
- [[Loan_to_Value_LTV_Policy]] — The surgical tool used to pop property bubbles.
