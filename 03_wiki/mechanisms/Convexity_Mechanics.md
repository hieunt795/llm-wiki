---
title: Convexity Mechanics
type: mechanism
status: reviewed
confidence: 5
expert_lens: ["Bruce Tuckman", "Angel Serrat"]
provenance: ["RAW-BOOK: Tuckman & Serrat (2022) Ch 4"]
half_life_years: 10
tags: ["fixed-income", "risk-management", "yield-math"]
---

## Thesis
Convexity is the second-order measure of interest rate sensitivity, quantifying the "curvature" of the price-rate relationship. It explains why duration estimates become less accurate for large rate moves and why some portfolios (barbells) outperform others (bullets) in volatile regimes.

## Mechanism

### 1. Mathematical Definition
Convexity ($C$) is the second derivative of the price-rate function divided by price.
- **Formula**: $C = \frac{1}{P} \frac{d^2P}{dy^2}$
- **Price Approximation**: $\frac{\Delta P}{P} \approx -D \Delta y + \frac{1}{2} C (\Delta y)^2$
- **Positive Convexity**: For standard coupon bonds, price-rate curves are "bowed" upward. This means DV01 falls as rates rise (lower sensitivity to losses) and DV01 rises as rates fall (higher sensitivity to gains).

### 2. Causal Chain
Rate Change $\rightarrow$ [Convexity] $\rightarrow$ Duration Adjustment $\rightarrow$ Non-linear Price Impact
- As rates $\downarrow$: $D$ $\uparrow$ $\rightarrow$ Price increases faster than a linear model predicts.
- As rates $\uparrow$: $D$ $\downarrow$ $\rightarrow$ Price decreases slower than a linear model predicts.

### 3. Structural Drivers
- **Maturity**: Convexity increases quadratically with term. A 30-year bond has significantly more convexity than a 10-year bond, far exceeding the linear increase in duration.
- **Coupon**: Lower coupons $\rightarrow$ Higher convexity (at a given maturity and yield). Zero-coupon bonds have the highest convexity for a given maturity.
- **Dispersion of Cash Flows**: For the same duration, a **Barbell** portfolio (short and long bonds) has higher convexity than a **Bullet** portfolio (intermediate bonds) because cash flows are more dispersed from the mean.

### 4. Convexity as Volatility Option
Long convexity is equivalent to being "long volatility."
- **The Payoff**: A long convexity position profits from large moves in either direction.
- **The Cost**: "Theta" or yield sacrifice. Markets price in convexity; therefore, more convex bonds usually offer lower yields than less convex ones with the same duration.

## Worked Example
An NSC century bond (100-year) with $D=24.1$ and $C=1,101$:
- For a -100bps shift:
  - Duration-only estimate: $+24.1\%$
  - Convexity correction: $0.5 \times 1,101 \times (0.01)^2 = +5.5\%$
  - Total estimated change: $24.1\% + 5.5\% = 29.6\%$ (Actual re-pricing: $30.98\%$).

## Failure Conditions
- **Negative Convexity**: Found in callable bonds and Mortgages (MBS). As rates fall, the issuer's option to refinance "caps" the price gains, and the duration shortens (contraction risk), causing the price-rate curve to bend downward.
- **Yield-Based Assumption**: Standard convexity assumes parallel yield shifts. In real markets, term structure twists can negate the expected "convexity gain."

## Related
- [[Macaulay_and_Modified_Duration]]
- [[DV01_Risk_Management]]
- [[Barbell_vs_Bullet_Strategies]]
- [[Negative_Convexity_MBS]]
