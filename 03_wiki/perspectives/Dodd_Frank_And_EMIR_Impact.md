---
title: Dodd-Frank and EMIR Regulatory Impact
aliases:
- Dodd-Frank Act
- EMIR
- Mandatory Clearing
- SEF Execution
type: perspective
tags:
- regulation
- derivatives
- post-gfc
status: verified
confidence: 5
half_life_years: 5
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: The post-GFC regulatory shift (Dodd-Frank and EMIR) mandates central clearing
  and exchange trading for standardized OTC derivatives, merging pre- and post-trade
  processes to reduce systemic risk.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 34
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Các quy định hậu GFC (Dodd-Frank tại Mỹ và EMIR tại EU) đã thay đổi cơ bản hạ tầng thị trường phái sinh bằng cách buộc các hợp đồng song phương (bilateral) chuyển sang bù trừ tập trung (CCP) và giao dịch trên các nền tảng có giám sát.

## 1. Core Mandates
- **Mandatory Clearing:** Các phái sinh chuẩn hóa (như Plain Vanilla IRS, CDS) bắt buộc phải được bù trừ qua CCP để loại bỏ rủi ro đối tác tích tụ.
- **Exchange/SEF Trading:** Chuyển dịch giao dịch từ điện thoại/chat sang các **Swap Execution Facilities (SEFs)** hoặc sàn giao dịch tập trung để tăng tính minh bạch về giá và khối lượng.
- **Standardization:** Khuyến khích chuẩn hóa hợp đồng để dễ dàng bù trừ và báo cáo rủi ro.

## 2. Impact on Financial Engineering
- **Funding & Margin Costs:** [RAW] Quy định mới yêu cầu ký quỹ hai chiều (IM và VM) cho cả các dẫn xuất không được bù trừ tập trung. Điều này làm tăng chi phí vốn và thay đổi cấu trúc định giá (XVA).
- **Operational Merging:** Quy trình Middle Office và Back Office ngày càng hội tụ để hỗ trợ yêu cầu "clearing certainty" (xác nhận bù trừ ngay lập tức khi thực hiện lệnh).
- **Standardized Reporting:** Việc báo cáo thời gian thực cho các Trade Repositories cho phép các cơ quan quản lý giám sát mức độ rủi ro hệ thống theo từng lớp tài sản.

## 3. Failure Conditions / Caveats
- **Liquidity Fragmentation:** Việc chia tách các giao dịch theo địa lý (US vs EU) có thể dẫn đến sự phân mảnh thanh khoản nếu các quy định không tương đương.
- **Procyclicality:** Yêu cầu ký quỹ bằng tiền mặt trong thời kỳ biến động mạnh có thể gây áp lực thanh khoản lên các thành viên bù trừ, dẫn đến hiện tượng bán tháo tài sản khác để lấy tiền mặt.

## Related
- [[Central_Counterparty_CCP]] — Hạ tầng bù trừ cốt lõi.
- [[Variation_Margin_Vs_Initial_Margin]] — Các lớp bảo vệ ký quỹ mới.
- [[Valuation_Adjustments_xVA]] — Tác động định giá từ chi phí vốn và ký quỹ.
- [[Dodd_Frank_And_JOBS_Act]]
- [[Physical_Vs_Cash_Settlement_Debate]]
- [[Alternative_Investment_Funds]]
- [[Bermudan_Swaptions]]
- [[Bond_Futures_Contract_Design]]
- [[Caps_And_Floors]]
- [[CMT_And_CMS_Floaters]]
- [[Credit_Default_Swaps_CDS]]
- [[ELTIF_And_AIFMD_Framework]]
- [[Forward_Volatility_Trading]]
- [[Model_Risk_And_Jumps]]
- [[Structured_Notes]]
- [[Coupon_Washing_Tax_Strategies]]
- [[LIBOR_And_Term_Benchmark_Fragility]]
- [[Asset_Swap_Structure]]
- [[Barrier_Options]]
