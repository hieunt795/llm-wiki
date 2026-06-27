---
title: CDS Basis and Credit Relative Value Triangle
aliases: [CDS basis trading, Bond-CDS relationship, Single-name CDS basis, CDS spread divergence, Long basis, Short basis]
type: mechanism
tags: [credit-derivatives, credit-risk, relative-value, CDS, trading-strategies]
status: draft
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Schofield
provenance: Schofield_Trading_Fixed_Income_2011.md
thesis: CDS basis = CDS spread minus Z-spread (or ASW). Despite both measuring credit risk, the two markets diverge due to participant types, liquidity differences, structural asymmetries (delivery options, restructuring triggers, financing costs), and correlation effects. Basis trading exploits these divergences.
source_refs:
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 5649-5768
    section: "Chapter 7.1.1: Bond-CDS Relationship and CDS Basis"
created: '2026-05-07'
updated: '2026-05-07'
---

## Summary

[RAW-BOOK:5] **CDS Basis Definition:** CDS spread minus Z-spread (or equivalently, CDS spread minus ASW spread). Two measures of credit risk for same issuer should theoretically be equal, but empirically diverge significantly.

**Why Basis Exists:**

*CDS > Z-spread (Positive Basis):*
- Delivery option value: CDS buyers can choose which bond to deliver from eligible basket (like CTD in futures)
- Restructuring triggers: CDS may be triggered by restructuring event that doesn't default bond
- Liquidity concentration: CDS most liquid at 3/5/7/10Y; off-the-run maturities have wider spreads
- Shorting friction: Harder to short corporate bonds; CDS provides easier short expression

*CDS < Z-spread (Negative Basis):*
- Financing costs: Banks finance bond purchases at spread to LIBOR, reducing net return vs CDS
- Counterparty risk correlation: CDS seller default correlation with reference entity reduces protection value
- Structured product demand: Issuance of structured products referencing CDS drives protection seller supply down
- Maturity liquidity: Some CDS maturities more liquid than bond maturities
- Basis trader residual risk: After credit event, asset swap leaves interest rate swap position needing unwind

**Basis Trading:**
- **Long Basis:** Buy bond (or receive LIBOR + spread in ASW) + buy default protection. Profits if basis compresses.
- **Short Basis:** Short bond (or pay LIBOR + spread in ASW) + sell default protection. Profits if basis widens.
- **Market Participants:** Investment banks, hedge funds react faster to credit changes; pension funds/insurers slower → basis opportunities

## CDS Indices

[RAW-BOOK:5] **Portfolio-level Credit Derivatives:** CDS indices reference portfolio of names (e.g., iTraxx Main = 125 investment-grade names, equally weighted). Different maturities (3/5/7/10Y) each have separate quoted spreads forming credit term structure.

**Roll Mechanics:**
- Index constituents fixed every 6 months (March 20, September 20) → "roll dates"
- New series created each roll date (Series 1, 2, 3...) → "on-the-run" (most recent) vs "off-the-run" (older)
- Participants typically roll exposures: terminate old series contract, enter new series
- Roll trade quoted as: "Buy roll" (net cost to go long new series) vs "Sell roll" (net cost to go short new series)

## Related
- [[Relative_Value_Framework]]
- [[Relative_Value_Triangle]]
- [[Credit_Spread_Pricing]]
- [[Credit_Default_Swap_CDS]]
- [[Interest_Rate_Swap_IRS]]
