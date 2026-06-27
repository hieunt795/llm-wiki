---
title: Discount Margin Vs Simple Interest
aliases:
- Simple Interest Method
- Discount Margin Method
type: mechanism
tags: []
status: reviewed
confidence: 4
half_life_years: 10
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch14.md"
thesis: Thị trường tiền tệ có hai cách chính để niêm yết giá và lãi suất của công
  cụ.
source_refs:
- '[[Fixed_Income_Alexander_During_Ch14.md#page=5]]'
created: '2026-04-16'
updated: '2026-04-28'
chapter: 13
---

# Discount Margin vs Simple Interest Methods

## Convention
Thị trường tiền tệ có hai cách chính để niêm yết giá và lãi suất của công cụ.

### 1. Simple Interest Method (Phổ biến nhất)
Giá được tính bằng cách lấy giá trị hoàn trả (redemption) chiết khấu ngược lại theo lãi suất $r$ và [[Daycount_Conventions|daycount fraction]] (DCF).

- **Công thức tính Giá (P)**:
$$P = \frac{100}{1 + r \times DCF}$$
- **Lãi suất tính từ giá**:
$$r = \left(\frac{100}{P} - 1\right) / DCF$$

[extracted] [[Fixed_Income_Alexander_During_Ch14.md#page=5]]

### 2. Discount Margin Method (Chuẩn US T-bill)
Phương pháp này coi lãi suất như một số tiền chiết khấu (discount amount) được trừ thẳng vào mệnh giá.

- **Công thức tính Giá (P)**:
$$P = 100 - r \times DCF$$
- **Lãi suất tính từ giá**:
$$r = \frac{100 - P}{DCF}$$

[extracted] [[Fixed_Income_Alexander_During_Ch14.md#page=5]]

## Mechanism
Đây là ví dụ điển hình cho việc **quy ước sinh ra từ sự tiện lợi**. 
- Phương pháp Simple Interest đòi hỏi phép chia ($100 / (1 + r \times DCF)$), vốn rất khó thực hiện chính xác bằng Thước trượt Loga (Slide rule) hoặc tính nhẩm.
- Phương pháp Discount Margin chỉ đòi hỏi phép nhân và trừ ($100 - r \times DCF$), cực kỳ dễ dàng cho các trader thời chưa có máy tính điện tử.
[extracted] [[Fixed_Income_Alexander_During_Ch14.md#page=5]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_14.pdf#page=5]] - So sánh hai phương pháp niêm yết.


## Related

- [[Discount_Margin_Mechanism]]
- [[Interest_Rate_Risk]]
- [[Wicksellian_Natural_Interest_Rate]]
- [[Bond_Pricing_And_Accrued_Interest_Conventions]]
- [[Mathematical_Conventions_Of_Interest_Accrual]]
- [[Interest_Rate_Parity]]
- [[Interest_Rate_Swap_Plain_Vanilla]]
- [[Usury_And_Interest_Prohibition]]
- [[Discount_Factors_Theory]]
- [[Discount_Window_Mechanism]]
- [[Forward_Discount_Factor_No_Arbitrage_Math]]
- [[Interest_Indexed_Bonds]]
- [[Compound_Interest_Mechanics]]
- [[Compound_Interest_Time_Value]]
- [[Interest_Rate_Options_Schofield]]
- [[Interest_Rate_Swap_IRS]]
