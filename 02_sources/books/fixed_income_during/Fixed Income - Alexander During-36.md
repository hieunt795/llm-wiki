---
title: "Fixed Income - Alexander During-36"
type: raw_source
source_pdf: "Fixed Income - Alexander During-36.pdf"
extractor: docling
---

<!-- image -->

## Portfolio Risk Management

## 35.1 RISK-NEUTRAL PORTFOLIOS

Aportfolio is a collection of assets that are managed for a common purpose. Assuming N assets, each held in a nominal amount of wi and a price (including accrued interest, where applicable) of P i , the total value V of the portfolio is simply the sum of its parts, i.e.,

<!-- formula-not-decoded -->

The essential idea of risk management is to minimise the sensitivity of V to instantaneous changes in so-called pricing factors. Essentially, one assumes that all asset prices are functions of certain variables v k :

<!-- formula-not-decoded -->

and therefore risk management consists of solving the problem:

<!-- formula-not-decoded -->

This task is not trivial, unless one allows for the pathological case wi = 0 ∀ i (the empty portfolio). To see why, assume the most simple functional form for Equation (35.2), namelythat the are N pricing factors and f i ( v 1 , v 2 , . . . v N ) = P i . In words, each asset price is itself a pricing factor or, equivalently, the price of each asset follows an idiosyncratic path. In this case /u1D715 V ∕/u1D715 v i = /u1D715 V ∕/u1D715 P i = wi and the only way to solve Equation (35.3) is wi = 0. Only an empty portfolio is completely riskless.

Somewhat less trivially, Equation (35.3) is a system of k equations and this implies that in a world with k pricing factors, a portfolio must contain at least N = k assets to allow a solution for Equation (35.3). For most institutional portfolios, N ≫ k so this is not a problem.

Even with sufficient degrees of freedom, 2 more problems arise. The first is risk stability. Equation (35.3) ensures that the portfolio will not change value in cases of an instantaneous, infinitesimally small shock to the pricing factors v k . This does not rule out that the values of the partial derivatives change through time of that asset prices are non-linear functions of the pricing factors. In either case, Equation (35.3) can be violated for an initially risk-neutral portfolio either through the passage of time or because pricing factors change. In option literature, the latter effect is known as /u1D6FE whereas in fixed income it is generally referred to as convexity.

For instance, if one treats the level of a given interest rate as a pricing factor, then the sensitivity of the bond price to that pricing factor is its DV01 1 . The DV01 declines as the bond ages and approaches maturity, so that the sensitivity of the bond price to rate changes declines. As discussed above, the DV01 of a bond also declines when interest rates rise (positive convexity). A risk-neutral portfolio involving bonds will therefore generally change its risk sensitivity over time and in response to interest rate changes. A portfolio manager aiming to maintain a given portfolio risk will therefore have to execute trades over to actively preserve that risk exposure.

In the sections on RMBS (page 297) and bond futures contracts (page 318), it was pointed out that these instruments can, in some yield configurations, exhibit negative convexity. These are extreme cases of changes in the risk sensitivities that will cause problems with hedges structured using Equation (35.3). This can be the result of an implicit, rather than explicit, equivalence assumption. A portfolio manager benchmark against a fixed-rate index can use mortgages as an alternative with better carry. However, matching the risk characteristics of the benchmark is then a challenging task.

The second hurdle to risk stability is that portfolio risk parameters do not only change due to the passage of time and convexity effects, but also in response to other market parameters; most notably, changes in FX rates. Portfolio managers are generally measured on their return in one currency (the home currency) but may hold assets denominated in other currencies. When currency valuations change, the portfolio exposure to the risk factors linked to those assets changes proportionally. The same is true for inflation-linked debt holdings which are in many ways mathematically equivalent to holdings in an inflation-free foreign currency. However, price index levels tend not to change as rapidly as FX rates. Such effects are part of a phenomenon known as cross-gamma. More generally, cross-gamma refers to second derivatives of price with two different independent variables. Standard gamma is simply:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where z is another variable, such as an FX rate, inflation index, etc.

Along-only portfolio is constrained to have strictly positive asset weights wi &gt; 0 ∀ i . Liability managers sometimes face the mathematically equivalent but opposite problem of a short-only portfolio wi &lt; 0 ∀ i .

The long-only constraint means that the existence of a solution to Equation (35.3) is only possible under certain conditions satisfied by the factor sensitivities /u1D715 V ∕/u1D715 v k . In

1 This argument neglects the term structure of interest rates for illustrative purposes.

