---
title: "Fixed Income - Alexander During-12"
type: raw_source
source_pdf: "Fixed Income - Alexander During-12.pdf"
extractor: docling
---

## CHAPTER 11

## Trading and Settlement

T he process of trading is the process of negotiating and agreeing the details of a transaction in securities and derivatives between two counterparties. After trading, the next step is settlement where the transaction is finalised. The steps undertaken to manage settlement and any ongoing obligations between the parties are known as clearing.

## 11.1 TRADING

Financial markets have evolved over time and are still evolving in response to changing social conditions and technological process. Trading in financial instruments first resembled trading in physical markets where traders met physically in a market place to negotiate transaction details. Various market places were specialised in particular types of financial instruments and became formalised over time from sections of particular streets or coffee houses to more formal bourses [35, 59]. Traders with no direct access could make use of intermediaries who would trade on their behalf in remote markets.

## 11.1.1 Trading and price formation

Trading involves agreement on the price at which an exchange of asset happens. The negotiation of this price is to some degree subject to the incentives of the counterparties involved. Many investors are in some cases strongly incentivised to conclude a transaction quickly. For instance, a fund manager tracking an index will at times find it necessary to invest coupons received to re-establish a carry position in line with the index. On the other hand, an investor may judge available market prices to be advantageous for establishing a new position and thus be more concerned with price than with timing. In practice, the bargaining over the transaction price involves a trade-off between immediacy of transacting and the optimisation of price.

This notion has an important consequence for how new information is incorporated in market prices. It is unrealistic to assume that new information can immediately affect negotiated prices across all securities in a market. Instead, all markets have a hierarchy of instruments where news affects the most liquid instruments first and prices of other instruments react through the repricing of these most liquid instruments. In the USmarket, the most liquid instruments are the on-the-run (most recently issued) Treasury securities, followed by on-the-run agency mortgage bonds. In Europe and Japan, the most liquid instruments are bond futures contracts.

Market makers will typically build pricing models that reflect the liquidity hierarchy in order to provide real-time pricing of less liquid instruments. Actual prices of such instruments will then be a combination of the output of such hierarchical models and adjustments for recent supply and demand information. This latter component reflects the time and price preferences of investors in the market as much as can be observed by a particular dealer.

The pricing hierarchy is self-reinforcing because investors who express macroeconomic views through fixed income positions will react to data releases by trading the most liquid instruments first. In contrast, pricing for less liquid instruments can become opaque immediately after data releases before the more liquid instruments settle on a new price. This can have the side effect of a permanent liquidity premium carried by benchmark bonds. Such a premium is observed in the US but is more or less absent for the on-the-run securities in Europe or Japan given the more dominant role of futures contracts in those markets.

## 11.1.2 Trading venues

Most modern trading venues can be seen as structures that lie between two extremes. The first is a public exchange operating on the basis of a public order book. Exchange members can place orders in this public book and such orders are matched according to rules set by the exchange. Trades occur when opposing orders are matched against each other (fully or partially, depending on the exchange) and the exchange acts as intermediary. Because the most basic order type is a limit order ('execute a trade in xxx securities at a price of yyy or better '), such exchange structures are also known as a central limit order book or CLOB.

Some exchange-type trading venues allow for the posting and matching of orders without making these orders public. Such dark pools enable trading but do not serve the purpose of price discovery by the wider public or even the exchange members.

The opposite trading model to an exchange is the over-the-counter or OTC market. In this market structure, a special type of trader known as a market maker advertises a willingness to provide prices for certain financial instruments and to trade on these prices on a bilateral basis. Market makers typically provide prices only to known clients to protect against various risks. In an OTC market, every dealer has a bilateral relationship with every customer. Most exchanges instead provide intermediation services that mean that each participant only faces the exchange as a counterparty.

The concept of market making is not tied to that of a liquidity provider in a public market. A liquidity provider is a market participant who is generally willing to trade in response to price movements. In contrast to a market maker, the role of liquidity provider can be less formal and not advertised. Significantly, some market participants act as liquidity providers only in normal market environments but may consume liquidity in crisis situations.

In market parlance, a firm price is a price quote at which a trader (usually a market maker) is willing to execute while an indicative price does not necessarily imply a willingness to trade at that price. Generally, market makers provide indicative prices on a continuous basis but firm prices only on request. A price request must include the the trade size but not necessarily the side (buy or sell) that the requestor wishes to execute. A price is said to be two-way if it includes a bid and an ask (prices at which the trader market maker would buy or sell the instrument, respectively), a bid or ask price by itself correspondingly is a one-way price. A (very rare) quote in which bid and ask price are the same is known as a choice price 1 .

