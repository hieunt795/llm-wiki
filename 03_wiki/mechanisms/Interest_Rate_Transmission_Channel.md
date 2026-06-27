---
title: Interest Rate Transmission Channel
aliases:
- Interest Rate Channel
- Cost of Capital Channel
- Intertemporal Substitution Channel
- Repo Rate Transmission
- Kênh lãi suất
type: mechanism
tags:
- monetary-policy
- macroeconomics
- investment
- consumption
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: The interest rate channel is the primary neoclassical and operational transmission
  mechanism where policy rate changes influence the real economy by altering the real
  user cost of capital for firms, the intertemporal substitution of consumption for
  households, and the cost of bank liquidity via the repo market.
source_refs:
- file: During_Fixed_Income_Ch06.md
  page: 44
- file: Perry_Central_Bank_Policy_P3.md
  page: 124
- file: Perry_Central_Bank_Policy_P3.md
  page: 125
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The interest rate channel is the "standard" MPTM model. Alexander Düring bóc tách ranh giới của hạ tầng thanh khoản (từ Repo đến Interbank), trong khi Perry Warjiyo giải mã cơ chế dẫn truyền đến các biến số thực (từ Chi phí vốn đến Tiêu dùng). Thành công của kênh này phụ thuộc vào việc NHTW ghim được lãi suất ngắn hạn thị trường vào lãi suất chính sách một cách ổn định. [[During_Fixed_Income_Ch06.md#page=44]] [[Perry_Central_Bank_Policy_P3.md#page=124]]

---

## 1. The Operational Layer (Düring's Micro-view)

Trước khi chạm đến sản lượng, lãi suất chính sách phải vượt qua "đường ống" thanh khoản:
- **Repo Anchor:** NHTW tác động trực tiếp lên lãi suất Repo (vốn được đảm bảo bằng tài sản).
- **Interbank Spillover:** Lãi suất Repo truyền sang lãi suất liên ngân hàng không đảm bảo ($PUAB$).
- **The Friction:** Sự truyền dẫn này có thể bị nghẽn nếu hệ thống ngân hàng bị phân mảnh (Segmentation) hoặc có rủi ro đối tác quá cao. [[During_Fixed_Income_Ch06.md#page=44]]

---

## 2. The Economic Layer (Warjiyo's Macro-view)

### A. Transmission to Investment (User Cost of Capital)
Nhu cầu đầu tư phụ thuộc vào **User Cost of Capital** ($\mu_c$):
$$\mu_c = p_c [i - (E(\pi_c) - \delta)]$$
- **The Mechanism:** Lãi suất chính sách giảm ($i \downarrow$) làm giảm phí tài trợ ngoài, khuyến khích doanh nghiệp vay vốn mở rộng sản xuất. [[Perry_Central_Bank_Policy_P3.md#page=125]]

### B. Transmission to Consumption (Substitution Effect)
Lãi suất thay đổi cấu trúc ưu tiên của hộ gia đình:
- **The Logic:** Lãi suất thấp làm giảm động lực tiết kiệm ($r_D \downarrow$) và giảm chi phí vay mua trả góp bền vững ($r_K \downarrow$).
- **The Shift:** Hộ gia đình chọn tiêu dùng ngay hôm nay thay vì trì hoãn sang ngày mai. [[Perry_Central_Bank_Policy_P3.md#page=125]]

---

## 3. The Market Depth Prerequisite (Financial Deepening)

Cơ chế truyền dẫn qua kênh lãi suất không hoạt động trong chân không; nó bị ràng buộc tuyệt đối bởi độ sâu của thị trường tài chính (Financial Deepening):
- **The Money Market (Interbank):** Nếu thị trường tiền tệ nông hoặc bị phân mảnh (Segmentation), thanh khoản từ Repo sẽ không thể truyền dẫn sang lãi suất liên ngân hàng ($PUAB$). Các ngân hàng sẽ giữ nguyên lãi suất do rủi ro đối tác cao.
- **The Bond Market (Yield Curve):** Doanh nghiệp và hộ gia đình vay mượn ở kỳ hạn dài. Nếu thị trường trái phiếu thiếu thanh khoản, đường cong lợi suất (Yield Curve) sẽ bị nhiễu, làm đứt gãy cầu nối giữa lãi suất chính sách (ngắn hạn) và chi phí vốn thực tế (dài hạn). Việc giảm lãi suất chính sách lúc này chỉ là một "con số trên giấy", không thể kích thích đầu tư hay tiêu dùng.

---

## 4. Case Study: Vietnam (Market 1 vs. Market 2 Separation)

[LLM] Tại Việt Nam, cơ chế truyền dẫn lãi suất bị đứt gãy do sự phân tách cơ học giữa hai tầng thị trường:
- **Market 2 (Interbank):** Nơi các ngân hàng vay mượn dự trữ ngắn hạn (O/N, 1W). Lãi suất này biến động theo thanh khoản tức thời nhưng không phải là nguồn vốn đầu vào cho tín dụng.
- **Market 1 (Retail):** Nơi ngân hàng huy động tiền gửi từ dân cư. Lãi suất cho vay (Lending Rate) bị "neo" vào chi phí vốn huy động trung bình (COF) từ Market 1, thay vì lãi suất Interbank.
- **The Result:** Ngay cả khi lãi suất liên ngân hàng giảm mạnh về mức 0.1-1%, lãi suất cho vay vẫn có thể duy trì ở mức cao (8-10%) do chi phí huy động từ dân cư chưa giảm tương ứng và rủi ro tín dụng thực tế tăng cao.

---

## Strategic Implications: The Lag of Rigidity

Cả hai tác giả đều nhấn mạnh tính phi tức thời:
- **Operational Lag:** 1-2 tháng để lãi suất chính sách ngấm vào thị trường liên ngân hàng.
- **Contractual Lag:** 3-6 tháng để ngân hàng tái định giá bảng cân đối (re-pricing).
- **Economic Lag:** 6-8 quý để lạm phát và sản lượng thực phản ứng toàn diện. [[Perry_Central_Bank_Policy_P3.md#page=118]]

## Evidence / Source Anchors

- Analysis of repo rate as the primary anchor for short-term rates: [[During_Fixed_Income_Ch06.md#page=44]]
- Formulation of the User Cost of Capital equation: [[Perry_Central_Bank_Policy_P3.md#page=125]]
- Identification of the 3-6 month lag in bank rate adjustments: [[Perry_Central_Bank_Policy_P3.md#page=118]]
- Analysis of the intertemporal substitution effect on household preferences: [[Perry_Central_Bank_Policy_P3.md#page=125]]

## Related

- [[Monetary_Policy_Transmission_Mechanism]] — The broader roadmap.
- [[Asset_Price_Transmission_Channel]] — The "Tobin's q" companion to this channel.
- [[Repurchase_Agreement]] — The operational instrument of this channel.
- [[Nominal_Rigidity_Models_Fischer_Taylor]] — Why transmission isn't instantaneous.
