---
title: Model Risk and Jumps
aliases:
- Model Risk
- Jump Risk
- Discrete-Time Approximation Error
type: concept
tags:
- risk-management
- modeling
- replication
- derivatives
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Model risk in dynamic replication arises from the gap between theoretical
  continuous-time assumptions and discrete-time execution, further exacerbated by
  'jumps' (discontinuous price movements) that violate the continuity required for
  perfect hedging.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 263
created: '2026-05-22'
updated: '2026-04-22'
---

## Thesis
[RAW] Rủi ro mô hình (Model Risk) trong mô phỏng động phát sinh từ sự sai lệch giữa các giả định lý thuyết (thời gian liên tục, biến động liên tục) và thực tế triển khai (thời gian rời rạc, bước nhảy giá). Trong khi mô hình lý thuyết cho phép mô phỏng hoàn hảo, thực tế rời rạc và sự xuất hiện của các "cú nhảy" (jumps) khiến chiến lược phòng hộ trở nên mong manh và có thể dẫn đến thất bại hệ thống.

## 1. Discrete-Time Approximation
[RAW] Hầu hết các mô hình tài chính (như Black-Scholes hay Binomial) được xây dựng trên nền tảng thời gian liên tục hoặc các bước rời rạc cực nhỏ.
- **Approximation Error:** Trong thực tế, việc tái cân bằng danh mục chỉ có thể thực hiện tại các khoảng thời gian hữu hạn ($\Delta t$). Điều này tạo ra một sai số xấp xỉ không thể tránh khỏi.
- **Model vs. Reality:** Mô hình giả định các tham số là hằng số hoặc biến đổi theo quy luật biết trước, trong khi thực tế chúng biến động ngẫu nhiên.

## 2. Jump Risk (Rủi ro bước nhảy)
[RAW] Một trong những giả định quan trọng nhất của dynamic replication là tính liên tục của giá tài sản (continuity).
- **The Gap:** Khi thị trường xuất hiện các bước nhảy giá đột ngột (jumps) — ví dụ do tin tức chấn động hoặc khủng hoảng — giá tài sản thay đổi từ $S_t$ sang $S_{t+\epsilon}$ mà không đi qua các mức giá trung gian.
- **Hedging Failure:** Vì danh mục phòng hộ (như delta-hedge) chỉ được điều chỉnh tại các thời điểm rời rạc, nó không thể phản ứng với các biến động xảy ra "giữa các nhịp". Kết quả là tỷ lệ phòng hộ (hedge ratio) trở nên lỗi thời ngay lập tức, dẫn đến lỗ (hoặc lãi) không dự tính.

## 3. Transmission Mechanism
[ASCII]
  [Shock/News] ───> [Jump in Asset Price] ───> [Hedge Ratio Discontinuity]
                          |                           |
                          v                           v
                [Continuous Model Fails] ───> [Unhedged Exposure/Loss]

## 4. Failure Conditions
- **Market Gapping:** Khi giá "mở cửa" ở mức thấp hơn nhiều so với giá đóng cửa hôm trước mà không có cơ hội giao dịch ở giữa.
- **High Frequency Jumps:** Khi tần suất các bước nhảy lớn hơn khả năng tái cân bằng của hệ thống vận hành.

## Related
- [[Dynamic_Replication_Methods]]
- [[Delta_Hedging]]
- [[Liquidity_Search_Problem]]
