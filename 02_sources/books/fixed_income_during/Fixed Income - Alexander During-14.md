---
title: "Fixed Income - Alexander During-14"
type: raw_source
source_pdf: "Fixed Income - Alexander During-14.pdf"
extractor: docling
---

## CHAPTER 13

## The Money Market

I nformally, the money market is defined as the market for funds with maturities of up to two years, and the associated derivatives.

The money market is the second largest capital market (the largest is the foreign exchange market). Money markets are extremely efficient and it takes only minutes to raise or place funds when standard documentation is in place.

## 13.1 MONEY MARKETINSTRUMENTS

Moneymarket instruments come in different shapes. Various instruments are issued by different entities and typically have different conventions. In the same market, almost identical paper may be traded in different ways depending on whether it is classified as CP or CD, so it is very important to make sure to understand what one is dealing with. Here are some examples for cash instruments traded in the money market:

Deposit Non-transferrable deposit with a given bank. Deposits may be callable or putable if this agreed in advance. Callable deposits carry slightly higher interest rates, for instance.

Loan The opposite of a deposit, i.e., cash obtained from a bank. Loans are usually not negotiated on a very short-term basis, but short term loans are used as part of a revolver facility or to bridge finance M&amp;A transactions, bond issues, etc.

Certificate of deposit (CD) Transferrable deposit, usually non-callable and non-putable. The idea of a CD is that the investor can realise cash ahead of the deposit maturity by selling the CD. The extra liqudity usually means that CD interest rates are slightly lower than those on equivalent deposits.

Treasury bill (T-bill) Short term paper issued by a government.

Commercial paper (CP) Short-term bonds issued by corporations and some governments. These instruments are very similar to CDs, but are quoted differently. Typically, a corporate has a programme to issue CP on a regular basis and the programmeis backed by a revolver loan (see below) in case the banks arranging the CP sales have temporary difficulties selling the paper. A variation of commercial paper (promissory notes) is known as tegata in the Japanese market.

Asset-backed commercial paper (ABCP) Short-term bonds issued by a special-purpose corporation that holds other assets which provide the cash to service the ABCP.

Banker's acceptance (BA) Effectively a trade receivable, a BA is a certificate from a bank that is backed by the right of a corporate to receive payment for goods sold. The corporate will present papers that evidence the right to receive payments (usually a contract and a bill of lading) to the bank and will receive the BA. The BA can then be sold by the corporate to receive cash immediately instead of when the goods are being paid for. The buyer of the BA faces the credit risk of the bank instead of the corporate or the buyer of the goods, as would be the case if CP was used instead.

Revolver loan, Standby facility Not a loan itself, but the commitment of a bank to make short-term funds available on demand as long as certain conditions are met. A borrower usually pays a commitment fee to the bank as long as the facility exists and the bank is required to set aside capital in case the facility is drawn.

The T-bill and CP markets are functionally fairly similar but some differences exist. Bills are usually sold in auctions like bonds while CP is issued on investor demand (reverse inquiry) at terms set by the issuer. While CP can be traded in the secondary market, the volume of secondary trading activity is substantially lower than for bills and price discovery in the CP market is much more difficult as a result. Issuers sometimes buy back their own CP to help investors liquidate such paper, but are usually under no obligation to do so. CP can also be issued in structured form, for instance with redemption amounts that vary in accordance with some index, or with option features. The two instruments have in common with other short-term instruments that they compete with bank deposits and CDs for short-term funds from a variety of investors such as money market funds, corporate treasuries and banks. As a result, they should be considered near money, and changes in the demand and supply of such paper can have impact on more visible interest rates such as interbank lending and FX swap rates.

## 13.2 DISCOUNTFACTORS

Monies paid in the future are usually less valuable than money paid in the present. There are a number of reasons for that; for instance:

- Inflation (money will buy less goods in the future than today)
- Credit risk (the risk that the person expected to pay the money in the future will not pay)
- Interest rate risk (the risk that if instead of lending money for a month today, one might be able to lend it at a better rate tomorrow)
- Liquidity preference (the fact that instead of lending money for a month today, one might decide tomorrow that one would rather buy a bicycle).

