---
title: Interest Rate Swap Engineering
aliases:
- IRS Engineering
- Synthetic Floating Position
- Bond-Swap Transformation
type: mechanism
tags:
- derivatives
- swaps
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: An Interest Rate Swap is engineered by adding a Forward LIBOR Loan (the financial
  zero) to a fixed-rate bond, allowing investors to exchange fixed and floating risk
  without upfront funding or balance sheet inflation.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 4
created: '2026-04-21'
updated: '2026-04-22'
---

## Mechanism: The Additive Construction

[RAW] Neftci explains that market practitioners rarely buy or sell bonds outright for risk management. Instead, they "engineer" the position through a swap to avoid funding costs and regulatory constraints.

### 1. Structural Equation
$$\text{Interest Rate Swap} = \text{Fixed Rate Bond} + \text{Forward LIBOR Loan}$$

- **Input 1 (Bond):** Long position in a fixed-rate bond (Receives Fixed $r_{t0}$, Pays Par at $t_2$).
- **Input 2 (Zero):** A LIBOR loan (Receives Par at $t_1$, Pays Par + Floating $L_{t1}$ at $t_2$).

### 2. The Resulting Cash Flows
When combined, the principal exchanges at $t_1$ and $t_2$ cancel out (assuming par bonds), leaving only the net exchange of interest:
- **Net Flow:** Receive Fixed ($r_{t0}$) / Pay Floating ($L_{t1}$).

## Strategic Advantages (The Inquiries)
1. **No Upfront Funding:** Unlike bonds, swaps require no initial cash payment.
2. **Off-Balance Sheet:** Swaps do not affect the size of the "books" (assets/liabilities) as much as outright purchases, which is critical for regulatory capital (Basel III).
3. **Jurisdiction Independence:** [RAW] Neftci lưu ý rằng khi mua trái phiếu US Treasury, bạn phải thực hiện tại Mỹ. Nhưng với Swap ($S_t + V_t$), bạn có thể thực hiện ở bất kỳ đâu trên thế giới (Offshore) vì đây chỉ là sự trao đổi các dòng tiền mặt.
4. **Anonymity:** [RAW] Hoán đổi dòng tiền không yêu cầu sở hữu chứng khoán đăng ký (Registered bonds). Nhà đầu tư có thể duy trì vị thế tương đương mà vẫn đảm bảo tính ẩn danh (tương tự Bearer bonds).
5. **Credit Risk Separation:** Tách biệt rủi ro tín dụng của nguồn vốn (funding) khỏi rủi ro thị trường của lãi suất.
6. **General Additive Strategy:** [RAW] Neftci định nghĩa chiến lược Swap tổng quát là: $\text{Basket} = \text{Asset} + \text{Zero}$. Trong đó "Zero" là một tài sản có độ biến động bằng 0 giúp chuyển đổi các đặc tính phi rủi ro của tài sản gốc.
7. **Funding Value Adjustment (FVA):** [RAW] Neftci (Footnote 3) lưu ý ranh giới về chi phí vốn: Việc hạch toán chi phí vốn trong định giá các dẫn xuất OTC (FVA) là một điểm gây tranh cãi lớn hậu GFC, sẽ được thảo luận sâu ở các chương sau.

## Evidence / Source Anchors
- Visual engineering of IRS from bond and LIBOR loan: [[Principles_of_Financial_Engineering_Neftci.md#page=5]]
- Comparison of regulatory and funding inconveniences (Anonymity, Balance Sheet): [[Principles_of_Financial_Engineering_Neftci.md#page=3-4]]
- The "Additive Zero" formal logic and Jurisdiction Independence: [[Principles_of_Financial_Engineering_Neftci.md#page=110]]
- ISDA Master Agreement and legal standardization: [[During_Fixed_Income_Ch13.md#page=110]]
- The shift from LIBOR to OIS discounting: [[During_Fixed_Income_Ch13.md#page=115]]

## Related
- [[Forward_LIBOR_Loan_Mechanism]] — The building block.
- [[Asset_Swap_Spread_ASW]] — A common way to trade this relationship.
- [[OIS_And_Benchmark_Reform]] — Modern replacement for LIBOR anchors.
