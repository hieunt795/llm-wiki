---
title: Direct Lending
aliases:
- Direct Lender
- Cash-Flow Lending
- Middle Market Lending
- One-Stop Lending
type: definition
tags:
- private-credit
- lending
- fixed-income
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: Direct lending is the dominant sub-asset class of private credit where a single
  non-bank lender or small club provides a floating-rate, senior secured, cash-flow
  loan to a mid-market company, bypassing syndicated markets entirely to offer speed
  and certainty of execution in return for an illiquidity premium.
source_refs:
- file: Deep Dive_ Private Credit.md
  page: 1
- file: BIS Quarterly Review, March 2025.pdf
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
---

## Thesis

Direct lending is the dominant sub-asset class of private credit where a single non-bank lender or small club provides a floating-rate, senior secured, cash-flow loan to a mid-market company, bypassing syndicated markets entirely to offer speed and certainty of execution in return for an illiquidity premium.

## Definition

Direct lending is the largest segment within [[Private_Credit]]. It involves a non-bank lender (or a small club of 1–5 lenders) providing financing directly to a borrower based on the company's enterprise value and cash-flow generation capacity (cash-flow lending).

Key structural characteristics include:
- **Floating-rate:** Typically priced at a base rate (e.g., SOFR) plus a wide credit spread.
- **Covenant-heavy:** Unlike modern syndicated loans which are increasingly covenant-lite, direct loans maintain robust financial maintenance covenants.
- **Capital structure position:** Usually senior secured, sitting at the top of the repayment waterfall.
- **Hold-to-maturity design:** Loans are originated to be held on the lender's balance sheet, explicitly lacking a secondary trading market.

The BIS taxonomy identifies direct lending as the predominant private credit strategy that has driven the sector's exponential growth over the past decade.

### Mechanism: The Unitranche Structure

The most defining innovation of modern direct lending is the **unitranche** loan.

> [!WARNING]
> A unitranche facility combines senior and subordinated debt into a single loan instrument with a blended interest rate. Behind the scenes, the lender often bifurcates the risk via an **Agreement Among Lenders (AAL)** into a "first-out" (lower risk, lower return) and "last-out" (higher risk, higher return) structure. Crucially, the AAL is **invisible to the borrower**. This creates significant opacity that can severely complicate restructuring efforts during a default, as the borrower must negotiate with a unified front that internally possesses conflicting economic incentives.

### Boundaries / Conditions

### Differentiating from Syndiated Loans and Mezzanine

| Feature | Direct Lending | Mezzanine | Syndicated Loan |
|---|---|---|---|
| **Seniority** | Senior secured (Unitranche) | Junior / Subordinated | Senior secured |
| **Lender Syndicate** | 1–5 entities (Club) | 1–3 entities | 50–100+ entities |
| **Covenants** | Maintenance covenants | Incurrence / Maintenance | Mostly Covenant-lite |
| **Secondary Market** | Virtually non-existent | Non-existent | Deep (driven by CLO buying) |
| **Coupon** | Floating (Cash) | Fixed / PIK | Floating (Cash) |

### The Value Proposition (Example)

A typical direct lending execution for a PE-sponsored middle market buyout:
- **Leverage:** 4.0x – 6.0x EBITDA
- **Pricing:** SOFR + 550bps to 650bps
- **Original Issue Discount (OID):** 98 to 99 (embedding a 1-2 point upfront fee)

While this translates to an an all-in cost of debt (10–11%) that is mathematically higher than issuing on the public High-Yield bond market, borrowers and Private Equity sponsors accept the premium for two absolute requirements: **speed and certainty of execution**. A direct loan can move from term sheet to closing in 4–5 weeks, avoiding the 8–16 week syndication process and the flex risk (the risk that the market rejects the pricing, forcing the underwriter to widen the spread to clear the book).

## Evidence / Source Anchors

- Direct lending defined and BIS taxonomy context: [[BIS Quarterly Review, March 2025.pdf#page=1]]
- Features: Floating rate, covenant-heavy, hold-to-maturity: [[Deep Dive_ Private Credit.md#page=1]]
- Unitranche and Agreement Among Lenders (AAL) hidden complexity: [[Deep Dive_ Private Credit.md#page=1]]
- Borrower preference for execution certainty over price: [[Deep Dive_ Private Credit.md#page=1]]

## Related

- [[Private_Credit]] — Market parent
- [[Debt_Seniority_And_Subordination]] — Relevance to capital structure placement
- [[Bond_Clauses_And_Covenants]] — Covenant maintenance context
- [[Payment_In_Kind_PIK]] — Feature sometimes embedded in stressed direct loans
- [[Private_Credit_Valuation_Mark_To_Model]] — How these held-to-maturity assets are priced
- [[NAV_Loans]] — PE fund-level financing that follows after Direct Lending deploys at company level.
- [[Private_Equity_Mechanism]] — PE sponsors are the primary demand driver (~70%) for Direct Lending.
