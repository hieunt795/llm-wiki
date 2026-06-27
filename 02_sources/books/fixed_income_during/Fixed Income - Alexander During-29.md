---
title: "Fixed Income - Alexander During-29"
type: raw_source
source_pdf: "Fixed Income - Alexander During-29.pdf"
extractor: docling
---

## PART Five Derivatives

## 28.1 INTRODUCTION

Traditional bond futures are exchange traded contracts where the seller (the short) commits to deliver a given notional amount of a bond out of a certain basket to the exchange and the buyer commits to buy such a bond from the exchange at a specified time. The notional amount to be delivered per futures contract is a fixed quantity, such as 100,000 euros or 100,000,000 yen. Most bond futures contracts are settled through the actual delivery of a bond, hence they are examples of physically settled contracts. This transaction is executed at a price that is given by the final trading price of the contract and a conversion factor that is specific to each bond in each contract. The invoice price for a bond on delivery is given as:

[Invoice price] = [Futures price] ∗ [Conversion factor] + [Accrued interest] (28.1)

There are bond futures contracts that are not settled by physical delivery but by simply closing out long and short positions through a cash payment calculated with reference to the yields of the bonds in the deliverable basket. Such cash-settled contracts usually follow a pricing formula such as:

<!-- formula-not-decoded -->

where wi are the fixed weights and y i the yields on the final trading day of each bond i in the deliverable basket, respectively. The EDSP (short for exchange-determined settlement price) determined the close-out price of the contract.

For both physical and cash settlement, the equivalence of contract and bond market at one point in time is the crucial link between futures contract and underlying market during the entire life of the contract.

The open interest is the total number of long positions in a contract which by definition is equal to the total number of short positions. On some exchanges, including Eurex, it is possible for a trader to hold both long and short positions in the same contract at the same time. This can happen for instance by first selling, and then buying back the same contract but not netting out the resulting position. When netting is not automatic, or implemented with a delay, the open interest will overstate the actual risk held in the contracts.

## CHAPTER 28

## Bond Futures

The motivation to trade futures contracts is that they are usually more liquid than actual bonds. Simply speaking, there are many bonds but only a few futures contracts, so trading in each of the contracts is more active. In the US, where trading in bonds is focused on only a few on-the-run issues, futures can be less liquid than those benchmark bonds. In some markets, such as the market for Japanese government bonds, there are other restrictions, such as taxation or reporting requirements, that cause some investors to use futures contracts instead of bonds to gain exposure to that market. In the bond market, the expression 'cash market' usually refers to physical bonds, as opposed to the futures markets.

Themajority of bond futures contracts are designed to settle through physical delivery. Delivery can occur at any time during the delivery period. In the case of the older bond futures contracts (US and UK), the delivery period is an entire month. Newer contracts (those on Eurex and in Japan) have a single delivery day. Before delivery, the short in the contract notifies the clearing house of the exchange of the intended delivery and the delivered bond is then assigned to one or more long positions. The event of notification has implications for risk management, detailed below.

Physical delivery is also to some degree the default mode of exchange-traded contracts, dating back to the Osaka rice exchange. This settlement approach has a drawback related to surprising instances of insufficiently available supply in the deliverable bonds. Open interest for the most commonly used bond futures contracts tends to be equivalent to a bond volume that far exceeds the available supply of the bond that is most economical to deliver, or even the entire deliverable basket. Contract users relying on the simple cash-and-carry arbitrage to value and risk-manage futures positions therefore face risks related to the delivery mechanism. For many users, however, the actual delivery mechanics have no bearing on the purpose they used the contracts for. Indeed, the vast majority of contracts is closed out before delivery, usually by rolling the exposure into the following expiry (the futures roll is described below).

These difficulties do not arise in cash-settled futures. Whether this makes cash settlement a better design is, however, a complex question.

Physical settlement has a built-in deterrent of attempts to push the contract valuations to extremes. Assume a trader who is long the contract and pushes the price above its intrinsic value to increase the value of the position. The rest of the market can simply react by delivering the CTD to that trader who will end up owning this bond, potentially to maturity, at an inflated entry price. Conversely, a trader pushing the contract price downtosupport a short position might find that the market asks for delivery of the CTD at an artificially low price. Physical delivery, in other words, means that the economic lifetime of the contract does not end with delivery. Physical delivery simply exchanges the futures contract with a physical asset at a valuation determined by the final contract price. The future development of the price of this physical asset can cause problems for those looking to manipulate the futures contract. This being said, the increased cost of managing bond portfolios under more recent regulation also makes it more expensive for the market to actually implement the trades that act as deterrents to price manipulation of physically settled contracts.

Cash-settled contracts, in contrast, provide a clean exit from the contract life-cycle at delivery. While this eliminates the risk of insufficient availability of deliverable bonds, one of the lessons of the financial crisis is that this finality may be problematic. All Libor futures and FRAs are by definition cash-settled contracts, as are the floating rate resets of interest rate swaps. From the public information available from court cases surrounding the Libor issue, some traders allegedly manipulated the Libor fixings in order to move such cash-settled contracts in their favour on the days when contracts they held were expiring. The absence of any direct link of such derivatives to physical assets, such as a deposit with another bank at Libor, arguably reduces the hurdles to such behaviour. Better policing of the way in which reference rates are being set may reduce this problem of cash settlement but it will not eliminate it. For instance, a trader may be willing to make a deposit at an off-market rate in order to shift the fixing of a transaction-based deposit rate benchmark if the size of that deposit is small compared to the derivatives contracts held by the same trader that expire linked to the benchmark.

New information and changes in market composition will continue to change the relative merits of physical and cash settlement. At the same time, it is very difficult to create new futures contracts and attract sufficient trading interest to generate a deep and liquid market in them. For this reason, even somewhat sub-optimal contract designs can remain in use for a long time. Occasional squeezes in physically delivered bond contracts have not reduced the interest in them, just as manipulated fixings have not reduced the interest in trading cash-settled contracts on money market rates.

## 28.2 FUTURES TRADING PATTERNS

## 28.2.1 Open interest and trading volume

Exchanges widely publish aggregate activity measures for the contracts that they offer. Market participants use these to judge the liquidity, and thereby the suitability for hedging and trading, of a given contract. In addition, changes in trading activity can signal changes in investor attitudes. The two measures used are open interest (the total number of long positions which is equal to the total number of short positions) and volume (the number of contracts traded in a given period of time).

It should be noted that open interest figures are not easily comparable across exchanges. On a very basic level, contracts have different sizes. The JPX JGB contracts are for JPY 100 million notional while the German and US bond contracts are for 100,000 euros or dollars, respectively. At current exchange rates, this makes a single JGB contract around ten times larger in value terms than an equivalent US contract. Second, exchanges have different rules for the netting of exposures which are related to their clearing models. US exchanges, which typically operate on an agency clearing model, tend to automatically net long and short positions of the same end users so that a user is either long or short. European exchanges operating under the principal clearing model do not have the required information to do so reliably and may choose to permit the simultaneous existence of long and short positions in the same contract for the same account. This inflates the open interest figures and the degree to which this happens is related to the total amount of trading that takes place from the point in time when a contract is listed 1 . Open interest figures are usually available only with a delay of one or two business days while trading volume can be observed in real time.

