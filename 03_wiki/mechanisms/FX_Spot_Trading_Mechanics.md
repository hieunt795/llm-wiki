---
title: FX Spot Trading Mechanics
aliases:
- Spot FX Operations
- FX Quoting Process
- Spot Position Keeping
- Cơ chế giao dịch FX Spot
type: mechanism
tags:
- FX
- trading
- mechanics
- position-keeping
- treasury
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: ACI_Dealing_Certificate_Mastering.md
thesis: The mechanical operation of the spot foreign exchange market, involving two-way
  pricing (BOB), T+2 settlement conventions, and weighted-average position management
  to capture spread or speculate on volatility. / Hoạt động cơ học của thị trường
  ngoại hối giao ngay, bao gồm báo giá hai chiều (BOB), quy ước thanh toán T+2 và
  quản trị trạng thái theo giá bình quân gia quyền để thu chênh lệch hoặc đầu cơ biến
  động.
source_refs:
- file: ACI_Dealing_Certificate_Mastering.md
  page: 157
created: '2026-04-24'
updated: '2026-04-24'
---

# FX Spot Trading Mechanics

## Thesis
The mechanical operation of the spot foreign exchange market, involving two-way pricing (BOB), T+2 settlement conventions, and weighted-average position management to capture spread or speculate on volatility. / Hoạt động cơ học của thị trường ngoại hối giao ngay, bao gồm báo giá hai chiều (BOB), quy ước thanh toán T+2 và quản trị trạng thái theo giá bình quân gia quyền để thu chênh lệch hoặc đầu cơ biến động.


The spot foreign exchange market is the primary engine of the treasury dealing room, providing the foundation for pricing derivatives and managing liquidity.

## 1. Value Date Conventions
*   **Spot Date**: Standard settlement is **T+2** (two business days from deal date).
*   **Exceptions**:
    *   **TARGET Business Days**: For EUR trades, the settlement depends on the TARGET system being open (closed only on Christmas and New Year).
    *   **Islamic Weekend**: Middle Eastern currencies often settle on Saturdays/Sundays, with USD settlement adjusted for the western weekend.
*   **Ante-Spot**: Dealing for "Today" (Value Today) or "Tomorrow" (Value Tom). Requires an adjustment to the spot rate (FX Swap points) to cover the cost of carry.

## 2. Market Structure: Makers vs. Users
*   **Market Maker (Price Provider)**: Quotes a two-way price (Bid/Offer). They are committed to buying at the Bid and selling at the Offer for a specified amount.
*   **Market User (Price Taker)**: Calls the market maker to ask for a price and decides whether to deal on the quoted rates.
*   **BOB Rule**: Always remember **Bid/Offer for the Base currency**.
    *   *Left side*: Maker buys Base, User sells Base.
    *   *Right side*: Maker sells Base, User buys Base.

## 3. Quotation Methods
*   **Direct Quotation (USD Base)**: Variable units of local currency per 1 USD (e.g., USD/CHF 1.6600).
*   **Indirect Quotation (Non-USD Base)**: Variable units of foreign currency per 1 unit of local currency (e.g., GBP/USD 1.4500, EUR/USD 0.9000).
*   **Cross Rates**: Calculated from two pairs involving a common base (usually USD).
    *   *Rule*: If USD is the base in one and quoted in the other, multiply or divide depending on the desired pairing.

## 4. Position Keeping
Dealers maintain an **Open Exchange Position** to track exposure.

### 4.1. The Weighted Average Method
Dealers calculate a running breakeven rate for their position.
*   **Example**:
    1. Buy 1M EUR at 0.9000 = 900,000 USD.
    2. Buy 2M EUR at 0.9030 = 1,806,000 USD.
    3. Total Position: Long 3M EUR.
    4. Average Rate: $(900,000 + 1,806,000) / 3,000,000 = 0.9020$.

### 4.2. Mark to Market (MtM)
Positions are revalued against the current market rate to assess unrealized profit/loss.
*   **Value of One Point Rule**: 
    *   For major currencies (4 decimal places): 1 point (0.0001) on 1 million base units = **100 units** of quoted currency.
    *   For JPY (2 decimal places): 1 point (0.01) on 1 million base units = **10,000 units** of quoted currency.

## 5. Trading Jargon
*   **Big Figure**: The stable part of the rate (e.g., 1.45 in 1.4520).
*   **Pips/Points**: The volatile last digits (e.g., 20).
*   **"Mine"**: I buy the base currency (taking your offer).
*   **"Yours"**: I sell the base currency (hitting your bid).
*   **"The Figure"**: Rate ending in .00.
*   **"Around the Figure"**: A quote spanning the .00 mark (e.g., 95/05).


## Related

- [[Order_Flow_FX_Determination]]
- [[OTC_Vs_Exchange_Trading]]
