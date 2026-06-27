---
title: Mathematical Conventions of Interest Accrual
aliases:
- Daycount Fractions (DCF)
- Simple vs Discount Margin Quotation
- Continuous vs Discrete Compounding
type: convention
tags:
- quantitative-finance
- market-infrastructure
- conventions
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch13.md"
thesis: The conversion of an annualized interest rate quote into actual physical cash
  requires the rigid application of pre-electronic computing conventions (Daycount
  Fractions) and the explicit mathematical choice between 'Simple Interest' division
  and 'Discount Margin' subtraction, fundamentally altering the terminal payout value
  of the asset.
source_refs:
- file: Fixed_Income_Alexander_During_Ch13.md
  page: 114
created: '2026-04-16'
updated: '2026-04-16'
---

## Thesis

Because interest rates are purely theoretical annualized concepts, they must be mathematically mutated through a Daycount Fraction (DCF) to compute the actual cash payout owed at the end of an interim accrual period. The modern money market operates using a fragmented patchwork of highly convoluted DCF algorithms (e.g., ACT/360, 30/360) designed originally to facilitate calculation on 1970s logarithm tables and analog slide rules. Furthermore, the translation of these rates into a physical security price diverges sharply between the computationally intensive 'Simple Interest' method and the archaic 'Discount Margin' method.

## Convention

To calculate the exact interest owed, the market multiplies the annualized rate by the Daycount Fraction: $\text{DCF} = \frac{\text{Days in interest period}}{\text{Days in year}}$. The algorithmic definitions of the numerator and denominator depend rigidly on the specific market:

1. **ACT/360 (Actual/360):** The dominant global money market standard (including Japan and the Eurozone). The numerator is the exact calendar duration; the denominator is permanently fixed at 360. *The Arbitration:* This mathematically results in the lender receiving *more* than the stated annualized rate over a calendar year (receiving $365/360 \times r$).
2. **ACT/365:** The standard utilized by legacy British Commonwealth markets (UK Gilts, Australia, South Africa).
3. **ISDA 30/360:** Designed for pre-computer simplicity. Both numerator and denominator map to an idealized 360-day year where every month has exactly 30 days. If a period begins on the 31st, it is forcefully rolled back to the 30th.
4. **ACT/ACT:** The strict, mathematically truthful model heavily utilized by bond and swap markets. The nominator is the exact duration, and the denominator observes whether the precise period falls under a true 365 or 366 (leap) year framework.

### Price Quotation Algorithms

Once a trader agrees to a rate $r$ and computes the DCF, they must convert this into a physical asset price $P$ (quoted as a percentage of Par 100). The market splits into two methodologies:

### 1. The Simple Interest Method
The mathematically rigorous, globally dominant standard for interbank deposits and most money market instruments. It relies on geometric division:
$$ P = \frac{100}{1 + (r \times \text{DCF})} $$

### 2. The Discount Margin Method (US T-Bills)
An archaic standard stubbornly retained by the most liquid money market on Earth: the US Treasury Bill market. Because performing complex divisions on 1970s slide rules was highly prone to error, the T-Bill market adopted a linear subtraction model that approximates the time value but sacrifices geometric rigor:
$$ P = 100 - (r \times \text{DCF}) $$
The inverse extraction is simple arithmetic: $r = (100 - P) / \text{DCF}$.

### Boundaries / Conditions

### The Mechanics of Compounding and the Weekend Anomaly
When interest is rolled over (added to the principal) rather than paid out, it compounds. The Annual Effective Rate ($\text{AER}$) of extreme frequency compounding (continuous) approaches the exponential limit: $r_{\text{eff}} = e^r - 1$.
However, the physical structure of the interbank market completely shatters theoretical continuous compounding because **interest cannot compound on non-business days (weekends)**.

Therefore, compounding a 14-day interbank loan using ACT/360 does not result in a clean 14-power exponent. Because the loan spans two weekends, the formula must split into 8 days of pure overnight compounding multiplying against two strict 3-day blocks of flat linear accrual across the weekends:
$$ i_c = N \left(1 + \frac{r}{360}\right)^8 \times \left(1 + \frac{3r}{360}\right)^2 $$

## Evidence / Source Anchors

- Definition of the core Daycount Fraction formula and the historic derivation of the 30/360 system for analog slide-rule calculations: [[Fixed_Income_Alexander_During_Ch13.md#page=114]]
- Contrasting the non-linear division of the "Simple Interest" formula matching global standard with the linear subtraction of the "Discount Margin" formula matching T-Bills: [[Fixed_Income_Alexander_During_Ch13.md#page=115]]
- The explicit mathematical proof showing how physical market closure (weekends) violently fractures continuous compounding mathematical models, requiring discrete linear blocks for weekend accruals: [[Fixed_Income_Alexander_During_Ch13.md#page=117]]

## Related

- [[Fixed_Income_Instrument_Definition]] — the underlying macro architecture driving these micro calculations
- [[Forward_Rate_Agreements_FRA_Mechanics]] — the derivatives explicitly leveraging these daycount fractions to settle net differences
- [[Credit_Ratings_And_Migration]]
- [[Liquidity_Measurement_Taxonomy]]
- [[Rolling_Vs_Fixed_Settlement]]
- [[Bond_Pricing_And_Accrued_Interest_Conventions]]
- [[OTC_Trading_Conventions]]
- [[Swap_Rate_Conversion_Conventions]]
