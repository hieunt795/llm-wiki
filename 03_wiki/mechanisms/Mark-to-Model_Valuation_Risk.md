---
title: Mark-to-Model Valuation Risk
aliases:
- Stale Valuation Risk
- Model-based Pricing Risk
- Private Credit Valuation Inertia
type: mechanism
tags:
- private-credit
- valuation
- accounting
- systemic-risk
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: '**Mark-to-Model Valuation Risk (Rủi ro định giá dựa trên mô hình)** xảy ra
  khi giá trị của một tài sản tài chính (thường là các khoản vay [[Private_Credit]])
  được xác định bằng các thuật toán toán học hoặc giả định của người quản lý quỹ hơn
  là bằng giá giao dịch thực tế trên thị trường.'
source_refs: []
created: '2026-04-13'
updated: '2026-04-16'
source: https://www.imf.org/en/Publications/GFSR/Issues/2024/04/16/global-financial-stability-report-april-2024
---

# Mark-to-Model Valuation Risk

## Mechanism

**Mark-to-Model Valuation Risk (Rủi ro định giá dựa trên mô hình)** xảy ra khi giá trị của một tài sản tài chính (thường là các khoản vay [[Private_Credit]]) được xác định bằng các thuật toán toán học hoặc giả định của người quản lý quỹ hơn là bằng giá giao dịch thực tế trên thị trường.

Khác với thị trường trái phiếu công khai nơi giá nhảy múa từng giây (Mark-to-Market), các khoản nợ tư nhân được định giá định kỳ (hàng quý hoặc hàng năm). Điều này tạo ra hiện tượng **Valuation Inertia (Tính ỳ định giá)**.

> [!CAUTION]
> **Masking Losses**: IMF (2024) cảnh báo rằng việc định giá theo mô hình có thể che giấu các khoản lỗ thực tế trong thời kỳ thị trường biến động mạnh, tạo ra cảm giác an toàn giả tạo về biến động (volatility) của danh mục. [extracted]

### Các yếu tố gây rủi ro
- **Stale Inputs (Dữ liệu đầu vào cũ)**: Sử dụng các bội số (multiples) hoặc lãi suất chiết khấu đã lỗi thời so với điều kiện vĩ mô hiện tại.
- **Subjective Assumptions (Giả định chủ quan)**: Người quản lý quỹ có xu hướng lạc quan về khả năng hồi phục của doanh nghiệp hoặc tỷ lệ thu hồi nợ (Recovery rate).
- **Illiquidity Premium Blindness**: Khó khăn trong việc định lượng chính xác mức phí bù đắp rủi ro thanh khoản (illiquidity premium) trong điều kiện stress. [researched]

### Hệ quả đối với Nhà đầu tư và Hệ thống
1. **Moral Hazard**: Các quỹ có thể duy trì mức phí quản lý cao dựa trên NAV "ảo".
2. **Abrupt Devaluation (Định giá lại đột ngột)**: Khi sự thật không thể che giấu (ví dụ: doanh nghiệp phá sản thực sự), NAV có thể sụt giảm mạnh một cách đột ngột, gây sốc cho nhà đầu tư.
3. **Redemption Pressure**: Trong các [[Semiliquid_Fund_Structures]], sự nghi ngờ về tính chính xác của NAV có thể kích hoạt các yêu cầu rút vốn đồng loạt. [inferred]

### Hình ảnh minh họa (Idea)
> **Gương ảo giác**: Vẽ một người (Fund Manager) đang nhìn vào chiếc gương (Model). Trong gương, anh ta thấy mình rất khỏe mạnh (High NAV). Nhưng thực tế bên ngoài, anh ta đang bị thương (Real losses). Chú thích: "Mô hình chỉ nhìn thấy những gì nó được lập trình để thấy".

## Evidence / Source Anchors
- [extracted] [IMF, "Global Financial Stability Report", April 2024](https://www.imf.org/en/Publications/GFSR/Issues/2024/04/16/global-financial-stability-report-april-2024)
- [researched] [Brookings Institution, "Risks in Private Credit", 2024](https://www.brookings.edu/articles/the-rise-of-private-credit-risk-stability/)
