---
title: Winner's Curse in Trading
aliases:
- Trade in comp
- Winner's Curse
- Lời nguyền kẻ thắng thầu
type: perspective
tags:
- market-dynamics
- trading
status: verified
confidence: 5
half_life_years: 5
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: extracted from _temp_ch11.md
thesis: 'In competitive quotes (''in comp''), the winning dealer suffers from winner''s
  curse: they offered the best price for the client, but their competitors are now
  aware of the dealer''s new position and will move the market against them.'
source_refs:
- file: Fixed Income Trading and Risk Management - Alexander Düring
  page: 89
- file: Fixed Income Trading and Risk Management - Alexander Düring
  page: 97
created: '2026-04-13'
updated: '2026-04-18'
---

## Thesis

Competitive bidding ("trading in comp") is often mandated for best execution, but it creates a specific disadvantage for the winning dealer known as the **Winner's Curse**. Not only did the dealer provide the most aggressive price (lowest bid or highest offer), but the losing dealers are now alerted to the trade interest. They can adjust their own quotes to make it more expensive for the winning dealer to hedge or unwind the position, potentially defeating the purpose of seeking the best price. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=89, 97]]

## Thesis

1. **Information Leakage:** Asking multiple dealers for a price reveals the client's intent to a wider group. Even dealers who lose the trade now know that a specific position exists in a competitor's book. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=97]]
2. **Adverse Market Movement:** Losing dealers may move their quotes in a direction that makes the winner's hedge more costly.
3. **The Best Execution Paradox:** While "in comp" is a tool for regulators to check for best execution, for very large trades, a **single dealer inquiry** may result in a better overall outcome by preventing the market from moving before the trade is fully hedged. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=98]]

## Mechanism

- **Trade Size:** Winner's curse is less meaningful for small, liquid trades but critical for large blocks.
- **Client Discretion:** Sophisticated clients judge whether to trade in comp or with a single dealer based on the liquidity of the security and the potential for market impact. [extracted] [[Fixed_Income_Alexander_During_Ch12.md#page=98]]

## Evidence / Source Anchors

- Market vernacular for competitive quotes: "in comp": [[Fixed_Income_Alexander_During_Ch12.md#page=89]]
- Analysis of dealer behavior post-competitive quote: [[Fixed_Income_Alexander_During_Ch12.md#page=97]]
- The argument for single-dealer inquiries for large trades to prevent information leakage: [[Fixed_Income_Alexander_During_Ch12.md#page=98]]

## Related

- [[Information_Leakage_In_Trading]] — The underlying cause of the winner's curse.
- [[Indicative_Vs_Firm_Quotes]] — How clients signal intent to dealers.
- [[OTC_Trading_Conventions]] — The process of rewarding dealers with "cover" information.
