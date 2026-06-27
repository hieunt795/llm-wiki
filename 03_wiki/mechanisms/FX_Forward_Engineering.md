---
title: FX Forward Engineering
aliases:
- Currency Forward Decomposition
- FX Forward Synthetic
- Phân rã kỳ hạn tỷ giá
type: mechanism
tags:
- fx
- financial-engineering
- synthetics
- arbitrage
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: FX Forward engineering is the process of decomposing a future currency exchange
  into elementary money market operations (borrowing and lending) using a 4-step vertical
  addition methodology to ensure no-arbitrage pricing.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 176-203
created: '2026-04-21'
updated: '2026-04-21'
---

## Thesis

[RAW] Salih Neftci trình bày FX Forward không chỉ là một hợp đồng mua bán đơn thuần mà là một cấu trúc có thể phân rã thành các hoạt động thị trường tiền tệ (Money Market). Cơ chế này cho phép các chuyên gia tài chính tạo ra các tài sản giả lập (Synthetics) xuyên biên giới, biến các thị trường vốn nước ngoài thành thị trường nội địa về mặt kinh tế. [[Principles_of_Financial_Engineering_Neftci.md#page=178]]

---

## 1. The 4-Step Engineering Methodology

Quy trình chuẩn để phân rã hoặc tái lập bất kỳ công cụ tài chính tuyến tính (linear instrument) nào, áp dụng cho FX Forward:

1.  **Step 1 (Visualization):** Vẽ sơ đồ dòng tiền của hợp đồng gốc (e.g., mua USD bằng EUR tại thời điểm $t_1$).
2.  **Step 2 (Detachment):** Tách rời hai luồng tiền mặt (Long USD và Short EUR) thành hai sơ đồ độc lập.
3.  **Step 3 (Normalization/Insertion):** Thêm và bớt các dòng tiền mới tại thời điểm hiện tại $t_0$ để biến các sơ đồ đơn lẻ thành các hợp đồng có ý nghĩa:
    - Long USD tại $t_1$ + Short USD tại $t_0$ = USD Deposit.
    - Short EUR tại $t_1$ + Long EUR tại $t_0$ = EUR Loan.
4.  **Step 4 (Vertical Addition):** Cộng các sơ đồ lại. Đảm bảo các dòng tiền mới tại $t_0$ triệt tiêu lẫn nhau qua một giao dịch Spot (Leg C). [[Principles_of_Financial_Engineering_Neftci.md#page=179]]

---

## 2. The Money Market Synthetic

Sử dụng quy trình trên, một FX Forward (Mua USD/Bán EUR) được tái lập bằng 3 chân giao dịch (Legs) tại $t_0$:

### The Contractual Equation (Formalized)
Dưới các giả định lý tưởng (No transaction costs, no bid-ask spreads, no credit/counterparty risk, liquid markets), ta có phương trình:

$$ \text{FX Forward} = \text{Loan (EUR)} + \text{Spot FX} + \text{Deposit (USD)} $$

**Transmission Flow (T-Shape):**
[FX FORWARD REPLICATION]
t=t0                       │  t=t1
───────────────────────────┼───────────────────────────
[Leg A: EUR Loan]          │
(1) +C_EUR (Inflow)  ───>  │  (2) -100/F EUR (Outflow)
                           │
[Leg B: Spot FX]           │
(3) -C_EUR / +C_USD  ───>  │  (No cash flow)
                           │
[Leg C: USD Deposit]       │
(4) -C_USD (Outflow) ───>  │  (5) +100 USD (Inflow)
───────────────────────────┼───────────────────────────
[NET RESULT]               │
Time t0: (1)+(3)+(4) = 0   │  Time t1: EUR/USD Swap
                           │

### Selection Criteria for Synthetics
[RAW] Khi có nhiều cách thiết lập synthetic (e.g., via Loans vs. T-Bills), Practitioner chọn dựa trên:
1. **Least Cost:** Chi phí thấp nhất.
2. **Liquidity:** Thành phần nào thanh khoản cao nhất.
3. **Regulatory:** Phù hợp với các quy định pháp lý/thuế.
4. **Balance Sheet:** Tác động tối ưu lên bảng cân đối kế toán. [[Principles_of_Financial_Engineering_Neftci.md#page=201]]

---

## 3. Pricing via Synthetics (CIRP)

### A. Money Market Parity (Cash-based)
Dựa trên lãi suất liên ngân hàng (Eurocurrency deposits):
$$ F_{t0} = e_{t0} \cdot \frac{1 + L_{USD} \cdot (\Delta t / 360)}{1 + L_{EUR} \cdot (\Delta t / 360)} $$

### B. T-Bill Parity (Bond-based)
Dựa trên giá trái phiếu chiết khấu không rủi ro:
$$ F_{t0} = e_{t0} \cdot \frac{B(t_0, t_1)_{EUR}}{B(t_0, t_1)_{USD}} $$

---

## 4. Worked Example: Synthetic USD Bond
[RAW] Một nhà đầu tư muốn mua trái phiếu USD nhưng chỉ có tiếp cận tốt với thị trường EUR.
1.  **Action:** Mua trái phiếu EUR (maturity $t_1$).
2.  **Hedge:** Bán EUR forward (mua USD forward) tại $t_1$.
3.  **Result:** Dòng tiền cuối cùng là USD tại $t_1$, tạo ra một synthetic USD bond với rủi ro tín dụng tương đương trái phiếu EUR gốc. [[Principles_of_Financial_Engineering_Neftci.md#page=176]]

---

## 5. Strategic Assumptions (The Ideal State)
Việc tái lập hoàn hảo dựa trên 5 giả định cốt lõi:
1. **No transaction costs:** Không phí giao dịch.
2. **No bid-ask spreads:** Không chênh lệch mua-bán.
3. **No credit risk:** Không rủi ro tín dụng (thường dùng T-bills để tiệm cận).
4. **No counterparty risk:** Không rủi ro đối tác.
5. **Liquid markets:** Thị trường luôn sẵn sàng giao dịch. [[Principles_of_Financial_Engineering_Neftci.md#page=203]]

---

## 6. Failure Conditions & Limits of Arbitrage
Mặc dù CIRP được coi là một trong những định luật bền vững nhất trong tài chính, các điều kiện thực tế có thể dẫn đến sự lệch pha (deviations):

- **Lehman Crisis (2008):** [RAW] Sau sự sụp đổ của Lehman Brothers, CIRP đã bị vi phạm trong nhiều tháng đối với các đồng tiền chính như EUR và GBP.
- **Creditworthiness Concerns:** Các tổ chức tài chính châu Âu cần USD nhưng đối mặt với lo ngại về rủi ro đối tác, buộc họ phải huy động USD qua thị trường FX Swap (one-sided order flow), đẩy giá synthetic USD cao hơn LIBOR USD.
- **Limits of Arbitrage:** Theo Mancini-Griffoli và Ranaldo (2013), các rào cản về vốn và thanh khoản ngăn cản các nhà giao dịch khai thác cơ hội trọng tài, giữ thị trường ở trạng thái không cân bằng trong thời gian dài. [[Principles_of_Financial_Engineering_Neftci.md#page=203]]

---

## Evidence / Source Anchors

- The 4-step decomposition methodology: [[Principles_of_Financial_Engineering_Neftci.md#page=179]]
- Selection criteria for synthetics: [[Principles_of_Financial_Engineering_Neftci.md#page=201]]
- Formalized contractual equation and 5 assumptions: [[Principles_of_Financial_Engineering_Neftci.md#page=203]]
- Synthetic USD bond example: [[Principles_of_Financial_Engineering_Neftci.md#page=176]]
- Deviations from CIRP and Limits of Arbitrage: [[Principles_of_Financial_Engineering_Neftci.md#page=203]]

## Related

- [[Synthetic_Loan_Engineering]] — Ứng dụng cụ thể trong thị trường FX.
- [[Covered_Interest_Parity]] — Cơ sở định giá dựa trên No-arbitrage.
- [[Interest_Rate_Parity]] — Định nghĩa rộng về cân bằng lãi suất.
