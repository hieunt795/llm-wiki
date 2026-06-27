---
title: "Fixed Income - Alexander During-16"
type: raw_source
source_pdf: "Fixed Income - Alexander During-16.pdf"
extractor: docling
---

## 15.1 FORWARD RATES

Forward rates are the bridge between interest rates of different horizons. One can ask the following question: Assume one can lend money from now ( t 0 ) until t 1 at the rate r 1 ( t 0 , t 1 ) and until t 2 &gt; t 1 at the rate r 2 ( t 0 , t 2 ) . At which future rate r f ( t 1 , t 2 ) does one need to be able to lend money between t 1 and t 2 so one has the same return from lending from t 0 to t 1 and then from t 1 to t 2 as from lending straight from t 0 to t 2 ? The meaning of these rates is shown in Figure 15.1.

## 15.2 NO-ARBITRAGE CALCULATIONS

Using discount factors, the answer is quite simple. Discounting a given amount of cash from t 2 back to t 0 gives a present value of Df ( t 0 , t 2 ) . Discounting the same amount of cash back to t 1 gives the forward present value Df ( t 1 , t 2 ) . To bring this forward present value back to t 0 , one has to multiply by the discount factor Df ( t 0 , t 1 ) , so the present value is Df ( t 0 , t 1 ) Df ( t 1 , t 2 ) . Because this present value reflects the same future cashflow, the following equation must hold in the absence of arbitrage:

<!-- formula-not-decoded -->

and so trivially the forward discount factor is:

<!-- formula-not-decoded -->

FIGURE 15.1 Relationship of spot and forward rates.

<!-- image -->

## CHAPTER 15

## Spot and Forward Rates

Discount factors are the fundamental building blocks of fixed income mathematics, but the market uses interest rates. Therefore, while forward discount factors are easy to calculate, they need to be translated back into interest rates.

In the money market, the relationship between interest rates and discount factor is given by the prices of pure discount instruments. For instance, the price of a deposit paying 1 yen in six months is equal to the six months discount factor. Depending on the market, these prices are given by Equation (13.2) or Equation (13.4). If simple yields are used, Equation (15.2) becomes:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

If one instead uses discount rates, Equation (15.2) has the simpler form:

<!-- formula-not-decoded -->

and the forward rate is:

<!-- formula-not-decoded -->

Note that, although the equations look very similar, they are in fact subtly different.

As mentioned in the section on money market futures, it is possible, and indeed the normal course of action, to construct spot rates from the current traded values of the Libor futures strip. In this case, the only spot rate taken from the deposit market is the so-called cash stub or stub rate that corresponds to the cash rate until the start of the reference period of the first Libor contract. From that date on, the futures implied interest rate is taken as a forward deposit rate and the spot rate to the end of the first contract's reference period is calculated according to Equation (15.2).

In principle, therefore, the term structure of money market rates is built from the stub rate which is successively extended using money market futures-implied rates using the recursive relationship:

<!-- formula-not-decoded -->

Note that the futures-implied forward rates require a convexity adjustment following Equation (13.17) before being used to produce the forward rates in Figure 15.2.

and therefore:

FIGURE 15.2 Relationship of Libor strip with the spot rate term structure.

<!-- image -->

## 15.3 OFFICIAL RATES VERSUS TERM RATES

Moneycreation can be influenced using different means but generally there is a concept of a policy rate or official rate that reflects the opinion of the central bank as to the appropriate level of borrowing rates in the economy. The official rate is most naturally a short rate because the central bank needs to ensure that changes in the policy rate feed quickly through into the economy. The longer existing deposits at the old rate are running off, the slower the impact of a policy change would be.

Because official rates in developed economies tend to be adjusted more frequently than other factors influencing money creation (such as reserve requirements), market attention is focused on the official rates and the front end of the interest rate curve is driven by expectations of changes in the official rates.

In general, official rates refer to the specific interest rates that a central bank can target through its open market operations. These operations do not necessarily start immediately after a change in the official rate has been decided by the central bank. Furthermore, market interest rates are not usually quoted on horizons that are adjusted to central bank policy decisions but in round maturities such as 'three months'. The relationship between official rates and the liquid market rates is therefore not trivial and it is important to understand the exact working of the central bank to understand the relationship.

## 15.3.1 The turn premium

Before discussing the extraction of policy rates from observed interest rates, it is important to explain a technical effect in the money market known as the turn premium. Banks have daily control over their balance sheet but balance sheet data has to be submitted to regulators on a periodical basis. The most important balance sheet date is year end, which usually coincides with the calendar year, but may be on some other date, such as 1st April in Japan.

Banks have a strong incentive to shrink their balance sheets towards year end, also called the turn 1 , in order to report the least risky assets on that occasion. Banks will therefore be more reluctant to conduct business, such as lending, when the transaction spans a year end than they are when the transaction opens and closes within the same year. As a result, interbank lending rates tend to jump when the horizon of the lending transaction spans year end. For instance, 3M deposit rates in most markets will jump in late September when the maturity changes from December to January. This is the turn effect. Although interest rates move daily, the turn effect is always positive, so it can be distinguished from normal fluctuations. Naturally, the turn premium is also reflected in forward rates and money market futures prices.

1 This term relates to the expression 'the turn of the year'.

