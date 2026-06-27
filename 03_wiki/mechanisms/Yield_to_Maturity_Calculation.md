---
type: mechanism
title: Yield to Maturity Calculation
tags: [yields, pricing, discounting, fixed-income]
source: 
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=82]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=83]]"
status: active
created: 2026-04-28
---

# Yield to Maturity Calculation

## Definition

Yield to maturity (YTM) is the single discount rate that, when applied to all future cash flows of a bond, equates the present value of those flows to the bond's market price [extracted].

YTM is also known as a bond's **internal rate of return** [extracted].

## Core Price-Yield Formula

For a bond with semiannual compounding and 2T remaining coupon payments:

$$P = \frac{c}{2} \sum_{t=1}^{2T} \frac{1}{\left(1 + \frac{y}{2}\right)^t} + \frac{100}{\left(1 + \frac{y}{2}\right)^{2T}}$$

Where:
- P = bond price (per 100 face)
- c = annual coupon rate
- y = yield to maturity (annual)
- T = maturity in years
- t = period index

[extracted]

### Annuity Form

The formula can be rewritten using annuity notation:

$$P = \frac{c}{y}\left[1 - \frac{1}{\left(1 + \frac{y}{2}\right)^{2T}}\right] + \frac{100}{\left(1 + \frac{y}{2}\right)^{2T}}$$

[extracted]

## Worked Example

**Bond:** US Treasury 7.625s of 11/15/2022  
**Settlement:** Mid-May 2021  
**Price:** 111.3969 per 100 face  
**Remaining Coupons:** 3 (May 15, Nov 15, May 15)

[extracted]

**Semiannual coupon payment:** 3.8125 (7.625% / 2)

The YTM satisfies:

$$111.3969 = \frac{3.8125}{\left(1 + \frac{y}{2}\right)} + \frac{3.8125}{\left(1 + \frac{y}{2}\right)^2} + \frac{103.8125}{\left(1 + \frac{y}{2}\right)^3}$$

[extracted]

**Solution:** y = 0.0252% (2.52 basis points annually) [extracted]

## Three Price-Yield Relationships

From the price-yield formula, three critical insights emerge: [extracted]

1. **Par Relationship:** When c = 100y, then P = 100
   - Coupon rate equals yield → bond trades at par [extracted]

2. **Premium Bond:** When c > 100y, then P > 100
   - Coupon exceeds yield → bond sells at premium [extracted]

3. **Discount Bond:** When c < 100y, then P < 100
   - Coupon below yield → bond sells at discount [extracted]

## Convexity in Price-Yield Curve

The relationship between bond price and yield is **nonlinear** (convex):

- As yields fall, prices rise at an accelerating rate
- As yields rise, prices fall at a decelerating rate
- This asymmetry is quantified by **convexity** (covered in Chapter 4)

[extracted]

## Why YTM Can Be Misleading

YTM as a performance metric assumes: [extracted]

1. All coupon payments are reinvested at the YTM rate
2. Bond is held to maturity
3. No default occurs

**Reality:** Actual realized returns often differ because reinvestment rates fluctuate and bonds are frequently sold before maturity [extracted]

## Compounding Conventions

US Treasury bonds use **semiannual compounding**. Other markets use:
- Monthly (mortgages)
- Quarterly (some corporate bonds)
- Annual (some government bonds)
- Continuous (theoretical/mathematical)

The YTM calculation must match the bond's actual coupon frequency [extracted]

## Related Nodes

[[Realized_Return_Mechanism]]
[[Bond_Spread_Framework]]
[[Price_Yield_Relationship]]
