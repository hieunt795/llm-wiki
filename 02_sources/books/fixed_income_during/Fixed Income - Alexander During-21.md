---
title: "Fixed Income - Alexander During-21"
type: raw_source
source_pdf: "Fixed Income - Alexander During-21.pdf"
extractor: docling
---

## CHAPTER 20

## Curve Analysis

T he preceding sections dealt with ways to represent curve shapes, and now is the time to consider why yield curves have the shapes they have. An insightful and influential series of papers by Ilmanen [49,50] broke down the drivers of the US Treasury yield curve into 3 categories, namely expectations, convexity bias and risk premia. It is prudent to add a fourth category, investor preferences (related to the preferred habitat concept in economics).

These4drivers will be discussed in more detail below but one statement can already be made upfront: While the aggregate result of them is the current shape of the yield curve, each individual component is unobservable. There are models that purport to be able to dis-aggregate yield curve changes into 2 or more of these drivers but such models generally rely on restricting the functional form of those drivers. The most commonly known such decomposition is the Fed's ACM model [2], named after the authors Adrian, Crump and Moench. It provides a separation of expectations from risk premia and this decomposition is available daily from the New York Fed. Like other such analyses, the decomposition is based on fairly restrictive assumptions of how risk should be priced, and those assumptions may not hold in practice. The general approach taken here is that, from time to time, one may be able to interpret a particular yield curve move as related to any of these 4 components, but mechanical quantitative decompositions should be treated with great care.

## 20.1 EXPECTATIONS

Market term interest rates should reflect expectations of future short-rate movements, and in most cases these will be related to central bank policy rate changes. Indeed, their influence on longer-term interest rates is an important factor in the transmission of monetary policy rates into the real economy. If no such influence existed, borrowers in the term fixed-rate market would not be affected by changes in monetary policy.

At the same time, expectations are unlikely to work over very long horizons. It is doubtful that the collective mind of the market has a concrete view on the monetary policy interest rate of the Fed or the ECB prevailing in 20 years, time. It is more reasonable to assume that very long-term expectations converge to some form of equilibrium rate like the Wicksellian natural interest rate [22,51]. This long-term neutral interest rate would then roughly correspond to the expected potential nominal growth rate of the economy. The expectations part of the term structure of interest rates should therefore be described by a path of short-term rates from their current levels towards this neutral rate. The Vasicek model introduced above contains the parameter /u1D703 that can be interpreted as such a long-run interest rate to which the short rate diffuses 1 .

If monetary policy is the driver of short-term interest rates, then economic developments as drivers of monetary policy can give some guidance of how the expectations component of the yield curve shape should behave. As a simple illustration one can use the original Taylor rule [79]:

<!-- formula-not-decoded -->

r is the target rate, p is the rate of inflation and y is the deviation of GDP from target. This rule can generate a term structure of the impact on interest rates from a shock to macro-economic data if one assumes that the economic data itself has a mean-reverting nature.

To do this, one can fit a standard VAR model to the historical observations of y and p , and consider the impact of a change in either on the future evolutions of these variables. This impulse-response function can be viewed as a simple model of the change in assumptions investors will make in response to learning of the most recent observation of economic data relative to their pre-release assumptions. Using the GDP deflator to describe the price level (instead of the core PCE deflator apparently preferred by the Fed), the impulse-response functions for a 1% shock to GDP and prices are shown in Figure 20.1 2 .

FIGURE 20.1 VAR model impulse-response functions of an assumed 1% shock to US GDP and GDP Deflator in Q4 2019. The models were calibrated to data from 1980 to 2019 and the lags are 4 for GDP and 2 for the deflator. Source: GDP data downloaded from FRED.

<!-- image -->

1 Indeed, the Vasicek spline is the simplest in a family of affine models that are based on such drift processes. The ACM model is also of this family.

2 Notethat such a large shock is unlikely in reality but the models used are linear so that the impact of a surprise is proportional to the size of the surprise. The calibration period for the VAR models