Some market analysts closely watch changes in open interest to gauge changes in directional trading interest in the market. For instance, when open interest increases while contract prices fall, one could argue that new risk positions were established through selling of contracts, and that this represents an increase in short positions. Conversely, a decline in open interest in a falling price environment could signal a closing-out of long positions, and so on. While this type of argument sounds compelling enough at first, there are some problems. First, by construction, there is a long position for every short position. The market as a whole is therefore always neutrally positioned, and long or short positioning can at most refer to investors with a greater or lesser risk capacity 2 . Second, open interest is reported daily and market direction can change during a trading day. For instance, if prices fall in the morning, but then rise in the afternoon, any change in open interest during the day could have occurred during the price decline or increase. Using day-on-day price changes and day-on-day changes in open volume not only makes the assumptions outlined above between position changes and market moves, but additionally adds the assumption that the relationship between position changes and price moves is strictly linear. Third, futures contracts are hedge instruments for underlying markets. Even if it were true that higher open interest on a given day with price declines is the result of a new short position in the contract, this short position may be the hedge of a long position in bonds or swaps. It would therefore not have any signalling effect on overall market direction. Fourth, open interest has some seasonality related to roll activity, as further outlined below. One should therefore generally not base directional assumptions on open interest figures. Increasing open interest and volume signals more activity but, because each contract seller requires a contract buyer, the driver of that increased activity is not always clear.

Trading activity has a seasonal pattern related to futures rolls. Contracts only exceptionally go through to delivery and positions are instead rolled from the front contract into the back contract before delivery. Most exchanges have mechanisms that let traders execute rolls, i.e., simultaneous buying of the front contract, and selling of the back contract, in a single transaction. Where this is not desirable or possible, a roll can be 'legged', which means that a trader attempts to execute the two trades separately in a short period of time 3 . The roll activity can be seen in the evolution of open interest in the two contracts, as shown on two examples in Figure 28.1. The open interest in the back contract tends to increase some time before delivery and this process appears to be happening systematically earlier for the CBOT contract. As the back contract open interest increases, the front contract open interest declines. Note that at delivery, the erstwhile back contract becomes the front contract which explains the jumps in front contract open interest in this chart.

1 Unkind minds might suggest that an exchange has an interest to report higher open interest figures given that some market participants views these as a sign of higher activity and better liquidity.

2 In the US market, where the CFTC provides a breakdown of open interest by investor type, perhaps such differentiation could be analysed. See Section 28.2.2 on page 307 for more discussion of this topic.

3

'Legging it' in some parts of London means 'running'.

FIGURE 28.1 Open interest for the front and back contracts during 2017 for the Eurex Bund and CBOT 10Y Note contracts. Sources: Data from Eurex and CBOT.

<!-- image -->

FIGURE 28.2 Daily trading volumes for the front and back contracts during 2017 for the Eurex Bund and CBOT 10Y Note contracts. Sources: Data from Eurex and CBOT.

<!-- image -->

Because rolling is itself a trading activity, total trading volume and, to a lesser extent, total open interest tend to spike during the roll period without there being any associated change in market risk sentiment. As Figure 28.2 shows, both front and back contracts become more active during the roll period, and this increase in activity is particularly pronounced for the back contract which rarely trades ahead of the roll. Exchanges generally publish total trading volume for all expiries and these figures show large spikes before delivery.

One way to construct volume series that are adjusted for roll activity is to consider that a roll trade creates one trade each in the front and back contracts while any outright trade will only generate a single trade in the active contract. This means that the better measure of activity is the difference between the daily volumes in the front and back contract, at least as long as the whole market considers the same contract as active for each day. Because it is not clear whether the front or the back contract is the most active, one can simply subtract the smaller of the two volumes from the larger of the two. Figure 28.3 shows that this difference measure does avoid the spikes around delivery that appear in the total volume figures. This measure underestimates activity when bothbackandfrontcontractsareusedforoutright trading, which happens when market participants differ in the timing of their roll activity.

FIGURE 28.3 Daily trading volumes (totals and maximum-minimum measures) for the Eurex Bund and CBOT 10Y Note contracts. Sources: Data from Eurex and CBOT.

<!-- image -->

Future roll activity can to some extent be predicted based on historical patterns. Some investor types, particularly futures specialists known as commodity trading advisors (CTAs) tend not to hold futures contracts when it could be possible that they would have to take or make delivery. They therefore execute their rolls before the start of a delivery window. Monitoring the progress of the roll provides a gauge of how much there is still left to do. The standard way to monitor rolls is to calculate the share of back contract open interest in the total open interest, as in Figure 28.4. This chart shows that there are clear differences in behaviour between different contracts. Note that US contracts can be delivered on any good business day during the delivery month while the Eurex and JPX JGB contracts have only a single delivery day. This means that a CTA would have to have closed out front contract positions before the expiry month of a US contract to rule out having to take delivery. Further, the somewhat less active BTP contract on Eurex appears to be typically rolled later in the delivery cycle. It should be noted that this observation could partly be explained by the overstating of back contract open interest due to the absence of netting as mentioned above.

FIGURE 28.4 Roll progress histories for the Eurex Bund and 10Y BTP and CBOT 10Y Note contracts. Sources: Data from Eurex and CBOT.

<!-- image -->

## 28.2.2 CFTC data for US futures contracts

The US market is peculiar in having a public system of position reporting by investor type. The Commodity Futures Trading Commission collects and published on its website weekly data on open futures positions. It is therefore possible to some extent to analyse the behaviour of some major investor classes in the market.

Some caveats should be borne in mind, however. Investors are broken down into four classes ('Dealer', 'Asset Managers', 'Leveraged Money', and 'Others') and reporting is by contract, but not by expiry. The data is published with a lag of about one week and does not cover all positions (adjustment series for 'non-reported' positions are part of the publication). From Figure 28.5 it is visible that the identified investor classes comprise between 35 and 45% of the total open interest in the 10Y note future used here as an example.

FIGURE 28.5 CFTC net positions (long minus short) in the CBOT 10Y note futures contract over time for three investor types. The thin dotted line, plotted against the right axis, shows the share of these positions in the total open interest (calculated as all longs plus all shorts of these three investor classes divided by the sum of all longs and all shorts). Source: From CFTC.

<!-- image -->

FIGURE 28.6 CFTC net positions (long minus short, in thousands of contracts) for Asset Managers and Leveraged Money in the 10Y note contract. Data period 2010-2019. Source: From CFTC.

<!-- image -->

Several details of these series are interesting. The net position of dealers is not uniformly short as would be expected in other markets (Europe and Japan), and it is indeed marginally long on average over the history shown here. Given that the default position of a European or Japanese dealer is to own bond inventory and sell futures to hedge this inventory, dealers should not normally have a net long position in futures contracts. In the US market, however, the on-the-run Treasury bonds are so liquid that they are used for inventory hedges to a much larger degree than in other markets. As will be explained further below, an additional factor may be misclassification in the split between dealers and speculators in the sense that some speculators are actually acting like dealers. Equally, the observation that asset managers are sometimes significantly short implies that futures contracts are not only used for the reduction of cash drag.

Despite the caveats of the CFTC data, the 'Leveraged money' (often called 'Speculators') series attracts some attention as a guide to future market developments. Market analysts are perennially looking for the 'pain trade' which is the speculative position that is crowded and therefore at risk of a fast unwind when prices move against it. The problem with using the CFTC series for this purpose is that the 'Speculators' position is not necessarily driven by active speculation.

Figure 28.6 demonstrates that the 'speculators' positioning follows more or less inversely the positioning of the asset managers. It is therefore conceivable that some speculators act as a bridge between the cash market and the futures market, i.e., provide liquidity in the futures basis.

This observation could also explain the developments in the US Treasury market during the well-publicised spike in repo funding rates in September 2019. This spike in rates occurred despite a significant level of liquidity 4 in the system, which meant

4 Liquidity is here used in the European sense of current account holdings at the central bank. In the US, the term 'reserves' is used for the same concept.

FIGURE 28.7 SOFR and CFTC positioning (speculator net positions across all US Treasury contracts) and US Treasury market liquidity (cf. Figure 18.3). Sources: Data from CFTC, TreasuryDirect, Federal Reserve Bank of New York.

<!-- image -->

