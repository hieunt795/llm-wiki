---
title: "Fixed Income - Alexander During-39"
type: raw_source
source_pdf: "Fixed Income - Alexander During-39.pdf"
extractor: docling
---

## CHAPTER 38

## Portfolio Rebalancing

A n existing portfolio can at any time be adjusted. Such adjustments may become inevitable due to certain events, such as cash or equity distributions, occurring in any of the assets in the portfolio. This creates definitional problems around simple questions such as that of portfolio performance.

Consider the following simple question: Given a portfolio worth 100 invested in equal amounts in 2 assets A and B, where A has an expected return of 3% per year and B has an expected return of 5%, what is the expected value V of the portfolio in 5 years? Which of the following answers is correct:

<!-- formula-not-decoded -->

The correct answer is that all 3 formulas could be correct. In fact there is an infinite number of correct answers until one properly defines the strategy followed to invest asset returns. The first formula above is appropriate when any gains are extracted and held in a zero-return asset like physical cash. The second formula is correct when gains are collected on an annual basis and reinvested to re-establish the original 50%:50% portfolio mix. The third formula is accurate when any gains are reinvested in the asset they originate from. Note that in this third scenario the portfolio weight of asset B would be around 52.4% at the end of the 5-year period, while the weight of A would be only 47.6%. This example shows that portfolio rebalancing is an essential determinant of portfolio performance, and the calculation of portfolio performance depends on the rebalancing strategy.

Portfolio rebalancing is the adjustment of asset holdings wi in response to certain events or on a periodic basis. The purpose of this chapter is to highlight that the choice of a portfolio rebalancing strategy implies a certain assumption about the autocorrelation structure of asset returns. In other words, the optimal rebalancing strategy depends on the correlation structure of the assets involved.

Thefirst rule taught to traders tends to be 'cut your losses short, let your profits run'. The purpose of this rule is to avoid emotional attachment to particular trading views. What is interesting is that this strategy is, as will be shown below, halfway between a no-rebalancing and a constant asset allocation strategy.

## 38.1 PASSIVE AND SEMI-PASSIVE STRATEGIES

## 38.1.1 No Reallocation

The no-reallocation strategy is to simply buy a portfolio and never revisit the asset allocation at all. Incoming cash is assumed to be reinvested in the asset class it originated fromorconsumed.Astimepasses,theweightofunderperformingassets in the portfolio declines because the better performing assets form a larger share of the total portfolio value. The adoption of this strategy amounts to some faith that the market valuations are rational and that it is indeed beneficial to be more exposed to assets that have performed well in the past.

The analytical drawback of this strategy, which also invalidates this theoretical argument, is that it is not time-invariant. The weight of each individual asset in the portfolio depends on the performance since the inception of the portfolio and therefore on the precise point in time when the portfolio was established. It is very unlikely that the future performance of assets should be dependent on the precise date when a given portfolio was established. Therefore, while past performance may sometimes be a good guide to future performance, expressing this view through a simple buy-and-hold strategy is likely to be suboptimal.

## 38.1.2 Passive Management

Passive management means that all assets are purchased in proportion to their outstanding amounts, or market weights. Portfolio rebalancing is only necessary to the extent that new assets appear in the market, that existing assets disappear, or that cash distributions from existing assets (coupons or dividends) need to be reinvested. Rebalancing is done periodically; usually monthly for bond portfolios. Given that several commercial data providers offer the service of collating the relevant information in the form of market indices, this type of strategy is also known as index tracking. Unlike the no-reallocation strategy above it avoids the problem of time-invariance and all passive portfolios targeted at a given asset universe with identical rebalancing periods have identical asset weights.

Passive management has a number of attractions. The most important one is cost: the analytical cost of following a market index is virtually zero and the only costs involved in running an index-tracking portfolio are transaction costs and custody feeds.

Apurported second attraction is more theoretical. All assets in the market need to be held by somebody, and so the the idea that one investor holds more than the market weight of a given asset due to some superior insight into the future performance of that asset implies that another investor holds less than the market weight of the same asset, presumably also on the basis that this other investor expects an underperformance. Clearly, one of these 2 investors must be wrong, and averaged over many investors and over time, every investor will be right as much as they are wrong and every portfolio will more or less follow the market performance. A theoretical underpinning of this idea is the efficient market hypothesis (EMH) which in essence postulates that asset prices reflect at all times all available information.

