---
title: Money Multiplier Formula
aliases:
- Monetary Multiplier
- 1/r Formula
- High-Powered Money Expansion
type: mechanism
tags:
- macroeconomics
- banking
- monetary-policy
- mathematics
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch02.md"
thesis: The money multiplier formula represents the theoretical limit of private money
  creation (Inside Money) based on an initial stock of reserves (Outside Money) and
  a constant reserve ratio.
source_refs:
- file: Fixed_Income_Alexander_During_Ch02.md
  page: 32
- file: Fixed_Income_Alexander_During_Ch02.md
  page: 33
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

The economic importance of banking is not merely the safe storage of cash, but the **lending of deposits**. This process allows for a mathematical expansion of the total money supply beyond the physical stock of foundational assets. Alexander Düring highlights that while the **Money Multiplier** is the standard textbook model for this expansion, its practical relevance is severely limited by modern interbank settlement requirements.

## Mechanism

The multiplier effect occurs because a single unit of currency can serve as the "reserve" for multiple layers of credit.

### 1. The Iterative Process
Imagine 10 gold coins deposited in Bank A.
- **Step 1:** Bank A holds a 10% reserve (1 coin) and lends 9 coins.
- **Step 2:** The borrower spends the 9 coins. The seller deposits them in Bank B.
- **Step 3:** Bank B holds a 10% reserve (0.9 coins) and lends 8.1 coins.
- **The Loop:** This continues *ad infinitum* as every loan becomes a new deposit.

### 2. The Mathematical Limit
The maximum amount of money $M$ that can be based on an initial deposit of 1 unit with a reserve ratio of $r$ is the limit of a sum of a geometric series:

$$M = \lim_{n \to \infty} \sum_{k=0}^{n} (1-r)^k = \frac{1}{r}$$

- **High-Powered Money:** The initial coins are known as "high-powered money" because each unit leads to a $1/r$-fold increase in the total circulating supply.
- **Example:** With a 10% reserve ratio ($r=0.1$), the 10 initial coins can support a maximum of 100 units of total money. [[Fixed_Income_Alexander_During_Ch02.md#page=32]]

### Boundaries / Conditions

### 1. The Theoretical vs. Practical Reality
Alexander Düring notes that while the $1/r$ relationship is mathematically intact, its **practical relevance is low** for two reasons:
- **Outside Money Settlement:** Interbank payments usually cannot be settled in the private "Inside Money" issued by the banks themselves. They must be settled in **specie** or **central bank money**. This creates a constant "drain" on reserves that the multiplier formula ignores.
- **Fractional Reserve Pooling:** Modern systems use central repositories (like the Bank of England or the Fed) to pool reserves, allowing banks to survive runs with much lower total reserves than the multiplier would suggest is safe. [[Fixed_Income_Alexander_During_Ch02.md#page=33]]

### 2. The Bank Run Risk
No matter how large the reserve is (unless it is 100%), there is always a risk that more claims are presented for payment than the bank holds in liquid assets. This is the definition of a **Bank Run**.

## Evidence / Source Anchors

- Step-by-step example of the 10-coin expansion process: [[Fixed_Income_Alexander_During_Ch02.md#page=32]]
- Equation (4.3) and the $1/r$ derivation: [[Fixed_Income_Alexander_During_Ch02.md#page=32]]
- Definition of "high-powered money": [[Fixed_Income_Alexander_During_Ch02.md#page=32]]
- Critique of the multiplier's practical relevance: [[Fixed_Income_Alexander_During_Ch02.md#page=33]]
- Discussion on reserve pooling and the Bank of England's historical role: [[Fixed_Income_Alexander_During_Ch02.md#page=33]]

## Related

- [[Bank_Money_Creation]] — The accounting process that drives the multiplier.
- [[Reserve_Ratio_Constraint]] — The "r" variable in the formula.
- [[Inside_Vs_Outside_Money]] — The multiplier describes the ratio of Inside Money to Outside Money.
- [[Narrow_Banking_Concept]] — A proposal to force the multiplier to exactly 1 by mandating $r=1$.
- [[Lender_Of_Last_Resort]] — The entity that provides high-powered money when the multiplier process breaks down during a crisis.
- [[Quantity_Equation_Of_Money]] — The macroscopic formula where the result of the multiplier ($M$) is used.
