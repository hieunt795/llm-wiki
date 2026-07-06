---
title: Swap Rate Survivorship Bias
aliases:
- Swap Spread Paradox
- Bank Credit vs Swap Rate
- Libor Panel Bias
type: mechanism
tags:
- derivatives
- swaps
- credit-risk
- behavioral-finance
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch30.md
thesis: The swap rate paradox—where swap rates are systematically lower than the bond
  yields of the prime banks they represent—is driven by survivorship bias, as the
  swap benchmark reflects only the funding costs of surviving panel members while
  bonds remain exposed to the specific default destiny of the issuer.
source_refs:
- file: During_Fixed_Income_Ch30.md
  page: 337
- file: During_Fixed_Income_Ch30.md
  page: 338
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

A persistent myth in finance is that the term structure of swap rates is equivalent to the senior unsecured funding costs of prime banks. Alexander Düring explains that this is mathematically and economically incorrect. While the floating leg of a swap (traditionally LIBOR) measures bank funding, the resulting **Swap Rate** exhibits a lower yield than the bonds issued by the very same banks due to a structural filter known as **Survivorship Bias**. [[During_Fixed_Income_Ch30.md#page=337]]

## Mechanism: The Filtered Benchmark

The divergence between swap rates and bank bond yields stems from how the reference index is constructed:

### 1. The LIBOR Panel Logic
LIBOR (the traditional floating leg) was calculated as a trimmed mean of quotes from a panel of "prime" banks.
- **The Rule:** If a bank's creditworthiness declines significantly, it is removed from the panel and replaced by a healthier institution.
- **The Result:** The benchmark always reflects the funding costs of banks that are currently "surviving" and healthy. [[During_Fixed_Income_Ch30.md#page=338]]

### 2. The Bond Default Logic
A bank bond, once issued, remains outstanding regardless of the bank's health.
- **The Outcome:** If a bank's credit deteriorates, its bond yields spike to reflect the specific risk of that institution. The bond buyer is exposed to that specific "default destiny" for the life of the instrument. [[During_Fixed_Income_Ch30.md#page=338]]

## Strategic Implications: The Swap Spread

Because of this bias, receiving fixed on a swap is fundamentally safer than holding a bank's senior unsecured bond.
- **The Spread:** The difference between a bank bond yield and the swap rate is usually positive. 
- **Systemic Risk:** In a crisis, this spread widens. While the swap rate stays relatively low (anchored by the "healthy" survivors), the yields on individual bank bonds explode as investors price in the risk of specific failures. [[During_Fixed_Income_Ch30.md#page=338]]

## Evidence / Source Anchors

- Analysis of the persistent myth linking swap rates to prime bank funding: [[During_Fixed_Income_Ch30.md#page=337]]
- Identification of Survivorship Bias as the primary driver of the swap-bond yield gap: [[During_Fixed_Income_Ch30.md#page=338]]
- Contrast between the panel-removal mechanism of LIBOR and the permanent nature of bond issuance: [[During_Fixed_Income_Ch30.md#page=338]]
- Discussion on how swap rates reflect the funding costs of banks *at that time* rather than a fixed set of institutions: [[During_Fixed_Income_Ch30.md#page=338]]

## Related

- [[Interest_Rate_Swap_Plain_Vanilla]] — The instrument where this bias is embedded.
- [[LIBOR_Transition_And_Benchmarks]] — How the move to SOFR/€STR alters the nature of the survivorship bias.
- [[Credit_Risk_Taxonomy]] — The risk that the bond reflects but the swap "filters out."
- [[Asset_Swap_Spread_ASW]] — The metric used to trade this specific credit-swap relationship.
- [[Interest_Rate_Swap_Engineering]]
- [[Swap_Rate_Conversion_Conventions]]
- [[Swap_Trade_Compression_And_Recouponing]]
- [[Credit_Default_Swaps_CDS]]
- [[OIS_And_Tenor_Basis_Swaps]]
- [[CDS_Settlement_Auction]]
- [[Commodity_Swap_Engineering]]
- [[Currency_Swap_Engineering]]
- [[Equity_Swap_Engineering]]
- [[Forward_Rate_Agreements_FRA]]
- [[Futures_Basis_And_Implied_Repo_Rate]]
- [[FX_Swap_Engineering]]
- [[Interest_Rate_Swap_Use_Cases]]
- [[Basis_Swap_Spreads_Valuation]]
- [[Interest_Rate_Swap_IRS]]
- [[Forward_Swap_Relative_Value]]
- [[Swap_Spread_Dynamics]]
- [[Credit_Default_Swaps_Schofield]]
- [[Asset_Swap_Structure]]
- [[Interest_Rate_Options_Schofield]]
- [[Overnight_Index_Swap_OIS]]
- [[Credit_Instrument_Market_Risk_PV01_DV01]]
- [[Forward_Risk_Basis_Risk]]
- [[Interest_Rate_Option_Models]]
- [[Swap_Market_Risk_DV01_Carry_Rolldown]]
- [[Spot_Swap_Relationship]]
- [[Bermudan_Swaptions]]
- [[Portfolio_Rebalancing_Strategies]]
- [[Range_Accrual_Swaps]]
- [[Credit_Trading_Applications_Term_Structure_And_Single_Entity]]
