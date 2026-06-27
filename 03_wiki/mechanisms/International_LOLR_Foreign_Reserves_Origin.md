---
title: "International LOLR and Foreign Reserves Origin"
aliases: [International Lender of Last Resort, Foreign Reserves Creation, Current Account Transactions, BOP Surplus, International LOLR, FX Reserve Accumulation]
type: mechanism
tags: [monetary-operations, lolr, international-finance]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "Foreign reserves originate from current account surpluses (exports > imports); in international LOLR, central bank provides foreign currency to domestic banks facing external funding stress."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 289
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
International LOLR function requires central bank to hold foreign currency reserves; reserves arise from trade surplus or FX intervention, then are lent to banks facing foreign currency funding drought.

## 1. Core Logic / Mechanism

[RAW] **Two-Country Model** (Bindseil p.289, sec 17, Annex A):

**Country A (Surplus Country)**:
- Exports > Imports (trade surplus)
- Domestic currency gets bid up
- Central Bank accumulates foreign currency reserves to stabilize exchange rate

**Country B (Deficit Country)**:
- Imports > Exports (trade deficit)
- Domestic currency gets bid down
- Banks need foreign currency to pay for imports; face funding gap

[RAW] **Foreign Reserves Origin** (Bindseil p.289, Annex A - detailed):

**Current Account Mechanism**:
```
Year 1: Trade Surplus (Goods)
- Country A exports €100M goods
- Country A imports €60M goods
- Trade surplus = €40M (foreign currency inflow)

Recording in Central Bank Balance Sheet:
Central Bank Assets:                Liabilities:
Foreign Currency Reserves: +€40M    Domestic Currency Issued: +€40M
[to sterilize capital inflow]

Effect on Money Supply:
- Unsterilized: Monetary base expands €40M (inflationary)
- Sterilized (typical): CB sells domestic securities = €40M → neutralizes inflation
```

**Accounting Diagram** (Bindseil financial accounts):
```
Domestic Country (A)
- Exporters: +€100M receivable (foreign currency)
- CB: +€100M foreign currency assets (balance sheet)
- Importers: -€60M payable (foreign currency)
- Net: +€40M foreign currency with CB

Foreign Country (B)
- Importers: -€100M payable (foreign currency)
- Foreign CB: -€100M reserves (paid to A's CB)
- Exporters: +€60M receivable (foreign currency)
- Net: -€40M foreign currency; must borrow from own CB
```

## 2. Three Scenarios for International LOLR

[RAW] **Scenario 1: Orderly Current Account Rebalancing**

Year 1 (Surplus):
- A accumulates €40M FX reserves
- B accumulates FX liabilities (owes foreign currency)
- Both manageable; trade slowly rebalances

Year 2-3:
- A's real wages rise (from export profits) → A's imports increase
- B's exports improve (from depreciation) → exports increase
- Trade gap narrows; reserve accumulation slows

[RAW] **Scenario 2: Sudden Stop (Capital Flow Reversal)**

Pre-Crisis:
- B is developing country; attracts foreign capital inflows (portfolio investment)
- B's currency strengthens; imports surge; trade deficit worsens
- CB reserves depleted (intervention to slow depreciation)

Crisis Trigger:
- Emerging market crisis elsewhere (Thailand, Russia)
- Foreign investors pull out of B
- Currency crashes; imports become expensive
- Domestic banks borrowed in foreign currency (foreign debt = €500M)
- Now need to repay but foreign currency unavailable

**International LOLR Role**:
- B's CB provides FX swap with IMF or central bank liquidity facility
- B's CB borrows US dollars, lends to domestic banks
- Banks can repay foreign borrowing
- Crisis contained (at cost of higher interest rates domestically)

**Example: Asian Financial Crisis 1997**:
- Thailand's CB reserves fell from $30B to $2B (July 1997)
- IMF provided $17B liquidity facility
- CB could then provide USD to domestic banks
- Banking system stabilized (after severe credit contraction)

[RAW] **Scenario 3: Negative Interest Rate on Foreign Reserves**

Post-GFC Period:
- Safe-haven flows into USD and CHF
- Emerging market CBs accumulate reserves (defensive)
- But reserve returns are negative (0% or negative US deposit rates)
- CB faces opportunity cost

**International LOLR Implication**:
- CB must sterilize reserve inflows (sell domestic securities) 
- Sterilization cost = domestic rate (3%) - foreign reserve rate (0%) = 3% annual cost
- For €100M reserves = €3M annual loss

[RAW] **Mechanics of FX Reserve Sterilization** (Bindseil financial accounts):

