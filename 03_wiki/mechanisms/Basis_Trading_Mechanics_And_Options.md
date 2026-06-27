---
title: Basis Trading Mechanics & Embedded Options
aliases: [Bond futures basis trading, Gross basis, Net basis, Delivery option value, Basis trade implementation]
type: mechanism
tags: [fixed-income, futures, derivatives, options, relative-value]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Basis trading = relative value play comparing cash bond to futures-adjusted price. Gross basis = clean price - (futures price × conversion factor). Net basis reflects delivery option value. Short seller owns option to choose which bond to deliver; net basis is the premium for this optionality.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 2890-3011
    section: "Chapter 4.1.5-4.1.6: Trading the basis, Implementing basis trade"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **Basis Trading Definition:** Long basis = long cash CTD bond + short futures. Short basis = short cash bond + long futures. Relative value play (focuses on spread, not absolutes). 

**Gross Basis:** Clean bond price - (futures price × conversion factor). Positive when carry is positive (coupon > repo cost). 

**Drivers of Gross Basis Changes:**
1. Repo rate ↑ → basis ↓ (higher funding cost)
2. Bond yield ↓ → basis ↓ (higher bond price, more carry cost)
3. Curve flattens → basis ↓ (long yields fall + short rates rise)
4. CTD goes special → basis ↑ (lower special repo rate)
5. Time decay → basis ↓ (carry runs off at delivery)

**Embedded Delivery Option:** Short futures seller chooses which bond to deliver. This is exchange option (exchange current CTD for another deliverable bond). Interdependent options (delivery of one bond eliminates others). Modeled using option pricing principles with probability distribution overlays.

**Net Basis Interpretation:** Net basis = total gross basis value = carry effect + option value. Short seller receives option premium; long basis buyer pays for optionality.

**Option-Adjusted Fair Value:** Calculate theoretical net basis using option models; compare to actual basis.
- Actual > Theoretical → basis rich (buy basis; futures cheap)
- Actual < Theoretical → basis cheap (sell basis; futures rich)

**Basis as Call/Put:**
- Yields < notional → long basis ≈ long put
- Yields = notional → long basis ≈ long straddle  
- Yields > notional → long basis ≈ long call

**Implementation:** Hedge ratio ≠ simple notional division. Must account for DV01 mismatch between bond and futures to achieve market neutrality.

**Volatility Impact:** Higher market volatility → higher probability of CTD switch → higher delivery option value → higher net basis premium required.

## Related
- [[CTD_Changes_And_Yield_Beta]]
- [[Bond_Futures_Pricing_CTD]]
- [[Option_Greeks_Risk_Management]]