Theproblemwiththisideaisthat it makes several assumptions about the behaviour of all other investors in the market. These are in particular that all of them are unconstrained and rational in their investment decisions, and that they can react to incoming information at the same time. While the rationality assumption may be correct, some investor classes are clearly constrained in what investments they can make at any one time, and some investors cannot time their investment decisions optimally. Essentially, the idea that passive investment is rational amounts to relying on the rationality of all other investors to justify not undertaking independent analysis.

## 38.1.3 Index Replication

Perfect passive management is impossible due to liquidity constraints. Assets may exist in the market but be held by investors unwilling to sell, and managing a portfolio consisting of thousands of securities would require trading in minuscule quantities. Meanwhile, most portfolio managers need to manage cash inflows and outflows as investors put more money into a fund, or ask for redemptions. In practice, the strategy of passive investing means constructing a portfolio that mimics the performance of a market index as much as possible while consisting of only a manageable number of assets and preserving sufficient liquidity to manage redemptions. Portfolio assets also may or may not be part of the market index itself 1 if investment policies allow for such deviations.

The construction of an index-tracking portfolio introduces a new problem, namely that the actual portfolio will be exposed more to the idiosyncratic risks of the assets that are in the portfolio and not to the idiosyncratic risks of the assets that are in the index but not held by the portfolio. This means that the choice of the number of assets in the tracking portfolio, and the selection of the actual assets is an essential risk management consideration. Index replication is therefore not a purely passive investment strategy. Instead, the asset manager must make decisions as to the construction of the replicating portfolio, usually under the constraint that simply holding the index portfolio is practically impossible.

At the same time, the obligation to track an index can be seen as equivalent to holding a short position in the entire index portfolio. The hedge for this short position is the long position in the tracking portfolio held by the asset manager. This means that the asset manager is a natural relative value investor. Given that index performance calculations generally only consider the return on the index constituents but not their financing costs, there is usually a clear arbitrage opportunity created by the variability of repo rates applicable to different index constituents.

## 38.1.4 Constant Asset Allocation

Constant asset allocation is a strategy that consists of periodically rebalancing the portfolio to achieve a given allocation to the constituent asset classes. Assets that have increased in portfolio weight through outperformance are sold to purchase more of those assets that underperformed and therefore saw their weight in the portfolio decline. It should be stressed that this approach amounts to periodically selling the best-performing assets in the portfolio and using the proceeds to buy more of the worstperforming assets.

1 For instance, the German REX government bond index is practically uninvestable due to the pecularities of its construction. Managers replicating this index therefore routinely invest in covered bonds (Pfandbriefe) to achieve the desired performance.

Unlike the no-rebalancing strategy, this approach leads to an asset allocation that is independent of the inception date of the portfolio.

The issue of rebalancing is particularly pertinent for portfolios consisting of assets denominatedinmultiple currencies due to the high volatility of exchange rates. A global equity portfolio managed to achieve a given asset allocation in euros might find itself selling dollar-denominated equities after a dollar appreciation even when these equities underperformed in dollars. A domestic fund in the US following the same strategy might therefore buy these same assets due to their dollar-based underperformance. It is not immediately clear which of the two funds takes the correct stance with regard to the asset class because their opposite actions are driven by changes in the exchange rate.

## 38.1.5 Trend-Following

Trend-following is a term for active management strategies that overweight assets that have shown an above-average performance and underweight underperforming assets. The rationale for such strategies is the positive auto-correlation of asset returns in subsequent periods observed for most assets. Trend-following can be seen as an amplified version of the no-rebalancing approach in that the weight of outperforming assets in the portfolio increases not just through the value gain of these assets, but also through additional purchases of these assets that are funded by sales of underforming assets. Trendfollowing is the usual investment model ascribed to a particular type of fund known as commodities trading advisors (CTA) which is a catch-all term for fund managers that operate in futures markets with a minimum of own capital.

Trend-following strategies are sometimes blamed for exacerbating market distortions because they create extra demand for assets that rise in price while selling assets that fall in price. When markets are inefficient, this is a valid concern when trendfollowers are sufficient in volume to affect price formation. The catch with this accusation is that market inefficiency is not always easy to prove.

Perhaps more pertinently, trend-following strategies rely on the investment choices of others to determine their own trading strategy. As such, they may be active in nature, but are passive in their actual decision-making.

## 38.1.6 Mean Reversion

Meanreversion strategies are the natural opposite of trend-following strategies. Instead of overweighting outperforming assets, they underweight these assets in anticipation of asset returns reverting to their mean. Such strategies are sometimes called contrarian because they appear to run counter to current market sentiment. However, just as trend following strategies use past asset returns to guide future investment decisions and are therefore essentially passive, mean reversion strategies do not require fundamental analysis of the assets involved.