that the Federal Reserve System waited one day before conducting liquidity-providing operations to address the funding stress. In essence, the spike in repo rates can be seen as the result of a demand for funds in the repo market that came from market participants outside the purview of the supervision exercised by the Federal Reserve. A good candidate group of participants is the so-called principal trading firms (PTFs) who are financial firms that trade for their own account on various trading platforms. PTFs usually hold themselves out as liquidity providers and post quotes on electronic platforms. PTFs can trade high volumes even with little of their own capital because the counterparty risk in Treasury trading is mitigated through central clearing and and very short settlement cycles. PTFs could be using US Treasury futures contracts for hedging just like dealers in other jurisdictions, but because they are not classified as dealers for CFTC purposes, these hedges show up as net shorts in the speculative positions.

Position funding for PTF takes place in the repo market, and increasingly via sponsored access clearing on FICC which limits the visibility of this funding for the Fed. In this setting, funding stresses in the repo market can have spill-overs into the market for US Treasuries because a given class of market makers, the PTFs, find it harder to operate.

Conversely, stresses in the funding market may manifest themselves in the liquidity of US Treasuries before they show up as spikes in repo funding rates. If this assumption is correct, then the spike in SOFR on 16 September 2019, which was followed by Fed liquidity injections from 17 September, was merely the climax of a deterioration in market conditions that started earlier in September and manifested itself in reduced hedge volumes in the futures contracts and more variability in US Treasury spline spreads. It should be noted, however, that the reduction in CFTC short positions over the course of was equivalent to USD 35bn while the size of Fed operations was significantly higher, namely USD 75bn initially, rising to over USD 250bn by the end of October. The PTF connection can therefore only be one part of the total picture.

## 28.3 VALUATION OF PHYSICALLY DELIVERED BOND FUTURES

Because a futures contract establishes the obligation to deliver a bond at a given point in time, at that point the contract and the bond that will get delivered are identical in economic terms. Out of a basket of bonds, usually one issue is most economical to deliver and this issue is called the cheapest to deliver (CTD). The sellers (shorts) of the contract can select which issue to deliver, so they will usually deliver the CTD. The convergence in value of the CTD and the contract is the essential feature of a futures contract. Only because of this convergence is there a pricing relationship between the futures contract and the bond market. Without such a relationship, futures would not be a useful hedge instrument.

Acorollary of the requirement that CTD and futures contracts converge at the point of delivery is that there must be a well-determined relationship between the spot price of any deliverable bond and its forward price for the delivery period. This means that there must be a deep and liquid repo market in order for a futures market to exist. Put differently, a futures contract will fail to attract genuine trading interest unless there is an existing and working repo market for the underlying bonds. An example for such a failure was the Eurex medium-term Euro-Jumbo Pfandbrief contract launched in June 1999.

## 28.3.1 Basis and implied repo rate

There are three ways to express the difference in the current valuation of a futures contract and the underlying bonds, namely gross basis, net basis and implied repo rate. All three measures can be transformed into each other using market information, so they represent the same information in different ways. Which representation is the most appropriate depends on the application. These quantities are introduced first in schematic fashion and the exact mathematics will be delivered later.

Thegross basis is the difference in price between a given bond and the price implied by the futures contract and it is calculated as:

<!-- formula-not-decoded -->

Because the contract and the bonds both move with interest rates and in the same direction, the gross basis is a lot more stable than bond prices or futures prices themselves. The expression basis is also used for a combination of bond and future that is traded in a single transaction 5 . In line with the signs in Equation (28.3), 'buying the basis' means buying the bond and selling the equivalent number of futures contract while 'selling the basis' means selling the bond and buying the future 6 .

5 In practice, the two counterparties agree on the basis trade and then settle the bond leg in the usual way while the futures leg of the trade is given up to the futures exchange ('crossed' on the exchange), bypassing the public order book.

6 A helpful mnemonic device for this sign convention is that bond and basis start with the same letter.

The gross basis of deliverable bonds is traded very actively and at relatively low bid-offer spreads. The high liquidity arises from the very low directional interest rate risk that is contained in a basis trade. It has become quite common in the European bond market to define conversion factors even for non-deliverable bonds so that basis trades can take place even for those securities. Such conversion factors are usually calculated using linear regression, rather than the exchange-defined formulas discussed earlier.

The futures price reflects the price to be paid for a bond on delivery date, i.e., a date in the future, so the gross basis contains an element of carry between the spot settlement date and the futures delivery date. Replacing the spot cash price in Equation (28.3) with the forward price of the relevant bond to delivery, gives the net basis:

<!-- formula-not-decoded -->

From this definition follows:

<!-- formula-not-decoded -->

The net basis of the cheapest to deliver (CTD) issue is usually very close to zero, at least when the CTD is relatively clear. This is because the market prices the spot price and the repo rate with the assumption that the CTD will get delivered and will therefore be equivalent to the contract on that forward date. On delivery day, net and gross basis are identical and reflect the profit or loss from delivering a bond into a short futures position. This profit or loss should be zero for the CTD, while delivering a different bond should lead to a loss equal to the net basis of that bond 7 . This provides a way to calculate the fair value of a futures contract, called the cash-and-carry arbitrage, explained below.

The third quantity expressing the relationship between futures price and bond prices is the implied repo rate (IRR). This repo rate is the financing rate that makes the net basis zero. In other words, it is given by solving the equation:

<!-- formula-not-decoded -->

for the repo rate. The intuitive interpretation of the implied repo rate is that it is the financing cost at which one can buy the relevant bond against the futures contract and later go into delivery without making any profit or loss. There is no reason why the implied repo rate of any given bond should be related to actual market repo rates and implied repo rates can have large negative values. The implied repo rate of the CTD is usually very close to the actual market repo rate while the other deliverable bonds have lower implied repo rates than their market repo rates. Intuitively, this expresses the same information as the net basis. A positive net basis means that with current prices and repo rates it would be uneconomical to deliver that bond. The implied repo rate shows where the repo rate would have to be to eradicate that loss while the net basis shows how much the spot price would have to move relative to the futures contract to achieve the same effect.

7 Note that physical delivery means that technical factors can influence the actual performance of this strategy. This is explained in more detail in the section on futures squeezes.

In the US market, where special repo rates for deliverable bonds do not move too much, it is quite common to use the implied repo rate as an indicator of CTD status and to call the bond with the highest implied repo rate the CTD [18]. This indirect argument can be misleading, however, and is frequently wrong in the euro area bond markets where CTDs can trade at very special repo rates.

## 28.3.2 Conversion factors and the notional coupon

So far, conversion factors were presented as abstract numbers but it is now time to explain them in more detail. The motivation to introduce conversion factors becomes clear if one sets the conversion factor for each bond in Equation (28.8) to 1. The futures price would then be a simple clean price and the bond with the lowest cash price at delivery would be the CTD. This would usually be the bond with the lowest coupon. In other words, the futures contract would in most cases be simply a forward contract on the deliverable bond with the lowest coupon. Such a situation is unsatisfactory because it negates the purpose of having a deliverable basket of bonds. At least in principle, all deliverable bonds in the basket should have some chance of getting delivered so that their pricing interacts with that of the contract.

Simply speaking, conversion factors are the mechanism to equalise bond prices in relation to the futures contract to make it more likely that multiple bonds are similarly economical to be delivered.

This aim is achieved by setting the conversion factor of a bond equal to the clean price the bond would have if it traded at a particular yield on the delivery day of the contract. Unfortunately, this particular yield is called the notional coupon of the contract, which causes a lot of confusion.

Starting on a more mathematical treatment of the futures contracts, one defines the conversion factor c i , tD of bond i in the basket of a contract with delivery date t D and notional coupon C as:

<!-- formula-not-decoded -->

which is nothing but Equation (16.10) using C instead of the yield 8 .

One can then write the invoice price I i , tD from Equation (28.1) using the futures price F as:

<!-- formula-not-decoded -->

to find that if one inserts Equation (28.7) into this equation it becomes:

<!-- formula-not-decoded -->

