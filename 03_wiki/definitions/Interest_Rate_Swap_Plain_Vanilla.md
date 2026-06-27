---
title: 'Interest Rate Swap: Plain Vanilla'
aliases:
- Fixed-Floating Swap
- Vanilla Swap
- Swap as a Sequence of Forwards
- Comparative Advantage in Swaps
- Par Swap
- Hoán đổi lãi suất cơ bản
type: mechanism
tags:
- derivatives
- fixed-income
- hedging
- infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Howard Corb | Alexander Düring"
provenance: Multi-source (During & Corb)
thesis: A plain vanilla interest rate swap is a bilateral agreement to exchange a
  series of fixed-rate interest payments for floating-rate payments (and vice versa)
  over a predefined period, economically functioning as a sequence of forward contracts
  designed to transform risk characteristics to match an investor's preferred habitat.
source_refs:
- file: During_Fixed_Income_Ch30.md
  page: 334
- file: During_Fixed_Income_Ch30.md
  page: 336
- file: Howard_Corb_Swaps.md
  page: 4
- file: Howard_Corb_Swaps.md
  page: 14
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Swap là "trái tim" của thị trường phái sinh lãi suất toàn cầu. Alexander Düring bóc tách ranh giới của việc định giá kỹ thuật (Mỏ neo Par Swap và PVBP), trong khi Howard Corb giải mã cơ chế kinh tế và trading logic đằng sau nó. Tại thời điểm khởi tạo, một hợp đồng Swap luôn có giá trị bằng không ($PV=0$), nhưng nó cho phép các thực thể kinh tế thay đổi toàn bộ cấu trúc rủi ro lãi suất của mình bằng cách tách rời "khoản đầu tư" khỏi "rủi ro" (decoupling). [[During_Fixed_Income_Ch30.md#page=334]] [[Howard_Corb_Swaps.md#page=4]]

---

## 1. Structural Interpretation: A Sequence of Forwards

Howard Corb nhấn mạnh một ranh giới toán học cực kỳ quan trọng để hiểu về định giá:
- **The Concept:** Một hợp đồng Swap thực chất là một chuỗi các thỏa thuận lãi suất kỳ hạn (**Forward Rate Agreements - FRAs**) được đóng gói lại với nhau.
- **The Identity:** Giá trị hiện tại (PV) của Swap là tổng PV của từng kỳ trao đổi dòng tiền trong tương lai. Lãi suất Fixed (Swap rate) được tính toán sao cho tổng PV của các dòng tiền trả (Fixed) bằng đúng tổng PV của các dòng tiền nhận dự kiến (Floating). [[Howard_Corb_Swaps.md#page=14]]

---

## 2. Technical Mechanics (Düring's Lens)

### A. The Pricing Anchor: Par Swaps
Thị trường có tính thanh khoản cao nhất ở các **Par Swaps**—các hợp đồng có giá trị bằng không tại thời điểm bắt đầu.
- **The Rate Solver:** Lãi suất swap ($S$) được giải sao cho: $PV(\text{Fixed Leg}) = PV(\text{Floating Leg})$.
- **Annuity (PVBP):** Mẫu số của phép tính này là giá trị hiện tại của chân cố định cho mỗi 1 điểm cơ bản thay đổi. Đây là mỏ neo để tính toán số lượng hợp đồng cần thiết để phòng vệ. [[During_Fixed_Income_Ch30.md#page=336]]

### B. Market Conventions: The "Mine" Paradox
Khác với thị trường trái phiếu, tên gọi trong Swaps đi theo logic của thị trường tiền tệ:
- **"Mine":** Nghĩa là nhà giao dịch nhận tiền (borrow) và do đó sẽ **Trả lãi suất cố định (Pay Fixed)**.
- **"Yours":** Nghĩa là nhà giao dịch cho vay tiền và do đó sẽ **Nhận lãi suất cố định (Receive Fixed)**. [[During_Fixed_Income_Ch30.md#page=336]]

---

## 3. The Economic Driver: Comparative Advantage (Corb's Lens)

Corb giải mã lý do tại sao các bên lại chấp nhận giao dịch Swap:
- **Market Frictions:** Một công ty có uy tín thấp có thể vay lãi suất nổi rẻ hơn, trong khi một định chế lớn vay lãi suất cố định rẻ hơn.
- **The Swap Play:** Cả hai bên thực hiện Swap để trao đổi lợi thế này. Kết quả là cả hai đều đạt được cấu trúc lãi suất mong muốn với mức chi phí thấp hơn so với việc vay trực tiếp trên thị trường. [[Howard_Corb_Swaps.md#page=12]]

---

## 4. Strategic Taxonomy: Natural Counterparties

Alexander Düring bóc tách các luồng lệnh "tự nhiên" dẫn dắt thị trường nghìn tỷ USD này:

| Sector | Payer (Pays Fixed) | Receiver (Receives Fixed) |
| :--- | :--- | :--- |
| **Intermediate** | Banks (hedging long bonds) | Corporates (matching cyclical earnings) |
| **Long End** | Banks | Pension Funds (matching liabilities) |
| **Asset Swappers** | Hedge Funds / Dealers | Life Insurers |
| **Mortgages** | Mortgage Lenders | Sovereigns (hedging duration) |

[[During_Fixed_Income_Ch30.md#page=337]]

---

## Evidence / Source Anchors

- Definition of Swap as a sequence of forward contracts: [[Howard_Corb_Swaps.md#page=14]]
- Analysis of the comparative advantage argument for swap existence: [[Howard_Corb_Swaps.md#page=12]]
- Description of Par Swaps and the mathematical solver requirement: [[During_Fixed_Income_Ch30.md#page=336]]
- Taxonomy of natural payer/receiver positions (Table 29.1): [[During_Fixed_Income_Ch30.md#page=337]]
- Rationale for the "Mine/Yours" nomenclature convention: [[During_Fixed_Income_Ch30.md#page=336]]

## Related

- [[Yield_Curve_Structure_And_Mechanics]] — The discount curve used to set the swap rate.
- [[Basis_Trade_Mechanics]] — Trading the difference between various swap legs.
- [[Asset_Swap_Spread_ASW]] — Using swaps to isolate credit risk of individual bonds.
- [[OIS_And_Benchmark_Reform]] — The modern "Dual Curve" discounting standard.
- [[Swap_Trade_Compression_And_Recouponing]] — How to manage large swap portfolios.
