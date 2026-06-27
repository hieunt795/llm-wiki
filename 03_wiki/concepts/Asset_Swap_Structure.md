---
title: Asset Swap Structure
aliases:
- Asset swap
- Par-par swap
- Par-in-par-out structure
type: concept
tags:
- derivatives
- fixed-income
- synthetic-instruments
- swap-mechanics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: An asset swap combines a fixed-rate bond purchase with a "pay fixed" IRS, economically converting the bond to floating-rate exposure (LIBOR ± spread). The spread to LIBOR balances advantages from off-par bond purchase and off-market swap rates.
source_refs:
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 626-649
  section: Asset swaps
created: '2026-05-07'
updated: '2026-05-07'
---

## Thesis

An asset swap is an investment package: buy a fixed-rate bond + enter a "pay fixed" IRS. The par-par structure (paying 100% of par at purchase, receiving par at maturity) eliminates net interest-rate exposure by offsetting bond and swap fixed cash flows; residual LIBOR cash flows create economically equivalent floating-rate note.

---

## 1. Structure: Par-in-Par-Out (Par-Par)

### A. Two Components
[RAW-BOOK:5] An asset swap combines:
1. **Investor buys fixed-rate bond** at market price (may be par or off-par)
2. **Simultaneously enters "pay fixed" IRS** with fixed rate equal to the bond coupon

### B. Par-Par Mechanics
[RAW-BOOK:5] In par-par structures:
- Investor pays 100% of the bond's face value (par) at transaction start
- Investor holds bond to maturity
- Investor receives par from issuer at maturity
- Fixed coupon on bond and fixed rate on swap are equal and opposite

### C. Off-Par Advantages & Disadvantages
[RAW-BOOK:5] If bond market price ≠ par at purchase:
- **Bond trading below par:** Investor "overpays" (disadvantageous). Example: buying at 95 but only receives 100.
- **Bond trading above par:** Investor receives advantage. Example: buying at 120 but only pays 100 at maturity.

[RAW-BOOK:5] The second element is the swap's fixed rate. Since bond coupon and swap fixed rate rarely match exactly, this creates an advantage for one party. These imbalances are resolved through an up-front adjustment or via the LIBOR spread embedded in the swap.

---

## 2. Economic Transformation: FRN Synthetic

### A. Cash Flow Offset
[RAW-BOOK:5] Since:
- Fixed coupon on bond and fixed rate on swap are equal and opposite
- Both have the same maturity

**Result:** The fixed cash flows have no net economic impact. The investor is left with **LIBOR ± spread**, making the structure economically equivalent to a floating-rate note (FRN).

### B. Spread as Balancing Mechanism
[RAW-BOOK:5] The spread to LIBOR acts as a **balancing mechanism** to ensure any advantage or disadvantage incurred from:
- Paying/receiving par (off-par purchase)
- Entering into an off-market swap

is returned over the life of the deal, making the entire package an equitable exchange of cash flows.

---

## 3. Risk Profile: Credit > Interest Rate

### A. Interest Rate Exposure
[RAW-BOOK:5] **Interest rate risk is nearly hedged** through the bond-swap offset:
- If rates rise: Bond loses value, but "pay fixed" swap becomes more attractive (increases in value)
- If rates fall: Bond gains value, but "pay fixed" swap decreases in value
- **Result:** The two elements "more or less cancel each other out"

### B. Credit Exposure (Dominant)
[RAW-BOOK:5] **Credit risk dominates** because:
- If interest rates remain unchanged **but the issuer's creditworthiness deteriorates**, the bond loses value
- The swap provides no offsetting profit (swap payoff depends on rates, not credit)
- **Net result:** Overall loss

### C. Investor Motivations
[RAW-BOOK:5] Why enter asset swaps:
1. Reduce market (interest-rate) risk of holding fixed-rate bonds
2. Take a view on floating-rate credit spreads (FRNs expose investors to credit, not rate risk)
3. Create synthetic FRN exposure when corporate issuer has no floating-rate debt outstanding
4. Exploit fixed-rate bonds trading cheap to fair value → create attractively priced synthetic FRN
5. Cross-currency structures: e.g., buy USD fixed-rate bond, asset swap using currency swap (fixed USD/floating EUR)

---

## 4. Applications & Variants

[RAW-BOOK:5] Asset swaps can be structured in many ways beyond simple par-par. Details covered in deeper chapters address variations in pricing, settlement, and multilegge structures. Key insight: par-par provides a clean pedagogical example of economic equivalence between bond-swap packages and floating-rate instruments.

---

## Evidence / Source Anchors
- Par-par structure definition: [[Schofield_Trading_Fixed_Income_2011.md#page=626-628]]
- Off-par advantages/disadvantages and coupon matching: [[Schofield_Trading_Fixed_Income_2011.md#page=628]]
- Cash flow offset and LIBOR-spread equivalence to FRN: [[Schofield_Trading_Fixed_Income_2011.md#page=630]]
- Spread as balancing mechanism: [[Schofield_Trading_Fixed_Income_2011.md#page=632]]
- Interest rate vs. credit risk analysis: [[Schofield_Trading_Fixed_Income_2011.md#page=634-640]]
- Investor motivations (5 reasons): [[Schofield_Trading_Fixed_Income_2011.md#page=642-648]]

---

## Related
- [[Interest_Rate_Swap_IRS]]
- [[Floating_Rate_Note_FRN_Mechanics]]
- [[Currency_Swap_Mechanics]]
- [[Bond_Valuation_Risk_Decomposition]]
- [[Credit_Risk_Taxonomy]]
