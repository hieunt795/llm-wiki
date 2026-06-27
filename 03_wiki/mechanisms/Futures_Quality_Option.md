---
title: Futures Quality Option
aliases:
- Quality Option
- CTD Switch Option
- Delivery Option
- Option-Adjusted Basis
type: mechanism
tags:
- fixed-income
- derivatives
- trading
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch29.md
thesis: The quality option is an implicit right held by the short position in a physically-settled
  futures contract to deliver any bond from a defined basket, creating a positive
  value for the seller that keeps the futures price systematically below the forward
  price of the cheapest-to-deliver bond.
source_refs:
- file: During_Fixed_Income_Ch29.md
  page: 315
- file: During_Fixed_Income_Ch29.md
  page: 316
- file: During_Fixed_Income_Ch29.md
  page: 318
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

While simple arbitrage models assume the [[Cheapest_To_Deliver_CTD_Mechanism|CTD]] bond is known with certainty, in reality, the CTD can change as market yields move. Alexander Düring explains that the right to switch bonds is a valuable **Quality Option** for the seller (short). Because the seller will always choose the bond that is cheapest at the time of delivery, the futures contract is worth less than a pure forward on a single bond. This option value is why the CTD's net basis is almost always positive. [[During_Fixed_Income_Ch29.md#page=315]]

## Mechanism: The Asymmetry of Delivery

The quality option is essentially a "multi-asset" option. The short position is long a series of options on the relative value of all bonds in the basket.

### 1. Payoff Structure
- **When Yields Fall:** The CTD status tends to move towards shorter-duration bonds.
- **When Yields Rise:** The CTD status tends to move towards longer-duration bonds.
- **The Option Value:** At any yield level where a CTD switch is probable, the net basis of the individual bonds resembles an option payoff (Calls, Puts, or Straddles depending on duration). [[During_Fixed_Income_Ch29.md#page=316]]

### 2. Time Decay (Theta)
Like all options, the quality option loses value as it approaches the delivery date.
- **Far from Delivery:** High uncertainty about market levels means a high probability of a CTD switch. The option value is high.
- **Near Delivery:** As the delivery date approaches, the likely CTD becomes obvious. The probability of a switch drops, and the option value decays towards zero. [[During_Fixed_Income_Ch29.md#page=320]]

## Strategic Implications: Negative Convexity

Because the short position is *long* the quality option, the futures contract itself can exhibit **Negative Convexity**—the opposite of a normal bond.

- **The Drag:** In the yield area where a CTD switch is likely, the PVBP (duration) of the future may **rise when yields rise** and fall when yields fall.
- **The Hedge Cost:** A trader maintaining a PVBP-neutral hedge using futures must buy and sell as yields fluctuate, losing money on each adjustment. This "Convexity Drag" is exactly equal to the time-value of the quality option. [[During_Fixed_Income_Ch29.md#page=318-319]]

## Evidence / Source Anchors

- Definition of the quality option as the right to choose between basket bonds: [[During_Fixed_Income_Ch29.md#page=315]]
- Analysis of the net basis as the manifestation of the quality option premium: [[During_Fixed_Income_Ch29.md#page=316]]
- Mapping of net basis payoffs to standard option geometries (Figure 28.9): [[During_Fixed_Income_Ch29.md#page=316]]
- Explanation of the Negative Convexity drag on hedge performance: [[During_Fixed_Income_Ch29.md#page=318]]
- Visualization of the time decay of the quality option (Figure 28.13): [[During_Fixed_Income_Ch29.md#page=321]]

## Related

- [[Cheapest_To_Deliver_CTD]] — The anchor the option allows you to switch from.
- [[Bond_Futures_Contract_Design]] — The instrument that embeds this option.
- [[Negative_Convexity_In_MBS]] — A parallel phenomenon driven by borrower behavior.
- [[Present_Value_Of_A_Basis_Point]] — The sensitivity measure affected by the quality option.
