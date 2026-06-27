---
title: "Fixed Income - Alexander During-22"
type: raw_source
source_pdf: "Fixed Income - Alexander During-22.pdf"
extractor: docling
---

## CHAPTER 21

## Carry and Roll-Down

A traditional way to assess the relative attractiveness of different curve sectors is the use of the forward curve. Figure 21.1 shows for introduction the par, zero and overnight rates of the German curve in August 2014. At the time, the ECB deposit facility rate acted as the effective policy rate and was set at -0.1 % but purchases of German government bonds under PSPP had not yet started. The curves show a standard behaviour for upwardly sloped curves, namely the zero (spot) curve is above the par curve, and the overnight forwards are above the swap curve. The only exception is the very front end of the curve where this relationship is inverted because the curve was sloping downward in this sector 1 .

Before discussing the implications of this relationship in more detail, it is worthwhile discussing why this relationship is as it is. The zero rate is the constant term interest rate that, when compounded at the appropriate frequency, delivers the same discount factor as compounding the time-varying overnight interest rate over the same time horizon. An upward curve slope means that interest rates are rising for longer and longer horizons. Conceptually, the zero rate is an average of overnight rates, bar compounding and daycount differences. If nearer-dated overnight rates are below this average, then further overnight rates must be above it in order to catch up. Therefore, the overnight forward curve must have a larger slope than the zero rate curve. Put differently, because the zero curve measures the average overnight discount rate over a given period, it must be below the last value of that rate if the values are in ascending order. In the same way, the par curve can be thought of as the average coupon on a package of zero-coupon instruments. The average rate must be below the zero rate applicable to the maturity point when the intervening zero coupon instruments have lower yields.

According to [49, 50], the forward curve can be seen as an indicator of the most attractive curve points. This curve shows the incremental return of leaving one's money invested for an extra day. If the current curve shape is the best predictor of future curve shapes (for which there is some evidence), the forward rate is also a measure of return for holding a bond until the next day.

1 One reason for this slope was the then expected cut in the deposit facility rate which occurred on 10 September 2014.

FIGURE 21.1 Par, spot and overnight forward curves on a Nelson-Siegel-Svensson German government bond spline in August 2014, before the start of PSPP. Prices from Bundesbank. Note that the overnight rates are quoted in actual/360, the other rates are actual/actual.

<!-- image -->

Instead of this formalism, a different analytical approach is now more common.

<!-- image -->

For each bond, if a curve is to hand, the expectation should be that, after a given holding horizon, the yield of that bond should have changed in line with the curve shape, i.e., declined in a normal yield curve environment. At the same time, the carry of each bond should be positive as (short-term) funding costs are lower than (long-term) coupon income. So, the forward price over the same period should be lower, and the forward yield therefore higher than the current yield. The holding-period return is therefore composed of two components, namely the difference between spot and forward price (the carry), and an expected decline in yield (the roll-down). One can see these two components as the funding-adjusted coupon income, and the expected capital gain, respectively.

As a concept this holding period return has the drawback of being a mix of price and yield concepts. Roll-down in particular has a cash value that depends on the forward DV01 of the bond. This implies that while a bond will eventually roll down to the overnight rate, no overall capital gain is associated with this process because the DV01 of the bond will at that point have fallen to zero.

Computationally, one works out the forward yield from the forward price, and the expected yield from the spot yield, and the change in fair value yield on the curve for the spot and forward date. Using the change in fair value yield together with the spot yield accounts for the fact that the spot yield may not be exactly on the curve. The result of this analysis is a yield difference called the buffer. The buffer, the difference between forward yield and expected yield on the curve, can be interpreted as the amount by which the current yield curve needs to shift up by the end of the holding period to eliminate the carry income of the bond.

FIGURE 21.2 Carry and roll-down of German government bonds in August 2014. Note that due to coupon effects, bond yields to not coincide with par yields at all maturities. Prices from Bundesbank.

<!-- image -->

The result of the analysis is a projected holding period return for each individual bond, expressed as a break-even yield shift. This return calculation takes into account all information about this security, including its specific repo rate, pull-to-par and pricing relative to other bonds, making this calculation superior to an analysis of the forward rate alone. Figure 21.2 shows the result of this calculation for the German market on a given day. Some features of the result are noteworthy. First, it is possible to have positive holding period returns even when yields are negative. A positive roll-down can offset negative carry. Second, the buffer first increases with maturity but then declines even as yields increase. Two effects play a role in this observation. On one hand, the curve becomes flatter towards longer maturities and roll-down therefore diminishes. Onthe other hand, the buffer is expressed in yield terms and the impact of higher carry is dominated by the division by an increasing DV01. Interestingly, the expected return is highest in the 4- to 9-year area, i.e., the bullet of the curve. This echoes some of the arguments made on convexity bias earlier (cf. Figure 20.4 on page 210).

One caveat should be mentioned for this type of analysis and that is the impact of the curve model used. The curve model in [49, 50] was a market model where forwards were obtained by bootstrapping. Such a model is in principle completely flexible but may sometimes be affected by idiosyncratic valuation effects of individual securities. Here, a Nelson-Siegel-Svensson spline provides the roll-down curve and the functional shape of the roll-down is constrained by the flexibility of that spline. Because the spline has only two 'humps', it is not possible to have a multitude of turning points in the roll-down curve. The apparent richer structure of the individual roll-down estimates in Figure 21.2 is the result of security-specific pricing effects.