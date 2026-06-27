---
title: Rediscounting
aliases:
- Bill Rediscounting
- Central Bank Discount Window
- Recourse Lending
type: mechanism
tags:
- central-banking
- history
- credit
- liquidity
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch08.md
thesis: Rediscounting is a foundational liquidity-providing mechanism where a central
  bank purchases short-term commercial bills from banks, providing immediate cash
  in exchange for an asset with dual-recourse protection.
source_refs:
- file: During_Fixed_Income_Ch08.md
  page: 51
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

While less prevalent in modern central banking than outright bond purchases, **Rediscounting** is the original tool through which central banks provided high-powered money to the system. It represents the point where commercial credit (bills between traders) is converted into central bank money. Alexander Düring explains that this mechanism provides the central bank with a passive but highly safe balance sheet expansion due to its unique legal recourse features. [[During_Fixed_Income_Ch08.md#page=51]]

## Mechanism

Rediscounting occurs when a commercial bank presents a bill it has already discounted (purchased from a trader) to the central bank for cash.

### 1. The Purchase of Debt
The central bank purchases the commercial bill outright. 
- **The Liquidity Effect:** Liquidity is injected into the general economy for the duration of the bill's life.
- **The Repayment:** When the bill matures and is paid to the central bank, the central bank's balance sheet shrinks (liquidity is pulled back).

### 2. Dual-Recourse Protection
The defining technical feature of rediscounting is the hierarchy of liability, making it an extremely safe asset for the central bank:
- **Primary Debtor:** The draftee of the bill (the original borrower/merchant).
- **Secondary Debtor:** The commercial bank that presented the bill.
- **Right of Redress:** If the draftee refuses payment at maturity, the central bank has a legal claim against the commercial bank. Thus, the central bank has recourse to **both** the bank it advanced cash to and the ultimate borrower. [[During_Fixed_Income_Ch08.md#page=51]]

### 3. Central Bank Passivity
Unlike OMOs, the central bank is passive in its rediscounting operations.
- ** Repayment Profile:** The central bank depends on the maturity dates of the bills for the repayment profile of its assets.
- **Control Limitation:** To target a specific volume of liquidity, the central bank would have to supplement this passivity with an active purchase strategy (like OMOs). [[During_Fixed_Income_Ch08.md#page=51]]

## Boundaries / Conditions: Historical Legacy
The practice of rediscounting bills explains modern terms such as the "Discount Window" at the United States Federal Reserve. Historically, banks would physically bring stacks of commercial paper to a central bank window to be rediscounted for cash. While still available, it has largely been superseded by repo operations in most jurisdictions. [[During_Fixed_Income_Ch08.md#page=51]]

## Evidence / Source Anchors

- Definition of rediscounting as purchasing previously discounted bills: [[During_Fixed_Income_Ch08.md#page=51]]
- Explanation of the right of redress and dual recourse to bank and borrower: [[During_Fixed_Income_Ch08.md#page=51]]
- Analysis of the passive nature of rediscounted liquidity: [[During_Fixed_Income_Ch08.md#page=51]]
- Link to the historical origin of the "Discount Window": [[During_Fixed_Income_Ch08.md#page=51]]

## Related

- [[Base_Money]] — The target variable created via rediscounting.
- [[Bills_Of_Exchange]] — The instrument being rediscounted.
- [[Open_Market_Operations]] — The "Active" alternative to "Passive" rediscounting.
- [[Repurchase_Agreement_Mechanism]] — The modern successor to rediscounting for collateralized lending.
- [[Lender_Of_Last_Resort]] — Historically, rediscounting was the primary tool for executing the LOLR function.