In practice, the extremes of exchange trading on the one hand and OTC trading on the other do rarely exist in these pure forms. Most public exchanges are in fact operating a mixed model where for at least some products, or trade sizes over a certain limit (so-called block trades), trades are negotiated outside the public order book and only published later. Exchanges also occasionally employ schemes where exchange members are financially incentivised to make markets in listed products by maintaining presence in the public order book. On the other hand, frequent and large issuers of bonds tend to ask investment banks to act as market makers in their bonds and monitor their activity. This establishes market structures that allow for easier price discovery and thereby move OTC markets closer to the setting of public exchanges.

## 11.1.3 The OTC trade lifecycle

Thetrade lifecycle is the sequence of steps between the initial trade negotiation and the final settlement of the resulting obligations between the trade counterparties. There is somevariation in the trade lifecycles of trades in different instruments and contracts but the aim of them is always identical: any asset transfers must faithfully reflect the intentions of the contracting parties at the time the trade was negotiated. At the same time, firms must protect themselves from unintentional errors and fraud. This requires a sufficient number of independent checks. Figure 11.1 shows a schematic overview of the parties involved and their main interactions in the lifecycle.

Generally speaking, a trade in the OTC market consists of the following steps which will be described in more detail later:

Inquiry A price taker (customer) inquires for a firm quote (one-way or two-way) from one or more market makers.

Negotiation Some form of communication between the parties takes place until the price taker accepts or rejects a price.

Agreement The market maker confirms that a trade at the negotiated price has taken place. Only after this step are both parties bound by the trade agreement.

Recording Customer and market maker record the trade in their systems.

Enrichment The original trade records are augmented with additional information, such as settlement instructions.

Reporting Some jurisdictions require the reporting of trades to regulators and potentially to data dissemination platforms (trade repositories).

1 It is not always irrational for a trader to provide a firm choice price even though this implies that the trader does not intend to benefit from buying at a lower price and selling at a higher price. A choice price maximises the chance of executing a trade. This can provide valuable information about market direction. It should be remembered that there is limited public disclosure of trading conditions in OTC markets.

FIGURE 11.1 The actors and interaction processes in the OTC trade lifecycle between 2 counterparties, A and B. Note that A and B may be using the same custodian in which case the Verfication/Settlement step would be internal to that custodian.

<!-- image -->

Pre-confirmation The front offices of customer and market maker exchange settlement instructions. Both sides compare the instructions received with instructions sent to spot discrepancies.

Allocation Institutional fund managers regularly execute trades for a number of funds in parallel and then ask the dealer to split the trade into pieces which are then allocated to various funds.

Confirmation After the trades have been agreed by the front offices, the middle offices of both counterparties exchange transaction details and report discrepancies.

Settlement instructions Both counterparties instruct their respective custodians to make the required payments and securities transfers.

Reconciliation Both counterparties compare the cash and securities positions reported by their custodians with the positions implied by the transactions that have taken place as recorded in their internal systems.

Before counterparties can transact, they generally conclude a so-called master agreement. Such agreements are highly standardised and templates are provided by industry organisations. An important aspect of the securities market is that communication between the parties can take place in a variety of forms (trading platforms, chats, email, telephone, fax). Whatever channel is used, instructions are considered binding if the other side reasonably understands them. Clarity in the language used is therefore essential to avoid miscommunication.

## The trade inquiry

An OTC trade starts when a customer asks one or more market makers to price a particular trade. At this stage of the process it is important that all parties are fully aware of all price-relevant information. At a minimum, this would be the security or contract details, the trade size, and the side of the transaction (buy or sell for securities, pay or receive for swaps, etc.). The latter is sometimes known as the verb. Some other details, such as settlement date or venue, can be left unspecified as long as they follow the market conventions that exist precisely for the purpose to simplify the trade process.

Atrade inquiry normally is not binding the customer in the sense that the customer has the option to reject all prices shown in response to the inquiry. However, because pricing an inquiry is not completely cost-free for market makers, it is considered detrimental to the relationship when customers frivolously ask for firm prices without any real intent to trade. A customer can ask explicitly for an indicative price to signal that a trade may not be intended. Conversely, a firm price inquiry signals an intent to trade and therefore reveals information about the direction in which the customer intends to adjust positions. As a result, the trade inquiry is an exchange of information. The customer reveals information about what security and size he or she is interested to trade in, and in case of a one-way quote inquiry, the direction of the trade interest. The market maker, by responding, reveals his or her estimate of a market-clearing price.