whereas cross-gamma has the form:

particular, there must be assets that have opposite signs in their sensitivities to each factor:

<!-- formula-not-decoded -->

This condition is similar but not equivalent to a negative correlation between assets k and j . There is a mathematical apparatus that formalises these ideas ( M -matrices) but there is an additional constraint that needs to be respected in practical applications: The individual asset weights wi needto be meaningfully large, where 'meaningful' is defined relative to trading costs. It is therefore very hard to formulate a consistent mathematical framework around the practical constraints of long-only portfolios.

For fixed income assets, which with very few exceptions have a non-negative interest rate sensitivity, the condition in Equation (35.6) is practically impossible to satisfy. Long-only bond portfolios are therefore generally not risk-free. For equities, there can be opposing sensitivities to risk factors so that it is possible to a larger extent to construct low-risk portfolios in this manner. However, given that equity prices tend to be positively correlated (if only through the actions of investors who trade entire market indices through the futures markets), completely riskless equity portfolios are also unrealistic.

This leaves open the beguiling idea of portfolios comprised of multiple asset classes (bonds, equities, commodities, etc.) that employ relationships of the type in Equation (35.6) to achieve very low risk along all pricing factors. Such portfolios are sometimes marketed as all-weather portfolios.

## 35.2 INDEX TRACKING

Index tracking, index replication or passive investing is the idea of replicating a market portfolio more or less exactly. Index tracking has become very popular due to the failure of active portfolio managers to consistently beat their target benchmarks after cost. The argument has been made that all asset managers combined hold the market portfolio and therefore the average manager can only achieve the market return. For an investor whois unable to identify ex-ante which particular manager will outperform the market over the relevant horizon, it therefore makes sense to simply aim to buy the market portfolio in the cheapest possible way by investing with a low-cost passive manager whodoesnotspendanyresourcesonsophisticated asset selection strategies. The advent of exchange-traded funds (ETFs) has provided further momentum to passive investing because passive funds are easier to document in the listing prospectus. Note, however, that not every ETF follows a passive strategy.

It should be noted that the arguments in favour of passive tracking have some logical gaps, particularly in the area of bond markets. First, it is not true that all private portfolio managers in aggregate hold the market portfolio. Instead, substantial parts of the bond market are being held by investors such as central banks with very specific investment preferences. The part of the market that remains available to private investors has therefore a risk structure that is different from the total market structure. More generally, the idea of passive investing amounts to the assertion that an asset included in a given index should be bought because it exists. This is only true under the assumption that every asset if fairly prices given all publicly available information, i.e., the efficient market hypothesis (EMH). Even if one accepts this hypothesis as broadly accurate, there is a sleight of hand involved: Information has to be incorporated in market prices in some way, and the EMH is silent as to how this happens. In practice assets are fairly priced because over-priced assets will be sold by active investors acting on information received and analysed, depressing their market prices, while under-valued assets will be bought by such investors, inflating the market prices. Efficient markets, in other words, are not a given; instead, they result from active decision-making of at least a subset of investors. Such investors are unlikely to remain in the market for long unless they are able to derive returns from this activity. In a market containing only passive investors, mis-priced assets would never correct. This raises the question, to be tested in the future, of whether the rise of passive investing will increase the excess returns available to active investors.

In the case of equity indices with few, liquid constituents, such as the DAX 30, passive tracking can be achieved by simply buying each constituent equity in proportion to the index weight (see, however, the section on friction effects), in an approach known as full replication. For larger equity indices and bond indices, which generally contain hundreds or thousands of securities with varying liquidity profiles, index tracking is more challenging. Fund managers tend to opt for partial replication where the actual fund portfolio contains fewer securities than the index.

One can start with the stylised balance sheet of an asset manager purporting to replicate an index (Figure 35.2).

Before any investment has taken place, the asset side consists of cash while the liability side will always comprise of all securities in the index. This initial situation is equivalent to an active trading book where a trader has borrowed and sold short every security in the index. The task of the asset manager is now to replace cash on the asset side with securities and derivatives so that the porformance of the asset side mimics that of the liability side.

The easiest way to do this is to enter into a total return swap (TRS) on the index so as to transform the carry income of the cash holding into that of the desired index. This amounts to simply outsourcing the index replication task to the TRS provider and exposes the investors in such a fund to various risks, such as failure of the counterparty, or costs related to early unwinds of the TRS. Somewhat less trivially, the fund manager may be able to buy index futures (if they exist for the target index) and then only manage the roll process of these exchange-traded instruments. Both strategies are called synthetic replication. Synthetic replication with futures is commonplace in ETFs to avoid cash drag, explained below.

