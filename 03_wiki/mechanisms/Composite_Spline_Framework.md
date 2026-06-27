---
title: Composite Spline Framework
aliases:
- Spread Spline
- Composite Model
- Multi-issuer Curve Fitting
type: mechanism
tags:
- quantitative-finance
- yield-curves
- valuation
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch20.md
thesis: The composite spline framework is a sequential fitting methodology that prices
  sub-markets (agencies, sub-sovereigns) by layering a simple spread-based spline
  onto a robustly established base-market curve (sovereign), preventing over-fitting
  in low-liquidity sectors.
source_refs:
- file: During_Fixed_Income_Ch20.md
  page: 202
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Comparing related sub-markets (e.g., US Treasuries vs. US Agencies) using independent splines often leads to mathematical absurdities, such as an agency spline dipping below the sovereign spline due to a lack of data points. Alexander Düring explains that the **Composite Spline** solves this by enforcing a hierarchical dependency: the sub-market's discount factors are defined as a product of the base market's factors and a specialized "spread" factor. [[During_Fixed_Income_Ch20.md#page=202]]

## Mechanism: The Sequential Fit

The discount factor for the composite model is written as:
$$Df(t) = Df_B(t) \times Df_S(t)$$
- **$Df_B(t)$ (The Base):** Derived from a highly liquid base market (e.g., JGBs or Treasuries).
- **$Df_S(t)$ (The Spread):** Constructed to reflect only the yield spread component. [[During_Fixed_Income_Ch20.md#page=202]]

### 1. Simplification of Functional Form
A major advantage is that $Df_S(t)$ can be much simpler than the base curve. While the base might require a 6-parameter Nelson-Siegel-Svensson model, the spread can often be modeled as a simple polynomial:
$$Df_S(t) = \exp\left( -t \sum_{i=0}^k c_i t^i \right)$$
Using just 2 or 3 parameters $(k=2)$ is typically sufficient to capture issuer-specific dynamics without over-fitting to noisy bond prices. [[During_Fixed_Income_Ch20.md#page=202]]

### 2. The Two-Step Calibration
1.  **Step 1:** Fit the base market curve using standard procedures.
2.  **Step 2:** Fix the base parameters and fit only the spread parameters $(c_i)$ using the sub-market bond prices. [[During_Fixed_Income_Ch20.md#page=202]]

## Strategic Application: Sub-sovereign Markets

Düring demonstrates this framework using Japanese sub-sovereigns (Tokyo Metropolis and Chubu Electric).
- **The Result:** Despite having few bonds outstanding, the spread splines accurately reflect the issuer yield curves because the primary interest rate movements are already "pre-captured" in the underlying JGB spline. [[During_Fixed_Income_Ch20.md#page=202]]

## Evidence / Source Anchors

- Definition of the composite discount factor identity: [[During_Fixed_Income_Ch20.md#page=202]]
- Functional form of the polynomial spread spline ($Df_S$): [[During_Fixed_Income_Ch20.md#page=202]]
- Description of the sequential process for curve calibration: [[During_Fixed_Income_Ch20.md#page=202]]
- Case study of Tokyo Metropolis and Chubu Electric (Figure 19.7): [[During_Fixed_Income_Ch20.md#page=202-203]]

## Related

- [[Nelson_Siegel_Spline_Models]] — Often used for the base curve $Df_B$.
- [[Yield_Curve_Fitting_Optimization]] — The mathematical engine for Step 2.
- [[Yield_Curve_Spline_Dispersion]] — How to measure the fit quality of the composite model.
- [[Agency_Vs_Sovereign_Basis]] — The economic spread being modeled here.
