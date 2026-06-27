---
title: Counterparty Credit Risk
aliases:
- Swap Counterparty Credit Risk
- Derivatives Counterparty Risk
- Closeout Netting
- Safe Harbor for Swaps
type: mechanism
tags:
- derivatives
- risk-management
- fixed-income
- market-infrastructure
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat | Alexander Düring"
provenance: "Tuckman_Serrat_Fixed_Income_2022.md"
thesis: Counterparty credit risk in swaps is the risk that a positive-NPV contract cannot be monetized after the other side defaults; margin, close-out netting, and collateral transform that risk into liquidity and replacement-cost risk.
source_refs:
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 334
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 335
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 336
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 337
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 338
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 339
created: '2026-04-29'
updated: '2026-04-29'
---

## Thesis

[RAW-BOOK] In a swap, the exposed party is the counterparty with positive NPV: if the other side defaults, the survivor must terminate, net, seize collateral if available, and replace the economics of the lost trade at current market terms. [[Tuckman_Serrat_Fixed_Income_2022.md#page=334]]

## 1. Core Logic / Mechanism

[RAW-BOOK] INTENT: Tuckman frames counterparty credit risk as a close-out problem, not merely a probability-of-default label. The loss is not the notional amount; it is the positive replacement value that may be lost when the defaulting party stops performing. The legal safe harbor for swaps is central because it allows the survivor to terminate contracts under the master agreement, net receivables and payables, and liquidate collateral rather than waiting through a bankruptcy stay. [[Tuckman_Serrat_Fixed_Income_2022.md#page=334]]

[RAW-BOOK] MECHANISM: variation margin covers current exposure by moving cash or collateral as NPV changes. Under collateralized-to-market (CTM), VM is collateral against the current positive NPV. Under settled-to-market (STM), VM is an irrevocable daily settlement of profit and loss, closer to futures-style cash settlement. Initial margin covers the gap between VM calls: market moves, replacement cost, and liquidity cost over the margin period of risk. [[Tuckman_Serrat_Fixed_Income_2022.md#page=335]] [[Tuckman_Serrat_Fixed_Income_2022.md#page=336]]

[RAW-BOOK] INTERACTIONS: this node is the mechanism underneath [[Risk_and_Valuation_Adjustments_xVA]]. CVA prices expected counterparty loss; FVA/MVA price the funding and liquidity cost of collateral. It also links to [[Central_Counterparty_CCP]], because central clearing changes the identity of the counterparty and standardizes margin, but does not erase liquidity demands. [[Tuckman_Serrat_Fixed_Income_2022.md#page=338]]

## 2. Worked Example

[RAW-BOOK] If Counterparty A receives fixed and rates fall, A can have positive NPV against B. B posts VM to A. If rates then rise enough that B has positive NPV, A returns the previous VM and posts new VM to B. If A defaults after B has positive NPV, B closes out the old swap and uses VM, plus IM if needed, to pay a replacement counterparty to enter the economically equivalent trade at current terms. [[Tuckman_Serrat_Fixed_Income_2022.md#page=335]] [[Tuckman_Serrat_Fixed_Income_2022.md#page=337]]

## 3. Failure Conditions / Boundaries

[RAW-BOOK] VM is sufficient only immediately after a margin call. Between calls, NPV can move, liquidity can disappear, and the surviving party must hedge or replace the exposure during MPOR. If the market move plus replacement cost exceeds posted IM, the survivor has residual loss. This boundary is why margin models must incorporate both volatility and liquidity, not just today's mark-to-market. [[Tuckman_Serrat_Fixed_Income_2022.md#page=337]] [[Tuckman_Serrat_Fixed_Income_2022.md#page=338]]

[RAW-BOOK] Dodd-Frank shifted liquid swaps toward trading, clearing, reporting, and margin rules, while exempting many nonfinancial commercial hedgers from clearing and margin. The policy trade-off is explicit: stricter collateralization reduces counterparty credit exposure but can create liquidity stress for users whose business model is economically hedged but cash-poor under margin calls. [[Tuckman_Serrat_Fixed_Income_2022.md#page=338]] [[Tuckman_Serrat_Fixed_Income_2022.md#page=339]]

## Related

- [[Risk_and_Valuation_Adjustments_xVA]]
- [[Central_Counterparty_CCP]]
- [[Variation_Margin_Vs_Initial_Margin]]
- [[Interest_Rate_Swap_Use_Cases]]
- [[Interest_Rate_Swap_Plain_Vanilla]]
