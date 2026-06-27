---
title: Equity Swap Engineering
aliases:
- Equity Swap
- Synthetic Stock Position
type: mechanism
tags:
- derivatives
- equity
- synthetics
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: An equity swap is engineered by adding a Forward LIBOR Loan (financial zero)
  to a forward stock purchase, allowing for synthetic equity exposure without upfront
  cash, balance sheet impact, or regulatory ownership constraints.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 6
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Một giao dịch mua cổ phiếu trực tiếp (outright purchase) thường gặp các rào cản về vốn (funding), thuế, và quy định sở hữu. Equity Swap giải quyết các ranh giới này bằng cách biến vị thế cổ phiếu thành một hợp đồng hoán đổi dòng tiền.

## 1. Core Logic: The Additive Zero
Cấu trúc của một Equity Swap được hình thành bằng cách cộng một vị thế cổ phiếu (marking-to-market hàng kỳ) với một khoản vay LIBOR (có giá trị bằng 0 tại $t_0$):

$$\text{Equity Swap} = \text{Stock Portfolio} + \text{Forward LIBOR Loan}$$

**Cơ chế truyền dẫn dòng tiền:**
- **Input 1 (Stock):** Nhà đầu tư thu cổ tức ($d$) và hưởng chênh lệch giá ($\Delta S_{ti}$) tại mỗi kỳ thanh toán.
- **Input 2 (Zero):** Nhà đầu tư trả lãi suất nổi ($L_{ti-1}$) cho vốn gốc $N$.
- **Net Result:** Trao đổi $(\Delta S_{ti} + d) \cdot \delta N$ lấy $L_{ti-1} \cdot \delta N$.

## 2. Worked Example (The "LIBOR - Spread" Quote)
[RAW] Trong thực tế, vì cổ tức ($d$) là biến số chưa biết hoàn toàn, thị trường thường gộp nó vào một mức spread so với LIBOR.
- **Mechanism:** Trader A muốn nhận Total Return của S&P 500.
- **Result:** Trader A trả $(\text{LIBOR} - \text{Spread})$ và nhận $\Delta S_{ti}$. Spread này chính là giá trị kỳ vọng của cổ tức ($E[d]$) cộng với phần bù cung cầu.
- **Transmission:** Cấu trúc này chứng minh rằng thị trường kỳ vọng danh mục cổ phiếu sẽ thay đổi một lượng đúng bằng $L_{ti-1} - d_{ti}$ mỗi kỳ (Risk-neutral expectation).

## 3. Boundary Conditions
- **Ownership Restrictions:** [RAW] Hữu ích cho các nhà đầu tư không được phép sở hữu trực tiếp cổ phiếu (e.g., Chinese A-shares cho tổ chức nước ngoài).
- **Tax Implications:** Tránh thuế đánh trên việc thực hiện giao dịch cổ phiếu trực tiếp ở một số quốc gia.
- **Dividend Treatment:** Ví dụ trên giả định không có cổ tức. Nếu có cổ tức, cấu trúc sẽ điều chỉnh phần thanh toán nhận được.

## Related
- [[Interest_Rate_Swap_Engineering]] — Cấu trúc tương tự áp dụng cho trái phiếu.
- [[Forward_LIBOR_Loan_Mechanism]] — Nền tảng "Financial Zero".
- [[Total_Return_Swap_TRS]] — Khái niệm bao hàm của Equity Swap.
