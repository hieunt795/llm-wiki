---
title: Bermudan Swaptions
aliases:
- Multi-European Swaption
- Bermudan Option on Swap
- Optimal Exercise of Bermudan Swaptions
type: concept
tags:
- derivatives
- swaptions
- exotic-options
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Howard Corb"
provenance: Howard_Corb_Swaps.md
thesis: A Bermudan swaption provides the holder with multiple discrete exercise dates,
  making it an 'exotic' instrument whose value depends on the path of interest rates
  and the complex trade-off between immediate exercise and the preservation of remaining
  optionality.
source_refs:
- file: Howard_Corb_Swaps.md
  page: 209
- file: Howard_Corb_Swaps.md
  page: 211
- file: Howard_Corb_Swaps.md
  page: 217
created: '2026-04-20'
updated: '2026-04-22'
---

## Thesis

Bermudan Swaptions là một trong những công cụ phái sinh "exotic" phổ biến nhất. Howard Corb bóc tách ranh giới định giá của nó không chỉ qua toán học mà qua **trading logic**: Một quyền chọn Bermudan phải luôn đáng giá ít nhất bằng bất kỳ quyền chọn European đơn lẻ nào cấu thành nên nó. Sự phức tạp nằm ở việc quyết định thực hiện quyền sớm (early exercise), nơi Trader phải so sánh giá trị của việc bước vào Swap ngay lập tức với giá trị của các quyền chọn còn lại trong tương lai. [[Howard_Corb_Swaps.md#page=209]]

---

## 1. Structural Definition

- **Mechanism:** Khác với European swaption (chỉ thực hiện 1 lần vào ngày đáo hạn), Bermudan swaption cho phép thực hiện quyền tại một chuỗi các ngày rời rạc (ví dụ: mỗi 6 tháng).
- **Physical Reality:** Một khi đã thực hiện quyền (Exercise), các quyền chọn còn lại trong chuỗi sẽ biến mất. Nhà đầu tư bước vào phần còn lại (remaining term) của hợp đồng Swap gốc.
- **Lower Bound:** Giá trị của Bermudan Swaption $\geq \text{max}(\text{Value of all constituent Europeans})$. [[Howard_Corb_Swaps.md#page=209]]

---

## 2. Optimal Exercise Strategy

Howard Corb giải mã bài toán quyết định tại mỗi ngày reset:
- **Immediate Exercise Value:** Giá trị MTM của việc bước vào hợp đồng Swap ngay bây giờ.
- **Continuation Value:** Giá trị của "residual options" (các quyền chọn còn lại trong chuỗi).
- **The Decision:** Chỉ thực hiện quyền nếu **Exercise Value > Continuation Value**.
  - Ranh giới kỹ thuật: Ngay cả khi Swap đang "in-the-money", Trader có thể chọn **không thực hiện quyền** nếu biến động kỳ vọng cao, khiến giá trị của việc giữ lại quyền chọn (time value) lớn hơn lợi ích từ việc nhận Swap ngay. [[Howard_Corb_Swaps.md#page=211]]

---

## 3. Valuation Complexity

Howard Corb nhấn mạnh rằng Bermudan Swaptions không thể định giá bằng công thức Black đơn giản:
- **Path Dependency:** Giá trị của nó phụ thuộc vào lộ trình của lãi suất.
- **Model Standard:** Cần các mô hình phức tạp như **Multi-Factor LIBOR Market Model** hoặc **Stochastic Volatility Models** để nắm bắt sự tương quan giữa các điểm trên đường cong lãi suất.
- **Heuristic Pricing (Zhou 2003):** Có thể xấp xỉ giá trị Bermudan bằng một danh mục các European Swaptions với các Strike khác nhau để nắm bắt xác suất thực hiện quyền tại mỗi thời điểm. [[Howard_Corb_Swaps.md#page=217-220]]

---

## 4. Howard Corb Perspective: Relationship with Skew

Corb chỉ ra rằng định giá Bermudan Swaption cực kỳ nhạy cảm với **Volatility Skew**:
- Vì Bermudan Swaption bao gồm nhiều quyền chọn với các ngày đáo hạn khác nhau, sự thay đổi của hình thái Skew (độ dốc của Volatility theo Strike) sẽ làm thay đổi giá trị của Continuation Value tại mỗi bước, ảnh hưởng trực tiếp đến ranh giới thực hiện quyền tối ưu. [[Howard_Corb_Swaps.md#page=217]]

---

## Evidence / Source Anchors

- Definition of Bermudan swaption and lower bound logic: [[Howard_Corb_Swaps.md#page=209]]
- Optimal exercise decision (Exercise vs. Continuation value): [[Howard_Corb_Swaps.md#page=211]]
- Complexity of valuation and limitations of Black's formula: [[Howard_Corb_Swaps.md#page=217]]
- Analysis of early exercise in different volatility environments: [[Howard_Corb_Swaps.md#page=214]]

## Related

- [[Swaptions]] — The European version of this instrument.
- [[Interest_Rate_Option_Models]] — The models used to estimate continuation value.
- [[Cancelable_Swaps]] — The most common application of Bermudan swaptions.
- [[Path_Dependency_In_Derivatives]] — The technical category of this instrument.
