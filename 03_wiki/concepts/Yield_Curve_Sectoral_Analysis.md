---
title: Yield Curve Sectoral Analysis
aliases:
- Sectoral richness
- Sectoral cheapness
- Re-centering spreads
type: concept
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch19.md"
thesis: Phân tích phân khúc (Sectoral Analysis) sử dụng các mô hình spline để xác
  định các cơ hội giao dịch giá trị tương đối (Relative Value) bằng cách tách biệt
  biến động chung của đường cong khỏi các đặc tính cục bộ của từng nhóm trái phiếu.
  [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=9]]
source_refs:
- file: Fixed_Income_Alexander_During_Ch19.md
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
chapter: 18
---

# Yield Curve Sectoral Analysis

## Mechanism

Phân tích phân khúc (Sectoral Analysis) sử dụng các mô hình spline để xác định các cơ hội giao dịch giá trị tương đối (Relative Value) bằng cách tách biệt biến động chung của đường cong khỏi các đặc tính cục bộ của từng nhóm trái phiếu. [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=9]]

### 1. Kỹ thuật tái chuẩn hóa (Re-centering)
Khi so sánh các mức sai lệch (spread) của từng trái phiếu so với đường cong spline, các nhà phân tích thực hiện tái chuẩn hóa mức spread trung bình của một phân khúc (ví dụ: nhóm trái phiếu 7-15 năm) về mức 0.
- **Mục tiêu:** Loại bỏ ảnh hưởng của việc toàn bộ phân khúc đó đang "đắt" (rich) hoặc "rẻ" (cheap) so với phần còn lại của đường cong do các yếu tố cung-cầu mang tính cấu trúc hoặc chu kỳ phát hành.
- **Hệ quả:** Cho phép nhà giao dịch tập trung vào rủi ro đơn lẻ của từng mã trái phiếu (idiosyncratic risk) trong phân khúc đó mà không bị nhiễu bởi xu hướng của cả nhóm. [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=9]]

### 2. Sự phân kỳ chỉ báo
Sự gia tăng độ phân tán spread (dispersion) trong một phân khúc, ngay cả khi mức spread trung bình không đổi, là tín hiệu cảnh báo về:
- Sự suy giảm khả năng hấp thụ rủi ro của Dealer.
- Sự xuất hiện của các rào cản quy chế (như Dodd-Frank) hạn chế nghiệp vụ [[Repurchase_Agreement|repo]] trong phân khúc đó. [extracted] [[Fixed_Income_Alexander_During_Ch19.md#page=9]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch19.md#page=9]] — Quy trình re-centering spread và phân tích độ đắt/rẻ của các phân khúc trái phiếu cụ thể.