8 Each futures exchange publishes its own specific formula for Equation (28.7) which may take account of local yield conventions, etc.

FIGURE 28.8 Behaviour of converted bond prices under a parallel downwards yield shift. The sample shows four bonds in the deliverable basket with different durations. The price of the bond with the lowest duration will react least to the yield shift, making it more likely to be CTD.

<!-- image -->

This equation becomes interesting when all bonds are in fact trading at a yield of C so that their invoice prices are equal to their market prices. One then finds

<!-- formula-not-decoded -->

This equation permits only one solution, namely F = 1. In other words, if all deliverable bonds were trading at a yield equal to the notional coupon, the futures contract would be trading at a price of 100 (futures contracts are quoted in percent of notional just as bonds) and all deliverable bonds would be equally CTD. A bond would be more likely to be CTD if its forward price was below that of other bonds, i.e., the CTD status would indeed be associated with relative cheapness of a particular issue, not its coupon or other details. This is precisely the purpose of conversion factors.

However, the assumption that bond yields are always close to the notional coupon is not necessarily true and indeed not true for most contracts. Notional coupons on the world's main bond contracts are 6% and market yield levels are below this level. This has an impact on the CTD status of the bonds in the basket as shown in Figure 28.8. The left hand side shows the converted forward price, i.e., the forward price divided by conversion factor, of each of four bonds in a hypothetical basket under the assumption that the forward yields are equal to the notional coupon. In this situation, the future trades at 100 and all bonds are equal CTD.

The right hand side shows the same four bonds after a parallel downmove in yields. Intuitively, they are still equally expensive because they still trade at the same yield. However, they are no longer equal CTD because their prices have moved by different amounts but the conversion factors are still the same. The bonds with the highest duration will move most in price and therefore the bonds with the lowest duration are cheaper to deliver. When yields move down, therefore, low duration bonds are more likely to be CTD than higher duration bonds.

Asmentionedabove, the European market quotes bases for bonds that are not actually deliverable and therefore have no conversion factor as such. Instead of using the same Equation (28.7), which is of course valid for any bond regardless of deliverability, the market convention is to use a regression analysis to find the price sensitivity of the bond relative to the future. This means solving the regression equation:

<!-- formula-not-decoded -->

and using /u1D6FD as the conversion factor. Because bases are only comparable through time if the conversion factors stay constant 9 , the time window across which the regression is run is usually fixed, often to some period before the futures contract becomes the front contract so the conversion factors can be used from the start of active trading in the contract. This procedure is not ideal because the regression /u1D6FD is not very stable, in particular because the liquidity of the futures contract during the time when the regression data is sampled is not very high. However, the procedure can easily be executed using just market data and avoids the necessity of conducting the analytical calculation outlined above.

## 28.3.3 The cash-and-carry arbitrage

The cash-and-carry arbitrage is the theoretical trading strategy that links the calculations done so far with actual market prices and repo rates. The strategy consists of buying a deliverable bond, selling an equal notional of bond futures against it, financing the bond in the repo market, and delivering the bond into the short futures position at expiry of the contract. Delivery is economically equivalent to selling the gross basis (which on delivery day is equal to the net basis) at zero, so the cash-and-carry arbitrage will break even only for zero net basis.

However, the strategy is the starting point for futures contract analysis and in particular for the valuation of the future relative to the cash bond prices. The standard way to do this is a so-called basis sheet which takes the deliverable basket of a contract together with all pricing data and calculates the necessary forwards. A sample basis sheet is shown in Table 28.1.

The sample shows an interesting point: The range of converted forward prices (106.554 to 106.946) is narrower than the range of spot prices (99.363 to 100.249). This is precisely the effect that conversion factors are there to achieve, namely to bring the deliverable issues closer in price relative to the future. The bonds shown here have very similar coupons and the effect of the conversion factors would be stronger for a wider coupon range.

For the purposes of a fair value calculation of the futures price, one would use the converted forward price of the CTD. This is the price at which one could sell the future today, buy the CTD bond at today's cash price, lend it out for financing at the specific repo rate, and go to delivery.

As will be discussed in more detail later, there are practical caveats to this calculation. The repo rates quoted for 'term' in the repo market are usually for bond lending until after the delivery. This means that a trader who obtains financing in a repo contract to 'term' will not have the bond available for delivery and therefore will fail towards the exchange. Even if the bond is lent out to just before delivery, a trader engaging in cash-and-carry arbitrage faces the risk that the repo counterparty does not return the bond in time. Taking the arbitrage calculations shown here at face value is therefore not without risks. The structure of this chapter will therefore be to start from the simple concept of pure arbitrage and then introduce the deviations that arise from various features that deviate from an ideal market.

9 Equation (28.7) provides this because the spot settlement date does not enter the calculation.

TABLE28.1 Sample basis sheet analysing a fictitious bond futures contract modelled on the Eurex contracts. CF stands for conversion factor, CFP for converted forward price (forward price divided by conversion factor), NBasis for net basis. The interest rate levels in this example are very far from actual interest rates on the analysis date.

| Analysis date:        | 14 Apr 2020   |
|-----------------------|---------------|
| Settlement date:      | 16 Apr 2020   |
| Delivery date:        | 10 Jun 2020   |
| Notional coupon:      | 6.0%          |
| Futures close:        | 106.573       |
| Fair value:           | 106.553       |
| Quality option (cts): | 0.2           |
| Contract PVBP:        | 7.771         |

| Bond          |   Price |   Yield |   Repo |       CF |     CFP |   NBasis |
|---------------|---------|---------|--------|----------|---------|----------|
| D4.875% 01/29 |  99.446 |   4.950 |   2.00 | 0.925874 | 106.946 |     36.3 |
| D5%07/29      |  99.904 |   5.010 |   2.00 | 0.931507 | 106.781 |     21.1 |
| D5%01/30      |  99.363 |   5.080 |   2.00 | 0.928327 | 106.554 |      0.0 |
| D5.125% 07/30 | 100.249 |   5.090 |   2.00 | 0.935186 | 106.711 |     14.6 |

## 28.3.4 The quality option

In principle, it is unclear what bond will be cheapest to deliver at the time a bond future expires. If there can be a change in the CTD, it may be profitable to sell the contract and buythecurrentCTD.IftheCTDchanges,onecanthensellthatbondandinsteaddeliver the new, now cheaper to deliver, issue.

The existence of this trading strategy means that the futures contract is less attractive to hold than the CTD. Therefore, the fair value of the CTD net basis should be slightly positive. In other words, the future should be slightly cheaper than the converted forward price of the CTD. This is equivalent to an option premium and this option is called the quality option 10 .

Because conversion factors only partially compensate for differences in bond details (maturity date and coupon rate), and large shifts in yields have the effect on net bases outlined in Figure 28.8 on page 313, the quality option is reflected in an option-like pay-off structure of net bases shown for an example in Figure 28.9.

10 This may not be an obvious name for the right to choose between bonds that are basically identical in quality. However, the name is carried over from commodity contracts where there are important economic differences between different varieties of deliverable products, such as lean hogs. In these markets, conversion factors or add-ons are applied to different grades of deliverable products in order to reduce the arbitrage opportunities between differing product grades.

FIGURE 28.9 Net bases (in cents) of the deliverable bonds in a futures basket as a function of parallel yield shifts.

<!-- image -->

At low yields, the CTD status is being pushed to the lowest duration bond, so that the net basis of this bond looks like a call option on yields (or, equivalently, a put option on bond prices). At high yields, the CTD status shifts to the highest duration bonds so that the net basis of that bond appears like a put option on yields. The net bases of the two bonds with intermediate durations look like straddles.

