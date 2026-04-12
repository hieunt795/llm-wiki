---
type: mechanism
trigger: "Cần tính present value của dòng thanh toán cố định"
output: "Giá trị hiện tại tương đương của annuity"
constraints: ["Giả định discount rate không đổi", "Thanh toán đều đặn"]
sources: ["Fixed Income - Alexander During-2.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 1
---

# Annuity Formula

## Cơ chế

Công thức annuity cho phép tính **present value** của một chuỗi thanh toán cố định trong một khoảng thời gian nhất định, dùng một discount rate cố định. [extracted] [[Fixed Income - Alexander During-2.pdf#page=6]]

Dạng tổng quát (sẽ được trình bày chi tiết trong Equation 16.1): [extracted] [[Fixed Income - Alexander During-2.pdf#page=6]]

$$PV = C \times \frac{1 - (1+r)^{-n}}{r}$$

Trong đó:
- $C$ = Cash flow mỗi kỳ
- $r$ = Discount rate
- $n$ = Số kỳ

## Điều kiện

- Discount rate phải được xác định trước (trong ví dụ: long-term yield 1.8%)
- Thanh toán đều đặn, cùng giá trị mỗi kỳ
- Không tính inflation adjustment

## Ví dụ số

**NHS (UK) - 2015/16:**
- Ngân sách NHS: £116.4bn → £1,800/người/năm
- Tuổi thọ trung bình còn lại: 30 năm
- Discount rate: 1.8% (long-term yield thời điểm đó)
- Present value tương đương: **£41,400** per person

→ Mỗi cư dân đăng ký NHS thực chất "sở hữu" một tài sản tương đương £41,400. [extracted] [[Fixed Income - Alexander During-2.pdf#page=6]]

**Germany welfare - 2017:**
- Stipend: €409/tháng cho người độc thân không phụ thuộc
- 30 year annuity tại lãi suất hiện hành → PV = **€127,000**

→ Một người cần tích lũy €127,000 để đạt thu nhập tương đương nếu không có welfare. [extracted] [[Fixed Income - Alexander During-2.pdf#page=7]]

## Nguồn

- [[Fixed Income - Alexander During-2.pdf#page=6]] — Ví dụ NHS
- [[Fixed Income - Alexander During-2.pdf#page=7]] — Ví dụ Germany welfare
