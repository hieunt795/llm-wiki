---
title: Credit Default Swaps (CDS) — Schofield Contract Structure
aliases:
- CDS contract
- Single-name CDS
- CDS protection
type: concept
tags:
- derivatives
- credit-risk
- fixed-income
- settlement-mechanics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: A CDS is a bilateral contract where a protection buyer pays periodic premiums (or upfront points) to isolate pure credit risk of a reference entity. Market conventions and settlement methods (physical vs. auction-cash) determine valuation, with modern auction processes eliminating settlement price risk.
source_refs:
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 660-700
  section: Credit default swaps
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 5649-6333
  section: "Chapter 7: Credit Trading and Relative Value"
created: '2026-05-07'
updated: '2026-05-07'
---

## Thesis

A CDS isolates and transfers pure credit risk: the protection **buyer** pays periodic premiums to a **seller**, who agrees to indemnify upon a defined credit event. Spread reflects expected loss and default probability. Market conventions evolved from physical delivery (matched-position simplicity) to auction-cash settlement (reduces post-default price disputes).

---

## 1. Basic Mechanics: Buyer, Seller, Premium

### A. Bilateral Structure & Definitions
[RAW-BOOK:5] A credit default swap (CDS) is a bilateral contract allowing one entity to **buy protection** against the possibility that a **reference entity** (or basket of reference entities) will suffer a **specific credit event**.

**Protection Buyer:**
- Pays a fixed premium (spread) **periodically** (typically quarterly, some markets semi-annually)
- Upon credit event: receives full indemnity ("made whole") from protection seller

**Protection Seller:**
- Collects periodic premiums
- Upon credit event: pays compensation to protection buyer
- Compensation = agreed notional amount (adjusted for recovery expectations)

### B. Buyer & Seller Positioning
[RAW-BOOK:5] 
- **Protection buyer:** "Short the credit risk" — economically equivalent to selling the credit risky asset
- **Protection seller:** "Long the credit risk" — economically equivalent to buying a bond; accepts risk of credit event in exchange for regular cash flow (premium)
- **By convention:** Protection seller is often termed an "investor" due to economic equivalence to bondholder

### C. Premium Concept
[RAW-BOOK:5] The fee paid by the protection buyer is referred to as a **premium** or **spread**. In theory (credit fundamentals from Section 1.4), the spread magnitude is a function of:
- Expected loss upon default
- Probability of default

---

## 2. Quotation Methods: Par Spread vs. Points Upfront

### A. Investment Grade: Par Spread
[RAW-BOOK:5] For **investment-grade names**, CDS are quoted as a **par spread** — a reflection of the market's current perception of the reference entity's creditworthiness.

**Standard Coupons in Par Spread Markets:**
- USA: 100 and 500 basis points
- Europe: 25, 100, 500, and 1000 basis points

[RAW-BOOK:5] Once a trade is executed at par spread:
1. An **upfront adjustment** is paid or received if current market spread ≠ coupon
2. **All subsequent cash flows** are based on the **agreed fixed coupon** (not the market spread)

**Example:** Investment-grade name quoted at 100 bps par coupon, but market perceives true spread at 90 bps.
- Buyer of protection pays quarterly premium at 100 bps coupon
- Buyer is "locked in" to 10 bps above market
- **Buyer receives upfront cash adjustment** of 10 bps/annum, discounted for time value and default probability

### B. High-Yield: Points Upfront
[RAW-BOOK:5] For **high-yield names**, quotation is given in terms of **points upfront** rather than par spread.

**Mechanics:**
- Upfront points represent an initial cash payment
- Subsequent cash flows still executed on a **fixed coupon basis** (standard market coupon)
- **Market conversion methodology** exists to convert between par spreads and points upfront

---

## 3. Settlement Methods: Physical vs. Auction-Cash

### A. Physical Settlement (Historical)
[RAW-BOOK:5] Originally the market norm. Upon credit event:
1. **Protection seller:** Delivers agreed notional amount in cash to protection buyer
2. **Protection buyer:** Delivers an asset issued by the reference entity (conforming to contract terms)
   - Could be a defaulted asset or non-defaulted asset "pari passu" (equal rank)

**Advantage (matched positions):** Banks typically held **matched offsetting positions** (identical terms/conditions):
- Pay one side, receive identical offsetting side
- Upon credit event: no **price risk** on delivered obligation (exchange identical amounts, transfer asset title)
- Market value of delivered asset is irrelevant (notional amounts are fixed monetary values)

### B. Cash Settlement (Early Period Issues)
[RAW-BOOK:5] Initially **less popular** because:
- Bank with matched position faces **price risk** in early markets
- If credit event occurs and settlement legs don't coincide perfectly: 
  - No guarantee that delivered obligation value on one side = received obligation value on other side
  - Creates **settlement price mismatch risk**

### C. Auction Process (Modern Standard)
[RAW-BOOK:5] As the CDS market grew, **notional amounts outstripped supply of reference obligations**. Result:
- Protection **buyers** (not obligated to own actual bonds) encountered difficulties sourcing deliverable obligations post-default
- Solution: **Auction process** with panel of traders agrees on **post-default valuation** of deliverable obligations
- **Single agreed value** used by all market participants → eliminates price mismatch risk
- Shift from physical delivery to **cash settlement** based on auction price

