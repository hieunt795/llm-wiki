---
title: "Collateral Constraints in Monetary Operations"
aliases: [Collateral Eligibility, Collateral Valuation, Haircuts, Borrowing Potential Constraint, Quantitative Collateral Limits]
type: mechanism
tags: [monetary-operations, collateral, liquidity]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "Collateral eligibility, valuation, haircuts, and quantitative limits jointly form the binding constraint on a bank's maximum borrowing from the central bank."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 22
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Collateral constraints directly limit borrowing potential of banks from central bank through four transmission channels: restricted eligibility, conservative valuation, haircuts, and quantitative limits.

## 1. Core Logic / Mechanism

[RAW] **Four-Channel Constraint Framework** (Bindseil p.22, sec 2.3):
1. **Restricted Eligibility**: Excludes non-liquid and non-transparent asset classes; sets minimum credit quality for collateral obligor
2. **Conservative Collateral Valuation**: Reduces risk of assuming too-high collateral values
3. **Haircuts** (h%): Caters for losses in value during liquidation period after counterparty default
4. **Quantitative Collateral Limits**: Addresses concentration and correlation risks

[RAW] **Maximum Borrowing Formula**:
$$B_{CB}^{max} = (1-h)(D + B - S_{CB})$$

Where:
- $B_{CB}$ = borrowing from central bank
- $h$ = haircut percentage
- $D$ = eligible collateral (loans to corporates)
- $B - S_{CB}$ = central bank credit facility

[LLM] **Transmission Mechanism**: When flow of liquidity shocks $(d-s)$ exceeds available collateral capacity $(1-h)D - h(B - S_{CB})$, banking sector hits collateral constraint → banks become illiquid and default unless CB extends collateral availability (haircut reduction) or lends against government guarantee.

## 2. Worked Example

[RAW] Assume bank balance sheet with:
- Loans to corporates: D
- Central bank credit available: B
- Haircut imposed by CB: h = 10%

Then: $B_{CB}^{max} = 0.9D$

If daily liquidity shocks (withdrawals net of deposits) total 15% of D, but haircut-adjusted collateral only provides 9% of D in equivalent borrowing capacity, bank must maintain precautionary reserves or access interbank market. If shock persists and interbank market dries up (crisis), collateral constraint becomes binding.

**Crisis Scenario**: Asset price decline reduces D valuation → effective haircut increases → borrowing capacity shrinks further → forced asset sales or default.

## 3. Failure Conditions / Boundaries

- **Collateral Scarcity Crisis**: When eligible collateral quantity becomes insufficient even at zero haircut (see [[Collateral_Scarcity_And_Effective_Term_Funding_Costs]])
- **Fire Sale Dynamics**: If bank attempts to liquidate ineligible collateral in stressed market, realized value << accounting value
- **Procyclicality**: Rising haircuts during downturns reduce borrowing capacity precisely when banks need it most
- **Counterparty Concentration**: If most eligible collateral issued by related entities, single-issuer stress cascades
- **Wrong-Way Risk**: Collateral value falls precisely when counterparty credit risk rises (e.g., domestic government bonds during sovereign crisis)

## Related
- [[Interest_Rate_Corridor_And_Standing_Facilities]]
- [[Central_Bank_Collateral_Frameworks]]
- [[Collateral_Haircut]]
- [[Liquidity_Management_Operations]]
- [[Collateral_Scarcity_And_Effective_Term_Funding_Costs]]
- [[Asset_Encumbrance_Problem]]
