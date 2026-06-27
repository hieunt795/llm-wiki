---
title: Bond Index Principles
aliases:
- Market Index
- Replicability
- Measurability
- Ex-ante Definition
- Chỉ số trái phiếu
type: definition
tags:
- index
- market-infrastructure
- risk-management
- portfolio-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch35.md
thesis: A bond index is a default portfolio designed to represent an investable market
  subset, governed by a triple mandate of ex-ante definition, replicability, and measurability
  to ensure objective performance benchmarking.
source_refs:
- file: During_Fixed_Income_Ch35.md
  page: 378
- file: During_Fixed_Income_Ch35.md
  page: 379
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Bond indices are the "yardsticks" of the asset management industry. Alexander Düring explains that a valid index must be more than just a list of bonds; it must represent a realistic and executable investment universe. Many popular indices, however, fall short of this ideal, incorporating illiquid or theoretical assets that create persistent tracking errors for real-world funds. [[During_Fixed_Income_Ch35.md#page=378]]

## The Triple Mandate of a Market Index

Any robust index must satisfy three fundamental requirements:

### 1. Ex-ante Definition
The rules for inclusion must be known before the investment period starts.
- **The Failure:** Definitions like "the top ten performers of the month" are ex-post and cannot be used for forward-looking investment decisions. [[During_Fixed_Income_Ch35.md#page=378]]

### 2. Replicability (Tính khả thi)
An investor must be able to actually purchase the constituents in the open market.
- **The Paradox:** Broad corporate bond indices often include issues older than one year. These bonds are typically locked in insurance company vaults and never trade, making the index impossible to replicate with new capital.
- **Theoretical Assets:** Some indices, like the German **REX Index**, use theoretical bonds with coupons that do not exist (e.g., 6% coupons in a 0% environment). Investors must use substitute assets (like Pfandbriefe), exposing them to unintended spread risk. [[During_Fixed_Income_Ch35.md#page=378]]

### 3. Measurability
The index must be valueable at a reliable frequency (usually daily) using transparent prices.
- **Real Estate & Private Equity:** Indices in these classes are often considered "un-measurable" at high frequencies due to a lack of transparent transaction data. [[During_Fixed_Income_Ch35.md#page=379]]

## Strategic Implications: The Pricing Bias

Index providers resolve the ambiguity of "fair value" through specific pricing conventions:
- **Liquidation Basis:** Existing long positions are valued at **Bid prices** (accounting for the cost of selling).
- **Inclusion Basis:** Bonds entering the index are often valued at **Ask prices**, reflecting the presumption that a tracker must buy them.
- **The Result:** Indices inherently incorporate a bid–offer spread, making the "cost of trading" part of the benchmark itself. [[During_Fixed_Income_Ch35.md#page=379]]

## Evidence / Source Anchors

- Establishment of the three fundamental requirements (Ex-ante, Replicable, Measurable): [[During_Fixed_Income_Ch35.md#page=378-379]]
- Analysis of the REX index and the necessity of substitute assets: [[During_Fixed_Income_Ch35.md#page=378]]
- Discussion on why illiquid assets (Private Equity/Real Estate) lead to measurability failures: [[During_Fixed_Income_Ch35.md#page=379]]
- Contrast between the mathematical map of outstanding amounts ($i \mapsto N_i$) and realistic pricing ($i \mapsto p_i$): [[During_Fixed_Income_Ch35.md#page=379]]
- Description of the Bid-Ask bias incorporated into index returns: [[During_Fixed_Income_Ch35.md#page=379]]

## Related

- [[Bond_Index_Rebalancing_Mechanics]] — How the index universe changes over time.
- [[Index_Tracking_And_Replication_Risk]] — How to manage the failure of the Replicability mandate.
- [[Liquidity_Measurement_Taxonomy]] — The pricing inputs for Step 3 (Measurability).
- [[Portfolio_Rebalancing_Strategies]] — The investor-side reaction to index changes.
