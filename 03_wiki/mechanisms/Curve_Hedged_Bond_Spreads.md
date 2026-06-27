---
title: Curve-Hedged Bond Spreads
aliases:
- 4-leg Bond Spread
- Yield-Curve Neutral Bond Trade
- Bond-Future Overlay
type: mechanism
tags:
- trading-strategies
- risk-management
- yield-curves
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Chênh lệch trái phiếu phòng vệ đường cong (Curve-hedged bond spread) là một
  chiến lược đa chân phức tạp nhằm tách biệt sự định giá sai tương đối giữa hai trái
  phiếu bằng cách trung hòa rủi ro lãi suất định hướng và rủi ro độ dốc đường cong
  thông qua việc sử dụng các hợp đồng tương lai làm lớp phủ.
source_refs:
- file: During_Fixed_Income_Ch33.md
  page: 365
created: '2026-04-13'
updated: '2026-04-22'
---

## Thesis

Simple bond spreads (Long Bond A, Short Bond B) are exposed to overall yield curve movements if the bonds have different maturities. Alexander Düring explains that for large institutional positions, this residual curve risk is unacceptable. The solution is to use highly liquid **Futures** or **On-the-run Benchmarks** to "lock" the curve, ensuring the P&L is driven exclusively by the idiosyncratic relative value of the two bonds. [[During_Fixed_Income_Ch33.md#page=365-366]]

## Mechanism: The 4-Leg System

Consider a spread between a 3-Year bond (Bond 1) and a 4-Year bond (Bond 2), hedged with 2-Year (Future 1) and 5-Year (Future 2) futures.

### The 3-Equation Risk System
To determine the four notionals, the trader must satisfy three neutrality conditions:
1.  **Level Neutrality (Bond Leg):** $N_1 PVBP_1 = -N_2 PVBP_2$ (Standard spread weighting).
2.  **Level Neutrality (Future Leg):** $N_{F1} PVBP_{F1} = -N_{F2} PVBP_{F2}$ (The hedge itself must be duration-neutral).
3.  **Slope Neutrality:** $N_1 PVBP_1 = -N_{F1} PVBP_{F1}$ (The short-end bond risk must be matched by the short-end future risk). [[During_Fixed_Income_Ch33.md#page=366]]

### Strategic Result
This setup creates a synthetic "box":
- The Bond leg is long a 3Y-4Y steepener.
- The Future leg is long a 2Y-5Y flattener.
- **The P&L:** The trader only makes money if the 3Y-4Y sector of the curve steepens *relative* to the 2Y-5Y benchmark. This isolates the most granular level of relative value. [[During_Fixed_Income_Ch33.md#page=366]]

## Strategic Implications: Cross-Market Basis

Düring identifies a "basis risk" even in this sophisticated setup.
- **The Case:** Hedging Dutch government bonds with German Bund futures.
- **The Risk:** While duration and slope are hedged, the trade is still exposed to the **Dutch vs. German Spread**.
- **The Merit:** This residual spread risk is substantially lower than the outright curve risk, making the trade more "defensive" during periods of broad market volatility. [[During_Fixed_Income_Ch33.md#page=366]]

## Evidence / Source Anchors

- Rationale for hedging bond spreads with futures due to tighter bid-offer spreads: [[During_Fixed_Income_Ch33.md#page=366]]
- Mathematical derivation of the 3-equation system for a 4-legged trade: [[During_Fixed_Income_Ch33.md#page=366]]
- Identification of the risk from cross-sovereign spread mismatches (Dutch vs. German example): [[During_Fixed_Income_Ch33.md#page=366]]
- Schematic visualization of the curve-hedged bond spread (Figure 32.4): [[During_Fixed_Income_Ch33.md#page=366]]

## Related

- [[Steepener_And_Flattener_Trades]] — The basic building blocks of the hedge.
- [[Bond_Relative_Value_Valuation]] — The source of the bond spread idea.
- [[Basis_Trade_Mechanics]] — How futures and bonds interact at a 1-to-1 level.
- [[Principal_Component_Analysis_PCA]] — Factor 2 (Slope) is what this trade attempts to neutralize.
- [[Yield_Curve_Trading_Strategies]]
- [[PCA_Neutral_Butterfly_Weights]]
