---
title: Trader Mental Models (Neftci)
aliases:
- Manufacturer Perspective
- Law of Two Prices
- Funding Constraints
type: perspective
tags:
- trading-strategy
- philosophy
- market-microstructure
status: verified
confidence: 5
half_life_years: 5
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Professional trading is viewed from a manufacturer's perspective, where practitioners
  face the 'law of two prices' (bid/ask) and operate under constant funding constraints.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 17
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Một nhà kỹ thuật tài chính (Financial Engineer) tiếp cận thị trường từ góc độ người "chế tạo" (Manufacturer/Dealer) sản phẩm, trái ngược với góc độ người dùng (User/Investor).

## 1. Core Logic: The Manufacturer Perspective
- **Manufacturer View:** Các ngân hàng, quỹ hưu trí và chính phủ là "khách hàng" (đối tác bên kia của deal). Trader nhìn nhận công cụ tài chính như một sản phẩm cần được lắp ráp từ các khối building blocks cơ bản.
- **The Law of Two Prices:** [RAW] Trái với kinh tế học vĩ mô (luật một giá), trader luôn đối mặt với hai mức giá: Bid (giá mua vào) và Ask (giá bán ra). Chênh lệch này không phải là chi phí, mà là doanh thu để bù đắp cho việc nắm giữ kho hàng (inventories) và rủi ro.

## 2. Worked Example: Funding Constraints
[RAW] Trong thực tế, một Practitioner "không bao giờ có sẵn tiền mặt". 
- **Mechanism:** Mọi vị thế mua đều phải được tài trợ (funded) bằng cách đi vay, và mọi vị thế bán đều tạo ra tiền mặt cần được tái đầu tư.
- **Result:** Đây là lý do tại sao các công cụ có **Zero-value at inception** (như Swaps, Forwards) được ưu tiên tuyệt đối. Chúng không làm phình bảng cân đối kế toán và không đòi hỏi chi phí funding trả trước (upfront cash).

## 3. Failure Conditions / Boundaries
- **Market Liquidity:** Khi thanh khoản cạn kiệt, chênh lệch Bid/Ask dãn rộng, phá vỡ mô hình lợi nhuận của "Manufacturer".
- **Regulatory Capital:** Mọi vị thế (ngay cả phái sinh) đều tiêu tốn vốn tự trọng (Capital Charge), tạo ra ranh giới cứng cho khả năng "chế tạo" sản phẩm của Dealer.

## Related
- [[Interest_Rate_Swap_Engineering]] — Ứng dụng của zero-value instruments.
- [[Market_Maker_Vs_Liquidity_Provider]] — Vai trò của Dealer trong việc báo giá hai chiều.
- [[Bid_Ask_Bounce]] — Hiện tượng kỹ thuật phát sinh từ quy tắc hai mức giá.
