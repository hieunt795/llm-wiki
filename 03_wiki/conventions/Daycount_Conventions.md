---
title: Daycount Conventions
aliases:
- Day Count Fraction
- DCF
- Act/360
- 30/360
- Act/Act
- Quy ước đếm ngày
type: convention
tags:
- fixed-income
- valuation
- history
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch14.md
thesis: Daycount conventions are standardized rules for calculating the number of
  days in an interest period and a year, originally designed to simplify manual calculation
  but resulting in systematic discrepancies in effective interest rates.
source_refs:
- file: During_Fixed_Income_Ch14.md
  page: 114
- file: During_Fixed_Income_Ch14.md
  page: 115
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

To translate an annualized (quoted) interest rate into actual interest paid for a period, one must multiply the rate by the **Daycount Fraction (DCF)**:
$$DCF = \frac{\text{Days in interest period}}{\text{Days in year}}$$
Alexander Düring notes that many "strange" conventions today are artifacts of the 1970s, when logarithmic tables and slide rules were the state of the art. These conventions were driven by the desire to simplify manual division rather than mathematical logic. [[During_Fixed_Income_Ch14.md#page=114]]

## Common Conventions

### 1. Act/360 (Actual/360)
- **Rule:** Count actual days in the period, divide by 360.
- **The "Bankers' Advantage":** Because a year has 365 or 366 days, this convention results in an actual interest amount slightly larger than the quoted rate (roughly $365/360$ of the amount).
- **Usage:** Standard for most money markets, including the US, Eurozone, and Japan. [[During_Fixed_Income_Ch14.md#page=114-115]]

### 2. 30/360 (and variations like ISDA/30E)
- **Rule:** Assume every month has 30 days and every year has 360 days.
- **Rationale:** Simplifies manual calculation by eliminating the need to track varying month lengths or leap years.
- **Usage:** Common in bond and swap markets. [[During_Fixed_Income_Ch14.md#page=114]]

### 3. Act/365
- **Rule:** Count actual days, divide by a fixed 365.
- **Usage:** Primarily used in Commonwealth countries (UK, Australia, South Africa). [[During_Fixed_Income_Ch14.md#page=115]]

### 4. Act/Act (Actual/Actual)
- **Rule:** Actual days divided by the actual days in the relevant year (accounts for leap years).
- **Rationale:** The most "natural" and accurate method, but historically the most difficult for manual calculation. Now standard for modern computer-driven bond valuation. [[During_Fixed_Income_Ch14.md#page=114]]

## Strategic Conventions: Working Backwards

For instruments with maturities beyond one year that span a leap year, the market convention is to **work backwards from the maturity date**.
- **The Process:** Split the instrument into a final 1-year segment and an initial remainder segment.
- **Rationale:** This improves **fungibility** between instruments originated on different days but maturing on the same date. [[During_Fixed_Income_Ch14.md#page=115-116]]

## Evidence / Source Anchors

- Formula for the Daycount Fraction (DCF): [[During_Fixed_Income_Ch14.md#page=114]]
- Historical link between conventions and slide rules/log tables: [[During_Fixed_Income_Ch14.md#page=114]]
- Analysis of the Act/360 discrepancy ($365/360$ advantage): [[During_Fixed_Income_Ch14.md#page=114]]
- Description of the "Working Backwards" leap year convention: [[During_Fixed_Income_Ch14.md#page=115-116]]

## Related

- [[Discount_Factors_Theory]] — The underlying value that DCF seeks to represent as a rate.
- [[Compounding_Mechanics]] — How DCF interacts with multi-period interest.
- [[LIBOR_Transition_And_Benchmarks]] — Different benchmarks often utilize different daycounts (e.g., SONIA uses Act/365).
