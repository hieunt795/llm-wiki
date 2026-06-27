---
title: Capital Controls & Synthetic Spot Operations
aliases:
- Kiểm soát vốn và Giao dịch Spot tổng hợp
- Parallel Loans
type: concept
tags:
- capital-controls
- arbitrage
- emerging-markets
- regulatory-arbitrage
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: 'Giao dịch Spot tổng hợp cho phép người tham gia thị trường lách các biện
  pháp kiểm soát vốn (ví dụ: cấm mua USD giao ngay) bằng cách kết hợp các công cụ
  phái sinh và thị trường tiền tệ.'
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 188
created: '2026-04-21'
updated: '2026-04-21'
---

## Overview

[RAW] Một số quốc gia áp đặt các hạn chế đối với việc di chuyển vốn, ví dụ như cấm mua USD giao ngay bằng nội tệ (X). Một kỹ sư tài chính có thể lách quy định này bằng cách tạo ra một cấu trúc tổng hợp tương đương với việc mua Spot. [[Principles_of_Financial_Engineering_Neftci.md#page=188]]

---

## 1. Mechanism of Synthetic Spot Purchase

Thay vì đổi trực tiếp X lấy USD, nhà đầu tư thực hiện một chuỗi giao dịch song song.

### Contractual Equation
$$ \text{Synthetic Spot (Buy USD / Sell X)} = \text{Borrow USD} + \text{FX Forward (Buy USD / Sell X)} + \text{Deposit X} $$

**Các bước thực hiện:**
1. **Borrow USD:** Vay USD từ một đối tác nước ngoài (không chịu kiểm soát vốn nội địa).
2. **Deposit X:** Gửi số tiền nội tệ X vào ngân hàng (làm tài sản đảm bảo hoặc để hưởng lãi suất).
3. **FX Forward:** Ký hợp đồng bán kỳ hạn X để mua USD trong tương lai tại thời điểm $t_1$.

---

## 2. Worked Example (Parallel Loans in Brazil)

[RAW] Một trong những tiền thân của cấu trúc này là các khoản "Vay song song" (Parallel Loans) được sử dụng rộng rãi bởi các doanh nghiệp, đặc biệt là ở Brazil và các thị trường mới nổi khác để huy động ngoại tệ khi có kiểm soát vốn. [[Principles_of_Financial_Engineering_Neftci.md#page=188]]

### Kịch bản:
- Quốc gia X cấm mua USD bằng đồng X.
- Doanh nghiệp cần USD để nhập khẩu máy móc.
- Doanh nghiệp vay USD từ ngân hàng quốc tế, đồng thời ký quỹ (deposit) một lượng đồng X tương đương tại chi nhánh nội địa của ngân hàng đó.
- Khi đến hạn, doanh nghiệp dùng đồng X để mua lại USD thông qua hợp đồng Forward để trả nợ.

---

## 3. Transmission Diagram (ASCII)

  [OFFSHORE ENTITY] <───(1) Borrow USD ─── [ONSHORE ENTITY]
                                              │
                                              │ (2) Deposit Local Currency (X)
                                              v
                                        [LOCAL BANK]
                                              │
                                              │ (3) Forward Buy USD / Sell X
                                              v
                                        [FX MARKET]

---

## Failure Conditions

- **Direct Borrowing Prohibition:** Nếu quy định cấm luôn cả việc vay ngoại tệ (External debt), cấu trúc này sẽ thất bại.
- **Convertibility Risk:** Ngay cả khi có Forward, nếu chính phủ tuyên bố đình chỉ việc chuyển đổi (Moratorium), nhà đầu tư sẽ không thể lấy được USD để trả nợ.
- **Basis Premium:** Chi phí vay USD (External) cộng với chi phí Forward có thể cao hơn nhiều so với tỷ giá Spot kỳ vọng, tạo ra một khoản "thuế" ẩn cho việc lách quy định.

---

## Related
- [[FX_Forward_Engineering]]
- [[Japanese_Premium_Synthetic_Loans]]
- [[Covered_Interest_Parity]]

─────────────────────────────────────────────
WRITEBACK
> [TYPE 2: SPAWN] Capital_Controls_Synthetic_Spot.md — Ingested from Neftci Ch 6.5.3.
