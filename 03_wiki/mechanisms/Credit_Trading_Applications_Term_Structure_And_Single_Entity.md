---
title: Credit Trading Applications (Term Structure, Single Entity, Basket Strategies)
aliases: [Credit curve trading, CDS steepening, CDS flattening, CDS butterfly, Credit-linked notes, CLN, Total return swaps, Basket CDS]
type: mechanism
tags: [credit-derivatives, credit-risk, trading-strategies, CDS, credit-curves]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: Credit term structure strategies (steepening/flattening/butterfly) apply fixed income curve trading mechanics to CDS curves. Single-entity views expressed via credit-linked notes, reverse repos, or protection buying. Basket strategies (total return swaps, basket CDSs, index tranches) aggregate single-name exposures.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 5934-6040
    section: "Chapter 7.2: Credit Term Structure Trading (Steepening/Flattening/Butterfly/Convexity)"
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 6041-6139
    section: "Chapter 7.3: Single Reference Entity Trading (Credit-Linked Notes)"
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 6139-6280
    section: "Chapter 7.4: Basket of Reference Entities (TRS, Basket CDS, Index Tranches)"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

### 7.2: Credit Term Structure Strategies

[RAW-BOOK:5] **Steepening/Flattening Trades:** Structure duration-neutral using DV01 ratios (same mechanics as fixed income curve trades). Steepener = buy long-dated protection, sell short-dated. Include carry (unequal notionals → coupon imbalance), pull-to-par (amortization of upfront payments toward zero), and roll (spread curve dynamics). Default risk calculated as notional sum × (100% - recovery) + upfront payments.

**CDS Butterfly (3-5-7 example):** Buy 3Y + 7Y protection, sell 5Y protection ("belly"). Neutral to parallel shifts and curve rotations. Profit/loss = notional × DV01 × butterfly spread change. Time decay components: (1) pull-to-par, (2) carry (coupon), (3) roll (curve shape).

**Convexity in Credit:** 
- Long protection = negative convexity (profits decelerate on spread widening)
- Short protection = positive convexity (losses decelerate)
- Flattening trade = positive convexity (profits exceed losses)
- Steepening trade = negative convexity (losses exceed profits)

---

### 7.3: Single Reference Entity Trading

[RAW-BOOK:5] **Credit-Linked Notes (CLN):** Synthetic funded security structured as floating-rate note. Investor pays par → issuer deposits funds at LIBOR → issuer sells CDS protection → pays enhanced yield to investor (LIBOR + CDS premium). Buyer gets enhanced return; issuer gets CDS premium income offset by funding cost.

**Investor Motivations:** Enhanced yield, credit exposure without outright bond holding, protection seller premium capture

---

### 7.4: Basket Strategies

[RAW-BOOK:5] **Total Return Swaps (TRS):** Synthetic structure for credit exposure. Swap agreement where one party receives total return of underlying bond/loan (coupons + price appreciation), pays fixed or floating rate + spread. Allows credit exposure without physical bond ownership, captures carry and roll-down.

**Basket CDS:** Protection on portfolio of names. Triggers on any single default in basket. More liquid than single-name CDS for correlated portfolios.

**Index Tranches:** Structured products on CDS indices (iTraxx, CDX) with capital structure (equity, mezzanine, senior). Senior tranches receive losses only after junior tranches absorbed them. Provide leveraged/subordinated credit exposure.

## Related
- [[CDS_Basis_And_Credit_RV_Triangle]]
- [[Steepener_And_Flattener_Trades]]
- [[Butterfly_Trade_Mechanics]]
- [[Credit_Default_Swap_CDS]]
- [[Interest_Rate_Swap_IRS]]
- [[Credit_Default_Swaps_CDS]]
- [[Credit_Default_Swaps_Schofield]]
- [[Credit_Ratings_And_Migration]]
- [[Credit_Risk_Transfer_CRT]]
