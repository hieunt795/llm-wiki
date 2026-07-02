---
title: DeepDive — quasi-fiscal sterilization central bank
date: 2026-07-01
query: "quasi-fiscal sterilization central bank"
threshold: 2
wiki_hits: 8
thin_nodes: 3
raw_hits: 3
status: draft
---

# DeepDive: quasi-fiscal sterilization central bank

## STAGE 1 — Wiki Coverage

- ⚠ THIN `FX_Sterilization_Mechanism::wiki` conf=5
  - Issues: no source_refs section
  - Thesis: FX sterilization is the two-step process of neutralizing the impact of foreign
- ⚠ THIN `Offset_and_Sterilization_Dynamics::wiki` conf=5
  - Issues: no source_refs section
  - Thesis: Offset and sterilization coefficients measure the degree to which domestic
- ⚠ THIN `Fiscal_Dominance_Exit_Strategy::wiki` conf=3
  - Issues: no source_refs section
  - Thesis: Thoát khỏi Fiscal Dominance đòi hỏi sự phối hợp đồng thời giữa kỷ luật tài
- ✓ SOLID `Autonomous_Factors_In_Central_Bank_Balance_Sheet::Autonomous_Factors_In_Central_Bank_Balance_Sheet` conf=4
  - Thesis: Autonomous central bank balance sheet factors (banknotes, government deposits, foreign reserves, investment portfolios) reduce reserve availability for banking system and create sterilization demand.
- ✓ SOLID `Quasi_Fiscal_Operations::Quasi_Fiscal_Operations` conf=4
  - Thesis: Quasi-fiscal operations — financial transactions of central banks and public financial institutions that generate revenue or expenditure effects equivalent to explicit fiscal policy — distort conventi
- ✓ SOLID `Treasury_Central_Clearing_Repo_Netting::Treasury_Central_Clearing_Repo_Netting` conf=3
  - Thesis: Việc Fed KHÔNG central-clear các nghiệp vụ repo của mình tạo friction netting: dealer bank không thể net repo với Fed (SRF) chống lại reverse repo của khách, nên repo SRF nở bảng cân đối và đội vốn (e
- ✓ SOLID `Central_Bank_Swap_Lines::Central_Bank_Swap_Lines` conf=5
  - Thesis: Central Bank Swap Lines are standing or temporary facilities between central banks designed to provide foreign currency liquidity (primarily USD) to local financial systems during periods of market st
- ✓ SOLID `Central_Bank_Evolutionary_Episodes::Central_Bank_Evolutionary_Episodes` conf=5
  - Thesis: The history of central banking is categorized into three major episodes defined by the shifting priority between price stability, government financing, and financial system integrity, each ending with

## STAGE 2 — RAW Source Evidence

### RAW: Bindseil_Monetary_Policy_Operations::Central Bank Balance Sheet Expansion due to Intermediation Between Banks, Reflecting the Lender of Last Resort Function of the Central Bank
- file: `02_sources\books\bindseil_monetary_policy\Bindseil_Monetary_Policy_Operations.md`
- score: 0.030
- thesis: Central Bank Balance Sheet Expansion due to Intermediation Between Banks, Reflecting the Lender of Last Resort Function of the Central Bank
- heatmap context:
```
L56: | 1. Basic Terminology and Relationship to Monetary Macroeconomics | 1. Basic Terminology and Relationship to Monetary Macroeconomics                                  | 9    |
          L57: | 1.1                                                              | Key Concepts and Terminology                                                                      | 9    |
          L58: | 1.2                                                              | Dichotomy Between Monetary Macroeconomics and Monetary Policy Implementation in Normal Times      | 11   |
          L59: | 2. Representing Mone
```

### RAW: Bindseil_Monetary_Policy_Operations::2.6  LIQUIDITY DEFICIT OF THE BANKING SYSTEM VIS-À-VIS THE CENTRAL BANK
- file: `02_sources\books\bindseil_monetary_policy\Bindseil_Monetary_Policy_Operations.md`
- score: 0.030
- thesis: 2.6  LIQUIDITY DEFICIT OF THE BANKING SYSTEM VIS-À-VIS THE CENTRAL BANK
- heatmap context:
```
L56: | 1. Basic Terminology and Relationship to Monetary Macroeconomics | 1. Basic Terminology and Relationship to Monetary Macroeconomics                                  | 9    |
          L57: | 1.1                                                              | Key Concepts and Terminology                                                                      | 9    |
          L58: | 1.2                                                              | Dichotomy Between Monetary Macroeconomics and Monetary Policy Implementation in Normal Times      | 11   |
          L59: | 2. Representing Mone
```

### RAW: Lipschitz_Schadler_Macroeconomics::4 Countercyclical Policy and the Central Bank Balance Sheet in Practice
- file: `02_sources\books\lipschitz_schadler_macro\Lipschitz_Schadler_Macroeconomics.md`
- score: 0.030
- thesis: 4 Countercyclical Policy and the Central Bank Balance Sheet in Practice
- heatmap context:
```
L52: | 3                                                                              | 4                                                                      | Exercises . . . . . . . . . . .                                           | .     | .   | .   | . . | .           |        | . . | .          | . . .       | . .         | .     | . .    | 92    |     |     |
          L53: | 4                                                                              | Monetary Policy and Accounts                                           | .                                                          
```

## STAGE 3 — Expansion Proposal

> **Action required:** Review RAW evidence above, then:

- [ ] UPDATE `03_wiki/mechanisms/FX_Sterilization_Mechanism.md` — address: no source_refs section
      Add source_refs from RAW hits above
- [ ] UPDATE `03_wiki/mechanisms/Offset_and_Sterilization_Dynamics.md` — address: no source_refs section
      Add source_refs from RAW hits above
- [ ] UPDATE `03_wiki/mechanisms/Fiscal_Dominance_Exit_Strategy.md` — address: no source_refs section
      Add source_refs from RAW hits above

---
*Generated by deepdive_search.py v2.1 on 2026-07-01*