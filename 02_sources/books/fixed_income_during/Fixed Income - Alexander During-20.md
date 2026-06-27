---
title: "Fixed Income - Alexander During-20"
type: raw_source
source_pdf: "Fixed Income - Alexander During-20.pdf"
extractor: docling
---

I

## CHAPTER 19

## Curves and Curve Models

n Section 16.7, on yields, it was pointed out that Equation (16.10):

<!-- formula-not-decoded -->

suffers from a fundamental defect, namely that the same discount rate y is applied to every cash flow of a given bond. In a typical market with more than one bond, it will generally be the case that these bonds trade at different yields. Cash flows occuring at the sameorsimilar times from different bonds would therefore be discounted with different rates depending on which bond they belong to. This is somewhat unsatisfactory when one associates yields with the expected rate of return available in the market for investments of a given horizon. One would therefore somehow prefer to change Equation (16.10) in such a way that y becomes a function of time, i.e., y ( t ) .

This of course runs into a mathematical problem, namely that a single equation can only define the value of a single variable. However, these two problems solve each other: By using information about multiple bonds simultaneously , one can derive time-dependent discount rates that are consistent with the prices of these bonds. Such a time-dependent set of discount rates is known as a term structure and the model representation of a term structure is a curve.

Therefore, a yield curve is the representation of market information contained in the prevailing prices of a set of fixed-income instruments. It can be seen as a holding bag for instrument definitions and prices. The complexity of this holding bag can differ widely between different representations.

The purpose of using curves is that they allow the pricing of instruments using discount factors. These instruments need not be the same ones as those used to define the curve itself, and they need not even exist at all. Overall, therefore, one has a structure as shown below where instrument definitions and prices are used to form a curve and the curve, and instrument definitions and a curve provide prices:

<!-- formula-not-decoded -->

The concrete representation of a curve is known as a model. Different types of curve models are explained in the next section. In this book, the focus is less on the many varieties of curve models that have been proposed because good literature exists on those ([40, 52, 69] etc.). Instead, the focus is on the use of models for trading.

## 19.1 MODELS

<!-- image -->

The concept of a curve is fundamental for the comparison of fixed income products over different time horizons. Generally speaking, a curve is the abstract concept of associating interest rates with investment horizons. The concept of interest rate curve of various kinds has already been used implictly when interest rates were treated as time dependent in the sections on money market calculations. It is important to be aware that there are many different ways of representing time-dependent interest rates and that there may be more than one interest rate applying to a given time horizon, namely when credit risk, liquidity factors, and legal issues (such as onshore versus offshore markets) are taken into account.

The simplest theoretical starting point for understanding curves is to consider the discount factor curve, i.e., a mapping from time t to a discount factor Df ( t ) . More generally speaking, a discount factor curve is a function Df ( t 1 , t 2 ) of two time arguments t 1 and t 2 &gt; t 1 giving the value of a unit payment at t 2 at the investment time t 1 . However, if the discount factors are unique, one can always use the reinvestment identity:

<!-- formula-not-decoded -->

to write the 'forward' discount factors in the form of a single argument function.

In general, one can think of 3 mathematically equivalent representations of the yield curve, namely via discount factors, zero rates, or instantaneous forward rates. The par curve, i.e. the mapping from a maturity time t to the coupon rate of a bond that will be priced at 100% of notional value differs from these 3 equivalent curves in that the par curve depends on bond market conventions, such as coupon frequency, holiday calendar, and daycount convention. The relationship between the 4 curve representations is therefore best represented by Figure 19.1.

FIGURE 19.1 Curve representations.

<!-- image -->

## 19.2 YIELD CURVE REPRESENTATION AND INTERPRETATIONS

## 19.2.1 Discount factors versus par curves

The discount factor form is the theoretically most natural way of expressing a term structure of discount factors, but it is by no means the only one. A common form of representing the same information is to write discount factors in the form of a par interest rate curve, i.e., as a mapping from a time to maturity to the interest rate (coupon) of a par bond. The price of any fixed coupon bond is given as the total present value of all its cash flows, so for a par bond with a coupon frequency of f :