Because every net basis has the pay-off of an option, the net basis of any bond must in theory always be strictly positive, i.e., larger than zero. In practice, the probability of a yield shift induced CTD switch may be so small that its value is close enough to zero not to be tradeable. In this case, the net basis of the CTD is zero and that is indeed how the fair value of futures contracts is calculated by many market participants. Note also that, when there is a perceived risk of delivery failure, the net basis of the CTD can be negative. The section on squeezes below explains this in more detail.

Because the quality option embedded in a future has itself an interest rate sensitivity, the total interest rate sensitivity of the future can have interesting properties. This is relevant for hedging with futures and will be discussed in the next section.

## 28.3.5 Hedging with futures

Thehighliquidity of bond futures contracts in most markets makes them an ideal hedge instrument. To construct a hedge for a given bond means to find the number of futures contracts that provides the same, but opposite exposure to interest rate movements. Assuming that there is a single yield y that drives the movements in price of both the bond and the future, this means finding the number /u1D706 so that:

<!-- formula-not-decoded -->

Here, NF is the notional amount of the futures contract.

The bond's sensitivity to yield changes is given by the PVBP of the bond. So far, however, it is not clear what the interest rate sensitivity of the futures contract price F is, because a futures contract does not have a yield. The essence of this section is therefore to discuss the calculation of the PVBP of a futures contract.

If there is a clear CTD situation, the futures contract is a simple forward contract on the bond, so one can try to extract the future's price sensitivity from information about the CTD. It is possible to calculate the sensitivity of the forward price of the CTD with respect to changes in the forward yield on the delivery date, i.e., one can calculate the quantity:

<!-- formula-not-decoded -->

for the CTD forward price and yield. In a clear CTD situation, the futures price is given by:

<!-- formula-not-decoded -->

so, by combining the last two equations:

<!-- formula-not-decoded -->

This links the futures sensitivity to changes in the forward yield of the CTD to the forward PVBP of the CTD. While this is already close to what is needed, it still does not give much information about the spot sensitivity. In common market practice, this problem is simplified by assuming that:

<!-- formula-not-decoded -->

in other words, that the sensitivity of the forward price of the CTD with respect to changes in the forward yield is equal to the sensitivity of the spot price to the spot yield. This assumption is not totally wrong because the impact of a 1 cent price change in the spot price is equal to a 1 ∗ ( 1 + r ∗ DCF ( spot , forward )) cent price change in the forward where r is the applicable repo rate. This means that:

<!-- formula-not-decoded -->

The quantity PVBP CTD ∕ c CTD , tD is called the converted PVBP of the CTD and Equation (28.17) implies:

<!-- formula-not-decoded -->

This means in particular that the hedge ratio for the CTD itself is simply given by the conversion factor. Note that this implies that the cash-and-carry arbitrage trade has interest rate risk because the delivery mechanism implies a hedge ratio of 1.

When the quality option of the futures contract plays a role (i.e. if there is a meaningful chance of a CTD switch) Equation (28.17) is no longer appropriate. Indeed, because lower yields tend to favour lower duration bonds for CTD status and higher yields favour higher duration bonds, the futures contract can exhibit a phenomenon known as negative convexity, i.e., a rising PVBP when yields decline, and vice versa. This is the opposite of a bond.

The following examples use a stylised deliverable basket containing four bonds for a futures contract with a 6% notional coupon expiring on 10 Jun 2020. The bond details with pricing are given in Table 28.1 and, unless stated otherwise, the analysis takes place for settlement on 16 April 2020. Yield volatility is assumed to be 40% lognormal annualised.

Figure 28.10 shows the PVBP of the futures contract given in Table 28.1 as a function of parallel yield shifts. At very low yields (high futures prices), the contract CTD is clearly the lower duration bond and the future behaves more or less like that bond, in line with Equation (28.17). Conversely, at higher yields, the higher duration bond is CTD and again the contract tracks this bond so that Equation (28.17) can be used. Around the yield level where the CTD situation is less clear, however, the futures contract duration falls when the futures price increases, which is the opposite of how a bond behaves.

This negative convexity is a problem for hedging because it leads to a drag on hedge performance. Starting from a perfectly hedged position of short bond, long futures contracts with a zero net PVBP in a negative convexity situation as described above, a decrease of bond prices will drive a decrease of the futures price and the two effects cancel out. However, while the decrease in the bond price would decrease the duration of that bond, the PVBP of the futures contract would increase. The position would therefore no longer be hedged and instead have a long duration. Futures contracts could

FIGURE 28.10 Spot PVBP of a futures contract for a simple deliverable basket. To highlight the role of the CTD switch, the spot PVBPs of the individual bonds are shown as well.

<!-- image -->

FIGURE 28.11 Fair value of the quality option for the standard basket Table 28.1 as a function of parallel yield shifts.

<!-- image -->

be sold to re-adjust the hedge but note that these sales would take place at the new, lower price. If bond prices then move back up to their original level, the hedge would be short duration. Futures contracts would have to be bought back, at the new higher level. For both upwards and downwards moves, the long future-short bond position loses money every time the hedge is adjusted to remain PVBP-neutral.

The conclusion is that a trader would ask to be paid to enter this type of position in anticipation of the convexity drag. In other words, the trader would pay less for the future than implied by the cost of the bond. This statement is equivalent to the one made when discussing the quality option: the net basis of any bond is in theory strictly positive. The equivalence here is the same noted by the Black-Scholes theorem, namely that the price of an option is equal to its expected hedge costs. Figure 28.11 shows the yield dependency of the fair value of this option, seen from the perspective of a long CTD basis position. At very high and very low yields, the quality option is worthless. In the negative convexity area, it becomes meaningful. The reason that there are only 2 local minima in this chart, despite 3 CTD switches in Figure 28.9, is that the economic value of a CTD switch between the middle 2 bonds happens to be relatively low in these examples.

Most contract users do not conduct detailed analyses of futures PVBP because the computational effort is substantial. At the time of writing, market yields are also so far below notional coupons that the chances of CTD switches are very low. The standard approach is therefore to simply treat the future as a forward contract on the CTD and equate the futures PVBP with the PVBP of the CTD, divided by the CTD conversion factor. This adjustment is essential given how the invoice price of a contract is calculated. As long as no CTD switches occur, the approach is unproblematic.

Alternatively, at least one large data provider takes a more direct approach to futures PVBP (and yields) by taking the contract definition literally and treating the future as a forward contract on the notionally deliverable bond. For instance, since the Eurex Bund contract is a 10Y contract with a 6% notional coupon, the future is treated analytically as a forward on a fictitious 10Y bond with a 6% coupon at time of delivery. This approach has the advantage that a yield for a futures contract can easily be derived (it is simply the yield of the fictitious bond). The disadvantage is that what is actually deliverable is someting completely different. In the case of the Eurex Bund contract, the actual CTD has a maturity of between 8.5 and 9 years at delivery (longer bonds are deliverable but unlikely to be CTD at current market levels). The shorter maturity of the actual CTD means it has a lower PVBP than the fictitious bond. This effect is somewhat counteracted by the higher coupon of the fictitious bond relative to actual current coupons. However, as Figure 28.12 shows, these two errors do not quite compensate for each other.

FIGURE 28.12 Futures PVBP approximations as a function of yield shifts. The converted CTD PVBP performs well in clear CTD situations (very high and very low yields) while the fictitious bond approximation is usually incorrect, particularly at low yields.

<!-- image -->

Aside from hedge costs, negative convexity has a second effect related to the time decay of the quality option. As time approaches the delivery date there is less of a chance for yields to move so much as to cause a CTD switch. It therefore becomes more likely that the CTD becomes relatively obvious and the futures contract PVBP moves towards the converted PBVP of that likely CTD. Figure 28.13 shows this effect.

The setting of Figure 28.13 is somewhat arbitrary in that the futures price is assumed to remain constant to isolate the time decay of the quality option. The evolution of the converted PVBP of the 2 bonds is shown for the futures price level where they are the CTD. Both decline over time as they move closer towards their own maturity. Far from delivery there is a high chance of a CTD switch and the contract has a PVBP roughly between those of the 2 bonds. As time passes, the contract drifts towards either of the 2 deliverable bonds, finally converging to what is implied by Equation (28.17). This means that hedges need to be adjusted even though Equation (28.17) would suggest that they do not.

