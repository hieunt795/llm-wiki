---
title: Swaptions
aliases:
- Interest Rate Swaption
- Payer Swaption
- Receiver Swaption
- Swaption Parity
- ATMF Swaption
type: concept
tags:
- derivatives
- swaptions
- hedging
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Howard Corb"
provenance: Multi-source (Corb)
thesis: A swaption is an option to enter into an interest rate swap, providing the
  holder with the right to pay or receive fixed in a future swap of a specified term
  and strike.
source_refs:
- file: Howard_Corb_Swaps.md
  page: 166
- file: Howard_Corb_Swaps.md
  page: 169
- file: Howard_Corb_Swaps.md
  page: 173
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 4979-5010
  section: "Chapter 6.3.4: Conditional Curve Trades using Swaptions"
created: '2026-04-20'
updated: '2026-05-07'
---

## Thesis

Swaptions (Swap Options) là cầu nối giữa rủi ro lãi suất tuyến tính (swaps) và phi tuyến tính (options). Howard Corb bóc tách swaptions qua lăng kính của cả **trường phái Black (Lognormal)** truyền thống và **trường phái Normal** hiện đại. Ranh giới kỹ thuật quan trọng nhất là mối liên hệ giữa Payer và Receiver swaptions thông qua **Swaption Parity**, tương tự như Cap-Floor Parity nhưng áp dụng cho toàn bộ kỳ hạn của Swap. [[Howard_Corb_Swaps.md#page=166]]

---

## 1. Structural Typology

- **Payer Swaption (Put Swaption):** Quyền được trả lãi suất cố định ($X$) và nhận lãi suất nổi. Đây là một công cụ **Bearish** (có giá trị khi lãi suất tăng).
- **Receiver Swaption (Call Swaption):** Quyền được nhận lãi suất cố định ($X$) và trả lãi suất nổi. Đây là một công cụ **Bullish** (có giá trị khi lãi suất giảm).
- **Settlement:**
  - **Physical Settlement:** Bên thực hiện quyền sẽ thực sự bước vào một hợp đồng Swap.
  - **Cash Settlement:** Thanh toán giá trị MTM của Swap tại ngày thực hiện quyền (Industry Standard). [[Howard_Corb_Swaps.md#page=167]]

---

## 2. Technical Mechanics: Swaption Parity

Howard Corb thiết lập ranh giới định giá liên kết:
$$\text{Value of Receiver} - \text{Value of Payer} = \text{Value of Receiving Fixed in Forward Swap}$$
*(Với cùng Strike $X$, cùng Expiry $T$, và cùng underlying swap tail $n$)*

- **Logic:** Một danh mục Long Receiver và Short Payer cùng strike tạo ra dòng tiền giống hệt như một Forward Starting Swap.
- **ATM Forward Strike:** Khi $Receiver = Payer$, thì Strike $X$ chính là **Forward swap rate** ($F$) hiện hành. [[Howard_Corb_Swaps.md#page=169]]

---

## 3. Valuation: Black vs. Normal Models

### A. The Black Model (Lognormal)
Giả định lãi suất Forward ($F$) phân phối lognormal.
- **Payer Price:** $A \cdot [F N(d_1) - X N(d_2)]$
- **Annuity Factor ($A$):** Tổng giá trị hiện tại của một chuỗi $1/m$ đô la thanh toán mỗi năm trong suốt kỳ hạn của Swap. Đây là thành phần quan trọng nhất tạo ra đòn bẩy cho Swaption. [[Howard_Corb_Swaps.md#page=173]]

### B. The Normal Model (Absolute Vol)
Giả định lãi suất phân phối normal (phổ biến hơn trong môi trường lãi suất thấp/âm).
- **Straddle Price (ATM):** $Value \approx \sqrt{T} \cdot 0.8 \cdot \sigma_N \cdot A$
- **Ưu điểm:** Normal Vol ($\sigma_N$) không phụ thuộc vào mức lãi suất ($F$), phản ánh trực quan hơn các biến động tính bằng basis points. [[Howard_Corb_Swaps.md#page=196]]

---

## 4. Howard Corb (Columbia) Perspective: Swaption Vol Matrix

Corb nhấn mạnh cách thị trường tổ chức thông tin biến động qua **Vol Matrix (Vol Grid)**:
- **Gamma vs. Vega:** Các swaptions ngắn hạn (expiry < 1 năm) được gọi là "gamma", trong khi các swaptions dài hạn được gọi là "vega".
- **Short-dated vs. Long-dated:** Swaptions thường được quote theo cặp "Expiry into Tail" (ví dụ: "1 into 10" là quyền chọn 1 năm vào swap 10 năm). [[Howard_Corb_Swaps.md#page=175]]

---

## Evidence / Source Anchors

- Definition and typology of payer/receiver swaptions: [[Howard_Corb_Swaps.md#page=166]]
- Mathematical derivation of Swaption Parity: [[Howard_Corb_Swaps.md#page=169]]
- Black's formula and the role of the Annuity Factor ($A$): [[Howard_Corb_Swaps.md#page=173]]
- ATM Straddle formula under the Normal Model: [[Howard_Corb_Swaps.md#page=196]]
- Classification of Gamma and Vega swaptions in the Vol Matrix: [[Howard_Corb_Swaps.md#page=175]]

## Related

- [[Caps_And_Floors]] — The counterpart on individual rate settings.
- [[Bermudan_Swaptions]] — Swaptions with multiple exercise dates.
- [[Interest_Rate_Option_Models]] — Detailed comparison of Lognormal vs Normal.
- [[Convexity_Bias_Mechanism]] — Relevant for long-dated swaptions.
