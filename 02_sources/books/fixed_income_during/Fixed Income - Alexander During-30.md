---
title: "Fixed Income - Alexander During-30"
type: raw_source
source_pdf: "Fixed Income - Alexander During-30.pdf"
extractor: docling
---

## 29.1 INTRODUCTION

Swaps have already been mentioned briefly in the context of overnight index rates. Generally, a swap is a transaction where two parties bilaterally agree to exchange (swap) cash flows in the future.

Essentially there are only two rules governing the swaps market:

First, if it moves it can be swapped;

Second, cash payments in the same location, currency and on the same day are netted.

The first rule means that there are swaps not only on fixed income benchmarks but also on oil prices, the number of sunny days, the degrees and number of days that temperatures fall below a certain level in a given area (so-called heating degree swaps), etc. A corollary to this rule is that things that do not move do not get swapped. The second rule is essentially a risk management measure.

The first ever interest rate swap was conducted in 1981 between IBM (then a triple-A rated bond issuer) and the World Bank (properly named the International Bank for Reconstruction and Development, IBRD) and the transaction was arranged by Salomon Brothers. At the time, IBM wished to raise dollars but found little demand in the USD market for new IBM bonds. At the same time, the World Bank wanted to raise Swiss francs but lenders in this currency already held a lot of World Bank debt. Therefore, IBM issued a Swiss franc bond and the World Bank a USD bond. IBM and the World Bank then agreed to swap the cashflows from these two bond transactions, so IBM ended up borrowing in USD and the World Bank effectively borrowed Swiss francs.

The structure of this first swap would today be considered unusual because it amounts to a cross-currency fixed-versus-fixed swap. However, that swap illustrates the immense transformation swaps have introduced in the fixed income world. Before swaps, a foreign buyer of a 10Y dollar-denominated corporate bond issued by corporation X was assuming the following risks:

- 10Y interest rate risk
- Dollar currency risk
- Default risk of X

## CHAPTER 29

## Swaps

Swaps, in conjunction with special purpose vehicles (SPVs), changed this picture completely. A buyer could transform the USD bond into a CHF bond (which is basically what happened in the first swap), hedge out the default risk (with a credit default swap), remove the 10Y interest rate risk (with an asset swap), etc. For that matter, the investor could turn the economic risk characteristics of the USD bond investment into that of holding a Peruvian equity portfolio (with a total return swap), or running the local brewery (with a cooling degree day swap). Swaps allow the extraction, and transformation, of selected risks in a given asset. As such, trading swaps can be seen as ways to trade pure risk whereas trading of actual assets commingles the trading of risk with the trading of investments.

In essence, swaps release some of the frictional losses embedded in preferred habitats (cf. Section 20.4). The existence of preferred habitats implies that investors buy assets with sub-optimal risk-return characteristics because those assets have certain features that outweigh their risk-adjusted returns. With a swap, an investor can modify the risk of a given asset to suit her or his preferred habitat. As such, swaps can add value to the total economy via more optimal capital allocation, even though each swap is a zero-sum game between two counterparties.

Swaps used to be pure bilateral instruments but have changed in nature over time. Standard swaps between banks were among the first instruments, after futures and FX transactions, to be centrally cleared. This turned out to be helpful in the financial crisis, and central clearing is now mandatory for standard swaps in most jurisdictions. In addition, swap-like futures contracts, which have been around since the 1990s, have seen a somewhat larger take-up in recent years.

The volume of swaps transactions is huge and far exceeds trading in bonds. The Bank for International Settlements estimates that around USD 341 trillion notional of interest rate swaps were outstanding in H2 2019. This accounts for almost a third of the total OTC derivatives of USD 558 trillion at the same point in time. Note that, at the sametime, the total size of the global debt market was only around USD 120 trillion, also according to the BIS. However, the market value of these swaps was only 7.5tr. Although still a large number, it implies that the average market value of an interest rate swap is only about 2.2% of its nominal amount. As will be discussed further below, there are strong incentives to keep the market value of a swap low, and there are ways to achieve that. Because most investors have portfolios of partially offsetting swaps, neither total gross value, nor market value are necessarily reliable indicators of the size of the swap market.