Trade inquiries usually are done 'in competition' ('in comp' in market vernacular) which means that a customer asks multiple dealers at the same time to quote on a particular trade. In some cases, this is mandated by regulation or internal trading rules. Whether such inquiries ultimately benefit the customer is not always obvious. On one hand, multiple dealers will compete to provide the best prices to the customer. On the other hand, the winning dealer will be subject to winner's curse which means not only that he or she sold at the lowest, or bought at the highest, price but also that the other dealers in the competition will be aware of the likely position of one of their competitors. A dealer might therefore adjust the quote depending on whether or not the inquiry is in competition or not. In addition, by alerting a larger number of dealers to the trade interest, the client might move the market in an adverse direction.

## Negotiation

Acustomer is free to ask a dealer to improve a quote and it is in any case assumed that a dealer will update a quote according to changing market conditions while the customer is considering the responses. Electronic trading platforms tend to impose minimum lifetimes for market maker quotes in the order of seconds, when trades are negotiated over the phone or electronic chats, less formal rules apply.

A quote is called subject when the dealer states explicitly the he no longer feels boundbyit, be it because too much time has passed since providing the quote or because the market has moved too much. In bilateral communication a dealer may indicate a quote going subject by stating 'subject' or 'your risk'.

In bilateral communication, a customer may attempt to guide a dealer by revealing information about other dealers' quotes ('seeing better away', etc.). Given that such statements are generally unverifiable, a dealer may discard such communication depending on the customer-dealer relationship. It is in any case up to the dealer to decide whether to move a quote in favour of the customer.

## Agreement

By convention, it is the customer who accepts a quote. On electronic platforms this is donebypressing a button, in bilateral communication by stating the relevant equivalent of 'mine' or 'yours' in whatever language is used to communicate. Important in this step in the communication is to reaffirm the intended side of the original inquiry. A customer who asked by phone or chat for a bid (indicating a willingness to sell) and then states 'mine' (indicating a buy confirmation) violates standard trade protocol and would signal a failure in the negotiation process.

By stating 'mine' or 'yours', the customer is bound to trade in the specified security in the specified size at the price quoted by the dealer unless the dealer rejects the trade.

Again by convention, a dealer must confirm the conclusion of the trade by some equivalent of 'done' or signal that the trade has not been concluded by some form of 'off that' etc. This convention gives the dealer an option to reject a trade that has already been accepted by the customer. In the FX market, this option is known as a last look but that term has a different meaning in the fixed income markets 2 . It is considered bad form to reject a trade unless there is an obvious reason such as a significant market move, late acceptance of a quote by the customer, and so on. A dealer can signal during the negotiation phase that a quote is no longer binding as mentioned above. Generally, unless a dealer confirms a trade with 'done' or the local language equivalent, no trade has been concluded. Whether a failure to honour a quote is a relationship issue between customer and dealer is not trivial.

It is not essential to follow the conventions outlined above. Trades executed away from electronic platforms involve human beings which implies a certain degree of freedom in how communication is structured. What is essential, however, is that both parties at all times are clear about what has taken place. The purpose of conventions is to reduce the incidence of misunderstandings and the main information-theoretical tool to achieve this is redundancy. For instance, the side the client wishes to deal on is evident both in the initial price request (asking for an offer signals the client will buy, asking for a bid means the client wishes to sell) as well as in the acceptance (a buying client accepts with 'mine', a selling client with 'yours'). In other words, the conversation conventions in the market involve deliberate duplication of information in different forms so that inconsistencies can be spotted easily. Electronic platforms can reduce such redundancies in the communication but need to replicate it in the user interfaces they present to human operators. For this reason, a sell transaction screen will usually not only have the word 'Sell' in a prominent location, but would normally also use a different colour scheme from a buy transaction screen.

2 In the fixed income market, a 'last look' means that a customer who has asked multiple dealers for a price is giving one dealer an option to take a last look and improve the price to conclude a trade. In other words, a last look is an option granted to one specific dealer selected by the client while in the FX world it is granted to the market maker by default.

## Recording

After a trade has been concluded (both customer and dealer agree that a trade has been done and on the trade details), the next step is for both customer and dealer to record it in their respective book-keeping systems. Electronic trading platforms automatically record trades on behalf of both sides of the trade and offer mechanisms to forward that information into the electronic booking systems used by client and dealer, known as straight-through processing, or STP. For trades concluded on the phone or via electronic chats, this step has to be performed manually. Phone lines are now generally taped and electronic chats also recorded so that the recording step at least in principle does not introduce room for misunderstandings. The following example of a perfectly normal conversation illustrates the relevance of trade recording:

Customer:

How are you left for 10 mio?