The two impulse-response functions look very different in that the inflation shock is much more persistent. This shock can now be translated into a response of par interest rates by integrating the adjustment to the policy rate r in the Taylor rule Equation (20.1) mandated by these shock responses of the two macro variables. Using a US Treasury spline curve from February 2020, the par rate changes resulting from changed expectations under these assumptions is shown in Figure 20.2.

Achange in growth expectations should be mostly reflected in the steepness of the front end of the curve (for instance, the 2Y-5Y spread), driven by changes in front-end yields. The inflation shock is more persistent but the increasing PVBP of longer bonds reduces the impact of this persistent response of policy rates on the par curve. Still, one could conclude that changes in the inflation outlook should lead to movements all along the curve.

Although the analysis is done here in terms of the quarterly real GDP and GDP deflator data, investors receive a multitude of other economic data releases that provide related information at higher frequency. For instance, growth estimates can also be informed by retail sales data, business confidence, new orders, unemployment and so on. Price developments are meanwhile visible in consumer prices, average hourly earnings, negotiated wage settlements, energy prices and the like. Not only are some of these indicators available at monthly frequency, but they arrive at different times so that growth and inflation estimates can be updated practically in real time.

This then raises the question why daily movements in the US yield curve, shown in Figure 31.9 on page 355, do not correspond to either of the two patterns shown in Figure 20.2. The main component of actual US yield curve changes is a nearly parallel movement of rates.

FIGURE 20.2 Projected par rate responses to a 1% shock to GDP and the GDP deflator using the 3 February 2020 UST Nelson-Siegel-Svensson spline for discounting. Source: GDP data downloaded from FRED, Treasury prices from TreasuryDirect.

<!-- image -->

has been chosen to be long, but not to include the oil price shock phase of the 1970s. Indeed, starting at 1980 means that some data predates the adoption of explicit inflation targeting in the US although the general idea of price stability was present before [9].

In the context of the expectations hypothesis, the prevalence of parallel curve shifts could be interpreted as meaning that investors assign a much higher degree of persistency to data surprises than is warranted by historical data. In addition, unlike the more sophisticated approaches taken in the modelling literature, no attention has been paid here to the difference between real and nominal returns.

However, these explanations retain the idea that investor decisions are based on constant long-term expectations. In other words, the modelling hierarchy assumed in the analysis so far has been that the long-term evolution of the economy remains the same, but that short-term surprises can occur, and these can have effects on asset prices:

<!-- image -->

In reality, it could well be that current data also affects long-run expectations. For instance, various market commentators do at the time of writing cite factors such as shifting demographics to justify expectations of a 'low for longer' outlook on interest rates. In this view, expectations could change not just for the near-term outlook on monetary policy rates, but the equilibrium level of the natural real rate of interest r ∗ . Additionally, monetary policy rates are being set specifically with a view to influence the macroeconomic variables used here to derive rate expectations. Investors face, not only uncertainty about the evolution of these variables, but also about the reaction function of the central bank, and the transmission of central bank actions into changes of economic activity. For instance, some central banks have debated the notion of an 'overshooting commitment', meaning that they will tolerate higher inflation for some time after periods of below-target inflation. Investors therefore need to reassess whether the Taylor rule Equation (20.1) remains a good guideline for translating changes in economic data into yield curve expectations.

Indeed, the calibration time period for Figure 20.1 has been chosen somewhat maliciously. Persistence of an inflation surprise should be associated with a central bank that is perceived as unwilling or unable to maintain price stability. A credible inflation targeting central bank should be able to reverse any shock to prices rather quickly, namely within the standard monetary policy horizon of 12 to 18 months. Comparing models calibrated to different periods of history, as in Figure 20.3, shows that the persistence of price shocks has indeed changed over time. Investors would therefore be unwise to base expectations on long historical horizons. Consequently, changes of models and their parameters should be as important to changes in expectations as changes in model inputs.

More broadly, it is no longer the case that macroeconomic surprises feed through to bond markets only through changes in the expectations for monetary policy rates. Central banks now use a variety of tools to affect yield curves directly beyond the front end [65]. Investors therefore now must translate incoming economic data into a variety of other market rates, such as spreads or long-term yields. Capturing a functional form for such expectations is practically impossible.

