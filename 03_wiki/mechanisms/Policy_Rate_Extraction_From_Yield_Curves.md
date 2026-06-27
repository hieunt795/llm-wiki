---
title: Policy Rate Extraction from Yield Curves
aliases:
- Central Bank Probability Pricing
- The Term Risk Premium Bias
type: mechanism
tags:
- quantitative-finance
- central-banking
- yield-curves
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch15.md"
thesis: Extracting pure Central Bank policy expectations from observable yield curves
  requires modeling an identical synthesized 'Overnight Cash Account' mapped physically
  against Central Bank scheduled meeting dates, violently scrubbing raw market data
  for structural distortions—specifically the Credit Basis, the Turn Premium, and
  the aggressively deceptive Term Risk Premium.
source_refs:
- file: Fixed_Income_Alexander_During_Ch15.md
  page: 134
created: '2026-04-16'
updated: '2026-04-16'
---

## Thesis

Market commentators frequently state: "The market is pricing in a $75\%$ probability of an ECB rate cut next month." This percentage is not a guess; it is mathematically reverse-engineered from the front end of the Yield Curve. However, central banks (like the Fed or ECB) define their policy rate using an idealized overnight risk-free dynamic, whereas the physical market trades in complex, credit-embedded, 3-month term derivatives. To perfectly align market rates back downward into pure central bank policy expectations, quants must execute a granular extraction methodology that strips away liquidity artifacts (Turn Premia), counterparty spread differentials (Credit Basis), and the massive distortion of the Term Risk Premium.

## Mechanism

### 1. The Synthetic Overnight Account Hierarchy
The base algorithm to extract the policy path is to model the compounded value of a theoretical "rolling overnight deposit."
$$ \text{Policy Rate} \rightarrow \text{O/N Rate} \rightarrow \text{Compounded O/N Account} \rightarrow \text{Synthesized Term Rate} $$
The quantitative model constructs a path of anticipated discrete central bank moves (e.g., $+25$ bps), but strictly locks these potential moves mapping exclusively to the **exact calendar dates of official Central Bank policy meetings**. The algorithm solves for the exact "probabilities" of hikes/cuts on those specific meeting dates that cause the trailing Synthesized Term Rate geometry to perfectly match the currently observable OIS/Futures market price.

### 2. Scrubbing the Distortions
Before matching the synthetic path to the market price, the raw market data must be violently de-noised:
- **The Cash/Policy Basis:** If the Central Bank policy rate is mathematically a secured Repo rate (e.g., ECB MRO), but the curve is built using unsecured Euribor fixings, an explicit Credit Spread structurally pads the market rate. This spread must be subtracted.
- **The Turn Premium:** The artificial interest rate spike bridging December 31st due to regulatory balance-sheet snapshotting must be zeroed out.
- **Convexity Bias:** If utilizing exchange-traded futures to proxy forward rates, the mathematical margin-funding bleed ($-\frac{1}{2}\sigma^2t^2$) must be completely recalibrated.

### Boundaries / Conditions

### The Term Risk Premium Deception (Flat Curve Paradox)
The singular most vicious constraint in policy extraction is ignoring the **Term Risk Premium**. 
In standard environments, an investor demands mathematically *more* yield to lock their cash up in a 6-month bond compared to leaving it in a 1-night deposit, purely as compensation for forfeiting the optionality to react to sudden systemic shocks. Therefore, an inherently "normal" curve naturally slopes upward, even if Central Bank policy is totally static.

*The Paradox:* If a quantitative desk observes that the 1-year yield is absolutely *flat* to the overnight yield, an amateur assumes the market expects 0 rate cuts. A professional quant realizes that because the Term Risk Premium *should* have pushed the 1-year yield strictly higher, the fact that it is completely flat proves the market is actually pricing in explicit, aggressive **Rate Cuts** to inherently offset the natural upward structural slope. Disregarding the Term Premium completely breaks the extraction model.

## Evidence / Source Anchors

- Describing the sequential extraction pathway linking the discrete policy rate through the rolling overnight account to back-fit Term Rates: [[Fixed_Income_Alexander_During_Ch15.md#page=134]]
- Emphasizing that algorithm paths must rigorously match the defined meeting calendars of the Central Bank rather than smooth continuous functions: [[Fixed_Income_Alexander_During_Ch15.md#page=135]]
- The requirement to scrub the credit basis when comparing un-collateralized Libor swaps against collateralized policy targets: [[Fixed_Income_Alexander_During_Ch15.md#page=135]]
- Conclusively defining the Term Risk Premium as the compensation for explicitly surrendering duration reinvestment optionality, making a flat term structure a de-facto predictor of rate cuts: [[Fixed_Income_Alexander_During_Ch15.md#page=136]]

## Related

- [[Forward_Discount_Factor_No_Arbitrage_Math]] — the foundational mathematics constructing the term rates being reverse-engineered
- [[Money_Market_Futures_And_Convexity]] — detailing the margin bias that requires scrubbing before analysis
- [[Policy_Rate_Expectations_Extraction]]
- [[Expectations_Hypothesis_In_Yield_Curves]]
- [[Nelson_Siegel_Svensson_Curve_Models]]
- [[PCA_Yield_Curve_Decomposition]]
- [[Yield_Curve_Fitting_Optimization]]
- [[Yield_Curve_Model_Hedges]]
