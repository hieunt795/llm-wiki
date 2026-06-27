---
title: Repurchase Agreement (Repo) Mechanism
aliases:
- Repurchase_Agreement
- Repo
- Reverse Repo
- GC Repo vs Special Repo
- BI 7-Day Reverse Repo Rate
- Hợp đồng mua lại
type: mechanism
tags:
- fixed-income
- money-market
- central-banking
- infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Salih Neftci | Alexander Düring"
provenance: Multi-source (During & Warjiyo)
thesis: A Repurchase Agreement (Repo) is legally a simultaneous sale and future repurchase
  of a security, but economically functions as a secured loan, serving as the vital
  infrastructure for bond short-selling and the primary anchor for modern monetary
  policy signalling.
source_refs:
- file: During_Fixed_Income_Ch15.md
  page: 122
- file: Perry_Central_Bank_Policy_P2.md
  page: 3
- file: During_Fixed_Income_Ch18.md
  page: 456
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 151
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 446-500
  section: "Chapter 1.3: Repurchase Agreements"
created: '2026-04-13'
updated: '2026-04-21'
---

## Thesis

Repo là "mạch máu" của thị trường thu nhập cố định. Alexander Düring bóc tách ranh giới của hạ tầng thị trường (từ GC đến Special Repo), trong khi Perry Warjiyo giải mã cơ chế sử dụng Repo làm mỏ neo chính sách tối thượng (Policy Anchor). [RAW] Salih Neftci làm sâu sắc thêm góc nhìn Kỹ thuật tài chính: Repo thực chất là một giao dịch đơn nhất viết trên cùng một ticket ("Single Ticket"), cho phép các Practitioner "mua mà không thực sự mua" và "bán mà không thực sự bán" thông qua việc thay đổi chuỗi giao dịch để tối ưu hóa chi phí vốn. [[During_Fixed_Income_Ch15.md#page=122]] [[Perry_Central_Bank_Policy_P2.md#page=3]] [[Principles_of_Financial_Engineering_Neftci.md#page=151]]

---

## 1. Technical Taxonomy (Düring & Neftci)

### A. General Collateral (GC) Repo
- **Purpose:** Vay tiền mặt (Borrowing cash).
- **Mechanism:** Người vay sử dụng bất kỳ trái phiếu nào trong một rổ tài sản đảm bảo tiêu chuẩn để vay tiền.
- **Pricing:** Lãi suất Repo phản ánh chi phí vốn ngắn hạn, thường bám sát lãi suất chính sách.

### B. Special Repo
- **Purpose:** Mượn một mã chứng khoán cụ thể (Borrowing a specific bond).
- **Mechanism:** Xảy ra khi một mã trái phiếu bị khan hiếm (short squeeze). Nhà đầu tư sẵn sàng cho vay tiền mặt với lãi suất cực thấp (thậm chí âm) chỉ để mượn được tờ giấy đó.
- **Indicator:** Khoảng cách giữa lãi suất GC và lãi suất Special là thước đo độ "nóng" của một mã trái phiếu. [[During_Fixed_Income_Ch15.md#page=123]]

### C. The Naming Convention (Neftci Nuance)
[RAW] Trong thị trường Repo, thuật ngữ "Lender" và "Borrower" được xác định dựa trên **Chứng khoán (Security)**, không phải tiền mặt:
- **Repo Dealer as Lender:** Dealer đưa chứng khoán (lends security), nhận tiền mặt -> Repo.
- **Repo Dealer as Borrower:** Dealer nhận chứng khoán (borrows security), đưa tiền mặt -> Reverse Repo.

---

## 2. Strategic Advantages: Funding Optimization

[RAW] Neftci giải thích cách Repo làm thay đổi chuỗi giao dịch truyền thống của một chuyên gia thị trường:

**Chuỗi mua đứt (Outright Purchase):**
`Tìm vốn -> Trả tiền -> Nhận chứng khoán (Vốn vay thường không đảm bảo, lãi cao)`

**Chuỗi tối ưu qua Repo (Repo-funded Purchase):**
`Mua trái phiếu -> Repo ngay lập tức -> Lấy tiền trả cho giao dịch mua`
- **Transmission:** Bằng cách biến chứng khoán vừa mua thành tài sản đảm bảo cho chính khoản vay để mua nó, nhà đầu tư nhận được lãi suất Repo (thấp hơn nhiều so với lãi suất vay không đảm bảo).

---

## 4. Repo Structures (US vs European Style)

[RAW] Neftci phân biệt hai cách tiếp cận chính trong việc cấu trúc hợp đồng Repo:

| Đặc điểm | Classic Repo (US Style) | Sell and Buy-back |
|---|---|---|
| **Văn bản** | Một hợp đồng duy nhất (Single ticket) | Thường là 2 hợp đồng tách biệt (Spot sale & Forward repurchase) |
| **Thanh toán lãi** | Tiền mặt + Lãi Repo | Chênh lệch giữa giá mua và giá bán |
| **Mark-to-market** | Có thực hiện hàng ngày | Thường không có |
| **Quyền lợi coupon** | Người bán (Seller) nhận coupon | Người mua (Buyer) nhận coupon nhưng điều chỉnh vào giá bán lại |
| **Rủi rro vỡ nợ** | Có quyền "Set-off" rõ ràng | Rủi ro pháp lý cao hơn nếu không có tài liệu (undocumented) |

### The Dirty Price Rule
[RAW] Mọi giao dịch Repo chuyên nghiệp đều dựa trên **Dirty Price** (giá đã bao gồm Accrued Interest).
- **Rationale:** Vì chứng khoán chuyển giao tạm thời, người nắm giữ chứng khoán trong thời gian Repo sẽ nhận được bất kỳ khoản lãi coupon nào phát sinh. Việc dùng Dirty Price đảm bảo tính công bằng trong định giá dòng tiền vay mượn.

---

## 5. Cash Flow Mechanics: Manufactured Payments

[RAW] Mặc dù quyền sở hữu pháp lý chuyển giao tạm thời cho người mua (Buyer), nhưng rủi ro và lợi ích kinh tế vẫn thuộc về người sở hữu gốc (Lender of security).
- **Manufactured Dividends/Coupons:** Mọi khoản lãi coupon hoặc cổ tức phát sinh trong thời gian Repo phải được chuyển lại cho bên bán (Seller). 
- **Timing Nuance:** Trong Classic Repo, tiền được chuyển vào đúng ngày thanh toán coupon; trong Sell and Buy-back, nó thường được gộp vào giá mua lại ở chân thứ hai (second leg).

## 6. Credit Risk and Seniority

[RAW] Repo mang đặc tính của một khoản vay siêu ưu tiên:
- **Seniority:** Repo có quyền ưu tiên (Senior) cao hơn ngay cả các Senior Tranches (định hạng AAA) của các cấu trúc CDO. 
- **Default Right:** Trong trường hợp đối tác không thực hiện lệnh Margin Call, Repo Dealer có quyền ưu tiên hàng đầu trong việc xử lý và chiếm hữu tài sản đảm bảo mà không cần thực hiện các thủ tục xác lập quyền sở hữu phức tạp.

---

## 7. Boundary Risks: The Repo Run

[RAW] Neftci bóc tách ranh giới của sự sụp đổ thanh khoản thông qua hiện tượng **Repo Run** (Tháo chạy khỏi thị trường Repo):
- **Mechanism:** Trong khủng hoảng (như GFC 2008), các bên cho vay tiền (cash providers) đột ngột mất niềm tin vào khả năng thanh toán của Dealer hoặc giá trị của tài sản đảm bảo.
- **Two Forms of Run:**
    1.  **Refusal to Rollover:** Bên cho vay từ chối gia hạn các hợp đồng Repo qua đêm (Overnight), cắt đứt nguồn vốn nuôi sống các Dealer (như trường hợp Lehman Brothers tại thị trường Tri-party).
    2.  **Haircut Spiking:** Bên cho vay tăng mạnh tỷ lệ Haircut (e.g., từ 2% lên 20%), buộc Dealer phải nộp thêm một lượng tiền mặt khổng lồ ngay lập tức. 
- **Result:** Hiện tượng bán tháo tài sản (Fire-sales) diễn ra để lấy tiền mặt, làm giá tài sản giảm sâu hơn và kích hoạt vòng xoáy khủng hoảng.

---

## 8. Policy Anchor: The BI 7-Day Reverse Repo

Perry Warjiyo bóc tách sự chuyển dịch mang tính chiến lược của Indonesia vào năm 2016:

### The Reform Logic
Từ 2005-2016, Indonesia dùng **BI Rate** (kỳ hạn 1 tháng). Tuy nhiên, lãi suất này bị "tách rời" khỏi nhu cầu thanh khoản hàng ngày của ngân hàng.
- **Shortening the Tenor:** Việc chuyển sang **7-Day Reverse Repo** giúp mỏ neo chính sách sát với kỳ hạn giao dịch thực tế của thị trường liên ngân hàng (PUAB).
- **Immediate Transmission:** Khi BI thay đổi lãi suất 7 ngày, các ngân hàng phải điều chỉnh ngay lập tức vì chi phí vốn ngắn hạn của họ bị tác động trực tiếp. [[Perry_Central_Bank_Policy_P2.md#page=3]]

---

## 3. Operational Advantages: Maturity Decoupling

Ưu điểm lớn nhất của Repo là khả năng **Tách rời kỳ hạn (Maturity Decoupling)**:
- Một nhà đầu tư có thể giữ trái phiếu 30 năm (để hưởng duration) nhưng vẫn có thể vay tiền mặt kỳ hạn 1 ngày qua Repo để đáp ứng nhu cầu thanh khoản tức thời. 
- Điều này cho phép tài sản dài hạn đóng vai trò là thanh khoản "ngủ đông" mà không cần phải bán đứt tài sản, tránh gây biến động giá không cần thiết. [[During_Fixed_Income_Ch15.md#page=122]]

## 9. Synthetic Engineering via Repo

[RAW] Neftci bóc tách cách sử dụng các phương trình hợp đồng (contractual equations) để tạo ra các vị thế giả lập (synthetics) từ các chân giao dịch Repo:

### A. Synthetic Repo
Một Repo thực chất có thể được tái lập bằng cách kết hợp:
`Synthetic Repo = Spot Sale of Asset - Forward Purchase of Asset`
- **Mechanism:** Nhà đầu tư bán tài sản ngay lập tức (Spot Sale) để lấy tiền và đồng thời cam kết mua lại nó ở một mức giá xác định trong tương lai (Forward Purchase). Chênh lệch giá giữa hai chân giao dịch chính là lãi suất Repo giả lập. [[Principles_of_Financial_Engineering_Neftci.md#page=169]]

### B. Synthetic Outright Purchase
Ngược lại, một giao dịch mua đứt tài sản có thể được giả lập để tránh việc phải bỏ ra toàn bộ vốn ngay lập tức:
`Synthetic Outright Purchase = Forward Purchase + Repo with term (T-t)`
- **Mechanism:** Thay vì mua ngay, nhà đầu tư mua kỳ hạn và thực hiện một giao dịch Repo có kỳ hạn tương ứng để tài trợ cho chân giao dịch đó.

## 10. Tax Arbitrage: Coupon Washing

[RAW] Repo là công cụ trung tâm trong các chiến lược tối ưu hóa thuế (Tax Strategies):
- **Mechanism:** Nhà đầu tư nội địa (phải chịu thuế khấu trừ - withholding tax) thực hiện Repo trái phiếu cho một đối tác nước ngoài (được miễn thuế - tax-exempt) ngay trước ngày trả coupon. 
- **Result:** Đối tác nước ngoài nhận coupon gộp (gross coupon) và chuyển lại cho nhà đầu tư nội địa dưới dạng "Manufactured Dividend".
- **Regulatory Conflict:** Các cơ quan quản lý (như tại Thái Lan và Indonesia) thường xuyên phải đưa ra các chỉ thị mới để ngăn chặn hành vi này bằng cách yêu cầu khấu trừ thuế dựa trên **Accrued Interest** (lãi cộng dồn) thay vì chỉ dựa trên việc ai nắm giữ trái phiếu vào ngày trả coupon. [[Principles_of_Financial_Engineering_Neftci.md#page=186]]

---

## Evidence / Source Anchors

- Definition of Repo as economically a secured deposit: [[During_Fixed_Income_Ch15.md#page=122]]
- Analysis of the 2016 BI policy rate reform to 7-day RR: [[Perry_Central_Bank_Policy_P2.md#page=3]]
- Distinction between GC Repo and Special Repo functionality: [[During_Fixed_Income_Ch15.md#page=123]]
- Discussion on T+0 settlement speeds in US/UK Repo markets: [[During_Fixed_Income_Ch15.md#page=122]]
- Case study on Singapore Bond vs Swap play and Repo funding: [[Principles_of_Financial_Engineering_Neftci.md#page=162]]

## Related

- [[Open_Market_Operations_And_Instruments]] — Repo là công cụ chính của OMO.
- [[Interest_Rate_Corridor_Mechanism]] — Repo đóng vai trò là "trần" hoặc "anchor" của hành lang.
- [[Short_Selling_Mechanics]] — Tại sao Repo là điều kiện tiên quyết cho bán khống.
- [[Haircut_And_Margin_Mechanics]] — Cơ chế quản trị rủi ro trong Repo.
