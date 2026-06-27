---
title: "Fixed Income - Alexander During-23"
type: raw_source
source_pdf: "Fixed Income - Alexander During-23.pdf"
extractor: docling
---

## CHAPTER 22

## Curve Spreads

T he previous chapters introduced curves as the theoretical reflection of maturitydependent discount rates, and therefore as a generalisation of the yield concept. It framedthis generalisation in the idea that a curve can be calibrated to a set of instrument prices, and then be used to price instruments.

In general, the curve-implied price of an instrument need not match the actual market price the instrument unless the curve model is a market model and the instrument is part of the calibration. This potential difference in price raises the question of how to express it. In general, the topic of this chapter is how to measure the distance between a curve and an instrument.

The most straightforward approach is a simple price difference:

<!-- formula-not-decoded -->

where P is the market price of the instrument, Cf i are its cash flows and Df ( t i ) the discount factors implied by the curve. As usual, the shortcoming of this price difference is that it does not reflect the duration risk of the instrument in question.

Thefollowingsections introduce various curve spread measures used in the market. These spreads are generally expressed in basis points.

## 22.1 Z-SPREAD

The most natural way to construct a risk-adjusted curve spread from a discount factor curve is to translate the difference between curve-implied and market price into a yield spread, namely by taking the difference in yields calculated for the two prices:

<!-- formula-not-decoded -->

The term z-spread for this expression is related to the use of cashflows, which are in essence zero bonds. This property makes z-spreads the natural choice of relative value measure for complex cashflow structures, and they are used extensively in the analysis of inflation-linked bonds. When the curve used to generate the discount factors Df ( t i ) is a spline, the same measure is also often called a spline spread.

At the same time, z-spreads are difficult to calculate for users who are unable to break down an instrument into its constituent cash flows. This should be a surprising problem but is related to the use of readily available libraries which can provide such calculations as yields, but do not provide cash flow extraction.

Like all spread discussed in this chapter, higher spreads imply cheaper pricing of the instrument relative to the curve. In Europe and Japan, this usage is uniform across spread measures. In the US, however, swap spreads are quoted as par spreads (discussed below) of swaps over US Treasuries. This means that a higher swap spread in the US implies a more expensive (relative to swaps) US Treasury. Unfortunately, the situation is muddled further by commercial data providers who use the US convention also for European and Japanese spread series.

## 22.2 PAR SPREAD

Theparspread is a simple comparison between the yield of an instrument and an appropriately measured par rate on the curve. The most common example of such spreads are the swap spreads in the US and the Australian EFP (exchange for physical) spread.

Rather than defining the price of a bond relative to a curve, par spreads are often used to define a curve relative to the price of benchmark bonds, or other instruments. In those cases, the liquidity of the bonds is so high that it provides superior price discovery relative to that of the curve. An additional incentive to quote curve points versus benchmark instruments is that traders can agree to exchange a position in the curve point (e.g., a paying position in a swap) against the offsetting position in the benchmark (a long position in this example). Such exchanges, which are equivalent to basis trades in a futures contract, have very little outright interest rate risk and can therefore be held for a longer period than each of the two legs alone. As a result, the bid-offer spreads on these trades are tighter for the same notional amount.

In the US case, swap rates are defined by their spread over the relevant on-the-run US Treasury. This market convention has the consequence that swap spreads can jump as a result of new Treasury issuance, namely when the relevant benchmark changes. As in Figure 31.5 on page 351, the driver of such jumps is the yield difference between the old and new benchmark. Because different points on the US swap curve use different benchmarks, which are changing at different times, such jumps occur at different times and in different amounts across the swap curve.

In the Australian swap market, the Australian bond futures are used as reference instruments. Swap rates are often represented as EFP spreads, and trading a swap at the same time as the offsetting position in a futures contract is a common inter-dealer trade. It should be recalled from Section 28.8 that the Australian bond futures contracts are cash-settled basket futures which are quoted in yield terms already. This makes the calculation of the EFP spread very easy and transparent.

The main drawback of par spreads is that they can be affected by differences in coupon conventions between the curve and the instrument that is compared to the curve. For instance, EUR swaps with maturities over two years have an annual fixed payment, which is in line with the coupon frequencies of all euro area government bond markets with the exception of Italy. The par spread between an Italian government bond (BTP) and EUR swaps is therefore misleading because a par BTP with the same coupon rate as a swap has a shorter duration due to half the coupons being paid out half a year earlier.

## 22.3 SWAP SPREADS

When spreads are measured against a swap curve, they can be expressed against the fixed or the floating leg of the swap. A first important difference between these two choices is that both legs usually have different daycount conventions because the floating side is a money market rate while the fixed side is a bond rate. In addition, the two legs can have different payment frequencies (for instance, semi-annual floating against annual fixed in EUR), so that the DV01 associated with a basis point of spread on the floating side is not identical to that on the fixed side. The spreads discussed in the previous section are expressed on the fixed side which a swap curve shares with other curve model. This section adds spread measures that are more specific to the swap market.

