---
title: "Fixed Income - Alexander During-35"
type: raw_source
source_pdf: "Fixed Income - Alexander During-35.pdf"
extractor: docling
---

## CHAPTER 34 Bond Index Mechanics

A bond index is a default portfolio designed to represent an investable market subset. Multiple index providers compete in providing indices that represent, as well as possible, potential investment universes and the actual risks and returns available in these universes.

## 34.1 BOND INDEX PRINCIPLES

The fundamental requirements of any market index are threefold:

Ex-ante definition means that the index universe should be known ex-ante and not only ex-post. This rules out index definitions like 'the ten best-performing stocks of the current month', or return definitions like 'the top decile of actively managed funds'. This requirement ensures that an actual portfolio manager is able to make investment decisions based on information available at the time of investing.

Replicability adds the requirement that the index can actually be bought in the market. This constraint is particularly important when instruments included in the index differ in liquidity.

Broad bond market indices tend to include the entire universe of bonds satisfying the index criteria. Corporate bonds older than one year, however, tend to be virtually unattainable under normal market conditions. An index including them is therefore relevant to long-running bond portfolios but practically impossible to replicate with newly invested money.

Animportant qualification to the replicability criterion is that it refers to replication within the index universe itself. More complex indices virtually rule out replicability through return calculations that are unrealistic. The REX index of German government bonds produced by Deutsche Börse involves theoretical bonds with coupons that do no exist in the market at the time of writing. However, investors are able to replicate REX index returns by resorting to substitute bonds outside the German government bond market such as German Pfandbriefe. Such investment strategies do expose investors to off-index risks, in this case for instance the spread and relative liquidity risks of government and covered bonds.

Measurability requires that the index can be valued at a reasonable, for instance daily, frequency. This requirement ensures that any portfolio can be compared to the index at all times.

Measurability is one of the reasons why real estate and private equity indices are comparatively uncommon. These less liquid assets tend to trade rarely, and at prices that are not always fully transparent. It would therefore be unreasonable to offer an investment product that tracks the performance of such illiquid assets.

A bond index offering therefore consists of 2 independent elements. One is the time-varying set of bonds that constitute the index members, with the index provider warranting that eligible bonds are reliably identified and screened, and their outstanding amounts known. Mathematically speaking, this information amounts to a map of bond identifiers to outstanding amounts:

<!-- formula-not-decoded -->

where Ni = 0 when bond i is not included in the index. The second is a realistic pricing for the constituent bond set, which should be as close as possible to executable prices. This also amounts to a map from bond identifiers to prices:

<!-- formula-not-decoded -->

where p i is the market price of a given bond i . As bond performances are calculated, other return factors, such as coupon payments, accrued interest, and inflation uplift (if applicable) would be taken into account. These return elements are, however, independent of market developments and can therefore be processed in a mechanical way.

Asdescribed in Chapter 18 on liquidity, the idea of a universally applicable price for a given asset at a given time is unrealistic. Pricing depends not only on the asset or the time, but also on the execution venue, the set of available counterparties, and the client in question. Index providers tend to resolve this ambiguity through averaging across multiple price providers, observed trades and so on. As a general principle, because index prices tend to be used to value portfolios, the relevant prices are bids because accounting standards require valuations of long positions on the basis of a liquidation trade. An exception is that bonds entering an index are valued at the ask side because the presumption is that a portfolio tracking the index will have to purchase, rather than sell, these bonds. As a result, indices incorporate an implied bid-offer spread that makes tracking errors more realistic.

Bond indices tend to be constructed such as to encompass multiple markets. This creates a fundamental problem for cross-market portfolios that attempt to reallocate investments from one market to another because there are different settlement conventions in different markets. For instance, an investor looking to sell a Japanese government bond portfolio to reinvest in US Treasuries is faced with the problem that JGBs settle T + 2 1 , so the cash obtained from selling the Japanese bonds will come due only

1 Note that T + 2 does not apply during the coupon period of JGB. Depending on the transaction date and the bond in question, settlement might occur later.

2 business days after the sale. This matches the T + 2 settlement of the FX transaction turning the Yen received into US dollars. However, US Treasuries settle T + 0 or T + 1 so that the the cash to pay for the purchase is not available in time to settle this leg of the trade. The standard solution to this problem is to ignore it. Bond index returns are calculated on a common T + 0 settlement basis across all markets. This makes virtually all derived information of the bond pricing incorrect in virtually all markets but leads to a consistent outcome for global indices. In practice, fund managers are able to negotiate trades on non-standard settlement in any case. In the example above, a fund manager could negotiate the US Treasury purchase on a T + 2 settlement and the trader offering the pricing would simply repo the bonds in question for one or two business days before delivering to the fund manager.

## 34.2 INDEX REBALANCING

Bonds are being issued, and mature, on a daily basis. This would normally imply that a bondindex-linked to market capitalisation changes on a daily basis as well. Rebalancing a bond portfolio tracking a few hundred securities every day in response to such supply events would lead to excessive transaction costs given the large number of required daily transactions. Because that approach is untenable, indices generally concentrate adjustments to the set of index constituents, and their outstanding amounts, usually to the last day of a trading month. Indices of less liquid markets may be rebalanced less frequently (usually quarterly) while daily rebalanced indices are available for comparison purposes at some index providers.