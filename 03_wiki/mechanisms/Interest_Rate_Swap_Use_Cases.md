---
title: Interest Rate Swap Use Cases
aliases:
- Uses of Interest Rate Swaps
- IRS Use Cases
- Swap Hedging Use Cases
- Synthetic Floating-Rate Debt
type: mechanism
tags:
- derivatives
- fixed-income
- hedging
- asset-liability-management
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat"
provenance: "Tuckman_Serrat_Fixed_Income_2022.md"
thesis: Interest rate swaps are used either as leveraged duration instruments that change DV01 exposure without using cash principal, or as cash-flow transformers that convert fixed and floating obligations into the balance-sheet profile an institution wants.
source_refs:
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 329
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 330
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 331
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 332
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 333
created: '2026-04-29'
updated: '2026-04-29'
---

## Thesis

[RAW-BOOK] Tuckman & Serrat split IRS use cases into two economic readings: a swap is a leveraged bond-like duration position when the user cares about DV01, and an exchange of payment streams when the user cares about transforming actual cash-flow obligations. [[Tuckman_Serrat_Fixed_Income_2022.md#page=329]]

## 1. Core Logic / Mechanism

[RAW-BOOK] INTENT: the swap lets an institution separate asset selection from interest-rate exposure. A pension fund can keep its cash invested in the credit portfolio it wants, then receive fixed in long-dated IRS to add missing liability duration. In Tuckman's example, liabilities have DV01 above the corporate-bond portfolio, so receiving fixed fills the duration gap without forcing the fund to buy only long bonds. [[Tuckman_Serrat_Fixed_Income_2022.md#page=329]]

[RAW-BOOK] MECHANISM: pay-fixed and receive-fixed are not just payment labels; they are directional rate exposures. Receiving fixed gains when rates fall and therefore behaves like being long duration. Paying fixed gains when rates rise and therefore hedges future borrowing costs or fixed-income asset losses. This connects to [[DV01_Risk_Management]] because the hedge size is chosen by matching dollar sensitivity, not by matching notional mechanically. [[Tuckman_Serrat_Fixed_Income_2022.md#page=329]]

[RAW-BOOK] INTERACTIONS: swaps convert balance-sheet funding profiles. A bank that wants floating-rate assets can give a borrower a floating loan while arranging swaps so the borrower experiences a fixed-rate loan and the bank retains floating exposure. A bank that wants long-term floating-rate debt can issue fixed-rate debt in the deeper fixed market, then receive fixed and pay floating in IRS, creating synthetic floating-rate funding. [[Tuckman_Serrat_Fixed_Income_2022.md#page=333]]

## 2. Worked Example

[RAW-BOOK] A corporation expecting to issue fixed-rate debt can pay fixed today in a forward-starting swap. If swap rates rise before issuance, the higher coupon on the debt is offset by the gain on the pay-fixed hedge; if swap rates fall, the lower coupon is offset by the hedge loss. Tuckman's example locks a borrowing cost when the future credit spread over swaps is assumed stable. [[Tuckman_Serrat_Fixed_Income_2022.md#page=331]]

[RAW-BOOK] The dense point is that the hedge locks the swap-rate component, not the credit-spread component. BOUNDARY: if the issuer's spread widens relative to swaps, the swap hedge does not protect that widening; if a spot-starting swap is used instead of a forward-starting swap, the issuer adds curve risk because the hedge and the future debt do not reference the same forward interval. [[Tuckman_Serrat_Fixed_Income_2022.md#page=332]]

## 3. Failure Conditions / Boundaries

[RAW-BOOK] IRS hedging fails as a full funding hedge when the target risk is not pure rates. A corporate debt pre-hedge leaves issuer spread risk open; a bank back-to-back customer swap leaves counterparty and operational risk; a pension receive-fixed overlay can create margin-liquidity stress even when the economic duration hedge is correct. [[Tuckman_Serrat_Fixed_Income_2022.md#page=332]] [[Tuckman_Serrat_Fixed_Income_2022.md#page=333]]

## Related

- [[Interest_Rate_Swap_Plain_Vanilla]]
- [[DV01_Risk_Management]]
- [[Entity-Netted_Notionals_ENNs]]
- [[Asset_Swap_Spread_ASW]]
- [[Counterparty_Credit_Risk]]
