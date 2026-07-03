---
title: Corporate Trade Credit
aliases:
- Accounts Payable Financing
- Non-bank Credit Supply
- Collection Period
type: mechanism
tags:
- corporate-finance
- short-term-funding
- macro
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Tín dụng thương mại doanh nghiệp đại diện cho một lớp cho vay phi ngân hàng
  khổng lồ và thường vô hình, nơi các tập đoàn tài trợ cho chuỗi cung ứng của họ bằng
  cách trì hoãn thanh toán hóa đơn, về mặt chức năng là cung cấp các khoản vay ngắn
  hạn không có bảo đảm cho các đối tác thương mại.
source_refs:
- file: Fixed_Income_Alexander_During_Ch04.md
  page: 28
created: '2026-04-16'
updated: '2026-04-22'
---

## Thesis

Macroeconomic analysis frequently errs by fixating exclusively on central banking and commercial bank lending while neglecting Corporate Trade Credit. Trading on credit via accounts payable and receivable represents a colossal, unregulated layer of non-bank lending operating globally. By deliberately misaligning the delivery of goods with the settlement of invoices, corporations structurally fund each other’s working capital, functioning as a decentralized shadow banking network completely insulated from direct monetary policy transmission.

## Mechanism

From an economic perspective, delivering a physical good or service but permitting payment in arrears (e.g., Net-30 or Net-60 terms) mathematically equates to the producer granting an uncollateralized loan to the trader. The duration and currency of this loan are freely negotiated, completely bypassing commercial banking constraints.

### The Collection Period Metric
The extent of this shadow lending on a corporate balance sheet is explicitly quantifiable via the **Collection Period** formula. By evaluating the ratio of outstanding receivables against the velocity of sales, analysts determine exactly how long the corporation is acting as a creditor to its supply chain:

$$\text{Collection Period} = \frac{\text{Accounts Receivable}}{\text{Total Sales}}$$

*(Note: Total Sales in this context is typically annualized or adjusted for the exact period matching the receivables).*

### Boundaries / Conditions

### Balance Sheet Arbitrage
Because terms of payment operate outside strict regulatory banking parameters, massive global corporations manage their payables aggressively as a form of balance sheet arbitrage:
1. **Window Dressing:** A titan corporation might squeeze its suppliers to pay before December 31st precisely to artificially suppress its outstanding accounts receivable on year-end financial reporting, mathematically projecting a falsely shortened collection period.
2. **Yield Arbitrage:** Treasurers actively model the cost of capital. If forcing a supplier to wait 90 days for payment yields an implied return (via preserved liquidity) higher than depositing idle cash in a commercial bank, the treasury algorithmically delays the payment.
3. **Implicit Currency Positions:** A multinational that deliberately pays its obligations rapidly in Currency A (e.g., Euros), while explicitly allowing invoices owed to itself in Currency B (e.g., Dollars) to linger for 90 days, effectively engineers a massive, un-reported "Short EUR / Long USD" macro position completely hidden within standard operational cash flows.

## Evidence / Source Anchors

- Definition of trade credit as a direct loan from producer to trader explicitly negating bank intervention: [[Fixed_Income_Alexander_During_Ch04.md#page=28]]
- The mechanical formula for the Collection Period: [[Fixed_Income_Alexander_During_Ch04.md#page=28]]
- Treasury execution of balance sheet manipulation and synthetic cross-currency positions using varied payment terms: [[Fixed_Income_Alexander_During_Ch04.md#page=29]]

## Related

- [[Shadow_Banking_Mechanics]] — comparing this decentralized credit to structural non-bank lending
- [[Factoring_And_Receivables_Discounting]] — when this corporate credit is ultimately sold to the financial sector
- [[Working_Capital_Management]] — the corporate framework governing these decisions
- [[Trade_Credit]]
- [[Trade_Credit_And_Non_Bank_Lending]]
- [[Private_Credit_Stress_Transmission]]
- [[US_Vs_Europe_Private_Credit_Dynamics]]
- [[Basis_Trade_Crisis_2020]]
- [[Credit_Default_Swaps_CDS]]
- [[Credit_Ratings_And_Migration]]
- [[Credit_Risk_Taxonomy]]
- [[Credit_Risk_Transfer_CRT]]
- [[Endogenous_Money_Credit_Creation]]
- [[Floating_vs_Fixed_Exchange_Rate_Regimes]]
- [[Monetary_Transmission_Credit_View]]
- [[Money_View_Vs_Credit_View_Debate]]
- [[BOP_Framework_and_Conventions]]
- [[BOP_Standard_Classification]]
- [[Commodities]]
