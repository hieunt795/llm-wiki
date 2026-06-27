---
title: Basis Trade Crisis 2020
aliases:
- March 2020 Treasury Basis Sell-off
- Cash-Futures Arbitrage Failure
- 2020 Basis Trade Unwind
type: concept
tags:
- case-study
- arbitrage
- treasury-market
- liquidity-crisis
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat"
provenance: Tuckman_Serrat_2022.md
thesis: The March 2020 Basis Trade Crisis occurred when a 'dash for cash' during the
  COVID-19 pandemic caused Treasury yields and futures prices to decouple violently,
  forcing highly levered hedge funds to unwind long basis positions due to margin
  calls and funding risk, which in turn exacerbated market dysfunction.
source_refs:
- file: Tuckman_Serrat_2022.md
  page: 281
- file: Tuckman_Serrat_2022.md
  page: 284
- file: Tuckman_Serrat_2022.md
  page: 285
- file: Tuckman_Serrat_2022.md
  page: 286
created: '2026-04-20'
updated: '2026-04-22'
---

## Thesis

For years leading up to 2020, the Treasury basis trade (Long [[Cheapest_To_Deliver_CTD_Mechanism|CTD]] bond, Short futures) was considered a "money machine" for relative value hedge funds. However, the extreme volatility of March 2020 demonstrated that even "riskless" arbitrage is subject to **contingent liquidity risk** and **funding volatility**, which can force liquidation at the worst possible time. [[Tuckman_Serrat_2022.md#page=284]]

## The Dislocation: March 2020

1. **Dash for Cash:** As the pandemic hit, market participants sold even the most liquid assets (Treasuries) to raise cash.
2. **Yield Volatility:** Treasury yields became hyper-volatile. The net basis of the 10-year (TYM0) CTD widened from -4 ticks to over -18 ticks in a matter of days. [[Tuckman_Serrat_2022.md#page=285]]
3. **Liquidity Premium:** CTD bonds, usually the most liquid, traded at a significant premium relative to comparable non-deliverable bonds as liquidity demand spiked, but the basis itself widened as futures prices fell faster than cash. [[Tuckman_Serrat_2022.md#page=284]]

## Failure Points (Why Arbitrage Failed)

Hedge funds were forced out of "winning" long-term trades due to three primary frictions:

### 1. P&L and Loss Limits
While the basis trade is mathematically guaranteed to converge to zero at expiration, the interim mark-to-market losses were massive. A $1 billion trade could lose $3.2 million in a single day (against a target profit of only $2.5 million). Many funds hit **stop-loss limits**, forcing immediate exits regardless of fundamental value. [[Tuckman_Serrat_2022.md#page=285]]

### 2. Margin and Cash Requirements
- **Variation Margin:** Daily settlement on short futures positions required immediate cash.
- **Initial Margin Hikes:** Exchanges (CME) increased margin requirements as volatility rose (e.g., from $1,275 to $1,600 per contract), creating massive **margin calls**.
- **The Result:** Even if a fund had the stomach for the P&L volatility, it might not have the ready cash to satisfy the exchange. [[Tuckman_Serrat_2022.md#page=286]]

### 3. Funding (Repo) Risk
Traders using overnight repo faced two additional risks:
- **Rate Spikes:** While SOFR generally fell, the **99th percentile repo rate** (the rate paid by the most stressed borrowers) hit 174 bps on March 16, far above the median.
- **Haircut/Credit Risk:** Prime brokers reduced lending or increased haircuts on Treasuries, effectively forcing a reduction in position size. [[Tuckman_Serrat_2022.md#page=287]]

## Aftermath & Intervention

The crisis only stabilized after massive Federal Reserve intervention, including trillions in repo injections and the launch of the **Primary Dealer Credit Facility (PDCF)**, which restored liquidity to the Treasury and repo markets.

## Related

- [[Basis_Trade_Mechanics]] — The theoretical foundation.
- [[Cheapest_To_Deliver_CTD]] — Why the two legs are linked.
- [[Futures_Basis_And_Implied_Repo_Rate]] — The metric that decoupled.
- [[Market_Maker_Vs_Liquidity_Provider]] — Role of dealers in the crisis.
- [[Capital_Controls_Synthetic_Spot]]
- [[Cash_And_Carry_Arbitrage]]
- [[Tax_Arbitrage_Synthetic_Bonds]]
- [[OIS_And_Tenor_Basis_Swaps]]
- [[Repo_Spike_September_2019_Case_Study]]
- [[Breakeven_Trade_Mechanics]]
- [[Butterfly_Trade_Mechanics]]
- [[Coin_Value_Corridor]]
- [[collateral_scarcity_transmission]]
- [[Emergency_Liquidity_Assistance]]
- [[Asian_Crisis_Contagion]]
- [[ERM_Crisis_1992_Mechanics]]