FIGURE 20.3 Changes in the impulse-response functions of the US GDP deflator through time. Each line represents the impulse-response function of a VAR model calibrated to two decades of data (1950-1969, 1970-1989, 1990-2009, 2010-2019). Source: GDP data downloaded from FRED.

<!-- image -->

## 20.2 CONVEXITY BIAS

Theexpectations hypothesis links the curve shape, and its dynamic, to changes in expectations for short rates. Convexity bias introduces an additional driver of curve shape, namely the volatility of interest rates. To understand this concept, it is useful to start with a butterfly position involving 3 bonds (this trade is explained in Section 31.1.3 on page 353):

<!-- image -->

Under normal circumstances, the weighted average yield, including funding costs, of the bullet (Bond B) is higher than that of the wings A and C in a duration-neutral butterfly. The weighted average convexity of this position, meanwhile, is negative. The negative aggregate convexity arises from the rapid increase in convexity of longer-dated cashflows relative to duration (cf. Figures 16.10 and 16.11 on page 166, 167).

As Section 16.9 pointed out, positive convexity means that re-hedging a durationneutral portfolio after yield changes will, subject to transaction costs, result in capital gains income, while re-hedging a negatively convex portfolio will result in losses when re-hedging. An investor would therefore normally not be willing to hold a negative convexity portfolio unless it provides some additional return. The idea of convexity bias is that the positive weighted average yield of the butterly reflects its negative convexity. In other words, the convex shape of the yield curve is the result of the non-linearity of the price-yield relationship.

This proposition can be tested by regressing the net yield of a butterfly on its convexity value. This has been done in Figure 20.4 for the US Treasury curve. Because the cost of holding a negative convexity portfolio is not only a function of the amount of negative convexity but also of volatility, the chart uses the product of negative convexity and implied volatility. For the history period shown there is indeed a good correlation in evidence. Since then, increased central bank activity around the globe has reduced both implied volatility (and thereby the value of convexity) and affected yield curve shapes.

Because the value of convexity is a function of how much a random walk deviates from its mean, the convexity premium c ( t ) is a function of the square root of maturity:

<!-- formula-not-decoded -->

Convexity bias is responsible for the inversion of the very long ends of most yield curves. At maturities beyond 25 to 30 years, expectations and risk premia reach nearly steady states while the convexity of bonds, and the value of that convexity, continues to increase. Most yield curve models have difficulties reflecting this effect, leading to an apparent over-valuation of very long-dated bonds. This apparent misvaluation is a shortcoming of the relevant model, not a real trading opportunity.

It should be noted that not every investor views portfolios relative to a duration target, and therefore assigns significant value to convexity. That does not mean, however, that such investors can ignore convexity bias. As long as a sufficient market influence is being exerted by convexity-sensitive investors, curve analysis has to respect this effect.

Convexity bias cannot be clearly separated from expectations because when central bank policy rates are perceived as being 'in play', implied volatility increases at the same time as policy rate expectations shift. Using the butterfly in Figure 20.4 as an example, the 2Y-5Y spread can increase because the market expects a rate cut (lowering the 2Y

FIGURE 20.4 US Treasury 2-5-10Y butterfly yield pickup as a function of convexity cost (net convexity times implied volatility) Jan 2009 to Jun 2010. The one-year spline rate has been used to approximate the net funding cost; butterfly rates are also par spline rates. Source: Treasury prices from TreasuryDirect, volatility VXTYN downloaded from FRED.

<!-- image -->

rate), and because higher implied volatility increases the implied cost of being short the 5Y in this butterfly. Delineating these two effects is practically impossible.

## 20.3 TERM RISK PREMIUM

The notion of a risk premium is relatively straightforward. As an example, one can consider a game where a player can wager 100 coins on a single toss of a fair coin. If the coin comes up heads, the money is lost. If it comes up tails, the player gets 200 coins. No rational person would participate in this game because the expected outcome is to have 100 coins. The player can achieve the same outcome by not participating and so avoid the risk of losing those coins 3 .

