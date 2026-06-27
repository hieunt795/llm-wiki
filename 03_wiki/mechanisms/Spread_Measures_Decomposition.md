---
title: Spread Measures and Bond Decomposition
aliases: [Spread measures, Credit spreads, I-spread, Z-spread, TED spread, OAS, Option-adjusted spread, Bond yield decomposition]
type: mechanism
tags: [fixed-income, credit-risk, valuation, spreads]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Bond yields decompose into risk-free rate + credit spread. Multiple spread measures exist for different purposes: I-spread and Z-spread measure credit risk in absolute terms; OAS accounts for embedded options; TED spread measures bank credit risk; swap spreads measure LIBOR premium; ASW spread measures relative value. Choosing the right spread metric depends on the analytical purpose.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 3063-3248
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 4491-4504
    section: "Chapter 5.5: Summary of Yield Measures"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Bond yield = risk-free rate + credit spread (simplified). Multiple spread measures decompose yields differently: (1) **I-spread (Interpolated)** = bond yield - interpolated government yield at same maturity; assumes credit risk constant across curve. (2) **Z-spread (zero-volatility)** = constant spread over entire spot curve that discounts bond cash flows to market price; more accurate than I-spread for bonds with varying credit risk by tenor. (3) **OAS (Option-Adjusted Spread)** = Z-spread adjusted for embedded options (callability, prepayment) by removing option cost from spread; true credit spread only. (4) **TED spread** = 3m LIBOR - 3m T-bill; measures banking sector credit risk relative to government, liquidity in money markets. (5) **Swap spread** = swap rate - government yield; measures LIBOR bank sector premium. (6) **Asset Swap Spread (ASW)** = bond yield - swap rate; equivalent to cost of converting fixed bond into LIBOR + spread floater.

## I-Spread (Interpolated Spread)

[RAW-BOOK:5] Simplest spread measure: bond yield - interpolated government yield at same maturity. Assumes credit risk is uniform across maturity spectrum. Limitation: may not accurately reflect credit risk if bonds have different embedded options or coupons. Advantage: easy to calculate, intuitive interpretation. Used for quick market comparisons but less precise for detailed analytics.

## Z-Spread (Zero-Volatility Spread)

[RAW-BOOK:5] More rigorous: constant spread added to entire zero-coupon (discount factor) curve such that discounted bond cash flows equal market price. Advantage: accounts for credit risk variation across maturities (each cash flow discounted at appropriate tenor zero rate + Z-spread). More accurate than I-spread for analytical purposes. Methodology: iteratively solve for spread that zeros net present value. Limitation: assumes credit spread constant (parallel shift across curve); non-parallel credit curve moves cause Z-spread to change even if credit quality unchanged.

## OAS (Option-Adjusted Spread)

[RAW-BOOK:5] Z-spread adjusted for embedded options (e.g., callable bonds with issuer call option, mortgage-backed securities with prepayment option). OAS removes the cost of the embedded option from Z-spread to isolate true credit spread. Formula: Z-spread = OAS + option cost. For callable bonds: bond can be called by issuer if rates fall → reduces upside for investor → option valuable to issuer, cost to investor. OAS higher than Z-spread when options are in-the-money (valuable). Used for bonds with significant embedded options where Z-spread alone would overstate credit risk.

## TED Spread

[RAW-BOOK:5] TED = 3-month LIBOR - 3-month US Treasury bill yield (or euribor - government equivalent). Measures credit/liquidity risk of LIBOR banking panel relative to government. Widens during banking stress (LIBOR rises as lenders demand premium for bank credit risk). Narrows when confidence in banks returns. Indicator of financial system stress; historically ranges 25-50bps in normal times, spiked to 450+bps during 2008 crisis. More of a market risk indicator than a bond-specific spread.

## Related Spreads

[RAW-BOOK:5] **Swap spread** = IRS swap rate - government yield (covered separately in Swap_Spread_Dynamics). **Asset Swap Spread (ASW)** = bond yield - swap rate (or equivalently, I-spread - swap spread). ASW represents pure relative value of bond vs. synthetic FRN (bond + pay-fixed swap = LIBOR + ASW floater). Useful for comparing credit spreads across currencies/markets without yield-curve timing bias. **CDS Spread** = covered separately; represents pure credit risk from protection market. **Basis between cash bond spreads and CDS spreads** can signal relative value opportunities.

---

## Comparative Summary: Advantages and Drawbacks

[RAW-BOOK:5] **Credit Spread:** Measured as basis points over sovereign benchmark; overestimates default risk if spread incorporates liquidity premium or funding costs. **ASW Spread:** May differ from CDS spread (market's preferred pure default-risk measure); net of interest rate and funding risk. **OAS:** Requires model + implied volatility; better for bonds with embedded options. **Z-Spread:** Assumes parallel credit curve shifts; doesn't adjust for bonds held to maturity assumptions failing. **I-Spread:** Single-maturity point measure; ignores curve shape; less precise than Z-spread. **CDS Spread:** May suffer liquidity issues in some markets (esp. sovereign); not always accurate reflection of true credit risk.

## Related
- [[Credit_Spread_Pricing]] — Theory of credit spread valuation
- [[Swap_Spread_Dynamics]] — IRS spread mechanics and trading
- [[Asset_Swap_Spread_ASW]] — ASW-specific applications
- [[Bond_Spot_Pricing_DCF]] — DCF framework for all spread calculations
