---
title: BoJ QE 2013 Case Study
aliases:
- Bank of Japan 2013 Quantitative Easing
- Kuroda QE Implementation
- JGB Market Seizure 2013
type: evidence
tags:
- central-banking
- boj
- qe
- fixed-income
status: verified
confidence: 5
half_life_years: 1
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Chương trình QE năm 2013 của Ngân hàng Trung ương Nhật Bản minh họa tầm quan
  trọng của kỹ thuật vận hành và truyền thông; lợi suất trái phiếu đã tăng ngược chiều
  kỳ vọng do ma sát trong quy mô vận hành và thông điệp không rõ ràng.
source_refs:
- file: During_Fixed_Income_Ch10.md
  page: 71
created: '2026-04-13'
updated: '2026-04-22'
---

## Case Study Overview

On April 4, 2013, the Bank of Japan (BoJ) under Governor Kuroda announced a massive QE expansion, purchasing around 70% of gross Japanese Government Bond (JGB) issuance across multiple asset classes (CP, corporate bonds, ETF, REIT).

Despite the announcement of unprecedented buying, JGB yields **increased**. Over a year after the start of QE, Japanese 10Y yields (0.6%) were still higher than they were before the announcement. [[During_Fixed_Income_Ch10.md#page=71]]

## Evidence: Failure Points in Implementation

Two primary factors explain the paradoxical yield increase:

### 1. Communication Ambiguity
Governor Kuroda was ambiguous about the exact channels through which QE was expected to work. When yields rose, he expressed indifference, stating it was an expression of higher inflation expectations. This caused market participants to struggle with the price signal the BoJ wanted to send—or whether it wanted to send one at all. [[During_Fixed_Income_Ch10.md#page=71]]

### 2. Operational Size Friction
The BoJ initially scheduled 11 operations per month, each with a massive size of JPY 1 trillion (EUR 7 billion). Market dealers judged these sizes as too large to effectively source and offer securities at each operation.
- **Result:** Market disappointment led to a sharp sell-off in JGBs immediately following the initial rally.
- **The Fix:** The BoJ had to refine its schedule twice within the first two months, increasing the frequency of operations (to 19 per month) while reducing the size of each to JPY 700 billion to match dealer capacity. [[During_Fixed_Income_Ch10.md#page=72]]

## Evidence: The Feedback Loop of Volatility

The spike in yields caused significant problems for commercial banks holding JGBs for carry.
- **The VaR Effect:** Higher volatility along the yield curve (especially the 2Y–5Y spread) triggered increased Value-at-Risk (VaR) charges.
- **The Panic:** Banks sold intermediate JGBs to reduce risk, creating a second wave of selling and further volatility. This rapid divestment by the private sector was an unintended and negative outcome of the initial policy announcement. [[During_Fixed_Income_Ch10.md#page=72]]

## Historical Context: The 2003 VaR Shock

The 2013 experience echoed the "VaR Shock" of summer 2003.
- **The Lesson:** When volatility has been suppressed for years by central bank easing, market-makers and short-sellers are weeded out.
- **The Crash:** When an external shock (like a change in Fed policy) returns volatility to such a market, existing long positions are hit with massive VaR charges. In a market with no short-sellers to provide liquidity on the way down, the resulting stop-loss selling creates a self-accelerating downward feedback loop. [[During_Fixed_Income_Ch10.md#page=72]]

## Evidence / Source Anchors

- Paradoxical increase in JGB yields after 2013 QE announcement: [[During_Fixed_Income_Ch10.md#page=71]]
- Impact of communication ambiguity on market interpretation: [[During_Fixed_Income_Ch10.md#page=71]]
- Failure of large JPY 1tr operation sizes (dealer friction): [[During_Fixed_Income_Ch10.md#page=72]]
- Connection between volatility, VaR charges, and bank sell-offs: [[During_Fixed_Income_Ch10.md#page=72]]
- Analysis of the 2003 VaR shock and the feedback loop of stop-loss selling: [[During_Fixed_Income_Ch10.md#page=72]]

## Related

- [[Quantitative_Easing_Channels]] — Specifically the Volatility channel (H).
- [[VaR_Shock_Mechanism]] — The technical driver of the market crash.
- [[Negative_Interest_Rate_Mechanics]] — The subsequent policy move in Japan (2016).
- [[Operational_Framework_Principles]] — Why implementation details (size/frequency) matter.
- [[Taper_Tantrum_2013_Case_Study]]
- [[Repo_Spike_September_2019_Case_Study]]
