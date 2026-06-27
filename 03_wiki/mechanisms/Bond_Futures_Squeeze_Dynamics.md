---
title: Bond Futures Squeeze Dynamics
aliases:
- Futures Squeeze
- Net Basis Squeeze
- Short Squeeze (Bonds)
- Delivery Failure Risk
- Ép giá tương lai
type: mechanism
tags:
- fixed-income
- derivatives
- market-manipulation
- liquidity
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch29.md
thesis: A bond futures squeeze is a market dislocation where a dominant participant
  establishes a long futures position that exceeds the available deliverable supply
  of the CTD bond, forcing shorts to deliver more expensive assets and driving the
  net basis into negative territory.
source_refs:
- file: During_Fixed_Income_Ch29.md
  page: 329
- file: During_Fixed_Income_Ch29.md
  page: 330
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The bond volume corresponding to the total open interest of a futures contract often exceeds the outstanding amount of the [[Cheapest_To_Deliver_CTD_Mechanism|CTD]] bond by several factors. Alexander Düring explains that while this mismatch is normally harmless (as most traders roll their positions), it creates a structural vulnerability for a **Squeeze**. By controlling both the long futures interest and the physical supply of the CTD (often via the repo market), an aggressor can "trap" the short positions, forcing them to settle at non-economic prices. [[During_Fixed_Income_Ch29.md#page=329]]

## Mechanism: The Squeeze Trap

### 1. Establishing Control
A trader establishes a massive long position in the front-month futures contract while simultaneously "buying up" the CTD bond supply.
- **The Repo Angle:** It is often cheaper to control the CTD supply via the **Repo Market** (borrowing all available bonds) than by outright purchase. If the shorts cannot borrow the CTD to deliver it, they are squeezed. [[During_Fixed_Income_Ch29.md#page=329]]

### 2. The Negative Net Basis Signal
In a normal market, the net basis is positive (reflecting the quality option).
- **The Signal:** A **Negative Net Basis** is the "smoking gun" of a squeeze. It means the futures contract is trading at a premium to the forward price of the cheapest bond.
- **The Implication:** Shorts would rather buy the next-cheapest bond (at a loss) or pay the squeeze trader a settlement fee than attempt to source the "trapped" CTD. [[During_Fixed_Income_Ch29.md#page=330]]

### 3. The IRR Capping
A squeeze also manifests in the **Implied Repo Rate (IRR)**.
- When a squeeze is imminent, the IRR of the CTD increases towards central bank or unsecured funding rates. This reflects the market's realization that funding the bond in the private specials market has become impossible. [[During_Fixed_Income_Ch29.md#page=330]]

## Strategic Implications: Inherent Instability

Düring identifies a "Free-rider Problem" that makes squeezes inherently unstable:
- **The Game:** If multiple traders collude to squeeze the market, the first one to "exit" and sell their long positions at the inflated price captures the largest profit. This incentive to defect often causes squeezes to collapse before the delivery window opens. [[During_Fixed_Income_Ch29.md#page=330]]

## Evidence / Source Anchors

- Analysis of the mismatch between open interest and CTD outstanding volume: [[During_Fixed_Income_Ch29.md#page=329]]
- Identification of the repo market as the primary tool for restricting CTD supply: [[During_Fixed_Income_Ch29.md#page=329]]
- Definition of Negative Net Basis as the market indicator of an expected squeeze: [[During_Fixed_Income_Ch29.md#page=330]]
- Description of the IRR approaching central bank rates as a floor for net basis: [[During_Fixed_Income_Ch29.md#page=330]]
- Discussion on the inherent instability of squeezes due to defection incentives: [[During_Fixed_Income_Ch29.md#page=330]]

## Related

- [[Cheapest_To_Deliver_CTD]] — The asset being squeezed.
- [[Futures_Basis_And_Implied_Repo_Rate]] — The metrics that signal the squeeze.
- [[General_Collateral_Vs_Special]] — Why the repo market is the battleground.
- [[Physical_Vs_Cash_Settlement_Debate]] — Why cash-settled futures are immune to this specific squeeze but vulnerable to others.
