---
title: Yield Curve Factor Analysis & Principal Component Analysis
aliases: [PCA yield curves, Yield curve factors, Eigenvalues bond yields, Yield betas, Curve movements]
type: mechanism
tags: [fixed-income, yield-curves, quantitative, risk-management]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Principal Component Analysis (PCA) decomposes yield curve movements into independent factors without assuming cause/effect. Three factors explain ~95% of daily curve variability: (1) parallel shifts, (2) steepening/flattening, (3) curvature changes. Eigenvalues interpreted as yield betas for each maturity.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 3919-4024
    section: "Chapter 5.2.4: How do yield curves actually move?"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **Principal Component Analysis:** Reveals structure of variable relationships without identifying dependent/independent. Reduces complex multivariate data into key components. Unlike regression, makes no assumptions about causality.

**Three Independent Factors:**
1. **Factor 1 (Parallel Shift):** ~75% of variance. Eigenvalues stable across maturities 2-30y, smaller at short end. Interpretation: tendency of entire curve to shift up/down uniformly.
2. **Factor 2 (Steepening/Flattening):** ~16% of variance. Positive values at short maturities, negative at long. Rotation point ~3-year maturity. Interpretation: curve slope changes with 3-year as pivot.
3. **Factor 3 (Curvature):** ~4% of variance. Peaks at 6-month, turns negative at 7-year. Interpretation: tendency for concave (rally) or convex (selloff) profile.
- First 3 factors = ~95% total variance

**Eigenvalues as Yield Betas:** Market convention treats factor values as yield betas. Example: 10-year eigenvalue 0.347 on factor 1 → 1 bp parallel shift causes 10-year yield to change 0.347 bp.

**Empirical Curve Behavior:** 
- **Bull market (rally, falling yields):** Curves steepen, become more concave (short end steep, long end flat)
- **Bear market (selloff, rising yields):** Curves flatten, become more convex (short-long compressed)
- Short-dated yields show greater volatility than long-dated

## Related
- [[Yield_Curve_Structure_And_Mechanics]]
- [[Yield_Curve_Construction_Modeling]]
- [[Forward_Yield_Curves]]
