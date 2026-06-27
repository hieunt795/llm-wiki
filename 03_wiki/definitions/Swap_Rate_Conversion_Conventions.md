---
title: Swap Rate Conversion Conventions
aliases:
- Annual Bond to Annual Money
- Payment Frequency Conversion
- Swap Rate Approximation
- Quy ước chuyển đổi lãi suất Swap
type: definition
tags:
- derivatives
- math
- conventions
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Howard Corb"
provenance: Howard Corb - Swaps and Derivatives (2012)
thesis: Swap rate conversion involves adjusting for different payment frequencies
  (compounding) and day count bases (bond vs. money), where minor technical errors
  in calculation can lead to significant present value losses in large-notional contracts.
source_refs:
- file: Howard_Corb_Swaps.md
  page: 15
- file: Howard_Corb_Swaps.md
  page: 16
- file: Howard_Corb_Swaps.md
  page: 17
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Trong thị trường Swaps, "một con số" lãi suất có thể mang nhiều ý nghĩa khác nhau tùy thuộc vào quy ước thanh toán. Howard Corb bóc tách ranh giới của việc chuyển đổi: một lỗi sai chỉ 2 điểm cơ bản (bps) do nhầm lẫn giữa chuẩn Bond (365 ngày) và chuẩn Money (360 ngày) có thể gây ra tổn thất hàng trăm nghìn USD trên một hợp đồng tiêu chuẩn. Việc nắm vững các công thức xấp xỉ (approximations) là mỏ neo để kiểm tra tính hợp lý của các mô hình định giá phức tạp. [[Howard_Corb_Swaps.md#page=17]]

---

## 1. Frequency Conversion (Bond Basis)

Khi thay đổi tần suất trả lãi (ví dụ từ Semi-annual sang Annual) trên cùng một chuẩn ngày (Bond basis), lãi suất phải được điều chỉnh để bù đắp cho hiệu ứng lãi kép:
$$s_{ab} \approx \left[ \left(1 + \frac{s_{sb}}{2}\right)^2 - 1 \right]$$
- **Intuition:** Người nhận lãi hàng năm ($s_{ab}$) không có cơ hội tái đầu tư coupon sau mỗi 6 tháng như người nhận lãi bán niên ($s_{sb}$), do đó lãi suất hàng năm phải **cao hơn** để bù đắp. [[Howard_Corb_Swaps.md#page=15]]

**Công thức tổng quát:**
$$s_{yb} \approx y \times \left[ \left(1 + \frac{s_{xb}}{x}\right)^{x/y} - 1 \right]$$
- **$x, y$:** Tần suất thanh toán mỗi năm.

---

## 2. Day Count Basis Conversion (Bond vs. Money)

Ranh giới giữa việc tính toán theo 365 ngày (Bond) và 360 ngày (Money):
- **Annual Money Rate ($s_{am}$):** Luôn thấp hơn lãi suất Bond tương ứng vì người nhận lãi được hưởng lợi từ việc dồn tích thêm 5-6 ngày mỗi năm.
- **Approximation:**
$$s_{am} \approx \frac{360}{365} \times s_{ab}$$
[[Howard_Corb_Swaps.md#page=16]]

---

## 3. Strategic Implications: The Pricing Mistake

Corb giải mã rủi ro vận hành (Operational Risk):
- **The $365,000 Error:** Đối với một hợp đồng $100mm kỳ hạn 30 năm, việc nhầm lẫn giữa mức 3.583% (semi bond) và 3.563% (annual money) dẫn đến sai lệch PV xấp xỉ $365,000.
- **Verification:** Các nhà giao dịch chuyên nghiệp luôn sử dụng các công thức xấp xỉ này để "sanity check" (kiểm tra tính hợp lý) các báo giá từ hệ thống trước khi ký xác nhận (confirmation). [[Howard_Corb_Swaps.md#page=16]]

---

## Evidence / Source Anchors

- Analysis of the reinvestment opportunity cost in payment frequency: [[Howard_Corb_Swaps.md#page=15]]
- Mathematical derivation of the 360/365 day count adjustment: [[Howard_Corb_Swaps.md#page=16]]
- Case study of a 2bps error on a 30-year swap contract: [[Howard_Corb_Swaps.md#page=16]]
- Generalization of frequency conversion for arbitrary payment cycles: [[Howard_Corb_Swaps.md#page=17]]

## Related

- [[Interest_Rate_Swap_Plain_Vanilla]] — The context for these conversions.
- [[Daycount_Conventions]] — The underlying rules for time measurement.
- [[Bond_Pricing_Conventions]] — Comparative rules in the cash market.
- [[Yield_Curve_Structure_And_Mechanics]] — How these rates are used to build the curve.
- [[Conversion_Factor_And_Notional_Coupon]]
- [[Interest_Rate_Swap_Engineering]]