<!-- formula-not-decoded -->

so that the par interest rate C ( t N ) of a bond maturing at t N is:

<!-- formula-not-decoded -->

This representation is common because fixed rate coupon bonds represent the most common investment universe for bond investors. However, it has a number of obvious drawbacks. First, the par rate is in general dependent on the coupon frequency and it will have a more complicated form when the time to maturity is not an integer multiple of the coupon period. Par curves are therefore usually restricted to node points that are evenly spaced at coupon periods. Furthermore, actual bond coupons are fixed at the time of issuance so that par bonds may not actually be available for investment. The par curve is therefore not directly observable in general. Note also that if the coupon frequency is not annual and the yield convention is not bond-equivalent, the yield of a par bond is not equal to the coupon. One could then alternatively define the par curve as the yield curve of par bonds. The translation between the two definitions is straightforward, however.

Equation (19.3) is a translation from discount factors to par rates. The opposite translation is referred to as bootstrapping, explained in Section 19.3.1.

There are two fundamentally different modes of curve representation. On the one hand, one can treat a curve as a collection of observable and tradeable instruments in the market, together with a prescription of how to calculate interest rates that are not given by these instruments, such as interpolation rules. The second type of representation uses a general functional form for the mapping between maturities and interest rates and this mathematical form is used with a set of parameters which will give discount factors or interest rates that best reproduce the rates observed in the market. The two representations can coincide in the extreme sense that the bootstrapping method above, together with the coupon bond price P i , the coupon Ci and the maturity point t i , form a parameter set. The intention of market-based curves is generally to obtain a set of discount factors that reprices all market instruments exactly to avoid apparent arbitrages between the model curve and the actual market. This exact repricing usually requires a large number of inputs and may lead to non-intuitive forwards. Parametric curves, in contrast, are usually chosen to arrive at a reduced number of curve parameters and smooth forward rates. Due to the restricted parameter space, not all market instruments, if any, are repriced exactly by such models. On the other hand, divergences between the prices implied by a parametric model and actual market prices can in some cases represent actual dislocations and parametric models are therefore an important tool to discover such opportunities.

Economists tend to focus on zero rates, which are (unfortunately) also known as spot rates. A zero rate z ( t ) is the market rate for investing money from today to t when there is no intervening cash flow (as opposed to a par curve, where there is a periodic coupon payment). Zero rates avoid the reinvestment risk associated with coupon payments. The interest rate at which a coupon can be reinvested can differ from the initial yield of a coupon bond. The disadvantage is that zero rates are practically unobservable in the market 1 and need to be extracted from coupon bond prices through bootstrapping or spline fits. The price of a zero coupon bond trading at a rate of z ( t ) is nothing but the discount factor Df ( t ) , namely:

<!-- formula-not-decoded -->

Zero rates also allow the easy calculation of forward rates, that is, the arbitrage-free interest rates f ( t 1 , t 2 ) that are consistent with zero rates from today to t 1 and t 2 . The no-arbitrage condition is:

<!-- formula-not-decoded -->

1 There are zero coupon government bonds created through the stripping of coupon bonds, i.e., the separation of coupon and principal payments. The low liquidity of such intruments means that their prices are not completely aligned with the liquid market prices of the original coupon bonds.

Therefore:

<!-- formula-not-decoded -->

This formula can be, and frequently is, simplified when all t are integer and one is looking for the one-period forward rate f ( t , t + 1 ) . Using the binomial expansion:

<!-- formula-not-decoded -->

and noting that when z ( t ) ≪ 1 the binomial expansion is dominated by its first terms:

<!-- formula-not-decoded -->

Noting also that, for small x :

<!-- formula-not-decoded -->

so that Equation (19.5) becomes:

<!-- formula-not-decoded -->

## 19.3 MARKET-BASED CURVE REPRESENTATIONS

Asmentionedintheoutline,market-basedcurvemodelsareessentially holding bags for market instruments and their prices, together with rules for extracting discount factors and pricing other instruments.