At the time of notification, a position in the futures contract irrevocably turns into the corresponding notional amount of the delivered bond. This creates a significant change in interest rate risk for the position. Prior to notification a 1 bp move in interest rates creates a profit or loss equal to the converted DV01 of the CTD times the size of the notional position as given by Equation (28.15) 11 . After notification, the P&amp;L is simply equal to the actual DV01 of the notified bond times the delivered amount. If, as is currently the case in most markets, notional coupons are far from actual coupon rates, and conversion factors therefore are very different from 1, this creates a sizeable jump in risk.

FIGURE 28.13 Spot PVBP of the futures contract from Figure 28.10 but as a function of time for just two different price levels in the negative convexity area.

<!-- image -->

## 28.4 FUTURES ROLLS

Usually, only a small share of bond futures contracts (small single digit percentages) are held to expiry and go through the delivery process. The bulk of positions is closed out by a process called rolling: holders of the contract that is about to expire simultaneously close this position through offsetting trades and re-establish the same risk exposure in the next expiry of the same contract. Most exchanges therefore allow the trading of the spread between different contract expiries, for instance between the March and June expiries, in a single trade.

The roll of a futures contract is the spread between the first and second expiry contracts, also known as the front and back contracts. In the parlance of exchange trading, the roll is known as a calendar spread 12 .

The roll is given by the equation 13 :

<!-- formula-not-decoded -->

11 Notification is for spot delivery and the likelihood of a CTD switch should be zero at that point for contracts with a single delivery day, or close to it in case of contracts with a longer delivery window.

12 Calendar spreads are a slightly more general concept because the contracts involved need not be sequential.

13 The mnemonic of this equation is that the front contract is infront of the back contract in this subtraction.

Because the carry on deliverables is positive in normal curve environments, bond futures usually trade in backwardation, i.e., the back contract is cheaper than the front contract and the roll is positive. The futures roll can be in contango when the CTD of the back contract is a different bond from the front contract CTD.

Because so many contracts are rolled rather than settled at expiry, the accurate valuation and risk management of the roll is essential for bond futures users. Fortunately, the roll is simply the difference between two contracts, and the valuation and risk calculations for these contracts have been dealt with in detail already. The main feature to look out for in any futures roll is whether there is a change in CTD because the front contract CTD falls below the minimum maturity specified in the contract specification. In addition, newly issued bonds may enter the deliverable basket of the back contract before its expiry. This analysis uses the delivery basket of Table 28.1 for front and back contracts but removes the shortest bond (D 4.875% 01/29) from the back contract basket for the examples involving a CTD switch. The delivery date of the back contract is assumed to be 10 September 2020, i.e., 3 months after the front contract delivery.

The quality option affects the roll even when the front and back contract have the same CTD because the probability that the CTD changes is usually higher for the back contract given that there is more time for yields to move. This means that even if all inputs to the carry calculation remain unchanged (or rather, move in line with the implied forwards), the roll should change through time because the time decay of the quality option is different for the 2 contract expiries (Figure 28.14).

Importantly, the roll fair value is sensitive to changes in the overall yield level for 2 reasons. The first is that the discount rate applied to deliverable bond cash flows for the purpose of calculating the conversion factors is the notional coupon. When this notional coupon differs from actual market yields, the time difference between front and back delivery creates a valuation difference (cf. Figure 28.15). The second is that if the CTD in the front contract is not the same as in the back contract, usually because the front contract CTD is not deliverable in the back contract, the duration risk of the CTDs will be different. Figure 28.16 shows this second sensitivity for the standard basket used here in the 2 roll scenarios (shortest bond drops out or not). In higher yield scenarios, the longest bond in the deliverable basket is CTD so the removal of the shortest bond has no impact. In low yield scenarios, the shortest bond is CTD in the front contract. Its absence in the back contract then leads to a larger difference in the roll fair value.

FIGURE 28.14 Futures roll with CTD change (shortest bond drops from the basket) through time. Disregarding the CTD switch option, the roll fair value is constant through time in this simulation where spot prices and repos simply follow the forwards. The time decay of the CTD switch option, however, means that the roll fair value changes through time when the option is taken into account.

<!-- image -->

FIGURE 28.15 Futures roll without CTD switch through time. Essentially the picture is unchanged relative to Figure 28.14 but the option-free roll value is different and here simply reflects the carry of the front and back contract CTD over the period between the 2 delivery dates.

<!-- image -->

FIGURE 28.16 Sensitivity of the futures roll to parallel yield changes. The kinks in the lines correspond to spikes in the quality option valuation due to the limited number of simulations used.

<!-- image -->

The difference in yield sensitivity between front and back contracts means that a contract user will not normally roll a position one for one. After all, the total futures position normally corresponds to a fixed amount of risk that needs to be hedged. When the back contract has a higher PVBP than the front contract, fewer back contracts need to be bought or sold than front contracts are sold or bought. The PVBP-neutral roll ratio is simply the ratio of the front and back contracts (cf. next section).

An alternative yield sensitivity measure of the roll is the amount by which yields have to move to change the fair value of the roll by 1 cent. This yield difference ∆ y is simply:

<!-- formula-not-decoded -->

Note that this measure is undefined when both contracts have the same PVBP as is for instance the case for cash-settled futures.

## 28.4.1 Roll ratios

While the value of the roll is expressed as a price difference, a futures hedge position is not usually rolled one for one. As the previous section has discussed, the difference in PVBPoffrontandbackcontractsmeansthattherollitselfisdirectional. A PVBP-neutral roll strategy requires that the risk in the front contract is matched with the risk in the back contract, not that the amounts match. In essence, the necessary condition is:

<!-- formula-not-decoded -->

which means that the PVBP-neutral roll ratio is:

<!-- formula-not-decoded -->

Typically, the roll ratio so defined is lower than 1 which means that the number of back contracts that need to be bought or sold to offset a given position in the front contract is less than the number of contracts in the front contract. This is because the back contract CTD tends to be the same or a longer bond than the front contract and so the back contract PVBP is usually higher than the front contract PVBP.

Before moving on, this observation raises a question: namely, Why if rolling futures contracts results in a reduction in positions due to a roll ratio of less than 1, do futures contracts still have any open interest? After all, a geometric series with a multiplier of less than 1 should converge to zero. The answer is that while existing bonds, including the CTDs of future contracts, have diminishing duration risk, new bonds appear all the time. In the long run, the average duration of new bonds must exceed the average duration of existing bonds or else the total market duration would shrink over time. Hedging these new bonds requires selling more futures contracts. The hedging of these new bonds is one reason why the open interest of individual bond futures contracts increases gradually over time, as shown in Figure 28.1 14 .

14 Depending on the exchange, a second reason can be deferred netting of long and short positions held by the same investor.

FIGURE 28.17 Sensitivity of the futures roll ratio (back contracts per 100 front contracts) to parallel yield changes. Shown are 2 scenarios, one where the delivery baskets are identical and one where the shortest bond of the front delivery basket is no longer deliverable into the back contract.

<!-- image -->

This equation for the roll is simple in principle but complex in the presence of a CTD switch option. As shown in Figure 28.10, the PVBP of a futures contract changes near the price levels where the CTD switches. If both front and back contracts are close to CTD switches, the price levels where these switches happen are unlikely to be exactly the same. As a result, the PVBP-neutral roll ratio can fluctuate in complex ways.

