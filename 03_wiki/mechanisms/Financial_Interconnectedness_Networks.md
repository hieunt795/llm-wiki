---
title: "Financial Interconnectedness and Networks"
aliases: [Financial Networks, Systemic Interconnectedness, Network Contagion, Interconnectedness Risk]
type: mechanism
tags: [systemic-risk, interconnectedness, contagion, networks, macroprudential]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Perry Warjiyo"
provenance: "Perry Warjiyo Ch.14"
thesis: "Financial interconnectedness through interbank markets, payment systems, and wholesale funding creates contagion channels where default at one institution can trigger cascading failures via network effects and herding behavior."
source_refs:
  - file: "Perry Warjiyo Ch.14"
    page: 445-448
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Interconnectedness facilitates both risk-sharing and contagion; during crises, network topology amplifies shocks through multiple channels: direct counterparty exposure, common asset holdings, funding market fragility, and information contagion triggering herding.

## 1. Core Logic of Interconnectedness

[RAW] Per Perry Warjiyo (p.1780-1793):

"While a crisis can be triggered by default at one financial institution, the bursting of a bubble due to procyclical macrofinancial imbalances, or international or domestic economic shocks, the contagion process leading to a systemic crisis event throughout the entire financial system can progress with rapidity due to interconnectedness and financial networks in the markets and infrastructures, including the payment system."

The mechanism operates through five transmission channels:

1. **Direct Counterparty Exposure:** Bank A's default directly affects creditors (Bank B, hedge funds, corporates)
2. **Common Asset Holdings:** Fire sales by stressed banks depress prices for all holders
3. **Funding Market Contagion:** Default signal triggers deposit/wholesale withdrawal from similar institutions
4. **Payment System Cascades:** Settlement failures propagate through real-time gross settlement (RTGS) systems
5. **Information Contagion:** Herding behavior and panic amplify initial default

## 2. Network Topology and Contagion Speed

[RAW] Perry presents three network configurations (Figs 14.3-14.5):

### 2.1 Incomplete Network (Sparse Connectivity)
"In the case of an incomplete network, financial institutions have limited direct exposures to each other. Not all financial institutions are interconnected."

**Contagion property:** Default propagates slowly; network gaps limit cascade
**Risk:** Illusion of diversification; hidden bilateral exposure concentration

### 2.2 Disconnected Network (Clustered)
Financial institutions form separate communities with minimal cross-cluster links.

**Contagion property:** Within-cluster contagion rapid; cross-cluster spillover dependent on bridge institutions
**Risk:** Bridge defaults trigger bifurcated system collapse

### 2.3 Complete Network (Dense Connectivity)
"In the case of a complete network, all financial institutions are interconnected... every financial institution has direct exposure to every other financial institution."

**Contagion property:** Shock propagates immediately and evenly across system
**Risk:** Systemic shock becomes economy-wide default cascade

## 3. Interbank Market and Systemic Banking Crises

[RAW] Perry (p.1906-1910) emphasizes interbank money market role:

"Macroprudential policy is directed toward managing interconnectedness and financial networks, in particular through the interbank money market and financial infrastructures, to mitigate systemic risk. While default at one financial institution could trigger a crisis, along with macrofinancial procyclicality, or international or domestic economic shocks, a systemic crisis event throughout the financial system could propagate with rapidity due to interconnectedness and financial networks."

### Interbank Market Fragility Mechanism:
1. **Normal times:** Overnight interbank rate = policy rate + small spread
2. **Stress begins:** Information asymmetry → counterparty risk premium → spread widens
3. **Cascade:** Term funding dries up → short-term rollover risk → liquidity hoarding
4. **Breakdown:** Markets seize; interbank lending halts; institutions compete for deposits
5. **Systemic:** Liquidity-dependent institutions face illiquidity spirals regardless of solvency

## 4. Payment System as Contagion Channel

[RAW] Implicit in Perry's discussion, explicit in macro-financial linkage framework:

Payment systems (RTGS, ACH, CLS) create:
- **Temporal concentration risk:** Massive value flows during settlement windows
- **Gridlock risk:** Failure to settle (A→B→C→D) freezes entire chain
- **Liquidity multiplier:** Small actual liquidity → large notional settlement volume
- **Procyclicality:** Stressed institutions hoard liquidity; gridlock intensifies stress

## 5. Worked Example: 2008 GFC Contagion Sequence

[RAW] Implicit in Perry's narrative (p.1607-1618):

**Stage 1 (Aug 2007):** Subprime housing vulnerability discovered
- Mortgage-backed securities (MBS) lose transparency
- Asset prices fall; margins tighten
- Banks with MBS exposure face mark-to-market losses

**Stage 2 (Sep-Oct 2007):** Counterparty default fear
- Interbank lending freezes (TED spread explodes)
- Term funding markets (ABCP) collapse
- Asset-backed commercial paper (ABCP) vehicles need CB support

**Stage 3 (Sep 2008):** Network cascade
- Lehman Brothers default → counterparties lose $billions
- Counterparty credit risk premium spikes across system
- Trust in institutions evaporates
- Simultaneous fire sales across asset classes

**Stage 4 (Oct 2008-2009):** Information contagion
- Herding behavior triggers margin calls across hedge funds
- Corporate bond spreads widen; credit crunch
- Currency runs in emerging markets
- Deposit runs (Northern Rock, Greek banks)

## 6. Herding and Panic Amplification

[RAW] Per Perry (p.1795-1805):

"A crisis typically peaks when contagion through interconnectedness and financial networks are accompanied by herding behavior and information contagion. Panic on the markets and among depositors, or even financial institutions, due to herding behavior and information contagion would further compound a financial crisis, resulting in fire sales, inadequate liquidity, and financial market collapse."

Herding feedback loops:
- Early movers (sophisticated investors/prime brokers) exit first
- Remaining participants observe departures → rational fear → mass withdrawal
- Fire sales depress collateral values → margin calls on others
- Information asymmetry → assume worst → panic accelerates

## 7. Policy Implications

[RAW] Perry (p.1927-1948) and implicit in framework:

**Macroprudential tools for interconnectedness:**
1. **Higher capital for systemic institutions:** G-SIB (Global Systemically Important Banks) surcharges
2. **Liquidity requirements:** Liquidity Coverage Ratio (LCR), Net Stable Funding Ratio (NSFR)
3. **Counterparty exposure limits:** Large Exposure Frameworks restricting single-party concentration
4. **Payment system resilience:** Antecedent funding; tiered settlement; collateral optimization

**Central bank liquidity provision:** LOLR function essential for breaking contagion feedback loops

## 8. Boundary Conditions and Failure Modes

Network-based contagion fails to propagate when:
- Central bank aggressively provides liquidity (removes rollover risk)
- Capital buffers absorb losses without cascading losses to creditors
- Information asymmetry resolved (transparency → discrimination between weak/strong)
- Bankruptcy framework swift; failed institution resolution orderly (depositor confidence restored)

Network contagion accelerates when:
- Liquidity support insufficient or slow
- Capital buffers inadequate for shock magnitude
- Institutional opacity prevents good/bad discrimination
- Resolution tools (deposit insurance, bridge banks) weak or absent

## Related
- [[Financial_Procyclicality_Mechanism]]
- [[Bank_Run_Mechanics]]
- [[Asset_Fire_Sales_Mechanism]]
- [[Financial_System_Stability_FSS_Concept]]
- [[Lender_Of_Last_Resort_Mechanism]]
- [[Macroprudential_Policy_Definition]]
