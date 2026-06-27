---
title: Yield Curve Construction & Modeling Techniques
aliases: [Yield curve fitting, Cubic splines, Bond selection curve construction, Par curves, Zero curves]
type: mechanism
tags: [fixed-income, yield-curves, valuation, mechanics]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Yield curves constructed from bond sample with subjective criteria (on-the-run preference, exclusions for distortions). Cubic splines fit smooth curves through observations, ensuring continuous first/second derivatives. Different institutions use different methods → no universal curve.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 4025-4061
    section: "Chapter 5.2.5: Yield curve modeling"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **Bond Sample Selection Criteria:**
- Same credit rating (can't mix sovereign and corporate)
- Prefer "on-the-run" issues (recent, liquid, representative)
- Exclude: high-coupon bonds (pull-to-par effect), callable bonds (short option), near-maturity issues
- Subjective process → different analysts use different samples

**Curve Fitting Requirements:**
1. Continuous (no gaps)
2. Smooth (no sharp jumps in forward yields)
3. Passes through all selected observations

**Cubic Spline Method:** Fits cubic equations between successive bond pairs, ensuring:
- Same slope (first derivative) at joining points → continuous forward rates
- Same curvature (second derivative) at joining points → smooth curve progression
- Result: smooth linked curve preventing wild forward rate jumps

**Alternative Approach:** Some analysts prefer swap rates (objective, observable) as benchmark vs bond-based curves (subjective sample selection).

**Practical Implication:** No universal curve across institutions due to methodological differences. Bilateral transactions require negotiation of curve-based valuations.

## Related
- [[Yield_Curve_Structure_And_Mechanics]]
- [[Yield_Curve_Factor_Analysis_PCA]]
- [[Par_Yield_Curve]]
- [[Zero_Coupon_Yield_Curves]]
