---
title: Macaulay Duration
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
thesis: '[RAW] Neftci tiếp cận Macaulay Duration ($D_{mac}$) không chỉ là thước đo
  thời gian, mà là một phép biến đổi tuyến tính giúp hiểu về độ nhạy của một gói dòng
  tiền (bundle of cash flows).'
source_refs:
  - file: Principles_of_Financial_Engineering_Neftci.md
    page: 85
  - file: Fixed_Income_Alexander_During_Ch02.md
    page: 13
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 1902-1948
created: '2026-04-21'
updated: '2026-04-21'
---

﻿---
title: "Macaulay Duration"
aliases: [Mac Duration, Thời lượng Macaulay]
type: definition
tags: [fixed-income, risk-measures]
status: active
confidence: 5
expert_lens: "Alexander During | Salih Neftci"
provenance: "Principles_of_Financial_Engineering_Neftci.md"
thesis: "Macaulay Duration is the weighted average time until a bond's cash flows are received, serving as the temporal 'center of gravity' for a series of fixed payments."
source_refs:
  - file: "Principles_of_Financial_Engineering_Neftci.md"
    page: 85
  - file: "Fixed_Income_Alexander_During_Ch02.md"
    page: 13
created: 2026-04-13
updated: 2026-04-21
---

## Thesis
[RAW] Neftci tiếp cận Macaulay Duration ($D_{mac}$) không chỉ là thước đo thời gian, mà là một phép biến đổi tuyến tính giúp hiểu về độ nhạy của một gói dòng tiền (bundle of cash flows).

## 1. Definition & Mechanism
$D_{mac}$ được tính bằng cách lấy tổng thời gian của mỗi dòng tiền, nhân với tỷ trọng giá trị hiện tại của dòng tiền đó trong tổng giá trị trái phiếu:
$$D_{mac} = \sum_{i=1}^{n} \frac{t_i \cdot PV(CF_i)}{P}$$
Trong đó:
- $t_i$: Thời gian nhận dòng tiền $i$.
- $PV(CF_i)$: Giá trị hiện tại của dòng tiền $i$ chiết khấu bằng lợi suất $y$.
- $P$: Giá thị trường của trái phiếu ($\sum PV(CF_i)$).

### Ý nghĩa kinh tế
[RAW] Đối với Neftci, $D_{mac}$ là "điểm cân bằng" (center of gravity) của các dòng tiền.
- Đối với trái phiếu không trả lãi định kỳ (zero-coupon bond), $D_{mac}$ chính bằng thời gian đáo hạn.
- Đối với trái phiếu có coupon, $D_{mac}$ luôn nhỏ hơn thời gian đáo hạn vì nhà đầu tư nhận lại một phần vốn sớm hơn thông qua các kỳ trả lãi.

## 2. Worked Example (Neftci)
[RAW] Xét một trái phiếu 2 năm, mệnh giá 100, coupon 10% trả hàng năm, lợi suất thị trường 10%.
- **Dòng tiền 1 (Năm 1):** Coupon 10. $PV = 10 / 1.1 = 9.09$.
- **Dòng tiền 2 (Năm 2):** Coupon 10 + Gốc 100. $PV = 110 / (1.1)^2 = 90.91$.
- **Giá trái phiếu (P):** $9.09 + 90.91 = 100$.
- **Tỷ trọng (w):** $w_1 = 0.0909$, $w_2 = 0.9091$.
- **Macaulay Duration:** $D_{mac} = (1 \times 0.0909) + (2 \times 0.9091) = 1.909$ năm.

## 3. Failure Conditions / Boundaries
- **Flat Yield Curve Assumption:** Công thức truyền thống giả định mọi dòng tiền được chiết khấu bằng một lợi suất duy nhất $y$ (đường cong lãi suất phẳng). Trong thực tế, mỗi dòng tiền nên được chiết khấu bằng lãi suất zero-coupon tương ứng với kỳ hạn của nó.
- **Not a Risk Measure:** $D_{mac}$ tự thân nó là thước đo thời gian (năm), không trực tiếp cho biết giá thay đổi bao nhiêu % khi lãi suất biến động. Để đo lường rủi ro giá, phải sử dụng [[Modified_Duration]].

## Related
- [[Modified_Duration]] — Công thức biến đổi trực tiếp sang độ nhạy giá.
- [[Convexity]] — Thước đo sai số bậc hai của Duration.
- [[Yield_Curve_Structure_And_Mechanics]] — Cơ sở để chiết khấu dòng tiền.
- [[Immunization]] — Chiến lược khớp duration để phòng vệ danh mục.
