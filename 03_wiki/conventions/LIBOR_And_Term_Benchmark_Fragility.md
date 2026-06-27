---
title: LIBOR Transition and Benchmarks
aliases:
- LIBOR
- EURIBOR
- TIBOR
- SOFR
- €STR
- SONIA
- TONAR
- Benchmark Reform
- Ibor
type: convention
tags:
- monetary-policy
- central-banking
- derivatives
- fraud
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch14.md
thesis: The global transition from LIBOR to overnight benchmarks represents a fundamental
  shift from opinion-based term rates to transaction-based compounded rates, necessitated
  by the collapse of the unsecured interbank term lending market.
source_refs:
- file: During_Fixed_Income_Ch14.md
  page: 117
- file: During_Fixed_Income_Ch14.md
  page: 118
- file: During_Fixed_Income_Ch14.md
  page: 119
- file: During_Fixed_Income_Ch14.md
  page: 120
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

For decades, the London Interbank Offered Rate (**LIBOR**) was the world's most successful interest rate benchmark. However, its reliance on "expert judgment" rather than actual trades made it vulnerable to manipulation and disconnected from market reality. Alexander Düring explains that the reform process is not just about fraud prevention, but about adapting to a market where excess liquidity has eliminated the need for unsecured term lending between banks. [[During_Fixed_Income_Ch14.md#page=117-119]]

## 1. The Era of Ibors (LIBOR, Euribor, TIBOR)

Genericly known as "Ibors," these rates were calculated as the **trimmed mean** of quotes provided by a panel of banks.

- **Mechanism:** Banks were asked at what rate they *expected* to be able to borrow unsecured.
- **The Weakness:** Unsecured term lending became increasingly rare after 2008. Traders were providing opinions on a market that barely existed.
- **The Scandal:** Traders colluded to shift fixings for the benefit of their derivatives positions. While the bias wasn't consistently up or down, it willfully misled the market on prevailing conditions. [[During_Fixed_Income_Ch14.md#page=118]]

## 2. The New Paradigm: Overnight Benchmarks

The reform has shifted the focus to high-volume, transaction-based overnight rates:

- **SOFR (US):** Secured Overnight Funding Rate, based on the massive US repo market.
- **€STR (Eurozone):** Euro Short-Term Rate, replacing Eonia and covering transactions where at least one participant is not a bank.
- **SONIA (UK), TONAR (Japan):** Similar overnight unsecured averages. [[During_Fixed_Income_Ch14.md#page=119]]

## 3. The Bridging Problem: Term Rates vs. Overnight Rates

The transition creates a structural gap for non-financial users (like mortgage borrowers) who need certainty about their interest payments *before* they are due.

### The "Lagged Compounded" Approach
To create a "term" rate from overnight observations, markets use lagged compounded rates:
- **The Mechanism:** Observe the compounded overnight rate over a period $p$ (e.g., 3 months) but lagged by a period $l$ (e.g., 5 days).
- **The Drawback:** For a central bank, this means policy rate changes affect borrowing costs only with a delay of roughly $p/2 + l$.
- **The Term Premium Paradox:** Averaging overnight rates does not induce a **Term Risk Premium**. There is no conceptual link between the length of the averaging period and the premium an investor would demand for a fixed-rate commitment over that same term. [[During_Fixed_Income_Ch14.md#page=121]]

## Evidence / Source Anchors

- Definition of LIBOR as a trimmed mean of panel bank expectations: [[During_Fixed_Income_Ch14.md#page=117]]
- Analysis of the structural decline in unsecured interbank term lending: [[During_Fixed_Income_Ch14.md#page=118]]
- Identification of new benchmarks (SOFR, €STR, TONAR): [[During_Fixed_Income_Ch14.md#page=119]]
- Discussion on the "Lagged Compounded" approach and the lack of term premium: [[During_Fixed_Income_Ch14.md#page=121]]
- Rationale for vigiliance in cash-settled benchmark setting: [[During_Fixed_Income_Ch14.md#page=119]]

## Related

- [[Overnight_Index_Swap_OIS]] — The bridge between overnight and term rates.
- [[Compounding_Mechanics]] — The mathematical engine of the new benchmarks.
- [[Floating_Rate_Notes_FRN]] — The primary instruments affected by the transition.
- [[Monetary_Policy_Transmission_Mechanism]] — How benchmark delay affects central bank efficacy.
