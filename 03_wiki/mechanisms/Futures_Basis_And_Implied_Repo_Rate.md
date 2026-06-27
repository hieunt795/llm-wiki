---
title: Futures Basis and Implied Repo Rate
aliases:
- Gross Basis
- Net Basis
- Implied Repo Rate
- IRR
- Basis Trading
type: mechanism
tags:
- fixed-income
- derivatives
- trading
- repo
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch29.md
thesis: The relationship between bond and futures prices is quantified through Gross
  Basis, Net Basis, and the Implied Repo Rate (IRR), three interchangeable metrics
  that measure the convergence profit and the cost of carry inherent in the delivery
  process.
source_refs:
- file: During_Fixed_Income_Ch29.md
  page: 310
- file: During_Fixed_Income_Ch29.md
  page: 311
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Because a futures contract and its underlying bond move in the same direction with interest rates, their relative value is far more stable than their absolute prices. Alexander Düring explains that the **Basis** is the primary "currency" of futures traders. It measures the mismatch between the cash market and the futures market, with the **Implied Repo Rate** providing a direct comparison to actual financing costs. [[During_Fixed_Income_Ch29.md#page=310]]

## Mechanism: The Three Metrics

### 1. Gross Basis
The raw price difference between the cash bond and the futures-implied price.
- **Formula:** $\text{Gross Basis} = \text{Spot clean price} - (\text{Conversion factor} \times \text{Futures price})$
- **Usage:** Trading the gross basis (Buying the Basis) means buying the bond and selling the future. It is a very liquid trade with low directional risk. [[During_Fixed_Income_Ch29.md#page=310]]

### 2. Net Basis
The basis adjusted for the **Carry** between the spot settlement and the futures delivery date.
- **Formula:** $\text{Net Basis} = \text{Forward clean price} - (\text{Conversion factor} \times \text{Futures price})$
- **Or:** $\text{Net Basis} = \text{Gross Basis} - \text{Carry}$
- **Significance:** In theory, the net basis of the **CTD** should be zero. A positive net basis implies the bond is too expensive to deliver; a negative net basis signals a [[Bond_Futures_Squeeze_Dynamics|Squeeze]]. [[During_Fixed_Income_Ch29.md#page=311]]

### 3. Implied Repo Rate (IRR)
The break-even financing rate that makes the net basis exactly zero.
- **Interpretation:** [RAW] Neftci định nghĩa IRR là chi phí vốn (carry cost) khiến cho chiến lược Cash-and-carry (Mua trái phiếu + Repo tài trợ) có kết quả kinh tế đúng bằng giá tương lai.
- **Formula (Neftci):**
  $$R_{t0} = \left( \frac{P_{futures}}{P_{bond}} - 1 \right) \times \frac{360}{days}$$
  Trong đó $P_{bond}$ là giá trái phiếu tại $t_0$ và $P_{futures}$ là giá thanh toán tương lai. 
- **CTD Rule:** In many markets (notably the US), the bond with the **highest IRR** is considered the CTD. However, Düring warns this is not always true in the Eurozone where "Specials" repo rates can distort the relationship. [[During_Fixed_Income_Ch29.md#page=311-312]] [[Principles_of_Financial_Engineering_Neftci.md#page=166]]

## Strategic Implications: The Convergence Bridge

A futures contract will fail to attract Genuine interest without a deep and liquid repo market.
- **The Link:** The repo market provides the "bridge" that allows arbitrageurs to enforce the relationship between spot and futures prices.
- **Failure Case:** The Eurex Euro-Jumbo Pfandbrief contract (1999) failed precisely because no liquid repo market existed for the underlying Pfandbriefe to facilitate basis trading. [[During_Fixed_Income_Ch29.md#page=310]]

## Evidence / Source Anchors

- Definition of Gross Basis and the "mnemonic" convention (Bond/Basis): [[During_Fixed_Income_Ch29.md#page=310]]
- Derivation of the Net Basis formula and its role in CTD identification: [[During_Fixed_Income_Ch29.md#page=311]]
- Definition of the Implied Repo Rate as the financing rate making net basis zero: [[During_Fixed_Income_Ch29.md#page=311]]
- Analysis of the necessity of the repo market for futures success: [[During_Fixed_Income_Ch29.md#page=310]]
- Table of sample basis calculations (Table 28.1): [[During_Fixed_Income_Ch29.md#page=315]]

## Related

- [[Cheapest_To_Deliver_CTD]] — How the basis helps select the bond.
- [[Bond_Carry_And_Forward_Pricing]] — The $Forward\ Price$ input for Net Basis.
- [[Repurchase_Agreement_Repo_Market_Structure]] — The market that provides the actual repo rate to compare against the IRR.
- [[Cash_And_Carry_Arbitrage]] — The strategy being quantified by these metrics.