Figure 28.17 shows the PVBP neutral roll ratios for the 2 types of contract roll used so far, 1 where the baskets of front and back contract are identical, and 1 where the shortest bond in the front contract is not deliverable into the back contract. For the changed basket at low yield levels (when the convexity bias of the contract favours shorter bonds for CTD status), the roll ratio is less than 1 because the shortest bond in the back basket is longer than the shortest bond in the front basket. This is the effect of basket changes on roll ratios discussed above. For the unchanged basket, the same bond is CTD in front and back contract and the roll ratio is therefore very close to one-for-one. Only the discounting effect embedded in the conversion factor calculation creates a small difference in contract PVBPs. At higher yields, the CTD switches to longer bonds, and these longer bonds are present in both the front and the back contract baskets. The roll ratios of both unchangedandchangedcontractsconvergetoeachother,andalsotowardsone-for-one. Only at much higher yields is there again a deviation from a one-for-one roll ratio, this time caused by convexity effects.

## 28.4.2 Advanced futures delivery models

The delivery option model used in this section is a simple 1-factor model where CTD switches arise only from the effect parallel yield shifts have via the basis effect. In general, 10,000 simulations of future yield scenarios have been used to generate the charts seen so far. Such a model is appropriate for a textbook but not for real risk management systems. In reality bonds exhibit idiosyncratic movements that increase the probability of CTD changes. Particularly for very long futures delivery baskets, like the US Long bond contract (US Treasuries between 15 and 25 years remaining maturity), various curve shape changes are also sources of additional CTD switch risks. Linear models like the one used here can be extended to higher numbers of risk factors. In principle, the number of required factors is equal to the number of deliverable bonds but these factors are highly correlated. Sampling a high-dimensional space of correlated random variables in turn raises questions of computational efficiency and stability. A natural compromise is to use dimension reduction techniques such as PCA to achieve a good mix of accuracy and stability.

FIGURE 28.18 Difference in contract fair value between a model that assumes repo rates to move in parallel with bond yields and one that assumes constant repo rates. For higher rates, the model with parallel rate shifts would give a higher contract value than one assuming constant repo rates.

<!-- image -->

Another important shortfall of this type of model is that it ignores the correlation between repo rates and bond yields. For short-term (e.g. 2 year) bond futures contracts in particular, central bank actions will affect both the current level of bond yields and the repo rates until delivery. Higher bond yields mean lower spot, and therefore lower forward, prices, but higher repo rates will mean higher forward prices relative to spot prices. The interplay between these two factors needs to be analysed. The simplest approach is to assume the 2 extreme cases of either repo rates move in parallel with bond yields or constant repo rates (as was assumed so far). Reality would then be between these 2 cases. Figure 28.18 shows the impact these approaches have on fair value estimates of the standard basket Table 28.1.

## 28.5 DELIVERY WINDOWS

So far the delivery process has been discussed in the context of a known delivery date. For the Eurex and Japanese futures contracts, that day is the 10th of the delivery month, or the next good business day if the 10th is not a business day. The US and UK bond futures contracts allow for delivery on any good business day during the delivery month. The choice of delivery day, as with the bond to be delivered, is with the short, and the exchange will automatically assign a randomly selected long to take delivery for each contract that is notified for delivery.

This additional option of delivery timing complicates the valuation of the contract. Given that the bond future has a given price at any point in time but bonds tend to have positive carry in a positively sloped yield curve, the short has a natural interest to delivery as late as possible in the delivery window so as to earn that carry before letting go of the bond at the futures-implied price. In practice that means that deliveries tend to be concentrated late in the delivery window. However, 2 effects can change this simple analysis. The first is the quality option which, like any option, decays in value as time passes. Because the short in the future is long the option, it may sometimes be advantageous to monetise the time value of the option through delivery rather than letting it decay. At the time of writing, the quality option is sufficiently worthless to make this consideration meaningless. A second complication is the repo market. The cash-and-carry arbitrage relies on repo funding which has fails risk. A repo counterparty may not return the CTD lent out for funding in time for delivery to the exchange. Arisk-reduction strategy is to give up 1 or 2 days of carry by delivering a little earlier.

In a downward-sloped (inverted) yield curve configuration, carry on the deliverable bonds can be negative. In this case, all 3 reasons above argue for early delivery.

## 28.6 INTERACTION BETWEEN FUTURES AND BONDS

Bond futures are the main avenue for price discovery in the European and Japanese bondmarketsandaregrowinginimportance in the US. Futures trading volumes exceed the trading volumes in the underlying cash markets by a large amount in the euro area and this poses the question of how reliably the cash-and carry arbitrage can tie futures prices to the underlying cash market.

Two possible decouplings are imaginable. The first is that the futures contract valuation decouples from the arbitrage-free forward price of the cheapest-to-deliver bond. Wherethefutureoutperforms the CTD, this could be an example of a squeeze, discussed in the next section, leading to a negative net basis. The second type of decoupling would be where the CTD decouples from the surrounding bond market. In this situation, the pricing implied by the cash-and-carry arbitrage stays intact but the specific situation of the CTD, combined with the non-fungibility of different bonds by the same issuer, leads to the CTD trading as a separate asset.

For hedging purposes, either type of decoupling is unwelcome because it removes the strong correlation between changes in the price of the futures contract and the bonds that are expected to trade in line with it. However, the first type is more concerning from a market functioning perspective because it implies that standard arbitrage relationships are breaking down. Extraordinary pricing of individual bonds, meanwhile, is not in itself too concerning.

So far, the first type of decoupling has been rare but the second is relatively common. In stressed market situations, it is quite common for investors to resort to the most liquid asset, namely the futures contract, to reduce risk. This means that the dislocation between CTD pricing and surrounding bonds can be a useful proxy for measuring market stress.

In Japan, a somewhat special situation is created by the coincidence of a high market weight of Japanese government debt in global government bond indices and the persistently low yields in the JGB market. Global bond fund managers are faced with the dilemma of having to maintain a high exposure to the Japanese market while seeing little expected return from these bonds. The standard investment strategy has therefore been to proxy JGB exposure through futures contracts and instead invest cash somewhereelse. This strategy means that buying JGB futures was not subject to relative value considerations and led to a structural expensiveness of the JGB future relative to surrounding cash bonds. Figure 28.19 shows the average spread of JGB to a Nelson-Siegel spline by maturity adjusted by the next futures delivery date. The 7-year point is the most expensive point on the curve in this metric.

FIGURE 28.19 Average spline spreads, including the 1 standard deviation bands of JGB by years to maturity after the next 10Y JGB delivery during the years 2009-2013, before the start of QQE. The JGB CTD is a 7-year bond and this maturity point tended to be the least attractive on the JGB curve from a carry-rolldown perspective. Daily data, price source JSDA.

<!-- image -->

The quantitative and qualitative easing programme of the Bank of Japan has disrupted this traditional pattern but it is still in evidence. Figure 28.20 shows the evolution

FIGURE 28.20 Average spline spread of the JGB contract CTD on the the JGB curve relative to the JGB 1 year shorter and longer on the same spline. Daily data, source: JSDA.

<!-- image -->

of the relative value of the JGB contract CTD versus surrounding bonds (bonds that are 1 year longer or shorter in maturity are chosen here to eliminate seasonality effects).

The opposite position in futures contracts relative to the long position of foreign investors is a structural short position of JGB dealers who hedge their long inventory. The structural richness of the contract results in subsidising the non-CTD bonds for domestic investors by improving the carry of these hedged inventory positions.

## 28.7 FUTURES SQUEEZES

A squeeze is a generic term for situations where the delivery of the futures contract is somehow affected by limited supply of the CTD. Different bonds are generally non-fungible and the delivery specifications and economics of bond futures contracts require that there is a sufficient amount of the right bonds available for the contract shorts to deliver through the exchange to the longs. Sometimes this sufficient supply is absent due to the actions of one or more market participants. More frequently, the mere prospect of insufficient supply affects trading in the contract and the underlying bonds ahead of the delivery period of the contract to such a degree that the actual delivery process becomes almost irrelevant. As will be explained below, the usual sign of an expected delivery problem is a negative CTD net basis.

