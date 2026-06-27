---
title: Central Bank Liquidity Provision Mechanics
aliases:
- Rediscounting
- Open Market Operations
- Repos
- Lombard Lending
type: mechanism
tags:
- central-banking
- liquidity
- money-markets
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Việc mở rộng bảng cân đối kế toán của NHTW (bơm thanh khoản) được thực hiện
  thông qua ba loại hình nghiệp vụ có cơ chế khác biệt—Tái chiết khấu, Nghiệp vụ thị
  trường mở (OMO) và Repo—trong đó mỗi loại hình sẽ phân bổ rủi ro kỳ hạn và rủi ro
  giá khác nhau giữa khu vực công và khu vực ngân hàng tư nhân.
source_refs:
- file: Fixed_Income_Alexander_During_Ch07.md
  page: 51
created: '2026-04-16'
updated: '2026-04-22'
---

## Thesis

To manipulate the short-term interbank interest rate, a central bank must organically increase its short-term liabilities (providing base money). This is surgically achieved by expanding the asset side of its balance sheet. However, the precise operational mechanism utilized—Rediscounting bills, conducting explicit Open Market Operations (OMO), or executing collateralized Repos—dictates entirely whether the central bank accepts structural price risk or forces the private sector to bear the mark-to-market volatility.

## Mechanism

### 1. Rediscounting (The Passive Approach)
Historically dominant and giving rise to the "Discount Window", Rediscounting occurs when the central bank purchases outright a short-term commercial bill previously discounted by a commercial bank.
- *Risk Profile:* The central bank holds dual recourse: against the originating corporate borrower, and the commercial bank explicitly presenting the bill.
- *Friction:* Because the central bank holds the bill to maturity, liquidity naturally drains organically when the bill matures. Managing aggregate liquidity requires the central bank to passively wait for maturation rather than actively trading.

### 2. Open Market Operations / Outright Purchases (The US Fed Model)
The central bank purchases long-term assets (typically sovereign debt) from the open secondary market.
- *Risk Profile:* Because the transaction is a true "true sale," the central bank absorbs total explicit **price risk** (e.g., if interest rates rise, the value of the bond on the central bank's balance sheet collapses).
- *Control:* Provides supreme active control. The central bank can hold the asset, or aggressively resell it before maturity to instantly violently drain liquidity from the system.

### 3. Repurchase Agreements / Lombard Lending (The ECB/BOJ Model)
Rather than buying assets outright, the central bank advances cash strictly as a collateralized loan against posted securities (historically termed Lombard Lending). In modern architecture, this is executed as a Sale and Repurchase (Repo).
- *Risk Profile:* The central bank takes zero duration or price risk. The commercial bank remains the ultimate economic owner of the bond and absorbs all mark-to-market losses. Furthermore, the central bank mathematically protects itself by applying explicit haircuts to the collateral.
- *Control:* Liquidity is injected for a definitively fixed maturity (e.g., 1 week).

## Evidence / Source Anchors

- Distinction between Rediscounting mechanics and the dual-recourse legal structure: [[Fixed_Income_Alexander_During_Ch07.md#page=51]]
- Active vs Passive liquidity duration management (OMO vs Discounting): [[Fixed_Income_Alexander_During_Ch07.md#page=51]]
- Structural assignment of price risk defining OMO vs the fixed-maturity, zero-price-risk nature of Lombard Repos: [[Fixed_Income_Alexander_During_Ch07.md#page=51]]

## Related

- [[Symmetric_Vs_Asymmetric_Corridor_System]] — how these operations frame the interbank rate environment
- [[Bill_Of_Exchange_Discounting]] — the origin of the commercial bills utilized in the Rediscount operation
- [[Monetary_Financing_Mechanism]] — the fiscal risk when OMO morphs into sovereign debt monetization
