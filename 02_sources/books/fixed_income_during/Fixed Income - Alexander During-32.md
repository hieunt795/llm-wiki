---
title: "Fixed Income - Alexander During-32"
type: raw_source
source_pdf: "Fixed Income - Alexander During-32.pdf"
extractor: docling
---

## CHAPTER 31

## Curve Trading

C urve trading is the summary term for trading strategies that are based on the anticipation of changes in the bond or swaps curve shape. Two important preliminaries must be remembered before going into the details of such strategies. First, although the strategies are analysed in terms of changes of the curve shape, they are implemented with specific instruments. The idiosyncratic valuation of these instruments relative to the overall curve shape creates additional risk in such strategies that should be borne in mind. The valuation of individual bonds or futures contracts in particular can deviate from surrounding bonds in the same curve segment. Second, carry in different parts of the curve is different and that means that a certain change in the curve shape is already priced into the current curve shape. Any risk position must be viewed relative to the forward curve on the analysis horizon, not the current curve.

There are a number of curve trading strategies and they can be visualised as in Figure 31.1. There, risk positions in bonds in four points A, B, C, and D are shown. Upwards arrows are meant to imply long positions, downward arrows short positions. Seen by themselves, A and C are outright longs, while B and D are outright shorts. Such individual positions can be combined, however, to express more complex views on curve movements. The possible combinations are shown in the following table.

| Legs   | Combination   | Name           | Positions for                                                                        |
|--------|---------------|----------------|--------------------------------------------------------------------------------------|
| 1      | A, C          | Outright long  | Falling yields                                                                       |
|        | B,D           | Outright short | Rising yields                                                                        |
| 2      | AB, AD, CD    | Steepener      | Long-term yields rising more, or falling less, than short-term yields                |
|        | BC            | Flattener      | Long term yields fallong more, or rising less, than short-term yields                |
| 3      | ABC           | Butterfly      | 5Y ('bullet') yields rising more, or falling less, than 2Y and 10Y ('wings') yields  |
|        | BCD           | Butterfly      | 10Y ('bullet') yields falling more, or rising less, than 5Y and 30Y ('wings') yields |
| 4      | ABCD          | Condor         | 5Y-10Y spread flattening relative to the 2Y-30Y spread                               |

FIGURE 31.1 An example of four curve positions on the German spline, shown here for 18 September 2018. The maturities for the positions have been chosen for illustrative purposes. Upwards arrows imply a long position, downwards arrows a short position. Source: Data from the Bundesbank.

<!-- image -->

FIGURE 31.2 Current par curve and implied 6 months forward par curve for the German Nelson-Siegel spline on 18 September 2018. Source: Data from the Bundesbank.

<!-- image -->

The carry (cf. Section 16.11 on page 167) and rolldown of a curve position is simply the weighted sum of the carry and roll-down of the individual legs. Naturally, a simple outright position has the largest carry and roll-down because the individual legs in higher-order trading strategies partially offset each other in this respect. However, an implication of Figure 31.2 is that curve positions have non-zero net carry. Because the forward par curve tends to be flatter than the current curve, a steepening trade has positive returns even in an unchanged yield curve scenario, for instance.

In general, a strategy with n legs requires the determination of n notionals and therefore a system of n equations. The first of these equations sets the size of the trade and there are two common ways of specifying this size. One is to simply select one notional amount. The more appropriate alternative is to specify the trade size in terms of risk, such as in currency units per 1 bps yield change. These representations are mathematically equivalent. For an outright trade with notional N , the risk R is simply:

<!-- formula-not-decoded -->

For more complex trades, the remaining equations are usually derived such that a trade with n legs is hedged against the risks of all trades with up to n -1 legs. For example, a butterfly trade ( n = 3) would therefore generally be set up so that it is hedged against outright yield moves ( n = 1) and steepening/flattening moves ( n = 2). The logic of this approach is that if one wanted to have steepening exposure in a butterfly, one could implement it in a separate additional trade. Hedging against n -1 exposures contributes n -1 equations so that together with the trade size, all n notionals can be determined. Details are discussed in the following subsections with sketches that show curve positions and an illustration of curve shifts, in dotted lines, that would lead to a positive P&amp;L from the respective trades. Trades that profit from the opposite curve shift can be set up by inversing the positions.

As will be seen later on, higher order curve movements (butterflies and condors) are smaller in absolute size than lower order movements (outrights or steepeners and flatteners). Given that the trading strategies aimed at profiting from correctly predicting these movements increase in transaction costs with each added leg, lower expected profits due to the smaller expected movement run against higher expected transaction costs.