Mathematically, the time value of money is usually expressed through discount factors, written here as Df ( t ) . A discount factor can be thought of as the value of a payment of one currency unit at a given point in time t . For instance, if one is willing to pay 98 sen for the promise to receive 1 yen from the Japanese government in one year's time, one could write Df ( 1 ) = 0.98. The 98 sen are also called the present value of the payment of 1 yen. This is related to the idea of 'net present value' in corporate finance.

The discount factor will generally depend on who makes the promise to pay the money. For instance, one would expect a lower discount factor for a corporate's promise to pay than for a government's promise to pay. This is because, for a corporate, there is a smaller or greater chance of the corporate being unable to pay when the sum becomes due. The discount factor therefore reflects not only the time value of the payment itself, but also the probability of loss and the expected size of the loss.

In theory, discount factors are unique. What this means is that for any given time t , there is exactly one Df ( t ) for each issuer and instrument type. Suppose there were instead two different discount factors Df ′ ( t ) &gt; Df ′′ ( t ) . One could then sell, say, 100 ∗ Df ′ ( t ) yen worth of the instrument trading with discount factor Df ′ ( t ) , so one would have to pay 100 yen at time t in the future. If one at the same time buys 100 ∗ Df ′′ ( t ) yen (which is less than 100 ∗ Df ′ ( t ) ; see above) worth of the instrument trading with discount factor Df ′′ ( t ) , one will get exactly the 100 yen needed to make that payment. The difference 100 ∗ ( Df ′ ( t ) -Df ′′ ( t )) would be a riskless profit, which, in theory, does not exist. The market would sell so much of the instrument with the higher discount factor and buy so much of the instrument with the lower discount factor that the prices move to reflect the same discount factor.

In practice, different discount factors for comparable cash flows may exist. The first, trivial reason, is the explanation given above: Unless somebody actually does the buying or selling necessary to bring the discount factors in line, there is no reason why they should be. This means that opportunities to make riskless profits (arbitrage) can exist, albeit only for a short time. The time may even be so short as to be useless. The more complex reason is that it may be impossible to actually do the trade. In order to sell an instrument, one has to be able to borrow it from somebody and perhaps nobody is willing to lend it. Even if somebody were willing to lend it, perhaps the premium they are asking may be too expensive to make the trade worthwhile (discussed in Chapter 14 on repo trading). Even if the trade could technically be executed, the time t may be so long that there is little point in exploiting the difference Df ′ ( t ) -Df ′′ ( t ) if it is very small. In the case of cash flows related to bonds, it may be impossible to separate individual paymentsfromthesamebond,andtradethemagainstpaymentsfromcomparableother bonds by the same issuer. Therefore, especially in the money market, instruments can trade at prices that would suggest that discount factors are not unique.

Despite these shortcomings of discount factors, they are the core of fixed income analysis. Everything else, interest rates, option pricing, etc., is built on top of discount factors. Economically, this is rational. At the end of the day, what matters is cash in hand. How much cash in hand is worth compared to cash in the future is given by discount factors.

Discount factors are difficult to work with in daily practice, so the market generally quotes interest rates instead. It is impossible to talk about interest rates as such because the meaning of a given interest rate depends on the instrument and the market. Discount factors, on the other hand, do not have that problem. An essential task of fixed income analysis is therefore the correct translation between different expressions of discount factors.

## 13.3 DAYCOUNTCONVENTIONS

Whencalculating interest, one needs to take into account the number of days for which the money is lent. Interest is generally quoted on an annualised basis for easy comparison, but even though a rate is annualised, it is only valid for the stated period. For example, there is no contradiction between being quoted 2.1% for 6 months' money in annualised terms and 2.5% for 1 year of money.

In order to get from the annualised (quoted) interest to the actual interest for the period, the annualised interest rate is multiplied by the daycount fraction DCF . As the name suggests, the daycount fraction is a fraction, namely:

<!-- formula-not-decoded -->

Markets use different ways of counting days for both the numerator and denominator of this fraction. The daycount convention describes how this is done and a number of common daycount conventions are outlined below. Different conventions can be used for different instruments in the same market.

