---
title: "Fixed Income - Alexander During-28"
type: raw_source
source_pdf: "Fixed Income - Alexander During-28.pdf"
extractor: docling
---

## Residential Mortgage-Backed

## CHAPTER 27 Securities

T he largest class of asset-backed securities are structures that refinance pools of residential mortgages, called residential mortgage-backed securities or RMBS. Cultural or tax effects create widely different rates of home ownership across different countries. The US, The Netherlands and Denmark have very high rates of home onwership, while Germany has traditionally been a country of renters. Accordingly, the former three countries have large markets for securities that refinance individual property loans. In the case of the US and The Netherlands these are ABS, while in Denmark they are covered bonds. RMBS differ from commercial mortgage-backed securities (CMBS) in that RMBS portfolios are more fine-grained than CMBS, and their exposure to industry performance is less concentrated on single sectors such as retail.

TheUSmarket,where30yearfixed-ratemortgagesformthemainfinancingvehicle for household purchases, has a large volume of loans known as conforming loans. Such loans are for single-family properties with a maximum size that depends on the location of the property. Conformance criteria are defined by the US Federal Housing Finance Agency. Crucially, conforming loans can be purchased, insured and refinanced by the so-called government-sponsored enterprises 1 (GSEs) Fannie Mae and Freddie Mac.

Trading in residential mortgage-backed securities dominates the private sector bond market in the United States. Over 80% of trade volume reported on TRACE relates to RMBS transactions. Specifically to the US, the bulk (around 90%) of trades are done in to-be-assigned (TBA) format. In this approach, new mortgages are traded on a forward basis and settled once the respective mortgage pool has been originated and securitised. Until assignment, the buyer has no information on the specific pool of mortgages. This type of trading works because the characteristics of conforming mortgages are highly standardised and pools therefore largely comparable. It is, however, possible that the mortgage origination speed is different from expectations. When fewer mortgages are originated than expected, the forward transaction may be impossible to settle because more new bonds have been sold than were originated. In this case, buyers and sellers can agree to a dollar roll which is equivalent to the old London market concept of a backwardation: The trade settlement is postponed to the next settlement cycle, and the purchase price adjusted for the value of the intervening carry. Alternatively, buyer and seller can agree on a coupon swap where securities with one coupon are exchanged against securities with a different coupon, with an attendant compensation payment. Such coupon swaps are particularly important when mortgage production rates shift between different coupons, and there is therefore a structural lack of certain expected coupons for the foreseeable future. Such a structural shift cannot be addressed through dollar rolls because the trades would consume balance sheet for some time, and because prepayments over time affect relative valuations of older and newer bond series.

1 In the US market, these entities are generally known as agencies despite being private companies. As with the term 'rating agency', as long as one does not take the market jargon as legal gospel, there should be no confusion.

## 27.1 RESIDENTIALMORTGAGE PREPAYMENTS

The expected rate of mortgage prepayments is determined by a variety of factors, corresponding to the types of decisions made by mortgage borrowers over the duration of the loan. Below is a list of factors which are then incorporated in a mathematical model.

Non-economic prepayments (attrition) refers to early mortgage redemptions that do not have an economic motivation. These could be driven by defaults (leading to foreclosure auctions and therefore at least partial repayment), moves (for instance as families trade up to a larger property after having children), fire damage, or death of the borrower (some jurisdictions require life insurance coverage of loan amounts). An important factor that determines the rate of such prepayments is whether properties are sold with the mortgage in place, or sales require remortgaging. Jurisdictions where it is common to transfer properties together with an existing loan see correspondingly lower attrition rates of mortgage pools.

Non-economicprepaymentratescanexhibitdependenciesonmacro-economic variables, for instance through higher default rates during economic downturns. They can also be somewhat seasonal because voluntary moves occur more often in summer than in the winter months. Even mortality rates in the general population have clear seasonal patterns in most climate zones.

In any case, non-economic repayments mean that the expected average life of a mortgage pool is shorter than the weighted average maturity of the pool independent of the future evolution of mortgage market conditions.

Economic prepayments are early redemptions of a mortgage loan due to economic incentives. This usually means that mortgages are available at a lower rate and the borrower decides to repay the existing mortgage early with cash raised in a new mortgage. Prepayments generally are associated with costs, such as notary fees and bank fees. Because some of these costs are fixed, rather than proportional to the loan size, larger loans tend to prepay faster than smaller ones.

Some jurisdictions allow the bank to charge the opportunity cost of losing the mortgage loan early which drastically reduces the economic benefits of early repayment. In other markets, for instance the US, the benefit of a lower mortgage rate needs to be weighed against the extension of the loan maturity. It needs to be kept in mind that the benefit of a lower rate depends on the remaining principal and amortisation schedule. A mortgage late in its life consists mostly of redemption payments and a lower interest rate has a diminished cash value.

