---
title: "Collateral Scarcity and Effective Term Funding Costs"
aliases: [Collateral Scarcity, Collateral Supply Shortage, Effective Funding Costs, Term Funding Cost Inflation, Repo Specialness]
type: mechanism
tags: [monetary-operations, collateral, liquidity-crisis]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "When eligible collateral becomes scarce (concentrated in few hands or encumbered), effective borrowing costs rise sharply even if policy rates fall; banks unable to obtain term funding face default risk."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 180
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Collateral scarcity breaks the transmission from policy rates to bank funding costs; even with CB policy rate at 1%, bank effective borrowing cost can spike to 4-6% if eligible collateral unavailable.

## 1. Core Logic / Mechanism

[RAW] **Scenario Definition** (Bindseil p.180, sec 12.1):
Collateral scarcity occurs when:
- Total eligible collateral outstanding < total CB borrowing demand
- Some banks cannot meet margin calls or rollover borrowing
- Haircuts increase (signaling scarcity)
- Interbank/term funding markets dry up (banks hoard collateral)

[RAW] **Mechanism of Cost Inflation**:

**Baseline Scenario (Normal Times)**:
- Bank borrows €100M at CB policy rate: 2.00%
- Haircut-adjusted cost: 2.00% + 0.15% (haircut cost) = 2.15% effective
- Bank can rollover daily or access term markets

**Collateral Scarcity Scenario**:
1. Asset prices fall (crisis shock) → haircuts increase to 20% from 10%
2. Haircut cost rises: 0.30% (from 0.15%)
3. CB policy rate: still 2.00%
4. **Bank's CB borrowing cost: 2.30% (forced into CB borrowing)**

5. But bank has €300M term funding maturities
6. Term repo market frozen (no one lending 3-month repo)
7. Bank attempts 3-month term loan in interbank market
8. Offered at LIBOR + 300 bps (spreads widened due to credit risk spike)
9. **Effective term funding cost: 2.00% + 3.00% = 5.00%**

10. Gap between CB rate (2.30%) and market rate (5.00%) = 270 bps
11. This gap reflects **collateral scarcity premium**

[LLM] **Algebraic Formulation** (Bindseil p.181-182):

Neutral CB credit rate = real rate of return on capital $r$ + expected inflation $\pi$:
$$i^*_{CB} = r + \pi$$

With collateral constraint:
$$i^*_{CB,\text{scarcity}} = (r + \pi) + \text{Haircut Markup} + \text{Scarcity Premium}$$

Where:
- **Haircut Markup** = implicit interest cost from collateral value haircut
- **Scarcity Premium** = additional cost when collateral becomes scarce relative to demand

**Empirical Magnitude**:
- Normal: Scarcity Premium ≈ 0 bps
- Moderate stress: Scarcity Premium ≈ 50-150 bps
- Severe crisis: Scarcity Premium ≈ 200-500+ bps

## 2. Worked Example

[LLM] **Lehman Collapse Scenario (September 2008)**

**Before (July 2008)**:
- Banks can repo government bonds at repo rate ≈ EONIA + 5 bps
- EONIA (ECB policy target): 4.2%
- GC (general collateral) repo rate: 4.25%
- Bank 3-month borrowing: LIBOR (4.5%) + 20 bps = 4.70% effective

**After (September 2008, Lehman failure)**:
- ABS market frozen; mortgage-backed securities unmarketable
- Flight to safety: only government bonds acceptable as collateral
- Government bond availability per bank drops 50% (capital requirements tighten)
- GC repo rate: EONIA - 10 bps (banks fear counterparty failure; deposit safety matters more than yield)
- But **Special collateral (specific government bonds)**: 1.50% (severe specialness)
- Term repo: unavailable (3-month roll = 300+ bps)

- Bank desperate for 3-month funding
- Option A: Roll overnight repo 90 times: 0.0% (today) × 5 days + ? (next week, unknown)
- **Outcome**: Rollover risk unbounded; bank defaults

- Option B: Access ECB Term Lending Facility
  - ECB rate: still 3.75% (cut from 4.25% but not faster)
  - Haircut on ABS: 40% (from 20%)
  - **Effective cost**: 3.75% + 0.40 × 3.75% / (1-0.40) ≈ 5.25%

[RAW] **Actual Empirical Evidence** (Bindseil citing September 2008 data):
- ECB Main Refinancing Operation (MRO) rate: 3.75%
- Term Funding Cost (3-month): 6.5%-7.5% (depending on bank and collateral)
- **Spread**: 275-375 bps (extraordinary)
- Pre-crisis spread: 20-40 bps

## 3. Failure Conditions / Boundaries

- **Encumbrance Risk**: If 80% of bank assets pledged as collateral, bank cannot generate new collateral for future needs → refinancing cliff
- **Counterparty Stigma**: Even with eligible collateral, if bank has high default risk, no one accepts collateral in interbank repo → forced to use expensive CB lending
- **Correlation Breakdowns**: In crisis, supposedly uncorrelated collateral (different sovereigns, corporates) all decline together → effective diversification disappears
- **Haircut Procyclicality**: Rising haircuts reduce collateral values available → feedback loop → asset fire sales
- **CB Firepower Limit**: If CB's balance sheet size constrains lending capacity, CB cannot absorb all collateral demand → effective scarcity persists despite CB policy rates at zero

## 4. Policy Response Mechanisms

[RAW] **ECB Actions in 2008-2009** (Bindseil p.180-188):
1. **Haircut Reduction**: Dropped haircuts on ABS from 20% to 10%
2. **Collateral Widening**: Added covered bonds, corporate bonds, national central bank claims
3. **Term Lending Expansion**: 12-month fixed-rate full allotment operations (unprecedented)
4. **Securities Lending**: Lent securities to banks to enable collateral transformation (see [[Collateral_Transformation_And_TSLF]])

**Result**: Scarcity premium compressed; term funding costs fell from 7% to 4-5% by Q1 2009

## 5. Counterfactual: Without Scarcity

[LLM] **Ideal World**:
- Collateral abundant; any bank can borrow against any asset
- Term funding cost ≈ CB policy rate + spread for bank credit risk
- Formula: $i_{\text{term}} = i^* + s_{\text{credit}}$
- Where $s_{\text{credit}}$ = 50-100 bps for normal bank credit risk

**Reality (Scarcity World)**:
- Collateral scarce; only pristine assets (government bonds) acceptable
- Term funding cost ≈ CB policy rate + credit risk spread + scarcity premium + liquidity premium
- Formula: $i_{\text{term}} = i^* + s_{\text{credit}} + s_{\text{scarcity}} + s_{\text{liquidity}}$
- Where $s_{\text{scarcity}}$ = 200-500 bps (dominates in crisis)

## Related
- [[Collateral_Constraints_In_Monetary_Operations]]
- [[Collateral_Framework_Logic_And_Implementation]]
- [[Asset_Encumbrance_Problem]]
- [[Collateral_Scarcity_Stigma_And_Overnight_Rate_Control]]
- [[Central_Bank_Collateral_Frameworks]]
- [[Liquidity_Management_Operations]]
