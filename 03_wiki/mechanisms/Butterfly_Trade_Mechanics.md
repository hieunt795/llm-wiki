---
title: Butterfly Trade Mechanics
aliases:
- Butterfly Spread
- Bullet and Wings
- Equal-weighted Butterfly
- Maturity-weighted Butterfly
- Butterfly Convexity
type: mechanism
tags:
- trading-strategies
- yield-curves
- convexity
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch32.md
thesis: A butterfly trade is a three-legged curve strategy—comprising a central 'Bullet'
  and two surrounding 'Wings'—designed to isolate curvature risk (hump) by neutralizing
  exposure to both parallel level shifts and slope steepening/flattening.
source_refs:
- file: During_Fixed_Income_Ch32.md
  page: 353
- file: During_Fixed_Income_Ch32.md
  page: 354
- file: During_Fixed_Income_Ch32.md
  page: 358
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 4716-4740
  section: "Chapter 6.2.2: Exploiting short-end curve anomalies with butterfly spreads"
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 5117-5250
  section: "Chapter 6.4: Trading the Curvature of the Yield Curve (Butterfly Trade Mechanics)"
created: '2026-04-18'
updated: '2026-05-07'
---

## Thesis

The butterfly trade is the archetypal tool for relative value analysis. Alexander Düring explains that by combining a steepener and a flattener with equal risks but opposite signs, the trader "strips out" everything except the convexity of the curve. Because of the different quoting conventions between bond and swap markets, a trader must be extremely cautious about the sign and scale of the butterfly spread they are observing. [[During_Fixed_Income_Ch32.md#page=353]]

## Mechanism: Weighting and Neutrality

A standard duration-neutral butterfly requires two equations to solve for the notionals of the three legs:

### 1. The Standard Model (Equal-weighted)
- **Equation 1 (Level-Neutral):** $N_{\text{bullet}} PVBP_{\text{bullet}} = -(N_{\text{wing1}} PVBP_{\text{wing1}} + N_{\text{wing2}} PVBP_{\text{wing2}})$
- **Equation 2 (Slope-Neutral):** $N_{\text{wing1}} PVBP_{\text{wing1}} = N_{\text{wing2}} PVBP_{\text{wing2}}$
- **The Logic:** This ensures that a parallel yield move or a linear rotation around the bullet results in zero P&L. [[During_Fixed_Income_Ch32.md#page=353]]

### 2. The Regression Model (Maturity-weighted)
- **Assumption:** Curve movements are not perfectly parallel but relate to maturity distance.
- **Equation 2 (Maturity-adjusted):** $(m_{\text{bullet}} - m_{\text{wing1}}) N_{\text{wing1}} PVBP_{\text{wing1}} = (m_{\text{wing2}} - m_{\text{bullet}}) N_{\text{wing2}} PVBP_{\text{wing2}}$
- **The Result:** Places higher absolute weight on the wing that is geographically closer to the bullet on the maturity axis. [[During_Fixed_Income_Ch32.md#page=354]]

## Strategic Implications: The Convexity Link

Düring highlights that every duration-neutral butterfly with a **Short Bullet** position has **Positive Convexity**.
- **The Profit:** In a volatile market, re-hedging this trade after every outright yield shift should theoretically result in a positive P&L (the convexity premium).
- **The Carry:** Because this benefit exists, the market "charges" for it by keeping the bullet yield higher than the interpolated yield of the wings (Positive Butterfly Spread). This is the empirical link between curve convexity and interest rate volatility. [[During_Fixed_Income_Ch32.md#page=358]]

## The Quoting Trap

- **Bond Market:** Quoted as **$\text{Bullet Yield} - 0.5 \times (\text{Wing1} + \text{Wing2})$**.
- **Swap Market:** Quoted as **$(\text{Wing1} + \text{Wing2}) - 2 \times \text{Bullet Rate}$**.
- **Sign Error:** For the same rates, the bond butterfly spread is exactly half the numerical value and has the **opposite sign** of the swap butterfly spread. [[During_Fixed_Income_Ch32.md#page=353]]

## Evidence / Source Anchors

- Definition of the bullet and wings components: [[During_Fixed_Income_Ch32.md#page=353]]
- Derivation of the level-neutral and slope-neutral weighting equations: [[During_Fixed_Income_Ch32.md#page=353]]
- Analysis of maturity-weighted butterflies (Equation 31.6): [[During_Fixed_Income_Ch32.md#page=354]]
- Critical comparison of bond vs. swap market butterfly quoting conventions: [[During_Fixed_Income_Ch32.md#page=353]]
- Identification of the positive correlation between butterfly carry and implied volatility (Figure 31.14): [[During_Fixed_Income_Ch32.md#page=359]]

## Related

- [[Yield_Curve_Trading_Strategies]] — The taxonomy where butterflies are "Order 3".
- [[Bond_Risk_Modified_Duration_And_PVBP]] — The $PVBP$ inputs for the weights.
- [[Convexity_Bias_Mechanism]] — The economic driver of the butterfly pickup.
- [[PCA_Factor_Interpretation]] — Factor 3 (Curvature) is the target of this trade.
