---
type: mechanism
title: Bond Spread Framework
tags: [spreads, yields, credit-risk, relative-value]
source:
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=89]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=90]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=91]]"
status: active
created: 2026-04-28
---

# Bond Spread Framework

## Definition & Purpose

A bond spread is the yield difference between two fixed income securities, typically expressing the price of an instrument relative to a benchmark [extracted].

Spreads serve to:
1. Quote yield differences vs. a reference instrument
2. Assess relative value across securities
3. Price credit risk, liquidity, and supply-demand imbalances
4. Facilitate fast-moving markets with standardized metrics

[extracted]

## Yield Spread (Simple Difference)

The most basic spread is the simple yield difference:

**Yield Spread = YTM(Bond) - YTM(Benchmark)**

**Example:** European Sovereigns (May 2021) [extracted]

- Italian government bond (Buoni del Tesoro Poliennali, 0.6s of 08/01/2031): 1.06% yield
- German government bond (Bunds, 0.0s of 02/15/2031): -0.132% yield
- **BTP-Bund Spread = 120 basis points** [extracted]

**Limitation:** Yield spreads conflate maturity and coupon effects; comparing bonds with different characteristics is misleading [extracted]

## Bond Spread (Price-Relative Formula)

A more rigorous approach uses discount factors (forward rates) to isolate the spread: [extracted]

$$\text{Bond Price} = \frac{3.8125}{\left(1 + \frac{0.0154\% + s}{2}\right)} + \frac{3.8125}{\left(1 + \frac{0.0154\% + s}{2}\right)\left(1 + \frac{0.1008\% + s}{2}\right)} + \frac{103.8125}{\left(1 + \frac{0.0154\% + s}{2}\right)\left(1 + \frac{0.1008\% + s}{2}\right)\left(1 + \frac{0.1833\% + s}{2}\right)}$$

Where s is the constant spread added to all forward rates [extracted]

### Worked Example

**Bond:** US Treasury 7.625s of 11/15/2022
**Forward rates:** 0.0154%, 0.1008%, 0.1833% for three periods
**Market price:** 111.2797
**Benchmark price:** 111.3969

Solving for s: **s = -0.0727% (approximately -7.27 basis points)** [extracted]

**Interpretation:** The bond is rich (negative spread) relative to the benchmark curve; its market price exceeds the present value computed from forward rates [extracted]

## Spread Interpretation

A bond's spread reflects its extra return relative to the benchmark, conditional on:
- **Rates stay the same** (or interest rate risk is hedged away)
- **No default occurs**
- **Benchmark curve remains fixed**

[extracted]

**Negative spread** → Bond is expensive; yields are lower than justified by forward rates [extracted]

**Positive spread** → Bond is cheap; yields are higher than justified by forward rates [extracted]

## High-Coupon Bond Spreads (Relative Value Application)

Spreads are particularly useful for trading high-coupon bonds against benchmarks:

**Scenario:** Selected US Treasury bonds vs. benchmark 7.625s of 11/15/2022

| Maturity | Coupon | Spread to Benchmark | Spread to SOFR Swaps |
|----------|--------|---------------------|----------------------|
| 11/15/2021 | 2.875% | 0.0 bp | -1.9 bp |
| 11/15/2022 | 1.625% | 0.0 bp | 3.1 bp |
| 11/15/2024 | 2.250% | 0.0 bp | 5.9 bp |
| 11/15/2026 | 2.000% | 0.0 bp | 16.0 bp |
| 11/15/2028 | 3.125% | 0.0 bp | 26.4 bp |

[extracted]

**Key findings:** [extracted]
- Rich bonds (high coupon, low spread) offer less value relative to benchmarks
- SOFR swap spreads diverge from Treasury spreads as maturity lengthens
- Long-term bonds show steeper spread curves, indicating market expectations

[extracted]

## Forward Curve & Spread Trading

When comparing spreads across markets, the underlying forward curve shape matters: [extracted]

- **Upward sloping SOFR curve:** Longer bonds require larger spreads to compensate
- **Inverted Treasury curve:** Shorter bonds may trade at tighter spreads
- **Asset swaps:** Trades that lock in relative spreads between bonds and LIBOR/SOFR swaps

[extracted]

## Limitations of Spreads

1. **Liquidity effects:** Illiquid bonds trade at wider spreads, obscuring true credit risk
2. **Maturity mismatch:** Comparing bonds with different maturities via simple yield spreads is problematic
3. **Coupon effects:** High-coupon bonds appear rich even if fairly valued on a duration basis
4. **Option-adjusted spreads:** For bonds with embedded options, simple spreads are insufficient

[extracted]

## Related Nodes

[[Yield_to_Maturity_Calculation]]
[[P&L_Attribution_Components]]
[[Bond_Futures_Pricing_CTD]]
[[Option_Adjusted_Spread]]