The main reason to be interested in higher-order trading strategies, aside from the simple fact that there are a lot more possible trades, is therefore related to information advantage or preferred habitat structures. Most taxi drivers have an opinion about the outright direction of interest rates and practically all investors have ways to express such views in their portfolios. A trader entering an outright position needs to question whether he or she has information that is not available to the general public, and therefore not already reflected in current market prices given the ease with which such a position can be established.

Higher-order curve positions tend to be related to more predictable short-term market dislocations, such as auctions or other supply events. They can also arise implicitly from hedging of outright positions. A trader who bought an illiquid 7 year security as part of market making might be hedging it with 5Y and 10Y futures. This creates a butterfly position which is likely to have little curve risk. The same trader might hedge all of the 7Y risk by selling 10Y futures to deliberately enter a steepening trade, or build a flattener by hedging with 5Y futures only. Because so many possible combinations of two, three or more legs exist, there are more ways in which specific information can be optimally expressed in trades.

It is sometimes assumed that higher order strategies lend themselves to more active trading because they show more volatility. After all, economic theory would predict that outright moves in interest rates should more or less follow the business cycle and therefore take around 8 years on average to change direction. The reality is more complex. As will be discussed later (on page 356),outright moves in fact tend to dominate daily yield curve dynamics. What sets more complex strategies apart is the difference in risk-return dynamics. In any case, the income volatility of a trading book is not determined solely by the volatility of the rates it is exposed to, but also the size of that exposure.

It is now relatively common to combine outright strategies in fixed income with outright positions in other asset classes, such as equities or commodities. This is very similar to building higher-order strategies in fixed income alone because the general aim is to hedge out common economic factors and target specific discrepancies in pricing of what is assumed to be similar risk.

## 31.1 SIMPLE CURVE TRADES

## 31.1.1 Outright Trades

FIGURE 31.3 Outright short

<!-- image -->

Outright trades reflect expectations of general upwards or downwards yield movements. They are easy to set up and are in many cases combined with positions in other asset classes, notably FX and equities. In order to reduce transaction costs, some investors implement these trades with futures rather than cash bonds. This can lead to dislocations between the futures CTD bonds and surrounding bonds in the same market when liquid-

ity in the cash bond or repo market prevents efficient arbitrage between these market segments.

## 31.1.2 Steepeners and Flatteners

FIGURE 31.4 Flattener

<!-- image -->

The basic form of curve trading are steepening and flattening trades. To measure the steepness of the curve, one generally uses spreads between the benchmark bonds at certain maturities, usually those where a sovereign is actively issuing. Two examples of such spreads for the German curve are shown in Figure 31.5. They are simply the differences in yields of the benchmark bonds.

Higher order curve shape indicators can be constructed in a similar fashion. Before discussing how to set

up trades, one drawback of benchmark spreads should be pointed out. Benchmarks change over time, here because the sovereign issues new bonds. Typically, a new bond will have a slightly higher yield than the previous benchmark at the same maturity point because it will have a longer maturity and curves have a positive slope. The change in benchmark therefore usually creates an upward jump in the benchmark yield. While this jump may be small to outright yield levels, it still signals a change in market rates that is not related to a change in prices of any of the outstanding bonds (a change in prices may of course happen at the same time as the benchmark change). For spreads, the impact may seem larger, and a good example is the issuance of a new OBL (German 5Y benchmark) on 25 July 2018. As Figure 31.5 shows, on this day the 2Y-5Y spread apparently steepened while the 5Y-10Y spread flattened. The actual driver of this apparent curve shape change was the change in 5Y benchmark from the older OBL177 to OBL178, with a maturity extension of about half a year.

FIGURE 31.5 German government curve benchmark spread examples. The arrows mark the switches of benchmarks where they affect the respective spread. Source: Data from the Bundesbank.

<!-- image -->

A steepening or flattening trade should be hedged against outright yield movements. For the two notional N 1 and N 2 this means:

<!-- formula-not-decoded -->

For the second equation one could simply select a fixed value for N 1 or N 2 , but it is better to express the exposure in terms of risk. A fall in the yield at leg 2 by 1 bp with an unchanged yield in leg 1 creates a P&amp;L of N 2 PVBP2 . By Equation (31.2), the same P&amp;L arises when the yield in leg 1 increases by 1 bp for an unchanged yield in leg 2. This means that a risk R determines the notionals of a flattening or steepening trade as:

<!-- formula-not-decoded -->

