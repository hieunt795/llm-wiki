---
title: Spread Taxonomy and Transmission
aliases:
- Spread Linkage
- Interest Rate Spreads
- Credit Spread Hierarchy
type: mechanism
tags:
- Spread
- Mechanism
- Pricing
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: '[WIKI] Spreads are the primary linguistic tool for quantifying relative value
  and risk compensation. Within a quant macro framework, they are not merely arithmetic
  differences but hierarchical measures of compensation for credit, liquidity, term,
  and volatility risks.'
source_refs: []
created: '2026-04-22'
updated: '2026-04-22'
---

# Spread Taxonomy and Transmission

## Thesis
[WIKI] Spreads are the primary linguistic tool for quantifying relative value and risk compensation. Within a quant macro framework, they are not merely arithmetic differences but hierarchical measures of compensation for credit, liquidity, term, and volatility risks.

## 1. Taxonomic Classification
The fixed income cosmos utilizes several spread metrics to "strip out" different risk components:

- **G-Spread (Government Spread):** The raw yield difference between a security and a government benchmark of similar maturity.
- **I-Spread (Interpolated Spread):** The difference between a security's yield and the interpolated swap rate. This links the bond to the [[OIS_And_Benchmark_Reform|Interbank funding market]].
- **Z-Spread (Zero-Volatility Spread):** A parallel shift applied to the entire spot curve that forces the bond's PV to equal its market price. It eliminates maturity mismatch noise found in G-spreads.
- **Option-Adjusted Spread (OAS):** The Z-spread minus the cost of embedded options (e.g., callability). This represents the "pure" credit and liquidity premium.
- **Asset Swap Spread (ASW):** The fixed spread over a floating reference (e.g., SOFR + Spread) that a dealer pays in a swap to receive the bond's coupons. This is the primary metric for [[Hedge_Based_Pricing_Anchor|relative value trading]].

## 2. Transmission Hierarchy (The Cascade)
[LLM] Risk transmission flows through spreads in a hierarchical structure. A shock in the risk-free rate (Level 1) propagates through funding costs and risk premia to reach the real economy.

[TRANSMISSION CASCADE]
  Risk-Free Rate (Policy) ──────> Swap Curve ─────────> Credit/Liquid Premia ──────> Real Rate
         |                          |                         |                        |
    [Duration]                [TED Spread]              [OAS / Z-Spread]          [Private Credit]

### Mechanism: The Feedback Loop
When spreads widen due to systemic risk:
1.  **Dealers Widening:** Market makers increase [[Bid_Ask_Bounce|Bid-Ask Spreads]] to compensate for increased inventory risk.
2.  **Margin Calls:** Wider spreads drop bond prices, triggering margin calls for leveraged holders.
3.  **Forced Selling:** Liquidation of assets further widens spreads, creating a self-reinforcing downward spiral.

## 3. Failure Conditions & Anomalies
- **Swap Spread Paradox:** In extreme crises, government yields can rise above swap rates (Negative Swap Spread) due to structural imbalances in the repo market or excessive hedging demand. [[During_Fixed_Income_Ch30]]
- **Spline Dispersion:** High [[Spline_Spread_Dispersion]] indicates that arbitrageurs are unable to trade against mispricings, signaling a total breakdown in market liquidity.

---
[[Z_Spread_Vs_OAS]] | [[TED_Spread_Mechanism]] | [[Asset_Swap_Spread_ASW]] | [[Credit_Risk_Taxonomy]]


## Related

- [[Forward_Volatility_Trading]]
- [[Liquidity_Measurement_Taxonomy]]
- [[Synthetics_Replicating_Portfolios]]
- [[Credit_View_Transmission_Channels]]
- [[Monetary_Policy_Transmission_Mechanism]]
- [[Money_Market_Instruments_Taxonomy]]
- [[Stone_Bhundia_Regime_Taxonomy]]
- [[Systemic_Risk_Taxonomy]]
- [[Z_Spread_Zero_Volatility_Spread]]
- [[Asset_Price_Transmission_Channel]]
- [[Balance_Sheet_Transmission_Channel]]
- [[Bank_Lending_and_Capital_Channels_Perry]]
- [[Basis_Swap_Spreads_Valuation]]
- [[Indonesia_ITF_Post_Adoption_Transmission]]
- [[Monetary_Policy_Transmission_Mechanism_MPTM_Indonesia_Edition]]
- [[Bank_Lending_Transmission_Channel]]