Dealer:

110.14

Dealer:

Off that

Customer:

Refresh pls

Dealer:

110.16

Customer:

Mine 10 mio for 110.16

Dealer:

OK, done.

In this case, customer and dealer would have executed a trade already (possibly on a different platform) and are therefore aware of the security involved and the side the customerwishestotradeon(here, customer buys). None of this information is evident from this chat protocol alone. The customer asks for a price and the dealer responds, only to revoke the quote shortly after. The customer asks for a refreshed price and accepts the response.

The recording step in the trade lifecycle is where the trader at the customer side and the relevant contact person at the dealer enter the trade into their relevant systems. In the example above that would require that both enter the security that was left out of the conversation above, and that both record the respective counterparties.

Clarity of communication is essential in avoiding situations where counterparties record conflicting versions of what has taken place. Because records of all communications exist, it is possible to reconstruct what exactly passed between counterparties when there are conflicting versions of what happened. A customer might respond 'Lovely!' to a quote in order to sarcastically indicate that a price is unacceptable while the counterparty would interpret it as 'Mine' and respond with 'Done'. A subsequent examination of phone tapes or chat protocols would do little to disentangle that sort of misunderstanding. The better route to correct trade recording is to stick to standard language. For instance, the customer above confirms size and price explicitly, and uses the words 'mine' and 'for' which both indicate a buy transaction. A sale would normally be confirmed with 'yours' and 'at'. Note that different markets use very different conventions, such as quoting yields or yield changes instead of prices 3 .

## Enrichment

Once a trade has been recorded, the bare trade information has to be augmented with the information required to successfully settle the trade. Normally, this is possible using information that both counterparties hold about each other in their respective counterparty databases. Such informaton would include standard security settlement instructions (SSIs) such as custodian and account details. For internal purposes, companies may add information about credits to be given to particular sales contacts or other statistical data. Generally, this process is automatic but front office staff have the option to override parts of the result, for instance specifying different custodian details from those filled in by default.

## Reporting

Many jurisdictions require trades to be reported and reporting obligations have increased since the financial crisis. Trade reporting can serve multiple purposes:

Price discovery The general public may have an interest to learn about the prices at which trades in certain securities have been concluded. Regulators therefore sometimes require market makers to report trades that have been concluded to central price dissemination platforms (known as a consolidated tape). Dealers in the OTC market generally oppose such price discovery on the grounds that they hold a balance sheet position as a result of the trade just concluded and would like to be able to unwind the position at a profit. It is therefore usually the case that large trades are disseminated to the wider market with a delay. The length of this delay, as well as the size cut-off for such delayed dissemination, are chosen to allow the dealer, at least in principle, to unwind or hedge the position without being taken advantage of by the wider market.

Public interest Aside from the narrow price discovery aim, the general public may have an interest in knowing about more general trends in financial markets. This would include aggregate trade volumes in classes of securities, types of counterparties involved etc., but may not involve price discovery on specific securities.

3 While trader communication is usually portrayed as terse, deliberate redundancies in fact abound in market vernacular. As Umberto Eco remarked (on page 249 in [32]) 'in a characteristic language, for every unit of one expression one is obliged to find a corresponding content-unit.' Trader language therefore stops short of becoming so terse as to make every possible statement meaningful. The general public may not be aware of these subtleties because the use of words in trader language has evolved away from their everyday meanings. This, however, is not specific to financial markets. The expression 'from time to time' means something very different to a lawyer than to a layman.

Systemic risk Regulators have an interest in knowing about interlinkages between financial firms. Knowing about trades that have been concluded can help in this endeavour, albeit only to the extent that regulators are able to analyse the resulting data sets. Such data on financial interlinkages is generally considered to be too sensitive for public disclosure.

Fraudandmoneylaundering Given the limited public discovery of OTC trading, there is a risk that traders collude to defraud their firms, or that trading is used to launder the proceeds of illegal activity. Financial firms generally have procedures in place that are designed to catch such activity but regulators may feel that they are better placed to conduct the required analysis. Regulators are in the advantageous position of having access to the data from multiple institutions. This advantage is, however, alloyed with the difficulty of having to analyse large sets of data coming from multiple institutions.

Note that for globally operating financial institutions a specific form of the trade reporting function is essential to manage their global risk management functions. While the various subsidiaries may be able to function more or less autonomously, they must report all the trades they conclude to their headquarters for aggregation and analysis.

## Pre-confirmation

