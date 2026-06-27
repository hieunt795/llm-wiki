---
title: DeepDive — BOJ normalization NIRP YCC exit MOF intervention 2026
date: 2026-05-07
query: "BOJ normalization NIRP YCC exit MOF intervention 2026"
threshold: 2
wiki_hits: 8
thin_nodes: 4
raw_hits: 3
status: draft
---

# DeepDive: BOJ normalization NIRP YCC exit MOF intervention 2026

## STAGE 1 — Wiki Coverage

- ⚠ THIN `FX_Sterilization_Mechanism::Case Study: Japan's MoF and Financing Bills` conf=5
  - Issues: no source_refs section
  - Thesis: FX sterilization is the two-step process of neutralizing the impact of foreign exchange interventions on the domestic money supply by exchanging liquid central bank liabilities (cash) for less liquid 
- ⚠ THIN `AOCI_Capital_Cliff::Cú sốc 2026 (The Re-proposal Impact)` conf=?
  - Issues: no source_refs section
  - Thesis: Cú sốc 2026 (The Re-proposal Impact)
- ⚠ THIN `Yield_to_Maturity_Calculation::Convexity in Price-Yield Curve` conf=?
  - Issues: no source_refs section
  - Thesis: Convexity in Price-Yield Curve
- ⚠ THIN `Yield_to_Maturity_YTM::wiki` conf=5
  - Issues: no source_refs section
  - Thesis: Yield to Maturity (YTM) is the internal rate of return (IRR) of a bond, representing the single discount rate that equates the present value of all future cash flows to the bond's current market price
- ✓ SOLID `Unconventional_Monetary_Policy_Taxonomy::Unconventional_Monetary_Policy_Taxonomy` conf=5
  - Thesis: Unconventional Monetary Policy (UMP) serves as a strategic extension of central banking when interest rates hit the Zero Lower Bound, utilizing balance sheet expansion and expectations management to r
- ✓ SOLID `BoJ_QE_2013_Case_Study::BoJ_QE_2013_Case_Study` conf=5
  - Thesis: Chương trình QE năm 2013 của Ngân hàng Trung ương Nhật Bản minh họa tầm quan trọng của kỹ thuật vận hành và truyền thông; lợi suất trái phiếu đã tăng ngược chiều kỳ vọng do ma sát trong quy mô vận hàn
- ✓ SOLID `2026-04-29_monetary_policy_synthesis::2026-04-29_monetary_policy_synthesis` conf=4
  - Thesis: Wisdom synthesis of 148 nodes tagged [monetary-policy]: top hubs Inflation_Targeting_Framework_ITF, Monetary_Policy_Transmission_Mechanism, Monetary_Policy_Strategic_Framework, 41 tension pairs identi
- ✓ SOLID `Japan_FX_Intervention_MOF_BOJ_Framework::Japan_FX_Intervention_MOF_BOJ_Framework` conf=5
  - Thesis: Nhật Bản là trường hợp đặc biệt — quyền lực FX intervention nằm hoàn toàn ở Bộ Tài chính (MoF), không phải BOJ. BOJ chỉ hoạt động như đại lý thực thi theo lệnh MoF thông qua Foreign Exchange Fund Spec

## STAGE 2 — RAW Source Evidence

### RAW: Tuckman_Serrat_Fixed_Income_2022::4.5 CONVEXITY
- file: `02_sources\books\tuckman_serrat_fixed_income\Tuckman_Serrat_Fixed_Income_2022.md`
- score: 0.033
- thesis: 4.5 CONVEXITY
- heatmap context:
```
L54: | CHAPTER 2                                                                  |      |
          L55: | Swap, Spot, and Forward Rates                                              | 65   |
          L56: | CHAPTER 3                                                                  |      |
          L57: | Returns, Yields, Spreads, and P&L Attribution                              | 79   |
          L58: | CHAPTER 4                                                                  |      |
      >>> L59: | DV01, Duration, and Convexity                                              | 103  |
    
```

### RAW: Tuckman_Serrat_Fixed_Income_2022::4.7 YIELD-BASED DV01, DURATION, AND CONVEXITY
- file: `02_sources\books\tuckman_serrat_fixed_income\Tuckman_Serrat_Fixed_Income_2022.md`
- score: 0.032
- thesis: 4.7 YIELD-BASED DV01, DURATION, AND CONVEXITY
- heatmap context:
```
L54: | CHAPTER 2                                                                  |      |
          L55: | Swap, Spot, and Forward Rates                                              | 65   |
          L56: | CHAPTER 3                                                                  |      |
          L57: | Returns, Yields, Spreads, and P&L Attribution                              | 79   |
          L58: | CHAPTER 4                                                                  |      |
      >>> L59: | DV01, Duration, and Convexity                                              | 103  |
    
```

### RAW: Fixed Income - Alexander During-10::9.2.3 Lessons from the initial BoJ quantitative easing
- file: `02_sources\books\fixed_income_during\Fixed Income - Alexander During-10.md`
- score: 0.029
- thesis: 9.2.3 Lessons from the initial BoJ quantitative easing
- heatmap context:
```
L141: 
          L142: Bank loans Banks lend under slightly less onerous conditions (albeit potentially at higher rates) than the public markets because they operate under less information asymmetry than bond investors and may have access to collateral. Purchasing bank loans would therefore be more stimulative for high-growth companies than the corporate bond market. Additionally, it would have a beneficial effect on bank equity via RWA reduction and potentially capital gains if banks have loans to sell at book value or above (banks are unlikely to sell loans below book value). However, a purc
```

## STAGE 3 — Expansion Proposal

> **Action required:** Review RAW evidence above, then:

- [ ] UPDATE `03_wiki\mechanisms\FX_Sterilization_Mechanism.md` — address: no source_refs section
      Add source_refs from RAW hits above
- [ ] UPDATE `03_wiki\mechanisms\AOCI_Capital_Cliff.md` — address: no source_refs section
      Add source_refs from RAW hits above
- [ ] UPDATE `03_wiki\mechanisms\Yield_to_Maturity_Calculation.md` — address: no source_refs section
      Add source_refs from RAW hits above
- [ ] UPDATE `03_wiki/mechanisms/Yield_to_Maturity_YTM.md` — address: no source_refs section
      Add source_refs from RAW hits above

---
*Generated by deepdive_search.py v2.1 on 2026-05-07*