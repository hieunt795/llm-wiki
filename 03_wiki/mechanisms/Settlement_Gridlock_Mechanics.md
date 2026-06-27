---
title: Settlement Gridlock Mechanics
aliases:
- Lỗi quyết toán hệ thống
- Settlement Fails Spiral
- Reserves-Settlement Link
type: mechanism
tags:
- market-infrastructure
- liquidity
- banking
- systemic-risk
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Ulrich Bindseil | Tuckman & Serrat"
provenance: Tuckman & Serrat (2022), Bindseil (2014)
thesis: Settlement gridlock occurs when a scarcity of bank reserves or high-quality
  collateral prevents the completion of interdependent securities transactions, creating
  a cascading failure that freezes interbank liquidity and forces central bank intervention.
source_refs:
- file: Tuckman_Serrat_Fixed_Income_2022.md
  line: 10476
- file: Bindseil_Monetary_Policy_Operations.md
  line: 2140
created: '2026-04-24'
updated: '2026-04-26'
---

## Thesis

[WIKI] **Settlement Gridlock** là trạng thái "tắc nghẽn giao thông" trên hạ tầng thanh toán, nơi các giao dịch không thể hoàn tất do thiếu hụt dự trữ (Reserves) hoặc tài sản đảm bảo tại các nút trung gian. Đây là rủi ro vận hành có khả năng biến thành rủi ro hệ thống nhanh nhất.

---

## 1. Transmission Flow: The Cascading Fail

**Transmission Flow:**
`[Reserves Scarcity] --(Settlement Fail at Bank A)--> [Liquidity Shortage at Bank B] --(Forced Fail at Bank C)--> [Systemic Gridlock] --(Market Freeze)--> [CB Emergency Injection]`

1.  **Trigger:** Ngân hàng A không đủ dự trữ tại NHTW để quyết toán lệnh mua trái phiếu từ Ngân hàng B.
2.  **Propagation:** Ngân hàng B, do không nhận được trái phiếu từ A, nên không thể giao trái phiếu đó cho Ngân hàng C.
3.  **Gridlock:** Toàn bộ chuỗi giao dịch "lưng tựa lưng" (Back-to-back) bị dừng lại.
4.  **Penalty:** Các bên bắt đầu chịu phí **Fails Charges** [L10476], nhưng phí này không giải quyết được vấn đề thiếu hụt dự trữ vật lý.

---

## 2. Expert Lenses

### A. Tuckman & Serrat (The Microstructure Guard)
[RAW] Tuckman nhấn mạnh rằng kỷ luật quyết toán được duy trì qua hệ thống ký quỹ (Margin) và các quy tắc "Safe Harbor" [L10476]. Tuy nhiên, ông cảnh báo rằng trong stress, các rào cản pháp lý này có thể làm trầm trọng thêm tình trạng thiếu hụt tiền mặt.

### B. Ulrich Bindseil (The Operational Anchor)
[LLM] Dưới lăng kính của Bindseil, Settlement Gridlock là minh chứng cho sự thất bại của việc dự báo các **Autonomous Factors** (Yếu tố tự trị). NHTW phải duy trì một lượng dự trữ dư thừa (Excess Reserves) đủ lớn để bôi trơn các bánh răng quyết toán này.

---

## Related

- [[Liquidity_Coverage_Ratio]] — Lớp đệm phòng ngừa.
- [[Lender_Of_Last_Resort_Mechanism]] — Van xả áp khi gridlock xảy ra.
- [[Fails_Charges_Mechanics]] — Cơ chế trừng phạt lỗi.
- [[Bid_Ask_Bounce]]
- [[Liquidity_Measurement_Taxonomy]]
