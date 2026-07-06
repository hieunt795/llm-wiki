---
title: DeepDive — Fed balance sheet total assets duration ample reserves normalization
date: 2026-07-06
query: "Fed balance sheet total assets duration ample reserves normalization"
threshold: 2
wiki_hits: 8
thin_nodes: 1
raw_hits: 3
status: draft
---

# DeepDive: Fed balance sheet total assets duration ample reserves normalization

## STAGE 1 — Wiki Coverage

- ⚠ THIN `Central_Bank_Balance_Sheet_Trilemma::Central_Bank_Balance_Sheet_Trilemma` conf=1
  - Issues: confidence=1 ≤ 2
  - Thesis: A central bank can simultaneously achieve only two of the following: (1) a small balance sheet, (2) low short-term rate volatility, and (3) limited intervention in money markets. / Một ngân hàng trung
- ✓ SOLID `QE_Balance_Sheet_Mechanics::QE_Balance_Sheet_Mechanics` conf=5
  - Thesis: QE forces the commercial banking system to lengthen its aggregate balance sheet as it acts as an intermediary, substituting private assets with new central bank reserves while creating matching deposi
- ✓ SOLID `Supply_Driven_Vs_Demand_Driven_Reserves::Supply_Driven_Vs_Demand_Driven_Reserves` conf=4
  - Thesis: Hai cách đạt 'ample reserves'. SUPPLY-DRIVEN giữ cung reserves dư an toàn để ngân hàng không phải chạm facility Fed → lãi ổn định nhưng bảng cân đối lớn. DEMAND-DRIVEN giữ cung nhỏ hơn, chấp nhận biến
- ✓ SOLID `Payment_System_Floor_On_Fed_Balance_Sheet::Payment_System_Floor_On_Fed_Balance_Sheet` conf=?
  - Thesis: Payment_System_Floor_On_Fed_Balance_Sheet
- ✓ SOLID `Outright_Purchase_Programmes_And_Balance_Sheet_Expansion::Outright_Purchase_Programmes_And_Balance_Sheet_Expansion` conf=4
  - Thesis: Outright purchase programmes expand central bank balance sheet; they differ from credit operations (repos) in that CB retains assets permanently, creating monetary base expansion and signaling commitm
- ✓ SOLID `Fed_Deferred_Asset_2022_2026::Fed_Deferred_Asset_2022_2026` conf=3
  - Thesis: Khi Fed nâng lãi suất từ mid-2022, chi phí IORB trên reserves (~4–5% thả nổi) vượt thu nhập coupon từ danh mục QE-era (~2–3% cố định). Fed hạch toán khoản chênh lệch này là 'deferred asset' — lợi nhuậ
- ✓ SOLID `Balance_Sheet_Transmission_Channel::Balance_Sheet_Transmission_Channel` conf=5
  - Thesis: The balance sheet channel transmits monetary policy by influencing the net worth and collateral value of borrowers, which in turn alters the external finance premium and leads to a 'financial accelera
- ✓ SOLID `Monetary_Survey_Banking_System_Structure::Monetary_Survey_Banking_System_Structure` conf=4
  - Thesis: The monetary survey — the consolidated balance sheet of the entire banking system — is built by consolidating the monetary authorities' balance sheet with the consolidated deposit money banks' balance

## STAGE 2 — RAW Source Evidence

### RAW: Singh_Collateral_Financial_Plumbing::The Fed's Balance Sheet, RRP and Excess Reserves
- file: `02_sources\books\singh_collateral_plumbing\Singh_Collateral_Financial_Plumbing.md`
- score: 375.900
- thesis: The Fed's Balance Sheet, RRP and Excess Reserves
- heatmap context:
```
L31: 
          L32: Author(s): Manmohan Singh
          L33: 
          L34: Publisher: Risk Books/Incisive Media Published Date: October 2016 DOI: http://dx.doi.org/10.5089/9781782723172.071 ISBN: 9781782723172 Page: 230
          L35: 
      >>> L36: Collateral is one of the building blocks on which the financial markets are constructed. Used for a number of purposes-including trading with central counterparties (CCPs), secured funding with market counterparties and central banks, OTC derivatives margining and settlement--the role of effective collateral management in monetizing assets has 
```

### RAW: Cargill_Financial_System_Policy::Federal Reserve balance sheet
- file: `02_sources\books\cargill_central_bank_policy\Cargill_Financial_System_Policy.md`
- score: 333.484
- thesis: Federal Reserve balance sheet
- heatmap context:
```
L9: 
          L10: <!-- image -->
          L11: 
          L12: ## The Financial System, Financial Regulation and Central Bank Policy
          L13: 
      >>> L14: Traditional money and banking textbooks are long, expensive and full of so much institu­ tional and technical modeling detail that students can't  understand the big picture. Thomas F. Cargill presents a new alternative: a short, inexpensive book without the "bells and whis­ tles" that  teaches students the fundamentals in a clear, narrative form. In an engaging writing style, Cargill explains the three core components of money a
```

### RAW: Watts_Wray_Macroeconomics::An  example  of  a  bank's  credit  creation:  a  balance sheet analysis
- file: `02_sources\books\watts_wray_mmt_macro\Watts_Wray_Macroeconomics.md`
- score: 314.080
- thesis: An  example  of  a  bank's  credit  creation:  a  balance sheet analysis
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

- [ ] UPDATE `03_wiki\mechanisms\Central_Bank_Balance_Sheet_Trilemma.md` — address: confidence=1 ≤ 2
      Add source_refs from RAW hits above

---
*Generated by deepdive_search.py v2.1 on 2026-07-06*