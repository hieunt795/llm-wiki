---
title: Multi-Factor Portfolio Volatility
aliases:
- Portfolio Volatility
- Risk Budgeting
- Biến động danh mục đa nhân tố
type: mechanism
tags:
- risk-management
- volatility
- fixed-income
- key-rate
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat"
provenance: Tuckman_Serrat_2022.md
thesis: Portfolio volatility is an aggregate risk measure that accounts for sensitivities
  all along the yield curve and the imperfect correlation between rate changes at
  different tenors, extending beyond simple one-factor models.
source_refs:
- file: Tuckman_Serrat_2022.md
  page: 151
created: '2026-04-21'
updated: '2026-04-21'
---

## Thesis

Trong quản trị rủi ro danh mục thu nhập cố định, việc giả định một yếu tố duy nhất (như sự dịch chuyển song song của đường cong lãi suất) là không đủ. Bruce Tuckman chỉ ra rằng độ biến động thực tế của danh mục phụ thuộc vào sự tương tác giữa các độ nhạy (key-rate exposures) và ma trận tương quan giữa các điểm kỳ hạn khác nhau. [[Tuckman_Serrat_2022.md#page=151]]

---

## 1. The Core Formula (2-Factor Example)

Sự thay đổi giá trị danh mục ($\Delta P$) được ước tính dựa trên hai Key-rate ’01s ($KR01_1$ và $KR01_2$):

$$ \Delta P \approx KR01_1 \times \Delta y_1 + KR01_2 \times \Delta y_2 $$

Độ biến động của danh mục ($\sigma_P$) được tính dựa trên quy tắc tính phương sai của tổng các biến ngẫu nhiên:

$$ \sigma_P \approx \sqrt{KR01_1^2 \sigma_1^2 + KR01_2^2 \sigma_2^2 + 2 KR01_1 KR01_2 \rho \sigma_1 \sigma_2} $$

Trong đó:
- $KR01_i$: Key-rate exposures (độ nhạy của giá trị danh mục đối với thay đổi 1 bps tại kỳ hạn $i$).
- $\sigma_i$: Độ biến động của thay đổi lãi suất tại kỳ hạn $i$.
- $\rho$: Tương quan (correlation) giữa thay đổi lãi suất của hai kỳ hạn.

---

## 2. Strategic Implications

### A. Diversification Benefits
Nếu các kỳ hạn khác nhau không có tương quan hoàn hảo ($\rho < 1$), tổng biến động của danh mục sẽ thấp hơn so với trường hợp giả định tất cả lãi suất di chuyển song song.
- **Risk Underestimation:** Ngược lại, nếu sử dụng mô hình 1 nhân tố (giả định $\rho = 1$), ta có thể đánh giá sai rủi ro của các chiến lược chênh lệch (spread trades) hoặc butterfly.

### B. Correlation Decay
Khi số lượng nhân tố (key rates, buckets) tăng lên, ma trận tương quan càng trở nên phức tạp. Việc ước tính chính xác $\rho$ từ dữ liệu lịch sử là chìa khóa để đo lường xác suất thua lỗ tối đa (VaR).

### C. Hedging Precision
Phòng vệ đa nhân tố (multi-factor hedging) không chỉ nhằm mục tiêu triệt tiêu độ nhạy (net KR01 = 0) mà còn nhằm mục tiêu ổn định $\sigma_P$. Một danh mục có tổng DV01 bằng 0 vẫn có thể có $\sigma_P > 0$ nếu các key-rate exposures không được khớp chính xác.

## 3. Case Study: Basis Risk in Bond-Swap-Repo (Neftci Nuance)

[RAW] Salih Neftci chỉ ra rằng trong các giao dịch "Arbitrage" dựa trên chênh lệch Repo và Swap (ví dụ tại thị trường Singapore), rủi ro đa nhân tố xuất hiện dưới dạng **Basis Risk**.
- **Scenario:** Một danh mục Long Bond + Pay Fixed Swap có vẻ "Duration-neutral" trong mô hình 1 nhân tố (Parallel shift).
- **Failure Condition:** Nếu lãi suất Repo (vốn vay) tăng nhanh hơn lãi suất SIBOR (vốn nhận từ Swap), danh mục sẽ bị ép biên lợi nhuận (margin squeeze) dù lãi suất tổng thể không đổi.
- **Application:** Công thức Tuckman phía trên được dùng để tính toán tương quan ($\rho$) giữa **Repo Rate** và **Swap Rate** để xác định độ an toàn của chiến lược "Spread Play" này. [[Principles_of_Financial_Engineering_Neftci.md#page=162]]

---

## Evidence / Source Anchors

- Derivation of portfolio volatility using two key rates and correlation: [[Tuckman_Serrat_2022.md#page=151]]
- Definition of portfolio variance in a multi-factor setting: [[Tuckman_Serrat_2022.md#page=151]]
- Linkage between risk metrics (DV01) and volatility quantification: [[Tuckman_Serrat_2022.md#page=151]]

## Related

- [[Key_Rate_Duration_Mechanics]] — Cơ sở để đo lường các KR01.
- [[Principal_Component_Analysis_PCA]] — Phương pháp thống kê để xác định các nhân tố biến động chính.
- [[Yield_Curve_Trading_Strategies]] — Các chiến thuật dựa trên cấu trúc rủi ro đa nhân tố.
- [[Portfolio_Risk_Budgeting_And_Optimization]]
- [[Forward_Volatility_Trading]]
