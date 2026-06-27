---
title: ACM Curve Decomposition
aliases:
- ACM model
- Adrian Crump Moench
- Curve decomposition
type: mechanism
tags:
- yield-curve
- macroeconomics
- term-premium
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: 'Mô hình ACM (Adrian, Crump, Moench) là một khung định lượng được New York
  Fed sử dụng để phân tách lợi suất trái phiếu thành hai thành phần chính: kỳ vọng
  lãi suất ngắn hạn và phần bù rủi ro kỳ hạn (Term Premium), giúp xác định động lực
  thực sự đằng sau các biến động của đường cong lợi suất.'
source_refs:
- file: Fixed_Income_Alexander_During_Ch21.md
  page: 1
created: '2026-04-13'
updated: '2026-04-22'
---

# ACM [[ACM_Curve_Decomposition|curve decomposition]]

## Mechanism

Mô hình ACM, được đặt tên theo các tác giả Adrian, Crump và Moench, là một khung định lượng được New York Fed sử dụng hàng ngày để phân tách lợi suất trái phiếu thành các thành phần không thể quan sát được. [extracted] [[Fixed_Income_Alexander_During_Ch21.md#page=1]]

## Mechanism
Mô hình này chia lợi suất của một trái phiếu tại mọi kỳ hạn thành hai phần chính:
1. **Thành phần Kỳ vọng (Expectations component):** Lợi suất trung bình kỳ vọng của các lãi suất ngắn hạn trong suốt kỳ hạn của trái phiếu.
2. **Phần bù rủi ro kỳ hạn (Term Premium):** Mức bù đắp bổ sung cho rủi ro lãi suất mà nhà đầu tư phải gánh chịu. [extracted] [[Fixed_Income_Alexander_During_Ch21.md#page=1]]

### Đặc điểm kỹ thuật
- **Lớp mô hình Affine:** ACM thuộc dòng mô hình cấu trúc kỳ hạn Affine, giả định rằng giá tài sản là các hàm tuyến tính của các nhân tố rủi ro (state variables).
- **Tính thực tiễn:** Dữ liệu phân tách từ mô hình này giúp các nhà quản lý quỹ và hoạch định chính sách hiểu liệu một đợt tăng lợi suất là do thị trường lo ngại lạm phát/tăng trưởng (kỳ vọng) hay do sự thay đổi trong khẩu vị rủi ro và cung-cầu (term premium). [extracted] [[Fixed_Income_Alexander_During_Ch21.md#page=1-2]]

### Hạn chế
Mô hình ACM dựa trên các giả định rất khắt khe về cách thức rủi ro được định giá trên thị trường. Trong thực tế, các giả định này có thể không duy trì được, [[General_Collateral_Vs_Special|đặc biệt]] là trong các giai đoạn thị trường bị bóp méo bởi các chương trình mua tài sản của [[Central_Bank|ngân hàng trung ương]]. [extracted] [[Fixed_Income_Alexander_During_Ch21.md#page=1]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch21.md#page=1-2]] — Định nghĩa và vai trò của mô hình ACM trong việc phân dis-aggregate đường cong lợi suất.
