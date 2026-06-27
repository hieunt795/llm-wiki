---
title: Caps and Floors
aliases:
- Interest Rate Cap
- Interest Rate Floor
- Caplet
- Floorlet
- Cap-Floor Parity
- Collar
type: concept
tags:
- derivatives
- fixed-income
- hedging
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Howard Corb"
provenance: Multi-source (Corb)
thesis: Interest rate caps and floors are portfolios of European options (caplets/floorlets)
  on a reference interest rate, typically LIBOR, providing protection against rising
  or falling rates respectively.
source_refs:
- file: Howard_Corb_Swaps.md
  page: 135
- file: Howard_Corb_Swaps.md
  page: 137
- file: Howard_Corb_Swaps.md
  page: 143
created: '2026-04-20'
updated: '2026-04-22'
---

## Thesis

Caps and Floors là các công cụ phái sinh lãi suất phi tuyến tính chủ chốt. Howard Corb bóc tách cấu trúc của chúng không phải như một quyền chọn đơn lẻ, mà là một **danh mục các caplets/floorlets**. Ranh giới kỹ thuật quan trọng nhất là tính chất tương quan giữa Caps, Floors và Swaps thông qua **Cap-Floor Parity**, cho phép các Dealer hoán đổi rủi ro giữa các thị trường này một cách cơ học. [[Howard_Corb_Swaps.md#page=135]]

---

## 1. Structural Definition

- **Cap:** Một quyền chọn mua (call) trên lãi suất. Người mua nhận được thanh toán nếu lãi suất tham chiếu (ví dụ: 3M LIBOR) vượt quá mức Strike.
  - Payout formula: $\text{max}(L - K, 0)$
- **Floor:** Một quyền chọn bán (put) trên lãi suất. Người mua nhận được thanh toán nếu lãi suất tham chiếu thấp hơn mức Strike.
  - Payout formula: $\text{max}(K - L, 0)$
- **Caplets/Floorlets:** Các thành phần riêng lẻ trong một chuỗi quyền chọn. Một Cap 5 năm trên 3M LIBOR thực chất là một danh mục gồm ~19-20 caplets. [[Howard_Corb_Swaps.md#page=136]]

---

## 2. Technical Mechanics: Cap-Floor Parity

Howard Corb thiết lập một ranh giới toán học (tương tự put-call parity trong equities):
$$\text{Value of Cap} - \text{Value of Floor} = \text{Value of Paying Fixed in Swap}$$
*(Với điều kiện cùng Strike, cùng kỳ hạn và cùng lịch reset)*

- **Parity Logic:** Việc long một cap và short một floor cùng strike $K$ tương đương về mặt kinh tế với việc trả lãi suất cố định $K$ trong một hợp đồng Swap.
- **ATM Strike:** Nếu một Cap và một Floor có giá trị bằng nhau tại thời điểm định giá, thì Strike đó chính là **Par swap rate** cho kỳ hạn tương ứng. [[Howard_Corb_Swaps.md#page=137]]

---

## 3. Valuation: The Black Model

Mô hình tiêu chuẩn (Industry Standard) để định giá từng caplet/floorlet là công thức Black:
- **Caplet Price:**
  $$\tau \cdot DF(0, t_{i+1}) \cdot [f(t_i, t_{i+1})N(d_1) - KN(d_2)]$$
- **Key Observation:** Có một khoảng trễ (payment lag) giữa thời điểm reset lãi suất ($t_i$) và thời điểm thanh toán thực tế ($t_{i+1}$). Mô hình Black tích hợp điều này bằng cách chiết khấu từ $t_{i+1}$. [[Howard_Corb_Swaps.md#page=143]]

---

## 4. Howard Corb (Columbia) Perspective: The Humped Vol Curve

Corb giải mã hình thái của đường cong biến động (Volatility Curve) trong thị trường Caps/Floors:
- **Base Vol vs. Average Vol:** Dealer thường sử dụng base vol cho từng caplet riêng lẻ, nhưng thị trường quote theo **Average Vol** (biến động trung bình cho toàn bộ kỳ hạn).
- **The "Hump" Shape:** Đường cong Vol thường dốc lên ở các kỳ hạn ngắn và dốc xuống ở các kỳ hạn dài.
  - **Lý giải:** Sự không chắc chắn ban đầu tăng lên do các cú sốc kinh tế và chính sách của Fed (làm Vol tăng). Tuy nhiên, về dài hạn, lãi suất có tính chất **Mean Reversion** (quay trở lại giá trị trung bình), làm giảm sự biến động kỳ vọng ở các kỳ hạn rất dài. [[Howard_Corb_Swaps.md#page=145]]

---

## Evidence / Source Anchors

- Definition of caps/floors and their payoff formulas: [[Howard_Corb_Swaps.md#page=135]]
- Mathematical derivation of Cap-Floor Parity: [[Howard_Corb_Swaps.md#page=137]]
- Use of Black's formula for individual caplet valuation: [[Howard_Corb_Swaps.md#page=143]]
- Analysis of the "humped" base vol curve and mean reversion: [[Howard_Corb_Swaps.md#page=145]]

## Related

- [[Interest_Rate_Swap_Plain_Vanilla]] — The linear counterpart to caps/floors.
- [[Swaptions]] — Options on the swap itself rather than individual rates.
- [[Negative_Convexity]] — Relevant for capped floaters.
- [[Interest_Rate_Option_Models]] — Black Model vs Normal Model discussion.
