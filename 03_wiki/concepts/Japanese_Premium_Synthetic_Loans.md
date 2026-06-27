---
title: Japanese Premium & Synthetic Loans
aliases:
- Phí chênh lệch Nhật Bản và Khoản vay tổng hợp
- Synthetic USD Loan via JPY
type: concept
tags:
- liquidity
- funding
- banking-crisis
- fx-swaps
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: 'Khi việc huy động vốn trực tiếp trong một đồng tiền (ví dụ: USD) bị hạn chế
  hoặc quá đắt đỏ do rủi ro tín dụng của bên vay (như Japanese Premium), các ngân
  hàng có thể tạo ra các khoản vay tổng hợp bằng cách sử dụng nguồn vốn rẻ hơn (ví
  dụ: JPY) kết hợp với các nghiệp vụ FX Spot và Forward.'
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 187
created: '2026-04-21'
updated: '2026-04-21'
---

## Overview

[RAW] **Japanese Premium** là một sự kiện lịch sử (đặc biệt trong năm 1997 sau khi Ngân hàng Hokkaido Takushoku sụp đổ) mô tả tình trạng các ngân hàng Nhật Bản phải trả một mức phí bổ sung cực lớn để vay USD trên thị trường liên ngân hàng. [[Principles_of_Financial_Engineering_Neftci.md#page=187]]

---

## 1. Mechanism of Synthetic USD Loan

Để lách mức phí này, các ngân hàng Nhật Bản đã chuyển sang huy động đồng Yên (JPY) nội địa và chuyển đổi sang USD bằng kỹ thuật "tổng hợp".

### Contractual Equation
$$ \text{Synthetic USD Loan} = \text{Borrow JPY} + \text{Spot (Buy USD / Sell JPY)} + \text{FX Forward (Sell USD / Buy JPY)} $$

**Transmission Flow:**
1. **Borrow JPY:** Vay JPY trên thị trường nội địa (thông thường rẻ hơn và dễ tiếp cận hơn đối với các ngân hàng Nhật).
2. **Spot Operation:** Dùng số JPY vay được để mua USD ngay trên thị trường Spot.
3. **FX Forward:** Ký hợp đồng bán kỳ hạn USD (để mua lại JPY) tại thời điểm đáo hạn. Điều này giúp chốt chi phí trả nợ bằng JPY ban đầu và loại bỏ rủi ro tỷ giá.

---

## 2. Worked Example (Market Event 1997)

[RAW] Vào tháng 11/1997, mức "Japanese premium" trong thị trường tiền gửi Eurodollar tăng vọt từ 30 bp lên 40 bp so với các khoản vay của Mỹ có cùng xếp hạng tín nhiệm. [[Principles_of_Financial_Engineering_Neftci.md#page=187]]

### Phản ứng thị trường:
- Thay vì vay trực tiếp USD, các ngân hàng Nhật vay JPY nội địa.
- Họ bán JPY để mua USD Spot và mua JPY kỳ hạn (bán USD kỳ hạn).
- **Hệ quả:** Hoạt động này làm tăng mạnh cầu mua JPY kỳ hạn, dẫn đến tỷ giá kỳ hạn USD/JPY trở nên "đắt đỏ" một cách bất thường (richen dramatically).

---

## 3. Balance Sheet Transmission (ASCII)

  [JAPANESE BANK]
  Assets              │  Liabilities
  ────────────────────┼──────────────────────────
  (1) + JPY Cash ───> │ (1) + JPY Loan
  (2) - JPY Cash      │
  (2) + USD Cash ───> │
  ┌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┐
  ┆ (3) Forward Commit: Sell USD / Buy JPY  ┆ (Off-balance sheet)
  └╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘

---

## Failure Conditions

- **Forward Liquidity:** Nếu thị trường Forward bị khô hạn thanh khoản, ngân hàng sẽ không thể chốt được tỷ giá hoán đổi JPY, gây ra rủi ro tỷ giá (FX exposure).
- **Interest Rate Volatility:** Nếu lãi suất JPY nội địa tăng vọt đồng thời với USD, lợi thế của khoản vay tổng hợp sẽ biến mất.
- **Basis Risk:** Sự chênh lệch giữa LIBOR và lãi suất vay thực tế có thể tạo ra rủi ro Basis.

---

## Related
- [[FX_Forward_Engineering]]
- [[Capital_Controls_Synthetic_Spot]]
- [[Tax_Arbitrage_Synthetic_Bonds]]

─────────────────────────────────────────────
WRITEBACK
> [TYPE 2: SPAWN] Japanese_Premium_Synthetic_Loans.md — Ingested from Neftci Ch 6.5.2.