To understand some of the strange daycount conventions, one has to be aware that interest rates are older than pocket calculators and computers. In the 1970s, slide rules andlogarithm tables were state of the art calculation tools. Therefore, some conventions are driven more by the desire to simplify calculations than logic.

ISDA 30/360 Each month is assumed to have 30 days and each year has 360 days. If the start date falls on a 31st, it is corrected to fall on the 30th. If the end date falls on the 31st and the start date is on the 30th or 31st, the end date is corrected to fall on the 30th.

30E/360 Each month is assumed to have 30 days and each year has 360 days. Both start and end date are always corrected to fall on the 30th when they fall on the 31st. Note that the end date in ISDA 30/360 is only adjusted if the start date falls on a month end.

act/360 (actual/360) The days in the interest period are counted correctly and the result is divided by 360. This means that the amount of interest paid after one year is slightly larger than the one year interest rate (namely 365/360 or 366/360 of that amount).

act/365 Similar to act/360, but the number of days in the year is assumed to be 365. act/act Actual number of days in the accrual period divided by the actual number of days in the relevant year. A leap year is assumed when the 29th of February is part of the accrual period. This is the most natural way of calculating interest, but also the most complicated for anything but a computer.

Moneymarkets, including Japan's, usually use act/360 as the daycount convention. ThemainexceptionsaretheoldCommonwealthcountries(UK,SouthAfrica,Australia, etc.) where act/365 is used.

Looking a little ahead, bond markets generally use act/act or 30/360, whereas swap markets tend to use act/act, act/365 or 30/360.

## 13.4 MONEY MARKETINTERESTRATES

There are effectively two ways to quote the price of a money market instrument. The first, and most common, is to de-annualise the interest rate and work out the discounted value of the redemption cashflow. The other method is to treat the interest rate as a discount amount and de-annualise that. The standard method is the simple interest method:

<!-- formula-not-decoded -->

(Note that prices are always quoted in percent of the notional amount, hence the 100.) The interest rate earned on an asset that is trading at P and pays back 100 is:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Here, the interest rate for a given price is simply:

<!-- formula-not-decoded -->

As mentioned, the discount margin method is used only in a few markets. However, a very important one of these markets is the market for US Treasury bills. This is a good example of how conventions can be driven by convenience. Although the discount margin quotation is not very precise, it is very easy to do with a slide rule (especially because the US money market uses act/360 daycount). In fact, it is quite easy to build a slide rule that is marked to make this calculation very easy. The division operation in the simple interest method is quite tricky to do precisely, so tables or a calculator are necessary.

Instruments with a maturity beyond 1 year are special when the daycount convention uses actual days as the nominator and the instrument spans a leap year. The problem is that if the instrument effectively straddles 2 years and 1 of them is a leap year, it is unclear whether 'actual' in the nominator means 365 or 366 days. The solution is to make it mean both. Generally, the instrument is split into 2 parts, namely 1 part that is exactly 1 year long and ends at the final maturity of the instrument, and a second one that starts immediately and ends at the start of the 1 year instrument. Each of the two parts then uses the appropriate nominator, i.e., 365 or 366, depending

The discount margin method is:

on which of the 2 contains the 29th of February. This is a first example of the general convention to work backwards from the maturity of an instrument, rather than forwards from its inception. The rationale for this convention is that it improves fungibility between instruments originated on different days.

## 13.5 COMPOUNDING

So far, interest rates have been discussed in the context of single-period investments. In general, contracts can cover multiple periods and can require interest to be paid at the end of each of them. For instance, a credit card loan typically requires monthly interest payments. While the interest used to calculate the payment amounts are annualised rates, the monthly payment frequency affects the total cost of a loan. Assuming 30/360 daycount for simplicity, a loan of EUR 100 for 1 year at 6% would require repayment of EUR106attheendoftheyear.Ifinterest is charged monthly, it is no longer immediately clear what the total interest cost is. If the borrower pays the interest at the end of each month, the total interest payment is 12 times 0.5%, equal to the stated annual interest of 6%.

