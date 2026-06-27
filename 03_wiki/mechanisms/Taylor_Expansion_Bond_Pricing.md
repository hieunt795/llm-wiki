---
type: mechanism
title: Taylor Expansion of Bond Price-Yield Function
tags: [duration, convexity, approximation, pricing, derivatives]
source: 
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=103]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=105]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=108]]"
status: active
created: 2026-04-28
---

# Taylor Expansion of Bond Price-Yield Function

## Overview

Bond prices are a nonlinear function of yields. The Taylor expansion provides a polynomial approximation that decomposes price sensitivity into its component parts: duration (first-order sensitivity) and convexity (second-order curvature) [extracted].

This framework allows traders to quantify and manage interest rate risk with precision [extracted].

## Price-Yield Relationship (Nonlinear)

The exact bond price as a function of yield y is: [extracted]

$$P(y) = \sum_{t=1}^{2T} \frac{c}{2 \cdot (1 + y/2)^t} + \frac{100}{(1 + y/2)^{2T}}$$

This function is convex: as yields rise, prices fall, but at a decelerating rate. As yields fall, prices rise, but at an accelerating rate [extracted].

## Taylor Expansion (First Order: Duration)

A first-order Taylor expansion around the current yield y₀ is: [extracted]

$$P(y) \approx P(y_0) + \frac{dP}{dy}\bigg|_{y_0} \cdot (y - y_0)$$

The slope of the price-yield curve at y₀ is: [extracted]

$$\frac{dP}{dy} = -\frac{1}{10,000} \cdot DV01$$

where **DV01** (dollar value of an 01) is the change in price for a 1 basis point change in yield.

**Rearranged:**
$$\Delta P \approx -DV01 \times \Delta y$$

where Δy is measured in basis points.

[extracted]

### DV01 Relationship to Duration

$$DV01 = -\frac{1}{10,000} \left|\frac{dP}{dy}\right| = \frac{P \times D}{10,000}$$

where D is **modified duration** (in years).

[extracted]

### Worked Example: NSC Century Bond

**Bond:** Norfolk Southern Company 4.10s of 05/15/2121  
**Price:** 100.1801  
**Slope:** −2.406 (price-rate curve slope at current level)  
**Basis point change:** +1 bp (yield rises 1 basis point)

**Price change (duration approximation):**
$$\Delta P = -\frac{2.406}{10,000} \times 1 = -0.0002406$$

**Actual price at +1 bp:** 99.9390  
**Predicted price:** 100.1801 - 0.0002406 = 100.1799

[extracted]

The duration-only approximation is accurate to within 0.001, demonstrating first-order sensitivity works well for small yield moves [extracted].

## Taylor Expansion (Second Order: Convexity)

A second-order Taylor expansion adds the curvature term: [extracted]

$$P(y) \approx P(y_0) + \frac{dP}{dy}\bigg|_{y_0} \cdot (y - y_0) + \frac{1}{2}\frac{d^2P}{dy^2}\bigg|_{y_0} \cdot (y - y_0)^2$$

The second derivative (convexity) is: [extracted]

$$\frac{d^2P}{dy^2} = \frac{\text{Convexity}}{(1 + y/2)^2}$$

Rearranged in basis points: [extracted]

$$\Delta P \approx -DV01 \times \Delta y + \frac{1}{2} \times \text{Convexity} \times (\Delta y)^2$$

where convexity is normalized per 10,000 of principal.

[extracted]

### Convexity Benefit

The convexity term is **always positive** (for bonds with positive convexity):

- **When yields rise (+Δy):** Convexity offsets some of the price decline
- **When yields fall (-Δy):** Convexity amplifies the price gain

This is why **long bonds are asymmetrically attractive**: gains exceed losses for equal-sized yield moves [extracted].

### Second-Order Example: Larger Yield Move (+50 bp)

For the NSC bond with a 50 basis point yield increase:

**Duration effect:** -0.0002406 × 50 = -0.01203  
**Convexity effect:** 0.5 × (convexity) × (0.0050)²  
**Total price change:** ≈ -0.012 + convexity adjustment

[extracted]

## Local vs. Global Measures

**DV01 and duration** are **local measures**: they apply accurately only near the current yield level [extracted].

For large yield moves:
- Duration underestimates losses (prices are convex)
- Duration overestimates gains slightly

**Convexity corrects this:** The second-order term captures the curved nature of the price-yield relationship [extracted].

## Practical Application: Risk Management

Portfolio managers use Taylor expansion to decompose interest rate risk: [extracted]

**Dollar duration** = Sum of all bond DV01s  
→ Tells you portfolio price change for 1 bp yield shift

**Dollar convexity** = Sum of all bond convexities  
→ Tells you how duration itself changes as rates move

Example: A portfolio with +$15,000 duration and +$50,000 convexity:
- Yields rise 10 bp → Price falls ~$150, but convexity limits loss
- Yields fall 10 bp → Price rises ~$150, plus convexity gains

[extracted]

## Limitations of Expansion

The Taylor expansion has limitations: [extracted]

1. **Convergence:** Only accurate near the initial yield (y₀)
2. **Large moves:** For 100+ bp moves, higher-order terms become important
3. **Embedded options:** Bonds with calls/puts have negative convexity (kinked price curve)
4. **Curve shape changes:** Assumes parallel shifts; non-parallel moves cause basis risk

[extracted]

## Related Concepts

The Taylor expansion foundation enables:
- [[DV01_Duration_Framework]]
- [[Convexity_Measurement]]
- [[Interest_Rate_Risk_Hedging]]
- [[Option_Adjusted_Spread]]

[extracted]

## Related Nodes

[[Yield_to_Maturity_Calculation]]
[[Bond_Spread_Framework]]
[[DV01_Duration_Framework]]
- [[Bond_Price_Yield_Relationship]]
- [[Bond_Futures_Contract_Design]]