Counterparties normally exchange trade pre-confirmations at the front office level as soon as trade details have been recorded internally, usually a few seconds or minutes after a trade has been concluded. The purpose of this process is to ensure that the trade and settlement details recorded in the systems of both parties match. Such matching is a precondition of successfully settling the transaction and costs will arise if problems are not caught at this early stage. Commercial providers offer standard tools for this process that integrate the pre-confirmation process into standard communication tools.

A small but significant portion of trades fails at this stage because manually recorded trade details do not match. This is usually the result of misunderstandings about trades conducted outside electronic platforms and can easily be rectified. Electronic trading platforms automate the pre-confirmation process because there is no uncertainty about trade details.

## Allocation

Allocation is an optional step in the trade lifecycle that is related to how institutional fund managers operate. Typically a manager is responsible for multiple funds that follow similar or even identical strategies but are legally separate. A trade executed by such a manager may therefore be meant for several such funds at the same time. In order to achieve maximum separation of the funds concerned, the fund manager may ask the dealer to split an agreed ticket into multiple parts and allocate them to several individual funds. The total amount of securities traded, and the total consideration paid, are unaffected by this process.

For the trade recording systems of both dealer and fund manager, the allocation process represents a meaningful complication. A single recorded trade has to be replaced with a multitude of trades for settlement purposes, and the relationship between these new trades and the original trade (which will never settle) needs to be preserved in case disputes arise at a later stage.

## Confirmation

Once the front offices of both counterparties have agreed the enriched trade details, they forward them to their respective middle offices for processing. The first stage of this process is for the middle offices to send confirmation messages on a pre-agreed platform, such as S.W.I.F.T. or fax. Any discrepancies discovered in this stage of the trade lifecycle are more costly to resolve because open questions have to be sent to the respective front offices for clarification which takes up valuable time. On the other hand, successful confirmation at the confirmation stage elevates a trade from an agreement between the front office staff to an agreement between the contracting firms.

When trade details cannot be matched at this stage, a counterparty's middle office may notify the other counterparty that it does not know the trade. The phrase 'don't know', or simply DK, is generally used in the English-speaking world to reject a trade confirmation that cannot be matched against any internally recorded transaction 4 . It should be borne in mind that to DK a transaction at this stage is not a free option to walk away from an unfavourably priced transaction for either party. Because so much data is recorded in the trade negotiation process by either party, a legitimately concluded trade can easily be reconstructed. Failure to agree on trade details at the confirmation stage are most likely to arise from human error, multiple recording of the same trade by one counterparty, or the failure to retract confirmation of amended trade details when errors were spotted in the pre-confirmation stage.

## Settlement instructions

Following succesful confirmation, both counterparties will instruct their custodians to settle the transaction. The custodians typically require shorter instruction periods than the standard trade cycles (e.g. T + 2 in Europe) so that settlement instructions need not be given as soon as confirmation has been successful. However, by instructing early, counterparties can use the pending transactions on their custodian accounts to check again that the transaction will settle as expected.

Custodians will not process transactions unless instructions received from the two counterparties match to a reasonable degree. After the pre-confirmation and confirmation cycle, this provides a third check on mismatched transactions. Because this check happens last, it is the most costly to unwind transactions at this stage. Counterparties therefore have a strong economic incentive to resolve any problems at the pre-confirmation stage.

4 As a result, the pseudo-verb 'to DK' has taken on a wider meaning in the financial sector as indicating the repudiation of a presumed contractual relationship.

## Fails

It sometimes happens that the seller of a security (either outright or in either leg of a repo transaction) fails to deliver that security to the other counterparty. This is known as a fail and is in principle an event of default. A partial fail is a situation where the seller can deliver some, but not all of the amount transacted. Some buyers accept partial settlement, some do not. Because fails can have multiple legitimate causes, it is extremely rare to declare a default on a failing counterparty. A typical cause for a fail is a clerical error in a repo financing transaction where a market maker has lent out inventory for funding and recalls that inventory from repo when it has been sold to a customer. If the internal interaction with the repo desk, or the external with the repo counterparty results in a delay, the outright sale will fail as a result of the repo fail. Less commonly, a market maker may believe that a particular bond is available in repo and sells it in the course of quoting to a customer, only to find out that it is not available after all. Various forms of settlement discipline exist to discourage fails.

The basic approach to discourage fails has been to let the economics of an agreed trade stand as they are even when a fail occurs. This means that if the buyer transfers the same amount of cash, and receives the same amount of the security, at a later date, then the fail is said to be cured. Because the seller of the security receives the same cash later, he or she loses the interest that could otherwise be earned on it while the fail continues. In essence, the seller lends cash to the buyer at a rate of 0% with the security as collateral. In other words, the seller borrows the security at a repo rate of 0% while the fail continues. When interest rates were higher, this was a sufficient incentive to encourage speedy fails mitigation. At the time of writing, interest rates are low, or even negative, so that this disincentive no longer exists to the same degree.

