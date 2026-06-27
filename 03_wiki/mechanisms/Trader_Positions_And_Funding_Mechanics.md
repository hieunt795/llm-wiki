---
title: Trader Positions & Funding Mechanics
aliases:
- Long Position Funding
- Short Position Funding
- Payoff Diagrams
type: mechanism
tags:
- trading
- funding
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: From a practitioner's perspective, positions (long or short) are initiated
  with zero net worth by borrowing either cash (to go long) or the asset (to go short),
  resulting in a linear payoff profile relative to price changes.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 42
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Khác với nhà đầu tư cá nhân sử dụng vốn tự có, một chuyên gia thị trường (market professional) "không bao giờ có tiền". Mọi vị thế đều bắt đầu từ con số 0 thông qua việc vay mượn.

## 1. Transmission Mechanism: Funding the Position

### A. Long Position (Funding)
[RAW] Để mua một tài sản giá 100:
1.  **Borrowing:** Trader vay 100 USD (Liabilities).
2.  **Purchasing:** Trader dùng 100 USD mua tài sản (Assets).
- **At inception:** Net Worth = 100 (Asset) - 100 (Loan) = 0.
- **Payoff:** Đường thẳng dốc lên ($+1$). Lợi nhuận phát sinh từ chênh lệch $\Delta P$ sau khi đã trừ chi phí lãi vay (funding cost).

### B. Short Position (Borrowing Asset)
[RAW] Để bán khống một tài sản giá 100:
1.  **Borrowing Asset:** Trader mượn tài sản giá 100 (Liabilities).
2.  **Selling:** Trader bán tài sản lấy 100 USD tiền mặt (Assets).
- **At inception:** Net Worth = 100 (Cash) - 100 (Asset Liability) = 0.
- **Payoff:** Đường thẳng dốc xuống ($-1$). Lợi nhuận phát sinh khi giá tài sản giảm, cho phép mua lại tài sản rẻ hơn để trả nợ.

## 2. Worked Example: Zero Value Instruments
[RAW] Trader ưu tiên các công cụ có giá trị bằng 0 tại thời điểm khởi đầu (như Swaps, Forwards):
- **Mechanism:** Không yêu cầu vay vốn ban đầu để mua tài sản.
- **Result:** Giảm áp lực lên bảng cân đối kế toán và hạn mức tín dụng (credit lines).

## 3. Boundary Conditions
- **Funding Costs:** Lợi nhuận thực tế phải vượt qua lãi suất vay vốn.
- **Collateral Haircuts:** Trong thực tế, việc vay 100% giá trị tài sản thường yêu cầu một phần ký quỹ (haircut), phá vỡ trạng thái "zero net worth" hoàn hảo.

## Related
- [[Short_Selling_Market_Microstructure]] — Chi tiết về rủi ro và chi phí khi bán khống.
- [[Forward_LIBOR_Loan_Mechanism]] — Công cụ "Additive Zero" dùng để biến đổi vị thế.
- [[Trader_Mental_Models_Neftci]] — Triết lý "Manufacturer perspective".