FIGURE 35.1 Asset-liability structure of a passive manager.

<!-- image -->

The bulk of passive investing is done through physical replication, however, which means that the asset manager buys actual bonds, equities, etc. to replicate the performance of the index. Typically, but not always, the assets in the replication portfolio will be part of the index. Including securities from outside the index universe is sometimes unavoidable, particularly when the index itself is not replicable, but some management mandates restrict the use of non-index securities.

Portfolio management essentially reduces down to three questions: Which securities should be in the portfolio?; How much of each security should be bought?; and, When should trading take place? Full replication of an index is fairly straightforward because the answers to these questions are trivial: buy all securities in the index, weigh each of them in proportion to its index weight, and trade whenever the index changes.

Partial replication is more complex because the first question becomes an optimisation problem. The more securities from the index are selected for the replication portfolio, the lower the performance divergence between tracking portfolio and index. However, more securities involve more trading costs, especially when the overall portfolio size changes, for instance due to fund inflows or redemptions. A portfolio manager will therefore strive to achieve a given tracking error with the minimum number of securities. Another systematic way of decribing this optimisation is finding a number of securities n so that the expected incremental trading costs caused by adding one more security exceed the expected reduction in tracking error gained by having n + 1 securities in the portfolio.

When the set of securities in the tracking portfolio is only a subset of the securities in the index, optimum tracking will normally also require that the relative asset weights in the portfolio are not proportional to the index weights. It is therefore also no longer obvious that trading should take place in response to changes in the index itself. Instead, trading might have to take place to restore some predetermined risk limits, which may be caused by a number of events not limited to changes in the index itself.

## 35.2.1 Factor Analysis and Spanning Sets

When one has decided on a factor analysis to risk modelling, which is the common course of action in equity portfolio management, then there is a mathematical tool at hand called a spanning set. A set of vectors r i , 1 ≤ i ≤ N is spanning a k -dimensional space ℝ k , k ≤ N if and only if for every e ∈ ℝ k ∃{/u1D706 i } ∶ ⃗ e = ∑ i /u1D706 i r i . Once one has chosen a k -factor model of the world, one can select a set of N ≥ k assets, measure their sensitivities to changes in each of the risk factors and verify that they form a spanning set. Note that correlations between the individual assets will reduce the effective dimensionality of their risk factors below their cardinality N . Once a spanning set is determined, the optimal weights of each asset can be determined, for instance through a Lagrange optimiser. The problem of replicating an index is therefore reduced to a three-step procedure:

1. Identify the relevant risk factors
2. Find a spanning set of assets that cover these factors, and
3. Calculate the optimal portfolio weights

The Lagrange formalism provides a set of linear equations that combine hard constraints with optimisation targets. In this case one would define the Lagrangian for assets i with weights wi and prices P i as:

<!-- formula-not-decoded -->

Here, the partial derivatives /u1D715 P i ∕/u1D715 f j are the factor sensitivities of asset i with respect to factor j and the first sum of the Lagrangian are the constraints that make the total portfolio sensitivity with respect to changes in factor j equal to the market sensitivity to that factor, here represented by F j . The second part of the Lagrangian is the optimisation target, here chosen to be the sum of squares of the deviations of portfolio weights from their market weights wi , scaled to include only the assets in the portfolio. This is essentially a soft liquidity constraint on the portfolio construction. While factor analysis alone does not prevent an outcome where the total sensitivity to a given factor is represented by exposure to one rare asset, this version of the Lagrangian would lead to a high cost assigned to such a portfolio. This liquidity constraint will only be satisfied to the extent that the /u1D6FD k constraints are satisfiable with reasonable, which usually means positive, weights. In essence, that amounts to a lower bond on N that is higher than the mathematical minimum N ≥ k . Higher N will in general lead to less extreme weights, and this formalism recovers market weights exactly when N is equal to the number of assets in the market.

As usual, the system of equations that determine the portfolio weights is derived by differentiating ℒ , i.e.,

<!-- formula-not-decoded -->

The resulting weights wi do, as has been hinted at, not necessarily match their market weights, or even achievable portfolio weights in the light of liquidity constraints. After they have been calculated, a useful cross-check is to verify that all weights are positive, and that the second term of the Lagrangian Equation (35.7) is indeed small. If that is not the case, then one can add other assets, or replace some of them, to try and rectify this problem.

