---
title: Binomial Trees
aliases:
- Binomial Model
- Discrete-Time Tree
type: concept
tags:
- financial-engineering
- modeling
- discrete-time
- binomial
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Binomial trees are discrete-time models used to approximate the continuous
  joint dynamics of risk factors (interest rates, stock prices) by assuming only two
  possible states at each node.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 250-251
created: '2026-05-22'
updated: '2026-04-22'
---

## Thesis
[RAW] Cây nhị thức (Binomial Tree) là một công cụ mô hình hóa thời gian rời rạc, giả định rằng tại mỗi bước thời gian ($\Delta$), biến số ngẫu nhiên (như lãi suất hoặc giá tài sản) chỉ có thể di chuyển đến một trong hai trạng thái: **Up** hoặc **Down**. Đây là nền tảng cho việc tính toán [[Dynamic_Replication_Methods|Dynamic Replication]] và định giá quyền chọn.

## 1. Structure and Notation
[RAW]
- **Time Periods ($j$):** Các bước thời gian rời rạc $j = 0, 1, 2, \dots$.
- **Interval ($\Delta$):** Độ dài của mỗi bước thời gian. Khi $\Delta \to 0$, mô hình nhị thức hội tụ về mô hình thời gian liên tục (Black-Scholes).
- **Nodes:** Tại mỗi nút, có 2 khả năng xảy ra. Với $n$ bước, sẽ có $2^n$ kịch bản cuối cùng (trong trường hợp cây không tái kết hợp).

## 2. Recombining vs. Non-recombining Trees
[RAW] Neftci nhấn mạnh sự khác biệt quan trọng trong ứng dụng kỹ thuật tài chính:
- **Recombining Tree:** Một đợt "Up" theo sau bởi "Down" dẫn đến cùng một kết quả như "Down" theo sau bởi "Up". Thường dùng cho giá cổ phiếu.
- **Non-recombining Tree:** Con đường (path) đi đến một nút có ý nghĩa quan trọng. Đối với lãi suất, việc lãi suất tăng rồi giảm có thể không đưa giá trái phiếu về cùng một mức như khi giảm rồi tăng (do tính lồi và sự thay đổi của các forward rates). Mô hình hóa lãi suất thường yêu cầu cấu trúc này để phản ánh đúng thực tế kinh tế. [[Principles_of_Financial_Engineering_Neftci.md#page=251]]

## 3. Application in Replication
[RAW] Cây nhị thức cho phép thực hiện **Backward Induction** (Truy hồi ngược):
1.  Bắt đầu từ giá trị tại các nút cuối cùng (đáo hạn).
2.  Tại mỗi nút trung gian, sử dụng giá trị tại hai nút kế tiếp (Up/Down) để giải hệ phương trình tìm trọng số danh mục mô phỏng ($\theta$).
3.  Giá trị tại nút gốc ($j=0$) chính là giá trị không arbitrage của tài sản.

## 4. Key Assumption: One-Factor Model
[RAW] Cây nhị thức cơ bản là một mô hình đơn yếu tố (one-factor model). Nó giả định rằng chỉ có một nguồn rủi ro duy nhất tác động đến tất cả các tài sản trong cây tại mỗi bước. Điều này dẫn đến sự tương quan hoàn hảo (perfect correlation) giữa các tài sản trong mô hình, cho phép mô phỏng chính xác bằng chỉ 2 công cụ cơ sở.

## 5. Refinements: Dividends and Discretization (Exercises 2-4)
[RAW] Các bài tập cuối chương 8 trong Neftci cung cấp các kỹ thuật tinh chỉnh mô hình cây nhị thức cho các trường hợp thực tế:

### 5.1. Handling Dividends
[RAW] Cổ tức ảnh hưởng đến giá cổ phiếu "ex-dividend" và cần được phản ánh trong cấu trúc cây:
1. **Continuous Dividends:** Tỷ lệ cổ tức $q$ được trừ trực tiếp vào suất sinh lời kỳ vọng của cổ phiếu, làm giảm giá trị các nút "up" và "down" một cách hệ thống.
2. **Percentage Dividends:** Cổ tức là một tỷ lệ phần trăm của giá cổ phiếu tại một nút cụ thể. Cây vẫn duy trì tính tái kết hợp (recombining).
3. **Discrete (Dollar) Dividends:** Cổ tức là một số tiền mặt cố định tại một thời điểm. Điều này làm mất tính tái kết hợp của cây, dẫn đến sự gia tăng số lượng nút cần tính toán.

### 5.2. American Options and Early Exercise
[RAW] Đối với quyền chọn kiểu Mỹ (American options), việc định giá tại mỗi nút không chỉ dựa trên giá trị kỳ vọng (continuation value) mà còn phải so sánh với giá trị thực hiện ngay lập tức (exercise value):
$$ V_{node} = \max(\text{Continuation Value, Exercise Value}) $$
Điều này yêu cầu tính toán tại mọi nút thay vì chỉ ở ngày đáo hạn.

### 5.3. SDE Discretization
[RAW] Để xác định các tham số $u$ (up), $d$ (down) và xác suất $p$, ta cần rời rạc hóa Phương trình vi phân ngẫu nhiên (SDE) của tài sản:
- **Example SDE:** $dS_t = \mu S_t dt + \sigma S_t dW_t$
- **Approximation:** Sử dụng các công thức như $u = e^{\sigma \sqrt{\Delta}}$ và $d = e^{-\sigma \sqrt{\Delta}}$ để khớp với biến động (volatility) của mô hình thời gian liên tục.

## Related
- [[Dynamic_Replication_Methods]] — Ứng dụng chính của cây nhị thức.
- [[Self_Financing_Portfolio]] — Điều kiện cần để vận hành danh mục trên cây.
- [[Martingale_Pricing]] — Khung lý thuyết rộng hơn cho các mô hình dạng cây.