The game can be altered by raising the amount that can be won. If tails results in a payout of not 200, but 300 coins, it may be rational to wager the 100 coins for an expected profit of 50 coins. Of clear importance is the value of 100 coins to the total wealth of the player. The smaller this value, the readier the player should be to risk it for a small gain.

In terms of investment, one could imagine the following alternative game. An investor has the choice between investing cash for 1 or 2 periods of equal length. There is no difference in the expected interest rate of the second period versus the first. The market interest rate for the 2-period investment equals the compounded expected interest rates over these periods.

<!-- image -->

Again, an investor would be unwise to commit invested money for 2 periods on the expectation of earning the same as if the money was invested subsequently for the 2 periods in independent investments. Committing to the 2-period term investment amounts to foregoing the option of consuming, or investing in other ways, the money after the first period. The 2-period interest rate should therefore exceed the compounded expected interest rates of the 2 single-period investments. Otherwise investors should prefer to keep their money in 1-period investments.

This logic informs the Chicago school of economics, which models risk premia in terms of log-utility [23] and is therefore able to quantify risk premia exactly relative to expected returns and risks. This approach is also the basis of the risk/expectations decomposition of the ACM model. The merit of this approach is tied to the realism of the rational utility-optimising investor 4 . In addition, the choice of log-utility as the appropriate target quantity in some ways makes the risk premia so derived comparable to a convexity premium. This is because the functional shape of the risk premiumis tied to the convexity of the presumed utility function of the investor. If investor utility was simply a linear function of wealth, then risk premia in this approach would not exist.

3 Those not convinced by this type of argument participate in the various lotteries around the world.

4 In other words, those investors not participating in the various lotteries around the world.

In this world view, higher interest rate volatility should lead to higher term risk premia, and so to a steeper curve. This is indeed in line with market experience, but with a twist. At longer horizons, interest rate expectations should be affected by mean reversion, and so should longer dated volatility. Very long rates should therefore react less to higher short-term volatility then intermediate rates. As a result, one would look for a volatility dependency not on the 2Y-30Y slope, but on butterflies like the 2Y-5Y-10Y, as discussed in the previous section.

In many analyses, the expression 'risk premium' is used differently. Analysts tend to create fair value models of various kinds and then ascribe any deviations to risk premia. In essence, given a set of known variables (potentially including their histories) /u1D711 , one could construct a model of interest rates r and write the standard modelling equation:

<!-- formula-not-decoded -->

The measurement error term /u1D700 can then be considered a risk premium because it is that part of market pricing that is not explained by the model f (⋅) . This interpretation of course is dependent on the assumption that one's model is indeed the appropriate yardstick for the yield curve. In this sense, the term risk premium in this usage amounts to the things one does not know, or at least things not included in one's curve model.

## 20.4 PREFERRED HABITAT

The notion of a preferred habitat is that certain investors have a structural bias towards particular types of investment. The implication is that their demand for certain assets will not be explained by economic factors such as expected risk-adjusted return (i.e., risk premia) or expectations. It is useful to take a broad view of this effect, and this section outlines the most relevant of them.

The effects discussed here have one thing in common, namely that they cannot be hedged. Depending on one's understanding of risk premia and convexity bias, one can replicate their non-linear effects through the use of interest rate derivatives. Similarly, the interest rate effect of monetary policy expectations can usually be replicated through other financial instruments, such as equities or inflation derivatives. Preferred habitat effects, meanwhile, may be predictable but difficult to offset. Large-scale buying of long-dated bonds by pension funds is difficult to offset by other means given that the activity of these funds may be large.

## 20.4.1 Asset-liability matching

Most financial institutions have a well-defined liability structure and choose assets with a view to matching these liabilities. This asset-liability matching (ALM) approach is not a strict necessity because similar effects could be achived through the use of derivatives; potentially, however, at a higher cost. For instance, retail banks tend to fund a large part of their balance sheet with deposits. The economics of deposit interest rates are a balance between their cost, which incentivises banks to offer lower rates, and their supply, which means that banks need to pay enough to prevent customers from pursuing other investments, including deposits at competing banks. The latter aspect links bank deposit rates to board market interest rates, and so to monetary policy rates. Banks therefore are natural investors in floating-rate notes. In some countries, such as Italy, an ecosystem has evolved where the sovereign issued floating rate notes (the CCTS) and banks absorb a large part of this supply.

