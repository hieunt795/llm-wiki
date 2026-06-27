---
title: "Fixed Income - Alexander During-37"
type: raw_source
source_pdf: "Fixed Income - Alexander During-37.pdf"
extractor: docling
---

## 36.1 INTRODUCTION

Hedging means adding instruments to an existing portfolio in order to neutralise the overall position against expected shifts in the market. In the simplest case, this may mean selling a futures contract against an existing bond position, or receiving in a swap against a short position in a money market futures strip. In a more complex setting, it may involve selling or buying different futures contract to adjust a large portfolio in order to follow changes in a benchmark index.

In general, hedging is done with a more liquid instrument, i.e., a government bond is hedged with a bond or money market futures contract, a sub-sovereign corporate bond with a sovereign bond, and so on. This is because the idea of a hedge is to voluntarily assume a new position in order to reduce the risk of an existing one. The cost of entering and unwinding this additional position should therefore be low.

The fundamental precondition for hedging is that the instruments involved need to have a stable relationship. In other words, their price changes in reaction to market movements need to be related to such a degree as to make it possible to offset the exposure inherent in one instrument with the exposure of another. Naturally, the offset cannot be perfect, but we can hope that the residual risk after hedging is small compared to the outright risk with no hedge. Using the simple example of a long bond position hedged with an appropriate futures contract, the outright exposure of the bond alone would translate into daily movements in the order of a few tens of ticks to perhaps a point or two, whereas the basis should normally move only a few cents per day. Hedging therefore reduces risk.

How an instrument is commonly hedged affects how it is priced. A trader views inventory in terms of its hedged cost. For instance, having bought a bond and hedged it with swaps at an I-spread of x bp, the trader will break even on the position when selling it at an I-spread of x -/u1D6FF where /u1D6FF is the bid-offer spread on the swap leg. This cost will therefore form an anchor for the price the trader will show to potential buyers and movements in the swap curve will be a decisive driver in the cash price of the bond. In other words, the hedge creates a correlation between swap rates, and the bond's yield in the profit-and-loss calculation of the trader. If traders generally agree on hedge strategies, then this correlation will be reflected in market prices more widely.

Hedging does not necessarily rely on linear assumptions such as stable correlation matrices, but normally this assumption is made. Even allowing for a general form of the relationship between instruments, there will always be idiosyncratic movements in a given position that are impossible to hedge against. In most cases, a trader will

## CHAPTER 36 Hedging

design a hedge position precisely in order to take a view on such movements. However, the implication is that only a completely flat portfolio is truly risk neutral. Any other portfolio is exposed to some form of risk.

The stability of the yield curve is the main reason why hedging is such an important topic in rates trading as opposed to equity and, to some degree, credit trading. The individual company risk in a share price is usually as large, if not larger, as the overall market risk, so effective hedging is a lot more difficult. In the credit markets, the existence of different bonds by the same issuer and of credit default swaps and other derivatives usually provides a larger spectrum of possible hedge instruments.

## 36.2 DURATION-NEUTRALHEDGES

The simplest form of hedging is the duration-neutral hedge. Here, one starts from the mathematical relationship between price and yield movements of a fixed-coupon bond given by the DV01 D :

<!-- formula-not-decoded -->

Assuming 2 bonds with notionals N 1 and N 2 in the portfolio, the hedge condition is that the total price change under a yield movement should vanish, i.e.,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

At this point it is useful to remember that the DV01 D of a bond is the product of dirty price P and modified duration D ∗ , so one could write the same equation in terms of the market values M 1 and M 2 as:

<!-- formula-not-decoded -->

The equations are totally identical, but real money managers usually tend to think about positions in terms of market value whereas trading desks generally use nominal amounts.

The problem with both Equations (36.3) and (36.4) is that they were derived using d y as a non-indexed variable. In other words, they implicitly assume that there is a single yield variable that explains the movements in both bonds. While that might be the case if both bonds have almost the same maturity and are in the same market; it is most likely to be very wrong if the bonds are in different markets or have very different maturities. In these cases, duration neutral hedges have little meaning.

from which follows:

## 36.3 REGRESSION HEDGES

One way of curing the deficiencies of Equations (36.3) and (36.4) is to start from the slightly more general equation:

<!-- formula-not-decoded -->

and impose the linear relationship:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

which then results in the equivalents:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

As should be expected, these equations revert to Equations (36.3) and (36.4) for /u1D6FD = 1. Once a /u1D6FD parameter has been introduced, there is little need to actually still use yields as the basic variables for the hedge construction. Instead, we could instead absorb the terms D d y into a simple d P and assume a relationship like:

<!-- formula-not-decoded -->

and construct the hedge based on price regression. Not only is this simpler, but it is also possible to use hedge instruments for which a yield cannot be defined, such as futures contracts or derivatives of othe underlying assets such as crude oil. Hedges so constructed are called price regression hedges.

Again, there is a fundamental problem in the background. The regression Equation (36.6) implies:

