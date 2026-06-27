---
title: FX Forward Quoting Conventions
aliases:
- FX Forward Points
- Forward Pips
- Quy ước báo giá kỳ hạn
type: convention
tags:
- fx
- market-conventions
- forwards
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: FX Forward rates are typically quoted as forward points (pips) relative to
  the spot rate, rather than outright rates, reflecting the interest rate differential
  between two currencies.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 191
created: '2026-04-21'
updated: '2026-04-21'
---

## Thesis

[RAW] Trong thị trường FX chuyên nghiệp, tỷ giá kỳ hạn không được báo giá trực tiếp (outright). Thay vào đó, các Dealer báo giá "điểm kỳ hạn" (Forward Points hoặc Pips). Salih Neftci giải thích rằng quy ước này phản ánh sự tách biệt giữa biến động tỷ giá (Spot) và chênh lệch lãi suất (Forward points). [[Principles_of_Financial_Engineering_Neftci.md#page=191]]

---

## 1. Forward Points (Pips) Mechanics

Điểm kỳ hạn là sự chênh lệch giữa tỷ giá kỳ hạn ($F_{t0}$) và tỷ giá giao ngay ($e_{t0}$):
$$ \text{Forward Points} = (F_{t0} - e_{t0}) \times 10,000 $$

### The Addition/Subtraction Rule
Dealer thường chỉ báo giá các con số (e.g., 8/15). Để xác định nên cộng hay trừ các con số này vào tỷ giá Spot, ta sử dụng quy tắc:

- **Case 1: Bid Pips < Ask Pips (e.g., 8/15)**
  - **Action:** Cộng điểm vào Spot rate.
  - **Meaning:** Đồng tiền cơ sở (Base Currency) có lãi suất thấp hơn đồng tiền định giá (Quote Currency). Đồng tiền cơ sở đang ở trạng thái **Forward Premium**.
- **Case 2: Bid Pips > Ask Pips (e.g., 23/18)**
  - **Action:** Trừ điểm khỏi Spot rate.
  - **Meaning:** Đồng tiền cơ sở có lãi suất cao hơn. Đồng tiền cơ sở đang ở trạng thái **Forward Discount**.

---

## 2. Bid-Ask Spread Escalation

[RAW] Một đặc tính quan trọng của báo giá kỳ hạn là sự mở rộng của biên độ mua-bán (Spread). Tỷ giá kỳ hạn (outright forward) luôn có spread rộng hơn tỷ giá giao ngay (spot). [[Principles_of_Financial_Engineering_Neftci.md#page=193]]

### Numerical Rule:
- **Formula:** $Spread_{Forward} = Spread_{Spot} + Spread_{Points}$.
- **Logic:** Điều này phản ánh sự kết hợp giữa rủi ro thanh khoản của thị trường FX và thị trường tiền tệ (Money Market).

---

## 3. Worked Examples (Quantitative Ingest)

[RAW] Giả sử ta có các báo giá tỷ giá giao ngay (Spot) và điểm kỳ hạn (Forward Points) cho EUR/USD. [[Principles_of_Financial_Engineering_Neftci.md#page=192]]

### Example 1: Forward Premium (Add Points)
- **Spot Bid/Ask:** 1.0110 / 1.0120
- **Forward Points:** 12 / 16
- **Calculation:** Vì **Bid Points (12) < Ask Points (16)**, ta thực hiện phép cộng.
    - **Forward Bid:** $1.0110 + 0.0012 = 1.0122$
    - **Forward Ask:** $1.0120 + 0.0016 = 1.0136$
- **Spread Analysis:**
    - Spot Spread = 10 pips.
    - Forward Spread = 14 pips (1.0136 - 1.0122).

### Example 2: Forward Discount (Subtract Points)
- **Spot Bid/Ask:** 1.0110 / 1.0120
- **Forward Points:** 23 / 18
- **Calculation:** Vì **Bid Points (23) > Ask Points (18)**, ta thực hiện phép trừ.
    - **Forward Bid:** $1.0110 - 0.0023 = 1.0087$
    - **Forward Ask:** $1.0120 - 0.0018 = 1.0102$
- **Spread Analysis:**
    - Spot Spread = 10 pips.
    - Forward Spread = 15 pips (1.0102 - 1.0087).

---

## 4. Approximate Pricing Equation

Đối với các kỳ hạn ngắn, điểm kỳ hạn có thể được ước tính nhanh bằng công thức:
$$ F_{t0} - e_{t0} \approx e_{t0} \cdot (r_{dom} - r_{for}) \cdot \frac{\Delta t}{360} $$
Trong đó $r_{dom}$ và $r_{for}$ là lãi suất nội tệ và ngoại tệ tương ứng.

---

## Evidence / Source Anchors

- Forward points definition and quoting convention: [[Principles_of_Financial_Engineering_Neftci.md#page=191]]
- Rule for adding/subtracting pips based on Bid-Ask relationship: [[Principles_of_Financial_Engineering_Neftci.md#page=193]]
- Escalation of Bid-Ask spreads in forward rates: [[Principles_of_Financial_Engineering_Neftci.md#page=193]]

## Related

- [[FX_Forward_Engineering]] — Cơ sở kỹ thuật tài chính.
- [[Covered_Interest_Parity]] — Lý thuyết định giá cốt lõi.
- [[Japanese_Premium_Hedge]] — Ứng dụng khi Forward points bị "đội giá" (richen).
- [[FX_Spot_Trading_Mechanics]]
- [[FX_Swap_Engineering]]
- [[Order_Flow_FX_Determination]]
- [[Cross_Currency_Rates_Synthetics]]
- [[Forward_Volatility_Trading]]
- [[Tax_Arbitrage_Synthetic_Bonds]]
- [[Daycount_Conventions]]
- [[Mathematical_Conventions_Of_Interest_Accrual]]
- [[OTC_Trading_Conventions]]
- [[Exchange_Rate_Determination_Theories]]