## 19.3.1 Bootstrapping

The standard way to extract discount factors from equally spaced market rates, such as government bonds or swap rates, is bootstrapping. This procedure consists of progressively stripping coupon instruments into zero coupon instruments, at each step using the zero rates obtained during the previous steps to take the next one. An example is shown in Table 19.1.

The calculation here assumes annual rates, and a daycount convention of annual/annual for simplicity 2 . Under this assumption, the 1Y swap is a zero coupon instrument paying par plus the coupon of 0.307%, so the 1Y discount factor Df 1 is determined by the 1Y par rate p 1 as:

<!-- formula-not-decoded -->

2 For USD swaps, the fixed rate is actually semi-annual.

TABLE19.1 Bootstrapping of the USD swap curve on 5 June 2020. For simplicity, swap rates have been assumed to be annual. Source: Data from ICE.

|   Years | Par rate   |       Df |     ∑ Df | Spot   | Fwd    |
|---------|------------|----------|----------|--------|--------|
|       1 | 0.307%     | 0.996939 | 0.996939 | 0.307% | 0.307% |
|       2 | 0.299%     | 0.994047 | 1.990986 | 0.299% | 0.291% |
|       3 | 0.346%     | 0.989687 | 2.980673 | 0.346% | 0.441% |
|       4 | 0.424%     | 0.983193 | 3.963866 | 0.425% | 0.660% |
|       5 | 0.517%     | 0.974469 | 4.938335 | 0.519% | 0.895% |
|       6 | 0.614%     | 0.963761 | 5.902096 | 0.617% | 1.111% |
|       7 | 0.704%     | 0.951749 | 6.853845 | 0.709% | 1.262% |
|       8 | 0.783%     | 0.938982 | 7.792827 | 0.790% | 1.360% |
|       9 | 0.854%     | 0.925545 | 8.718373 | 0.863% | 1.452% |
|      10 | 0.915%     | 0.911883 | 9.630256 | 0.927% | 1.498% |

The 2Y swap then is a coupon payment (here of 0.299%) after 1 year, and a payment of par plus the same coupon after 2 years. The discount factor to the 2Y point is at this stage unknown but the discounted values of the coupon of 0.299% paid after 1Y and the payment of 100.299% after 2 years must add up to par. Therefore,

<!-- formula-not-decoded -->

Moving on to the 3Y swap, it pays 2 coupons of 0.346% (after 1 and 2 years) which have now known discount factors, plus a final payment of 100.346% after 3 years. Hence,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Table 19.1 contains the auxiliary column ∑ Df containing the sum of discount factors up to the current line, used in the numerator of Equation (19.11). The zero and forward rates are merely derived quantities in this algorithm. The zero rates are given by:

<!-- formula-not-decoded -->

This series continues as:

FIGURE 19.2 'Bootlacing' representation of the bootstrapping process. Sources: Data from ICE and graphics produced in LibreOffice Calc.

<!-- image -->

and the forwards starting at period i by:

<!-- formula-not-decoded -->

When done in a spreadsheet application, the iterative nature of the bootstrapping process can be visualised as a 'bootlacing' by switching on tracing of precedents, shown in Figure 19.2.

In an actual application on coupon bonds, a stub discount factor will apply to the first cashflow which in general occurs earlier than a full coupon period. This stub discount factor carries through to all subsequent cashflows. Similarly, the price of each coupon instrument has been assumed to be par in Equations (19.8, 19.9, 19.10) but this will not generally be the case for actual coupon bonds. These changes can easily be incorporated into the equations and do not fundamentally alter the process.

## 19.3.2 Reverse bootstrapping

The bootstrapping process outlined above decomposes a regular sequence of coupon instruments into discount factors and zero rates. Occasionally, there is a need to decompose a series of cashflows into par instruments, for instance to translate a given payment obligation into a portfolio of par swaps, or to construct a par bond portfolio with a given payment profile.

