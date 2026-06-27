---
title: "Fixed Income - Alexander During-31"
type: raw_source
source_pdf: "Fixed Income - Alexander During-31.pdf"
extractor: docling
---

<!-- image -->

## Standard Trading Strategies

## 30.1 DEFINITIONS

Atrade is a voluntary and deliberate assumption of market risk with the aim of closing out this position at a profit. Given the fallibility of human intelligence, a trade can also result in a loss. A trade need not be related to a new position in financial instruments, but can also be the deliberate decision not to adjust a position in the face of new risks or information.

The profit and loss (P&amp;L) of a trade is the valuation gain or loss associated with that trade, including any cash income or payments during the lifetime of the trade.

Investors make a finite number of trading decisions and the number of investors is large. It is therefore possible that 1 or more investors achieve a very high share of successful trades simply throgh the operation of the law of large numbers (a fraudulent way of achieving a perfect streak of success is outlined in [78]). This creates a natural limitation to how much one can learn from the trading experience of others. The success of a successful trader may be the result of sheer luck and replicating the same strategy might not be successful.

With this caveat, some ingredients to a successful trading strategy can be identified, as follows:

Rationale Atrade should have a clearly defined rationale, i.e., a clearly articulated justification for the expected outcome.

Profit target and stop-loss The trader should define an envisaged profit target and a loss level at which the trade will be closed out to prevent further losses.

Exit strategy At the time the trade is entered into, it must be clear how to exit it, with a rational assessment of the costs involved.

Consistency The motivation for the trade will be the expectation of some market price changes. The actual instruments chosen by a trade to express this view, and their position sizes, should match the analysis done.

The need for a clear trade rationale is the essential motivation for all preceding chapters of this book. Taking risks requires an understanding of the valuation mechanisms of the instruments involved. While this may at times be tedious, it is a prerequisite for understanding opportunities to take calculated risks.

Clearly stated profit targets and stop-loss levels allow a simple probabilistic calculation of capital risked for a given expected return. An old trader rule, 'let profits run and

## CHAPTER 30 Trading Principles

FIGURE 30.1 Illustration of the use of stop-loss levels and adjustments. X marks a stop-loss closing of the trade, the vertical lines in the stop loss adjustments denote the time of the adjustment. Time units are arbitrary.

<!-- image -->

cut losses short' translates into the idea to regularly revise stop-losses to follow positive gains from the trade. Instead of leaving the stop-loss at the initial level, an adjustment of the stop-loss to follow profit means that not all gains will be lost if the trade first moves into one's favour and then against it. Target levels can be similarly adjusted. If a target level has been reached, most traders would move their stop-loss to that level and leave the trade in place with a new target.

An illustration of systematic adjustment of stop-loss levels is given in Figure 30.1. The trade is assumed to start at a P&amp;L of 0 and 2 sample evolutions are shown. In Path 1, the trade is successful and every time the P&amp;L has moved up by a fixed amount, the stop-loss is moved up by this amount. The trade is not closed even after the initial target is reached and eventually the stop loss is higher than that target. Variations of this approach would be to adjust the stops periodically or to set them in terms of the underlying variable (e.g., yield or spread level) rather than P&amp;L. At the same time, trades can be closed out without waiting for a stop loss. In this illustration, since P&amp;L moves sideways between Time 9 and 11, a trader might decide to redeploy balance sheet and close out a trade with static performance.

A commonly assumed exit strategy is the 'greater fool' approach, namely the assumption that prices will continue to move in their current direction and there will be a new investor willing to take on one's position later. The name of this strategy stems from the phrase 'Who is more tool, the fool or he who follows the fool?' and it is usually related to late stages in a bubble. In these situations, there is no obvious justification for current valuations other than the observation that new buyers (or sellers) appear to be emerging. While money has been made with this approach, it does not require much in the way of analysis and will therefore not be discussed here.

In many cases, liquidity conditions can be correlated with market outcomes. For instance, a trade that is designed to inoculate a portfolio against large market swings needs to be designed with the understanding that such large market swings will probably lead to wider bid-offer spreads, or impaired access to repo funding. Trades that involve many legs, or borrowed positions in rare securities would then be subject to higher frictional costs.

Consistency tends to be the most common problem with trade implementation in fixed income markets because most fixed income instruments have a finite lifetime. A non-exhaustive list of examples is given below:

Model error Aspline model is used to identify rich and cheap curve sectors and a trade is designed to benefit from this mispricing. Because the trade involves actual bonds, it could be that in the cheap sectors in the spline model all bonds appear rich, or that in the rich sectors of the model all bonds appear cheap. This would be a sign that the model simply does not fit the curve, rather than that bonds are mispriced.