If the borrow instead does not pay the interest, it is added to the outstanding loan balance. After the first month, the loan balance would then be EUR 100.50 and so the 6% interest rate would be charged for the following month. The payment obligation at the second month would therefore be EUR 100.50 ∗ 1.005 = 101.0025. After the full year has elapsed, the loan balance would be 100 ∗ ( 1 ∗ 6 %∕ 12 ) 12 ≈ 106.17. This addition of interest payable to the outstanding loan balance, and the corresponding increase in the interest obligation, is known as compounding. Compounding can lead to surprisingly high interest charges. At 12% annual interest, monthly compounding generates a total compound interest of 12.68 % . In retail lending, many countries therefore require the disclosure of the total interest cost chargeable over 1 year, including the effects of compounding and applicable fees. Such interest rates have names like annual effective rate (A. E. R.). Absent fees and as long as non-business days and daycount conventions do not affect the calculation, the annual effective rate r eff for an annualised rate r is given as:

<!-- formula-not-decoded -->

Interbank lending takes place predominantly on an overnight basis. This makes it useful to consider the limit n →∞ which is known as continuous compounding. Using the well-known limit relationship:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

one finds:

In actual interbank lending, compounding of overnight interest is made more complex by the fact that interest cannot be paid on non-business days. Compounding therefore has no effect on weekends. For a two-week horizon with no holidays, for instance, the total interest using actual/360 is not given by:

<!-- formula-not-decoded -->

but by the (for positive rates r somewhat smaller):

<!-- formula-not-decoded -->

because the two weekends spanned by the lending period simply require 3 days of linear accrual without compounding.

## 13.6 LIBOR, EURIBOR, AND FRIENDS

Because trading in money markets is done between institutions and not on an exchange, the market is not very transparent. To provide reference rates for the market as a whole, the British Bankers' Association (BBA) introduced the concept of LIBOR (London InterbankOffered Rate). To find LIBOR, the BBA asked panels of banks to submit the interest rate at which they expect a highly rated bank to be able to borrow unsecured to other high-quality banks at 10am on each London business day over certain horizons. From the quotes obtained, the highest and lowest were thrown out and the average of the remaining quotes (a so-called trimmed mean) was published as LIBOR. There are different LIBOR rates for different time horizons (1M, 3M, etc), and for different currencies (USDLIBOR,GBPLIBOR,etc.).LIBORissuchausefulideathatsimilar fixings are now done in many places and the term Libor is used to summarise these rates. One would for instance talk about a Libor account in Czech krona even though there is no actual fixing in London. The rates produced in other centres are named very similarly. There are CIBOR (Copenhagen, DKK), TIBOR 1 (Tokyo, JPY), STIBOR (Stockholm, SEK), KLIBOR (Kuala Lumpur, MYR), PRIBOR (Prague, CZK), and so on. Note that both JPY LIBOR and TIBOR exist, but because the panel banks are different, they do not represent the same credit risk.

The bid side of LIBOR is called LIBID, but this rate is rarely used. Typically, LIBID is assumed to be 12.5 bp below LIBOR (1/8th of one percent).

With the introduction of the Euro, the European Bankers' Federation introduced a fixing called Euribor that is very similar to EUR LIBOR, but has a much larger bank panel. For a few months in 1999, there was competition between the two fixings, but by now Euribor has completely superseded EUR LIBOR as the market benchmark.

1 There are two separate TIBOR fixings, one for the on-shore and one for the off-shore yen market.

The LIBOR concept has been extremely successful and many interest rate derivatives, like money market futures and swaps, are linked to this type of benchmark which is generically known as an Ibor. Many loans and FRN coupons are set with a link to Libor or a related rate. The essential weakness of the concept is that traders are invited to provide opinions, rather than actual traded rates. Indeed, unsecured term lending is now comparatively rare; many interbank lending transactions are now overnight and secured. Hence, the quotes submitted to the Libor fixings tend to be simply spread off overnight swaps which are discussed below.