<!-- formula-not-decoded -->

i.e., the regression coefficient of the reverse regression should just be the inverse of the original /u1D6FD . However, when one actually does the standard linear regressions of the 2 variables in both directions, the regression coefficients will usually not be the inverse of each other. This is a sign that the regression equation is misspecified, in particular that the assumption that the independent variable contains no noise is incorrect. The most general way to address this problem is through the use of principal component analysis, discussed in Chapter 33.

to find:

## 36.4 YIELD CURVE MODELHEDGES

Once the term structure of interest rates has been captured in a yield curve model, that model can be used to generate hedge coefficients that are appropriate for the type of curve movements that are consistent with the model. Different curve models generate different curve movements, so the hedge structures in model-based hedges will depend not only on the instruments, but also on the model. To give a very simple example, one can assume a curve model where the yields of all bonds are equal to the same number y . In this model, the only possible yield change is one where y changes, i.e., a parallel shift of the whole curve. One can then calculate the change in the value of a portfolio of n bonds under such a change:

<!-- formula-not-decoded -->

The hedge condition is d V = 0 and one can try to solve this equation given a fixed position in 1 of the bonds. Without loss of generality it can be assumed that N 1 is fixed, so the portfolio will be hedged if:

<!-- formula-not-decoded -->

This equation has an infinite number of solutions if n &gt; 2. For n = 2 is simplifies to:

<!-- formula-not-decoded -->

which has the solution Equation (36.3). In other words, in a flat yield curve model, duration neutral hedges are the natural model-implied hedges.

Generally, calibrating a given model with a view to using it for hedging is different from calibrating it for other purposes, such as the best possible fit of current yields, or prediction of future interest rates. The main criterion for a good hedging model is that the amount of unexplained profit and loss from a hedged position should be as small as possible. For trading desks, this generally means that on an overnight basis, the model should explain as much as possible of the price movements of the individual bonds in the market. In contrast, a simple curve fit will aim to reduce the current residuals as much as possible, i.e., there is no relationship to carry and rolldown on the position.

The simple model used above had a single parameter and that parameter directly explained the yield of each bond, so price changes are most naturally expressed via the DV01 of the bonds. Most structural curve models will instead generate a term structure of discount factors, so the natural approach to hedges is directly through price changes. One starts from the fact that the model price of a bond is the function of the bond and two sets of parameters:

<!-- formula-not-decoded -->

The assumption is that the vector /u1D741( t ) is a time-dependent set of k state variables whereas the structural parameters /u1D714 are unchanged through time. In the simple model

above, /u1D741 = ( y ) and /u1D74E = ∅ .

To hedge a portfolio in a model context means making the portfolio value independent of changes in the state variables /u1D741( t ) . Aside from noise, the evolution of /u1D741( t ) is usually explained by the model and the parameters (/u1D741( t ), /u1D74E) . The change in the portfolio value can be written as a total derivative:

<!-- formula-not-decoded -->

In order to be hedged against an arbitrary move in the state variables, all the terms in the square brackets of the equation above must vanish. This gives k linear equations of the form:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

for the notional amounts Ni in the hedged portfolio. In general, therefore, a portfolio of k instruments is necessary to completely hedge against movements in a k -factor curve model. The number of instruments can be smaller if this system of equations is degenerate. Such a situation can occur if, for instance, some of the derivatives vanish for all the instruments in the portfolio.

If there are more instruments than model factors, there is an infinite number of hedged portfolios. To isolate a single set of portfolio weights, additional conditions have to be specified. The most important case is one where there are k + 1 instruments in the portfolio and one of the notionals, say N 1 is specified. This represents the common case where a trader is given a particular position NB in a given bond from a client trade and needs to establish a hedge using liquid market instruments, such as futures contracts. Assuming that the trade is using a 2-factor model, 2 hedge instruments are needed in general to neutralise the position. Given the easy availability of linear equation solvers, it is easiest to write the hedge condition as a set of 3 equations for the 3 notionals N 1 = NB , N 2 , and N 3 , namely:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The bond position is recovered from the first of these 3 equations, while the other 2 establish the neutrality against changes in the 2 model state variables /u1D707 1 and /u1D707 2 . Note that, although the price sensitivities of the model are expressed here in terms of partial derivatives, it will in most cases be necessary to calculate these derivatives numerically

because a closed form does not exist.

One can use the same formalism to derive PCA-neutral butterfly weights. In this case, the model describes yields, not prices, so with the DV01 of each bond:

<!-- formula-not-decoded -->

Here, the state variables /u1D707 1 and /u1D707 2 are simply the current factor values for the first 2 principal components given by the scalar products /u1D707 1 = y ⋅ f 1 and /u1D707 2 = y ⋅ f 2 . The partial derivatives are simple constants given by the factor loadings, namely:

<!-- formula-not-decoded -->

Equation (36.18) then takes the form:

<!-- formula-not-decoded -->

The sign of the bullet notional of course depends on whether the bullet is rich or cheap.