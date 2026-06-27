---
title: Collateral Haircut and Wrong-Way Risk
aliases:
- Haircut
- Collateral Haircut
- Wrong-Way Risk
- Risk-based Haircut
type: mechanism
tags:
- risk-management
- repo
- central-banking
- collateral
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch15.md
thesis: A collateral haircut is a risk-mitigation tool that discounts the market value
  of an asset to protect the cash lender against price volatility and the systematic
  danger of wrong-way risk.
source_refs:
- file: During_Fixed_Income_Ch15.md
  page: 128
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

While the repo rate is the primary economic variable of a trade, the **Haircut** is its primary risk control. Alexander Düring explains that a haircut serves as a protective buffer, ensuring that the cash lender is over-collateralized. This buffer is essential because of the potential for market movements during the period it takes to liquidate a defaulted position and the insidious correlation known as "Wrong-Way Risk." [[During_Fixed_Income_Ch15.md#page=128]]

## Mechanism: The Discount Buffer

The haircut is a percentage deduction from the collateral's market value.
- **Example:** At a 1% haircut, JPY 10bn of collateral allows for only JPY 9.9bn of cash borrowing.
- **Initial Margin Analogy:** [RAW] Neftci so sánh Haircut với Initial Margin (Ký quỹ ban đầu) trong thị trường Futures. Cả hai đều là rào cản vốn để bảo vệ bên mua tài sản trước sự sụt giảm giá đột ngột.
- **Calibration:** Haircuts depend on:
    1. **Asset Quality:** Government bonds typically carry 0-1% haircuts.
    2. **Price Volatility:** Equities can require haircuts of 50% or higher.
    3. **Credit Risk:** The relative stability of the borrower vs. the lender. [[During_Fixed_Income_Ch15.md#page=128]]

## Strategic Implications: Haircut Arbitrage

[RAW] Neftci chỉ ra ranh giới giữa các loại người chơi trên thị trường có mức độ tín nhiệm khác nhau:
- **The Gap:** Một khách hàng (Client) có thể phải chịu Haircut 1% khi vay vốn qua Repo Dealer. Tuy nhiên, chính Repo Dealer đó có thể mang chứng khoán đó đi repo tiếp trên thị trường liên ngân hàng (Interbank) với Haircut 0%.
- **The Profit:** Dealer không chỉ hưởng lợi từ spread lãi suất mà còn hưởng lợi từ việc giải phóng vốn (Capital efficiency). Đây là một dạng kinh doanh dựa trên sự chênh lệch về uy tín tín dụng và quy định về tài sản đảm bảo.

## The Concept of Wrong-Way Risk

Wrong-way risk occurs when the **probability of default** of a counterparty is positively correlated with the **risk of loss** on the collateral they provided.

- **The Logic:** A bank often funds its operations using collateral that is linked to its own sector or region. If that sector/region faces a crisis, the bank's stability declines at the exact same moment that its collateral value drops.
- **The Result:** The collateral is most likely to fail precisely when it is most needed to cover a default.
- **Central Bank Response:** Because central banks are the "ultimate" lenders and cannot default in their own currency, they can enforce asymmetric, high haircuts to protect against this systemic correlation. [[During_Fixed_Income_Ch15.md#page=128]]

## Boundaries / Conditions: Daily Margining
To prevent the haircut buffer from being eroded by price moves, repo counterparties typically agree to **daily mark-to-market**. If the collateral value falls below the required threshold (Market Value minus Haircut), the borrower must post additional securities or return a portion of the cash. [[During_Fixed_Income_Ch15.md#page=128]]

## Evidence / Source Anchors

- Definition of the haircut as a percentage disregarded for borrowing purposes: [[During_Fixed_Income_Ch15.md#page=128]]
- Typical haircut ranges (Bonds 0-1% vs. Equities 50%): [[During_Fixed_Income_Ch15.md#page=128]]
- Analysis of Wrong-Way Risk as a correlation between borrower stability and collateral value: [[During_Fixed_Income_Ch15.md#page=128]]
- Rationale for central bank asymmetric haircut enforcement: [[During_Fixed_Income_Ch15.md#page=128]]

## Related

- [[Repurchase_Agreement_Repo_Market_Structure]] — The market where haircuts are applied.
- [[Margining_IM_Vs_VM]] — The daily process of maintaining the haircut buffer.
- [[Central_Bank_Collateral_Frameworks]] — How central banks define their specific haircut schedules.
- [[Counterparty_Credit_Risk]] — The broader risk that haircuts seek to mitigate.