```
Central Bank Balance Sheet (Sterilization Mode)
Assets:                          Liabilities:
FX Reserves: €100M               Domestic Banknotes: €100M
[earning 0% from US Treasury]    [but CB pays 3% on bonds sold to public]

CB Must Do:
Sell domestic bonds €100M; get domestic currency
Use currency to pay interest on bonds (3%) = €3M cost
Interest income from FX reserves: €0M
Net cost: €3M per year

Alternative (No Sterilization):
- Leave FX reserves on balance sheet earning 0%
- But don't sell domestic bonds
- Domestic currency supply increases €100M (too inflationary)
- Central bank inflation target missed
```

## 3. Worked Example

[LLM] **Czech National Bank (CNB) FX Intervention, 2013**

**Context**: 
- ECB cuts rates to near-zero (2012-2013)
- Money floods into Czech koruna (safe-haven + interest rate differential)
- CNB rate = 0.05%, EUR rate = 0% → 5 bps differential attracts hot money

**CNB Response**:
- Currency appreciating too fast (koruna was 27 CZK/EUR, wanted 27.5)
- Decided: lower rates further OR intervene in FX market
- Chose: FX intervention (unconventional in developed market)

**Intervention Mechanics**:
1. CNB offers koruna for sale, buys EUR
   - Sells CZK 1,000B; buys EUR 35B
   - FX reserves increase: EUR 35B

2. Sterilization:
   - CNB repo CZK 1,000B back to banks (absorbs excess CZK)
   - Repo cost to CNB: 0.05% (policy rate)
   - Cost: CZK 500M annually (tiny)

3. Effect:
   - Koruna depreciated to 27.5 CZK/EUR (goal achieved)
   - FX reserves increased EUR 35B (for future crisis use)
   - Sterilization cost minimal (since policy rate already very low)

**International LOLR Benefit**:
- If future external shock occurs (foreign credit freeze), CNB has EUR 35B firepower
- Can provide FX to Czech banks avoiding forced depreciation
- Example: 2008 crisis, Czech banks short EUR 10-15B; CNB intervened successfully

## 4. Failure Conditions / Boundaries

- **Reserve Adequacy Paradox**: Building large reserves (for LOLR preparedness) attracts hot money inflows → currency appreciation → exports suffer
- **Sterilization Unwind Risk**: If CB holds too many FX reserves, must sterilize with high domestic rates → creates carry-trade incentive (borrow domestic, invest foreign) → reverses inflow dynamics
- **Confidence Threshold**: Once reserves fall below ~3 months of imports or €2-3B, market perceives shortage → sudden capital outflows accelerate → LOLR needed at worst time
- **Political Economy**: Large reserve holdings raise question "Why does CB hold foreign assets?" → suggests government deficits possible; triggers runs if confidence lost
- **Cross-Border Coordination Failure**: If multiple CBs need USD simultaneously, no central authority to allocate USD → scramble for collateral → spreads widen sharply

## 5. Formal Requirements for International LOLR

[RAW] **Bagehot's Principle** (adapted to international):
CB should lend freely at penalty rate against good collateral

**Applied Internationally**:
1. **Freely**: CB provides USD/EUR to domestic banks facing funding shortage
2. **At Penalty Rate**: 300+ bps above normal overnight rate (discourages moral hazard)
3. **Against Good Collateral**: Domestic assets (government bonds, corporate bonds, mortgages) with 30-50% haircut
4. **To Solvent Banks**: Not insolvent ones (must apply solvency test, not just liquidity test)

**Example: Fed Dollar Swap Lines (Post-2008)**:
- Fed committed to provide unlimited USD to BoE, ECB, SNB, BoJ, etc.
- Rate: 50 bps + OIS (index rate)
- Collateral: BoE/ECB/SNB/BoJ accept any domestic assets; repo to Fed
- Result: International LOLR fully activated 2008-2010; reduced substantially 2010-2012; reactivated 2020 (COVID)

## Related
- [[Lender_Of_Last_Resort_Mechanism]]
- [[Central_Bank_As_Lender_Of_Last_Resort_LOLR]]
- [[LOLR_Moral_Hazard_And_Liquidity_Regulation]]
- [[Foreign_Exchange_Sterilisation]]
- [[Capital_Flow_Management_CFM_Instruments]]
- [[Exogenous_Risk_LOLR]]
- [[Endogenous_Risk_LOLR]]
- [[Foreign_Capital_Flows_Determinants]]
- [[Eurobond_And_Foreign_Bonds]]
