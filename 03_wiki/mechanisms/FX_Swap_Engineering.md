---
title: FX Swap Engineering
aliases:
- FX Swap
- Foreign Exchange Swap
- Hoán đổi tỷ giá
- FX Swap-implied Rate
type: mechanism
tags:
- fx
- swaps
- funding
- money-market
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: An FX Swap is a simultaneous spot purchase and forward sale (or vice-versa)
  of a currency, functioning economically as a collateralized loan while remaining
  off-balance sheet.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 194
created: '2026-04-21'
updated: '2026-04-21'
---

## Thesis

[RAW] FX Swap là công cụ lỏng nhất trong thị trường ngoại hối (chiếm ~42% doanh số). Salih Neftci định nghĩa FX Swap là sự kết hợp của một khoản vay và một khoản tiền gửi khác đồng tiền được ghi trên cùng một "ticket". Đây là công cụ ưu việt để quản lý thanh khoản ngắn hạn mà không làm phình to bảng cân đối kế toán. [[Principles_of_Financial_Engineering_Neftci.md#page=194]]

---

## 1. Structure and Interpretation

Một FX Swap (e.g., Mua Spot USD / Bán Forward USD bằng EUR) có hai cách hiểu:
1.  **Market Interpretation:** Trao đổi một lượng EUR lấy USD ngay hôm nay ($t_0$) và cam kết trao đổi ngược lại tại một tỷ giá xác định ($F_{t0}$) trong tương lai ($t_1$).
2.  **Financial Engineering Interpretation:** Vay EUR (Collateral) và cho vay USD (hoặc ngược lại). Mỗi bên dùng đồng tiền của mình làm tài sản đảm bảo cho đồng tiền mượn được.

### T-Shape Transmission (Interbank Swap)

┌─────────────────────────────────────────────────────────────┐
│        [BANK A] (USD Borrower) │       [BANK B] (EUR Borrower)    │
│   Assets      │ Liabilities    │   Assets      │ Liabilities      │
│───────────────┼────────────────┼───────────────┼──────────────────│
│ (1) + Cash USD│ (1) + Loan EUR ┼──> (1) - Cash USD │ (1) - Loan EUR   │
│ (2) - Cash USD│ (2) - Loan EUR <──┼ (2) + Cash USD │ (2) + Loan EUR   │
└─────────────────────────────────────────────────────────────┘
(1) Leg 1: Spot exchange at t0.
(2) Leg 2: Forward re-exchange at t1 (at Forward rate F).

---

## 2. The Implied Funding Rate

[RAW] Chi phí vay USD ngầm định từ một giao dịch FX Swap (sử dụng đồng EUR làm nguồn tài trợ) được tính bằng công thức:
$$ r_{USD}^{implied} = \frac{F_{t0}}{e_{t0}} \cdot (1 + r_{EUR} \cdot \delta) - 1 $$
- **Significance:** Nếu $r_{USD}^{implied}$ cao hơn đáng kể so với USD Libor/SOFR, đó là dấu hiệu của sự thắt chặt thanh khoản USD (USD funding squeeze). [[Principles_of_Financial_Engineering_Neftci.md#page=197]]

### 2.1. Phân biệt Swap Points âm và Khan hiếm thanh khoản
Cần phân biệt rõ ranh giới giữa biến động lãi suất và biến động thanh khoản:
- **Swap Points âm (Discount):** Thường là trạng thái bình thường khi lãi suất đồng tiền mượn ($r_{USD}$) thấp hơn lãi suất đồng tiền đảm bảo ($r_{VND}$). Đây là kết quả tự nhiên của lý thuyết CIP.
- **Implied Rate bị lệch (Basis Risk):** Chỉ khi lãi suất ngầm định tính từ Swap Points ($r_{USD}^{implied}$) cao hơn hẳn lãi suất thị trường thực tế ($r_{USD}^{SOFR}$), chúng ta mới kết luận có sự khan hiếm thanh khoản (Liquidity Scarcity).

---

## 3. Strategic Advantages

Tại sao các ngân hàng ưu tiên FX Swap hơn là giao dịch Outright Forward hay vay/gửi trực tiếp?

| Ưu điểm | Giải thích |
| :--- | :--- |
| **Cost Efficiency** | Chỉ chịu 1 lần Bid-Ask spread duy nhất thay vì 2 lần. |
| **Balance Sheet** | Là công cụ ngoại bảng (Off-balance sheet), không làm tăng tài sản/nợ phải trả như vay/gửi trực tiếp. Giảm thiểu yêu cầu vốn tự có (CAR) cho rủi ro thị trường (market risk) và rủi ro tín dụng (credit risk). |
| **Risk Separation** | Điểm kỳ hạn (Swap Points) chỉ phụ thuộc vào chênh lệch lãi suất, giúp tách biệt rủi ro tỷ giá (cho Spot trader) và rủi ro lãi suất (cho Forward trader). |
| **Regulatory** | Thường được miễn trừ khỏi các yêu cầu ký quỹ ban đầu (Initial Margin) và bù trừ tập trung (CCP). |

[[Principles_of_Financial_Engineering_Neftci.md#page=195]] [[Principles_of_Financial_Engineering_Neftci.md#page=203]]

---

## Evidence / Source Anchors

- Definition of FX Swap as collateralized borrowing/lending: [[Principles_of_Financial_Engineering_Neftci.md#page=195]]
- Formula for FX swap-implied funding rate: [[Principles_of_Financial_Engineering_Neftci.md#page=197]]
- Off-balance sheet advantages and CAR impact: [[Principles_of_Financial_Engineering_Neftci.md#page=196]]
- Market turnover statistics (FX Swap vs Currency Swap): [[Principles_of_Financial_Engineering_Neftci.md#page=202]]

## Related

- [[Currency_Swap_Engineering]] — Phân biệt với FX Swap (dài hạn & interim payments).
- [[FX_Forward_Engineering]] — FX Swap + Spot = Outright Forward.
- [[Covered_Interest_Parity]] — Cơ sở định giá Swap points.
- [[Central_Counterparty_CCP]] — Các quy định miễn trừ cho FX.
