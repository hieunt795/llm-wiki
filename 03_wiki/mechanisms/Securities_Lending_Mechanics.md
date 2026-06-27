---
title: Securities Lending Mechanics
aliases:
- Cho vay chứng khoán
- Stock Lending
- Securities Borrowing
type: mechanism
tags:
- market-infrastructure
- liquidity
- equity
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Securities lending is the process of temporarily transferring securities to
  a borrower in exchange for a fee, primarily driven by the borrower's need to possess
  the specific asset rather than the lender's need for cash.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 156
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Mặc dù có kết quả kinh tế tương tự Repo (chuyển giao chứng khoán lấy tài sản đảm bảo), Securities Lending khác biệt ở động lực giao dịch. Trong Repo, bên đưa chứng khoán thường cần tiền mặt; trong Securities Lending, bên nhận chứng khoán mới là bên chủ động vì nhu cầu thực hiện nghĩa vụ giao hàng (settlement) hoặc bán khống.

## 1. Mechanism: Fee-based Exchange
[RAW] Quy trình thực hiện:
1.  **Lending:** Bên sở hữu chứng khoán (thường là các quỹ hưu trí, Custodian Banks) cho mượn tài sản.
2.  **Collateralization:** Bên mượn đưa tài sản đảm bảo (Tiền mặt, chứng khoán khác, hoặc Thư tín dụng - L/C). Giá trị tài sản đảm bảo phải ít nhất bằng giá trị thị trường của chứng khoán mượn.
3.  **The Fee:** Khác với lãi suất Repo, Securities Lending được báo giá bằng một khoản phí (e.g., 50 bps).

## 2. Worked Example (Neftci)
[RAW] Một Bond Dealer bán khống trái phiếu GBP 10 triệu nhưng không tìm được hàng để giao vào ngày thanh toán (Failure to deliver).
- **Scenario:** Euroclear tự động thực hiện cơ chế cho vay chứng khoán để cứu Dealer.
- **Mechanism:** Euroclear mượn ngẫu nhiên từ một thành viên khác và cho Dealer mượn lại.
- **Result:** Dealer trả phí (ví dụ 50 bp tính trên 14 ngày) để tránh lỗi thanh toán. Tài sản đảm bảo là một mã chứng khoán khác trị giá GBP 10.62 triệu.

## 3. Boundary Conditions
- **Motivation:** Lenders trong Securities Lending không cần tiền mặt (họ có thể đã có dư thừa thanh khoản), họ tham gia để tối ưu hóa lợi suất từ kho chứng khoán đang nằm yên.
- **Collateral Flexibility:** Chấp nhận các loại tài sản đảm bảo phi tiền mặt (non-cash collateral) rộng rãi hơn Repo.

## 4. The Prime Broker as Intermediary
[RAW] Prime brokers’ securities lending divisions have better information on borrowable assets.
[LLM] Trong cấu trúc thị trường hiện đại, [[Prime_Broker]] đóng vai trò là "Matching Engine" giữa các Institutional Lenders (Custodian Banks, Quỹ hưu trí) và các Hedge Funds có nhu cầu bán khống.
- **Revenue Model**: PBs kiếm lợi nhuận từ chênh lệch phí (spread) giữa mức họ trả cho lender và mức họ thu từ hedge fund, cộng với commission.
- **Information Centralization**: PBs tích hợp dữ liệu từ nhiều nguồn để biết chính xác chứng khoán nào "easy-to-borrow" (ETB) và chứng khoán nào "hard-to-borrow" (HTB).

## Related
- [[Short_Selling_Market_Microstructure]] — Động lực chính của mượn chứng khoán.
- [[Repurchase_Agreement_Mechanism]] — So sánh cơ chế vay vốn có đảm bảo.
- [[Settlement_Fails_And_Cures]] — Ứng dụng để tránh lỗi thanh toán.
