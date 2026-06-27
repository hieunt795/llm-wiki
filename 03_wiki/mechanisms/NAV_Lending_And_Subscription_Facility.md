---
title: NAV Lending and Subscription Facility
aliases:
- Fund-level indebtedness
- Subscription Line
- NAV Financing
- Hidden Leverage
type: mechanism
tags:
- private-credit
- fund-financing
- leverage
- liquidity
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: Đây là hai công cụ tài trợ cấp quỹ (fund-level financing) tạo ra đòn bẩy bổ
  sung cho các quỹ [[Private_Credit]], thường được gọi là "hidden leverage" (đòn bẩy
  ẩn).
source_refs: []
created: '2026-04-13'
updated: '2026-04-16'
source: Deep Dive_ Private Credit.md
---

# NAV Lending and Subscription Facility

## Mechanism

Đây là hai công cụ tài trợ cấp quỹ (fund-level financing) tạo ra đòn bẩy bổ sung cho các quỹ [[Private_Credit]], thường được gọi là "hidden leverage" (đòn bẩy ẩn).

### 1. Subscription Facility (Subscription Line)
- **Định nghĩa**: Một khoản vay mà quỹ thực hiện dựa trên cam kết góp vốn chưa thực hiện (unfunded commitments) của các nhà đầu tư (LPs).
- **Mục tiêu**: Giúp quỹ thanh toán nhanh cho các deal mà không cần gọi vốn liên tục từ LPs.
- **Tác động**: Làm trì hoãn việc gọi vốn thực tế, từ đó **đẩy chỉ số IRR** lên cao hơn một cách ảo thuật vì thời gian tính toán ngắn lại. [extracted]
- **Cảnh báo từ SEC**: Phải trình bày hiệu suất một cách nhất quán khi có và không có tác động của Subscription Facility để tránh gây hiểu lầm cho nhà đầu tư. [extracted]

### 2. NAV Lending (NAV Financing)
- **Định nghĩa**: Các khoản vay mà quỹ thực hiện dựa trên giá trị và dòng tiền (NAV - Net Asset Value) của các khoản đầu tư hiện có trong danh mục.
- **Mục tiêu**: Cung cấp thêm thanh khoản cho quỹ để đầu tư thêm hoặc phân phối cho LPs khi các deal chưa thoát được (exit). [inferred]
- **Tác động**: Tạo ra một tầng đòn bẩy thứ hai — quỹ vay tiền dựa trên các khoản nợ mà doanh nghiệp đang vay. [extracted]

> [!CAUTION]
> Cả hai công cụ này đều có rủi ro: chúng biến một danh mục "hold-to-maturity" thành những công cụ tài chính có tính thanh khoản phụ thuộc vào **niềm tin của bên cho vay** (thường là ngân hàng) và việc định giá tài sản thế chấp. [extracted]

### Điều kiện và Rủi ro

- **Liquidity Mismatch**: Khi bên cho vay gọi nợ (margin call) hoặc không gia hạn hạn mức, quỹ có thể bị buộc phải bán tài sản với giá rẻ (fire sale). [inferred]
- **Valuation Event**: Trong bối cảnh stress, "liquidity event" (sự kiện thanh khoản) và "valuation event" (sự kiện định giá) sẽ hợp nhất — việc đánh giá sai lệch NAV sẽ làm rung chuyển toàn bộ cấu trúc nợ này. [extracted]

### Hình ảnh minh họa (Idea)

> **Leverage Layering Chart**: Vẽ một tòa tháp (Tầng dưới cùng: Portfolio Company Debt). Tầng giữa: Private Credit Fund (Sử dụng NAV Loan để tăng đòn bẩy). Tầng trên cùng: Subscription Facility (Vay dựa trên LP Commitments). Minh họa một mũi tên sét đánh trỏ vào "Bank Trust / Collateral Value" làm lung lay toàn bộ tòa tháp. [inferred]

## Evidence / Source Anchors

- [extracted] Arya Deniz, *Deep Dive: Private Credit*, Substack, 2026-04-07
- [extracted] SEC Marketing Rule Guidance (on subscription facilities)
- [extracted] Cadwalader, "Fund Finance Friday" (on NAV financing ratings)
- [extracted] Fitch, "NAV Finance Rating Methodology"

### Liên kết

- [[Private_Credit]] — bối cảnh mẹ
- [[Nonbank_Financial_Intermediation]] — một ví dụ về đòn bẩy phi ngân hàng
- [[Private_Credit_Valuation_Mark_To_Model]] — cơ sở tính toán NAV cho việc vay nợ
- [[Business_Development_Company]] — nơi đòn bẩy tập trung cao nhất
- [[Lender_Of_Last_Resort]] — rủi ro khi các ngân hàng cung cấp hạn mức cho vay này gặp stress


## Related

- [[NAV_Loans]]
- [[Subscription_Lines]]
