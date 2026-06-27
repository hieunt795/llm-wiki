---
title: Nelson-Siegel-Svensson (NSS) Curve Models
aliases:
- Nelson-Siegel Splines
- NSS Model
- Parametric Curve Fitting
- Level-Slope-Curvature Model
- Mô hình đường cong Nelson-Siegel
type: mechanism
tags:
- quantitative-finance
- yield-curves
- central-banking
- modeling
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: The Nelson-Siegel-Svensson (NSS) models are parsimonious parametric frameworks
  that describe the entire yield curve using a small set of interpretable parameters,
  serving as the global standard for central banks to filter market noise and extract
  long-term economic expectations.
source_refs:
- file: During_Fixed_Income_Ch20.md
  page: 197
- file: During_Fixed_Income_Ch21.md
  page: 205
- file: Perry_Central_Bank_Policy_P4.md
  page: 287
- file: During_Fixed_Income_Ch20.md
  page: 198
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Làm sao để biến một tập hợp các điểm lợi suất rời rạc thành một đường cong mượt mà có ý nghĩa kinh tế? Alexander Düring bóc tách ranh giới của sự tinh gọn (Parsimony) và rủi ro quá khớp (Overfitting), trong khi Perry Warjiyo giải mã cơ chế sử dụng mô hình này như một "cỗ máy chiết xuất kỳ vọng" tại Bank Indonesia. NSS không chỉ là một công cụ khớp dữ liệu; nó là một ngôn ngữ vĩ mô chuyển đổi giá thị trường thành các thành tố Level, Slope và Curvature. [[During_Fixed_Income_Ch20.md#page=197]] [[Perry_Central_Bank_Policy_P4.md#page=287]]

---

## 1. The Nelson-Siegel (NS) Foundation

Mô hình NS biểu diễn lãi suất giao ngay (zero rate) $z(t)$ dưới dạng tổng của 3 thành phần:
$$z(t) = \beta_1 + \beta_2 \left( \frac{1 - e^{-t/\lambda}}{t/\lambda} \right) + \beta_3 \left( \frac{1 - e^{-t/\lambda}}{t/\lambda} - e^{-t/\lambda} \right)$$

### The Interpretation of Beta Parameters (Düring's Lens)
1.  **$\beta_1$ (The Level):** Đại diện cho lãi suất dài hạn. Nó là mỏ neo cố định cho toàn bộ kỳ hạn.
2.  **$\beta_2$ (The Slope):** Thành phần giảm dần theo hàm mũ. Nó đại diện cho sự chênh lệch giữa lãi suất ngắn hạn và dài hạn. Một $\beta_2$ âm lớn tương ứng với đường cong dốc lên mạnh.
3.  **$\beta_3$ (The Curvature/Hump):** Thành phần bắt đầu từ không, đạt đỉnh ở trung hạn và quay về không. Nó mô tả "cái bụng" của đường cong.
4.  **$\lambda$ (The Decay):** Tham số điều chỉnh tốc độ suy giảm của các thành phần slope và curvature. [[During_Fixed_Income_Ch20.md#page=197]]

---

## 2. The Svensson Extension (NSS) & Identification Risk

Để xử lý các đường cong có hình thù phức tạp hơn (ví dụ: có hai "bướu" trong thời kỳ khủng hoảng), Svensson thêm vào tham số $\beta_4$ và $\lambda_2$.

### The Technical Boundary
Alexander Düring cảnh báo về **Identification Problems**:
- Khi hai tham số curvature ($\beta_3$ và $\beta_4$) có vùng tác động chồng lấn, thuật toán tối ưu hóa sẽ gặp khó khăn trong việc phân biệt đóng góp của từng thành phần.
- **Result:** Mô hình có thể cho ra các kết quả không ổn định (unstable parameters) dù giá trị khớp tổng thể rất tốt. Điều này làm giảm tính tin cậy khi dùng để quản trị rủi ro. [[During_Fixed_Income_Ch20.md#page=197]]

---

## 3. Central Bank Implementation (Warjiyo's Lens)

Tại Bank Indonesia, NSS được tích hợp sâu vào hệ thống **Forecasting and Policy Analysis System (FPAS)**:
- **Smoothing Market Noise:** Thị trường trái phiếu SBN đôi khi bị nhiễu do thanh khoản thấp ở một số kỳ hạn. NSS giúp "lọc bỏ" các điểm nhiễu này để tạo ra một đường cong mượt mà phục vụ phân tích.
- **Extracting Expectations:** BI sử dụng NSS để tính toán **Break-even Inflation** (Lạm phát hòa vốn) bằng cách so sánh đường cong lợi suất danh nghĩa và thực tế. Đây là dữ liệu đầu vào sống còn cho các cuộc họp RDG. [[Perry_Central_Bank_Policy_P4.md#page=287]]

---

## 4. Operational Comparison: NSS vs. Polynomial Splines

Düring giải mã lý do NHTW ưu tiên NSS hơn các mô hình đa thức (Cubic Splines):
- **Economic Meaning:** Các tham số của NSS có ý nghĩa kinh tế trực tiếp (Level, Slope), trong khi các hệ số của đa thức chỉ là các hằng số toán học vô hồn.
- **Extrapolation Risk:** NSS có xu hướng hội tụ về $\beta_1$ ở kỳ hạn xa, giúp giảm rủi ro dự báo vô lý (extrapolation noise) so với các mô hình đa thức thường bị "văng" ra ở các điểm đầu và cuối. [[During_Fixed_Income_Ch20.md#page=198]]

---

## Evidence / Source Anchors

- Mathematical formula for the Nelson-Siegel zero-rate spline: [[During_Fixed_Income_Ch20.md#page=197]]
- Description of the $\beta_{1,2,3}$ components as Level, Slope, and Hump: [[During_Fixed_Income_Ch20.md#page=197]]
- Analysis of the Svensson extension and the identification problem: [[During_Fixed_Income_Ch20.md#page=197]]
- Rationale for using NSS in Bank Indonesia's modeling zoo: [[Perry_Central_Bank_Policy_P4.md#page=287]]

## Related

- [[Yield_Curve_Structure_And_Mechanics]] — The context for curve modeling.
- [[Yield_Curve_Fitting_Optimization]] — The process of solving for $\beta$ and $\lambda$.
- [[Principal_Component_Analysis_PCA]] — The statistical counterpart to NSS parameters.
- [[Expectations_Hypothesis_In_Yield_Curves]] — What the NSS parameters seek to reveal.