Because this decomposition is in some ways the reverse of bootstrapping, it starts at the longest maturity point and progresses towards the shortest. Table 19.2 demonstrates the decomposition of a simple annuity into par swaps using the same curve as in Table 19.1.

Starting at the end, the payment obligation V 6 at the 6Y point is translated into a notional payment plus the par coupon on this notional. The notional is:

<!-- formula-not-decoded -->

TABLE19.2 Reverse bootstrapping of a 6-year annuity using the USD swap curve on 5 June 2020. For simplicity, swap rates have been assumed to be annual. Source: Data from ICE.

|   Years | Par rate   |   Obligation |   Notional |       ∑ I |
|---------|------------|--------------|------------|-----------|
|       1 | 0.307%     |            1 |  0.9752964 | 0.0247036 |
|       2 | 0.299%     |            1 |  0.9782906 | 0.0217094 |
|       3 | 0.346%     |            1 |  0.9812157 | 0.0187843 |
|       4 | 0.424%     |            1 |  0.9846107 | 0.0153893 |
|       5 | 0.517%     |            1 |  0.9887854 | 0.0112146 |
|       6 | 0.614%     |            1 |  0.9938975 | 0.0061025 |

At the next shorter, the 5Y point, the payment obligation is equal to the 6Y coupon payable on the 6Y swap, plus the 5Y coupon and 5Y notional repayment. Therefore, the notional is:

<!-- formula-not-decoded -->

Moving on to the 4Y point, this becomes:

<!-- formula-not-decoded -->

In this form it continues to every shorter point as:

<!-- formula-not-decoded -->

Again, it is helpful algorithmically to carry the summation term of Equation (19.17) as a separate variable, as done in the last column of Table 19.2.

In this example, a flat annuity has been decomposed into par notionals and as one would expect for positive interest rates, these notionals increase gradually towards longer maturities as the interest payable declines with each maturing par instrument. This calculation differs from the mortgage formula Equation (16.1) on page 141 in that it uses an actual market par curve to discount each cashflow with the appropriate discount factor while the mortgage formula uses a flat interest rate r .

## 19.4 PARAMETRIC CURVE MODELS

As mentioned earlier, parametric curve models, sometimes also labelled reduced-form models, do not attempt to reprice all market instruments exactly. Instead, their aim is to arrive at a reasonably accurate representation of market rates, and the identification of relative valuation opportunities.

FIGURE 19.3 Sensitivities of zero rates given by a Nelson-Siegel spline to 25% bumps in each curve parameter.

<!-- image -->

## 19.4.1 The Nelson-Siegel and Nelson-Siegel-Svensson splines

The Nelson-Siegel spline is a curve model that expresses spot (zero) rates as:

<!-- formula-not-decoded -->

The contributions of the 3 terms prefixed by /u1D6FD 1 , 2 , 3 represent a constant, an exponentially declining short-term contribution and a hump-shaped medium-term component. The time scale of the second and third components is calibrated by the /u1D706 parameter. This easy interpretation means that this type of model is often used by economists, including central banks, to represent bond yield curves in a parsimonious manner.

Auseful way to demonstrate the role of each parameter is to fit the curve to a given market so as to obtain a realistic set of parameter values. One can then measure the changes on interest rates induced by changing the value of one parameter at a time. For the Nelson-Siegel spline Equation (19.18), this is done in Figure 19.3 for the example of zero rates.

The Nelson-Siegel-Svensson model is simply the Nelson-Siegel model Equation (19.18) with a second hump term added:

<!-- formula-not-decoded -->

Theadditional two parameters ( /u1D6FD 4 and /u1D706 2 ) make the Nelson-Siegel-Svensson model somewhat more flexible. At the same time, the separation between the two /u1D706 parameters can be weak, which leads to identification problems between the terms led by /u1D6FD 3 and /u1D6FD 4 .

A Nelson-Siegel spline is used in the calculation of the REX index of Germany government bond yields. The REX index is administered by Deutsche Börse AG and the associated REXP performance is used by some German domestic fund managers. Because German government bonds used to exhibit a strong tax-driven coupon effect, the Nelson-Siegel form of a polynomial yield curve is augmented by a second-order polynomial of the coupon for each bond.

