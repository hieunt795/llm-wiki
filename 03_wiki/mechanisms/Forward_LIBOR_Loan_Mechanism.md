---
title: Forward LIBOR Loan Mechanism
aliases:
- The Financial Zero
- LIBOR Forward Zero
- Forward-Starting Floating Loan
type: mechanism
tags:
- derivatives
- pricing-theory
- no-arbitrage
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: The forward LIBOR loan is the unique financial instrument whose market value
  is identically zero at inception and throughout the forward period, serving as the
  'additive zero' for engineering synthetic assets.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 2
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 3
created: '2026-04-21'
updated: '2026-04-22'
---

## Mechanism: The Additive Zero

A contract struck at $t_0$ to borrow $100$ USD at a future date $t_1$, to be repaid at $t_2$ at the prevailing rate $L_{t1}$ (LIBOR), has a net present value of zero for all $t \in [t_0, t_1]$.

### 1. Mathematical Proof (No-Arbitrage)
The value of the cash flows at $t_1$ is calculated by discounting the repayment ($Principal + Interest$) at $t_2$ back to $t_1$ using the same floating rate $L_{t1}$:

$$PV_{t1} = \frac{L_{t1}\delta \cdot 100}{1 + L_{t1}\delta} + \frac{100}{1 + L_{t1}\delta}$$
$$PV_{t1} = \frac{(1 + L_{t1}\delta) \cdot 100}{1 + L_{t1}\delta} = 100$$

Since the borrower receives $100$ at $t_1$ and the PV of the obligation is $100$, the net value is:
$$\text{Net Value} = 100 - 100 = 0$$

### 2. Strategic Implication: The Building Block
[RAW] Vì cộng số 0 vào bất kỳ phương trình nào cũng không làm thay đổi giá trị của nó, nhà kỹ thuật tài chính có thể cộng một Khoản vay LIBOR kỳ hạn vào bất kỳ tài sản rủi ro nào (Trái phiếu, Cổ phiếu, Hàng hóa) để thay đổi cấu trúc dòng tiền (e.g., từ cố định sang thả nổi) mà không làm thay đổi giá trị thị trường của nó tại thời điểm khởi đầu.

### 3. Volatility Preservation
[RAW] Neftci chứng minh rằng vì giá trị của công cụ này luôn bằng 0 ($V_t = 0$), nên độ biến động của nó cũng bằng 0 ($\text{Volatility}(V_t) = 0$). 
- **The Equation:** Nếu $S_t$ là giá trị của một tài sản rủi ro, thì $\text{Volatility}(S_t + V_t) = \text{Volatility}(S_t)$.
- **Insight:** Việc thêm "số 0" này không làm thay đổi đặc tính rủi ro thị trường (biến động và tương quan) của tài sản gốc, nhưng cho phép thay đổi các đặc tính về thuế, kế toán, và quy định pháp lý.

## Evidence / Source Anchors
- Proof that LIBOR loan value is independent of interest rate expectations: [[Principles_of_Financial_Engineering_Neftci.md#page=3]]
- Definition of LIBOR as the fundamental pricing anchor (pre-GFC context): [[Principles_of_Financial_Engineering_Neftci.md#page=2]]
- Mathematical proof of Volatility Preservation: [[Principles_of_Financial_Engineering_Neftci.md#page=109]]

## Related
- [[Interest_Rate_Swap_Engineering]] — The primary application of this zero instrument.
- [[Equity_Swap_Engineering]] — Applying the zero to equity positions.
- [[No_Arbitrage_Pricing]] — The underlying economic principle.
