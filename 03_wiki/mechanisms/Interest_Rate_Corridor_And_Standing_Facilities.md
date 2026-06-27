---
title: Interest Rate Corridor and Standing Facilities
aliases:
- Interest Rate Corridor
- Standing Facilities
- Floor and Ceiling System
- FASBI
- Discount Window
- Hành lang lãi suất
type: mechanism
tags:
- central-banking
- monetary-policy
- operations
- liquidity
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: The interest rate corridor is an operational architecture that bounds interbank
  rate volatility between a floor (Deposit Facility) and a ceiling (Lending Facility),
  evolving from a scarcity-based symmetric system to a surplus-based floor system
  in the post-QE era.
source_refs:
- file: During_Fixed_Income_Ch06.md
  page: 47
- file: During_Fixed_Income_Ch07.md
  page: 49
- file: Perry_Central_Bank_Policy_P4.md
  page: 211
- file: Perry_Central_Bank_Policy_P4.md
  page: 218
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

The corridor system provides an "Automatic Stabilizer" for the money market. Alexander Düring bóc tách ranh giới của cấu trúc thị trường (Sự chuyển dịch từ Scarcity sang Floor system), trong khi Perry Warjiyo giải mã cơ chế thực thi tại các EME (Sử dụng FASBI và LF để ghim lãi suất liên ngân hàng). Một hành lang được thiết kế tốt đảm bảo rằng ngay cả khi các nghiệp vụ thị trường mở (OMO) không chính xác tuyệt đối, lãi suất thị trường vẫn sẽ luôn nằm trong tầm kiểm soát của NHTW. [[During_Fixed_Income_Ch06.md#page=47]] [[Perry_Central_Bank_Policy_P4.md#page=211]]

---

## 1. The Three Pillars of the Corridor

An operational corridor is defined by three interest rates:

1.  **Lending Facility (Ceiling - Trần):** Lãi suất mà NHTW cho các ngân hàng vay khẩn cấp (thường yêu cầu tài sản đảm bảo). Nó tạo thành giới hạn trên cho lãi suất liên ngân hàng.
2.  **Policy Rate (Anchor - Mỏ neo):** Lãi suất mục tiêu (ví dụ: BI 7-day Reverse Repo). Thường nằm ở giữa hành lang trong hệ thống đối xứng.
3.  **Deposit Facility (Floor - Sàn):** Lãi suất NHTW trả cho các khoản tiền gửi dư thừa của ngân hàng. Nó tạo thành giới hạn dưới vì không ngân hàng nào dại gì cho vay trên thị trường với lãi suất thấp hơn mức NHTW trả. [[Perry_Central_Bank_Policy_P4.md#page=211]]

---

## 2. Evolutionary Models: Symmetric vs. Asymmetric

Düring bóc tách sự thay đổi cấu trúc mang tính lịch sử hậu khủng hoảng 2008:

### A. The Symmetric Corridor (Pre-2008 Standard)
- **Condition:** NHTW giữ cho hệ thống luôn "đói" thanh khoản (Scarcity).
- **Mechanism:** Các ngân hàng phải tích cực vay mượn lẫn nhau để đáp ứng dự trữ bắt buộc. Lãi suất thị trường (PUAB/FFR) dao động linh hoạt quanh mỏ neo chính sách ở giữa hành lang. [[During_Fixed_Income_Ch06.md#page=47]]

### B. The Asymmetric Floor System (Post-QE Era)
- **Condition:** Các chương trình QE bơm một lượng tiền khổng lồ vào hệ thống (Surplus).
- **Mechanism:** Vì mọi ngân hàng đều dư thừa tiền, lãi suất liên ngân hàng sụp đổ về mức sàn. **Deposit Facility Rate** trở thành lãi suất thị trường thực tế. 
- **The Non-Bank Leakage:** Tại Eurozone, lãi suất €STR thường thấp hơn sàn của ECB vì các định chế phi ngân hàng (pension funds) không có quyền gửi tiền tại NHTW nên chấp nhận cho vay rẻ hơn mức sàn để giải tỏa tiền mặt. [[During_Fixed_Income_Ch07.md#page=49]]
- **The "Soft Floor" / Range Floor (May 2026 Update):** [RAW-CLIP: Constâncio (2025-11-28)] Cấu trúc sàn đã tiến hóa thành "Hệ thống sàn biên độ" (Range Floor System). ECB duy trì chênh lệch (spread) 15 bps, trong khi Fed duy trì 10 bps giữa lãi suất dự trữ và lãi suất thị trường. Đây được gọi là "Soft Floor" vì nó không phải là một tỷ lệ cố định duy nhất mà là một dải hẹp được quản trị bởi sự chênh lệch giữa các cơ sở tiền gửi và cơ sở repo nghịch đảo (ON RRP).

---

## 3. EME Context: The Indonesia Model (FASBI & LF)

Perry Warjiyo giải mã cơ chế ghim giữ tại Indonesia:
- **LF (Lending Facility):** Mỏ neo trần.
- **FASBI (Bank Indonesia Facility):** Mỏ neo sàn.
- **Corridor Width:** BI thiết lập hành lang đối xứng (thường là ±50-75 bps). Nếu hành lang quá hẹp, thị trường liên ngân hàng sẽ "chết" vì các ngân hàng thà giao dịch với NHTW. Nếu quá rộng, lãi suất PUAB sẽ biến động quá mạnh làm hỏng tín hiệu chính sách. [[Perry_Central_Bank_Policy_P4.md#page=218]]

---

## 4. Behavioral Friction: The Stigma Effect

Alexander Düring nhấn mạnh một yếu tố tâm lý sống còn: **Vết nhơ (Stigma)**.
- **The Logic:** Việc vay từ Lending Facility (Discount Window) thường bị coi là tín hiệu của sự yếu kém trầm trọng.
- **The Result:** Các ngân hàng có thể chấp nhận vay với lãi suất "trên trần" từ thị trường tư nhân chỉ để tránh bị NHTW soi xét, làm suy yếu hiệu quả ổn định của hành lang lãi suất. [[During_Fixed_Income_Ch07.md#page=46]]

---

## 4. The PBoC Model: Transition to Price-based (2024-2025)

Zhaoyan Guo (2025) giải mã sự thay đổi mang tính cấu trúc của NHTW Trung Quốc (PBoC):
- **Ceiling (Trần):** **SLF (Standing Lending Facility)**. PBoC cung cấp thanh khoản ngắn hạn cho thị trường liên ngân hàng qua SLF, thiết lập giới hạn trên cho lãi suất thị trường.
- **Floor (Sàn):** **Excess Reserve Requirement Rate** (Lãi suất dự trữ vượt mức).
- **Policy Anchor (Mỏ neo):** Từ tháng 07/2024, PBoC chính thức xác lập **7-day Reverse Repo Rate** là lãi suất chính sách chính, thay thế vai trò của MLF.
- **LPR Decoupling:** Lãi suất cho vay cơ bản (LPR) được tách rời khỏi MLF và liên kết trực tiếp với lãi suất OMO (7-day reverse repo), giúp truyền dẫn từ lãi suất ngắn hạn sang lãi suất vay thực tế trở nên thông suốt hơn, tương tự mô hình của các nước phát triển. [[Guo_Chinas_Monetary_Policy_Framework_2025.md]]

---

## Evidence / Source Anchors

- Transition from symmetric to asymmetric corridors due to surplus liquidity: [[During_Fixed_Income_Ch07.md#page=49]]
- Definition of the three-rate hierarchy in Indonesia: [[Perry_Central_Bank_Policy_P4.md#page=211]]
- Analysis of the "Stigma" effect on discount window usage: [[During_Fixed_Income_Ch07.md#page=46]]
- Identification of non-bank liquidity pushing €STR below the floor: [[During_Fixed_Income_Ch07.md#page=49]]

## Related

- [[Open_Market_Operations_And_Instruments]] — The active tool used within the corridor.
- [[Lender_Of_Last_Resort_Mechanism]] — When the Lending Facility acts as a systemic backstop.
- [[Quantitative_Easing]] — The driver of the shift to the Floor System.
- [[Negative_Interest_Rate_Policy_NIRP]] — When the floor itself becomes negative.