In practice, the inverse relationship between trend-following and mean reversion strategies is not perfect. Both strategies involve 2 principal time scales. First, the comparison of recent performance to trend requires the definition of the interval over which trend performance is measured. Second, the adjustment of portfolio weights in practice takes some time and this defines a time scale over which portfolio weights adjust to the moving targets defined by the strategy itself. It is in principle therefore possible for a fund manager to be both trend-following and mean-reverting at the same time, as long as the 2 timescales are sufficiently separated.

## 38.2 NUMERICAL EXAMPLES

The previous section has hinted that supposedly passive investment strategies like constant weights and no rebalancing can be understood to express views on the auto-correlation of asset returns. Given that active strategies like trend-following and mean reversion explicitly take views on the same auto-correlation properties, it is useful to compare the performance of these strategies in the controlled environment of simulations where mean reversion of asset returns can be set externally. Real world probability distributions have time-varying parameters that can obscure the contribution of the asset allocation strategy to the observed portfolio return.

The examples here are use a set of 3 assets which are intended to be identified with, for instance, bond, equities and cash. They have returns that follow a mean-reverting process in discrete time:

<!-- formula-not-decoded -->

The stochastic process w has zero mean and the covariance matrix M = w T w is constant. To be consistent with the capital asset pricing model (CAPM), the mean return of each asset is defined to be proportional to its variance:

<!-- formula-not-decoded -->

For illustration, Asset 3 has a low volatility while Assets 1 and 2 are more volatile. The main parameters that are used to show the effects of changing asset return characteristics on the performance of particular asset allocation strategies are the mean reversion speed /u1D706 and the covariance of the 2 most volatile assets /u1D70E 1 , 2 . One sample price path for each asset is shown in Figure 38.1 for 4 different combinations of strong or weak mean reversion, and positive or negative correlation between the innovations w .

The assets can be combined in a portfolio where each of them has a time-varying weight wi , t with the constraint ∑ i wi , t = 1. For illustration, all weights are assumed to be equal at the inception of the portfolio wi = 1 ∕ 3. The next step is to then assume that portfolio managers apply one of 4 possible illustrative asset allocation strategies during a monthly rebalancing: No rebalancing, fixed weights, mean reversion, or trendfollowing. The mean reversion strategy implements a gradual decrease in the weight of an asset that exceeded its average return over the last period:

<!-- formula-not-decoded -->

FIGURE 38.1 Asset returns for 4 different settings of mean reversion and covariance. Top row: fast mean reversion, bottom row: slow mean reversion. Left column: positive covariance, right column: negative covariance. Time is assumed to be in years with monthly returns.

<!-- image -->

subject to w ′ i , t &gt; 0 and after calculating all w ′ , the weights are renormalised to 1:

<!-- formula-not-decoded -->

The trend following strategy implements the exact opposite approach by overweighting assets that outperformed:

<!-- formula-not-decoded -->

Note that the only difference between Equations (38.3) and (38.5) is the sign before the strategy sensitivity parameter k .

Portfolio performances are caculated in the usual way, i.e.,

<!-- formula-not-decoded -->

Figure 38.2 shows the outcome of 1 simulation path per choice of mean reversion and correlation between Assets 1 and 2. The asset return series are the same for each strategy, so the portfolio performance is only a function of how well the strategy performs for a particular type of covariance structure. The outcomes are somewhat as expected. For weak mean reversion, trend-following pays off and this strategy performs better than its logical opposite, the mean reversion strategy. The difference in outcomes is a function of the covariance between the 2 series. For a negative covariance, there is more of a difference between being invested in one asset versus another, and therefore asset allocation decisions are more decisive for the overall outcome.

FIGURE 38.2 Portfolio performances of 4 different asset allocation strategies for different assumptions on asset returns. As in Figure 38.2, top row: fast mean reversion, bottom row: slow mean reversion. Left column: positive covariance, right column: negative covariance.

<!-- image -->

These examples give a flavour of the topic of dynamic asset allocation. Although the limitations of mean-variance optimisation for single-period investment analysis are there, the idea of systematic strategies that incorporate auto-correlation provides a natural extension. Of course, correlations change over time, and so do optimal strategies. As highlighted in Section 20.1, the expectations on central bank reaction functions do, and should, change over time. This should affect investors' asset allocation decisions.