Economic prepayments are subject to a phenomenon known as burn-out which is the observation that economic prepayments at a given refinancing rate decline over time. This is because cost-sensitive borrowers for whom refinancing is triggered at that rate are eliminated from the current mortgage pool 2 so that the pool becomes less likely to refinance at that rate. There can also be a drift higher in economic repayments due to an increased availability of information about refinancing terms, and the emergence of mortgage brokers who seek out borrowers that might refinance in return for a fee. A somewhat curious but significant aspect of economically driven refinancing is known as the newspaper effect: When interest rates have been low for some time but appear to be on the verge of a rise, newspapers tend to run articles in their weekend property sections that highlight the imminent loss of attractive refinancing options. This can lead to a spike in mortgage refinancing after the trough in interest rates is reached.

Some markets exhibit further special effects. In Denmark, for instance, speculative repayments can occur when borrowers deliver below-par mortgage bonds to their banks and refinance with current higher-rate mortgages. This type of refinancing reduces the mortgage principal and leads to a refinancing option at the newhigher rate. In an ideal scenario, a Danish mortgage borrower would refinance a mortgage at the current principal amount at low rates through prepayment, and use times of higher interest rates to reduce the principal amount through delivery. During the 30 year lifetime of the standard mortgage in this market, this could lead to multiple savings occasions. The option to buy back one's mortgage below par does not exist in most other markets. In the Danish case, it also does not directly lead to an early redemption of bond held by other investors because the borrower has to purchase the mortgage bond in order to deliver it. An investor not selling the bond will therefore be unaffected.

Non-economic non-prepayments are situations where a borrower has a clear incentive and opportunity to refinance but does not exercise this option. Depending on the market, there can be multiple reasons for such behaviour beyond disinterest in one's financial affairs, or the time and effort involved in realising a potential reduction in mortgage costs. For instance, refinancing might require a re-appraisal of the property value, and that value may have declined, making refinancing unavailable. The same can be true for the credit rating of the borrower 3 .

The modelling implication of this effect is that refinancing rates never reach 100% even in the most advantageous circumstances. More broadly speaking, this effect means that one does not model prepayment behaviour as a step function of the incentive (no economic prepayments below a threshold and 100% refinancing above it), but as a gradual saturation function.

2 These borrowers will of course appear again in a new pool with their refinancing loan.

3 Most developed markets have some form of credit assessment of retail borrowers available, such as the Schufa system in Germany or the FICO score in the US. Banks would then typically consult such information before granting any loan, including a renewed mortgage.

Clean-up call is a feature in some RMBS transactions where the originator will repurchase the remaining asset pool at a set time and the SPV uses the proceeds of this purchase to redeem all remaining bonds. In essence, the mortality on the clean-up call date is 100%. Such a call is in essence a cost management strategy because it leads to a dissolution of the SPV structure at a time when only a small share of the original pool is left but a large part of the servicing cost remains.

Prepayments are observed in principle at each payment date and the share of mortgages that prepay are called the mortality, or single month mortality (SMM). It is sometimes more convenient to express the prepayment speed in an annual variable. This is known as the constant prepayment rate CPR [45], given by:

<!-- formula-not-decoded -->

where f is the payment frequency ( f = 12 for monthly, f = 4 for quarterly, etc.).

## 27.2 PREPAYMENTMODELLING

Investors in pre-payable mortgages need to carefully model the risk of early repayment. As the previous section has made clear, prepayment is largely driven by the availability of more favourable financing conditions relative to a current mortgage. This means that refinancing does not imply that a borrower ceases to pay interest on the financing of a property. Instead, the borrower ceases to pay interest on one loan, and instead pays interest on another. For the investor in the original loan, or the RMBS it has been repackaged into, that means a loss of interest payments. A mortgage valuation model consists of two components. The first is a model for the mortality of a mortgage at a single payment date (the SMM). This basic mortality model is then used to value the mortgage, taking into account prepayments at any future date.

In what follows, a simplified model will be used to illustrate the basic features of a prepayment model for hypothetical USD-denominated mortgages with a quarterly payment frequency 4 . At each payment date, the borrower has the choice to either make only the scheduled payment or additionally repay the entire remaining principal and take out a new mortgage for that amount at current conditions. The refinancing incentive is assumed to be the ratio between the cost reduction created by refinancing and the original mortgage amount. This cost reduction s is determined by the difference in the discounted value of cashflows on the original mortgage and a new mortgage used for refinancing that has the same original years to maturity as the existing mortgage. The discount curve is the current mortgage curve which is defined as the US Treasury zero-coupon curve 5 plus a flat spread. Lastly, to align this with the US market, the original years to maturity of a new mortgage is assumed to be 30 years.