## 22.3.1 Asset swap spreads

An asset swap is a trade where two counterparties exchange a floating-rate payment against the cash flows of an asset. Such trades had in the past the connotation of a credit derivative because paying the fixed side in the trade removes all duration risk for the holder of the asset, leaving him or her exposed mainly to the credit risk of the asset. At the same time, asset swaps are used by issuers to remove the duration component of their own liabilities.

<!-- image -->

In principle, an asset swap amounts to a transfer of all cashflows from the asset from the investor to the counterparty, while the counterparty pays the investor the flows on the floating side of a swap with a floating leg of Libor plus a spread x , including a virtual upfront payment of par which is offset by a payment of a reference price of the asset. The asset swap spread is the spread x that makes the package worth zero at inception. Put differently, the investor transfers, in economic terms, to the counterparty the bond at the reference price and receives back a package of floating rate cash flows of equal value. The bond in question need not be a fixed-rate bullet bond but can have any structure (including an FRN).

Asset swaps of this form, also more specifically called par-par asset swaps, involve some degree of upfront balance sheet commitment. The difference between the reference price of the bond and par is an upfront transfer from the investor to the counterparty. If this is positive, then the investor is in effect granting a loan to the counterparty which is amortised via the spread x over the lifetime of the asset. If the price is below par, the loan is from the counterparty to the investor and is equally amortised via the spread.

FIGURE 22.1 Simple fair-value asset swap spread model.

<!-- image -->

Because the balance sheet exposure can be expensive, an alternative form of asset swap, the proceeds asset swap exists. In this type of trade, the notional of the swap is not equal to the par amount of the bond, but its price (the proceeds). This structure reverses the credit exposure because the bond will redeem at par while the notional payment of the swap is not par.

Because asset swaps are very bespoke structures, they do tend to be less easy to enter or unwind than standard swaps.

For low-risk bonds, a fair value asset swap spread can be constructed from an analogy (cf. Figure 22.1). To a speculator, a bond is a contract that pays a periodic coupon in return for regular payment of the repo rate required to fund the bond. A swap resembles this arrangement in that a regular swap coupon is paid in exchange for a regular Libor payment. This analogy implies that the asset swap spread of a bond should reflect the expected spread between the repo rate of the bond and Libor over the lifetime of the bond.

While compelling, this argument has some flaws. The future repo-Libor spreads are unknown and it may well be argued that the asset swap spread is an informative guess of how this spread will evolve, rather than that an assumed repo-Libor spread provides information about the fair value of asset swap spreads. At the same time, no bond is truly free of default risk. The Libor leg of a swap has a built-in survivorship bias (cf. page 337) that is not present in bond repo rates because a defaulted bond has no value as repo collateral. In summary, this analogy is most likely to provide only a floor to asset swap spreads but no point estimate.

## 22.3.2 I-spreads

The interpolated, or I-spread, is a simplified version of an asset swap. Instead of modelling the flows of the bond on the swap curve, one interpolates a rate on the swap curve at the correct maturity point. The interpolated swap spread is then the difference between yield of the bond and the interpolated swap rate. Unlike the asset swap spread, this makes it a fixed-side spread in the fixed-side daycount and compounding convention. In line with standard practice elsewhere, the interpolated swap has a short first, rather than a short last, coupon if the maturity of the bond does not fall on the maturity date of a standard swap. This tends to also involve a short first coupon on the floating rate leg of the swap.

I-spreads are of greater relevance to short-term hedges than asset swaps because the swaps used are par swaps at inception and so are faster to price and have a lower balance sheet cost. At the same time, the potential coupon differences between the bond and swap mean that larger curve movements will create a larger drift between bond and swap value. The trade-off between asset and interpolated swap is therefore one between liquidity and hedge quality.

## 22.3.3 The TED spread

The TED spread, also sometimes called the option-adjusted spread (OAS) is fundamentally different from the spreads discussed so far. It takes its historical name from 2 futures contract strips, namely the 13 week (91 day) T-bill contracts (T) and the 3 month eurodollar contracts (ED), both traded in the Chicago Board of Trade. The TED spread is the amount by which the ED curve needs to be shifted in oder to reprice a given bond. Illustratively speaking, it is the distance by which the ED curve needs to shift to obtain the T curve. The T-bill contract was delisted in July 2014 and the TED spread is now decribed by the CBOT as the Treasury-Eurodollar spread.

Unlike all the spreads discussed thus far, the calculation of this spread requires a change in the discount curve itself, rather than changes in intrument rates or spreads. In practice, this creates difficulties for non-US markets because the contracts equivalent to the Eurodollar contracts (Euribor on ICE, 3M Euroyen on TFX) have only a limited amount of liquidity in reds or further out contracts. TED spreads can therefore not be calculated from the money market futures curve alone. Instead, one shifts the implied forward rates in a market model, and rebuilds the discount curve from these shifted forward rates.