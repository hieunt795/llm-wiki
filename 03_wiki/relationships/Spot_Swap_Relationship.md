---
title: Spot-Swap Relationship
aliases: [Swap pricing, Spot-swap link, Bond-pair equivalence]
type: relationship
tags: [fixed-income, derivatives, swap-mechanics, pricing-relationships]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Swap value = value of fixed-coupon bond minus value of floating-rate note. Fixed cash flows discounted at zero-coupon rates. Swap fairly priced when both legs have equal present value. Forward-starting swaps priced by removing near-term cash flows and solving for new fixed rate.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 1332-1512
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Swap = buy fixed bond + issue floating note. Fair swap: PV(fixed leg) = PV(floating leg). Fixed leg discounted at zero-coupon swap rates. Floating leg = forward LIBOR rates. Circularity resolved via observable vanilla swap quotes. Forward-starting swap: remove initial cash flows, solve for fixed rate. CVA + OIS discounting post-crisis (collateral valued at OIS, not LIBOR).

## Post-Crisis: CVA and OIS Discounting (2.5.1)

[RAW-BOOK:5] Prior to financial crisis (pre-2010), swap traders subjectively adjusted prices for counterparty default risk. Post-crisis formalization: Credit Value Adjustment (CVA) method adjusts quoted prices to reflect counterparty's CDS spread. Discount rate choice changed fundamentally: tradition was LIBOR (assumed interbank counterparties wouldn't default). Under CSA (ISDA Credit Support Annex), collateral earns overnight index rate (OIS: SONIA/EONIA/Fed Funds), not LIBOR. For collateralized swaps: discount using OIS curve (reflects collateral rate earned). For uncollateralized swaps: discount at bank's own cost of borrowing (no common benchmark post-crisis). LIBOR-OIS spread widened post-crisis, creating valuation mismatch between collateral (OIS-discounted) and swap (LIBOR-discounted). Worked example: 1-year out-of-money swap marked -0.5% on $100 notional. LIBOR discounting: PV = 0.5% / 1.03 = $0.4854. OIS discounting at 2%: PV = 0.5% / 1.02 = $0.4902 (higher, since collateral earns lower OIS rate). Discount rate choice must be consistent with actual collateral or financing terms.

## Forward-Swap Decomposition (2.6)

[RAW-BOOK:5] Interest rate swap = strip of FRAs (forward rate agreements) with identical fixed rate across all periods. Relationship between swap rates and forward rates: product of consecutive short-term rates equals long-term rate of equivalent maturity. Swap rate derived as *weighted average* of forward rates, with weights being discount factors from futures rates. Example: 5Y swap rate calculated from five consecutive 1Y forward rates, each discounted by cumulative discount factors. This decomposition shows swap pricing is fundamentally no-arbitrage pricing of cash flows: if any period's forward rate diverges from the composite swap rate, traders can profit by decomposing the swap into FRAs and re-pricing.

## Related
- [[Interest_Rate_Swap_IRS]]
- [[Zero_Coupon_Yield_Curves]]
- [[Forward_Yield_Curves]]
- [[Risk_and_Valuation_Adjustments_xVA]]
- [[ISDA_Master_Agreement_And_CSA]]
- [[Overnight_Index_Swaps_OIS_Pricing_Dynamics]]