The general principle of a futures squeeze predates the existence of bond futures and indeed the existence of futures exchanges. In [82], Mark Twain describes a short squeeze on railway shares so cursorily that he could evidently presume that his readers in 1889 would understand the strategy without much explanation. In a short squeeze, a trader will establish the right to receive particular securities in an amount that exceeds the total amount of such securities available in the market at that point. The traders who are under obligation to deliver the securities will be forced to either deliver alternative, more valuable, securities, or negotiate a settlement. In Mark Twain's fictional example, the delivery obligation was for newly issued shares and the obligation arose through a bilateral contract. In that case, a negotiated, if punitive, bilateral settlement was possible. In the case of bond futures, the delivery obligation arises through exchange rules and it is more likely that a different bond than the CTD gets delivered.

Futures squeezes are a prominent topic for discussion because the bond volume corresponding to the total open interest in most bond futures contracts usually exceeds the outstanding amount of the CTD by several factors and usually also exceeds the total outstanding amount of deliverable bonds. Because only a small portion of the open interest in a given contract is actually put through delivery, this volume mismatch is normally not a problem. However, it allows a trader to build up a large position with the intention to demand delivery without this showing up in open interest statistics in a meaningful way.

Somewhat more subtly, bond futures squeezes usually involve the repo market because the delivery window is fairly short. The deliverable bonds have to be delivered to the exchange to satisfy the delivery obligation and that means that the bonds do not have to be owned by the shorts, they just have to be in their possession; for instance, through repo borrowing. In order to restrict the ability of the shorts to borrow the bonds for delivery, it is therefore sufficient to buy up the supply in the repo market. This is usually cheaper and less risky than outright purchases of the CTD.

The following paragraphs provide a guide to analysing the economics of a squeeze situation. However, financial markets regulators have taken an increasingly dim view of such trades and it is unlikely that severe squeeze situations will occur in the future.

A trader could follow the example given by Mark Twain and buy futures contracts as well as the CTD so that delivery of that bond would be constrained. The trader would hedge this position by short-selling the next-to-CTD bond or the far contract. As shorts would find themselves unable to deliver the CTD, they would have to deliver the next-to-CTD at a much higher cost, allowing the trader to obtain this bond comparatively cheaply. Depending on which bond is CTD in the far contract, the trader could exit the position through delivering the bonds received in the near contract delivery into the short position of that far contract.

The market would reflect the likelihood of this scenario in a negative CTD net basis because the value of the futures contract increases with the probability of receiving a bond other than the CTD. In other words, while normally the CTD net basis would be non-negative and merely reflect the quality option, a potential squeeze implies that the cash and carry arbitrage for the CTD is no longer realistic.

The negative net basis of the CTD emerging in a squeeze situation translates into an implied repo rate (IRR) that is higher than the market term repo rate for this bond. Suchasituation can be interpreted as reflecting the repo market view of a squeeze rather than the futures delivery view, namely that the reverse leg of a specials repo transaction in the CTD is likely to fail. Borrowers of the CTD might be shorts in the contract who prefer to deliver the borrowed bonds to the exchange rather than returning it to the lender because the penalties of the exchange for non-delivery are higher than those in the repo market. If this risk is substantial, a bond trader looking to make delivery wouldnotfundtheCTDinthespecialsmarketbutwithatrustedcounterpartyinamore generic market (such as central bank refinancing operations) 15 or even in the unsecured market. In other words, squeeze risk does not only manifest itself in a negative net basis, but equivalently in an IRR that approaches central bank or unsecured funding rates. As long as there is an expectation that sufficient amounts of the CTD are available in the market, these rates provide caps on the IRR, and thereby floors on the net basis, of the CTD.

Animportant aspect of futures squeezes is that they are inherently unstable. A single entity will find it hard to muster the balance sheet necessary to control a meaningful amount of deliverable bonds. Even if that were possible, exchanges can impose position limits in the near contracts to lower the risk of excessive deliveries. While in theory multiple agents could conspire, through explicit collusion or by independently happening to execute the same strategy, to act collectively to engineer a squeeze, it would always be the first such agent who exits the strategy that realises the largest profit. This form of a free-rider problem reduces the likelihood of squeezes.

15 Eurex has recently established a segregated pooling basket for CTDs to enable users to employ this specific type of funding strategy.

## 28.8 CASH-SETTLED FUTURES

Contracts like the Australian government bond future are settled in cash using Equation (28.2). By definition, this means that the PVBP of the futures contract is equal to 1. As a result, the hedge ratio between future and deliverable baskets is not constant as shown in Figure 28.21. Other than that, the fair value estimate of a cash-settled future is exactly equivalent to the cash and carry arbitrage described in Section 28.3.3. The only difference is that every deliverable bond plays a role in the calculation of the contract fair value at all times whereas in a physically settled future the CTD is usually sufficient.

Given that price changes are the integral of PVBP over yield changes, it should be unsurprising that the price development of the future will not be reflective of the volume-weighted average price change in the deliverable basket. Figure 28.22 shows this effect.

Optically at least, cash-settled futures are not prohibitively inefficient. The divergence between the fair values of future and deliverable baskets is an example of convexity 16 . As mentioned in the introduction to this section, the choice between cash and physical settlement is essentially undecidable. Both delivery methods have substantial merits but are also problematic. The high switching cost between contract specifications is likely to remain an essential factor in keeping both models active in the market.

Acash-settled bond futures contract should require a convexity adjustment in line with that for money market futures Equation (13.17) to reflect the daily margining requirement. However, because the contracts have a short time to expiry, this convexity adjustment would be very small and is not applied in practice.

FIGURE 28.21 PVBP of a cash settled future with deliverable baskets as in Table 28.1 versus the volume-weighted PVBP of the basket itself.

<!-- image -->

16 This divergence is also an example of the broad use of the word 'convexity' in the fixed income context.

FIGURE 28.22 Fair value of a cash settled future with deliverable baskets as in Table 28.1 versus the volume-weighted price of the basket itself.

<!-- image -->

## 28.8.1 Exchange-for-physical transactions

An exchange-for-physical, or EFP, means in the commodity markets that two counterparties agree to exchange a given position in a futures contract for an equivalent size of the underlying, or a related, physical commodity. The exchange is then notified of this off-exchange transaction so that clearing of the residual futures contract positions can take place as usual.

In the Australian rates market, an EFP refers to an exchange of a position in an Australian government bond futures contract against entering an interest rate swap with an equal notional amount. As in a commodity EFP, the transaction takes place outside the futures exchange but is then given up to the exchange for clearing. Because the Australian bond future is a cash-settled contract trading on yield terms, it is fairly straightforward to value the transaction. In some ways, it can be compared to trading on a bond basis in a physically settled futures market, with a similarly low residual interest risk. The spread between the swap curve and the implied yield on the futures contracts is known as the EFP spread.

## 28.9 NEW BOND ISSUES

The analysis of bond futures, both physically and cash-settled, has to incorporate expectations of bonds that will be issued between the analysis date and the delivery date. Depending on the contract, two approaches can be differentiated. In either case, the new issues would be included in the projected deliverable basket.

In the more simple case, the newly issued bond is clear CTD. This could be due to its duration relative to the rest of the basket or due to other features. In this case, an analyst would take the market price of the future as given and infer a price for the new issue from the pricing of the future. This information might then inform an opinion about the new bond, such as that it is expensive or cheap.

In a more complex setting, the new bond is not obviously the CTD. An analyst would derive a price estimate for the new bond based on historical experience and then see what this projected pricing would mean for the deliverable basket. If the new bond happens to be CTD, the market may already be pricing the future as a proxy for the new bond, as in the case above, or be reflecting a compromise between different delivery scenarios.

In either case, expert judgement is important to establish the fair value of the futures contract.