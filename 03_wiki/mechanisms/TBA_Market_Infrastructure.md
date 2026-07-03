---
title: TBA Market Infrastructure
aliases:
- TBA Trading
- To-Be-Announced
- Mortgage Forward Trading
- Assignment
type: mechanism
tags:
- rmbs
- mortgages
- market-infrastructure
- US-Treasury
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch28.md
thesis: The TBA (To-Be-Announced) market is the world's largest mortgage forward market,
  enabling the high-volume trading of fungible RMBS blocks before their underlying
  loan pools have been finalized or assigned.
source_refs:
- file: During_Fixed_Income_Ch28.md
  page: 289
- file: During_Fixed_Income_Ch28.md
  page: 290
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

RMBS trading in the United States is uniquely standardized. Alexander Düring explains that over 90% of trades occur in the **TBA (To-Be-Announced)** format. This architecture allows the mortgage market to function with a degree of liquidity similar to the US Treasury market, as it bypasses the complexity of individual loan pool analysis in favor of standardized forward contracts. [[During_Fixed_Income_Ch28.md#page=289]]

## Mechanism: The Forward Pipe

The TBA market operates on the principle of **Fungibility**:

### 1. The Forward Trade
- **Action:** A buyer and seller agree on a price for a generic block of mortgages (e.g., "Fannie Mae 30Y, 4.0% coupon") for a future settlement date.
- **The Information Gap:** At the time of the trade, the buyer has **no information** on the specific pool of mortgages. They are buying a "promise" that the pool will meet the standardized conformance criteria. [[During_Fixed_Income_Ch28.md#page=289]]

### 2. Assignment and Settlement
- **The Trigger:** Right before the settlement date, the seller "assigns" a specific pool of mortgages that satisfy the contract terms.
- **The Perfection:** Settlement only occurs once the respective mortgage pool has been originated, securitized, and assigned. [[During_Fixed_Income_Ch28.md#page=289]]

## Strategic Implications: Production Risk

Because TBA trades happen before loan pools are finalized, the market is exposed to **Production Risk** (the risk that fewer mortgages are originated than expected).

- **The Problem:** If a bank sells more TBA blocks than it successfully originates, it cannot settle the trade.
- **The Fix (Dollar Rolls):** To avoid default, the bank can enter a **Dollar Roll**. They buy back the current TBA and sell a forward TBA for the next settlement cycle. The price difference reflects the cost of carry and the backwardation penalty for failing to deliver. [[During_Fixed_Income_Ch28.md#page=290]]

## Evidence / Source Anchors

- Analysis of TBA trading dominating the private sector bond market (90% of US RMBS): [[During_Fixed_Income_Ch28.md#page=289]]
- Definition of conforming mortgages as the basis for TBA fungibility: [[During_Fixed_Income_Ch28.md#page=289]]
- Description of the assignment process before settlement: [[During_Fixed_Income_Ch28.md#page=289]]
- Identification of Dollar Rolls as the primary tool for managing production imbalances: [[During_Fixed_Income_Ch28.md#page=290]]
- Rationale for high price transparency in TBA markets due to standardization: [[During_Fixed_Income_Ch28.md#page=289]]

## Related

- [[Residential_Mortgage_Backed_Securities_RMBS]] — The securities traded in this market.
- [[Mortgage_Prepayment_Drivers]] — Why production speed is unpredictable.
- [[Conforming_Loan_Criteria]] — The rules that make TBA trading possible.
- [[Dollar_Roll_Mechanics]] — Detailed view of the backwardation adjustment.
- [[Market_Depth_Vs_Breadth]]
- [[On_The_Run_Liquidity_Premium]]
- [[Preferred_Habitat_Market_Distortions]]
- [[Bond_Market_Liquidity_Architectures]]
- [[Market_Portfolio_Paradox]]
- [[Primary_Market_Syndication_And_Auction_Mechanics]]
- [[Global_Sovereign_Bond_Markets]]
- [[Bid_Ask_Bounce]]
- [[Bond_Futures_Contract_Design]]
- [[Bond_Index_Principles]]
- [[Credit_Ratings_And_Migration]]
- [[Credit_Risk_Transfer_CRT]]
- [[European_Private_Credit_Market]]
- [[Financial_Deepening]]
- [[FRN_Market_Risk_Duration]]
- [[Futures_Market_Parameters]]
- [[German_Bunds_Market]]
- [[Herstatt_Risk]]
- [[Liquidity_Measurement_Taxonomy]]
- [[Margining]]
- [[Market_Maker_Vs_Liquidity_Provider]]
- [[Market_Risk_Framework]]
