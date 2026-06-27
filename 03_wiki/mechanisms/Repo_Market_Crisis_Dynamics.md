---
title: Repo Market Crisis Dynamics
aliases:
- Run on Repo
- Repo Runs
- Fire Sales
type: mechanism
tags:
- market-crisis
- liquidity
- repo
- systemic-risk
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: A 'Run on Repo' occurs when cash providers lose confidence in dealers or collateral
  value, leading to a sudden refusal to roll over short-term funding and a spike in
  haircuts, triggering systemic fire-sales.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 170
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Khủng hoảng tài chính toàn cầu (GFC) chứng minh rằng thị trường Repo không phải là nơi trú ẩn an toàn tuyệt đối. Các ranh giới về tín nhiệm có thể bị phá vỡ cực nhanh, biến một thị trường tài trợ có đảm bảo thành một cuộc tháo chạy thanh khoản dây chuyền (Run on Repo).

## 1. Transmission Mechanism: The Repo Run Cycle
[RAW] Neftci bóc tách vòng xoáy khủng hoảng qua 3 giai đoạn:
1.  **Confidence Shock:** Sự nghi ngờ về khả năng thanh toán của Dealer (như Lehman Brothers) hoặc chất lượng tài sản đảm bảo (như MBS/ABS).
2.  **Funding Withdrawal:**
    - **Tri-party Run:** Các quỹ thị trường tiền tệ (MMFs) từ chối gia hạn (rollover) các khoản vay qua đêm.
    - **Bilateral Run:** Các bên mua tài sản tăng đột ngột tỷ lệ Haircut (e.g., từ 5% lên 25%).
3.  **Fire-sale Spirals:** Dealer bị thiếu hụt tiền mặt nghiêm trọng, buộc phải bán tháo chính tài sản đảm bảo đó trên thị trường giao ngay (Spot) để lấy tiền trả nợ. Giá tài sản giảm mạnh -> Kích hoạt thêm Margin Call -> Khủng hoảng lan rộng.

## 2. Worked Example: Lehman Brothers (2008)
[RAW] Sự sụp đổ của Lehman Brothers bị đẩy nhanh bởi ranh giới thanh khoản tại thị trường Tri-party Repo. Khi các chủ nợ (cash lenders) thấy rủi ro đối tác quá cao, họ ngừng cho vay ngay cả khi có tài sản đảm bảo. Không còn nguồn vốn duy trì hoạt động hàng ngày, Lehman buộc phải nộp đơn phá sản chỉ trong vài ngày.

## 3. Boundary Conditions & Institutional Mitigants
- **CCP Resilience:** [RAW] Các thị trường Repo dựa trên **Central Counterparties (CCP)** như tại Châu Âu tỏ ra bền bỉ hơn trong khủng hoảng nhờ tính chất giao dịch ẩn danh và cơ chế bù trừ tập trung giúp loại bỏ rủi ro đối tác trực tiếp.
- **Collateral Quality:** Tài sản đảm bảo chính phủ (Treasuries) ít bị ảnh hưởng bởi "Haircut Run" hơn so với các tài sản rủi ro (Equities, Structured Credit).

## Related
- [[Repurchase_Agreement_Mechanism]] — Nền tảng vận hành Repo.
- [[Central_Counterparty_CCP]] — Vai trò ổn định hệ thống.
- [[Collateral_Haircut]] — Biến số chính kích hoạt tháo chạy.
- [[Liquidity_Hierarchy_Mechanism]] — Vị trí của Repo trong tháp thanh khoản.
- [[Repurchase_Agreement_Repo_Market_Structure]]
- [[Repo_Operations]]
- [[Market_Depth_Vs_Breadth]]
- [[Bond_Market_Liquidity_Architectures]]
