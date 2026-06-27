---
title: "Fixed Income - Alexander During-33"
type: raw_source
source_pdf: "Fixed Income - Alexander During-33.pdf"
extractor: docling
---

## CHAPTER 32 Bond Trading

B onds tend to be traded to express views on yield developments. In this respect, trading bonds is not different from trading swaps or interest rate derivatives. How to analyse and implement such strategies has been discussed in the previous chapter. This chapter will instead focus on trading ideas that are not expressible in these ways.

That being said, some of the concepts presented here also affect some curve trading strategies. When putting on a 2Y-10Y curve steepener through bonds, it may be useful to sell an expensive 10Y and buy a cheap 2Y. In this respect, a curve trade is overlayed with 2 bond relative value trades. The focus of this chapter is on such relative value ideas.

## 32.1 BOND RELATIVE VALUE

The start to trading individual securities is valuation. Yields alone are insufficient for this purpose because the yield concept suffers from a number of drawbacks that were discussed in the relevant Chapter 16.7. Instead, curve spreads of various kinds are used to identify the relative valuation of bonds.

Given that multiple spreads can be calculated for each security against multiple curves (G-spreads against government curves, I-spreads against the swap curve, Z-spreads against an issuer-specific spline, etc.), a first question is which is the most appropriate. The simple answer is that usually the most sensible spread is the 1 that reflects the usual hedge strategy for the bond in question.

Government bonds are hedged with other government bonds and a Z-spread against government bond spline is the natural first choice for a relative valuation measure.

Sub-sovereigns, supranationals and agencies tend to be hedged with sovereign bonds and G-spreads would appear the natural first choice. However, G-spreads are not directly comparable between bonds that reference different benchmarks, and G-spreads do not correct for duration differences. A Z-spread against a government spline is therefore more meaningful. In the euro area, most SSA bonds are traded against French government bonds rather than the German curve. Constructing issuer-specific splines in the SSA segment is usually difficult given the lower number of outstanding securities, but the composite spline curves outlined in Section 19.4.5 on page 202 can be used in many cases.

High-grade corporate bonds, covered bonds and senior secured bank debt are usually hedged with swaps, so an I-spread or asset swap spread is a good first choice.

Corporate debt in general is subject to wide, and potentially steep, credit curves. A fair value model based on a risk free curve (usually the swap curve) and credit default swaps is a more approriate choice than the swap curve alone. Such models are beyond the scope of this book, cf. for instance [73].

Splines tend to be calibrated with no reference to repo rates. They therefore neglect the additional value that securities lending (collateral swaps) can bring to holding a bond that is special in the repo market, or the higher cost of shorting such a bond. The logically consistent way to incorporate this information would be to calibrate the spline not to spot prices, but to some form of forward. The reason this is not done widely is that on one hand it is not clear over what horizon the forward should be calculated, and that repo rates beyond the overnight horizon are very opaque. Calculating forwards over short horizons does not make much of a difference, and over longer horizons one would have to make some assumptions about the evolution of the overnight repo rates.

Beyond the simple answer that hedge strategies determine valuation benchmarks lies a more complex one. Hedging determines near-term price changes with reference to the more liquid hedge instruments. This is the appropriate frame of reference for identifying temporary misalignments in valuation patterns. However, if the aim is to identify underlying value, then these curve spread measures do not help so much. Seeing a KFW bond trade at 2 bps over a composite KFW spline means that the bond is cheaper than other KFW bonds, but not that it is a good investment. To determine whether it is a good investment, one would have to compare its spread to other substitutes (other German agencies, other euro area agencies), outlook for supply, trends in investor demand and so on.

## 32.2 RELATIVE VALUE STRATEGIES

## 32.2.1 Spread Widener/Tightener

FIGURE 32.1 Spread widener

<!-- image -->

If one expects a bond to underperform a curve, one can express this view with a spread widener. This involves selling the bond and receiving the appropriate curve. The default strategy would be to sell the bond in an asset swap and so hedge virtually all of the individual cash flow risk of the bond. Given the expense of executing such a non-standard swap, one might instead execute a matched (interpolated) swap. A spread tightener, the opposite trading view, involves the opposite positioning: Long the bond and paying the curve.

An area of uncertainty is the nomenclature. If the bond is trading above the curve, an underperformance of the bond will widen the spread to the curve. If the bond instead is below the curve, an underperformance will tighten it. The choice made here is to be consistent in terms of positioning and associate a short bond position with spread widening, even if it means a negative spread becoming less negative (as shown in the sketch). This is appropriate in a global curve environment where some government bond markets trade below and above the corresponding swap curves.

If one uses a spline curve to identify bond valuations, then positive spline spreads signal relative cheapness and so potentially a signal to put on a spread tightener. Negative spline spreads, correspondingly, might be a signal for future underperformance to correct relative richness. While the interpretation of this spread is straightforward, its expression in a trade is not because unlike swaps, spline curves cannot be traded directly. The solution is to embed the widening or tightening trade in a bond spread or butterfly position against one or two other bonds with the opposite valuation signals. The incentive to use a butterfly instead of a simple spread is a potential duration difference between the 2 bonds which exposes the trade to curve steepening or flattening risk. A butterfly removes this curve risk while butterfly risk is smaller in magnitude (cf. Figure 31.10 on page 356).

