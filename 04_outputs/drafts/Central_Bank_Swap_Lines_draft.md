---
title: "Central Bank Swap Lines"
aliases:
  - Reciprocal Currency Arrangements
  - USD Liquidity Swap Lines
  - Đường dây hoán đổi NHTW
type: mechanism
tags:
  - monetary-policy
  - fx
  - liquidity
  - central-banking
status: active
confidence: 5
provenance: "Ulrich Bindseil - Central Bank Operations (2014) & Tuckman (2022)"
thesis: "Central Bank Swap Lines là các thỏa thuận song phương giữa Ngân hàng Trung ương (thường là Fed với các NHTW khác) nhằm cung cấp thanh khoản ngoại tệ (chủ yếu là USD) cho các thị trường ngoài phạm vi tài phán trực tiếp của NHTW phát hành, đóng vai trò là 'Người cho vay cuối cùng quốc tế' (ILOLR) để ổn định thị trường tài chính toàn cầu."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 286
  - file: "Tuckman_Serrat_2022.md"
    page: 40
created: 2026-04-24
updated: 2026-04-24
---

## Thesis

[RAW] Trong các cuộc khủng hoảng tài chính, nhu cầu về đồng USD từ các ngân hàng ngoài Mỹ thường vượt quá khả năng cung cấp của thị trường tư nhân, dẫn đến sự đứt gãy của thị trường FX Swap và hiện tượng **[[Cross_Currency_Basis|Negative Basis]]** âm sâu. Swap Lines cho phép Fed bơm thanh khoản USD thông qua các NHTW đối tác để giải tỏa áp lực này mà không trực tiếp chịu rủi ro tín dụng từ các ngân hàng thương mại nước ngoài. [[Bindseil_Monetary_Policy_Operations.md#page=286]]

---

## 1. Mechanics: The Double Swap (Cơ chế Hoán đổi kép)

Một giao dịch Swap Line tiêu chuẩn (ví dụ: Fed và ECB) diễn ra qua hai giai đoạn đồng thời:

1.  **Giai đoạn Fed - ECB (The Bridge):**
    - Fed chuyển USD cho ECB.
    - ECB chuyển một lượng EUR tương ứng cho Fed làm tài sản đảm bảo theo tỷ giá giao ngay (Spot).
    - Cả hai cam kết hoán đổi ngược lại tại **cùng một tỷ giá** trong tương lai (thường là 7 ngày hoặc 3 tháng).
    - **Ý nghĩa:** Fed không chịu rủi ro tỷ giá (FX risk) và ECB trả lãi cho Fed bằng USD (thường là OIS + spread).

2.  **Giai đoạn ECB - Commercial Banks (The Distribution):**
    - ECB thực hiện các phiên đấu thầu cung cấp USD cho các ngân hàng tại khu vực Eurozone.
    - Các ngân hàng thương mại nhận USD và cung cấp tài sản đảm bảo (Collateral) cho ECB theo khung quy định thông thường của ECB.
    - **Ý nghĩa:** ECB chịu rủi ro tín dụng đối với các ngân hàng thương mại nội địa, không phải Fed. [[Bindseil_Monetary_Policy_Operations.md#page=288]]

---

## 2. Impact on Cross-Currency Basis

[LLM] Swap Lines hoạt động như một công cụ "triệt tiêu" Basis âm thông qua hai kênh:

- **Arbitrage Ceiling (Trần Arbitrage):** Khi Fed ấn định lãi suất Swap Line (ví dụ: OIS + 50 bps), mức này trở thành chi phí tối đa mà một ngân hàng chấp nhận trả để có USD. Nếu thị trường tự do yêu cầu một mức Basis khiến chi phí vay USD > OIS + 50 bps, các ngân hàng sẽ chuyển sang vay từ NHTW.
- **Liquidity Backstop:** Sự tồn tại của Swap Lines ngăn chặn hiện tượng "tranh mua USD bằng mọi giá" (panic buying), giúp ổn định tâm lý thị trường và đưa Basis về gần mức 0.

---

## 3. Financial Accounts Representation (Figure 17.5)

Theo Bindseil, cấu trúc bảng cân đối khi Swap Line được kích hoạt (khi k là lượng USD thiếu hụt):

| Central Bank 1 (Fed) | Central Bank 2 (ECB) |
| :--- | :--- |
| **Assets:** USD Claim on CB 2 (+k) | **Assets:** Special USD Lending to Bank 2 (+k) |
| **Liabilities:** USD Currency/Reserves | **Liabilities:** USD Liability to CB 1 (+k) |

*Ghi chú: ECB giữ EUR của Fed làm tài sản đối ứng (không hiển thị trong bảng rút gọn này).* [[Bindseil_Monetary_Policy_Operations.md#page=290]]

---

## 4. Evolution of Swap Lines

- **GFC (2007-2009):** Swap Lines lần đầu tiên được sử dụng ở quy mô chưa từng có để cứu các ngân hàng Châu Âu nắm giữ tài sản MBS bằng USD.
- **Standing Facilities (2013):** Fed chuyển các đường dây hoán đổi với 5 NHTW lớn (BoC, BoE, BoJ, ECB, SNB) thành các thỏa thuận **vĩnh viễn (standing)**.
- **Pandemic (2020):** Fed mở rộng mạng lưới Swap Lines sang 9 NHTW khác (bao gồm Brazil, Mexico, Korea...) và hạ lãi suất xuống OIS + 25 bps để tối đa hóa hiệu quả can thiệp. [[Tuckman_Serrat_2022.md#page=40]]

---

## Evidence / Source Anchors
- Mechanism of ILOLR and currency bridges: [[Bindseil_Monetary_Policy_Operations.md#page=286]]
- T-Account logic for CB FX Swaps: [[Bindseil_Monetary_Policy_Operations.md#page=290]]
- History and expansion during 2020: [[Tuckman_Serrat_2022.md#page=40]]

## Related
- [[Cross_Currency_Basis]] — The primary metric Swap Lines aim to stabilize.
- [[Lender_Of_Last_Resort]] — The domestic version of this function.
- [[FIMA_Repo_Facility]] — The Treasury-based alternative for USD liquidity.
- [[FX_Swap_Engineering]] — The underlying market instrument.
