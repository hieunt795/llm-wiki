---
title: Bid-Ask Bounce Mechanism
aliases:
- Bid-Ask Bounce
- Artificial Volatility
- Transaction-induced Volatility
- Price Jumping
type: mechanism
tags:
- trading
- market-infrastructure
- liquidity
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch19.md
thesis: The bid-ask bounce is a phenomenon where the mere act of trading in an illiquid
  market generates artificial price volatility as observed prices jump between the
  bid and ask sides, even when the underlying economic mid-price remains static.
source_refs:
- file: During_Fixed_Income_Ch19.md
  page: 187
- file: During_Fixed_Income_Ch19.md
  page: 188
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Observed market volatility is composed of two distinct components: (1) news-driven changes in value and (2) liquidity-driven price jumping. Alexander Düring explains that the **Bid-Ask Bounce** occurs when a market is illiquid enough that the spread between buying and selling prices dominates the underlying signal. This effect creates a feedback loop of "phantom risk" that can trigger unnecessary stop-loss orders in algorithmic risk models. [[During_Fixed_Income_Ch19.md#page=187]]

## Mechanism: The Price Jump Paradox

In a standard model, the **Mid-Price** reflects the consensus economic value of an asset. However, trades only occur at the **Bid** (selling) or **Ask** (buying) prices.

1.  **The Process:** If an investor buys, the trade is recorded at the Ask. If the next investor sells, the trade is recorded at the Bid.
2.  **The Result:** To an observer (or a risk management system), the price appears to have "jumped" or "bounced."
3.  **Artificial Volatility:** If the bid-ask spread is wide, this bouncing generates a high statistical standard deviation in price history. The **Mid-Price** may have remained perfectly constant throughout, meaning there was zero economic change in value, but the "observed" volatility is high. [[During_Fixed_Income_Ch19.md#page=187-188]]

## Strategic Implications: The Risk Management Trap

### 1. The Volatility Feedback Loop
Risk management systems (like VaR models) use historical price moves to calibrate risk limits.
- **The Trap:** A widening bid-ask spread during a crisis causes more frequent bounces.
- **The Consequence:** The model interprets this liquidity friction as an increase in economic risk and forces portfolio managers to reduce positions. This selling further drains liquidity, widening the spread more and accelerating the "bounce." [[During_Fixed_Income_Ch19.md#page=188]]

### 2. Clearing the Market
In practice, there is no "true" mid-price known only to market makers. Instead, prices move to find a level where buying and selling interests are equalized. A transition from a buy-heavy to a sell-heavy market (e.g., during an index rebalancing) forces prices to "hop" across the mid-point, creating apparent volatility that is merely a transition between the ask and bid levels. [[During_Fixed_Income_Ch19.md#page=188]]

## Evidence / Source Anchors

- Definition of bid-ask bounce as artificial volatility in illiquid instruments: [[During_Fixed_Income_Ch19.md#page=187]]
- Analysis of how wide spreads can dominate underlying mid-price volatility: [[During_Fixed_Income_Ch19.md#page=188]]
- Discussion on news vs. structural factors (index rebalancing) driving the bounce: [[During_Fixed_Income_Ch19.md#page=188]]
- Visual schematic of the bid-ask bounce mechanism: [[During_Fixed_Income_Ch19.md#page=187]] (Figure 18.6)

## Related

- [[Market_Depth_Vs_Breadth]] — Breadth determines the size of the spread (and thus the bounce).
- [[Liquidity_Measurement_Taxonomy]] — Why pre-trade spreads are used to anticipate this effect.
- [[VaR_Shock_Mechanism]] — How bid-ask bounce can trigger systemic sell-offs.
- [[Information_Leakage_In_Trading]] — The risk that reveals the need for a bounce.
