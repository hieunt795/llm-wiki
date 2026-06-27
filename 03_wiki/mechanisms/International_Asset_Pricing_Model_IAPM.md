---
title: International Asset Pricing Model (IAPM)
aliases:
- IAPM Formula
- Global Portfolio Optimization
- Exchange Rate Adjusted CAPM
type: mechanism
tags:
- finance
- exchange-rates
- portfolio-management
- math
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The International Asset Pricing Model (IAPM) extends the standard CAPM by
  incorporating exchange rate risk, where the expected return on a global asset is
  a function of the risk-free rate, its sensitivity to global market movements, and
  its sensitivity to changes in the exchange rate.
source_refs:
- file: Perry_Central_Bank_Policy_P6.md
  page: 390
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

The IAPM is the micro-foundation for **Push and Pull** determinants. It explains why international investors move capital: they are not just looking at the interest rate of a country, but at how that asset's risk-reward profile (including currency risk) diversifies their global portfolio.

## Mechanism: The Expected Return Formula

For a global portfolio, the expected return ($E(R_P)$) is formulated as:
$$E(R_P) = R_F + \beta_W R_W + \sum_{i=1}^{k} \delta_i S_i$$
Where:
- $R_F$: Return on the home risk-free asset (e.g., US T-Bills).
- $R_W$: Return on the global benchmark portfolio (World index).
- $\beta_W$: Sensitivity of the asset to global market movements.
- $S_i$: The magnitude of change (appreciation/depreciation) in the exchange rate of currency $i$.
- $\delta_i$: The sensitivity of the portfolio to currency $i$.

## Key Insight: Diversification and Home Bias
- **Diversification:** IAPM proves that adding EME assets (like SUN bonds or Indonesian stocks) reduces overall portfolio risk because their correlations ($\sigma_{ij}$) with advanced market assets are often low.
- **The Currency Factor:** Because investors prioritize the final return in their *own* currency, a high domestic yield can be completely wiped out by a small depreciation. This is why **Exchange Rate Stability** is a more important pull factor than the interest rate itself for "Real Money" investors.

## Evidence / Source Anchors

- Formula for expected return in a global portfolio: [[Perry_Central_Bank_Policy_P6.md#page=390]]
- Use of Markowitz efficient frontier in global diversification: [[Perry_Central_Bank_Policy_P6.md#page=390]]
- Distinction between 'Real Money' and 'Carry Trade' motives: [[Perry_Central_Bank_Policy_P6.md#page=391]]

## Related

- [[Push_and_Pull_Determinants_of_Capital_Flows]] — The macro drivers of the IAPM variables.
- [[Dornbusch_Overshooting_Model]] — Why $S_i$ is so volatile.
- [[Exchange_Rate_Determination_Theories]] — How the exchange rate part of IAPM is formed.
