---
title: TED Spread Mechanism
aliases:
- TED Spread
- Treasury-Eurodollar Spread
- Curve Shifting Spread
- Option-Adjusted Spread
- OAS
type: mechanism
tags:
- interbank-market
- central-banking
- yield-curves
- credit-risk
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch23.md
thesis: The TED spread (Treasury-Eurodollar) is a systemic risk indicator that measures
  the distance by which the Eurodollar curve must be shifted to reprice Treasury securities,
  effectively quantifying the premium for interbank unsecured risk relative to sovereign
  safety.
source_refs:
- file: During_Fixed_Income_Ch23.md
  page: 224
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Historically named after the 13-week T-bill contracts (T) and the 3-month Eurodollar contracts (ED), the **TED Spread** is fundamentally different from other spreads. While Z-spreads or ASW spreads adjust the bond's yield, the TED spread adjusts the **Discount Curve** itself. Alexander Düring explains that it measures the macro-economic "distance" between the risk-free rate and the unsecured interbank rate across the entire term structure. [[During_Fixed_Income_Ch23.md#page=224]]

## Mechanism: Curve Shifting

Unlike I-spreads which interpolate a single rate, calculating a TED spread involves a global curve modification:

1.  **Baseline Curve:** Start with a market model of implied forward rates (e.g., from Eurodollar/Euribor futures).
2.  **The Shift:** Shift the entire forward curve by a constant basis-point amount.
3.  **Reconstruction:** Rebuild the discount factor ($Df$) curve from these shifted forward rates.
4.  **Convergence:** The TED spread is the amount of shift required to perfectly reprice a given T-bond using this new curve. [[During_Fixed_Income_Ch23.md#page=224]]

## Strategic Implications: Non-US Market Limitations

The TED spread was originally designed for the highly liquid US Eurodollar market. Applying it to other markets (Eurozone, Japan) creates significant technical friction:
- **Liquidity Gaps:** Contracts equivalent to Eurodollars (Euribor on ICE, Euroyen on TFX) often lack liquidity beyond the immediate "red" or "green" years.
- **Model Reliance:** Because one cannot build a complete TED curve from futures alone, analysts must rely on market models to extrapolate forward rates into the illiquid far-end. This introduces model risk into the "objective" TED measure. [[During_Fixed_Income_Ch23.md#page=224]]

## Evidence / Source Anchors

- Historical origin of the TED acronym (Treasury-Eurodollar): [[During_Fixed_Income_Ch23.md#page=224]]
- Identification of TED as a curve-shifting spread rather than a yield adjustment: [[During_Fixed_Income_Ch23.md#page=224]]
- Description of the 4-step process for rebuilding the discount curve from shifted forwards: [[During_Fixed_Income_Ch23.md#page=224]]
- Analysis of the liquidity limitations of non-US Eurocurrency futures markets: [[During_Fixed_Income_Ch23.md#page=224]]

## Related

- [[Yield_Curve_Theoretical_Representations]] — The mathematical object that TED spread modifies.
- [[Money_Market_Futures_And_Convexity]] — The source of the Eurodollar (ED) inputs.
- [[LIBOR_Transition_And_Benchmarks]] — How the death of Libor/Eurodollars affects TED utility.
- [[Option_Adjusted_Spread_OAS]] — The broader category to which TED belongs.
