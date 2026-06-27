---
title: PCA Yield Curve Decomposition
aliases:
- PCA
- Principal Component Analysis
- Yield Curve Factors
- Level Slope Curvature
- Phân tích nhân tố đường cong lợi suất
type: mechanism
tags:
- quantitative-finance
- yield-curves
- risk-management
- statistics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: Principal Component Analysis (PCA) is a statistical technique used to decompose
  yield curve movements into independent, orthogonal factors—Level, Slope, and Curvature—providing
  a parsimonious roadmap for both portfolio hedging and systemic risk monitoring.
source_refs:
- file: During_Fixed_Income_Ch34.md
  page: 371
- file: During_Fixed_Income_Ch34.md
  page: 374
- file: During_Fixed_Income_Ch35.md
  page: 379
- file: Perry_Central_Bank_Policy_P6.md
  page: 428
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Yield curve không di chuyển ngẫu nhiên; nó có "vân tay" thống kê. Alexander Düring bóc tách ranh giới của việc nén chiều dữ liệu (Sử dụng 3 nhân tố để giải thích >99% biến động), trong khi Perry Warjiyo giải mã cơ chế sử dụng PCA để phát hiện các cú shock hệ thống lan tỏa. PCA biến một ma trận hiệp phương sai khổng lồ thành một bộ hướng dẫn thực thi: nếu bạn muốn hedge rủi ro đường cong, bạn phải đối đầu với 3 nhân tố này. [[During_Fixed_Income_Ch34.md#page=371]] [[Perry_Central_Bank_Policy_P6.md#page=428]]

---

## 1. The Trinity of Factors (Düring's Lens)

PCA phân rã biến động đường cong lợi suất thành 3 vector riêng (eigenvectors) có hình dạng vật lý đặc trưng:

| Factor | Name | Physical Shape | Variance Explained | Economic Driver |
| :--- | :--- | :--- | :--- | :--- |
| **Factor 1** | **Level** | Song song (tất cả các điểm cùng tăng/giảm). | ~90% - 95% | Kỳ vọng lạm phát dài hạn & lãi suất chính sách. |
| **Factor 2** | **Slope** | Đổi dấu 1 lần (ngắn hạn tăng, dài hạn giảm hoặc ngược lại). | ~5% - 7% | Chu kỳ kinh doanh & thắt chặt/nới lỏng tiền tệ. |
| **Factor 3** | **Curvature** | Đổi dấu 2 lần (hai đầu tăng, bụng giảm). | ~1% - 2% | Biến động thị trường (Volatility) & phần bù rủi ro kỳ hạn. |

[[During_Fixed_Income_Ch34.md#page=374]]

---

## 2. Mathematical Implementation: The Eigen-system

Hệ thống vận hành thông qua việc phân tích ma trận hiệp phương sai ($\Sigma$):
1.  **Covariance Matrix:** Düring nhấn mạnh dùng lợi suất thay đổi hàng ngày ($\Delta y$) để đảm bảo tính Stationary.
2.  **Eigenvalues ($\lambda_i$):** Đại diện cho lượng biến động giải thích bởi mỗi nhân tố.
3.  **Eigenvectors ($v_i$):** Chỉ ra hướng di chuyển của đường cong khi nhân tố đó bị kích hoạt.
4.  **Identity:** $\text{Total Variance} = \sum \lambda_i$. [[During_Fixed_Income_Ch34.md#page=373]]

---

## 3. PCA as a Hedging Roadmap

Düring bóc tách ranh giới của việc phòng vệ rủi ro (Ch 35):
- **Factor Neutrality:** Để một danh mục thực sự "miễn nhiễm" với đường cong, nó phải trung lập với ít nhất 3 nhân tố đầu tiên.
- **The N+1 Rule:** Một giao dịch Butterfly (3 chân) có thể được thiết kế để trung lập với Factor 1 (Level) và Factor 2 (Slope), từ đó "cô lập" Factor 3 để đầu cơ vào Curvature.
- **PVBP-weighted PCA:** Kết hợp độ nhạy giá (PVBP) với các trọng số PCA để tạo ra bộ hedge tối ưu. [[During_Fixed_Income_Ch35.md#page=379]]

---

## 4. Macro-Systemic Risk (Warjiyo's Lens)

Perry Warjiyo sử dụng PCA như một "Radar" cảnh báo sớm:
- **Common Shocks:** Nếu Factor 1 (Level) giải thích tỷ trọng cao bất thường trên một nhóm các quốc gia EME, điều đó chứng tỏ dòng vốn đang bị dẫn dắt bởi một cú shock vĩ mô toàn cầu (ví dụ: US Fed tightening) thay vì các yếu tố nội tại.
- **Contagion Monitor:** Sự gia tăng tính tương quan (giá trị riêng của Factor 1 tăng) là dấu hiệu cho thấy các ranh giới rủi ro đang bị xóa nhòa, chuẩn bị cho một đợt sụp đổ hệ thống. [[Perry_Central_Bank_Policy_P6.md#page=428]]

---

## Evidence / Source Anchors

- Analysis of eigenvectors as Level, Slope, and Curvature: [[During_Fixed_Income_Ch34.md#page=374]]
- Mathematical derivation of variance explanation ratios: [[During_Fixed_Income_Ch34.md#page=373]]
- Rationale for hedging exactly 3 principal factors: [[During_Fixed_Income_Ch35.md#page=379]]
- Application of PCA in monitoring macro-financial linkages: [[Perry_Central_Bank_Policy_P6.md#page=428]]

## Related

- [[Yield_Curve_Structure_And_Mechanics]] — The data source for PCA.
- [[Nelson_Siegel_Svensson_Curve_Models]] — The parametric equivalent of PCA factors.
- [[Yield_Curve_Carry_And_Roll_Down]] — Trading the Slope and Curvature.
- [[Systemic_Risk_Taxonomy]] — Using PCA as a metric for interconnectedness.
