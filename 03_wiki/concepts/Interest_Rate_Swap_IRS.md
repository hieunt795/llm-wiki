---
title: Interest Rate Swap (IRS)
aliases:
- IRS
- Fixed-for-floating swap
- Vanilla swap
type: concept
tags:
- derivatives
- interest-rate-risk
- fixed-income
- swap-mechanics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield | Tuckman & Serrat
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: An interest rate swap exchanges periodic cash flows—one fixed, one floating (LIBOR)—on a notional principal. Market conventions net cash flows when payment dates coincide, while bid-offer spreads reflect hedging costs and counterparty credit risk.
source_refs:
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 586-625
  section: 1.5.3 Swaps
created: '2026-05-07'
updated: '2026-05-07'
---

## Thesis

An IRS is a periodic exchange of fixed and floating (LIBOR-linked) cash flows on a notional amount. The structure eliminates actual principal exchange; instead, standardized conventions (semi-annual fixed vs. quarterly LIBOR in USD) set payment frequency. Where payment dates coincide, netting is market convention, eliminating unnecessary gross flows.

---

## 1. Mechanics: Vanilla Fixed-for-Floating Swap

### A. Notional vs. Cash Flows
[RAW-BOOK:5] The notional amount is a reference value only—it does not represent an actual cash flow. It determines the magnitude of cash flows subsequently exchanged. Swaps are typically long-term (maturities extending 30–50 years) despite frequent periodic exchanges (semi-annually or quarterly).

### B. Cash Flow Calculation: Worked Example (GBP £10M, 182-day period)
[RAW-BOOK:5] Given:
- Fixed rate: 5.00% (semi-annual)
- Floating rate: 4.50% LIBOR (semi-annual)
- Notional: £10M
- Day count: 182 days in the 6-month period

**Fixed cash flow:** £10M × 5.00% × (182/360) = £25,277.78

**Floating cash flow:** £10M × 4.50% × (182/360) = £22,750 (approximately)

**Net payment:** £24,931.51 in favour of the receiver of fixed.

[RAW-BOOK:5] **Market convention:** Where the two payment dates coincide, the cash flows are netted rather than exchanged gross.

### C. Swap Structure Variations
[RAW-BOOK:5] Although the "fixed/float" structure is vanilla, the OTC nature means:
- Payment frequencies can differ (e.g., semi-annual fixed vs. quarterly LIBOR is USD convention)
- All terms and conditions are negotiable
- Many variations exist beyond simple vanilla structures

---

## 2. Market Quotation & Dealer Conventions

### A. Bid-Offer Pricing
[RAW-BOOK:5] Swaps are quoted on a bid-offer basis. The quotation is given **in terms of the fixed rate**. Interpretation depends on perspective:
- **Bid price (Dealer's perspective):** Dealer is "long" the swap—buying a LIBOR stream, paying fixed at the bid rate
- **Offer price:** Dealer is "short" the swap—delivering a LIBOR stream, receiving fixed at the offer rate

[RAW-BOOK:5] A market user (institution requesting the quote) interprets the bid-offer in the opposite manner.

### B. LIBOR Cash Flow Assumption
[RAW-BOOK:5] **Key convention:** Since many investment banks run 'matched positions' (offsetting pay/receive positions), the LIBOR cash flows are assumed to cancel out. Only the fixed rate difference needs to be quoted.

### C. Alternative Convention: "Long" vs. "Short" Language
[RAW-BOOK:5] Some practitioners describe position direction differently:
- Some view the offer side (receiving fixed) as **long the market** (analogous to buying a bond), since the dealer receives a fixed coupon and finances at LIBOR.
- Others use opposite semantics.

[RAW-BOOK:5] **Best practice:** Use "pay fixed" and "receive fixed" to avoid costly confusion.

---

## 3. Dealing Margins: Liquidity & Credit Components

### A. Liquidity Charge
[RAW-BOOK:5] The cost of hedging interest rate risk when entering a single swap. If:
- Immediate offset is not possible, or
- The notional amount is very large (difficult to hedge in one transaction),

then the liquidity charge is larger.

### B. Credit Value Adjustment (CVA)
[RAW-BOOK:5] Reflects the risk of counterparty default:
- **Interbank & hedge fund clients with cash collateral:** Small credit charge
- **Lower-quality or less-liquid collateral:** Larger credit charge (but less than unsecured accounts)

[RAW-BOOK:5] The total dealing margin reflects the customer's liquidity profile and creditworthiness, not just prevailing interbank rates.

---

## 4. Link to Other Derivatives

[RAW-BOOK:5] A swap can be conceptualized as a **multi-period, cash-settled forward contract executed at a uniform fixed rate**. This relationship connects IRS to both floating-rate instruments (FRNs, when paired with bonds) and forwards.

---

## Evidence / Source Anchors
- Basic swap structure and notional amount definition: [[Schofield_Trading_Fixed_Income_2011.md#page=586]]
- Worked example (GBP payment calculation, netting): [[Schofield_Trading_Fixed_Income_2011.md#page=606]]
- Payment frequency conventions (USD: semi-annual fixed vs. quarterly LIBOR): [[Schofield_Trading_Fixed_Income_2011.md#page=590]]
- Bid-offer quotation and LIBOR cash flow assumption: [[Schofield_Trading_Fixed_Income_2011.md#page=608]]
- Dealer position semantics ("long" vs. "short" conventions): [[Schofield_Trading_Fixed_Income_2011.md#page=618-620]]
- Liquidity and credit components of dealing margins: [[Schofield_Trading_Fixed_Income_2011.md#page=622]]

---

## Related
- [[Asset_Swap_Structure]]
- [[Overnight_Index_Swap_OIS]]
- [[Fixed_Rate_Bond_Valuation]]
- [[LIBOR_Floating_Rate_Mechanics]]
- [[Counterparty_Credit_Risk]]
