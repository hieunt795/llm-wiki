---
title: Short Selling Market Microstructure
aliases:
- Short Selling Mechanics
- Stock Lending
- Recall Risk
- Short Squeeze
type: mechanism
tags:
- equity
- trading
- microstructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Short selling is not merely the inverse of going long; it involves a complex
  securities lending infrastructure, capital consumption via collateral, and significant
  operational risks such as recall risk and short squeezes.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 44
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Khác với lý thuyết học thuật, bán khống (short selling) trong thực tế tốn kém vốn (capital intensive) và mang theo các rủi ro không đối xứng mà vị thế mua (long) không có.

## 1. Transmission Mechanism: Stock Lending
[RAW] Quy trình thực hiện một lệnh bán khống:
1.  **Borrowing:** Trader mượn chứng khoán từ một Custodian Bank (như State Street) thông qua Broker Dealer.
2.  **Collateralization:** Trader phải đặt cọc bằng tiền mặt (Cash Collateral), thường là **102%** giá trị thị trường của chứng khoán đó. 
3.  **The Rebate Rate:** Bên cho vay trả lãi (rebate rate) cho khoản tiền cọc này. Chênh lệch giữa lãi suất thị trường và rebate rate chính là phí mượn chứng khoán (Loan Fee).

## 2. Worked Example: The Porsche-VW Short Squeeze (2008)
[RAW] Một ví dụ cực đoan về ranh giới thanh khoản:
- **Scenario:** Các quỹ đầu cơ bán khống cổ phiếu VW. Porsche âm thầm dùng derivatives để gom hơn 74% cổ phiếu lưu hành.
- **Mechanism:** Khi Porsche công bố sự thật, các quỹ đầu cơ nhận ra không còn cổ phiếu trên thị trường để mua lại và trả nợ (Short Squeeze).
- **Result:** Giá VW vọt từ <200 EUR lên >1000 EUR trong thời gian ngắn. Nhiều quỹ phá sản do không thể đóng vị thế (Infinite Squeeze).

## 3. Boundary Conditions & Risks
- **Recall Risk:** [RAW] Bên cho vay có quyền đòi lại chứng khoán bất cứ lúc nào (Open loan). Nếu không tìm được nguồn thay thế, trader buộc phải đóng vị thế ngay lập tức.
- **Capital Consumption:** Bán khống không giải phóng tiền mặt mà thực tế là "ngốn" vốn do yêu cầu ký quỹ 102%.
- **Dividend Obligation:** Trader bán khống có nghĩa vụ trả cổ tức cho bên cho vay nếu đợt chi trả diễn ra trong thời gian mượn.

## Related
- [[Trader_Positions_And_Funding_Mechanics]] — So sánh đồ thị Payoff.
- [[Margining]] — Cơ chế quản lý rủi ro bằng tiền ký quỹ.
- [[Put_Call_Parity]] — Mối quan hệ bị ảnh hưởng bởi chi phí vay chứng khoán.