Many insurance companies have long-dated liabilities linked to life insurance that in many cases have defined yield floors. Although the entire asset mix of the investment portfolio is designed to earn at least this guaranteed income, some life insurance companies aim to purchase long-dated bonds if and when their yields rise above this guarantee rate. This approach is known as target buying. In this case, the preferred habitat of these companies is the set of bonds that has the necessary yield, not one particular sector of the yield curve. This can have effects on yield curve shapes. For instance, the JGB market sometimes exhibits a fairly predictable steepening or flattening behaviour at the long end (e.g., the 20-30Y spread) as life insurance buying in effect caps interest rates in times of slow interest rates. As soon as yields in any one sector reach their yield targets, demand for JGB increases and prevents further yield increases. The long end of the curve then bear-flattens or bull-steepens. Figure 31.6 on page 352 shows this effect.

In the US market, mortgage convexity hedging has a comparable effect. Holders of large RMBS portfolios generally attempt to maintain a steady duration risk in their portfolio. When interest rates decrease, mortgage prepayment risk increases and RMBS durations shrink. Mortgage hedging then requires the purchasing of US Treasuries, which has the effect of depressing yields further. Conversely, rising interest rates lead to longer mortgage durations, and US Treasury selling from the same type of investor. Whether the effect of this activity is large or not depends on how the mortgage coupons in the market are distributed relative to new production coupons. An interest rate level that leads to large-scale mortgage hedging is known as a convexity trigger. It should be noted that the prepayment option of a callable mortgage is an option that financial markets have sold to the mortgage borrower. Financial market participants can trade options between themselves but such trading does not change the aggregate negative convexity position of the market as a whole. Convexity hedging is the only other alternative for the market to buy back this option, namely dynamic replication.

## 20.4.2 Regulatory constraints

The preferred habitats described above amount to more or less voluntary behaviour of some market participants. In addition, there are regulatory reasons for some investors to make investments which then influence market prices.

Thelargest such sector in the European fixed income markets is the pension system, particularly in Denmark and The Netherlands. Pension fund regulation has undergone several transformations over the last decades and moved along one axis in particular. Because pension funds invest for very long horizons, one could take the approach that over such long time spans, asset returns should mean-revert. The appropriate way to regulate such funds would then be to make some actuarial assumptions about longevity and compare the assets held by a fund to its future obligations. The alternative approach is to be agnostic about mean-reversion of returns and instead demand that a fund has sufficient assets to cover liabilities discounted at current market rates 5 . An intermediate approach is to assume mean reversion in the very long run, but to use market rates in the short to intermediate sector. This is known as the ultimate forward rate (UFR) approach where forward rates beyond a certain horizon (chosen as the end of the 'liquid' part of the yield curve, however defined) are assumed to converge to a constant 6 . Discounting liabilities with market interest rates means that pension funds need to hedge againt interest rate risk. The most straightforward hedge, namely a fixed income asset portfolio that exactly matches the liability, is unattainable in the market. Some governments are large enough borrowers to create a sufficiently large long-dated bond portfolio but have for cost reasons not chosen to do so 7 . In addition, because pension funds are long-term investors, it makes sense for them to hold riskier assets such as equities, real estate and commodities and so earn the associated risk premia. As a result, pension funds tend to see the values of the liabilities increase relative to their assets when interest rates fall, andarethensometimesforced to reduce their duration gap through buying bonds when yields fall. In this sense, pension fund regulation, combined with the structure of the bond market, imposes a form of short convexity on pension fund managers.

## 20.4.3 Passive investing

Investors with no leeway over their investments, such as Exchange Traded Funds (ETF) are a special form of preferred habitat investors where the preferred habitat is the entire market that the ETF is linked to. For risk management reasons and because they are not incentivised to to so, such funds are unable to under-invest in overvalued sectors, or over-invest in undervalued sectors. Although such behaviour is ostensibly passive, it can affect relative pricing. Bond indices are not free-float adjusted and ETFs therefore need to achieve market-weight exposures even in yield curve segments where other preferred habitat investors create excess demand. ETF demand can then amplify the relative shortage in such market segments.

