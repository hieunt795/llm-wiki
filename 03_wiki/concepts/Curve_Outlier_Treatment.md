---
title: Curve Outlier Treatment
aliases:
- Outlier removal
- Distorted prices
- Benchmark distortion
type: concept
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch20.md"
thesis: 'Trong quá trình xây dựng đường cong, việc có các mức giá không đại diện (polluted/[[Curve_Outlier_Treatment|distorted
  prices]]) có thể làm chệch toàn bộ cấu trúc lãi thuật. Có hai chiến lược chính để
  xử lý vấn đề này: loại bỏ theo thống kê và loại bỏ theo đặc tính công cụ. [extracted]
  [[Fixed_Income'
source_refs:
- file: Fixed_Income_Alexander_During_Ch20.md
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
chapter: 19
---

# Curve Outlier Treatment

## Mechanism

Trong quá trình xây dựng đường cong, việc có các mức giá không đại diện (polluted/[[Curve_Outlier_Treatment|distorted prices]]) có thể làm chệch toàn bộ cấu trúc lãi thuật. Có hai chiến lược chính để xử lý vấn đề này: loại bỏ theo thống kê và loại bỏ theo đặc tính công cụ. [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=16]]

### 1. Loại bỏ theo thống kê (Outlier Removal)
Hệ thống sẽ thực hiện khớp hàm sơ bộ, sau đó đánh giá độ lệch (spread) của từng trái phiếu so với đường cong mô hình.
- **Cơ chế:** Các trái phiếu có mức lệch vượt quá một ngưỡng nhất định (ví dụ: số lần độ lệch chuẩn $k\sigma$) sẽ bị loại bỏ và quy trình hiệu chuẩn được thực hiện lại cho đến khi mẫu dữ liệu ổn định.
- **Rủi ro:** Việc loại bỏ liên tục có thể khiến các đường cong giữa các ngày khác nhau bị mất tính nhất quán do thành phần mẫu thay đổi (sample change bias). [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=16]]

### 2. Loại bỏ các công cụ bị méo mó giá (Distorted Benchmarks)
Một số trái phiếu "chuẩn" (Benchmarks) hoặc các trái phiếu dễ giao chuyển nhất (CTDs) thường có giá bị méo do phần bù thanh khoản (liquidity premia) hoặc sự khan hiếm trên thị trường [[Repurchase_Agreement|repo]].
- **Tranh luận:**
    - *Phe ủng hộ loại bỏ:* Cho rằng các trái phiếu này không đại diện cho cấu trúc chiết khấu "thuần túy".
    - *Phe phản đối:* Lập luận rằng chính những trái phiếu này mới là những công cụ phản ứng nhạy bén nhất với các yếu tố kinh tế. Việc loại bỏ chúng có thể dẫn đến một đường cong "lười biếng" không phản ánh đúng diễn biến thị trường thực. [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=16]]

### Kết luận
Cách tiếp cận trung dung là giữ lại toàn bộ mẫu nhưng thực hiện xác minh thủ công đối với các điểm dị biệt, thay vì để thuật toán tự động loại bỏ một cách máy móc. [extracted] [[Fixed_Income_Alexander_During_Ch20.md#page=16]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch20.md#page=16]] — Chiến lược xử lý Outliers, tác động của Benchmark premium lên hiệu chuẩn đường cong.