Trading in the swaps market is usually done using standard documentation based on the ISDA Master Agreement drawn up by the International Securities Dealers Association and normally two counterparties wishing to trade swaps just sign an ISDA Master (perhaps adjusting minor details to suit their particular situation) and then trade swaps using a simple short-form confirmation each time a new swap contract is concluded. In bilateral contracts, parties usually agree on a standard Credit Support Annex (CSA) to the ISDA Master that requires the swap to be marked to market every trading day. Depending on the outcome of the mark-to-market, the party which faces a loss in the transaction has to deposit collateral (cash, bonds, or cash or bonds, depending on the CSA) with the counterparty to protect the counterparty from default risk. The use of CSAs has largely been superseded by central clearing but some exceptions remain. Some market participants, particularly pension funds, tend to have assets but not cash on hand to make daily margin payments in cash. They therefore tend to prefer trading with bond CSAs. Some sovereign treasuries, meanwhile, find it difficult to post collateral under CSAs and therefore use one-sided CSAs where they receive collateral when their swaps are in the money, but do not post collateral when they are not 1 . In recent years, however, even sovereigns have moved towards central clearing to reduce the xVA costs associated with other clearing arrangements (cf. Section 12.3 on page 108).

What sets swaps apart from securities is that they can be, and frequently are, tailored to the specific needs of particular users. For instance, swaps can use a multitude of calendars for the observation of the reference indices on a floating side, the payment of any cash due, possible termination dates, and so on. In a trade between counterparties in London and Athens, for example, it may be useful to use the combined holiday calendars of both locations because many public holidays in one location are not holidays in the other 2 .

## 29.2 PLAIN VANILLA SWAPS

Plain vanilla swaps are the essential building block of the fixed income swaps market. These swaps have the two counterparties exchange a fixed versus a floating rate payment. The fixed side generally matches the daycount convention and payment frequency of the local sovereign bond market (actual/actual in most cases, and semi-annual in the US, the UK, and Japan, annual in the euro area). The floating side is traditionally given by quarterly or semi-annual payments equal to the local Libor, quoted in the appropriate money market convention (actual/360 or actual/365). This makesplain vanilla swaps hybrids between the bond and money markets. Both sides are expressed in percentages of a fixed amount which is the nominal amount of the swap.

Swaps have a tenor (the time between settlement date and maturity) and can be forward starting. A forward swap is usually written in the form 5Yx10Y which would be a swap starting in 5 years' time and then running for 10 years 3 . This notation is subtly different from that for FRAs, where there is no 'x' and the second period is not the tenor but the maturity.

The market is most liquid in par swaps, which is a swap that at inception has zero fair value (before xVA adjustments). Par swap rates are the natural ingredient for bootstrapping a discount factor term structure of swap rates (cf. Section 19.3.1).

On balance, convention comes down on the money market side because the fixed side of the swap is treated as the borrowing side. Swap rates are quoted in terms of the fixed rate given while the floating side is simply the Libor rate. A swap trader saying 'mine' on a swap agrees to pay the fixed side, whereas a bond trader saying 'mine' will receive the fixed coupon on the bond that was quoted. The swap convention stems from the money market convention of taking the money ('mine') in exchange for paying the quoted interest rate on it.

1 Because swap dealers still have to manage the risk associated with sovereign counterparties that have net obligations under swaps, they tend to buy protection in the form of sovereign CDSs. This is an important reason for sovereign CDSs to exist.

2 In this specific example, even Easter falls on different days.

3 For a swap like this in EUR, the first fixed cash flow would occur after 6 years, and the last after 15. In USD, GBP or JPY, the first fixed cash flow would be after 5 years and 6 months.

FIGURE 29.1 Cash flows in a 4Y plain vanilla swap in euros (annual fixed against semi-annual floating) for a notional of 100. The dotted lines refer to the exchanges of nominal which are netted out. Fixed payments are also netted against the floating payments occurring on the same day.

<!-- image -->

There are manifold reasons to use interest rate swaps. For instance, corporate earnings tend to be closely correlated with the economic cycle, which in turn is closely correlated with short-term interest rates. Corporates therefore are natural borrowers in the floating rate market. At the same time, most investors tend to favour fixedrate bonds. By using an interest rate swap, a corporate is able to issue such fixed rate bonds but in reality maintain a floating rate exposure. Banks, meanwhile, are natural receivers of floating rate coupons to defease floating rate liabilities (cf. Chapter 17). Where banks buy fixed-coupon assets, they therefore tend to swap them down to floating rate. Some sovereigns use swaps to hedge long-dated issuance down to their preferred issuance duration. Overall, the natural fixed rate payer and receiver sides of the market are roughly distributed as shown in Table 29.1.

