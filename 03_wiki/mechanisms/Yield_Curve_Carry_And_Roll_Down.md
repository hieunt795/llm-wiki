---
title: Yield Curve Carry and Roll-Down
aliases:
- Holding Period Return
- Static Return
- P&L Attribution
- The Buffer
- Break-Even Yield Shift
- Roll-Down
- Vùng đệm lợi suất
type: mechanism
tags:
- trading-strategies
- valuation
- yield-curves
- EMEs
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Tuckman & Serrat | Alexander Düring"
provenance: Multi-source (During, Warjiyo & Tuckman)
thesis: The total return of a bond position is decomposed into static components (Carry
  and Roll-down) and dynamic components (Market moves), providing a framework for
  P&L attribution and defining the margin of safety against interest rate shocks.
source_refs:
- file: During_Fixed_Income_Ch22.md
  page: 217
- file: Tuckman_Serrat_2022.md
  page: 79
- file: Perry_Central_Bank_Policy_P6.md
  page: 394
- file: During_Fixed_Income_Ch15.md
  page: 136
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Trong một hệ thống nơi đường cong lợi suất dốc lên, thời gian chính là lợi nhuận. Alexander Düring bóc tách ranh giới của vùng đệm an toàn (Buffer), Howard Corb giải mã động lực giao dịch, và Tuckman & Serrat (2022) cung cấp framework **P&L Attribution** để phân rã chính xác nguồn gốc của lợi nhuận. Một nhà đầu tư chuyên nghiệp không chỉ nhìn vào việc "có lãi hay không," mà phải biết bao nhiêu phần trăm lợi nhuận đến từ việc trôi đi của thời gian (Static) và bao nhiêu đến từ dự báo đúng hướng đi của thị trường (Dynamic). [[Tuckman_Serrat_2022.md#page=79]] [[During_Fixed_Income_Ch22.md#page=217]]

---

## 1. P&L Attribution Framework (Tuckman's Lens)

Tổng lợi nhuận của một vị thế trái phiếu ($\text{Total Return}$) được phân rã thành 3 thành phần mỏ neo:

1.  **Carry (Lợi thế tài trợ):** Chênh lệch giữa coupon thu được và chi phí vay vốn (Repo). Đây là lợi nhuận nếu giá trái phiếu không đổi.
2.  **Roll-Down (Lợi nhuận lão hóa):** Lợi nhuận từ việc trái phiếu "trượt" xuống phần thấp hơn của đường cong lợi suất khi kỳ hạn ngắn lại. 
    - **Static Return = Carry + Roll-down.** Đây là mức lợi nhuận "hứa hẹn" nếu cấu trúc kỳ hạn không thay đổi.
3.  **Market Moves (Biến động thị trường):** Phần lợi nhuận (hoặc lỗ) do toàn bộ đường cong dịch chuyển hoặc do rủi ro tín dụng riêng lẻ thay đổi. [[Tuckman_Serrat_2022.md#page=82]]

---

## 2. Static Return Components (Düring's Lens)

### A. The Buffer (Break-Even Yield Shift)
Thước đo "độ bền" của một giao dịch trước các cú shock lãi suất:
$$\text{Buffer} = \frac{\text{Carry} + \text{Roll-down}}{\text{Forward-dated DV01}}$$
- **Interpretation:** Nếu một trái phiếu có Buffer 30bp, đường cong có thể tăng 30 điểm cơ bản trong một năm trước khi vị thế bắt đầu thua lỗ. [[During_Fixed_Income_Ch22.md#page=219]]

### B. The 4-9Y Sweet Spot
Düring bóc tách dữ liệu thực nghiệm: vùng bụng (4Y–9Y) thường mang lại Roll-down tối ưu do đây là khu vực đường cong có độ dốc (slope) lớn nhất, tạo ra "gia tốc" giảm lợi suất mạnh nhất khi trái phiếu già đi. [[During_Fixed_Income_Ch22.md#page=219]]

---

## 3. The Slope Hierarchy (Tuckman & Düring)

Trong môi trường đường cong dốc lên (normal curve):
$$\text{Forward Rate} > \text{Zero Rate} > \text{Par Yield}$$
- **Forward Rate:** Phản ánh tổng lợi nhuận tĩnh (Static Return).
- **Par Yield:** Phản ánh mức coupon cần thiết để trái phiếu giao dịch tại giá 100.
- **Strategic Note:** Tuckman nhấn mạnh rằng sự chênh lệch giữa Forward và Par chính là "động cơ" tạo ra Roll-down. [[Tuckman_Serrat_2022.md#page=71]]

---

## 4. EME Strategic Core (Warjiyo's Lens)

Perry Warjiyo bóc tách ranh giới của dòng vốn PI vào các EME:
- **Carry-to-Risk:** Các quốc gia như Indonesia thu hút vốn bằng cách duy trì độ dốc đường cong lớn, tạo ra vùng đệm (Buffer) đủ dày để bù đắp cho rủi ro biến động tỷ giá.
- **The Sudden Stop:** Khi rủi ro toàn cầu tăng, nhà đầu tư lo ngại biến động tỷ giá sẽ "thủng" vùng đệm này, dẫn đến việc tháo chạy hàng loạt bất chấp Roll-down vẫn đang rất hấp dẫn. [[Perry_Central_Bank_Policy_P6.md#page=394]]

---

## Evidence / Source Anchors

- Framework for P&L attribution (Static vs. Dynamic): [[Tuckman_Serrat_2022.md#page=79]]
- Mathematical formula for the Buffer using Forward-dated DV01: [[During_Fixed_Income_Ch22.md#page=219]]
- Establishment of the slope hierarchy (Forward > Zero > Par): [[Tuckman_Serrat_2022.md#page=71]]
- Identification of carry and roll-down as primary pull factors for EME debt: [[Perry_Central_Bank_Policy_P6.md#page=394]]

## Related

- [[Yield_Curve_Structure_And_Mechanics]] — The foundation for all return calculations.
- [[Bond_Carry_And_Forward_Pricing]] — Detailed view of the Carry component.
- [[Principal_Component_Analysis_PCA]] — Decomposing the 'Market Moves' component.
- [[Foreign_Capital_Flows_Determinants]] — The macro-impact of these returns.
