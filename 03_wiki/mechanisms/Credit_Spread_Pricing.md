---
title: Credit Spread Pricing
aliases: [Credit spread, Corporate spread, Credit risk premium, Default probability]
type: mechanism
tags: [fixed-income, credit-risk, valuation]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Credit spread = excess yield over sovereign rate, compensating for default risk. Fair spread = expected loss / recovery rate = (probability of default × loss-given-default). Market conventions: 40% recovery (IG senior), 20% recovery (subordinated). CDS spreads back out implied default probabilities.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 1241-1256
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] Credit spread = corporate yield - sovereign yield. Fair value = (prob default × loss) / initial amount. Market convention: 40% recovery (IG, senior), 20% (subordinated). Estimation challenge: recovery unknown until default. CDS spreads used to back out implied default probability: rearrange formula with observed CDS spread to solve for prob(default). Higher CDS → higher implied default risk.

## Related
- [[Credit_Default_Swaps_Schofield]]
- [[Credit_Risk_Taxonomy]]
- [[Bond_Relative_Value_Valuation]]
