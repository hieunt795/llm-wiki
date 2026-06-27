---
title: Annuity Formula
aliases:
- Annuity Value
- Welfare Valuation
type: mechanism
tags:
- mathematics
- valuation
- economics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Công thức Annuity dùng để tính giá trị hiện tại (PV) của một chuỗi thanh toán
  cố định trong một khoảng thời gian xác định với một mức lãi suất chiết khấu không
  đổi; nó được Alexander Düring sử dụng để lượng hóa giá trị kinh tế của các chương
  trình phúc lợi xã hội (như NHS tại Anh) dưới góc độ một tài sản tài chính.
source_refs:
- file: Fixed_Income_Alexander_During_Ch02.md
  page: 6
created: '2026-04-13'
updated: '2026-04-22'
---

# [[Annuity_Formula]]

## Mechanism

Công thức annuity cho phép tính **present value** của một chuỗi thanh toán cố định trong một khoảng thời gian nhất định, dùng một discount rate cố định. [extracted] [[Fixed_Income_Alexander_During_Ch02.md#page=6]]

Dạng tổng quát (sẽ được trình bày chi tiết trong Equation 16.1): [extracted] [[Fixed_Income_Alexander_During_Ch02.md#page=6]]

$$PV = C \times \frac{1 - (1+r)^{-n}}{r}$$

Trong đó:
- $C$ = [[Cash]] flow mỗi kỳ
- $r$ = Discount rate
- $n$ = Số kỳ

### Điều kiện

- Discount rate phải được xác định trước (trong ví dụ: long-term yield 1.8%)
- Thanh toán đều đặn, cùng giá trị mỗi kỳ
- Không tính inflation adjustment

### Ví dụ số

**NHS (UK) - 2015/16:**
- Ngân sách NHS: £116.4bn → £1,800/người/năm
- Tuổi thọ trung bình còn lại: 30 năm
- Discount rate: 1.8% (long-term yield thời điểm đó)
- Present value tương đương: **£41,400** per person

→ Mỗi cư dân đăng ký NHS thực chất "sở hữu" một tài sản tương đương £41,400. [extracted] [[Fixed_Income_Alexander_During_Ch02.md#page=6]]

**Germany welfare - 2017:**
- Stipend: €409/tháng cho người độc thân không phụ thuộc
- 30 year annuity tại lãi suất hiện hành → PV = **€127,000**

→ Một người cần tích lũy €127,000 để đạt thu nhập tương đương nếu không có welfare. [extracted] [[Fixed_Income_Alexander_During_Ch02.md#page=7]]

## Evidence / Source Anchors

- [[Fixed_Income_Alexander_During_Ch02.md#page=6]] — Ví dụ NHS
- [[Fixed_Income_Alexander_During_Ch02.md#page=7]] — Ví dụ Germany welfare