For bond portfolio managers tracking an index, the benchmark acts like a short position in the entire curve (cf. Section 38.1.3 on page 405). A spread widener can then be implemented through an underweight in this specific bond, while a spread tightener would suggest an overweight.

## 32.2.2 Basis Trade

FIGURE 32.2 Short basis trade

<!-- image -->

The alternative to paying or receiving a curve, where possible, is to be short or long a futures contract against a bond, i.e., a basis trade. In the example here, the short position in the bond is hedged with a long in a futures contract. This approach assumes that the futures contract will move in line with the curve in question, and that the futures contract CTD is close in maturity to the bond so that curve risk is not relevant.

The hedge equation is simply that the bond risk should be matched by the futures risk, with an opposite sign:

<!-- formula-not-decoded -->

Because a DV01-neutral package of a bond and a future has no duration risk, it is often tradeable with a lower bid-offer spread than an outright trade in the bond 1 .

Should bond and futures CTD differ significantly in maturity, then two different futures contracts can be used to eliminate the curve risk in line with a usual butterfly position. A useful assumption is that any yield curve steepening or flattening is linear, so the futures should be weighted according to their distance to the bond:

<!-- formula-not-decoded -->

where mB etc. are the times to maturity (in any unit) for the bond and the futures CTDs. This equation will lead to a higher hedge weight assigned to the future that is closer to the bond. Note that it is not necessary for the futures to bracket the bond ( mF 1 &lt; mb &lt; mF 2 ) and if the bond is outside the maturity points of the CTDs, the signs of NF 1 and NF 2 will differ.

## 32.2.3 Bond Spread

FIGURE 32.3 Bond spread trade

<!-- image -->

A bond spread trade is a simple long position in one bond and a short position in another. The mathematics match those of a curve steepener or flattener trade as discussed in Section 31.1.2. The difference is one of motivation, and that provides the link to bond relative value analysis.

In a steepening/flattening trade, the expectation is that curve shape changes and the bonds are chosen to implement this curve view. The trade suggested here is driven by an expectation that the relative valuation

of two bonds changes but the overall curve shape does not.

## 32.2.4 Bond Spread with Curve Hedge

The bond spread in the previous example is exposed to overall curve steepening/flattening risk. If the bond maturities are sufficiently far apart, this risk can negatively affect the risk/reward characteristics of the trade.

1 In this type of trade, the counterparties agree to cross the appropriate number of futures contracts on the exchange immediately after the trade.

FIGURE 32.4 Curve-hedged bond spread

<!-- image -->

Where suitable futures contracts are available, this curve risk can be hedged out by entering an opposite flattening/steepening position to the one formed by the spread trade. For instance, a spread trade between a 3Y and a 4Y bond could be hedged with 2Y and 5Y bond futures. Futures contracts, or in the US market the on-the-run benchmarks, have very tight bid-offer spreads compared to cash bonds so that the extra cost of entering or unwinding the hedge is comparatively low.

The appropriate amounts follow in essence the calculation for a curve steepener or flattener (cf. Section 31.1.2). For the 2 bonds and 2 futures, Equation (31.2) must hold, and in addition the risks on the bond leg must be the opposite as for the futures leg. This yields a system of 3 equations for 3 unknowns, in addition to the fourth parameter determining the aggregate risk:

<!-- formula-not-decoded -->

Evenwiththis hedge, the curve risk may not be fully hedged. For instance, if the 2 bonds in question were Dutch government bonds and one were to use German bond futures to hedge the curve because there are no futures on Dutch bonds, then the hedge would still be at risk from a relative steepening or flattening of the Dutch versus the German curve. This risk should be substantially lower, however, than the steepening risk of the Duch curve alone.

Note also that the configuration shown here, where the futures contracts surround the bonds in question, is not the only possible one. One can equally, and with the same equations, hedge a spread between a 3Y and 4Y bond using 5Y and 10Y futures. However, the more the futures diverge from the bonds in terms of curve sectors, the higher the residual curve risk of the trade.

## 32.2.5 Alternative Strategies

More complex trading strategies than the ones used here are possible, and more will become available with the development of new instruments. Swap futures are gradually building more liquidity and may at some point become a more natural way to express spread views than bilateral swaps. Money market futures strips already provide this opportunity in some cases (for instance, Euribor contracts against the Eurex Schatz futures, or Eurodollars against the US 2Y and 5Y Note futures). The essential designs of these trades are similar to the examples shown here and should not be too difficult to quantify for the reader.

One point that should be borne in mind, however, is that simplicity is a virtue for active trading strategies. An over-engineered trading strategy with too many parts tends to require a lot of re-adjustment during its lifetime which blurs the performance attribution.