A flattening trade has the same notional amounts but with opposite signs as a steepening trade. For the steepening trade, the longer maturity leg has a negative notional, for the flattening trade it is the shorter maturity leg.

Like all trades in this and the following sub-sections, one needs to be aware that the relationship Equation (31.2) will change over time because the two PVBP will decline over time. In relative terms, the decline will be faster for the shorter maturity leg. This implies that the hedge will have to be continuously adjusted over time, or should be executed in forward PVBP in the first place, with a forward horizon set in relation to the expected holding period.

FIGURE 31.6 Japanese 10Y and 30Y rates 2010-2015. Nelson-Siegel par yields with prices from JSDA.

<!-- image -->

Somewhat inevitably, steepening and flattening positions are also sometimes expressed in ownership terms. Being 'long the curve' is a steepener, 'short the curve' is a flattener [86]. Helpful mnemonics for this convention are that it is consistent with futures terminology (long the roll means long the front, short the back contract), and being long the curve means wishing that it goes up (steepens).

Although steepeners and flatteners are linear trades, they can sometimes exhibit non-linear behaviour. For example, Figure 31.6 shows a scatterplot of the Japanese 10Y and 30Y JGB yields and there is a clear change in the slope between the two variables at around 0.75% in 10Y yields and 2% in 30Y yields. The explanation for this behaviour is that in the JGB market is largely domestic and some local investors base their behaviour on fixed yield targets related to life insurance liabilities. This creates strong demand for long-dated bonds above these target yields. In a sell-off, the long end of the curve is thereby supported at a certain level.

Foratrader, such changes in behaviour create interesting opportunities, namely linear trading strategies that have an option-like non-linear pay-out when yields are near their pivot point. Of course, while it is possible to mine historical data for such opportunities, trading decisions require more structural analysis. The reason why Figure 31.6 presents data before 2016 is the change in JGB curve dynamics induced by the Bank of Japan quantitative easing policy. Interest rate levels in Japan are now far below most investors' target levels and BoJ operational implementation is now more significant for curve movements than before.

## 31.1.3 Butterflies

FIGURE 31.7 Butterfly

<!-- image -->

A butterfly trade is exposed to the performance of one instrument relative to two instruments of shorter and longer maturities. The centre instrument is known as the bullet (less often as the body), the other two are the wings. A difference exists between the conventions in the swap and bond markets when it comes to the measurement of butterfly spreads. While bond traders quote butterflies as bullet yield minus half of the sum of the two wing yields, swap traders quote the sum of the two wing

rates minus twice the bullet rate. For identical interest rates, a bond butterfly spread is therefore half the number, with the opposite sign, of the swap butterfly spread. This inconvenience stems from the idea that swap rates are imagined as borrowing rates whereas bond yields describe incomes.

For bond butterflies, the benchmark change problem becomes more acute because it applies to three legs of a trade that tends to have little volatility. The standard remedy is to use spline yields instead of actual bond yields for analysis although the actual trade would still have to be implemented with specific bonds.

The weights of the legs follow from the principle outlined above that the trade should not have directional or steepening risk. These translate into the two equations:

<!-- formula-not-decoded -->

An alternative way to interpret these equations is to visualise a butterfly as a combination of a steepener and a flattener with identical risks and a shared leg that forms the bullet. Each of the two trades is duration neutral, and if they have equal but opposite exposure to steepening risk, the butterfly will also be hedged against this type of risk. In terms of equations, one can split the bullet position N 2 into two parts N a 2 and N b 2 ( N 2 = N a 2 + N b 2 ) and specify the trade as follows:

<!-- formula-not-decoded -->

where the last equation is equivalent to N a 2 PVBP2 = N b 2 PVBP2 , i.e., N a 2 = N b 2 which means an even split between the two components of the bullet.

A variation of the equal-weighted butterfly is to adjust the wing risks to the maturity difference between each wing and the bullet. This corresponds to the assumption that the curve steepening or flattening is mostly linear, and Equation (31.4) is then replaced by:

<!-- formula-not-decoded -->

This butterfly will have a higher absolute weight on the wing closer to the bullet. It should be borne in mind, however, that the risk characteristics of very unevenly weighted butterflies are essentially those of steepening or flattening trades. It is therefore rare to see recommendations like a 2Y-4Y-30Y butterfly.

## 31.1.4 Condors

FIGURE 31.8 Condor

<!-- image -->