4 This frequency, instead of monthly, is chosen to make Figure 27.4 more readable.

FIGURE 27.1 The prepayment model Equation (27.2) and its four parameters: Baseline b k , centre c , width w and the saturation level 1 -m + b k .

<!-- image -->

The main simplification of the model is that it does not take rates volatility into account. The benefit of prepaying is determined only by the change in interest costs, not the value of the option that is being exercised by prepaying, or the option received by taking out a new mortgage.

The prepayment model has four parameters which in an actual modelling setting would be calibrated to historically observed prepayment data. Here, reasonable values have been chosen more or less at random for illustration. There is a baseline attrition rate ( b k ) linked to non-economical repayments which is set at 5% per year. At a saving c of 6% of original mortgage amount, half of the interest-rate sensitive borrowers are expected to prepay. There is a 2% uncertainty interval w around this point, and a share m of 60% of borrowers are assumed not to be sensitive to interest rates (non-economic non-prepayments). These parameters are then put into a logistic function:

<!-- formula-not-decoded -->

(shown in Figure 27.1) to yield the mortality at the payment date k as a function of the available saving from prepaying a mortgage on a given date. In a more realistic model, some of these parameters (particularly b k ) would be time-dependent.

The mortgage used as an example is a 4.5% coupon mortgage with a maturity date of December 2040. The original maturity of the mortgage is 30 years so at the time of analysis (May 2020) it is already ten years old. This information is then used to calculate the economic gain from prepaying, i.e., the parameter s of the model Equation (27.2).

5 The US Treasury curve is represented by a Nelson-Siegel spline fitted to actual Treasury prices on the analysis date.

FIGURE 27.2 The basic mortality model used in this section. The control parameter of the model is the spread of mortgages over US Treasuries. As the spread increases, the cost saving from prepaying declines, and so does mortality.

<!-- image -->

Figure 27.2 illustrates this basic mortality model. The decisive variable is the spread of mortgage rates over the US Treasury curve. Higher spreads make new mortgages more expensive and it is therefore less attractive to refinance. The same effect would occur when US Treasury rates themselves increase. The spread parameter used here is therefore best thought of as a general shift in mortgage rates rather than as a mortgage spread. The general picture is then that when mortgage rates are lower, borrowers have a higher incentive to prepay an existing mortgage with a higher coupon. The connection between the cost saving of refinancing, and the actual refinancing rate is given by the logistic function Equation (27.2). This function needs to be understood as a statistical model. The choice of each mortgage borrower is the binary decision to prepay or not, and this decision is affected by many factors. The assumption of Equation (27.2) is that when averaging over a large pool of borrowers, their collective decisions combine to a deterministic relationship between refinancing conditions and refinancing rates.

This mortality model contains several simplifications compared to the considerations in the previous section. There is no notion of burn-out so that there is no path-dependency of the model. In other words, prepayments depend on current interest rates, but not on past levels. Second, there is no size dependence of prepayments because the saving is assessed purely on the basis of relative savings with no regard to potential fixed fees. Relative fees (fees proportional to the mortgage amount) would be expected to be reflected in the parameter c . There is an apparent problem with this function, namely that prepayments rise from the baseline level even when the refinancing incentive if zero or even negative, which for these parameter values happens at spreads of over 80bps. Because the logistic function is never exactly zero, this effect is unavoidable and it has no meaningful impact on the accuracy of the model. While it would be possible to cure this defect by introducing explicit cut-offs, the advantage of retaining the logistic function is that it is infinitely smooth. More complex valuation models that rely on yield curve scenario analysis tend to struggle with discontinuities.

FIGURE 27.3 Comparison of the mortalities of three identical bonds with different seasoning. The solid line in the middle refers to the same bond as the one used in Figure 27.2.

<!-- image -->

Ashasbeenpointed out earlier, the incentive to prepay is dependent on the remaining life of the mortgage. To illustrate this, Figure 27.3 compares the mortalities of three bonds that are identical in all aspects except their origination and maturity year.

The mortality for a given spread is higher for longer mortgages simply because the longer remaining life means that the borrower pays an above-market coupon for longer whenrates are low. At extremely favourable conditions, all three bonds prepay as fast as possible. At very high refinancing rates, meanwhile, none of these mortgages prepays and so all three mortalities converge to zero.

Having discussed prepayment models, it is time to turn to the valuation aspect of prepayments implied by these models. Simply speaking, prepayment means that an investor in an RMBS receives less cash faster than scheduled. The decline in total cash is the result of a loss of future interest payments on the part of the principal that has been repaid early. This principal, meanwhile, is being repaid ahead of schedule. These two effects have an opposing impact on the value of the mortgage because an earlier payment has (at positive interest rates) a higher present value than a later one. The purpose of a valuation model is to calculate the combined impact of these two effects.