The standard Libor derivative is a forward-rate agreement (FRA). A FRA is a bilateral contract where one party makes a fixed payment while the other one pays a variable amount linked to a Libor fixing at the expiry of the contract. In line with other derivatives, only the net amount is actually paid. The fixed payment is expressed as an interest rate r FRA . With a notional N and a fixing rate r fix , the difference d in interest payable at the end of an accrual period of t days between the fixed and floating rate is:

<!-- formula-not-decoded -->

whereforsomecurrencies, like Sterling, 365 would be used in the denominator. Because the market rate is known at the beginning of the accrual period, the FRA is closed out at that point, and the interest difference d is discounted to the start of the period with a payment that is:

<!-- formula-not-decoded -->

The party making the fixed payment is known as the buyer while the other side is the seller, which reflects the money and swap market convention to assume that the buyer takes cash and agrees to pay a certain amount of interest. Higher interest rates r fix therefore are beneficial to the buyer of the FRA, although this would be offset by interest payable on an actual borrowing transaction that the FRA is used to hedge. Money market futures contracts (discussed below) follow the bond market convention where the buyer is a lender, and hence has the opposite exposure.

A FRA is usually labelled by its start and end date. A 6M9M FRA would be a FRA on a deposit covering a period starting in 6 months and ending in 9 months, i.e., a 3 month deposit.

In the course of the financial crisis, it was discovered that some traders colluded with others, in some cases across multiple firms, to manipulate various Libor fixings on certain days 2 . Generally, these manipulations appear to have been undertaken to achieve favourable outcomes on derivatives fixings and there appears to have been no bias to manipulate these rates consistently upwards or consistently downwards. This may explain why money market futures and swap volumes failed to decline substantially as the manipulation was discovered. Most users appear to have taken the extent of manipulation as less significant than the benfits of the benchmarks. That being said, willfully misleading markets on prevailing conditions is morally and legally wrong. Regulators, as a result, have worked globally to reduce the use of Libors for financial products and at the time of writing, various reform processes are underway to replace these benchmark. This process is discussed in a later section.

2 A single trader is perceived as less able to shift the Libor fixing because extreme submissions will be eliminated in the trimmed mean calculation. That being said, the trimmed mean can still move upwards when an extremely high rate is submitted because another submission that would otherwise have been discarded will be included in the mean calculation instead. The reverse is true for a very low submission.

Before moving to this topic, it should be borne in mind that one can change the benchmark fixing process but the incentives of manipulating the reference rate for cash-settled derivatives are likely to remain. If a trader who pushes up a reference rate would have to carry an overpriced amount of cash for a longer period, the associated cost and balance sheet commitment would be a strong, and perhaps sufficient disincentive 3 . As money market derivatives will for practical reasons remain cash-settled, vigilance on bechmark setting will remain required.

## 13.7 OVERNIGHTBENCHMARKS

Given the shift of interbank cash trading to overnight markets, several secured and unsecured overnight rate benchmarks have sprung up. The euro area has always had the Eonia (Euro Overnight Index Average) and before that the Japanese market focused on the mutan (literally 'unsecured') overnight rate. More recently, rates like Sonia (Sterling Overnight Index Average), Tonar (Tokyo Overnight Average Rate) and so on have been developed. In the case of Japan, Tonar replaced the mutan rate in December 2016 as overnight benchmark [8]. The main innovation in the US market has been the introduction of SOFR (Secured Overnight Funding Rate) which is based on a broader range of transactions than the traditional Effective Fed Funds 4 rate. The euro area switched to a similarly broader benchmark with the introduction of €STR. Futures markets exist for some of these benchmark rates.

Onereason why at the current juncture there is a need for interest rate benchmarks that look beyond the interbank market is that current monetary policy configurations work with an excess liquidity in the banking system. This excess liquidity reduces the need for banks to trade funds between themselves and therefore the volume of interbank transactions. The wider benchmarks extend to transactions where at least one participant is not a bank.

Thebridgebetweenovernightratesandtermratesistheovernightindexswap(OIS) swap market, particular the short end of this market. There is active quasi-arbitrage trading between 3M term rates and 3M OIS swaps, for instance. Such a swap is an exchange between a fixed payment (corresponding to the term rate) and a floating payment corresponding to the compound interest on an overnight deposit carrying the benchmark rate:

