---
title: "Cross-Currency Basis"
aliases:
  - XCCY Basis
  - Basis Spread
  - CIP Deviation
  - Độ lệch CIP
type: mechanism
tags:
  - fx
  - swaps
  - liquidity
  - monetary-policy
status: active
confidence: 5
provenance: "Ulrich Bindseil - Central Bank Operations (2014) & Neftci (2008)"
thesis: "Cross-Currency Basis là mức chênh lệch lãi suất (spread) cộng thêm vào chân ngoại tệ trong một giao dịch hoán đổi tiền tệ, phản ánh sự lệch pha giữa lý thuyết Covered Interest Parity (CIP) và thực tế thị trường do các rào cản về quy định, thanh khoản và nhu cầu phòng vệ."
source_refs:
  - file: "Principles_of_Financial_Engineering_Neftci.md"
    page: 203
  - file: "Interest_Rate_Parity.md"
created: 2026-04-24
updated: 2026-04-24
---

## Thesis

[RAW] Trong điều kiện lý thuyết CIP hoàn hảo, Cross-Currency Basis bằng 0. Tuy nhiên, kể từ sau GFC 2008, Basis thường xuyên duy trì ở mức âm (đặc biệt đối với cặp EUR/USD và JPY/USD), biến nó thành một "loại tiền tệ" riêng biệt đo lường chi phí tiếp cận thanh khoản USD. [[Principles_of_Financial_Engineering_Neftci.md#page=203]]

---

## 1. The Pricing Equation (CIP Deviation)

Công thức định giá Forward có điều chỉnh Basis ($b$):
$$ F = S \times \frac{1 + (r_d \times \delta)}{1 + (r_f + b) \times \delta} $$
Trong đó:
- $r_d$: Lãi suất đồng tiền định giá (Domestic/Quote).
- $r_f$: Lãi suất đồng tiền cơ sở (Foreign/Base).
- $b$: **Cross-Currency Basis**.

### Quy ước dấu:
- **Negative Basis ($b < 0$):** Đồng tiền cơ sở (thường là USD) đắt hơn so với lý thuyết. Bên vay USD qua Swap phải trả thêm phí.
- **Positive Basis ($b > 0$):** Đồng tiền cơ sở rẻ hơn lý thuyết.

---

## 2. Drivers of the Basis (Tại sao CIP bị phá vỡ?)

### 2.1. Regulatory Frictions (Rào cản quy định)
[LLM] Sau GFC, các quy định như **Leverage Ratio (Basel III)** khiến các ngân hàng không thể thực hiện arbitrage vô hạn. Việc phình to bảng cân đối để ăn chênh lệch Basis vài bps không còn hiệu quả về mặt chi phí vốn (ROE).

### 2.2. Supply-Demand Imbalance (Mất cân đối cung cầu)
- **Hedging Pressure:** Các tổ chức tài chính lớn (Bảo hiểm, Quỹ hưu bổng Nhật/EU) có nhu cầu phòng vệ tỷ giá rất lớn khi đầu tư vào tài sản USD. Điều này tạo ra nhu cầu vay USD qua Swap một chiều.
- **Corporate Issuance:** Các công ty phát hành trái phiếu bằng ngoại tệ (e.g., Apple phát hành trái phiếu EUR) rồi hoán đổi lại sang USD cũng tác động mạnh đến Basis.

### 2.3. Liquidity Stress (Căng thẳng thanh khoản)
Trong các giai đoạn khủng hoảng, Basis trở thành thước đo sự hoảng loạn. Khi thị trường liên ngân hàng USD đóng băng, XCCY Basis là kênh duy nhất để các ngân hàng ngoài Mỹ tiếp cận USD, đẩy Basis âm rất sâu.

---

## 3. Transmission via T-Accounts (Basis Trade)

Khi một ngân hàng Châu Âu cần USD và chấp nhận Basis âm (-30 bps):

| Assets [EU BANK] | Liabilities [EU BANK] |
| :--- | :--- |
| (1) + USD Cash (t=0) | (1) + EUR Liability (XCCY Swap) |
| (2) - EUR ESTR + 30bps (Interest paid) | (2) + USD SOFR (Interest received) |
| **Net Cost:** | **SOFR + (ESTR - (ESTR - 30bps)) = SOFR + 30bps** |

*Kết quả: Ngân hàng EU phải trả chi phí vay USD cao hơn lãi suất SOFR thị trường 30 điểm cơ bản.*

---

## 4. Historical Context: March 2020
[WIKI] Trong đại dịch COVID-19, XCCY Basis của JPY/USD và EUR/USD đã sụt giảm mạnh (âm sâu) trước khi Fed kích hoạt các đường dây hoán đổi (Swap Lines) với các ngân hàng trung ương khác để bơm thanh khoản USD toàn cầu, giúp kéo Basis trở lại mức cân bằng.

## Evidence / Source Anchors
- Definition and GFC impact on Basis: [[Principles_of_Financial_Engineering_Neftci.md#page=203]]
- Link to Leverage Ratio and Arbitrage limits: [[Principles_of_Financial_Engineering_Neftci.md#page=204]]

## Related
- [[FX_Swap_Engineering]]
- [[Currency_Swap_Engineering]]
- [[Interest_Rate_Parity]]
- [[Central_Bank_Swap_Lines]]
