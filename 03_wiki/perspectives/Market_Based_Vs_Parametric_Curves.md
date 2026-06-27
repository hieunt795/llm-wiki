---
title: Market Based Vs Parametric Curves
aliases:
- Market-based vs Parametric curves
- Reduced-form models
- Exact repricing vs Smooth forwards
type: perspective
tags: []
status: verified
confidence: 4
half_life_years: 5
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch20.md"
thesis: Việc lựa chọn giữa mô hình dựa trên thị trường (Market-based) và mô hình tham
  số (Parametric) phản ánh sự đánh đổi chiến lược giữa tính chính xác cục bộ và tính
  trơn vĩ mô của đường cong. [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=4]]
source_refs:
- file: Fixed_Income_Alexander_During_Ch20.md
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
chapter: 19
---

# Market Based Vs Parametric Curves

## Mechanism

Việc lựa chọn giữa mô hình dựa trên thị trường (Market-based) và mô hình tham số (Parametric) phản ánh sự đánh đổi chiến lược giữa tính chính xác cục bộ và tính trơn vĩ mô của đường cong. [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=4]]

### 1. Market-Based Curves (Mô hình dựa trên thị trường)
- **Mục tiêu:** Tái định giá (reprice) chính xác tất cả các công cụ đầu vào trên thị trường để triệt tiêu các cơ hội chênh lệch giá hiển nhiên giữa mô hình và thực tế.
- **Đặc điểm:** Yêu cầu số lượng lớn dữ liệu đầu vào. Đường cong thu được thường có các đoạn [[Forward_Rates_Derivation|lãi suất kỳ hạn]] (forwards) không trực quan, bị nhiễu do sai số giá hoặc thanh khoản cục bộ của từng công cụ. [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=4]]

### 2. Parametric Curves / [[Market_Based_Vs_Parametric_Curves|reduced-form models]] (Mô hình tham số)
- **Mục tiêu:** Tìm kiếm một biểu diễn hàm số tinh gọn (parsimonious) đại diện cho xu hướng chung của lãi suất.
- **Đặc điểm:** Sử dụng số lượng tham số ít (ví dụ: NS, NSS). Mô hình không cố gắng khớp chính xác mọi giá thị trường.
- **Giá trị sử dụng:** Các "độ lệch" (divergences) giữa giá mô hình và giá thực tế không được coi là sai số, mà là các điểm **mất cân đối (dislocations)** tiềm năng. Đây là cơ sở để các nhà giao dịch phát hiện các cơ hội đầu tư giá trị tương đối (Relative Value). [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=4]]

### Kết luận
Nhà giao dịch sử dụng mô hình Market-based để quản lý rủi ro và định giá chính xác (valuation), trong khi sử dụng mô hình Parametric để tìm kiếm ý tưởng giao dịch và phân tích cấu trúc vĩ mô của đường cong. [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=4]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch20.md#page=4]] — Phân kỳ giữa hai phương pháp tiếp cận mô hình hóa đường cong.