Passive portfolio re-hedging is also responsible for large-scale trading activity at the points in time when index rebalancings become effective (usually the market close of

5 It should be noted that this does not amount to a rejection of mean-reversion, but simply to the assumption that current market rates incorporate the best estimate of the economic value of such a mean-reversion.

6 Douglas Adams, had he still been alive at the time, would undoubtedly have felt vindicated by the choice of 42 % as the answer to the question about the ultimate forward rate in The Netherlands in 2012. That being said, the Dutch UFR has been revised since then (to 3.9%) which calls into question what the economic rationale of the UFR is. To be logically self-consistent, an ultimate forward rate should be constant.

7 Aside from the argument about government funding costs, it should be borne in mind that a funded pension system holding only domestic government bonds is redundant. Because the government bond coupons that feed into the pension system would then be funded by taxes, it would be more efficient to eliminate the cost overhead of pension funds and make tax transfers to pensioners directly.

the last trading day in a given month). This rebalancing is not uniformly distributed across the market and instead requires the purchase of newly issued securities and selling of newly excluded securities. However, such trading is to some extent predictable and therefore arbitraged across time.

## 20.4.4 Central bank reserve portfolios

Some central banks hold large-scale foreign currency portfolios designed to be liquidated quickly when required. Such sales can be required when a country faces a sudden capital outflow or a drastic fall in the value of its own currency 8 . Reserve portfolios can be built in various ways, but tend to result from times when the opposite problem occurred (excessive money inflows and currency appreciation). As a guide to sizing and structuring such a portfolio, a country may examine its import-related external payments and attempt to match them with a reserve portfolio that allows it to fund these outflows from maturing reserve assets, asset sales and repos. Large internationally connected financial systems can create the need for additional reserves.

To ensure the ability to intervene rapidly, reserve portfolios need to be liquid and do therefore generally not carry much duration risk. The preferred habitat of a reserve portfolio is therefore the short-dated sector of highly rated bonds denominated in the international trade invoice currencies, such as US dollars, euros and yen.

Note that not all foreign assets held by sovereigns are held for FX intervention purposes. Some sovereigns have sufficiently large assets to invest a large part of them with a view to earning returns. In such investments, preferred habitats play a lesser role.

## 20.4.5 Market technicals

Markets do not always work perfectly and local supply-demand imbalances can lead to price distortions. These effects are known as market technicals. Such technicals can take various forms. For instance, when sovereigns offer post-auction non-competitive allocations, the price at which these allocations happen can act as a temporary anchor of prices around the time of allocation. Option trader positions can force them to buy or sell in a way that may amplify or dampen market volatility [77].

Aside from these effects, which are localised and reasonably well understood, there is a cottage industry of technical analysis which purports to be able to predict future market movements from historical prices more generally [61, 63]. Various theories are proposed why past prices should be sufficient for prediction, such as investor psychology and supposedly special numbers. Technical analysis has the hallmarks of a cargo cult, with its own language of resistance and support lines, retracement levels and the like. Multiple schools exist that follow diverse signals such as Fibonacci levels, Japanese candle sticks and market pictures. The large amount of financial data means that a large number of supportive examples can be found for every rule. However, no systematic analysis of false positives exists and some concepts defy common logic. For instance, given the close relationship between yields and bond futures prices, any 'special' level in yields should correspond to a special level in futures prices. Because the CTD of bond futures contracts often changes between deliveries, the yield-price relationship also changes, but this is not reflected in technical analysis.

8 Usually both types of event are connected.

While one might disagree with technical analysis on this basis, there is a possibility that it can become self-fulfilling. If a sufficient number of investors believes that a given price is a support level, they can end up buying at that level in sufficient volumes to indeed make that price level act as a floor. For this reason it can be useful to be aware of the outcome of technical analysis even though the analysis itself is based on questionable arguments.