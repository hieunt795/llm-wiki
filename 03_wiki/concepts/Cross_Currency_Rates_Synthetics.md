---
title: Cross Currency Rates as Synthetics
aliases:
- Tỷ giá chéo và Giao dịch tổng hợp
- Cross Rates via USD
type: concept
tags:
- fx
- liquidity
- execution
- transaction-costs
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: 'Tỷ giá chéo (ví dụ: EUR/JPY) thường được thực hiện dưới dạng giao dịch tổng
  hợp sử dụng USD làm đồng tiền trung gian vì tính thanh khoản cao và chi phí giao
  dịch thấp của các cặp tiền tệ chính liên quan đến USD.'
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 189
created: '2026-04-21'
updated: '2026-04-21'
---

## Overview

[RAW] **Tỷ giá chéo** (Cross rate) là giá của một cặp tiền tệ không bao gồm đồng USD (như EUR/JPY, EUR/CHF, GBP/EUR). Mặc dù có thể mua trực tiếp các cặp tiền này, các Dealer thường chọn cấu trúc tổng hợp thông qua USD vì lý do chi phí. [[Principles_of_Financial_Engineering_Neftci.md#page=189]]

---

## 1. Mechanism of Synthetic Cross Rate

Thay vì thực hiện một giao dịch giao ngay trực tiếp giữa hai đồng tiền hiếm, nhà đầu tư thực hiện hai giao dịch riêng lẻ với USD.

### Contractual Equation
$$ \text{Buy CHF using Taiwan Dollars (TWD)} = \text{Buy USD against TWD} + \text{Sell USD against CHF} $$

**Các bước thực hiện:**
1. **Transaction 1:** Đổi đồng tiền nội địa (TWD) lấy USD.
2. **Transaction 2:** Đổi USD vừa nhận được để lấy đồng tiền đích (CHF).
3. **Kết quả:** Đồng USD được triệt tiêu, để lại kết quả cuối cùng là sở hữu CHF bằng TWD.

---

## 2. Worked Example (The Taiwan CHF Trade)

[RAW] Tại sao một nhà giao dịch tại Đài Loan muốn mua Franc Thụy Sĩ (CHF) lại chọn thực hiện qua hai bước thay vì mua trực tiếp? [[Principles_of_Financial_Engineering_Neftci.md#page=189]]

### Phân tích chi phí:
- **Cặp trực tiếp (CHF/TWD):** Thị trường hẹp, Bid-Ask spread rộng do thiếu thanh khoản.
- **Cặp tổng hợp (USD/TWD + USD/CHF):** Cả hai đều là các cặp tiền tệ cực kỳ thanh khoản với spread rất mỏng.
- **Tổng hợp:** Phí giao dịch của hai bước (USD/TWD và USD/CHF) cộng lại thường vẫn thấp hơn phí giao dịch của một bước trực tiếp.

---

## 3. Transmission Diagram (ASCII)

  [TWD] ────────(1) Buy USD───────> [USD] ────────(2) Sell USD───────> [CHF]
     │                                ^                                 │
     │                                │ (Intermediate Step)             │
     └────────────────────────────────┼─────────────────────────────────┘
                                 (Net result: TWD/CHF)

---

## Failure Conditions

- **Direct Liquidity Spike:** Nếu một cặp chéo (ví dụ: EUR/JPY) có biến động cực lớn hoặc thanh khoản tập trung đột ngột, việc thực hiện qua hai bước USD có thể gây ra rủi ro trễ thời gian (latency risk).
- **USD Volatility:** Nếu đồng USD biến động cực mạnh trong tích tắc giữa hai giao dịch, lợi thế về spread có thể bị xóa sạch bởi rủi ro biến động giá.

---

## Related
- [[FX_Forward_Engineering]]
- [[Japanese_Premium_Synthetic_Loans]]

─────────────────────────────────────────────
WRITEBACK
> [TYPE 2: SPAWN] Cross_Currency_Rates_Synthetics.md — Ingested from Neftci Ch 6.5.4.
- [[Cross_Currency_Basis]]
- [[Cross_Currency_Repo]]