In the European market, this incentive was insufficient even when rates were higher because, as is discussed for instance in Chapter 28, specials rates can be very low relative to GC. It is not uncommon for bonds to trade 5% or more special. This implies negative repo rates for such special collateral even when rates are reasonably positive. Being able to borrow a special security at 0% by the simple expedient of not delivering would not be a sufficient disincentive. For quite some time, therefore, the European market has seen fails charges that reflect the actual cost of a fail. The US market only introduced such charges in May 2009 [39] in the form of a flat 3% fee. Fails charges are the most common way to disincentivise fails but do not cure fails. An additional disincentive is bilateral: A fund manager may simply choose not to interact in future transactions with a counterparty that has a consistently high fails rate. The loss of business should also incentivise that counterparty to improve its inventory management practices.

Multiple ways to cure fails exist, listed below:

Fails mitigation lending is a facility offered by some CSDs where a failing transaction is cured automatically by borrowing the security for delivery from a pool of collateral providers. Such lending is generally very expensive because the CSD sees this as a source of profit, while the collateral providers would not make their securities available in such a way if they did not earn at least the going market rate for lending them.

Dollar rolls and coupon swaps are the standard ways of dealing with fails in the US mortage market when TBA transactions cannot be settled as expected due to insufficient production.

Bilateral O/N and T/N repos are securities lending transactions with settlement terms that are shorter than the standard spot settlement. A trader finding that securities will not be available as expected can borrow them in time for spot (T + 2) settlement even at T + 1 or even T + 2 through non-standard repo terms. This can cure a fail, but obviously only if these transactions settle on time.

Buy-ins are transactions where the clearer or the counterparty that is being failed to buys the security in the open market to settle the transaction, with the purchase consideration being charged to the failing counterparty. Usually a buy-in is an option available to the securities buyer under some conditions set in the master agreement between the two counterparties. Buy-ins are extremely costly, easily subject to dispute over the execution terms, and may even fail if the security in question is indeed not readily available. In these cases, both the original seller (who is still trying to settle) and the buy-in agent are looking for the same security in the same market. The European Union has made buy-in transactions mandatory for transactions that fail beyond a certain period in the Central Securities Depositories Regulation (CSDR) as of 1 February 2021 5 .

With the exception of buy-ins, the failing counterparty can make some economic choice between continuing to fail, or use one of the available avenues to cure the fail. That being said, fails contradict the fundamental principle of bond markets, dictum meum pactum and market participants agree that fails should be rare exceptions.

## Reconciliation

Once a transaction has been settled, each counterparty will conduct a process of reconciliation between its internal books and the account statements received from its custodian or custodians. For instance, a counterparty that has sold EUR 10 million notional of security A would expect that its holding of this security at the relevant custodian has declined by exactly EUR 10 million while its cash holdings should have increased by the relevant consideration, taking into account all other transactions conducted for the relevant settlement date.

Problems identified at the reconciliation stage are difficult to resolve because they can in principle only arise as a result of errors made by the custodian, given that the relevant settlement instructions were approved by the counterparty itself.

## 11.1.4 The exchange trade cycle

Trading on a public exchange differs from OTC trading in that both counterparties generally do not know the identity of the other because both face the exchange or, more precisely, its designated clearing house as a central counterparty (cf. Chapter 12).

5 This aspect of the CSDR has been widely criticised by the financial industry.

This generally simplifies trade processing because neither counterparty requires settlement instructions other than those of the exchange. Trade reporting is also generally handled by the exchange. Given that most exchanges nowadays operate on purely electronic platforms, the scope for manual error in the confirmation and reconciliation process is also minimal.

Exchanges generally permit the use of their clearing facilities for trades in listed products that have been agreed outside the exchange trades (so-called off-exchange trades). This such cases two counterparties agree bilaterally the details of the trade and then cross them, bypassing the central limit order book of the exchange. The trade is then entered into the exchange's trade system as a block trade. Exchanges generally impose minimum sizes on such trades because such trades do not contribute to price discovery in the central limit order book. The reason why block trades exist is that they permit the transfer of exceptionally large amounts of risk without the information leakage that would occur if the trade interests were published in the order book before execution.

## 11.1.5 Trading in competition versus single dealer inquiries and orders

Multilateral trading platforms allow, and many fund management rules mandate, that each trade interest is shown to a group of dealers in competition and that the dealer with the best price is selected for execution.

