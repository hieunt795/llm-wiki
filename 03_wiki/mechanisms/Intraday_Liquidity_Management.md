---
title: Intraday Liquidity Management
aliases:
- Intraday Overdraft
- Daylight Overdraft
- Intraday Liquidity
type: mechanism
tags:
- payment-systems
- central-banking
- liquidity
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch04.md"
thesis: Transaction ordering within a single settlement day can convert an otherwise
  balanced position into an intraday overdraft or eliminate one entirely. Central
  banks must therefore choose between (a) providing intraday credit  absorbing the
  credit risk but enabling smooth settlement  or (b) prohibiting
source_refs:
- file: Fixed_Income_Alexander_During_Ch04.md
  page: 8
created: '2026-04-16'
updated: '2026-04-16'
---

## Thesis

Transaction ordering within a single settlement day can convert an otherwise balanced position into an intraday overdraft or eliminate one entirely. Central banks must therefore choose between (a) providing intraday credit  absorbing the credit risk but enabling smooth settlement  or (b) prohibiting overdrafts  forcing banks to hoard reserves and reorder payments  which can create payment gridlock.

## Mechanism

### The Ordering Problem

A bank's intraday liquidity balance is path-dependent: the sequence in which incoming and outgoing payments clear determines the *realised* minimum balance, not the net end-of-day position.

**Numerical example** (from source, Table 4.2):

| Time | Payment | Case A Balance | Case B Balance |
|---|---|---|---|
| 06:00 | Opening | 100 | 100 |
| 08:15 | +50 | 150 | 150 |
| 09:23 | ?200 | **?50** ? overdraft | *not sent yet* |
| 10:01 | +100 | 50 | 250 |
| 11:04 |  |  | 50 (?200 now sent) |
| 12:03 | +50 | 100 | 100 |
| 19:00 | Close | 100 | 100 |

**Conclusion:** End-of-day balance is identical but Case A requires an intraday overdraft at 09:23; Case B does not. Both participants have zero incentive to produce Case B voluntarily because delaying outgoing payments is individually rational.

### The Gridlock Incentive Problem

If participants can reorder payments to avoid overdrafts, they *will* delay outflows and accelerate inflows. Because one participant's inflow is another's outflow, this creates a Prisoner's Dilemma: universal delay ? payment gridlock. This is the structural rationale for central bank intraday credit.

### Design Responses

**Option A  Intraday credit (overdraft) permitted:**
- Central bank allows current accounts to go negative intraday
- Balances must be positive by end-of-day
- Credit risk borne by central bank
- Participation restricted to monetary policy counterparties (entities with standing access to central bank facilities)
- **Used by:** TARGET2 (ECB), BOJ-NET (Bank of Japan)

**Option B  No intraday overdraft:**
- Banks must hold sufficient pre-funded reserves to cover outgoing payments at any point in the day
- Incentivises larger precautionary cash holdings (substituting reserve holdings for overdrafts)
- Intraday liquidity provision effectively privatised (provided via repo in the private market)
- **Used by:** FedWire (US Federal Reserve)
- The Fed conducts daily open market operations, reducing the risk of aggregate shortfall; FedWire access stigma is therefore more likely to signal bank-specific rather than aggregate problems

**Hybrid  Intraday via private repo:**
- Banks hold excess reserves in overnight accounts and trade intraday liquidity in the private repo market
- This form of provision occurs *off* the central bank's balance sheet but creates dependency on private market functioning

### Monetary Policy Interaction

Intraday credit creates a *visible* extra liquidity demand when settled in overnight reserves (US model). In the euro area, TARGET2 overdrafts are *implicit*  they do not appear as overnight positions and therefore do not directly conflict with weekly MRO signalling. This is one reason why:
- TARGET2 (with intraday overdraft) + ECB's weekly tender framework = stable equilibrium
- FedWire (no intraday overdraft) + Fed's daily open market operations = stable but different equilibrium

Both are independently coherent designs; neither is universally superior.

### Boundaries / Conditions

- Applies strictly to **gross settlement systems** (RTGS). Net settlement systems (e.g., DNS) batch-net out most intraday flows, reducing the ordering problem.
- RTGS participation is restricted to institutions with central bank accounts (monetary policy counterparties, supervised banks). Smaller institutions access settlement indirectly via banks.
- End-of-day negative balances may be covered via emergency standing facilities but signal distress; central banks treat them as exceptions.

## Evidence / Source Anchors

- Table 4.2 in source: shows Case A vs Case B ordering with numerical example [[Fixed_Income_Alexander_During_Ch04.md#page=8]]
- ECB TARGET2 provides intraday overdrafts; Fed FedWire does not  observed as stable equilibria with respective operational frameworks [[Fixed_Income_Alexander_During_Ch04.md#page=9]]
- Banks substituting overdrafts with larger reserves increases visible cash demand, complicating policy signalling [[Fixed_Income_Alexander_During_Ch04.md#page=9]]

## Related

- [[Interbank_Netting]]  netting reduces gross flows, reducing the ordering problem
- [[RTGS_Systems_Global]]  global RTGS comparison table
- [[Symmetric_Interest_Rate_Corridor]]  the corridor framework within which overnight positions are managed
- [[Repurchase_Agreement_Mechanism]]  private intraday liquidity mechanism when overdrafts are unavailable
- [[Central_Bank]]  counterparty for overdraft provision
- [[Intraday_Credit_and_Liquidity_Gridlock]]
- [[Liquidity_Management_Corridor_System]]