The REXP is based on the performance of 30 theoretical bonds with integer maturities of 1, 2, . . . 10 years and coupons of 6%, 7.5%, and 9% to calculate the daily performances. The REXPis not representative of the German debt market because it uses fixed weightings for the 30 theoretical bonds instead of actual market weights for the maturity sectors. More fatally for investors looking to replicate the REXP performance, current German government coupons are lower than the theoretical benchmark coupons and the tax effect is such that the yield of higher coupon bonds is higher than that of lower coupon bonds. The running carry of the REXP benchmark basket is therefore higher than what can be achieved with the actual underlying bonds. Managers benchmarked to the REXP index therefore generally carry spread risk to earn back the basis between the benchmark and the actual underlying market.

## 19.4.2 Polynomial splines

Although the word 'spline' has already been used in the context of the Nelson-Siegel spline, mathematically a spline refers to a narrower class of functions, namely piecewise polynomials. It is therefore natural to try and use such piecewise polynomials to represent yield curves. To define a spline, one uses a set of N node points t i where time ordering is assumed for simplicity ( t i &gt; t j ∀ i &gt; j ). One can, but does not have to, assume t 0 = 0.

Apiecewise polynomial of degree n is a set of polynomials defined by:

<!-- formula-not-decoded -->

This definition provides a set of N -1 basis funtions over the closed intervals [ t i , t i + 1 ] and these basis functions have n coefficients each. To reduce the number of free parameters, one adds the constraint that the first n -1 derivatives of these polynomials should agree at the node points, i.e.,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

. . .

These constraints can of course be expressed in terms of the polynomial coefficients /u1D6FD i , k which then give a system of ( N -1 )( n -1 ) linear equations. This set of equations is incomplete as long as no additional constraints are posed to resolve the remaining N -1 free coefficients. There are two possible ways to define these equations. The approach

taken in computer graphics, where splines are most commonly applied, is to define the values of the polynomials at the node points t i . Because there are N node points, the most useful choice for a curve model is to leave the value free at t N = ∞ . However, the choice of restricting the values at the node points means that one needs to obtain market yields at the node points which generally means that node points are set to correspond to the maturities of benchmark instruments. Replicating the swap curve with such a spline model is unproblematic because swap rates to fixed maturities are observable in daily market data. If cash bonds are used instead, one has to live with the fact that the time to maturity for each node point will be changing every day. Normally, the time to maturity will drop by one business day each business day, but there will be jumps in the node location whenever a new benchmark appears. This may be a problem in some applications, especially because the smoothness condition does not extend far enough to generate continuous forward overnight rates (unless of course overnight rates are used to build the spline). However, a polynomial spline fitted to market par yields in general delivers a yield curve that can be hedged with market instruments (albeit with a number of instruments that is equal to the number of node points). This means that the polynomial spline curve is tradeable; which is, of course, a precondition for using it in curve arbitrage trades.

Apolynomial spline was the basis for the now discontinued JEX/JEXP index family produced by Deutsche Börse AG for the German Jumbo Pfandbrief market.

## 19.4.3 The exponential spline

The exponential spline model is a model that is formulated explicitly in discount factor space. In particular, discount factors are written as:

<!-- formula-not-decoded -->

The boundary condition Df ( 0 ) = 1 translates directly into:

<!-- formula-not-decoded -->

The basis functions of this spline are ever faster declining exponentials, and in the special case of n = 1 the model is simply one where the yield 'curve' is given by a constant exponentially compounded interest rate /u1D6FC . For n &gt; 1, this interpretation is preserved in the limit of very large t because for t ≫ 1:

<!-- formula-not-decoded -->

/u1D6FC therefore has the natural interpretation as the infinite maturity exponentially compounded zero rate. In practice, however, it is much better to think of /u1D6FC as a time scale parameter similar to the /u1D706 parameter in the Nelson-Siegel spline. Larger values of /u1D6FC make the spline more flexible.

