---
title: Basis Swap Spreads and Valuation
aliases:
- Basis Swap
- Float-Float Swap
- Tenor Basis Swap
- OIS-Libor Basis
type: mechanism
tags:
- derivatives
- fixed-income
- pricing
status: reviewed
confidence: 5
half_life_years: 10
expert_lens: Bruce Tuckman | Angel Serrat
provenance: '[RAW-BOOK: Tuckman & Serrat (2022) Ch 13]'
thesis: A basis swap is a float-float interest rate swap where counterparties exchange two different floating rate indexes. Its valuation is anchored by the principle that while a risk-free floating leg is worth par, a risky or term-rate leg requires a basis spread to reach par value, reflecting liquidity and credit risk premia.
---

## Thesis

Trong thế giới hậu 2008, khái niệm "một đường cong lãi suất" đã sụp đổ. **Basis Swap** là công cụ để giao dịch và định giá sự khác biệt (spread) giữa các loại lãi suất nổi khác nhau (ví dụ: 3M Euribor vs €STR). Tuckman & Serrat giải mã cơ chế định giá "Two-Curve": dùng đường cong OIS để chiết khấu (discounting) và đường cong Term Rate để dự báo dòng tiền (projecting). [[Tuckman_Serrat_2022#page=348]]

---

## 1. Structural Identity: The "Par" Benchmark

DENSE UNPACK:
- **INTENT:** Xác định giá trị kinh tế của việc nắm giữ một lãi suất có rủi ro (term rate) so với một lãi suất phi rủi ro (OIS).
- **MECHANISM:**
  - Nếu lãi suất nổi là **risk-free** (ví dụ: OIS/SOFR), chân nổi (floating leg) luôn có giá trị bằng **Par** ($100$) tại mỗi ngày reset.
  - Nếu lãi suất nổi là **risky** hoặc có tính thanh khoản thấp (ví dụ: Euribor 3M), chân nổi này sẽ có giá trị **khác Par** nếu không có spread.
- **INTERACTIONS:** Trực tiếp dẫn dắt việc tính toán [[Asset_Swap_Spread_ASW]] và định giá các khoản vay ngân hàng.
- **BOUNDARY:** Cơ chế này giả định việc ký quỹ (collateralization) được thực hiện bằng tiền mặt lãi suất OIS. Nếu tài sản thế chấp khác đi, spread sẽ thay đổi.

---

## 2. Valuation Logic: The Two-Curve Framework

Tuckman & Serrat bóc tách công thức định giá chân nổi của một Basis Swap:

$$Value = Par + PV(\text{Basis Spread})$$

- **The Risk-Free Leg:** Luôn được định giá là Par vì lãi suất reset kỳ vọng khớp chính xác với tỷ lệ chiết khấu OIS.
- **The Term-Rate Leg:** Phải cộng thêm một khoản spread ($s$) để tổng PV của nó bằng Par:
  $$\sum_{i=1}^n \frac{(L_i + s) \times \tau_i \times Notional}{DF_i} + \frac{Notional}{DF_n} = Notional$$
  *Trong đó $L_i$ là term rate dự báo, $DF_i$ là discount factor từ OIS.*

### Euribor vs. €STR Example
Một giao dịch hoán đổi Euribor 3M lấy €STR (Overnight) phản ánh:
1. **Credit Risk:** Euribor chứa rủi ro liên ngân hàng.
2. **Liquidity Risk:** 3M funding khó khăn hơn Overnight funding.
3. **Tenor Basis:** Chênh lệch giữa việc vay 1 lần 3 tháng so với vay 90 lần qua đêm. [[Tuckman_Serrat_2022#page=349]]

---

## 3. Market Application: Spread Sensitivity

- **Hedging:** Các ngân hàng dùng Basis Swaps để khớp (match) tài sản (cho vay Euribor 3M) với nguồn vốn (huy động OIS).
- **Pricing:** Khi Basis Spread tăng, nó cho thấy sự thắt chặt trên thị trường vốn (funding stress), ngay cả khi lãi suất chính sách không đổi.

---

## Evidence / Source Anchors

- Floating leg worth par if rate is risk-free: [[Tuckman_Serrat_2022#page=348]]
- Basis Swap valuation formula ($Par + PV(Spread)$): [[Tuckman_Serrat_2022#page=349]]
- Two-Curve pricing rationale (OIS discounting vs Term projecting): [[Tuckman_Serrat_2022#page=348]]

## Related

- [[OIS_And_Benchmark_Reform]] — The transition from Libor to risk-free rates.
- [[Interest_Rate_Swap_Plain_Vanilla]] — The base instrument for swaps.
- [[Discount_Margin]] — Similar concept for Floating Rate Notes (FRNs).
- [[OIS_And_Tenor_Basis_Swaps]]
- [[Futures_Basis_And_Implied_Repo_Rate]]
