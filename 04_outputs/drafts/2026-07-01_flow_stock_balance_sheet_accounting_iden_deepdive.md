---
title: DeepDive — flow stock balance sheet accounting identity
date: 2026-07-01
query: "flow stock balance sheet accounting identity"
threshold: 2
wiki_hits: 8
thin_nodes: 3
raw_hits: 3
status: draft
---

# DeepDive: flow stock balance sheet accounting identity

## STAGE 1 — Wiki Coverage

- ⚠ THIN `System_of_National_Accounts_SNA::Balance Sheets` conf=4
  - Issues: no source_refs section
  - Thesis: The System of National Accounts (SNA) is an internationally standardized accounting framework that organizes a continuous flow of economic data — across production, income distribution, and asset accu
- ⚠ THIN `Flow_of_Funds_Framework::wiki` conf=4
  - Issues: no source_refs section
  - Thesis: The flow of funds account is a zero-sum matrix that integrates all four macroeconomic accounts (national income, BOP, GFS, monetary survey) into a single consistent framework by recording each sector'
- ⚠ THIN `Central_Bank_Balance_Sheet_Trilemma::Central_Bank_Balance_Sheet_Trilemma` conf=1
  - Issues: confidence=1 ≤ 2
  - Thesis: A central bank can simultaneously achieve only two of the following: (1) a small balance sheet, (2) low short-term rate volatility, and (3) limited intervention in money markets. / Một ngân hàng trung
- ✓ SOLID `External_Debt_Stocks_and_Flows::External_Debt_Stocks_and_Flows` conf=4
  - Thesis: The stock of gross external debt evolves as debt_t = debt_{t-1} + disbursements_t − amortization_t, but this baseline understates dynamics from valuation changes (multi-currency debt), interest capita
- ✓ SOLID `Balance_Sheet_Transmission_Channel::Balance_Sheet_Transmission_Channel` conf=5
  - Thesis: The balance sheet channel transmits monetary policy by influencing the net worth and collateral value of borrowers, which in turn alters the external finance premium and leads to a 'financial accelera
- ✓ SOLID `Macroeconomic_Accounting_Identities::Macroeconomic_Accounting_Identities` conf=?
  - Thesis: Macroeconomic_Accounting_Identities
- ✓ SOLID `Monetary_Survey_Banking_System_Structure::Monetary_Survey_Banking_System_Structure` conf=4
  - Thesis: The monetary survey — the consolidated balance sheet of the entire banking system — is built by consolidating the monetary authorities' balance sheet with the consolidated deposit money banks' balance
- ✓ SOLID `Capital_Flows_BOP_Macroeconomic_Impact::Capital_Flows_BOP_Macroeconomic_Impact` conf=4
  - Thesis: Capital inflows generate four macroeconomic policy challenges — reversibility risk, inflationary monetary expansion, real exchange rate appreciation, and consumption boom financing — and the standard 

## STAGE 2 — RAW Source Evidence

### RAW: Cargill_Financial_System_Policy::3.3  Sector Budgets, Income and Balance Sheets and the Fundamental Flow of Funds Equation
- file: `02_sources\books\cargill_central_bank_policy\Cargill_Financial_System_Policy.md`
- score: 0.033
- thesis: 3.3  Sector Budgets, Income and Balance Sheets and the Fundamental Flow of Funds Equation
- heatmap context:
```
L9: 
          L10: <!-- image -->
          L11: 
          L12: ## The Financial System, Financial Regulation and Central Bank Policy
          L13: 
      >>> L14: Traditional money and banking textbooks are long, expensive and full of so much institu­ tional and technical modeling detail that students can't  understand the big picture. Thomas F. Cargill presents a new alternative: a short, inexpensive book without the "bells and whis­ tles" that  teaches students the fundamentals in a clear, narrative form. In an engaging writing style, Cargill explains the three core components of money a
```

### RAW: Watts_Wray_Macroeconomics::6.4 Integrating NIPA, Stocks, Flows and the Flow of Funds Accounts
- file: `02_sources\books\watts_wray_mmt_macro\Watts_Wray_Macroeconomics.md`
- score: 0.032
- thesis: 6.4 Integrating NIPA, Stocks, Flows and the Flow of Funds Accounts
- heatmap context:
```
L17: 
          L18: Finally,  a  macro  textbook  that  rejects  neoclassical  microfoundations as  a  basis  for  understanding  how  capitalism  works.  The  authors replace  maximizing  individuals  with  social  classes  where  capitalist firms exercising differential power largely determine economic outcomes.
          L19: 
          L20: ## -Robert Chernomas , University of Manitoba, Canada
          L21: 
      >>> L22: The  most  progressive  macroeconomics  textbook  on  the  market. Organized around a balance sheet view, the authors carefully examine the most important issues of ou
```

### RAW: Watts_Wray_Macroeconomics::A stylised sectoral balance sheet
- file: `02_sources\books\watts_wray_mmt_macro\Watts_Wray_Macroeconomics.md`
- score: 0.032
- thesis: A stylised sectoral balance sheet
- heatmap context:
```
L17: 
          L18: Finally,  a  macro  textbook  that  rejects  neoclassical  microfoundations as  a  basis  for  understanding  how  capitalism  works.  The  authors replace  maximizing  individuals  with  social  classes  where  capitalist firms exercising differential power largely determine economic outcomes.
          L19: 
          L20: ## -Robert Chernomas , University of Manitoba, Canada
          L21: 
      >>> L22: The  most  progressive  macroeconomics  textbook  on  the  market. Organized around a balance sheet view, the authors carefully examine the most important issues of ou
```

## STAGE 3 — Expansion Proposal

> **Action required:** Review RAW evidence above, then:

- [ ] UPDATE `03_wiki\concepts\System_of_National_Accounts_SNA.md` — address: no source_refs section
      Add source_refs from RAW hits above
- [ ] UPDATE `03_wiki/concepts/Flow_of_Funds_Framework.md` — address: no source_refs section
      Add source_refs from RAW hits above
- [ ] UPDATE `03_wiki\mechanisms\Central_Bank_Balance_Sheet_Trilemma.md` — address: confidence=1 ≤ 2
      Add source_refs from RAW hits above

---
*Generated by deepdive_search.py v2.1 on 2026-07-01*