FIGURE 19.4 Sensitivities of zero rates to 25% bumps in /u1D6FC and absolute bumps of 0.1 to the /u1D6FD parameters of the exponential spline model. The role of the /u1D6FD terms as successively faster declining exponential funtions is clearly visible.

<!-- image -->

The prices of coupon bonds are linear functions of the /u1D6FD i so that the square errors of bond prices become a quadratic function in the /u1D6FD i . The equations for the minimum square error, i.e., the first derivatives with respect to the /u1D6FD i are therefore linear in the /u1D6FD i which makes the exponential spline very efficient to fit to bond prices.

## 19.4.4 The Vasicek spline

The Vasicek spline is a simple structural curve model where the evolution of the short rate follows the process:

<!-- formula-not-decoded -->

where Wt is a Wiener process. It has the useful property of allowing a closed-form calculation of the discount factors which means that calculating asset prices does not require a computationally costly numerical integration. This makes the model a useful entry point to structural curve analysis.

Following [12] using two shortcuts A ( t ) and B ( t ) as follows:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The theoretical beauty of a structural curve model is that the curve shape is determined by the volatility of the short rate, here characterised by /u1D70E and the mean-reversion strength k . In principle, therefore, one should find a calibration of the model where

one has:

FIGURE 19.5 Sensitivities of zero rates to 25% bumps the parameters of the Vasicek spline model.

<!-- image -->

FIGURE 19.6 Scatter plot of the /u1D70E parameter of a daily Vasicek spline fitted to the US Treasury curve against the CBEO VXTYN Treasury implied volatility index. History 2014-2019. Sources: Treasury prices from treasurydirect.gov and VXTYN data retrieved from FRED.

<!-- image -->

the model-implied volatility is somehow related to the observable implied volatilities traded in the market.

However, this is not a trivial task. Figure 19.6 shows the correlation between the /u1D70E extracted from fitting a Vasicek spline to daily observations of the US Treasury curve against an index of market-traded volatility (the CBOE VXTYN index) 3 . The R 2 between these two series is less than 0.1. In defense of the Vasicek model it should be noted that the VXTYN is an index of short-dated options on a 10Y Treasury future while the /u1D70E

3 The figure deliberately excludes data after July 2019 when the US curve had several bouts of volatility.

parameter of the model is a long-dated volatility of the overnight rate. This mismatch in volatility type is, however, only a partial explanation of the low correlation. In general, it is very difficult to achieve a self-consistent calibration of market interest rates and volatility in a structural model without inserting the interest rate path explicitly, or working with an unwieldy number of parameters.

## 19.4.5 Composite models

The yield curve models presented so far work well for individual markets but may face some problems when comparing related sub-markets. For instance, the debt of national agencies would normally be expected to trade at slightly higher yields than that of the sovereign due to a small liquidity premium for sovereign bonds. Fitting two independent splines to the sovereign and agency bonds sometimes results in situations where the agency spline is partly below the sovereign spline, usually because there are fewer bonds in the agency market, resulting in over-fitting behaviour. In some cases, there are so few bonds on the agency curve that a reliable calibration of splines with a larger number of parameters is impossible.

A useful solution to this problem is the use of composite splines. One defines the discount factors of the composite model as:

<!-- formula-not-decoded -->

where Df B ( t ) are discount factors derived from a base market (in this example the sovereign bonds) and Df S ( t ) is constructed to reflect only a spread component so that the agency bonds are correctly priced. An attraction of this approach is that the functional form of Df S ( t ) can be much simpler than that of Df B ( t ) . Instead of a fully fledged Nelson-Siegel-Svensson with 6 parameters for Df B ( t ) one could define Df S ( t ) simply as:

<!-- formula-not-decoded -->

so that the spread between the 2 curves, expressed as continuously compounded zero rates, is a simple polynomial defined by only k + 1 parameters. The calibration of such a spline is a sequential process where the Df B ( t ) are first constructed using a model like those discussed earlier and a base market, and in a second step the Df S ( t ) are fitted using the spread market bonds. Each step follows standard fitting procedures as discussed in the next section.

