---
title: "Fixed Income - Alexander During-38"
type: raw_source
source_pdf: "Fixed Income - Alexander During-38.pdf"
extractor: docling
---

## CHAPTER 37

## Mean-Variance Optimisation

T he simplest framework in which to analyse and optimise portfolio performance is to consider only a single investment period. By implication, this means that autocorrelation of asset returns is irrelevant. If one further assumes that asset returns are normally distributed, then the only 2 parameters describing portfolio returns are the expected return and the uncertainty around this return, i.e., the risk of the portfolio. The idea of optimising the balance between return and risk is therefore equivalent to optimising the mean and variance of the expected portfolio returns. The presentation here follows essentially [56].

Given the expected returns m and the covariance matrix V of a portfolio with asset weights w , return and return variance of the portfolio are:

<!-- formula-not-decoded -->

In the following, 2 related examples are used. They use 3 hypothetical assets which have the same expected returns in both examples but different covariance matrices. Two of the assets are supposed to represent riskier investments while the third is a close cash equivalent. The expected returns are:

<!-- formula-not-decoded -->

while the 2 covariance matrices are:

<!-- formula-not-decoded -->

Although the variances of the 3 assets are the same in both covariance matrixes, the first one has positive correlations between the returns of the 2 risk assets while the second has negative correlations. The expected return of each asset in these examples is related to its riskiness which should also be the case for actual market assets. The expected return on the third asset is close to the risk-free rate which is here assumed to and:

FIGURE 37.1 Expected portfolio returns and variances for different asset weight combinations. The left-hand chart is for the positive covariance matrix V P , the right for V N . The convex hull of each set of risks and returns is labelled 'Efficient frontier' and the tangent on that line through the riskless asset as the capital markets line (CML).

<!-- image -->

<!-- image -->

be 0.5. For now, portfolios are assumed to be constrained to full investment across the three assets and no borrowing, which translates into:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

There is an infinite number of possible portfolio combinations, even with these constraints. Selecting a regular grid of weights from the possible ranges and calculating the expected portfolio returns and risks results in a data set that is known as the 'Markovitz bullet', shown in Figure 37.1.

Both data sets share the same minimum risk point which corresponds to a portfolio consisting only of the least risky asset. Beyond that, there is a clear difference in the 2 expected risk and return distributions. Negative correlation between assets increases the chance that negative returns in one asset are compensated for positive returns in another. As a result, the negative correlation portfolio shows higher returns for the same risk. Put differently, a positive correlation between the 2 risk assets makes them partial substitutes which is why for a given amount of risk, there is a lower dispersion of returns in the left data set where the risk assets are positively correlated.

Aportfolio (set of asset weights) A is said to dominate a portfolio B if A has a higher return than B but the same risk, or if A has lower risk but the same return. In the geometry of Figure 37.1, A dominates B if it is above B or left of B. For an investor, A would always be preferable to B. From this it follows that the convex hull, i.e., the points forming the boundary of the data set, of the set of possible risk and rerun combinations has a special meaning for portfolio allocation. Every portfolio inside the convex hull is dominated by 2 portfolios in the hull, namely a portfolio to the left (lower risk but same return) and 1 above it (same risk but higher return). This means that only portfolios in the hull, and specifically those in the upper part of the hull, are sensible investment allocations. These portfolios are said to form the efficient frontier of the set of assets available for investment. Constructing an investment portfolio therefore amounts to picking the desired spot on the efficient frontier.

If restriction Equation (37.4) is relaxed, the investor can invest in the riskless asset or borrow the riskless asset to invest more. This provides a special meaning to the point where a line through the riskless asset return forms a tangent on the efficient frontier. The tangent is marked as the capital markets line (CML) in the chart. An investor can hold a combination of the riskless asset and the portfolio corresponding to this tangent point on the efficient frontier. The tangent itself then denotes all the risk-return combinations that are possible with such a combined portfolio. All points of this line to the left on the tangent point represent partially invested portfolios, where some of the investment is held in the riskless asset, while all points to the right correspond to portfolios where the riskless asset has been borrowed to invest more in the risk assets. Because the efficient frontier is convex, every point of this tangent represents a portfolio that dominates every other point on the efficient frontier.

This concept of mixing the riskfree asset with risk asset portfolios is related to the Miller-Modigliani theorem according to which, in the absence of taxes and frictional costs, an investor can choose to adjust any investment to his or her risk preference by choosing to hold the riskless asset or borrow. The risk-return choices of the manager of the risk asset portfolio should therefore not depend on that of the investor. This idea has an important implication for the meaning of this tangent point.