Figure 27.4 compares the expected cashflows from the same mortgage under different rate assumptions. When market mortgage rates are very high, then no prepayment occurs and the expected cashflow structure matches the regular annuity that follows from the mortgage formula Equation (16.1) on page 141. When refinancing is attractive, prepayments add to the early cashflows while later cashflows are lower because the mortgage pool is then smaller than it is at the beginning as a result of prepayments.

Figure 27.4 shows only the next 20 cash flows. To value the mortgage, all subsequent cashflows need to be taken into account. This is done in Figure 27.5 which shows the simple sum of all cash expected from the mortage together with two sample discount factors, all as a function of the interest rate level. At very low rate levels, the mortgage prepays as fast as possible and the total cash received is essentially the remaining principal plus the next few coupons. At very high rate levels, the total cash paid converges to the sum of all scheduled payments because no early redemptions occur. Put differently, at high interest rates all the interest payments originally scheduled actually take place. The lower the interest rate, the more borrowers will refinance and their future interest payments will then go to the holders of the new mortgages that were originated for refinancing.

FIGURE 27.4 Total cashflows (interest, amortisation and prepayment) from the 2040 sample quarterly mortgage over the next five years (20 quarters) for different spreads. At a spread of 200, practically no prepayment occurs and the cashflow structure is simply the scheduled annuity. At a spread of 50, the mortgage prepays very fast.

<!-- image -->

FIGURE 27.5 Total cash paid (as a fraction of the remaining principal) by a mortgage as a function of refinancing conditions, and two discount factors. The first has a fixed maturity of three years, the second has a maturity equal to the weighted average life of the mortgage.

<!-- image -->

This figure shows that the non-linear shape of the mortality function Equation (27.2) means that the spread dependency of the cash payable and the discount factors are different. The slope of the cash amount is steepest where the prepayment option is most at the money which in this model is around the 80 bps spread level. At high rate levels, prepayments are more or less irrelevant and the amount of cash received converges to a constant. The discount factors, meanwhile, have the usual bond-like price-yield relationship. As a result, the total value of the mortgage is very sensitive to prepayment speeds where those speeds vary most, whereas it is more sensitive to discounting at higher rates. The figure also shows another effect. As prepayments decline, more of the cash is paid later, and therefore subject to discounting over longer periods than when prepayments are higher. To measure this extension, the figure uses the weighted average life (WAL) defined as:

FIGURE 27.6 Price-yield (here, price-spread) relationship of a prepayable mortgage. The weighted average life of the cashflows is added for illustration.

<!-- image -->

<!-- formula-not-decoded -->

The extension of payments in time happens when interest rates rise, so the cash flows from the mortgage have to be discounted over longer periods at higher rates. The discount factor applicable to the weighted average life of the mortgage therefore declines faster than than a constant-maturity discount factor as rates rise.

The end result of this analysis is the price-yield relationship shown in Figure 27.6. Unlike a standard bond, the price of this mortgage initially increases with rising yields because prepayments become less likely and the mortgage holders therefore receive moreinterest payments. This decline in prepayments is also leading to an increase in the weighted average life of the mortgage. Only at high yield levels, where prepayments are no longer relevant, and the weighted average life stabilises, does the mortgage behave like a normal bond and declines in price as a result of falling discount factors.

A rising price for a rising yield implies a negative duration, so in this example, the mortgage duration is negative up to a spread of around 140 bps. Around this spread level, duration increases from the initial negative value to a bond-like positive one as yields rise. A rising duration for rising yields implies negative convexity. To achieve a bond-like behaviour for a mortgage portfolio, portfolio managers have to buy and sell duration risk in response to yield movements on an ongoing basis. The standard duration instrument in the US market is the on-the-run Treasury and hedge activity in this bond is an important source of liquidity in this security.

The negative convexity of the US, and also the Danish, mortgage market is a reflection of the prepayment option that the RMBS and Danish mortgage market has written for mortgage borrowers. The trading required to hedge mortgage convexity is equivalent to the trading required to hedge any other short option position. What is unique to the mortgage market is the size of this options position and that the long side of this option is being held by ordinary households. Unlike options traded between financial market participants, this rules out one particular hedge for an option seller, namely to repurchase the option from the buyer.

In general, it should be noted that while the graphical examples here are based on a realistic prepayment model, they do not span the full universe of effects that can occur in RMBS. In particular, the relative impact of having more cash to discount as a result of lower prepayments, and the lower present value of future cash flows, depends on the baseline yield level and curve steepness which are very low at the time of writing. This current yield configuration emphasises the hump of the price-yield relationship.