---

## 4. CDS Contract Structure: Key Characteristics

### A. Reference Entity
[RAW-BOOK:5] **Critical requirement:** Two counterparties must agree on the **exact legal entity** on which protection is being bought or sold. Ambiguity can lead to disputes over which subsidiary, parent, or affiliated entity triggers protection.

### B. Reference Obligation
[RAW-BOOK:5] Deal confirmation specifies a **debt obligation** issued by the reference entity. This:
- **Identifies the credit risk** being transferred (which obligation in the capital structure?)
- Different obligations have **different credit risk** depending on recovery in default (senior vs. subordinated)
- **Typical market convention:** Senior unsecured debt
- **Alternative:** Subordinated or other components (to express different credit view)

**Importance:** Reference obligation pricing determines fair contract value and deliverable asset in case of physical settlement.

### C. Credit Events
[RAW-BOOK:5] Market participants agree on **market-standard events** triggering seller compensation:

1. **Bankruptcy:** Legal insolvency proceeding
2. **Restructuring:** Modification of debt terms (maturity extension, coupon reduction, etc.) — multiple variations exist
3. **Failure to pay:** Missed payment on obligation
4. **Obligation acceleration/default:** Creditor acceleration clause triggered
5. **Repudiation/moratorium:** Sovereign refusal to pay (for sovereign reference entities)

[RAW-BOOK:5] **Not all contracts include all terms.** Each market develops conventions:
- **USA:** Typically includes bankruptcy + failure to pay (no restructuring)
- **Europe & other markets:** Different conventions for restructuring inclusion

### D. Obligations (Triggering Concepts)
[RAW-BOOK:5] Once credit events are specified, counterparties agree on which **population of issuer obligations** can trigger a credit event:

- **Market standard:** "Borrowed money" (bonds, loans, CDs)
- **Varies by market** (differences in interpretation and scope)

### E. Deliverable Obligations
[RAW-BOOK:5] If credit event triggered and **physical settlement elected**:
- Protection seller delivers cash equal to agreed notional amount
- Protection buyer delivers **acceptable asset** issued by reference entity
- Asset need **not be the reference obligation** (supply constraints post-default)
- **Key criterion:** Asset must **not be subordinated to reference obligation** (would possess different credit risk)

---

## 5. CDS as Pure Credit Risk Benchmark

### A. Spread as Credit Benchmark
[RAW-BOOK:5] CDS spreads are viewed by market participants as representing the **"pure" credit risk** of a reference entity, distinct from bond yields (which embed interest-rate risk).

### B. Credit Curve Concept
[RAW-BOOK:5] CDS trade across many **different maturities**, even where:
- The reference entity has **no debt at equivalent maturity**
- Creates synthetic term structure of credit risk

Result: **Credit curve** — a representation of CDS spreads across different maturity tenors, analogous to yield curves for interest-rate risk.

### C. Cross-Market Linkage
[RAW-BOOK:5] CDS spreads are now used as **benchmark for pricing credit risk** in the **bond markets**. A widening CDS spread signals deteriorating credit view → bond yields widen; narrowing CDS spreads → bond yields tighten.

---

## Evidence / Source Anchors
- Basic CDS structure and buyer/seller roles: [[Schofield_Trading_Fixed_Income_2011.md#page=662]]
- Premium/spread relationship to expected loss and default probability: [[Schofield_Trading_Fixed_Income_2011.md#page=666]]
- Par spread mechanics (investment grade): [[Schofield_Trading_Fixed_Income_2011.md#page=666-672]]
- Points upfront quotation (high-yield): [[Schofield_Trading_Fixed_Income_2011.md#page=672]]
- Physical settlement and matched-position advantage: [[Schofield_Trading_Fixed_Income_2011.md#page=674-675]]
- Cash settlement price risk in early markets: [[Schofield_Trading_Fixed_Income_2011.md#page=676]]
- Auction process evolution and modern standard: [[Schofield_Trading_Fixed_Income_2011.md#page=678]]
- Reference entity definition (exact legal entity): [[Schofield_Trading_Fixed_Income_2011.md#page=682]]
- Reference obligation and credit risk hierarchy: [[Schofield_Trading_Fixed_Income_2011.md#page=684]]
- Credit events taxonomy (bankruptcy, restructuring, failure to pay, acceleration, repudiation): [[Schofield_Trading_Fixed_Income_2011.md#page=686-694]]
- Obligations vs. deliverable obligations distinction: [[Schofield_Trading_Fixed_Income_2011.md#page=696-698]]
- CDS spreads as pure credit benchmark and credit curves: [[Schofield_Trading_Fixed_Income_2011.md#page=700]]

---

## Related
- [[Credit_Default_Swaps_CDS]] — Complementary engineering decomposition (Risky Bond + LIBOR Loan - IRS synthesis)
- [[Credit_Risk_Taxonomy]]
- [[Bond_Relative_Value_Valuation]]
- [[Counterparty_Credit_Risk]]
- [[Credit_Derivatives_Market]]
- [[Interest_Rate_Swap_IRS]]
- [[Settlement_Risk_Herstatt_Risk]]
