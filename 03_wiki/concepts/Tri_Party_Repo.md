---
title: Tri Party Repo
aliases: []
type: concept
tags: []
status: draft
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: legacy_migrated
thesis: '[RAW] Tri-party Repo là giải pháp tối ưu hóa hạ tầng cho các định chế tài
  chính không có khả năng vận hành back-office phức tạp. Trong khi Alexander Düring
  nhấn mạnh ranh giới về việc không thể "sờ" vào tài sản vật lý cho mục đích short-selling,
  Salih Neftci làm rõ vai trò của Clearing Bank trong vi'
source_refs: []
created: '2026-04-26'
updated: '2026-04-26'
---

﻿---
title: "Tri-Party Repo"
aliases: [Repo ba bên, Triparty Repurchase Agreement]
type: mechanism
tags: [fixed-income, market-infrastructure, liquidity, settlement]
status: active
confidence: 5
expert_lens: "Alexander During | Salih Neftci"
provenance: "Principles_of_Financial_Engineering_Neftci.md"
thesis: "A Tri-party repo is a repurchase agreement where a neutral third-party agent (Clearing Bank) manages the collateral, settlement, and daily marking-to-market, significantly reducing the back-office operational burden for cash lenders."
source_refs:
  - file: "Principles_of_Financial_Engineering_Neftci.md"
    page: 158
  - file: "Fixed_Income_Alexander_During_Ch15.md"
    page: 4
created: 2026-04-13
updated: 2026-04-21
---

## Thesis
[RAW] Tri-party Repo là giải pháp tối ưu hóa hạ tầng cho các định chế tài chính không có khả năng vận hành back-office phức tạp. Trong khi Alexander Düring nhấn mạnh ranh giới về việc không thể "sờ" vào tài sản vật lý cho mục đích short-selling, Salih Neftci làm rõ vai trò của Clearing Bank trong việc tự động hóa các khâu DVP và quản trị tài sản đảm bảo.

## 1. Mechanism: The Clearing Bank Intermediary
[RAW] Trong cấu trúc Tri-party, thay vì chuyển giao chứng khoán trực tiếp giữa hai bên (Delivery Repo), một ngân hàng bù trừ (Clearing Bank - e.g., BNY Mellon, JP Morgan) đóng vai trò trung gian:
- **Collateral Management:** Bên thứ ba tự động lựa chọn các chứng khoán đủ tiêu chuẩn từ tài khoản của người bán để làm tài sản đảm bảo.
- **Mark-to-Market:** Tự động định giá lại tài sản hàng ngày và thực hiện các lệnh gọi ký quỹ (margin calls) nếu cần thiết.
- **DVP Efficiency:** Đảm bảo việc thanh toán tiền và giao chứng khoán (Delivery versus Payment) diễn ra đồng thời trên hệ thống sổ sách của chính mình.

## 2. Strategic Advantages
- **Operational Scalability:** Người cho vay tiền (e.g., Money Market Funds) không cần đội ngũ vận hành để cầm giữ tài sản đảm bảo vật lý.
- **Cost Reduction:** Phí giao dịch thấp hơn do chỉ là các bút toán nội bộ trong cùng một ngân hàng lưu ký.
- **Simplicity:** Thủ tục đơn giản hóa, phù hợp cho các giao dịch General Collateral (GC) khối lượng lớn.

## 3. Boundary Conditions
- **Physical Possession:** [RAW] Nhược điểm lớn nhất là người mua không thực sự chiếm hữu chứng khoán (HIC - Hold-in-Custody style). Do đó, Tri-party Repo gần như vô dụng đối với các chiến lược cần chứng khoán cụ thể để giao hàng (Specials Market).
- **Concentration Risk:** Rủi ro hệ thống tập trung vào một số ít các Clearing Banks lớn (như bài học từ cuộc khủng hoảng 2008).

## Evidence / Source Anchors
- Role of Clearing Bank and US market structure (BNY Mellon/JPM): [[Principles_of_Financial_Engineering_Neftci.md#page=158]]
- Automated DVP and MTM functions: [[Principles_of_Financial_Engineering_Neftci.md#page=158]]
- Limitation regarding Specials and short-selling delivery: [[Fixed_Income_Alexander_During_Ch15.md#page=4]]

## Related
- [[Delivery_Versus_Payment_DvP]] — Nguyên tắc thanh toán cốt lõi.
- [[General_Collateral_Vs_Special]] — Phân loại thị trường theo nhu cầu chứng khoán.
- [[Money_Market_Instruments_Mechanics]] — Người chơi chính trong Tri-party repo.
- [[Repo_Spike_September_2019_Case_Study]]
- [[Cross_Currency_Repo]]
- [[Equity_Repo_Mechanics]]
- [[Futures_Basis_And_Implied_Repo_Rate]]
- [[Repo_Market_Crisis_Dynamics]]
- [[Repo_Operations]]
- [[Central_Counterparty]]
- [[Central_Counterparty_CCP]]
- [[Counterparty_Credit_Risk]]
- [[Standing_Repo_Facility_SRF_Mechanics]]
- [[Treasury_Central_Clearing_Repo_Netting]]
- [[Japan_May_2026_CPI_Report]]
