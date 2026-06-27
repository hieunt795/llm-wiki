---
title: General Collateral vs Special
aliases:
- GC vs Special
- Specialness
- Repo Spread
- Specific Collateral
type: mechanism
tags:
- money-market
- repo
- liquidity
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch15.md
thesis: The spread between General Collateral (GC) and Special repo rates measures
  the market's demand for specific securities, where a security is 'Special' if its
  repo rate is driven down by scarcity rather than the cost of cash.
source_refs:
- file: During_Fixed_Income_Ch15.md
  page: 126
- file: During_Fixed_Income_Ch15.md
  page: 127
created: '2026-04-13'
updated: '2026-04-21'
---

## Thesis

In the repo market, the interest rate (the price of cash) is fundamentally linked to the quality and scarcity of the security used as collateral. Alexander Düring explains that the market is bifurcated by the **driver** of the trade: is the participant seeking cash (GC) or seeking a specific document (Special)? This distinction creates a pricing hierarchy that is critical for market makers and short-sellers. [[During_Fixed_Income_Ch15.md#page=126]]

## Mechanism: The Pricing Dynamics

### 1. General Collateral (GC) - The Baseline
- **The Driver:** Cash placement or borrowing.
- **The Pricing:** Reflects the general risk-free rate plus a small risk premium based on the broad collateral class (e.g., German GC vs. Italian GC).
- **Control:** The borrower of cash has the "option" to deliver any bond within the defined GC basket. [[During_Fixed_Income_Ch15.md#page=126]]

### 2. Specials - The Scarcity Premium
- **The Driver:** The need to possess a specific ISIN (e.g., to deliver against a futures contract or to cover a short position).
- **The Pricing:** When demand for a bond exceeds supply, cash lenders are willing to accept a lower return on their cash just to hold that bond.
- **Cheapest-to-deliver (CTD):** [RAW] Neftci lưu ý ranh giới cung cầu: Các "shorts" trên thị trường Bond Futures cần giao một mã trái phiếu cụ thể có chi phí thấp nhất để thực hiện hợp đồng. Mã này thường bị "vắt kiệt" thanh khoản và trở nên đặc biệt nóng (go special) trong thị trường Repo.
- **The "Leasing" Mechanism:** [RAW] Neftci mô tả Special Repo như việc "thuê" (leasing) một chứng khoán. Trader không mua chứng khoán đó, mà dùng tiền mặt để đổi lấy quyền sở hữu tạm thời.
- **The Quote:** If the GC rate is 1.00% and a bond can only be borrowed by paying 0.20% on the cash, that bond is **"80bp special."**
- **Negative Rates:** In extreme scarcity, the repo rate for a bond can turn negative even when the GC rate is positive. This means the borrower of the security is effectively being paid to take the cash. [[During_Fixed_Income_Ch15.md#page=127]] [[Principles_of_Financial_Engineering_Neftci.md#page=153]]

---

## 3. Strategic Implications: The Interdealer Bridge

The **Interdealer Market** acts as the bridge between GC and Specials. 
- **The Arbitrage:** Dealers find bonds that have been lent out as GC (where they earn the high GC rate) and "pull them back" to lend them into the Specials market (where they borrow cash cheaply).
- **The Reward:** The dealer pockets the spread between the GC rate and the Special rate. This activity provides essential liquidity to the bond market by making scarce securities available to those who need them most. [[During_Fixed_Income_Ch15.md#page=127]]

---

## 4. Market Interplay: Strips, Repo and Swap Spreads

[RAW] Neftci bóc tách mối quan hệ liên thị trường giữa các công cụ:
- **Strips and Specialness:** Nếu các trái phiếu có coupon (whole-coupon bonds) bị "tách" thành các Zero-coupon bonds (Strips) và được các nhà đầu tư nắm giữ đến hạn, số lượng trái phiếu nguyên bản lưu hành sẽ giảm xuống. Sự khan hiếm này làm tăng xác suất trái phiếu đó trở nên "Special" trên thị trường Repo.
- **Link to Swap Spreads:** Khi trái phiếu trở nên Special, lãi suất Repo giảm xuống (chi phí funding rẻ đi). Sự sẵn có của vốn rẻ làm cho việc **trả lãi suất cố định (Paying Fixed)** trở nên hấp dẫn hơn so với nhận cố định. Điều này có thể dẫn đến sự gia tăng của **Swap Spreads** trung bình trên thị trường.
- **Caveat:** Tuy nhiên, ranh giới này gây tranh cãi vì đa số trái phiếu bị tách (stripped) thường là loại **Off-the-run**, vốn ít khi trở nên Special so với các loại On-the-run.

---

## Evidence / Source Anchors

- Definition of GC as cash-focused with discretion over collateral: [[During_Fixed_Income_Ch15.md#page=126]]
- Definition of Special as security-focused where lenders accept lower rates: [[During_Fixed_Income_Ch15.md#page=127]]
- Analysis of how "Specialness" is quantified as a basis point spread below GC: [[During_Fixed_Income_Ch15.md#page=127]]
- Role of interdealer brokers in capturing the GC-Specials spread: [[During_Fixed_Income_Ch15.md#page=127]]
- Analysis of Strips and specialness risk: [[Principles_of_Financial_Engineering_Neftci.md#page=169]]

## Related

- [[Repurchase_Agreement_Repo_Market_Structure]] — The broader market context.
- [[Short_Selling_Mechanics]] — The primary driver of Specials demand.
- [[Bond_Futures_Contract_Design]] — Why certain bonds become Special during delivery cycles.
- [[Collateral_Transformation_And_TSLF]] — Upgrading collateral from non-Special to GC-eligible.