A condor is a comparatively rare strategy involving 4 positions along the same curve with equal risk amounts. The simplest way to conceptualise this strategy is as a combination of a steepener and a flattener with equal risks. The 2 legs of 1 of these strategies are outside 2 legs of the other. While multiple positions across the curve are common in most trading books, the specific choice to make the risks of the 2 constituent strategies equal sets the condor apart.

The equations determining the notionals follow those of a simple steepener and flattener Equation (31.2) for each of the two basic strategies, and an additional equation ensures the equality of the risk of these two strategies:

<!-- formula-not-decoded -->

## 31.2 INTRINSIC CURVE MOVEMENTS

Curve spreads describe the curve shape in terms of standard yield differences. As pointed out in the previous section, such spreads can be subject to various correlations that need to be taken into account before judging the appropriateness of their levels. This suggests an alternative approach, namely to extract characteristic curve movements from the historical data instead of imposing them ex-ante. A useful, but by no means exclusive approach to that is a PCA of par yields as demonstrated in Figure 31.9. A number of par yields are put into a PCA and the 3 factors (eigenvectors) corresponding to the largest three eigenvalues are shown 1 .

1 Note that, even with normalisation, eigenvectors are invariant to a change of sign on each component. The signs PCA factors shown here have been adjusted so as to correspond to standard curve strategies.

| Eigenvalue   |       1 |       2 |       3 |       4 |
|--------------|---------|---------|---------|---------|
| Value (% 2 ) | 0.02226 | 0.00358 | 0.00039 | 0.00013 |

FIGURE 31.9 Normalised PCA factor loadings for the US Treasury Nelson-Siegel spline. History 2014-2018, PCA on daily first differences. Source: Data from treasurydirect.gov.

<!-- image -->

PCA is often used in this context because the preconditions for PCA to give meaningful results are aligned with those of a good trading strategy. Yield movements are assumed to be driven by independent factors that follow stationary normal distributions, and the contributions of these factors are additive. Under these conditions, hedging against 1 or more factors will present an optimal reduction in market risk.

In the examples used here, as in some other studies, an additional issue should be borne in mind. Bond yield curves extracted from parametric models are very convenient as PCA inputs because they avoid the problems created by the aging of underlying bonds. That said, the underlying curve model imposes a correlation structure on the yields at various horizons and reduces the number of independent variables in the system. Logically, there cannot be more independent factors driving those model yields than the model has parameters, no matter how many bonds are used to fit the model. A PCA may, however, show a larger number of independent factors because the model parameters have a non-linear impact on model yields.

Once PCA factors have been calculated, one can calculate the residuals of the yield curve after removing a given number of factors. Assuming the input yields are given as the vector y ( t ) , the residual curve y k ( t ) after removing the first k factors e i is simply:

<!-- formula-not-decoded -->

FIGURE 31.11 Normalised PCA factor loadings for the German government bond Nelson-Siegel spline. History 2014-2018, PCA on daily first differences. Source: Data from Bundesbank.

<!-- image -->

| Eigenvalue   |       1 |       2 |       3 |       4 |
|--------------|---------|---------|---------|---------|
| Value (% 2 ) | 0.01138 | 0.00109 | 0.00016 | 0.00002 |

FIGURE 31.12 First PCA factor realisations for the US and Germany. History 2014-2020. Source: Data from treasurydirect.gov and Bundesbank.

<!-- image -->

PCA factors of the US and German curves, shows essentially two different correlation regimes. One is a nearly one-for-one correspondence of changes, the other has a nearly static German first factor against a volatile US one. Given that during the observation period the ECB started a sizeable public sector bond purchase programme that had a significant dampening effect on yield levels in the euro area, while the Fed started a reduction in the bond portfolio it had accumulated earlier, such changes in correlation should not be surprising 2 .

FIGURE 31.13 PCA factor realisations for the US Treasury Nelson-Siegel spline. Because the factors are normalised, their realisations show a good measure of their actual yield impact. History 2014-2020. Source: Data from treasurydirect.gov.

<!-- image -->

The second PCA factor tends to describe relative yield changes between the front and back end of the yield curve, i.e., a steepening or flattening of the yield curve. The relationship between maturity and yield change is only rarely linear. Also, the first PCA factor tends to already incorporate some degree of yield curve shape change rather than a parallel move. A correlated movement of yield levels and curve slope is known as bear-steepening, bear-flattening, or their opposites bull-flattening and bull-steepening, respectively. The steepening or flattening captured by the second factor therefore is a movement that is uncorrelated by the steepening or flattening already incorporated by the first factor.

