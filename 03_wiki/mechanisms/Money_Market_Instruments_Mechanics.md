---
title: 'Money Market Instruments: Mechanics & Valuation'
aliases:
- Money Market Instruments
- Commercial Paper vs T-Bills
- Discount Rate vs Simple Yield
- Bills of Exchange
- Near Money
- Công cụ thị trường tiền tệ
type: mechanism
tags:
- money-market
- fixed-income
- math
- liquidity
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: Money market instruments are short-term, highly liquid debt obligations characterized
  by their unique discount-based valuation models and their economic function as 'Near
  Money', serving as the primary interface between corporate funding and central bank
  liquidity management.
source_refs:
- file: During_Fixed_Income_Ch14.md
  page: 28
- file: During_Fixed_Income_Ch14.md
  page: 56
- file: Perry_Central_Bank_Policy_P3.md
  page: 70
- file: During_Fixed_Income_Ch13.md
  page: 115
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Thị trường tiền tệ là "phòng chờ" của tiền mặt. Alexander Düring bóc tách ranh giới toán học (Sự khác biệt giữa lãi suất chiết khấu và lợi suất thực tế), trong khi Perry Warjiyo giải mã cơ chế của **"Tiền gần" (Near Money)**. Một sự gãy vỡ trong việc định giá T-bills hay Commercial Paper không chỉ là vấn đề của các Dealer, mà là tín hiệu của một cuộc khủng hoảng thanh khoản hệ thống đe dọa toàn bộ mỏ neo cung tiền của quốc gia. [[During_Fixed_Income_Ch14.md#page=28]] [[Perry_Central_Bank_Policy_P3.md#page=70]]

---

## 1. The Mathematical Paradox: Discount Rate vs. Yield

Alexander Düring giải mã ranh giới định giá đặc thù của thị trường tiền tệ. Khác với trái phiếu dài hạn, các công cụ ngắn hạn không trả coupon mà được bán với giá thấp hơn mệnh giá (at a discount).

### A. The Discount Rate (T-bill Standard)
Sử dụng mệnh giá (Face Value) làm mỏ neo để tính toán:
$$d = \frac{F - P}{F} \times \frac{360}{t}$$
- **Result:** Vì mẫu số là $F$ (luôn lớn hơn giá mua $P$), lãi suất chiết khấu luôn **thấp hơn** lợi suất thực tế mà nhà đầu tư nhận được. Đây là một "ảo giác" toán học cần được điều chỉnh khi so sánh với các tài sản khác. [[During_Fixed_Income_Ch13.md#page=115]]

### B. The Simple Yield (Interbank Standard)
Sử dụng giá mua (Price) làm mỏ neo:
$$y = \frac{F - P}{P} \times \frac{360}{t}$$
- **Application:** Được dùng cho CD, tiền gửi và Repo. Nó phản ánh chính xác tỷ lệ sinh lời trên số vốn thực tế bỏ ra. [[During_Fixed_Income_Ch13.md#page=115]]

---

## 2. Institutional Mechanics of Instruments

### A. Treasury Bills (T-bills)
- **Issuer:** Chính phủ.
- **Issuance:** Qua đấu thầu (Auction).
- **Function:** Mỏ neo "không rủi ro" cho toàn bộ cấu trúc lãi suất ngắn hạn.

### B. Commercial Paper (CP)
- **Mechanism:** Khác với T-bills, CP thường phát hành qua **Reverse Inquiry** (Nhà đầu tư yêu cầu kỳ hạn, Dealer đáp ứng).
- **Safety Net:** Vì CP là nợ không đảm bảo, doanh nghiệp phát hành phải duy trì các **Standby Revolvers** (hạn mức tín dụng dự phòng) tại ngân hàng để đảm bảo có thể hoàn trả nếu không thể phát hành CP mới (roll-over risk). [[During_Fixed_Income_Ch14.md#page=2]]

### C. Certificates of Deposit (CD)
- **Distinction:** CD là tiền gửi có thể chuyển nhượng (negotiable). Nó biến một khoản tiền gửi tĩnh thành một tài sản có tính thanh khoản cao, cho phép ngân hàng huy động vốn trung hạn mà nhà đầu tư vẫn có thể thoát vị thế sớm trên thị trường thứ cấp. [[During_Fixed_Income_Ch14.md#page=56]]

---

## 3. Macro-Financial Linkages (Warjiyo's Lens)

Perry Warjiyo bóc tách ranh giới của sự mất kiểm soát:
- **Near Money Competition:** CP và T-bills cạnh tranh trực tiếp với tiền gửi ngân hàng. Khi lãi suất thị trường tiền tệ tăng, dòng tiền rút khỏi hệ thống ngân hàng để chảy vào các quỹ thị trường tiền tệ (MMF), làm gãy vỡ truyền dẫn lãi suất của NHTW.
- **The Liquidity Fuse:** Thị trường tiền tệ là "ngòi nổ". Khi rủi ro đối tác tăng, các lệnh Repo và CP bị dừng lại đầu tiên, tạo ra một **Liquidity Black Hole** buộc NHTW phải kích hoạt vai trò [[Lender_Of_Last_Resort_Mechanism|LoLR]]. [[Perry_Central_Bank_Policy_P3.md#page=70]]

---

## Evidence / Source Anchors

- Comparison of Discount Rate vs. Simple Yield formulas: [[During_Fixed_Income_Ch13.md#page=115]]
- Analysis of CP issuance via reverse inquiry and standby facilities: [[During_Fixed_Income_Ch14.md#page=2]]
- Identification of Money Market instruments as 'Near Money': [[Perry_Central_Bank_Policy_P3.md#page=70]]
- Rationale for using T-bills as the primary liquidity buffer in portfolios: [[During_Fixed_Income_Ch10.md#page=50]]

## Related

- [[Yield_Curve_Structure_And_Mechanics]] — The short end is built from these instruments.
- [[Repurchase_Agreement_Mechanism]] — The primary funding source for these instruments.
- [[TED_Spread_Mechanism]] — Measuring the gap between T-bills and Interbank rates.
- [[Lender_Of_Last_Resort_Mechanism]] — The safety net when these markets freeze.