Figure 19.7 shows examples of such splines for two Japanese sub-sovereign issuers. Despite the low number of parameters 3 per issuer), the spread splines reflect the issuer yield curves with reasonable accuracy because the main interest rate dynamics are captured in the base JGB spline.

FIGURE 19.7 Spread splines ( k = 2) calibrated to the 1-10Y bonds issued by the Tokyo Metropolis and Chubu Electric based on the 1-10Y JGB Nelson-Siegel-Svensson spline for 24 January 2019. Source: Data from JSDA.

<!-- image -->

## 19.5 FITTING CURVE MODELS

Fitting a curve means finding the set of parameters for a given parametric curve that minimises an appropriately defined error term relative to market data.

When the market data consists of bond prices, the most common approach is to fit bond yields, by defining the error term E as:

<!-- formula-not-decoded -->

where y i are the market and y model i the model-implied yields. Model-implied yields should not be simply taken as the par yields given by the model but be calculated from model prices coming using the actual cashflows of each bond and the model-implied discount factors:

<!-- formula-not-decoded -->

where the summation index j runs over all future cashflows of bond i . Note that the resulting price in this equation is a dirty price.

Given that, for small price changes, yield changes are well approximated by the DV01 of the bond ( ∆ y = ∆ P ∕ DV 01), the error term above can be approximated as:

<!-- formula-not-decoded -->

While this may seem like a trivial mathematical trick, it has in practice a significant computational impact. Calculating a yield from a given bond price is a costly operation because it involves a non-linear root search. Most parametric curve models, especially the exponential spline model, can calculate model-implied prices very fast from the bond cashflow structures. Using DV01-weighted prices to derive the error term is therefore usually several magnitudes faster than using yields.

Some applications, including the ECB spline curves, use outlier removal techniques. After minimising the error term Equation (19.31), individual spline spreads are evaluated and bonds that more than a certain number of standard deviations, or more than a given number of basis points, away from their spline-implied yields are removed from the sample. A new fitting procedure is then conducted until the sample becomes stable. The obvious advantage of this approach is that it automatically deals with polluted price or bond static data 4 . The downside of outlier removal is that the comparison of spline curves from day to day will become tainted with sample changes. These are not always immediately obvious because increased noise can lead to an increase in the sample size when the outlier removal algorithm adopts a more lenient approach due to an increase in the observed standard deviation of spline spreads. In general, it is a bad idea to preserve tainted data and rely on post-processing to remove it. The better course of action would be to use outliers as suggestions for data that needs manual verification.

A related idea is the removal of bonds that are known to have distorted prices. This could be recently issued benchmark bonds, or futures contract CTDs. Such bonds can have sizeable repo or liquidity premia embedded in them, which makes them non-representative for the overall discount factor term structure. Again, there are arguments in favour and against such techniques. The main argument against removing bonds on the basis of systematic premia is that these tend to be the most liquid securities in the market. One could argue that their pricing responsed more to changes in economic factors than other bonds and instead of removing the benchmark, one might rather remove less liquid bonds from the sample. Also, it can be argued that the idea of a liquidity premium for the most active bonds is equivalent to an 'illiquidity discount' on the less liquid bonds. The 'true' discount factor curve is therefore somewhere between the curve formed by the most liquid bonds and that formed by the least liquid ones. While simply mixing all bonds equally in the sample recovers this 'true' curve is not obvious, but it should produce a closer result than either extreme.

4 It is often the case that data sources contain errors that are hard to spot in very large data sets. For instance, a given bond may be callable but not marked as such in the incoming data set. The market price of this call option will generate a larger deviation from the spline curve if the bond is included under the assumption that no call option exists. Another common problem is the distinction between unsecured and secured or guaranteed liabilities of the same issuer. Outlier removal would catch most of such instances, or cases where supposed market prices are simply erroneous. This is not to suggest that polluted data is the reason why the ECB is using outlier removal.