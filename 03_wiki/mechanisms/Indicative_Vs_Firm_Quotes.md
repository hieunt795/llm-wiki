---
title: Firm vs Indicative Quotes
aliases:
- Firm Price
- Indicative Price
- One-way Quote
- Two-way Quote
- Choice Price
- Subject Quote
- Last Look
type: mechanism
tags:
- market-infrastructure
- trading
- OTC
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch12.md
thesis: The distinction between firm and indicative quotes defines the legal and operational
  commitment of a market maker to execute a trade at a specific price.
source_refs:
- file: During_Fixed_Income_Ch12.md
  page: 86
- file: During_Fixed_Income_Ch12.md
  page: 89
- file: During_Fixed_Income_Ch12.md
  page: 90
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

In OTC markets, price discovery is a bilateral process. A market maker provides different levels of price commitment depending on the stage of the negotiation. Understanding the nuances of "Firm" vs. "Indicative" and "Subject" quotes is essential to avoid violating market protocols or incurring execution risk. [[During_Fixed_Income_Ch12.md#page=86]]

## Mechanism: Types of Price Quotes

### 1. Indicative Price
- **Commitment:** No immediate willingness to trade.
- **Usage:** Market makers provide indicative prices on a continuous basis (e.g., on Bloomberg/Reuters screens) to signal where the market is.
- **Information Reveal:** Requesting an indicative price signals interest without revealing an intent to trade immediately. [[During_Fixed_Income_Ch12.md#page=86-89]]

### 2. Firm Price
- **Commitment:** A binding offer to execute a trade.
- **Usage:** Provided only upon request for a specific size.
- **Protocol:** A firm price inquiry reveals an intent to trade and thus reveals information about the customer's position. [[During_Fixed_Income_Ch12.md#page=86-89]]

### 3. Subject Quote (or "Your Risk")
- **Commitment:** A previously firm quote that the dealer no longer feels bound by.
- **Trigger:** Too much time has passed or the market has moved significantly.
- **Protocol:** In bilateral communication, a dealer indicates this by stating "subject" or "your risk." [[During_Fixed_Income_Ch12.md#page=89]]

### 4. Special Quote Types
- **Two-way:** Includes both a Bid (buy) and an Ask (sell).
- **One-way:** Only a Bid or an Ask.
- **Choice Price:** A rare quote where the Bid and Ask are the same price. This maximizes the chance of execution and provides the dealer with valuable information about market direction. [[During_Fixed_Income_Ch12.md#page=87]]

## Strategic Protocol: "Last Look"

The term **Last Look** has different meanings depending on the asset class:

- **In Fixed Income:** A customer who has asked multiple dealers for prices (In Competition) gives one specific dealer the option to match the best price found to conclude the trade. It is an option granted *by the client* to a preferred dealer. [[During_Fixed_Income_Ch12.md#page=90]]
- **In FX (Comparison):** It is an option granted to the market maker *by default* to reject a trade after the customer has accepted it.

## Boundaries / Conditions: Market Usance
Rejecting a trade after a customer has accepted a firm quote is considered "bad form" unless there is a legitimate reason (e.g., late acceptance). The conclude-of-trade convention requires the dealer to confirm with "Done" or reject with "Off that." [[During_Fixed_Income_Ch12.md#page=90]]

## Evidence / Source Anchors

- Distinction between indicative and firm price commitment: [[During_Fixed_Income_Ch12.md#page=86]]
- Definition of Choice Price as an information-gathering tool: [[During_Fixed_Income_Ch12.md#page=87]]
- The logic of "Subject" quotes and "Your Risk" vernacular: [[During_Fixed_Income_Ch12.md#page=89]]
- Definition of "Last Look" in fixed income vs. FX markets: [[During_Fixed_Income_Ch12.md#page=90]]

## Related

- [[OTC_Trade_Lifecycle]] — Where these quotes occur (Steps 1-3).
- [[Bid_Ask_Bounce]] — How two-way quotes create artificial volatility.
- [[Information_Leakage_In_Trading]] — The risk of asking for multiple firm quotes.
- [[OTC_Trading_Conventions]] — The language of "Mine", "Yours", "Done", and "Off that".
