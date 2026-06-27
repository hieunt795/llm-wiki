---
title: Negative Interest Rate Mechanics
aliases:
- NIRP
- Negative Interest Rate Policy
- Breaking the Zero Lower Bound
- Lãi suất âm
- ZLB Breach
type: mechanism
tags:
- central-banking
- monetary-policy
- money-markets
- interest-rates
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch10.md
thesis: Negative Interest Rate Policy (NIRP) pushes nominal interest rates below zero,
  a maneuver enabled by the significant storage and transaction costs of physical
  cash which prevent it from being a perfect zero-rate floor.
source_refs:
- file: During_Fixed_Income_Ch10.md
  page: 73
- file: During_Fixed_Income_Ch10.md
  page: 74
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Before the 2008 financial crisis, the "Zero Lower Bound" (ZLB) was considered a hard limit for nominal interest rates, based on the assumption that rational agents would always prefer holding cash (yielding 0%) over negative-yielding deposits. NIRP shattered this academic consensus by demonstrating that cash has non-zero frictional costs, allowing central banks to charge a "tax" on reserves to force liquidity into the real economy. [[During_Fixed_Income_Ch10.md#page=73]]

## Mechanism: Why the ZLB is Not Absolute

The ability to push rates below zero rests on the **Storage and Transaction Costs of Cash**:
- **Storage:** Large-scale cash holdings require secure vaults, insurance, and specialized personnel.
- **Logistics:** Moving billions in physical currency involves armored transport and counting/verification delays.
- **The Result:** Central bank electronic deposits (current accounts) offer superior liquidity and safety. Institutions will accept a negative rate (typically down to -0.5% or -1.0%) for the convenience of electronic money before the cost of building physical vaults becomes economical. [[During_Fixed_Income_Ch10.md#page=74]]

## Systemic Implications

### 1. Multi-Currency Significance
In a globalized economy, a floor on domestic interest rates limits a central bank's ability to maintain relative accommodation. If a foreign central bank (e.g., the Fed) cuts rates but the domestic central bank (e.g., the BoJ) is stuck at 0%, the interest rate differential narrows, potentially causing an unwanted appreciation of the domestic currency. NIRP restores this room for maneuver. [[During_Fixed_Income_Ch10.md#page=74]]

### 2. Yield Curve Modeling
Standard yield curve models that assume rates cannot go negative systematically underestimate the probability of low-rate environments. NIRP forces models to assign probability mass to negative short rates, which mathematically results in **flatter predicted yield curves**. [[During_Fixed_Income_Ch10.md#page=74]]

### 3. Signaling Effects
While NIRP signals a central bank's willingness to use all available tools, it can also be self-defeating if perceived as a sign that standard ammunition is exhausted, potentially anchoring deflationary expectations.

## Case Study: The Japan "Shock" (2016)

The Bank of Japan introduced NIRP on January 29, 2016, with very little prior guidance.
- **The Shock:** Overnight uncollateralized interbank lending (Mutan) volumes plummeted by **75% in a single day**.
- **The Reason:** Bilateral lending became unattractive as both lenders and borrowers faced negative rates on their central bank accounts, eliminating the spread that justifies credit risk.
- **The Recovery:** It took approximately one year for market volumes to recover as participants adapted to a new **Tiered Deposit System** designed to mitigate the impact on bank profitability. [[During_Fixed_Income_Ch10.md#page=74]]

## Boundaries / Conditions: The Physical Lower Bound
NIRP is feasible only up to the point where the negative rate equals the cost of holding physical cash. Beyond this "Physical Lower Bound," massive cash hoarding would occur, potentially destabilizing the banking system. Furthermore, banks find it difficult to pass negative rates to retail depositors, which compresses their Net Interest Margin (NIM).

## Evidence / Source Anchors

- Refutation of the hard ZLB due to cash friction costs: [[During_Fixed_Income_Ch10.md#page=74]]
- Impact on yield curve models and flattening: [[During_Fixed_Income_Ch10.md#page=74]]
- Multi-currency arbitrage and relative accommodation logic: [[During_Fixed_Income_Ch10.md#page=74]]
- The 75% collapse of Japanese interbank volumes in 2016: [[During_Fixed_Income_Ch10.md#page=74]]

## Related

- [[Tiered_Deposit_System]] — Used to shield a portion of bank reserves from negative rates.
- [[Yield_Curve_Representations]] — The target of NIRP-driven flattening.
- [[Quantitative_Easing]] — Often used in conjunction with NIRP to stimulate the economy.
- [[Cash]] — The physical competitor to NIRP.
- [[Asymmetric_Lending_Corridor]] — The framework where the floor is pushed below zero.