Basis Instead of implementing a trade in cash bonds, one could use futures contracts to minimise entry and exit costs. If the analysis is done in bonds, however, one needs to check that the basis is at fair value. It could be that the evolution of the basis will counteract the anticipated performance of the underlying bonds.

Sample bias Aninvestor concluding that a certain type of asset class (for instance, AA-rated bank bonds) is rich or cheap may implement a trade using a subset of this asset class (for instance, a single bond issued by an AA-rated bank). This exposes the trade to the idiosyncratic risk of this single bond in addition to the generic risk of this asset class.

Carry Atradermayconductananalysisthatsuggestsaspreadtradeandthenadjust the risk-neutral weights of the trade so as to achieve zero or positive carry when the original weights would result in negative carry. Because the adjusted weights do not reflect the original spread analysis, the trade is inconsistent with its rationale.

## 30.2 TRADE IDENTIFICATION

Theidentification of potentially profitable trading strategies is of course the crux of trading. The simplest approach is to simply collect a sufficient amount of data and then mine this data for significant deviations from the historical mean. This approach, optimistically called statistical arbitrage 1 [86], or stat arb, is comparatively straightforward. Because it is so straightforward, one could argue that it has limited potential because too much money is being wagered on it already. In fact, automated portfolio strategies (sometimes called smart beta strategies) are being offered by various providers. These strategies follow pre-defined statistical arbitrage algorithms which have been back-tested and optimised. A trader looking to exploit statistical arbitrage therefore competes with a number of computers watching the same relationships. An often overlooked limitation of statistical arbitrage is that, by construction, it misses half of the potential opportunities to make profits. Waiting for a given spread to be away from its perceived equilibrium level, and then putting on a trade that benefits from the reversal is statistical arbitrage. That approach means, however, passing up the chance to profit from the initial move away from the equilibrium level. This is not to say that statistical arbitrage does not work, but one should be aware of its constraints.

1 Strictly speaking, 'arbitrage' is a term reserved for riskless strategies. Because statistical arbitrage relies on past probability distributions remaining unchanged; it is not riskless, and therefore not arbitrage.

An alternative approach is to establish positions ad hoc, based on some perceived insights into near-term market moves. The difference to statistical arbitrage is that ad hoc strategies can take into account information outside market rates while statistical arbitrage usually only considers market rates themselves. One would hope, albeit perhaps falsely, that additional information and human intellect can create an edge over purely statistical strategies.

The synthesis of these 2 approaches is common sense. If one has a reason to expect a given market move, one can consider a trading strategy. If a certain spread is far from its mean, that could be an indication that it will be reverting to that mean. That said, even when one detects such a statistical anomaly, one should first try to understand why it happened in the first place. Investor behaviour could have changed, and so could the regulatory environment. Different macro-economic environments affect curve shapes in different ways. Seen in this way, a small dislocation might be a harbinger of bigger things to come and expecting a continuation might be more profitable than positioning for a reversion.

Deciding on a trading strategy is only the first part of the process. The next step is the selection of specific instruments and the notional positions that will be held in each instrument. The determination of nominal amounts depends on the risks (PVBP) of each instrument and may also incorporate other factors as discussed below. The specific instruments to be used depends on the trade strategy but can also be influenced by other considerations such as liquidity of relative valuations. A long position in 10Y bonds would by default be established in the most liquid 10Y bond, but a trader might decide that a nearby comparable bond is relatively cheap and therefore purchase this alternative bond instead.

## 30.3 TRADE PORTFOLIOS

Few reasonable traders would commit all available risk capital to a single trade. This meansthat for a given risk capital budget, multiple trades compete for risk capital, bearing in mind that different trades may partly compensate inherent risks. Risk therefore has to be rationed across active trades.

While models exist for this purpose, notably the Black-Litterman model [56], there are some fundamental challenges to doing so in an epistemologically consistent manner. Mean-variance optimisation, for instance, is a single-period approach that is hard to reconcile with portfolios of trades that have diverse expected horizons. In addition, complex trades tend to have strongly non-normal return distributions so that mean and variance are insufficient to describe their risk profiles. Last but not least, trades tend to be determined on the basis that a recent development will revert (statistical arbitrage), or that a trend will change. This would normally imply adjusting one's expectations, not only of expected returns (means) but also of correlations (variances), not to mention higher-order moments of the relevant multi-dimensional distributions.