In case of a tie between two dealers in a competitive quote (multiple dealers show the same price), it is up to the client to select who to award the trade to. It is a common courtesy, but not more than that, to select the dealer who printed the last trade with that customer.

The price shown by a dealer is usually valid only for a limited time period which is in the order of seconds for liquid markets. After this period, the quote is assumed to be subject, i.e., subject to the dealer still being willing to transact at this price.

Following a trade in competition, it is market usance to provide non-monetary rewards to some dealers. The winning dealer, who accepts the risk of the trade, will usually be told what his or her cover was, namely the price quoted by the next best dealer. This information may allow that dealer to adjust the next client quote, bearing in mind that the losing dealers may adjust their quotes as well, and potentially in the opposite direction. The dealer providing the cover price will usually only be told that he or she 'was cover' but with no or only a vague indication of how far they were from winning in order to protect the winning trader. All other dealers are usually told that the trade ended as even the information that the trade concluded ('traded away') may be valuable.

The competitive quote approach follows the logic that it is the fiduciary duty of a trader (who rarely trades his own money) to ensure the best execution of the trade. The countervailing argument to this thinking is that the winning dealer will have acquired a position as a result of the executed trade and will have to hedge or unwind this position. Since multiple dealers were alerted to the trade by the original inquiry, they will be aware of this trade interest and use this information to the detriment of the winning dealer. Any dealer asked to quote a price in competition will therefore factor higher hedge cost into the initial quote, defeating the purpose of best execution.

In practice, this argument has some merit for very large trades where it may indeed be advantageous for a client to ask a single dealer to execute the trade. That dealer can then hedge or unwind the position without the wider market being aware of what is happening. Pricing will generally be done relative to a market benchmark and clients that trade frequently will be able to judge whether they are better off asking for a single quote or trading in competition. For smaller trades, it is unlikely that information leakage is meaningful.

What should be noted, however, is that requiring multiple dealers in competition is not a sufficient precondition for best execution. Unless the dealers selected for the competition are indeed able and willing to provide competitive prices, the overall result may still be poor. As a tool to ensure best execution, a multiple quote requirement is therefore a very blunt instrument unless it is augmented by monitoring which counterparties were selected to compete. That being said, given that it is easy to check mechanically how many dealers were asked for a price on a given trade, it is a tool that lends itself to regulators.

Dealers will sometimes offer clients to work an order instead of quoting a firm price on the spot. Working an order means that the dealer will, on a best effort basis, try to execute the client's trade interest in the market over a period of time. In an illiquid market this may be preferrable to being told that the dealer cannot quote a firm price at all. However, an order provides a number of options to the dealer related to the timing of execution and hedging. A client may choose to grant these options to a trader in order to get the desired transaction done but should remain aware of the value of that option.

## Mistrades

A mistrade is a trade that was conducted at a clearly erroneous price. The difference between a mistrade and an erroneous trade confirmation is that with a mistrade, the trader agreed to trade at an off-market price. A mistaken trade confirmation is simply an error later in the trade recording process.

What constitutes a mistrade or fat finger error, and how it is dealt with, depends on the trading venue. Most exchanges and electronic trading platforms have mechanical rules to identify and automatically cancel mistrades. When counterparties interact bilaterally, the situation is less clear and no general rules exist. In principle, a trader who said 'Done' on a given trade is bound by his or her word 6 . In practice, however, it would be unreasonable for counterparties who interact on an ongoing basis not to allow for human error and be willing to set aside trades from time to time. On the other hand, declaring a mistrade should not be a free option to a dealer to cancel trades that in retrospect could have been executed at a more advantageous price.

## 11.2 SETTLEMENT

Settlement follows the trading of securities and gives finality to the transfer instructions that arise from each trade.

6 Viz. the motto of the London Stock Exchange, which still governs fixed income markets: Dictum meum pactum.

## 11.2.1 Settlement mechanisms

Settlement involves instructing banks that hold cash and securities to transfer these valuable assets between counterparties. In a bygone era, such instructions would be given independently after a trade had been concluded. For instance, the seller of a security would instruct the custodian to transfer ownership to the buyer, and the buyer would instruct a bank to transfer cash to the seller. The problem with this approach is that if one of the counterparties fails to fulfill its obligations, the other one would face an immediate outflow of an asset (because this side of the instructions would remain valid) but would enjoin other creditors in any attempt to settle the receipt of the other side of the transaction. This type of risk is usually known as Herstatt risk 7 or settlement risk.