3 Cf. the introduction to Chapter 28 on page 301.

4 Note the word 'effective'. This rate is the volume-weighted average rate at which federal funds actually trade and are reported. The policy rate of the Federal Reserve is known as the Federal Funds rate. It is the task of the Open Markets desk at the Fed New York to make the Effective Funds Rate trade within the band prescribed for the Federal Funds rate by the Fed's Open Market Committee.

<!-- image -->

Forward-starting OIS are the natural equivalent of FRAs. At the same time, many large-scale issuers of floating-rate notes are switching to overnight rate benchmarks, and there is an active market in long-term swaps against these very short rates. To some extent, this could obliviate the need for term benchmarks, at least between financial firms. As will be discussed next, however, the same may not be true for non-financial users of short-rate benchmarks.

## 13.8 BENCHMARK REFORM

Thediscovery of Libor manipulation, combined with the realisation that there are fewer transactions between financial firms in the unsecured term market, have spurred market regulators into action to encourage the creation of benchmarks that are both more robust against fraud, and more representative of actual transactions. Both these desiderata work in the same direction because a benchmark representing a larger volume of actual trading is presumably harder to manipulate. The initial step taken has been a tightening of supervision for benchmark providers in order to make the benchmark production process more robust. Submitters of benchmark quotes have also made subject to more stringent penalties for wrong-doing 5 . In the longer run, more sustainable solutions need to be found.

Broadly speaking, there are two directions this effort is taking. One is to base term benchmarks to a larger extent on actual trades and less on trader assessments. This is known as the 'hybrid methodology'. The second is to fundamentally shift benchmarks towards overnight trading activity where there is the most volume.

For financial firms and very large corporates, overnight rates are a natural interest rate reference because their treasury operations operate on a high frequency. For private households and smaller firms, there is a need for intermediate rate references that are linked to terms of a week to a few months. As an example, a mortgage borrower with a floating-rate mortgage (common in the UK, Italy and Spain) needs certainty about the interest due some time before the payment date. With a Libor link, this amount is

5 Given that providing quotes to a benchmark fixing is mostly a badge of pride (because only the most active firms in a market are asked to contribute) which has actual costs associated with it, some financial firms reacted to this extra risk by stopping to submit quotes.

knownatthestart of the interest period. When benchmark rates shift to overnight rates, then there needs to be a replacement for the term rates provided by the Libors.

Oneobvious solution would be to use OIS swap fixing but one might argue that this wouldhandthesetting of term rates to money market derivatives traders. An alternative is to use lagged compounded overnight rates. In this approach, the floating rate interest payable is determined by observing the compounded overnight interest rate over a period p but lagged by a period l .

<!-- image -->

For l = 2 (where 2 stands for the T + 2 money market settlement convention), the interest payment corresponds to the OIS swap rate and hence the professional money market. As discussed on page 172, the European FRN market is using l = 5. In the case where l is equal to the coupon period, the payment at the end of an accrual period of length l wouldbeknownatitsbeginning(asis the case for standard Libor contracts) and if also p = l , it would be based on observing the overnight rates over an equal period in the past. One could therefore construct floating rate contracts where, for example, the interest payable on a quarterly leg is determined by the compounded interest on the overnight benchmark during the preceding quarter.

While this approach may sound reasonable, it is a misinterpretation of the observation period p . If l does not match the money market settlement convention, then the interest rate on the term it applies to is not directly linked to overnight market rates over that period, independent of the value of p . More importanly, the length of p does not induce a term risk premium because the averaging is always one of overnight rates which have no term premium. Averaging over more or less periods does not change that. There is therefore no conceptual link between the length of the averaging period p andthe term for the term rate one wishes to link to it. Market participants using a lagged averaged overnight rate to set term rates will then probably apply an explicit mark-up that depends on the term (note that there will be in any case a quoted margin on any lending contract).

For a central bank, contracts with lagged rates have the marginal drawback that changes in the policy rate will affect borrowing costs under such contracts only with a delay of around p ∕ 2 + l . That would be longer than under the current term rate environment where new resets immediately reflect the new policy rate. This may not be a technical problem because economic actors are forward-looking and will factor future borrowing expenses into investment decisions.

