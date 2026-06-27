---
title: "Reserve Requirements as Monetary Control Instruments"
aliases: [Minimum Reserve Requirements, Reserve Requirement Ratio, Cash Reserve Requirement, CRR, RRR]
type: mechanism
tags: [monetary-operations, reserve-requirements, monetary-control]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "Reserve requirements create a structural demand for bank deposits at central bank; they serve three functions: monetary control, emergency liquidity cushion, and demand-dampening tool."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 96
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Reserve requirements mandate that banks hold minimum sight deposits with central bank, proportional to their liabilities; they create enduring liquidity need and enable monetary control through requirement adjustments.

## 1. Core Logic / Mechanism

[RAW] **Definition & Specification** (Bindseil p.96-97, secs 8.1-8.2):
"Reserve requirements oblige banks to hold a certain minimum level of sight deposits on their account with the central bank ('current accounts', 'reserves', and 'central bank liquidity' are used as synonyms for banks' sight deposits with central banks in monetary policy implementation jargon)."

**Typical Structure** (ECB example):
- Reserve Requirement = 1% × (Liabilities to non-banks with maturity < 2 years)
- Measured as average over one month (reserve maintenance period)
- Remuneration: At policy rate $i^*$ (not zero)

[LLM] **Core Transmission Mechanism**:
$$RR = r_{req} \times L$$

Where:
- $RR$ = Reserve requirement quantity
- $r_{req}$ = Reserve requirement ratio (ECB: 1%)
- $L$ = Reserve-eligible liabilities

**Consequence**: 
1. Banks MUST borrow from CB on average to meet $RR$
2. If aggregate system reserves < $RR$, banks must access:
   - Interbank market (to borrow from other banks' reserves)
   - CB standing facilities/OMOs (to inject liquidity)
3. This creates baseline demand for CB operations
4. CB can steer overnight rate by adjusting supply of liquidity relative to $RR$ demand

## 2. Key Functions (Three-Layer Model)

[RAW] **Function 1: Monetary Control** (p.99, sec 8.3)
- Reserve requirement creates structural demand for central bank money
- CB adjusts supply of OMO liquidity relative to demand → steers overnight rate
- Without RR, banking system could theoretically zero out overnight deposits (no need for CB intermediation)
- **Effect**: RR makes overnight rate steering feasible

[RAW] **Function 2: Demand Control** (p.99)
- Raising $r_{req}$ increases reserve demand → banks must cut credit to firms/households
- Lowering $r_{req}$ decreases reserve demand → banks have more lending capacity
- **Example**: ECB lowered $r_{req}$ from 2% to 1% (2012 crisis) → freed ~€100B of bank reserves for lending

[RAW] **Function 3: Safety Net** (p.99)
- Requirement to hold reserves = precautionary buffer against liquidity shocks
- In crisis, averaging period allows banks to use reserves; RR becomes implicit LOLR facility
- **Effect**: Reduces probability of bank default due to intraday gridlock

## 3. Worked Example

[LLM] **Scenario: Bank Managing Reserve Requirement**

**Month 1: Normal Conditions**
- Bank liabilities eligible for RR: €1 billion
- Required reserve: 1% × €1B = €10 million
- Daily operating reserve (above requirement): €5 million
- Total reserves held: €15 million
- Cost: Interest forgone (€15M held at 1% policy rate vs. invested at 2%)

**Day 1-15 (First Half of Month)**:
- Deposits flow in (payroll, sales): +€2M daily on average
- Bank accumulates reserve balance: €20 million (above requirement)
- Interbank rate: 1.05% (banks have surplus, lend to CB at deposit facility)

**Day 16-30 (Second Half)**:
- Deposits withdrawn (investments, loan repayments to customers): -€1.5M daily
- Bank reserve balance declines: €5 million (below requirement at day 20)
- **Bank must act**: Borrow from CB at 1.10% (standing facility) or reduce lending

**Day 25 (End of Period Check)**:
- Average reserves over 30 days: (€20M × 15 days + €5M × 15 days) / 30 = €12.5 million
- **Requirement met** (€12.5M ≥ €10M required)
- No penalty

**Alternative Scenario (No Averaging)**:
- Each day must satisfy €10M requirement
- On day 20, reserve = €5M < €10M → violation
- Bank forced to borrow €5M at higher emergency rate
- Overnight rate spikes on day 20 due to concentrated demand

## 4. Failure Conditions / Boundaries

- **Excess Reserves**: In QE regime, system-wide reserves far exceed RR requirement
  - RR loses relevance as monetary control tool
  - Banks can meet RR without accessing CB operations
  - CB must use OMOs for other reasons (balance sheet management, QE)

- **Zero Lower Bound**: RR remunerated at policy rate; at zero or negative rates
  - Holding reserves at 0% cost (no penalty vs. alternative use)
  - RR becomes binding only through averaging mechanism, not rate incentive

- **Money Market Dysfunction**: If interbank market freezes
  - Banks cannot transfer reserves from surplus to deficit banks
  - Each bank must access CB individually → reserve spread widens (bidding war)
  - Effective RR cost increases sharply

- **Collateral Constraint**: If banks hit collateral limits for OMO borrowing
  - Cannot borrow enough to meet RR
  - Default risk increases
  - CB may need to relax collateral eligibility or implement LOLR

## 5. Alternative Systems

[LLM] **Countries Without Reserve Requirements**:
- **UK** (abolished 2009): Floor system with overnight reverse repo facility instead
- **Canada** (abolished 1992): Uses OMO framework without RR

**Why keep RR?**:
- ECB/US Fed view: RR creates operational predictability
- Alternative: Pure corridor system (standing facilities only) + large OMOs
- Trade-off: RR lowers implementation cost; pure OMO system more flexible in crisis

## Related
- [[Interest_Rate_Corridor_And_Standing_Facilities]]
- [[Reserve_Averaging_And_Martingale_Property]]
- [[Liquidity_Management_Operations]]
- [[Open_Market_Operations_And_Instruments]]
- [[Central_Bank_Balance_Sheet_Structure]]
