---
title: 'Convexity Adjustment: Futures vs. Forward'
aliases:
- Futures-Forward Basis
- Convexity Bias
- Daily Margining Impact
- Điều chỉnh lồi Futures-Forward
type: mechanism
tags:
- fixed-income
- derivatives
- math
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income (2021)
thesis: The convexity adjustment is a necessary correction applied to money market
  futures rates to derive equivalent forward rates, accounting for the economic benefit
  of daily margin settlement in futures contracts which is absent in forward agreements.
source_refs:
- file: During_Fixed_Income_Ch15.md
  page: 133
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Tại sao không thể dùng trực tiếp lãi suất Futures để định giá Swaps? Alexander Düring bóc tách ranh giới của cơ chế thanh toán (Daily Margining): vì hợp đồng tương lai (Futures) được quyết toán hàng ngày, người giữ vị thế có thể tái đầu tư lợi nhuận ngay lập tức. "Quyền chọn" tái đầu tư này tạo ra một giá trị lồi (**Convexity**) làm cho lãi suất Futures luôn bị đẩy cao hơn lãi suất Forward tương ứng. Nếu bỏ qua bước điều chỉnh này, toàn bộ đường cong lợi suất sẽ bị định giá sai lệch (bias). [[During_Fixed_Income_Ch15.md#page=133]]

---

## 1. Mechanism: The Daily Margining Benefit

Sự khác biệt cốt lõi nằm ở dòng tiền (cash flow timing):
- **Forward Rate Agreement (FRA):** Không có dòng tiền cho đến khi đáo hạn. Rủi ro và lợi nhuận được tích lũy và thanh toán một lần duy nhất.
- **Futures:** Dòng tiền diễn ra hàng ngày (Mark-to-market).
    - Nếu giá tăng, bạn nhận tiền ngay và có thể gửi tiền đó lấy lãi.
    - Nếu giá giảm, bạn phải nộp tiền ngay và mất chi phí lãi vay.
- **The Asymmetry:** Do tính chất lồi của hàm giá trái phiếu, lợi ích từ việc nhận tiền khi giá tăng lớn hơn tổn thất khi phải nộp tiền khi giá giảm (trong môi trường lãi suất biến động). Đây chính là **Convexity Bias**. [[During_Fixed_Income_Ch15.md#page=133]]

---

## 2. Mathematical Approximation

Trong thực tế, mức điều chỉnh convexity ($\gamma$) thường được ước lượng dựa trên biến động của lãi suất ($\sigma$):
$$\text{Rate}_{forward} = \text{Rate}_{futures} - \frac{1}{2} \sigma^2 t_1 t_2$$
- **$t_1$:** Thời gian đến ngày bắt đầu hợp đồng.
- **$t_2$:** Thời gian đến ngày kết thúc hợp đồng.
- **Interpretation:** Mức điều chỉnh tăng dần theo thời gian (kỳ hạn càng xa, convexity càng lớn) và theo độ biến động của thị trường. [[During_Fixed_Income_Ch15.md#page=133]]

---

## 3. Strategic Implications: The "Futures Strip" Trap

Düring cảnh báo các nhà giao dịch:
- **Pricing Bias:** Nếu dùng Futures strip chưa điều chỉnh để xây dựng đường cong, bạn sẽ thấy đường cong forward dốc hơn thực tế. Điều này dẫn đến việc định giá Swaps quá đắt.
- **Hedging:** Khi dùng Futures để hedge một vị thế Forward (hoặc Swap), bạn phải liên tục điều chỉnh tỷ lệ phòng vệ (Hedge ratio) để bù đắp cho sự khác biệt về convexity này, nếu không sẽ xuất hiện rủi ro **Basis Risk**. [[During_Fixed_Income_Ch15.md#page=133]]

---

## Evidence / Source Anchors

- Analysis of daily margining as the source of convexity bias: [[During_Fixed_Income_Ch15.md#page=133]]
- Rationale for the rate gap between futures and forwards: [[During_Fixed_Income_Ch15.md#page=133]]
- Description of the convexity adjustment in the bootstrapping process: [[During_Fixed_Income_Ch15.md#page=133]]
- Identification of volatility ($\sigma$) as the primary driver of the adjustment magnitude: [[During_Fixed_Income_Ch15.md#page=133]]

## Related

- [[Forward_Rates_Derivation]] — Where this adjustment is applied.
- [[Money_Market_Instruments_Mechanics]] — The source of Futures and Forward contracts.
- [[Variation_Margin_Vs_Initial_Margin]] — The operational engine of daily margining.
- [[Yield_Curve_Structure_And_Mechanics]] — The final output after adjustments.