The third PCA factor also tends to have a characteristic shape, namely an underor out-performance of the centre of the curve relative to the short and long ends. Because every duration-neutral butterfly with a short bullet position has positive convexity, re-hedging the trade after every outright yield shift should over time result in a positive P&amp;L, at least before transaction costs. To the extent that volatility is expected by the market, this positive P&amp;L should be reflected in the carry of the trade which is determined by the shape of the yield curve. By implication, therefore, the yield of the bullet should be higher than the straight-line interpolated yield of the 2 wings at the bullet maturity point. This means that the usual convex shape of the yield curve is related to the convexity of butterfly trades. Although it is unlikely that this is the sole explanation for the yield curve shape, the convexity of the yield curve does tend to be connected with volatility. Because curve convexity tends to be captured by the third eigenvector of a curve PCA (cf. Figures 31.9 and 31.11), this connection is visible when plotting the realisation of this factor against implied volatility. This is done in Figure 31.14 for the US Treasury market (as in Figure 31.13) against a measure of fixed income volatility, namely the VXTYN index produced by CBOE.

2 Non-standard monetary policy tools affect the formation of market prices. If different markets can reflect changes in economic fundamentals only to a limited degree, than this should suppress the correlation between their yield movements.

FIGURE 31.14 Scatter plot of the PCA factor 3 realisation versus the CBOE VXTYN volatility index. US Treasury Nelson-Siegel spline. History 2014-2018. Source: Data from treasurydirect .gov, index data downloaded from FRED.

<!-- image -->

The correlation is positive in this dataset but clearly not strong enough to argue that implied volatility is the sole driver of curve convexity. Again, the nature of PCA is such that if implied volatility were itself very volatile and responsible for very significant changes in curve shape, the effect would show up already in the lower eigenvectors. In addition, the convexity effect on curve shapes tends to be fairly localised, and is therefore more clearly evident in analyses such as Figure 20.4 on page 210.

It should therefore not surprise that there is also not too much of a relationship between the model volatility of a structural curve model such as the Vasicek model and realised curvature (cf. Figure 31.15).

While the Vasicek spline parameter k does change curvature (cf. Figure 19.5 on page 201), the way in which this occurs need not coincide with how curvature is captured by the PCA analysis. An important contributor to this discrepancy is the correlation between the various parameters of the Vasicek spline, or indeed generally the parameters of structural curve models.

At the time of writing, the yield curves in major markets, and the implied volatilities of interest rates, are heavily influenced by direct central bank actions, namely large-scale asset purchase programmes or portfolios, and relatively clear forward guidance of interest rates. To some degree, this limits the impact of economic factors, such as the relationship between volatility and convexity, on the curve shape.

FIGURE 31.15 Scatter plot of the PCA factor 3 realisation against the k parameter of a Vasicek spline fitted to the US Treasury curve. History 2014-2020. Source: Data from treasurydirect.gov.

<!-- image -->

FIGURE 31.16 History of the /u1D706 parameters of the daily ECB AAA Nelson-Siegel-Svensson spline. Source: Based on ECB SDW. Note that the ECB specification refers to these parameters as /u1D70F 1 and /u1D70F 2 .

<!-- image -->

## 31.2.1 Alternative specifications

As mentioned above, it is by no means clear that PCA is the most appropriate way to extract patterns of curve shapes and measure their changes. The Nelson-Siegel and Nelson-Siegel-Svensson splines are explicitly designed to reflect standard yield curve changes ('level', 'slope' and 'hump') through different /u1D6FD parameters (cf. Figure 19.3 on page 197). Without going through the circuitous route of fitting a spline to market yields, and then running the resulting spline par yields through PCA, one could directly use the relevant parameters of these models.

While this is an interesting thought, there are 2 problems with it. The first is that the /u1D706 parameters of the Nelson-Siegel splines tend to be very volatile, as shown in Figure 31.16. The parameters /u1D6FD 3 and /u1D6FD 4 measure the size of humps but it is not possible to consistently express the size of such a hump through a butterfly trade because the location of that hump is shifting. The second difficulty is that the /u1D6FD i are correlated through time. A butterfly trade with 3 legs has 2 free parameters for hedging and finding the corresponding 2 equations requires bumping each of the /u1D6FD parameters to establish model sensitivities 3 and a historical correlation analysis of the /u1D6FD .

3 One might argue that the /u1D6FD linearly determine interest rates and model sensitivity should therefore be straightforward. This would be true if the trade was implemented with zero-coupon instruments. Usually that is not the case, however, so the non-linear dependencies of par instrument prices need to be used.