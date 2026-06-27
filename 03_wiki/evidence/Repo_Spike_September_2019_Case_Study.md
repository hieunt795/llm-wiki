---
title: Repo Spike September 2019 Case Study
aliases:
- Repo 2019
- September 2019 Liquidity Crunch
type: evidence
tags:
- repo-market
- monetary-policy
- financial-stability
- case-study
status: verified
confidence: 5
half_life_years: 1
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat"
provenance: Tuckman & Serrat (2022), NY Fed Staff Report
thesis: Sự kiện Repo tháng 9/2019 là một cuộc khủng hoảng thanh khoản kỹ thuật, minh
  chứng cho việc 'Dự trữ dồi dào' (Abundant Reserves) có thể trở nên khan hiếm đột
  ngột do ma sát quy chế (Basel III) và các đợt rút vốn định kỳ của Kho bạc (TGA).
source_refs: []
created: '2026-04-22'
updated: '2026-04-22'
---

## Thesis

Sự kiện Repo tháng 9/2019 là một cuộc khủng hoảng thanh khoản kỹ thuật, minh chứng cho việc "Dự trữ dồi dào" (Abundant Reserves) có thể trở nên khan hiếm đột ngột do ma sát quy chế (Basel III) và các đợt rút vốn định kỳ của Kho bạc (TGA). Ngay cả khi tổng lượng dự trữ trong hệ thống lớn, sự xơ cứng trong việc luân chuyển vốn của các ngân hàng thương mại có thể làm đứt gãy hoàn toàn cơ chế truyền dẫn lãi suất.

---

## 1. The Trigger: The Double-Drain Shock

[RAW] Theo Tuckman & Serrat (2022), vào giữa tháng 9/2019, dự trữ sụt giảm đột ngột khoảng 9% do hai nguyên nhân chính hội tụ:
1.  **Corporate Tax Payments:** Các đợt nộp thuế doanh nghiệp hàng quý làm dịch chuyển một lượng lớn tiền gửi từ hệ thống ngân hàng vào tài khoản TGA tại Fed.
2.  **Treasury Settlement:** Các đợt tất toán trái phiếu Kho bạc mới yêu cầu các Dealer phải sử dụng dự trữ để thanh toán, đồng thời tăng nhu cầu vay Repo để tài trợ cho lượng hàng tồn kho này.

## 2. The Pricing Spike

[RAW] Trong khi lãi suất mục tiêu của Fed (Fed Funds Target) là 2.00% - 2.25%:
-   Lãi suất Repo bình quân (weighted-average) vọt lên **5.25%**.
-   Đỉnh điểm có giao dịch được thực hiện ở mức **10%**.
[[Tuckman_Serrat_2022.md#L2641-L2642]]

## 3. Structural Frictions (Tại sao thanh khoản không chảy?)

[RAW] Tuckman bóc tách 4 rào cản quy chế khiến các ngân hàng lớn (vốn có dự trữ) không dám cho vay ra để bình ổn thị trường:
1.  **Leverage Ratio (Tỷ lệ đòn bẩy):** Việc cho vay Repo làm phình to tổng tài sản, buộc ngân hàng phải tăng vốn chủ sở hữu tương ứng, làm giảm tỷ suất sinh lời trên vốn (ROE).
2.  **HQLA Preference (Ưu tiên dự trữ):** Quy định LCR cho phép dùng cả Trái phiếu Kho bạc và Dự trữ làm tài sản thanh khoản. Tuy nhiên, các nhà giám sát (examiners) ưu tiên Dự trữ hơn vì tính thanh khoản tức thời.
3.  **Daylight Overdraft Stigma:** Nỗi sợ về việc để tài khoản tại Fed bị thấu chi tạm thời trong ngày khiến các ngân hàng cực kỳ thận trọng trong việc giải ngân dự trữ.
4.  **SMC (Supervisory Monitoring of Liquidity):** Các quy trình giám sát nội bộ (internal liquidity stress tests) thường yêu cầu các ngân hàng phải duy trì một lượng dự trữ "vượt mức" tối thiểu tại Fed vào cuối ngày để đáp ứng các kịch bản rút tiền khẩn cấp ảo định, khiến thanh khoản thực tế bị "đóng băng" tại chỗ.
[[Tuckman_Serrat_2022.md#L2648-L2661]]

---

## 4. Transmission Failure Schematic

```text
       [ FED TARGET: 2.25% ]
               │
               ▼
    [ SHOCK: TGA + TAX DRAIN ] ─────────┐
               │                        │
               ▼                        ▼
    [ BANK RESERVES ↓ ] <──── [ REGULATORY FRICTION (Basel III / SMC) ]
               │             (Banks lock their cash due to LCR/SMC)
               ▼
    [ REPO RATE: 10% ] <───── (Demand > Supply)
```

## 5. Strategic Context: The Financial Repression Link

Sự kiện 2019 minh chứng cho một hình thái của [[Financial_Repression]] trong kỷ nguyên hiện đại: việc chính phủ duy trì mức nợ cao và thâm hụt lớn (dẫn đến các cú sốc TGA) kết hợp với các quy định ngân hàng thắt chặt (Basel III) đã vô tình tạo ra một hệ thống "giòn" (brittle). Trong hệ thống này, dự trữ ngân hàng không còn là "dầu bôi trơn" tự do mà trở thành "con tin" của các quy định an toàn vốn, làm suy yếu khả năng điều tiết lãi suất của chính sách tiền tệ truyền thống.

## Evidence / Source Anchors

- [RAW] Tuckman, B., & Serrat, A. (2022). *Fixed Income Securities*. Section "Abundant Reserves Implementation", pp. 43-44. [[Tuckman_Serrat_2022.md#L2631]]
- [WEB] NY Fed Staff Report 974: "Reserves Were Not So Ample After All" (2021).

## Related
- [[Treasury_General_Account_Mechanism]] — Kênh rút vốn chính gây ra sự cố.
- [[Basel_III_Liquidity_Standards]] — Nguồn gốc của các rào cản LCR.
- [[Standing_Repo_Facility_SRF]] — Công cụ phòng vệ vĩnh viễn được Fed thiết lập sau sự kiện.
- [[Lean_Vs_Clean_Monetary_Debate]]
- [[The_Case_for_Leaning_Consensus]]
- [[Case_Study_Monetary_Policy_Credibility_in_Indonesia]]
- [[BoJ_QE_2013_Case_Study]]
- [[Taper_Tantrum_2013_Case_Study]]
