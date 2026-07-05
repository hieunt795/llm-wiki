---
title: Monetary Multiplier (Geometric Series)
aliases:
- Monetary Multiplier
- Money Multiplier Formula
- High-Powered Money Expansion
type: mechanism
tags:
- macroeconomics
- banking
- math
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch05.md
thesis: The monetary multiplier is the theoretical limit to which an initial deposit
  of high-powered money (Outside Money) can be expanded into the total money supply
  (Inside Money) through the fractional reserve banking system.
source_refs:
- file: During_Fixed_Income_Ch05.md
  page: 32
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

The expansion of money is a cascading process where the "Leakage" at each step is the mandatory reserve held by banks. This creates a geometric series that converges to a fixed multiple of the original monetary base.

## Mechanism: The Mathematical Limit

Assuming a constant reserve ratio ($r$), the maximum total money ($M$) created from one unit of initial high-powered money is:
$$M = \sum_{k=1}^{\infty} \frac{1}{(1+r)^k} = \lim_{n \to \infty} \frac{1}{r} (1 - (1-r)^n) = \frac{1}{r}$$

### The Chain of Expansion
1. **Initial Deposit:** 10 gold coins.
2. **First Loan:** Bank keeps 10% reserve (1 coin), lends 9 coins.
3. **Second Deposit:** 9 coins are deposited back into the system.
4. **Second Loan:** Bank keeps 10% (0.9 coins), lends 8.1 coins.
5. **Final Result:** Total money = 100 coins (Multiplier = 10).

## Boundaries / Conditions

### 1. High-Powered Money
Coins, specie, or central bank reserves are known as **High-powered money** because an increase in these units leads to an $M$-fold increase in the total money in circulation.

### 2. Practical Relevance
Alexander Düring notes that in modern practice, the theoretical multiplier has limited relevance because:
- **Settlement Constraints:** Interbank payments must be settled in Outside Money, requiring banks to hold more than the legal minimum reserve.
- **Lender of Last Resort (LoLR):** The presence of a central bank pooling reserves reduces the "cost" of maintaining liquidity, altering the banks' incentive to expand credit to the theoretical limit.

## Evidence / Source Anchors

- Equation (4.3): Mathematical derivation of the multiplier: [[During_Fixed_Income_Ch05.md#page=32]]
- Definition of high-powered money: [[During_Fixed_Income_Ch05.md#page=32]]
- The role of LoLR in mitigating bank run risks: [[During_Fixed_Income_Ch05.md#page=33]]

## Related

- [[Inside_Vs_Outside_Money]] — The two types of money involved.
- [[Reserve_Requirement_GWM_Evolution]] — The variable $r$ in the formula.
- [[Bank_Money_Creation_Accounting]] — The micro-level step in the chain.
- [[Money_Multiplier_Formula]]
- [[Monetarist_Vs_Keynesian_Monetary_Views]]
- [[Monetary_Policy_Frameworks_Evolution]]
- [[Monetary_Policy_Strategic_Framework]]
- [[Monetary_Policy_Transmission_Mechanism]]
- [[Monetary_Policy_Trilemma]]
- [[Narrow_Banking_Concept]]
- [[Bank_Lending_Transmission_Channel]]
- [[Baseline_ITF_Macroeconomic_Model]]
- [[Financial_Procyclicality_Mechanism]]
- [[Fractional_Reserve_Banking_Mechanism]]
- [[Monetary_Financing]]
- [[Monetary_Policy_Transmission_Mechanism_MPTM]]
- [[OLG_Model_Monetary_Mechanics]]
- [[Quantity_Theory_Of_Money_MV_PY]]
- [[Reserve_Ratio_Constraint]]
- [[Monetary_Analysis_Transition_Economy_Issues]]
- [[Monetary_Survey_Banking_System_Structure]]
- [[Monetary_Survey_Identity]]
- [[Money_Multiplier_IMF_Framework]]
- [[Monetary_Base_Constraint_Specie]]
- [[Monetary_Policy_Pendulum]]
- [[Stiglitz_Monetary_Paradigm_Credit_Matters]]
- [[OLG_Model_Monetary_Analysis]]
