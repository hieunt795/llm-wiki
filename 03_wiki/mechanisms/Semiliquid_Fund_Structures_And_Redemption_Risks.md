---
title: Semiliquid Fund Structures and Redemption Risks
aliases:
- Semi-liquid Funds
- Interval Funds
- Redemption Gate
- Liquidity Mismatch in Private Credit
- Quỹ bán thanh khoản
type: mechanism
tags:
- private-credit
- liquidity
- risk-management
- investment-funds
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: Deep Dive_ Private Credit (2024)
thesis: Semiliquid fund structures, such as perpetual non-traded BDCs, create a structural
  liquidity mismatch by offering periodic redemptions to investors while holding illiquid
  private assets, relying on 'redemption gates' as a primary but potentially destabilizing
  defense mechanism during market stress.
source_refs:
- file: Deep Dive_ Private Credit.md
  page: 15
- file: Deep Dive_ Private Credit.md
  page: 16
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Làm sao để bán một tài sản không thanh khoản cho nhà đầu tư nhỏ lẻ? Các công ty quản lý quỹ (như Blackstone, Blue Owl) giải mã cơ chế thông qua **Quỹ bán thanh khoản (Semiliquid Funds)**. Đây là mỏ neo tăng trưởng của Private Credit, nhưng ranh giới của nó nằm ở một nghịch lý: quỹ hứa hẹn thanh khoản dựa trên giả định rằng không phải ai cũng rút vốn cùng một lúc. Khi giả định này sụp đổ, ranh giới giữa một quỹ đầu tư và một cuộc tháo chạy ngân hàng (Bank Run) trở nên cực kỳ mong manh. [[Deep Dive_ Private Credit.md#page=15]]

---

## 1. Mechanism: The Liquidity Bridge

Khác với các quỹ đóng (Closed-end funds) truyền thống khóa vốn trong 10 năm, Semiliquid funds (ví dụ BCRED) cho phép:
- **Subscriptions:** Huy động vốn hàng tháng từ nhà đầu tư.
- **Redemptions:** Cho phép rút vốn hàng quý (thường giới hạn ở mức 5% tổng giá trị tài sản ròng - NAV).
- **The Asset Side:** Toàn bộ số tiền này được dùng để cho doanh nghiệp vay dài hạn (Direct Lending) với kỳ hạn 5-7 năm. [[Deep Dive_ Private Credit.md#page=15]]

---

## 2. Defensive Gates (Ranh giới phòng thủ)

Để bảo vệ quỹ khỏi việc phải bán tháo tài sản (Fire Sales), các quỹ này thiết lập các rào chắn:
- **Redemption Gates:** Nếu tổng yêu cầu rút vốn vượt quá 5% NAV trong một quý, quỹ có quyền từ chối phần vượt quá.
- **Side Pockets:** Tách riêng các tài sản xấu hoặc cực kỳ khó bán ra khỏi danh mục chung để không làm ảnh hưởng đến giá NAV của những người ở lại.
- **The Stigma:** Düring và IMF cảnh báo ranh giới tâm lý — việc kích hoạt "Gate" thường là tín hiệu báo động, khiến những nhà đầu tư còn lại hoảng loạn và nộp lệnh rút vốn cho kỳ sau, tạo ra hiện tượng **Nghẽn cổ chai thanh khoản**. [[Deep Dive_ Private Credit.md#page=16]]

---

## 3. Strategic Implications: The Retailization Risk

Tài liệu bóc tách ranh giới của việc "Retailization" (Bán lẻ hóa) Private Credit:
- **Information Asymmetry:** Nhà đầu tư cá nhân không có khả năng thẩm định các khoản vay phức tạp bên dưới, họ chỉ nhìn vào mức lợi suất ổn định và uy tín của thương hiệu quản lý quỹ.
- **The Feedback Loop:** Khi lãi suất tăng, chi phí vốn của người đi vay tăng, làm NAV của quỹ giảm. Nếu NAV giảm đột ngột, nhà đầu tư cá nhân—vốn nhạy cảm với rủi ro hơn nhà đầu tư định chế—sẽ kích hoạt đợt tháo chạy thanh khoản. [[Deep Dive_ Private Credit.md#page=16]]

---

## Evidence / Source Anchors

- Analysis of the 5% quarterly redemption limit in semiliquid BDCs: [[Deep Dive_ Private Credit.md#page=15]]
- Description of redemption gates as a tool to prevent fire sales: [[Deep Dive_ Private Credit.md#page=15]]
- Case study of the 'Barings Flash Point' and its impact on fund flows: [[Deep Dive_ Private Credit.md#page=15]]
- Identification of the mismatch between perpetual fundraising and illiquid lending: [[Deep Dive_ Private Credit.md#page=15]]

## Related

- [[Securitization_And_Asset_Based_Finance_ABF]] — The asset side of these funds.
- [[Systemic_Risk_Taxonomy]] — Why semiliquid funds shift risk to the network dimension.
- [[Fire_Sale_Mechanism]] — The consequence of gate failure.
- [[Lender_Of_Last_Resort_Mechanism]] — Should central banks rescue non-bank semiliquid funds?
- [[Semiliquid_Fund_Structures]]
- [[Rehypothecation_Mechanism_And_Risks]]
- [[Bid_Ask_Bounce]]
- [[Liquidity_Measurement_Taxonomy]]
- [[Margining]]
- [[Market_Depth_Vs_Breadth]]
- [[Bank_Deposit_Types]]
- [[Private_Credit_Secondary_Market]]
