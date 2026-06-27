---
title: Credit Default Swaps (CDS)
aliases:
- CDS
- Single-name CDS
- Credit Insurance Synthetic
type: concept
tags:
- derivatives
- credit-risk
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Tuckman & Serrat | Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: A Credit Default Swap (CDS) isolates credit risk by engineering a synthetic
  insurance contract through the combination of a risky bond, a financial zero (LIBOR
  loan), and an interest rate swap.
source_refs:
- file: Tuckman_Serrat_2022.md
  page: 367
- file: During_Fixed_Income_Ch12.md
  page: 109
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 7
created: '2026-04-20'
updated: '2026-04-21'
---

## Thesis
Tại sao CDS lại quan trọng hơn bản thân trái phiếu trong việc định giá rủi ro? [RAW] Tuckman giải mã ranh giới của việc "cô lập rủi ro", trong khi Neftci chứng minh CDS là một cấu trúc phái sinh được tách ra từ các công cụ sơ cấp thông qua phương trình: $CDS = \text{Risky Bond} + \text{LIBOR Loan} - \text{IRS}$.

## 1. Mechanism: The Insurance & Engineering Structure

### A. Insurance View (Tuckman)
- **Protection Buyer:** Thanh toán phí định kỳ (CDS Spread).
- **Protection Seller:** Nhận phí và cam kết bồi thường nếu **Credit Event** xảy ra.

### B. Engineering View (Neftci)
[RAW] CDS có thể được coi là việc mua một trái phiếu rủi ro nhưng triệt tiêu rủi ro lãi suất và nhu cầu vốn:
$$\text{cdst}_0 = c_{t0} - s_{t0}$$
Trong đó:
- $c_{t0}$: Coupon của trái phiếu rủi ro.
- $s_{t0}$: Swap rate (lãi suất cố định của IRS).
- Hiệu số chính là phần bù rủi ro tín dụng thuần túy (Credit Spread).

## 2. Worked Example (Neftci)
[RAW] Giả sử một trái phiếu rủi ro trả coupon 8% ($c_{t0} = 0.08$) và swap rate 10 năm hiện tại là 5% ($s_{t0} = 0.05$).
- **Mechanism:** Nhà đầu tư mua trái phiếu (nhận 8%) và thực hiện Payer IRS (trả 5% cố định, nhận LIBOR). Sau đó dùng LIBOR nhận được để trả cho khoản vay LIBOR (Funding).
- **Result:** Dòng tiền còn lại là nhận ròng 3% ($8\% - 5\%$). Đây chính là mức CDS Spread (300 bps) mà thị trường đòi hỏi để bảo hiểm cho trái phiếu này.

## 3. Failure Conditions & Caveats
- **Liquidity Wedge:** [RAW] Trái phiếu cơ sở có thể kém thanh khoản hơn chính hợp đồng CDS.
- **Counterparty Risk:** Khác với trái phiếu, CDS phụ thuộc vào khả năng chi trả của Protection Seller.
- **Credit Events Taxonomy:** [RAW] ISDA định nghĩa Bankruptcy, Failure to Pay, và Restructuring là các ranh giới kích hoạt. [[Tuckman_Serrat#page=369]]
- **Opportunistic Strategies:** [RAW] Tuckman cảnh báo về các ranh giới đạo đức như "Manufactured Default" (vụ Hovnanian) hay "Orphaning" trái phiếu cơ sở. [[Tuckman_Serrat#page=385]]

## Evidence / Source Anchors
- Basic mechanics and roles of buyer/seller: [[Tuckman_Serrat#page=367]]
- ISDA credit event definitions: [[Tuckman_Serrat#page=369]]
- Discussion on physical vs. cash settlement: [[Tuckman_Serrat#page=380]]
- Analysis of opportunistic strategies: [[Tuckman_Serrat#page=385]]
- Derivation of CDS from Risky Bond + LIBOR Loan - IRS: [[Principles_of_Financial_Engineering_Neftci.md#page=9]]
- Definition of CDS Spread as $cdst_0 = c_{t0} - s_{t0}$: [[Principles_of_Financial_Engineering_Neftci.md#page=10]]

## Related
- [[Credit_Default_Swaps_Schofield]] — Complementary market mechanics & settlement methods (physical/auction/cash)
- [[Interest_Rate_Swap_Engineering]]
- [[Forward_LIBOR_Loan_Mechanism]]
- [[CDS_Settlement_Auction]]