Thereis a persistent myth that the term structure of swap rates is linked to the senior unsecured funding costs of prime banks. The source of this belief is that the floating side is the short-term funding cost of prime banks, and the present value of the fixed side payments should equal the expected value of the floating side payments to make the swap fair. A simple examination of the interest rates on newly issued senior unsecured bank bonds shows that they are usually higher than the swap rate of the same maturity. Aside from the term premium in interest rates (cf. Section 20.3), an important source of this difference is survivorship bias in the swap rate. The yield to maturity of a bond reflects that buyer of a bond is in principle exposed to the borrower until the bond matures. The receiver of a swap, however, pays a Libor fixing that at the time reflects the funding costs of prime banks at that time . If any one bank should decline in creditworthiness, it will be removed from the Libor panel, but its bonds remain outstanding.

TABLE29.1 Natural positions in the plain vanilla swap market for different investor types.

| Sector       | Payer                           | Receiver                                          |
|--------------|---------------------------------|---------------------------------------------------|
| Intermediate | Banks Sovereigns Banks          | Corporates Banks Pension Life insurers Sovereigns |
| Long end     | Asset swappers Mortgage lenders | funds                                             |

A specific form of a plain vanilla swap are IMM-dated swaps which are forwardstarting swaps with a start date that equals the next IMM date (cf. Section 13.9.1). Using IMMswaps is in the first instance a way of ex-ante trade compression because there are only 4 possible start dates per year. In addition, the floating leg of an IMM swap is fixed on a money market futures expiry date so that the fixing is easier to hedge.

## 29.3 TRADE COMPRESSION AND RE-COUPONING

Swaps can be closed out by mutual agreement, usually against a final payment to settle the remaining valuation. In case of bilateral swaps, it is also possible to use a technique called novation where 3 counterparties agree that 1 counterparty steps into an existing contract, replacing 1 other. The default mode of removing the economic risk of a swap, however, is to enter a new, offsetting swap. The reason for this development is that the new swap can be executed with any counterparty and the rate on the offsetting swap may therefore be more competitive than the close-out rate offered by the original counterparty.

As a result of this practice, swap users tend to end up with large portfolios of partially offsetting swaps. In the first instance, this inflates the total gross volume of swaps outstanding. This practice also creates unnecessary settlement risk because the cashflows on these swaps do not fully align 4 . Regulators now require in some jurisdictions that counterparties analyse the swaps they have and attempt to reduce them. For instance, if bank A pays in a 10Y and 8Y6M swap to bank B, and receives in a 9Y3M swap from the same bank, then it may be possible to collapse the economic exposure into 1 or 2 swaps, for instance by eliminating the 9Y3M swap. This process is known as trade compression. Commercial providers, such as the CME-owned TriOptima, offer the service to compress trades across multiple counterparties. As a result of better trade compression, the global total gross volume of swaps may be declining as the impact of compression outweighs the flow of new trades. Note that compression is difficult for asset swaps because these are specific to securities, and compression may have consequences for users who apply hedge accounting.

In addition to trade compression, swap users can reduce the amount of margin tied up in a transaction by restructuring it. When an existing transaction has moved away from fair value, one of the counterparties has to post margin to the other. This margin, and the fair value of the swap, consume balance sheet of both counterparties.

4 As mentioned above, this is one reason to use IMM swaps.

The two counterparties may therefore agree to terminate the existing non-par swap and immediately conclude a new swap with the same cashflow dates but a new, par, coupon. This is known as re-couponing. Because swaps can be re-couponed at any time, the total net value of swaps in existence is a relatively meaningless number because swaps with a non-zero net value are those that have not been, and perhaps cannot be, re-couponed. Reasons not to re-coupon can include taxes (margin crystallises as profit and loss on such a transaction), and non-standard clearing arrangements.

Because a re-couponing is technically a combination of 2 transactions (1 swap exactly offsetting the existing non-par swap, and a second replacing it with a new par swap), reported swap transaction volumes are inflated by this practice. A 30Y swap can be re-couponed many times throughout its long life, but would be initiated only once. As a result, the re-couponing volume may completely dominate the observed trade universe.