Settlement risk remains in place for certain types of transaction where payments occur in different currencies and different locations. In the case of outright foreign exchange transactions, where this risk is most prevalent, a special bank (the CLS, or Continuous Linked Settlement, Bank) was set up to eliminate this risk. The mitigation technique used by this bank and others operating in simpler environments is known as 'delivery versus payment' or DvP. In a DvP process, a trusted bank will accept incoming asset transfers but only execute them if both parties have the necessary assets in account with that trusted bank. This process is similar to the use of escrow accounts in non-financial private sector transactions 8 .

The use of DvP involves the holding of assets at the trusted intermediary (which is usually a GCSD) and this warehousing is costly for all involved parties. To reduce this cost, DvP in bond markets is generally conducted not on a continuous basis but in so-called settlement cycles. At predefined times in a trading day, the intermediary will try to match and execute all transactions pending at that time. This process creates a netting benefit similar to that outlined in Figure 4.3 on page 23 while at the same time preserving the benefit of only finalising transactions that can actually settle in full.

## 11.2.2 Settlement conventions

When talking about time and trading, it is important to distinguish between two dates. The first is the valuation date which is the date on which prices are being observed. If a trade actually occurs, the same day is also the trade date. However, it takes some time to process a trade once it has been agreed between two parties, so the actual exchange of cash and securities happens usually at a later point in time, the so-called settlement date. Unfortunately, it is also common in the market to trade 'for value of . . . ' , meaning 'for settlement on . . . ' , so valuation date (trade date) is easy to mix up with value date (settlement date). Note that a security can be sold again regardless of whether the buy transaction has already settled or not. A trader can therefore trade in and out of an issue several times a day. All the required settlement instructions are handled by today's sophisticated back office systems. The only important requirement is that when settlement is set to occur, the necessary cash and securities are in the right accounts. Otherwise, the trade fails and penalties may be incurred.

7 The insolvency of the Herstatt Bank in 1974 took more than 30 years to resolve and was one of the less salubrious episodes of German banking regulation. The bank was ordered to suspend banking operations on 26 June 1974 but the wider market was not immediately informed. As a result, counterparties continued to pay Herstatt even though the bank would not make any outgoing payments. Some 35 years later, a government-owned German bank earned the newspaper moniker 'Germany's most stupid bank' by making payments to Lehman Brothers the day after the US company declared its insolvency.

8 For instance, transactions in German real estate usually involve the notary public entrusted with the transaction notifying the land registry of an impending sale. Upon confirmation of this notification, the buyer transfers the purchase price to an escrow account of the notary who then instructs the land registry to transfer title. When the title transfer is confirmed, the notary transfers the cash from the escrow account to the seller. While this process takes more time, it allows the unwinding of any transfers in case of unexpected problems.

When settlement is supposed to happen relative to a given trade date is generally decided by market convention although it is possible and common to agree earlier or later settlement between two parties on a case by case basis. By and large, most bond markets settle in T + 2, meaning settlement occurs two business days after the trade has been agreed. Because there is a risk that a counterparty defaults during these two days (note that with public holidays, T + 2 can easily become almost a week), market participants and regulators usually try to push the settlement times down. For instance, US and UK government bonds (Gilts) can settle T + 0, i.e., on the same day, under some circumstances. Money and FX markets usually settle T + 2. Note that until settlement, the buyer of a bond earns interest on the cash paid for the bond, while the bond holder accrues interest. Therefore, when settlement is done on a non-standard day, the price at which the bond is bought or sold is adjusted. Economically, the settlement date is the essential date of a transaction.

While shorter settlement periods reduce credit risk, they increase the cost of human error. In modern trading, counterparties' back offices usually confirm trade details to each other within minutes of a trade. This confirmation process ensures that when instructions are sent to the clearer by both counterparties, there is a minimal risk of a mismatch between these instructions (or indeed, that one of them is missing). If the initial confirmation fails, counterparties will seek to find and redress the reasons. The shorter the time between trade and settlement, the more likely it is that trivial misunderstandings can lead to delayed settlement because there is insufficient time for reconciliation.

On a historical note, conventions like T + 2 are referred to as rolling settlement because the settlement date is always rolling two days after the trade is done. In the (ancient) past, markets used fixed settlement where all transactions done in a certain period were all settled on a single day [59]. This was more practical when a lot of paper had to change hands, but of course nobody could be certain that the counterparty to any trade would still be able to settle on that day (fixed settlement days could then be spaced 60 days apart).

Incidentally, when two parties in a fixed settlement market agreed to settle on the following settlement day instead of the upcoming one, the trade was said to be backwarded. This term still survives in the word backwardation in the futures market. There, it describes the normal situation where the further away contract is cheaper than the front contract. The opposite of backwardation in this sense is contango.