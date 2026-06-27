---
title: Macaulay and Modified Duration
type: mechanism
status: reviewed
confidence: 5
expert_lens: ["Bruce Tuckman", "Angel Serrat"]
provenance: ["RAW-BOOK: Tuckman & Serrat (2022) Ch 4"]
half_life_years: 10
tags: ["fixed-income", "risk-management", "yield-math"]
---

## Thesis
Duration serves as the primary linear measure of interest rate risk, representing both the weighted average time to receipt of cash flows (Macaulay) and the price sensitivity of a bond to interest rate shifts (Modified). It effectively translates a stream of future cash flows into a single-maturity equivalent.

## Mechanism

### 1. Macaulay Duration ($D_{mac}$)
Defined as the weighted average of the times at which cash flows are received, where each weight is the proportion of the bond's total present value contributed by that specific cash flow.
- **Formula**: $D_{mac} = \sum_{t=1}^{n} \left[ t \times \frac{PV(CF_t)}{P} \right]$
- **Intuition**: For a zero-coupon bond, $D_{mac}$ equals its maturity ($T$). For coupon bonds, $D_{mac} < T$ because coupons pay out value before maturity.

### 2. Modified Duration ($D_{mod}$)
Measures the percentage change in price for a unit change in yield. It is the derivative of price with respect to yield, normalized by price.
- **Formula**: $D_{mod} = -\frac{1}{P} \frac{dP}{dy}$
- **Relationship**: $D_{mod} = \frac{D_{mac}}{1 + y/k}$ (where $k$ is the compounding frequency, e.g., 2 for semi-annual).

### 3. Drivers of Duration (Regime Lock)
- **Coupon Effect**: Higher coupon rates → Lower duration. Higher coupons pay more value earlier, shortening the "weighted average life."
- **Yield Effect**: Higher yields → Lower duration. Higher discount rates reduce the present value of distant cash flows more than near-term ones, shifting the value weight toward the present.
- **Term Effect**: Longer maturity → Higher duration. Sensitivity increases with term, though at a decreasing rate (non-linear).

### 4. Portfolio Duration
The duration of a portfolio is the value-weighted sum of the durations of its component holdings.
- **Formula**: $D_p = \sum w_i D_i$, where $w_i = \frac{Market Value_i}{Total Portfolio Value}$

## Worked Example
A 5-year Treasury bond with a 1.625% coupon trading at a yield of 0.82277%:
- **Macaulay Duration**: 4.8267 years.
- **Modified Duration**: $4.8267 / (1 + 0.0082277/2) = 4.8069$.
- **Interpretation**: A 100bps (1%) increase in yield will result in an approximate 4.8069% decrease in the bond's price.

## Failure Conditions
- **Non-Parallel Shifts**: Duration assumes a parallel shift in the yield curve. If the curve twists (steepens/flattens), a single duration measure fails to capture the risk.
- **Large Rate Changes**: Duration is a first-order (linear) approximation. For large moves, the curvature (convexity) makes the duration-only estimate inaccurate.
- **Embedded Options**: Duration (specifically Modified) fails for bonds with options (callable/putable) because cash flows change with rates. In these cases, **Effective Duration** (numerical re-pricing) is required.

## Related
- [[Convexity_Mechanics]] (Second-order correction)
- [[DV01_Risk_Management]] (Dollar-based sensitivity)
- [[Key_Rate_Duration]] (Non-parallel shift management)
- [[Bond_Price_Yield_Relationship]]