## 13.9 MONEY MARKETFUTURES AND FUTURES TRADING

## 13.9.1 Money market futures

Moves in short-term interest rates can be hedged using exchange traded contracts. Depending on the underlying currency, these contracts are known as Euroyen, Eurodollar, Short sterling, or Euribor contracts 6 . The contracts are generally linked to the equivalent of 3 months Libor for the respective currency (Euribor in the case of euros) and the main contract expiries fall on the third Wednesday of every third month in the year (the so-called IMM days). On this day, the final price of the future is determined by the exchange as:

<!-- formula-not-decoded -->

Futures contracts can only move in discrete steps specified by the exchange, for instance 0.005 (equal to 0.5 bp) in the case of a Euribor contract. This minimum price move is called a tick. The notional amount of a money market future tends to be USD 1 million or the closest local equivalent (EUR 1 mio for euro-linked contracts and so on). The cash value of a one-tick move on a 3M contract is then about one quarter of half a basis point on one million, which amounts to 12.5 dollars or the local equivalent. Note that Equation (13.13) provides a rates exposure that is opposite in sign to Equation (13.12) so that the buyer of a FRA has a position matching that of a seller of a future , and vice versa.

## 13.9.2 Identification of futures contracts

Individual futures contracts are identified by a combination of the underlying and the delivery date. While delivery date identifiers follow a common convention, the identification by underlying can sometimes differ for the same contract across data providers. For instance, the Eurex 10Y Bund contract is known as FGBL 7 on Eurex and Reuters (now Refinitiv) is using the same designation. The data provider Bloomberg instead uses the code RX for the same contract 8 . Money market contracts also follow this pattern on Bloomberg, with Euribor contracts ER, eurodollars ED, and short sterling L\_ (note the space, also present in the Gilt contract G\_).

The delivery date is specified by a single code letter for the month and a one- or two-digit year. The month code letters, given in the table below, are unfortunately somewhat cryptic 9 .

The contracts expiring in the next year are also known as white, the next years as red, green and blue 10 , followed by gold, purple, orange, pink, silver and copper, although most traders would struggle to name the contracts past gold. In 2020, the March 2021 expiry would be called 'white March' (or simply 'March'), the March 2022 expiry 'red March' and so on.

6 The reason for the use of the word 'euro' in some of these contracts is explained in Section 16.4.

7 Future German Government Bond Long, which is in line with the 2Y Schatz contract FGBS and

the 5Y Bobl FGBM.

8 The Eurex Schatz is DU and the Bobl OE on Bloomberg.

9 One way to remember them is to write down the alphabet starting with F and striking out all those letters that appear in the word WORSTIPLY. Why this should be the case is not immediately obvious.

10 Auseful mnemonic is that a standard RGB colour monitor makes up white light from red, green and blue colours.

TABLE13.1 Standard future expiry month codes.

| January   | F   | February   | G   | March     | H   |
|-----------|-----|------------|-----|-----------|-----|
| April     | J   | May        | K   | June      | M   |
| July      | N   | August     | Q   | September | U   |
| October   | V   | November   | X   | December  | Z   |

Colour codes are not used for bond contracts because bond futures contracts generally expire within 1 year. Instead, one uses the designations front and back for the next and the following expiry.

Bond futures contracts generally expire in March, June, September and December and so it is sufficient to remember the codes H, M, U and Z, marked in bold in the table. A Eurex Bund future for delivery in June 2019 would therefore be identified as FGBMM9onReuters and RXM9 on Bloomberg. These designations are called specifics because they identify one individual contract. The downside of working with specifics for analysis purposes is that they exist only for a relatively short time interval, which is usually 9 months for bond contracts, and that they roll down the curve (shorten in remaining maturity) for money market contracts.

