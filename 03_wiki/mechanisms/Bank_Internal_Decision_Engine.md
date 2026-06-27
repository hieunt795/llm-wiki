---
title: Bank Internal Decision Engine
aliases:
- ROE Hurdle Engine
- RWA Optimization logic
- Internal Threshold Mechanism
type: mechanism
tags:
- banking
- basel-iii
- risk-management
- profitability
status: reviewed
confidence: 4
half_life_years: 10
expert_lens: "Blackstone | AltsWire"
provenance: Blackstone & AltsWire Reports (2026)
thesis: Bộ máy ra quyết định nội bộ của ngân hàng vận hành dựa trên việc tối ưu hóa
  ROE so với ngưỡng rào cản (Hurdle Rate); khi các quy định Basel thắt chặt làm tăng
  chi phí vốn, các khoản vay không đạt ngưỡng lợi nhuận sẽ bị đẩy ra khỏi bảng cân
  đối thông qua tăng giá, thoái vốn hoặc chuyển giao rủi ro cho các quỹ Private Credit.
source_refs:
- file: https://howfinanceworks.substack.com/p/how-private-credit-works
  page: 1
created: '2026-04-22'
updated: '2026-04-28'
---

# Bank Internal Decision Engine

## Mechanism
Hệ thống ra quyết định của ngân hàng trong bối cảnh [[Regulatory_Implementation_Framework]] không chỉ là tuân thủ, mà là một quy trình tối ưu hóa lợi nhuận (Profitability Optimization).

### 1. Phân rã cấu trúc (The Inputs)
- **RWA Recalculation:** Ngân hàng liên tục tính toán lại Trọng số rủi ro (RWA) theo khung Basel mới. Tại Mỹ, phương pháp **ERBA** đơn giản hóa việc này thành một "Single Stack".
- **Cost of Capital:** Chi phí huy động vốn tự sở hữu (CET1) tăng lên khi yêu cầu tỷ lệ vốn cao hơn.
- **ROE Hurdle Rate:** Ngân hàng đặt ra một ngưỡng tỷ suất lợi nhuận trên vốn chủ sở hữu mục tiêu (**~12-15%**).

### 2. Quy trình kiểm tra (The Engine)
Sử dụng công thức đơn giản hóa để kiểm toán tính khả thi của một khoản vay:
$$ \text{ROE}_{\text{loan}} = \frac{\text{Spread} - \text{OpEx} - \text{Expected Loss}}{\text{Capital Required} \times \text{CET1 Ratio}} $$

**Logic Decision:**
- Nếu $\text{ROE}_{\text{loan}} \geq \text{Hurdle}$: **Tiếp tục giữ (Keep)**.
- Nếu $\text{ROE}_{\text{loan}} < \text{Hurdle}$: **Dịch chuyển (Migrate)**.

### 3. Các hành động (The Output)
Khi khoản vay không đạt ngưỡng ROE, động cơ của ngân hàng là:
1.  **Tăng giá (Pricing ↑):** Tăng Lending Spread để bù đắp chi phí vốn. Ước tính mỗi **1% yêu cầu vốn tăng** có thể đẩy spread tăng **15-20 bps**.
2.  **Giảm phơi nhiễm (Exposure ↓):** Thoái vốn hoàn toàn hoặc không tái cấp hạn mức.
3.  **Hợp tác/Đẩy rủi ro (Risk Offloading):**
    - Sử dụng [[Significant_Risk_Transfer]] (SRT) để "thuê" bảng cân đối kế toán.
    - Chuyển sang mô hình **Partnership** (ví dụ: Citi & Apollo).

### Result: Credit Migration
Quy trình này trực tiếp đẩy các doanh nghiệp có rủi ro cao hoặc không đủ "lợi nhuận biên" cho ngân hàng sang thị trường [[Private_Credit]].

## Mechanism
- [[Regulatory_Implementation_Framework]]
- [[Basel_III_Impact_On_Private_Credit]]
- [[Significant_Risk_Transfer]]
- [[Bank_Private_Credit_Partnership]]

### Citations
- *"The increase in capital and funding costs is transmitted into loan pricing, raising spreads."* — [[https://howfinanceworks.substack.com/p/how-private-credit-works]]
- Fed Z.1 Technical Q&A on Banking Sector Capital.
