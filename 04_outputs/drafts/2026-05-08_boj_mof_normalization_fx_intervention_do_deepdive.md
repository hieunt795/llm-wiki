---
title: DeepDive — BOJ MOF normalization FX intervention Double Kill mechanism
date: 2026-05-08
query: "BOJ MOF normalization FX intervention Double Kill mechanism"
threshold: 2
wiki_hits: 8
thin_nodes: 1
raw_hits: 3
status: draft
---

# DeepDive: BOJ MOF normalization FX intervention Double Kill mechanism

## STAGE 1 — Wiki Coverage

- ⚠ THIN `Foreign_Exchange_Sterilisation::wiki` conf=1
  - Issues: no source_refs section
  - Thesis: Because unilateral Foreign Exchange interventions to depress a domestic currency
- ✓ SOLID `FX_Sterilization_Mechanism::FX_Sterilization_Mechanism` conf=5
  - Thesis: FX sterilization is the two-step process of neutralizing the impact of foreign exchange interventions on the domestic money supply by exchanging liquid central bank liabilities (cash) for less liquid 
- ✓ SOLID `FX_Spot_Trading_Mechanics::FX_Spot_Trading_Mechanics` conf=5
  - Thesis: The mechanical operation of the spot foreign exchange market, involving two-way pricing (BOB), T+2 settlement conventions, and weighted-average position management to capture spread or speculate on vo
- ✓ SOLID `EM_Balance_Sheet_Crisis_Mechanism::EM_Balance_Sheet_Crisis_Mechanism` conf=5
  - Thesis: Rapid financial opening in emerging markets with weak regulation and currency pegs creates structural vulnerabilities: rising FX leverage, maturity mismatches, and collateral concentration that trigge
- ✓ SOLID `Order_Flow_Mechanism::Order_Flow_Mechanism` conf=5
  - Thesis: Market microstructure analysis shows that short-term exchange rate fluctuations are driven by order flows—the net of buy and sell orders—which transmit private information and reflect heterogeneous ex
- ✓ SOLID `Japan_FX_Intervention_MOF_BOJ_Framework::Japan_FX_Intervention_MOF_BOJ_Framework` conf=5
  - Thesis: Nhật Bản là trường hợp đặc biệt — quyền lực FX intervention nằm hoàn toàn ở Bộ Tài chính (MoF), không phải BOJ. BOJ chỉ hoạt động như đại lý thực thi theo lệnh MoF thông qua Foreign Exchange Fund Spec
- ✓ SOLID `Japan_FX_Intervention_Double_Kill_Mechanism::Japan_FX_Intervention_Double_Kill_Mechanism` conf=?
  - Thesis: Japan_FX_Intervention_Double_Kill_Mechanism
- ✓ SOLID `Japan_FX_Intervention_May_2026_Event::Japan_FX_Intervention_May_2026_Event` conf=4
  - Thesis: Japan's $34.5B (¥5.4T) FX intervention on May 1–3, 2026 was not a standard market-stabilization tool but a symptom of institutional credibility breakdown: the Takaichi administration forced a dovish B

## STAGE 2 — RAW Source Evidence

### RAW: Wystup_FX_Options::Wystup_FX_Options
- file: `02_sources\books\wystup_fx_options\Wystup_FX_Options.md`
- score: 0.033
- thesis: Wystup_FX_Options
- heatmap context:
```
L359: 225
          L360: 2.1.14
          L361: Auto-Renewal Forward
          L362: 227
          L363: 2.1.15
      >>> L364: Double Shark Forward
          L365: 228
          L366: 2.1.16
          L367: Forward Start Chooser Forward
          L368: 229
          L369: 2.1.17
      [... skip to next heatmap section ...]
          L11387: cate statically a double-no-touch paying one unit of domestic currency using two
          L11388: double-knock-out options.
          L11389: Static Replication of a FOR-Paying Double-No-Touch The nominal amounts of the respective
          L11390: doubl
```

### RAW: Duffie_BPEA_Payments_Liquidity_2026::VII.C Case illustration: Japan's Liquidity Savings Mechanism
- file: `02_sources\books\duffie_bpea_payments_2026\Duffie_BPEA_Payments_Liquidity_2026.md`
- score: 0.030
- thesis: VII.C Case illustration: Japan's Liquidity Savings Mechanism
- heatmap context:
```
L7: 
          L8: ## DARRELL DUFFIE Stanford University
          L9: 
          L10: ## The Payment System Puts a Floor on the Fed's Balance Sheet
          L11: 
      >>> L12: ABSTRACT The Fed is now growing its balance sheet roughly in step with the quantity of reserve balances needed by banks within each day to make timely payments to each other. Systemically important banks also demand large quantities of reserve balances to comply with liquidity regulations. If the Fed were to aim for a smaller balance sheet, subject to effective monetary policy implementation, the enabling policies co
```

### RAW: Perry Warjiyo and Solikin M. Juhro - Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-3::4.4.4. Exchange Rate Stabilization Policy: Foreign Exchange Intervention
- file: `02_sources\books\central_policy_Perry\Perry Warjiyo and Solikin M. Juhro - Central Bank Policy_ Theory and Practice-Emerald Publishing (2019)-trang-3.md`
- score: 0.030
- thesis: 4.4.4. Exchange Rate Stabilization Policy: Foreign Exchange Intervention
- heatmap context:
```
L197: 
          L198: The analysis explains the empirical fact of a correlation between money and real output as a short-term phenomenon because of imperfect information among economic agents due to unanticipated changes in money supply. Therefore, Neoclassical  economics  recommends  formulating  monetary  policy  based  on  rules rather than discretion, thus clarifying and providing assurance when anchoring economic expectations. According to this perspective, money neutrality requires monetary policy to focus on price stability, while real output must be driven by productivity gains and te
```

## STAGE 3 — Expansion Proposal

> **Action required:** Review RAW evidence above, then:

- [ ] UPDATE `03_wiki/mechanisms/Foreign_Exchange_Sterilisation.md` — address: no source_refs section
      Add source_refs from RAW hits above

---
*Generated by deepdive_search.py v2.1 on 2026-05-08*