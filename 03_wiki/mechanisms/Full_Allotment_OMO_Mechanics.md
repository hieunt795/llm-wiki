---
title: Full Allotment Open Market Operations within a Corridor
aliases:
- Đấu thầu khối lượng cố định (Full Allotment)
- Fixed-rate full allotment
type: mechanism
tags:
- monetary-policy
- OMO
- liquidity-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Ulrich Bindseil
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: In a full allotment system, banks determine the liquidity volume by bidding
  such that the expected interbank rate equals the fixed OMO rate, shifting the forecasting
  burden and liquidity risk from the central bank to the banking system.
source_refs:
- file: Bindseil_Monetary_Policy_Operations.md
  page: 59
created: '2026-04-26'
updated: '2026-04-26'
chapter: 4
---

# [[Full_Allotment_OMO]]

## Thesis
[WIKI] Unlike standard OMO where the central bank sets the volume, Full Allotment OMO lets banks take as much liquidity as they want at a fixed rate ($i_{OMO}$). This ensures the market rate stays pinned to $i_{OMO}$ through bank bidding behavior.

## Mechanism

### The Bidding Logic
[RAW] Banks will bid in the operations such that the expected interbank rate prevailing after the conduct of the open market operation will be equal to the rate at which the full allotment OMO is offered. [[Bindseil_Monetary_Policy_Operations.md#page=59]]

[LLM] Banks calculate their bids based on their own forecasts of autonomous factors and the cost of falling into the standing facilities. The target bid volume follows the equation:
$$Bid = RR + B - \sigma_d \Phi^{-1}\left(\frac{i_{OMO} - i_D}{i_B - i_D}\right)$$

### Information Asymmetry and Noise
[RAW] In practice, information asymmetries (e.g. the central bank having a better aggregate banknote forecast than the banks) and bid aggregation issues will make a difference. [[Bindseil_Monetary_Policy_Operations.md#page=60]]

[LLM] Because individual banks focus on their own liquidity shifts rather than aggregate autonomous factors, the sum of bids often contains "noise." If the central bank stops forecasting and relies entirely on full allotment, this noise can lead to higher volatility in the overnight rate once the total bid volume is revealed.

### Crisis Performance: Euro Area (2008)
[RAW] The European Central Bank moved to such a framework in October 2008. Interestingly, during the crisis, euro area banks often bid in excess of what would have been implied by the model. Therefore, the post-allotment short-term interbank overnight interest rate was driven well below the rate of the fixed-rate tender. [[Bindseil_Monetary_Policy_Operations.md#page=61]]

[LLM] This "over-bidding" reflects precautionary liquidity demand during periods of high counterparty risk, effectively pushing the market rate toward the deposit facility floor (Variant 2 of one-directional steering).

## Evidence / Source Anchors
- [[Bindseil_Monetary_Policy_Operations.md#page=59]] — Definition of full allotment mechanism.
- [[Bindseil_Monetary_Policy_Operations.md#page=60]] — Comparison with standard volume-set OMO.
- [[Bindseil_Monetary_Policy_Operations.md#page=61]] — Historical application and crisis behavior (ECB 2008).

## Related
- [[Symmetric_Corridor_Approach]]
- [[One-directional_Standing_Facility]]
- [[Liquidity_Forecasting]]
- [[OMO_Tender_Mechanics]]
- [[Open_Market_Operations_And_Instruments]]
