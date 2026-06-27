---
title: DeepDive — repo market liquidity stress
date: 2026-05-04
query: "repo market liquidity stress"
threshold: 2
wiki_hits: 8
thin_nodes: 2
raw_hits: 3
status: draft
---

# DeepDive: repo market liquidity stress

## STAGE 1 — Wiki Coverage

- ⚠ THIN `Repo_Market_Crisis_Dynamics::wiki` conf=5
  - Issues: no source_refs section
  - Thesis: A 'Run on Repo' occurs when cash providers lose confidence in dealers or collateral
- ⚠ THIN `Liquidity_Reflexivity_in_Private_Credit::wiki` conf=5
  - Issues: no source_refs section
  - Thesis: Liquidity reflexivity occurs when redemption requests in semi-liquid vehicles
- ✓ SOLID `Repo_Market_Crisis_Dynamics::Repo_Market_Crisis_Dynamics` conf=5
  - Thesis: A 'Run on Repo' occurs when cash providers lose confidence in dealers or collateral value, leading to a sudden refusal to roll over short-term funding and a spike in haircuts, triggering systemic fire
- ✓ SOLID `Market_Depth_Vs_Breadth::Market_Depth_Vs_Breadth` conf=5
  - Thesis: The distinction between market breadth (microscopic) and depth (macroscopic) defines the market's resilience, differentiating between the ability to execute single isolated trades and the capacity to 
- ✓ SOLID `Repurchase_Agreement_Repo_Market_Structure::Repurchase_Agreement_Repo_Market_Structure` conf=5
  - Thesis: The repo market is the primary infrastructure for secured interbank lending, functioning as a dual-purpose machine for both cash management (General Collateral) and securities sourcing (Specials).
- ✓ SOLID `Market_Maker_Vs_Liquidity_Provider::Market_Maker_Vs_Liquidity_Provider` conf=5
  - Thesis: While often used interchangeably, market making is a formal, advertised role of providing two-way quotes, whereas liquidity provision is a more general willingness to trade that may disappear in times
- ✓ SOLID `Market_Maker_of_First_Resort::Market_Maker_of_First_Resort` conf=5
  - Thesis: The 'Market Maker of First Resort' is an expanded central bank role where it ensures the continuous functioning of financial market infrastructure and plumbing during systemic shocks, preventing liqui
- ✓ SOLID `Central_Bank_Swap_Lines::Central_Bank_Swap_Lines` conf=5
  - Thesis: Central Bank Swap Lines are standing or temporary facilities between central banks designed to provide foreign currency liquidity (primarily USD) to local financial systems during periods of market st

## STAGE 2 — RAW Source Evidence

### RAW: Elkenbracht_Huizing_Handbook_ALM::LIQUIDITY STRESS TESTING
- file: `02_sources\books\elkenbracht_huizing_alm\Elkenbracht_Huizing_Handbook_ALM.md`
- score: 0.0
- thesis: LIQUIDITY STRESS TESTING
- heatmap context:
```
L15: 
          L16: ## The Handbook of ALM in Banking
          L17: 
          L18: Second Edition
          L19: 
      >>> L20: Managing New Challenges for Interest Rates, Liquidity and the Balance Sheet
          L21: 
          L22: Edited by Andreas Bohn and Marije Elkenbracht-Huizing Published by Risk Books Infopro Digital Haymarket House 28-29 Haymarket London SW1Y 4RX
          L23: 
          L24: <!-- image -->
          L25: 
      [... skip to next heatmap section ...]
          L2825: 
          L2826: A static replicating portfolio served as the benchmark with time buckets of s
```

### RAW: Elkenbracht_Huizing_Handbook_ALM::Use of repos in the money and capital markets
- file: `02_sources\books\elkenbracht_huizing_alm\Elkenbracht_Huizing_Handbook_ALM.md`
- score: 0.0
- thesis: Use of repos in the money and capital markets
- heatmap context:
```
L15: 
          L16: ## The Handbook of ALM in Banking
          L17: 
          L18: Second Edition
          L19: 
      >>> L20: Managing New Challenges for Interest Rates, Liquidity and the Balance Sheet
          L21: 
          L22: Edited by Andreas Bohn and Marije Elkenbracht-Huizing Published by Risk Books Infopro Digital Haymarket House 28-29 Haymarket London SW1Y 4RX
          L23: 
          L24: <!-- image -->
          L25: 
      [... skip to next heatmap section ...]
          L2825: 
          L2826: A static replicating portfolio served as the benchmark with time buckets of s
```

### RAW: Choudhry_Principles_of_Banking::Liquidity Risk Reporting
- file: `02_sources\books\choudhry_banking_fixed_income\Choudhry_Principles_of_Banking.md`
- score: 0.0
- thesis: Liquidity Risk Reporting
- heatmap context:
```
L57: 
          L58: -  Chris Blake
          L59: 
          L60: Senior Manager, Global Treasury, HSBC Group, London
          L61: 
      >>> L62: I have been involved in Banking and more specifically Treasury and Risk for over 37 years now and throughout this time have read many a publication pertaining to our profession. In my opinion, Professor Choudhry's The Principles of Banking is the singularly most complete reference book of its kind it has been my pleasure to read. From its opening introduction on the basics of banking, the reader is guided through capital, liquidity and ALM throug
```

## STAGE 3 — Expansion Proposal

> **Action required:** Review RAW evidence above, then:

- [ ] UPDATE `03_wiki/mechanisms/Repo_Market_Crisis_Dynamics.md` — address: no source_refs section
      Add source_refs from RAW hits above
- [ ] UPDATE `03_wiki/mechanisms/Liquidity_Reflexivity_in_Private_Credit.md` — address: no source_refs section
      Add source_refs from RAW hits above

---
*Generated by deepdive_search.py v2.0 on 2026-05-04*