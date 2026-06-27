---
title: Wash Sale Rules & Tactics
aliases:
- Wash Sale
- Bed and Breakfasting
- Tax Postponement Synthetic
type: convention
tags:
- taxation
- regulation
- options
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Financial engineers use synthetic instruments (like combinations of options)
  to circumvent wash-sale rules, allowing investors to realize capital losses for
  tax purposes while maintaining their market exposure.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 14
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Các cơ quan thuế áp dụng quy tắc Wash Sale để ngăn chặn việc bán tài sản nhằm ghi nhận lỗ tạm thời rồi mua lại ngay lập tức. Financial Engineering cung cấp các giải pháp thay thế bằng cách tạo các vị thế tổng hợp (synthetics) để duy trì rủi ro thị trường mà không vi phạm trực tiếp các ranh giới pháp lý.

## 1. The Strategy: Synthetic Short Position
[RAW] Để hiện thực hóa lỗ của một cổ phiếu Z (đang lỗ từ 100 xuống 50) mà không thực sự bán nó:
1.  **Step 1:** Mua thêm một cổ phiếu Z mới tại giá 50.
2.  **Step 2 (Synthetic Short):**
    - Bán (Short) một At-the-money Call option với Strike 50.
    - Mua (Long) một At-the-money Put option với Strike 50.
    - Tổ hợp Short Call + Long Put tương đương với một vị thế Short cổ phiếu.

## 2. Worked Example (Tax Recognition)
- **Initial State:** Nắm giữ cổ phiếu Z (Cost 100, Market 50).
- **Strategy Execution:** Thực hiện Step 1 và 2 như trên. Sau 31 ngày (vượt ranh giới Wash Sale rule của Mỹ):
    - **Scenario A (Z tăng):** Short Call bị thực hiện (exercised). Nhà đầu tư giao cổ phiếu Z cũ (giá 100) để nhận 50. Ghi nhận lỗ 50.
    - **Scenario B (Z giảm):** Long Put được thực hiện. Nhà đầu tư bán cổ phiếu Z cũ (giá 100) lấy 50. Ghi nhận lỗ 50.
- **Result:** Trong cả hai trường hợp, nhà đầu tư đều ghi nhận được khoản lỗ 50 trên sổ sách thuế, nhưng vẫn giữ được 1 cổ phiếu Z (mua tại giá 50) trong danh mục để duy trì chiến lược đầu tư ban đầu.

## 3. Boundary Conditions & Risks
- **Legal Timing:** [RAW] Tại Mỹ, Wash Sale rule áp dụng nếu giao dịch mua lại xảy ra trong vòng 31 ngày. Kỹ thuật này đòi hỏi việc quản lý thời hạn (expiration) của Option cực kỳ chính xác.
- **Counterparty/Operational Risk:** Sử dụng OTC Options cho phép tùy chỉnh ngày hết hạn linh hoạt hơn so với các Option niêm yết trên sàn (Exchange-traded).
- **Execution Cost:** Chi phí hoa hồng và chênh lệch Bid-Ask của Options có thể làm giảm hiệu quả thuế.

## Related
- [[Option_Payoff_Principles]] — Nền tảng cấu tạo vị thế Short/Long từ các công cụ lồi.
- [[Synthetics]] — Nguyên lý cốt lõi của việc tái tạo rủi ro.
- [[Portfolio_Rebalancing_Strategies]] — Mục đích cuối cùng của việc giữ lại tài sản.
- [[Circular_16_2021_Vietnam_Banking_Bond_Rules]]
- [[Coupon_Washing_Tax_Strategies]]
- [[Alternative_Investment_Funds]]
- [[Business_Development_Company]]
- [[ELTIF_And_AIFMD_Framework]]
- [[Rules_Vs_Discretion_Debate]]
