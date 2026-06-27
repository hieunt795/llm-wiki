---
title: RTGS Intraday Liquidity Mechanism
aliases:
- Intraday Overdrafts
- Transaction Reordering Deadlock
- TARGET2 vs FedWire
type: mechanism
tags:
- settlement
- central-banking
- liquidity-risk
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch04.md"
thesis: To ensure fluid operation of Real-Time Gross Settlement (RTGS) systems and
  prevent transaction-sequencing deadlocks, central banks structurally provide intraday
  overdrafts, acting as implicit intra-day liquidity bridges that smooth systemic
  flows without permanently inflating the overnight monetary base.
source_refs:
- file: Fixed_Income_Alexander_During_Ch04.md
  page: 26
created: '2026-04-16'
updated: '2026-04-16'
---

## Thesis

Real-Time Gross Settlement (RTGS) systems fundamentally eliminated the systemic contagion risk of delayed netting operations by settling transactions individually in un-alterable Central Bank money. However, requiring absolute positive funding for every gross transfer introduces severe gridlock risk based merely on transaction ordering. To solve this friction, central banks mathematically intervene by providing Intraday Overdrafts—functioning as structural intraday liquidity bridges that allow the payment pipeline to flow continuously without demanding that commercial banks hold punitively massive permanent cash reserves.

## Mechanism

In a pure RTGS system (e.g., FedWire, TARGET2), every interbank payment clears instantly on the balance sheet of the ultimate Central Bank. 

### The Transaction Sequencing Deadlock
Assume Bank A holds 100 in reserves. 
- At 9:00 AM, it must pay out 200.
- At 10:00 AM, it will receive 100 from an incoming flow.

Despite balancing absolutely flat (0 Net obligation) across the day, under strict pre-funding rules, Bank A’s 9:00 AM payment fails immediately. 

If every bank responds to this constraint by intentionally delaying outgoing payments until they receive their incoming flows, the entire global payment system seizes in a Mexican standoff (gridlock).

### Intraday Overdrafts
To break the deadlock, Central Banks (like the ECB via TARGET2) grant explicit permission for monetary policy counterparties to run negative balances (overdrafts) purely during the daylight operating hours of the system. 
By allowing Bank A to temporarily hit -100 at 9:00 AM, the flow naturally completes, and the incoming 100 at 10:00 AM returns the account to 0.

> [!WARNING]
> While intraday credit lubricates the system smoothly, it exposes the Central Bank to daylight default risk. The bank must clear the negative balance by the close of business. If a bank fails while overdrawn at 3:00 PM, the Central Bank crystallizes a loss. Therefore, access is restricted exclusively to vetted monetary policy counterparties, and drawings are often heavily collateralized.

### Boundaries / Conditions

### FedWire vs TARGET2 Philosophy
Different central banking frameworks manage this problem uniquely:
- **Zero Overdraft Focus:** Systems structured to penalize or disallow overdrafts aggressively force private commercial banks to hold massively elevated caches of permanent structural cash (substituting central bank daylight credit with private reserve hoarding).
- **Intraday Overdraft Focus (TARGET2):** By accommodating transactional demand implicitly during daylight, it prevents temporary transaction friction from muddying the broader signaling of the Central Bank's target benchmark interest rate operations.

## Evidence / Source Anchors

- The comparison of RTGS central architectures (FedWire, TARGET2, BOJ-NET, CHAPS): [[Fixed_Income_Alexander_During_Ch04.md#page=26]]
- The mathematical matrix proving transaction ordering triggers deadlock: [[Fixed_Income_Alexander_During_Ch04.md#page=27]]
- The operational friction of avoiding central bank intervention (hoarding reserves): [[Fixed_Income_Alexander_During_Ch04.md#page=28]]

## Related

- [[RTGS_Systems_Global]] — the umbrella framework capturing global architecture
- [[Central_Bank_Liquidity_Support_Programs]] — how banks resolve those overdrafts if they cannot clear them by 5 PM
- [[Interbank_Settlement_Mechanisms]] — the netting framework that RTGS explicitly replaced