In addition to the specifics, therefore, data providers construct data series that span longer periods. The simplest form are serials where active contracts are simply numbered according to their expiry date. The contract expiring soonest is the first, the next the second contract, and so on. Data providers would therefore offer a FGBM1, FGBM2, etc. series 11 . At any given point in time, each serial contract refers to one specific contract but that association changes at each expiry. For instance, in February 2019, the second Bund contract FGBM2 would be the June 2019 delivery FGBMM9 but from the March delivery onwards, the same FGBM2 would refer to FGBMU9. In this sense, the expressions 'front contract' and 'back contract' are serials.

A more subjective series construction is by activity where providers such as Bloomberg designate a 'most active' specific for each underlying. Such series end in A for the most active and B for the next most active. Traders therefore routinely refer to RXA in chats when they do not simply talk about 'the Bund'. The complication of these actives series is that it is not always obvious when the designation changes. Most of the time the first serial contract will also be the most active, but as explained later, trading activity switches from the front to the back contract some time before delivery.

Fromthe traded prices of money market market futures, it is possible to build interest rate curves out to the maturity underlying the Libor rate that is linked to the furthest traded money market contract. In Yen and euros, this is roughly 1-2.5 years, and up to 10 years in the US. To look ahead a little, this is done by solving Equation (15.4) for the term rate rather than the forward rate.

11 On Bloomberg accordingly these would be RX1, RX2, etc.

## 13.9.3 Futures trading basics

Money market futures are only one example of exchange traded futures. The daily closing price of a contract on an exchange depends on the exchange trading in the contract. For instance, it might be the last traded price or some average of the prices seen over the last few minutes of trading. Given the margining mechanism, this price has limited relevance as it may be corrected on the next trading day. On the last trading day of a futures contract, however, the final price (also called the exchange-determined settlement price EDSP) is given by the Libor fixing, as explained above. This ties the trading of the contract to the underlying money market rate. After the fixing, the exchange will calculate a final margin payment and returns the sum of the last day's variation margin and the initial margin to the investors. Contracts where a fixing determines the final settlement price and closing out is done through the normal daily margin mechanism are called cash-settled contracts as opposed to physically settled contracts, such as most bond futures contracts.

## 13.9.4 Convexity adjustment

The price calculation of a money market futures contract Equation (13.13) implies:

<!-- formula-not-decoded -->

This is different from a simple money market deposit. By Equation (13.2) the price of the deposit is given by:

<!-- formula-not-decoded -->

so the second derivative is:

<!-- formula-not-decoded -->

The second derivative of price with respect to interest rate is the convexity of a fixed income instrument. In the derivatives world, the same quantity is called gamma.

Here, the convexity of a deposit is always positive while that of a money market contract would appear to be strictly zero. In practice, the requirement to post variation margin against a futures position means that money market futures do in fact have convexity. A trader holding a long position in the future will have to post additional margin when rates rise because the mark-to-market value of the future declines. If the trader has to fund this margin, it will be at the new, higher, rate. If yields then decline again, the trader will receive variation margin from the clearing house but can only invest this cash at the new, lower, rate. Volatility in rates therefore leads to the trader borrowing at higher rates and investing at lower ones.

Theresult of this dynamic is that futures-implied rates are not unbiased estimates of future short-term rates. Instead, a trader would only buy a futures contract if the implied rate were higher than his or her expectations of future market rates, and the difference between the futures implied rate and the actual expectation is the compensation for the cost introduced by the marging requirement. This rate difference is known as the convexity adjustment and given by:

<!-- formula-not-decoded -->

where /u1D70E is the interest rate volatility (usually proxied by the implied volatility of options on the contract itself) and t the time to expiry of the contract. Notably, the convexity adjustment increases quadratically with time to expiry and volatility. This makes the adjustment more relevant for long-dated contracts, and more volatile short-rate markets. For the euro and yen strips, convexity adjustment play a small role because the contracts do not extend far enough into the future.

In days gone by, the convexity adjustment of a money market future was the difference between the implied rate on a futures contract and the equivalent forward-rate agreement (FRA). This was because futures contracts had margining while FRAs did not. In today's world of central or bilateral clearing, FRAs also require margining. The convexity adjustment is therefore still relevant for the building of discount curves but FRAshavebecomemorecomplextovalueduetoxVAadjustments(discussedinSection 12.3 on page 108).