The size of the turn premium is not constant and is subject to supply and demand. Given sufficient data points (observable rates), one can establish a forward rate from the last day of the year to the first day of the following year. The difference between this interest rate and the neighbouring overnight rates is the turn premium proper and it usually ranges around a few percent. Exceptionally large turn premia could be observed in some markets on occasions where the new year coincided with market changes, such as the introduction of the euro in 1998/1999, the Y2K worries in 1999/2000, and the introduction of euro cash in 2000/2001. In more recent times, the introduction of the leverage ratio has led to spikes in repo market rates around turn dates. While this regulatory tool remains in place, turn premia have declined as market participants adjusted their behaviour, particularly by funding earlier.

Theextent of the turn premium depends to some degree on the instrument used. An unsecured interbank loan has a different balance sheet treatment from a repo transaction, or an overnight index swap. Central banks generally limit the impact of the turn on their policy rate, so different rate instruments will reflect the turn to differing degrees. It is important to keep in mind that the turn premium is unrelated to any changes in the economy, and therefore the 'natural' level of interest rates or the policy rate. Therefore, the turn premium needs to be compensated for when extracting policy rate expectations from market rates.

## 15.3.2 Matching policy expectations to market rates

The basic way of reconciling policy expectations with observed rates is to use an overnight account and roll this account using the expected path of the policy rate. In doing so, any differences between the policy rate and market rates need to be adjusted for.

In Figure 15.3, there is one assumed path of the policy rate, shown as a thick line near the bottom of the chart. From that policy path, one derives an assumed path of overnight rates, taking into account any expected differences in level and timing of changes. For instance, ECB policy MRO rate changes are decided upon and announced on Thursdays, but only apply to the next MRO which settles on the following Wednesday. At the same time, there may be differences between the policy rate and the market rate. For instance Figure 6.2 on page 49 shows that the overnight benchmark rate in the euro area differed from what was at the time the main policy rate. In addition, actual market rates may have turn effects which also need to be taken into account. With a projected path of overnight rates, one can track the value of a deposit made at time t 0 until time t which is in essence the inverse of the discount factor Df ( t o , t ) .

Fromthecompoundedvalueoftheovernightaccount, one can extract the complete termstructure of interest rates and forwards. The expected policy path, i.e., the sequence of imputed policy rate changes, is then adjusted so as to achieve the best possible overall fit with market rates.

FIGURE 15.3 The hierarchy of matching policy rate expectations to observed market rates. The ordering along the vertical axis does not imply the level of rates.

<!-- image -->

Typically, one abstracts away from the discrete nature of policy changes (usually 25 bp) and allows any amount of rate changes. Changes are then interpreted as probabilities of discrete changes, i.e., a 10 bp implied change is interpreted as a 40% probability of a 25 bp change. Note that the resulting probability picture hides the effect of cumulative probabilities. For instance, one may obtain 50% probabilities of a 25 bp change in the policy rate in two successive meetings. This should usually not be interpreted as a 25% probability of two consecutive hikes (as would be possible if the probabilities were strict unconditional probabilities), but rather that the market expects exactly one 25 bp hike, but is split as to the exact timing. Therefore, while talking about probabilities is standard usage, it is important to realise that this is just a loose manner of speaking.

In any case, policy changes on the overnight account are applied only on those days when they could actually occur. This means that the meeting calendar of the respective central bank is part of the inputs to the fitting process. Otherwise, the solution space becomes too large.

As can be surmised from the picture, a number of concerns need to be addressed when using market rates to infer policy changes. These are discussed below.

Basis of cash versus policy rates In some cases, the most liquid cash rate is actually a different instrument from the policy rate. For instance, the policy rate of the ECB is a repo rate while Euribor is an unsecured rate. The credit spread incorporated in unsecured lending will therefore introduce a maturity-dependent basis. The basis can be corrected for using observable spreads that reflect a similar basis, such as the Libor-GC spreads for different terms.

Term structure and other effects As has been discussed when introducing the turn effect, market interest rates are driven by factors other than central bank policy changes. The turn effect is an obvious example, but more significant in economic terms is the impact of the term risk premium. This premium, which is not observable in the market, is a spread over the interest rates that would be consistent with an overnight account rolling at the policy rate. The premium reflects the fact that lenders committing to a term deposit give up the option to reinvest the money elsewhere, which is an option that an overnight investor has. The term risk premium grows with longer investment horizons and is not constant through time. While models for the term risk premium exist, they usually work on timescales that are not relevant for forecasting central bank actions.

Normally, the term risk premium is simply ignored because it is assumed to be growing sufficiently slowly with the maturity of the underlying instrument. This is acceptable for short horizons. However, it is important to keep in mind that a flat term structure reflects rate cut expectations compensating the increasing term risk premium.

Futures vs cash basis There is a basis between the interest rate futures markets and the underlying cash rates that is created by the convexity bias of futures contracts. This is addressed in Equation (13.17).

It should be noted that all of these factors can change, and so can the monetary policy framework. At the time of writing, developed countries' financial markets operate in an environment of excess liquidity which makes the lower end of interest rate corridors binding. In more normal environments, this may not be the case. Such changes would affect the modelling of the translation from policy rates into market rates in Figure 15.3.