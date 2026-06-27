---
title: Forward Rates Derivation
aliases:
- Forward Rate Calculation
- Futures Strip Bootstrapping
- Cash Stub Rate
- Lãi suất kỳ hạn
type: mechanism
tags:
- fixed-income
- math
- yield-curves
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income (2021)
thesis: The derivation of forward rates is a recursive process of 'stitching' together
  market instruments—starting from the overnight cash stub and extending through the
  futures strip—to create a continuous term structure consistent with the principle
  of no-arbitrage.
source_refs:
- file: During_Fixed_Income_Ch15.md
  page: 132
- file: During_Fixed_Income_Ch15.md
  page: 133
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Làm sao để biết lãi suất 3 tháng của 2 năm sau là bao nhiêu? Alexander Düring bóc tách ranh giới của việc "nối gối" (stitching): lãi suất kỳ hạn (Forward rate) không phải là một dự báo chủ quan, mà là một hệ quả toán học từ các tài sản đang được giao dịch hôm nay. Bằng cách sử dụng quy trình đệ quy từ tiền mặt ngắn hạn (Stub) đến dải hợp đồng tương lai (Futures Strip), chúng ta có thể dựng lên một lộ trình lãi suất đầy đủ cho tương lai. [[During_Fixed_Income_Ch15.md#page=132]]

---

## 1. The Recursive Anchor: Cash Stub to Futures

Để xây dựng đường cong, thị trường không lấy tất cả dữ liệu từ một nguồn. Quy trình diễn ra như sau:

### Step 1: The Cash Stub
Điểm bắt đầu của đường cong là **Cash Stub** (lãi suất tiền mặt). Đây là lãi suất giao ngay từ hôm nay cho đến ngày đáo hạn của hợp đồng tương lai (Futures) gần nhất.

### Step 2: The Futures Strip extension
Từ mốc đó trở đi, chúng ta sử dụng lãi suất ngụ ý từ các hợp đồng tương lai (ví dụ Euribor 3M Futures). Công thức đệ quy mỏ neo:
$$1 + r(0, t_{i+1}) \times \text{DCF}(0, t_{i+1}) = (1 + r(0, t_i) \times \text{DCF}(0, t_i)) \times (1 + r_{fwd}(t_i, t_{i+1}) \times \text{DCF}(t_i, t_{i+1}))$$
- **Mechanism:** Lãi suất giao ngay kỳ hạn tiếp theo bằng tích của lãi suất giao ngay kỳ hạn trước và lãi suất kỳ hạn (forward) tương ứng. [[During_Fixed_Income_Ch15.md#page=133]]

---

## 2. Technical Boundary: The Convexity Adjustment

Düring vạch rõ một sai lầm phổ biến: **Lãi suất Futures không bằng lãi suất Forward.**
- **The Gap:** $r_{fwd} = r_{futures} - \text{Convexity Adjustment}$.
- **Reason:** Hợp đồng tương lai được ký quỹ hàng ngày (Daily Margining), trong khi Forward chỉ thanh toán một lần khi đáo hạn. Hiệu ứng lãi kép của việc tái đầu tư ký quỹ tạo ra một lợi thế (convexity) cho người giữ Futures, khiến lãi suất Futures luôn cao hơn Forward tương ứng.
- **Requirement:** Trước khi đưa vào quy trình đệ quy ở Step 2, lãi suất Futures phải được điều chỉnh giảm đi một lượng Convexity Adjustment. [[During_Fixed_Income_Ch15.md#page=133]]

---

## 3. Strategic Implications: No-Arbitrage Pricing

Mọi định giá trái phiếu và Swaps đều phụ thuộc vào độ chính xác của quy trình Derivation này:
- Nếu quy trình nối gối (stitching) không mượt mà, sẽ xuất hiện các "nhát cắt" (kinks) trên đường cong Forward, tạo ra các cơ hội Arbitrage giả (do lỗi mô hình).
- **Turn Premium Adjustment:** Phải điều chỉnh các điểm forward đi qua các mốc cuối năm tài chính để tránh việc "Turn premium" làm méo mó kỳ vọng lãi suất chính sách thực tế. [[During_Fixed_Income_Ch15.md#page=134]]

---

## Evidence / Source Anchors

- Mathematical recursive identity for spot rate construction (Equation 15.7): [[During_Fixed_Income_Ch15.md#page=133]]
- Analysis of the cash stub as the foundation of the curve: [[During_Fixed_Income_Ch15.md#page=132]]
- Description of the convexity adjustment necessity for futures-implied rates: [[During_Fixed_Income_Ch15.md#page=133]]
- Rationale for using simple yields vs. discount rates in derivation: [[During_Fixed_Income_Ch15.md#page=132]]

## Related

- [[Yield_Curve_Structure_And_Mechanics]] — The output of this derivation process.
- [[Convexity_Adjustment_Futures_Vs_Forward]] — Detailed math of the adjustment.
- [[Money_Market_Instruments_Mechanics]] — The source of the Stub and Futures rates.
- [[Repurchase_Agreement_Mechanism]] — The funding rate used to verify no-arbitrage.
