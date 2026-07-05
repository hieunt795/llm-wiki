---
title: Volatility Monetization & Convexity
aliases:
- Volatility Trading
- Convexity Gains
- Delta Hedging Volatility
type: mechanism
tags:
- volatility
- derivatives
- convexity
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Volatility trading is the extraction of cash flows from price oscillations
  by holding a convex instrument (like an option) and dynamically rebalancing it against
  a linear instrument (like a forward).
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 21
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Giao dịch biến động (Volatility trading) không phải là cá cược vào hướng đi của giá, mà là khai thác "convexity gains" phát sinh từ sự chênh lệch giữa công cụ lồi (nonlinear) và công cụ tuyến tính (linear).

## 1. Transmission Mechanism: Monetizing Oscillations
[RAW] Quy trình "thu hoạch" (monetizing) biến động:
1.  **Hold Convexity:** Mua một công cụ có đường cong lợi nhuận lồi (C). Giá trị của nó tăng nhanh hơn khi giá tài sản cơ sở biến động mạnh.
2.  **Delta Neutrality:** Tại mỗi thời điểm, tính toán độ dốc (slope) $D_i$ của đường cong này. Thực hiện bán/mua ngược lại $D_i$ đơn vị tài sản cơ sở (Linear Forward) để triệt tiêu rủi ro hướng giá.
3.  **Result:** Khi giá dao động:
    - Giá tăng: $D_i$ tăng -> Bán thêm tài sản cơ sở tại giá cao.
    - Giá giảm: $D_i$ giảm -> Mua lại tài sản cơ sở tại giá thấp.
    - **Kết quả:** Mỗi chu kỳ dao động tạo ra một khoản thặng dư tiền mặt ròng (Gamma Profit).

## 2. Worked Example (The Gamma Profit)
[RAW] Xét một tổ hợp Long Option (Convex) và Short Forward (Linear):
- **Mechanism:** Giả sử giá dao động quanh mức $F_0$. 
    - Khi giá lên $F_1$, trader bán thêm $(D_1 - D_0)$ đơn vị tại giá $F_1$. 
    - Khi giá quay lại $F_0$, trader mua lại số đơn vị đó tại giá $F_0$.
- **Result:** Khoản lãi ròng thu được là: $\text{Gain} = (D_1 - D_0)(F_1 - F_0)$.
- **Key Insight:** Khoản lãi này luôn dương bất kể giá tăng rồi giảm hay giảm rồi tăng, miễn là có sự dao động (Volatility).

## 3. Boundary Conditions: Realized vs. Implied
- **The Profit Condition:** [RAW] Lợi nhuận từ việc tái cân bằng (rebalancing) chỉ dương nếu biến động thực tế (**Realized Volatility**) cao hơn mức biến động đã trả tiền để mua trong Option (**Implied Volatility**).
- **Time Decay (Theta):** Chi phí để giữ vị thế lồi là sự hao mòn thời gian. Nếu giá không dao động đủ mạnh để bù đắp Theta, chiến lược sẽ lỗ.
- **Transaction Costs:** Việc tái cân bằng liên tục tốn phí giao dịch, có thể ăn mòn lợi nhuận từ biến động nhỏ.

## Related
- [[Option_Greeks_Delta_Gamma_Theta]] — Các thông số đo lường rủi ro này.
- [[Forward_Volatility_Trading]] — Ứng dụng trong thị trường forward.
- [[Convexity]] — Khái niệm toán học nền tảng.
- [[Portfolio_Volatility_MultiFactor]]
- [[Convexity_Adjustment_Futures_Vs_Forward]]
- [[Money_Market_Futures_And_Convexity]]
- [[Bermudan_Swaptions]]
- [[Bond_Futures_Contract_Design]]
- [[Caps_And_Floors]]
- [[CMT_And_CMS_Floaters]]
- [[Credit_Default_Swaps_CDS]]
- [[Model_Risk_And_Jumps]]
- [[Negative_Convexity]]
- [[Structured_Notes]]
- [[LIBOR_And_Term_Benchmark_Fragility]]
- [[Taylor_Expansion_Bond_Pricing]]
- [[Interest_Rate_Swap_Plain_Vanilla]]
- [[Basis_Trading_Mechanics_And_Options]]
- [[Credit_Instrument_Market_Risk_PV01_DV01]]
- [[Forward_Risk_Basis_Risk]]
- [[Asset_Swap_Structure]]
- [[Barrier_Options]]
- [[Binary_Options_Digital]]
- [[Credit_Default_Swaps_Schofield]]
- [[Exotic_Options_Schofield]]
- [[Interest_Rate_Options_Schofield]]
- [[Interest_Rate_Swap_IRS]]