With a certain amount of handwaving, this tangent point is known as the market portfolio where every asset is held in direct proportion to its market weight. This handwaving is best explained in an indirect way and relies on what is known as the efficient market hypothesis (EMH). To begin with, it should be recalled that all assets are held by somebody. If it was possible to identify a market asset that should be held below its market weight, investors should underweight this asset. Such underweighting will lead to a surplus of supply over demand and will lead to a lower price of the asset which will increase its future returns. Conversely, prices that should be held above their market weight will see a surplus of demand over supply, leading to a price increase and lower future returns. This means that eventually all future returns should adjust, via an adjustment in market prices, so that holding the market portfolio becomes the optimal asset allocation. The Miller-Modigliani theorem then makes the optimality of this portfolio independent of investor risk preferences because those can be expressed through the split of investment between the riskless asset and the market portfolio.

There are several problems with this argument and the main one is crytallised in the preconditions of the Miller-Modigliani theorem. In the real world, taxes and friction costs do exist. These mean that investors are unable to simply hold the market portfolio and achieve the correct risk preference via allocation to the riskless asset, and in particular when this involves borrowing it (cf. the introduction to [20]). Instead, most investors face frictions that restrict their investment choices. Few investors can access every global market at the same cost. They are therefore more likely to skew portfolio allocations towards assets that are more easily accessible, which means that it is unclear what the market portfolio actually is. It is therefore optimistic to assume that relative returns adjust in order to make every conceivable market portfolio optimal. To give another example, General Motors, the car maker, underwent a Chapter 11 restructuring in 2009. As part of that restructuring bond holders received equity in a new post-restructuring entity. The EMH implies that this event shifted the optimal portfolio allocation for every investor in the world from bonds towards equities.

While the EMH may have some conceptual arguments against it, there is an alternative way to interpret the capital markets line. If investors are unconstrained in their investment decisions, then the return r they demand for investing in an asset with volatility V should be a function of V :

<!-- formula-not-decoded -->

One can then approximate f (⋅) through a Taylor series around the point marked by any given portfolio, and there is no reason not to use the market portfolio with its volatility Vm and expected return rm as a reference point. Specifically,

<!-- formula-not-decoded -->

