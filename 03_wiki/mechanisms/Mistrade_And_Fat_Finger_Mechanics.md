---
title: Mistrade and Fat-Finger Mechanics
aliases:
- Fat Finger
- Erroneous Trades
- Cancellation Thresholds
- Price Tolerance
- Giao dịch sai sót
type: mechanism
tags:
- market-infrastructure
- trading
- risk-management
- operations
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income (2021)
thesis: A mistrade is a technical or clerical error in trade execution where the recorded
  price or volume deviates significantly from prevailing market conditions, governed
  by strict institutional and exchange-based cancellation thresholds to balance market
  integrity with the principle of trade finality.
source_refs:
- file: During_Fixed_Income_Ch11.md
  page: 98
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Trong thế giới tài chính tốc độ cao, một lỗi gõ phím (**Fat-finger**) có thể làm bay màu hàng tỷ USD trong vài giây. Alexander Düring bóc tách ranh giới của việc xử lý sai sót: không phải mọi giao dịch nhầm lẫn đều được hủy. Thị trường vận hành trên nguyên tắc "Lời nói là cam kết" (*dictum meum pactum*), và việc hủy giao dịch chỉ được phép nếu sai lệch vượt qua một **Ngưỡng chấp nhận (Price Tolerance)** nhất định để bảo vệ tính công bằng chung mà không làm tê liệt niềm tin vào tính quyết toán (finality). [[During_Fixed_Income_Ch11.md#page=98]]

---

## 1. Mechanism: The Tolerance Band

Các sàn giao dịch và nền tảng OTC thiết lập các ranh giới tự động để phát hiện Mistrade:
- **Price Thresholds:** Nếu một giao dịch được khớp ở mức giá chênh lệch quá X% (ví dụ 5% hoặc 10%) so với giá tham chiếu gần nhất, hệ thống sẽ tự động đình chỉ (halt) hoặc đánh dấu là nghi vấn.
- **Volume Checks:** Các lệnh có quy mô lớn bất thường so với mức thanh khoản trung bình của mã tài sản đó sẽ kích hoạt cảnh báo "Fat-finger". [[During_Fixed_Income_Ch11.md#page=98]]

---

## 2. The Cancellation Process

Khi một Mistrade được xác nhận, quy trình xử lý bao gồm 3 bước:
1.  **Notification:** Bên mắc lỗi phải thông báo ngay lập tức cho đối tác và sàn giao dịch (thường trong vòng vài phút).
2.  **Negotiation (OTC):** Trên thị trường song phương, việc hủy giao dịch thường dựa trên thiện chí. Nếu đối tác đã phòng vệ (hedge) vị thế đó, họ có quyền từ chối hủy hoặc yêu cầu bồi thường chi phí hedge.
3.  **Arbitration (Exchange):** Sàn giao dịch đóng vai trò là trọng tài tối cao, có quyền đơn phương hủy các giao dịch nằm ngoài dải giá quy định để duy trì trật tự thị trường. [[During_Fixed_Income_Ch11.md#page=98]]

---

## 3. Strategic Implications: Operational Risk

Düring nhấn mạnh ranh giới rủi ro vận hành:
- **Trade Finality vs. Fairness:** Việc dễ dàng cho phép hủy giao dịch sẽ khuyến khích sự cẩu thả và cho phép các bên "hối hận" khi thị trường đi ngược hướng (Moral Hazard).
- **Automation:** Sự trỗi dậy của thuật toán (Algorithmic Trading) làm tăng nguy cơ Mistrade dây chuyền, nơi một lỗi hệ thống của một bên kích hoạt hàng loạt lệnh sai sót từ các bên khác. [[During_Fixed_Income_Ch11.md#page=98]]

---

## Evidence / Source Anchors

- Analysis of mistrades as a violation of market price discovery: [[During_Fixed_Income_Ch11.md#page=98]]
- Definition of the time-window requirement for reporting errors: [[During_Fixed_Income_Ch11.md#page=98]]
- Rationale for price tolerance bands in maintaining trade finality: [[During_Fixed_Income_Ch11.md#page=98]]
- Distinction between clerical errors and algorithmic cascading failures: [[During_Fixed_Income_Ch11.md#page=98]]

## Related

- [[OTC_Trade_Lifecycle_Mechanics]] — Where a mistrade is identified (Step 3: Agreement).
- [[Settlement_Fails_And_Incentives]] — When a mistrade leads to a failure to deliver.
- [[Market_Maker_Vs_Liquidity_Provider]] — Who typically bears the brunt of fat-finger shocks.
- [[Central_Counterparty_CCP]] — How CCPs manage the risk of un-cancelled mistrades.
- [[Bid_Ask_Bounce]]
- [[Trade_Implementation_Consistency]]
- [[Mistrade_And_Fat_Finger]]
- [[Bond_Futures_Contract_Design]]
- [[Bond_Index_Principles]]
- [[Herstatt_Risk]]
- [[Liquidity_Measurement_Taxonomy]]
- [[Margining]]