In bond markets, the factor sensitivities would not, as in the equity world, be obtained by historical regressions. Bond risk characteristics change over time in a predictable way as a result of aging (cf. for instance Section 16.10). Historical regressions would capture the average state of this aging process in the past. Instead, the useful risk factors are yields, and the factor sensitivities are durations. Hence, a one-factor version of Equation (35.7) for bonds would naturally be:

<!-- formula-not-decoded -->

where D ∗ i is the duration of bond i and D ∗ m the duration of the market 2 .

More complex versions of Equation (35.9) could for instance compartmentalise the duration matching so that duration is not matched for the entire portfolio, but also for market segments, like 1-5Y, 5-10Y, etc., so that:

<!-- formula-not-decoded -->

where I ( c , i ) → ( 0 , 1 ) is an indicator function signalling whether bond i is in the maturity bucket c and the Dc are the weighted average durations of the market in bucket c . Note that, because the weighted average market duration equals the weighted duration of each bucket, Equation (35.10) recovers Equation (35.9) when the entire market is treated as a single maturity bucket. Portfolio managers tracking corporate bonds will in general be less concerned with curve risk than sector risk, so for them the split into sub-universes that should be duration-matched would be along industry sectors.

An interesting variation on this Lagrangian is to also change the optimisation term. Instead of using remaining degrees of freedom to tie asset weights to their market weight, one can add terms that systematically skew these weights. For instance, one could add a term that punishes high weights for expensive assets, where 'expensive' could be proxied by an appropriate spline spreads, or skew weights towards assets with high carry and rolldown. The algorithm would then systematically skew the portfolio towards higher ex-ante carry. Whether this leads to an actual outperformance, and whether the increased tracking error versus the benchmark that is induced by such skews is acceptable, are complex questions, and the answer depends very strongly on the market at hand.

## 35.2.2 Friction Effects

Portfolio management incurs costs, and the spanning-set approach to replication, leaves unhedged exposures to risk factors that are not considered in the construction of the spanning set. In practice, most portfolio managers need to hedge an additional risk, namely that of redemptions of fund shares.

2 Note that this expression implies that the wi are defined in market value, not nominal value, terms. This would be the usual case for a portfolio manager. For nominal weights, DV01 needs to be used instead of duration.

Index providers incorporate into the index level calculations some, but not all, of the frictional costs associated with index replication. For instance, coupon payments are not simply added to the daily index performance (which would imply that they are immediately re-invested in the index), but use a virtual money market account where such cash is accumulated and reinvested at the next index rebalancing date. Also, while bonds are usually evaluated on the bid side, newly added bonds are brought in on the ask side of the market pricing.

These calculation rules cover the cost of full replication in a reasonably frictionless market. Partial replication usually requires trading outside the rebalancing window and the associated costs are not included in the index calculation.

The largest hurdle to replicating index performance in most cases, however, tends to be the cost of holding cash, known as the cash drag. To give an example, the ECB's government yield curve on 10 June 2020 had a 5Y yield of -0.113 % . €STR on that day was -0.548 % , equivalent to -0.556 % in the actual/actual yield convention used for euro-area government yields. Assuming that a fund manager tracks an index with an average yield given by that 5Y yield, and can invest cash at €STR, then the cost of carry of cash held to match short-term redemptions is -44.3 bp ; i.e., the difference in yield between benchmark and actual return. A 5% cash balance would therefore translate into an underperformance of just over 2bps versus the benchmark.

In theory, an asset manager could run a 0% cash balance and pay any redemptions byborrowingcashintherepomarketagainstportfolioassets. To the extent that outflows are not compensated for by near-term inflows, the manager could close out the repo transaction with cash raised from an actual asset sale. While attractive in theory, this approach is illegal in most jurisdictions because it means that the manager is actually leveraging the portfolio. If outflows were to continue over some time in an environment of declining asset prices, this repo strategy would imply increasing losses for investors who keep their assets in the fund.

In practice, fund managers eliminate cash drag through the use of derivatives. Equity, ETF usually contain equity futures to achieve 100% index exposure despite cash holdings.

A separate class of frictions concerns indices that are not actually investable. Such indices are now rare, but even supposedly investable indices may in practice be difficult to replicate. For instance, broad bond indices in Japan are hard to replicate with new cash because secondary market liquidity of spread products (corporate bonds and municipal debt) is poor. The same is true for some broad European indices. Fund managers receiving fund inflows tend to find it hard to source older bonds, and so tend to have to accept higher tracking error risks to match the index carry.