TheCMLcanthenbeinterpreted as the second, linear, term of this series, while the first is the expected return rm of the market portfolio. This interpretation does however not explain why this CML should coincide with the expected return on the riskless asset for V = 0, or why it should be tangential to the Markovitz bullet rather than cut through its boundary. The arguments in favour of these 2 statements is first a geometrical consideration (a line is defined by 2 points as per Euclid's first axiom) under the assumption that the price of an additional quantum of risk is constant, i.e., if higher-order derivatives in Equation (37.7) vanish. The tangent property requires a weaker form of the EMH which is a local equilibrium argument: At any given time, deviating from the market-neutral allocation will increase portfolio risk. In other words, the market portfolio need not be the globally most efficient portfolio, it just needs to be a local optimum. This local optimum is then a global one as long as risk premia are constant.

This alternative interpretation of the capital markets line builds a bridge to the preferred habitat theory which then amounts to the statement that different investors have different risk preferences, i.e., different and potentially more complex functional forms of Equation (37.6).

If the riskless asset is not available for investment or borrowing, a different approach needs to be followed to construct optimal portfolios. In order to come to an optimisation problem for any individual investor, it is necessary to define a cost function. Given that investors tend to hold assets with a view to later consuming their monetary equivalent, the standard approach is to assume some risk-return preference for an investor based on a utility model. The utility of a portfolio return is assumed to be the return minus some representation of the risk of the portfolio, i.e., the portfolio variance:

<!-- formula-not-decoded -->

where /u1D706 expresses the risk aversion of the investor. A higher /u1D706 means that an investor is willing to sacrifice more expected return in exchange for a given reduction in portfolio risk. In other words, there is no overall optimal portfolio structure. Instead, the optimal portfolio structure is a function of the risk preference of each investor.

FIGURE 37.2 Example of sample mean and standard deviation of a normally distributed random number with mean 1 and standard deviation 1 as a function of the sample size.

<!-- image -->

Equation (37.8) can be solved for the optimal weights w through a simple differentiation. At the w that maximises U , all derivatives with respect to w must be zero, so one has:

and:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

One needs to bear in mind the essential limitations of this framework. The first and foremost is that mean and variance are statistics of a probability distribution. That means that they describe random numbers but not determine them. Even if expected returns and variances are known exactly, and the statistical distribution of returns is completely determined by these numbers, the experience of any investor holding the assets, or a portfolio of them, will only over time converge to that given by these quantities. Figure 37.2, known in some form to most science students, shows the mean and standard deviation measured from samples of increasing size of a normally distributed random number sequence. Only over the course of many observations does that sample mean stabilise around the true mean of the distribution.

Auseful test is therefore to study this effect on portfolio returns. Figure 37.3 shows the same efficient frontiers and capital markets lines as Figure 37.1. Instead of showing expected returns and variances, however, multivariate normal random number generators were used to draw samples from the return distributions of the 3 assets. These samples are then weighted with the weights given by the market portfolio and averaged over 12 observations to give a flavour of the return and risk experience of an investor with a monthly analysis horizon over the course of a year. Fifty such simulations are plotted in the chart.

FIGURE 37.3 Simulated risk and return samples for the market portfolio in the positive (left) and negative (right) correlation examples (see Equations (37.2) and (37.3)). Efficient frontier and CML are the same as in Figure 37.1.

<!-- image -->

Over long periods, the actual return and risk experience will converge to the values expected by the mean-variance framework 1 . Over shorter periods, however, these simulations demonstrate that actual returns can differ substantially from predictions. Note, however, that the data in this simulation is much more dramatic than would be expected from a realistic portfolio because the small number of assets (3) limits the scope for diversification.

The result form portfolio managers is that, while the returns predicted by the mean-variance framework are the best possible predictor of actual returns, actual returns can differ substantially from these predictions. While a long investment horizon would seem sufficient to reduce this discrepancy through the operation of the law of large numbers, in practice the return and variance structure of the investment universe is likely to change over time due to changes in central bank policies, technological progress, etc. In other words, while the investor is waiting for actual returns to converge to their predicted values, those predictions will change 2 .

For fixed income portfolios, an additional complication arises from the finite lifetime of most fixed income securities. As bonds approach their maturity or call date, their duration, and thereby their price sensitivity to yield changes declines. At the same time, expected carry and roll-down returns change over time as bonds move down the yield curve. A historical return covariance matrix of fixed income securities is therefore fairly meaningless for the prediction of future returns.

1 Statistically speaking there is an alternative way to achieve a convergence, namely to sample returns across a large set of independent realisations. Given that each asset exists only once in this universe, this would require sampling across multiple alternative universes. While a manyworlds hypothesis exists as one possible explanation of quantum mechanics, the application of this theory to finance is unlikely to be fruitful. Investment managers tend to have to justify losses in the present universe without taking recourse to alternative universes where their investors made a lot of money.

2 A dramatic example of this effect was the behaviour of airline bonds following the terrorist attacks of 11 September 2001. Airlines were large bond issuers given that they operated in a stable cashflow environment. The decline in passenger traffic following the attacks led to a drastic underperformance of these bonds. By the time passenger numbers recovered, the low-cost revolution in airline travel made earnings much more violatile.

Theusualsolution to this problem is to abstract away from individual bonds any use bond indices to estimate returns. Sub-indices for several maturity bands are published by index providers so that one can in essence measure the expected return and variance properties of a generic 5Y euro-denominated A-rated corporate bond by observing an index like the iBoxx Euro Corporate A 3-5Y. This level of aggregation is generally sufficient for portfolio structuring, bearing in mind also that estimating a large covariance matrix with any confidence requires a lot of data. One should bear in mind, however, that index constituents change over time. For instance, corporate bond issuers tended to come mostly from stable industries like utilities, car makers, etc. Recently, technology companies have issued large bonds in response to changes in taxation. This changes the return characteristics of the relevant bond segments.

Somewhat more insidiously, most issuers tend to adjust supply to demand so that the relative weights of index components changes over time, and partly in response to market movements. For instance, several sovereigns used the unusually low interest rate environment created by the asset purchase programmes of the ECB from 2015 to issue extremely long-dated bonds with maturities of up to 100 years. On an index level, this increased the weight of longer-dated maturity buckets in the overall indices. This means that the structure of the market portfolio is changing, and this has implications for expected returns under the assumption of efficient markets.

Thepractical problems of mean-variance optimisation are that V is hard to estimate from sample data with any certainty for a larger number of assets, and that solving Equation (37.10) requires inverting V which can be numerically unstable.

One approach to fixing the numerical problems of mean-variance optimisation is, unsurprisingly, dimension reduction. The simplest way to achieve this is to replace individual asset return and variance data with that of asset classes (domestic equities, German bonds 2-5 years, etc.) and then optimising the portfolio structure in terms of these asset classes. Individual assets inside each class can then be assumed to follow natural weights, such as market capitalisation.

Alternatively, a reasonably low-dimensional set of risk factors can be postulated (such as industry-specific risks) or extracted from historical data through techniques such as PCA. One then constructs a mean-variance optimal factor portfolio and then maps the factor allocation back to an allocation to individual assets.

Both of these approaches side-step the numerical problems of inverting the covariance matrix V but introduce other issues at the same time. The return r i of any given asset i in either approach is determined by a linear combination of k factors, i.e.,

<!-- formula-not-decoded -->

In the case of asset class returns, each asset is mapped to a single return factor corresponding to the asset class it belongs to. The higher the number of factors, the more variance of each asset can be captured by the deterministic part of this equation. However, the idiosyncratic risks of each asset, /u1D700 i , remains. Whether a higher number of factors is better or worse is open to debate and depends on the problem at hand. For a bond portfolio in a liquid market, the performance of a subindex containing a given bond can be a good proxy for the performance of that bond. A low number of subindices can then give some stability to the solution Equation (37.10). Using a single common factor across multiple bonds is then feasibile. The experience in the equity market meanswhile suggests that a factor decomposition, i.e., a higher number of factors for each security, is a better solution for this asset class.