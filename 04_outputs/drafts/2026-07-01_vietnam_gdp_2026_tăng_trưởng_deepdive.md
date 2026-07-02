---
title: DeepDive — Vietnam GDP 2026 tăng trưởng
date: 2026-07-01
query: "Vietnam GDP 2026 tăng trưởng"
threshold: 2
wiki_hits: 8
thin_nodes: 2
raw_hits: 3
status: draft
---

# DeepDive: Vietnam GDP 2026 tăng trưởng

## STAGE 1 — Wiki Coverage

- ⚠ THIN `Vietnam_Private_Credit_Outlook_2025::1. Động lực Tăng trưởng (Drivers)` conf=1
  - Issues: confidence=1 ≤ 2, no source_refs section
  - Thesis: Thị trường tín dụng Việt Nam năm 2025 đang đứng trước một bước ngoặt lớn, chuyển dịch từ sự phụ thuộc hoàn toàn vào hệ thống ngân hàng sang một cấu trúc đa dạng hơn với sự góp mặt của [[Private_Credit
- ⚠ THIN `NBFI_Surveillance_Priorities::NBFI_Surveillance_Priorities` conf=1
  - Issues: confidence=1 ≤ 2
  - Thesis: Trong báo cáo cuối năm 2024 và kế hoạch 2025, các cơ quan giám sát tài chính quốc tế (FSB, IMF, BCBS) đã chuyển trọng tâm từ việc quan sát sự tăng trưởng sang việc **giám sát rủi ro hệ thống** phát si
- ✓ SOLID `US_Treasury_Balance_Sheet_H1_2026::US_Treasury_Balance_Sheet_H1_2026` conf=4
  - Thesis: Tại tháng 5/2026, tổng nợ bruto của Mỹ đạt $39.16T với nợ khả thị ~$31.52T. Bills chiếm 21.44% — trên mức TBAC khuyến nghị 15-20%. WAM 70 tháng (5.83 năm). ACM term premium 10Y đã chuyển dương (+67-83
- ✓ SOLID `Circular_16_2021_Vietnam_Banking_Bond_Rules::Circular_16_2021_Vietnam_Banking_Bond_Rules` conf=5
  - Thesis: Thông tư 16/2021/TT-NHNN của Ngân hàng Nhà nước Việt Nam quy định các giới hạn an toàn đối với việc tổ chức tín dụng mua trái phiếu doanh nghiệp, đóng vai trò là cơ chế ngăn chặn tình trạng sử dụng vố
- ✓ SOLID `GDP_Three_Approaches::GDP_Three_Approaches` conf=4
  - Thesis: GDP can be measured equivalently via three approaches — production (sum of value added), income (sum of factor incomes plus taxes less subsidies), and expenditure (sum of final uses) — and the identit
- ✓ SOLID `Nominal_Income_Targeting::Nominal_Income_Targeting` conf=5
  - Thesis: Nominal income targeting is a hypothetical monetary policy strategy where the central bank targets the growth rate of nominal GDP (the sum of inflation and real output growth).
- ✓ SOLID `BOJ_April_2026_Rate_Decision::BOJ_April_2026_Rate_Decision` conf=5
  - Thesis: The BOJ held its policy rate at 0.75% in April 2026 despite a hawkish policy statement, with 3 board dissenters calling for a hike. Governor Ueda's presser revealed caution on underlying inflation anc
- ✓ SOLID `Fiscal_Sustainability_Debt_Dynamics::Fiscal_Sustainability_Debt_Dynamics` conf=4
  - Thesis: Fiscal sustainability requires that the debt-to-GDP ratio does not rise persistently, which — through the government's intertemporal budget constraint — translates into the condition that the primary 

## STAGE 2 — RAW Source Evidence

### RAW: US_Treasury_H1_2026_Refunding_And_Debt::Q2 2026 — May 6, 2026 (Brian Smith, Deputy Asst Secretary)
- file: `02_sources\Clipping\US_Treasury_H1_2026_Refunding_And_Debt.md`
- score: 0.032
- thesis: Q2 2026 — May 6, 2026 (Brian Smith, Deputy Asst Secretary)
- heatmap context:
```
>>> L1: # US Treasury H1 2026 — Refunding, Debt Outstanding, Yield Curve, ACM Term Premium
          L2: 
          L3: *Clipping tổng hợp từ web research 2026-06-29. Nguồn: Treasury.gov, MSPD FiscalData, CRFB, PrimeRates, NY Fed, WebSearch.*
          L4: 
          L5: ---
          L6: 
      [... skip to next heatmap section ...]
          L14: - **Coupon sizes:** Maintained stable; no major changes announced
          L15: - Source: [home.treasury.gov/news/press-releases/sb0010] (timed out — data from search summary)
          L16: 
          L17: ### Q2 2026 — May 6, 2026 (Brian Smith, D
```

### RAW: US_Treasury_H1_2026_Refunding_And_Debt::Q1 2026 — February 4, 2026 (Brian Smith, Deputy Asst Secretary)
- file: `02_sources\Clipping\US_Treasury_H1_2026_Refunding_And_Debt.md`
- score: 0.032
- thesis: Q1 2026 — February 4, 2026 (Brian Smith, Deputy Asst Secretary)
- heatmap context:
```
>>> L1: # US Treasury H1 2026 — Refunding, Debt Outstanding, Yield Curve, ACM Term Premium
          L2: 
          L3: *Clipping tổng hợp từ web research 2026-06-29. Nguồn: Treasury.gov, MSPD FiscalData, CRFB, PrimeRates, NY Fed, WebSearch.*
          L4: 
          L5: ---
          L6: 
      [... skip to next heatmap section ...]
          L14: - **Coupon sizes:** Maintained stable; no major changes announced
          L15: - Source: [home.treasury.gov/news/press-releases/sb0010] (timed out — data from search summary)
          L16: 
          L17: ### Q2 2026 — May 6, 2026 (Brian Smith, D
```

### RAW: Watts_Wray_Macroeconomics::Annual growth = 100 × (Real GDP t  - Real GDP t-4 )/Real GDP t-4
- file: `02_sources\books\watts_wray_mmt_macro\Watts_Wray_Macroeconomics.md`
- score: 0.030
- thesis: Annual growth = 100 × (Real GDP t  - Real GDP t-4 )/Real GDP t-4
- heatmap context:
```
L7517: 
          L7518: Third, firms also resist cutting prices when demand falls because they want to avoid so-called adverse selection problems, whereby they gain a reputation only as a bargain price supplier. Firms value 'repeat sales' and thus want to foster consumer goodwill.
          L7519: 
          L7520: Circumstances change somewhat when the economy approaches full  productive  capacity.  Then  the  mix  between  output  growth  and price  rises  becomes  more  likely  to  be  biased  toward  price  rises (depending  on  the  bottlenecks  in  specific  areas  of  productive activi
```

## STAGE 3 — Expansion Proposal

> **Action required:** Review RAW evidence above, then:

- [ ] UPDATE `03_wiki\perspectives\Vietnam_Private_Credit_Outlook_2025.md` — address: confidence=1 ≤ 2, no source_refs section
      Add source_refs from RAW hits above
- [ ] UPDATE `03_wiki\perspectives\NBFI_Surveillance_Priorities.md` — address: confidence=1 ≤ 2
      Add source_refs from RAW hits above

---
*Generated by deepdive_search.py v2.1 on 2026-07-01*