---
title: PBOC CFETS Infrastructure
aliases:
- China Foreign Exchange Trade System
- National Interbank Funding Center
- China Money
- CFETS Plumbing
type: mechanism
tags:
- china
- pboc
- infrastructure
- fx-market
- money-market
- transmission
status: verified
confidence: 5
expert_lens: "Treasury Desk Strategy | PBoC Operational Framework"
thesis: "The China Foreign Exchange Trade System (CFETS) serves as the central nervous system of China's interbank markets, providing the technical infrastructure for price discovery, centralized clearing, and monetary policy transmission across FX, Money Market, and Bond sectors."
created: '2026-05-08'
updated: '2026-05-08'
---

## 1. Operational Overview
CFETS (China Money) is the primary venue where the PBoC implements its monetary policy and where commercial banks manage their liquidity and FX risk. It consolidates fragmented trading into a unified electronic platform (FX2017 system).

## 2. FX Market Plumbing

### A. RMB/FX Spot
- **Definition:** Exchange of RMB and FX settled/delivered within T+2.
- **Trading Mechanisms:**
    - **Anonymous:** PBoC's preferred mode for "Stealth Intervention" through state-owned banks to maintain the CNY within its +/- 2% daily band without revealing the central bank's direct footprint.
    - **Bilateral:** Used for high-volume block trades where counterparties have established credit lines.
    - **Matching:** Automated matching based on best price.
- **Instruments:** USD/CNY, EUR/CNY, JPY/CNY, HKD/CNY, GBP/CNY, and 20+ other pairs.
- **Clearing:** Centralized clearing via Shanghai Clearing House (SHCH) for anonymous trades; bilateral or CCP for others.
- **Treasury Insight:** Used to "Square the Position" (e.g., selling USD surplus acquired from clients). Traders must monitor Spot vs. Central Parity to avoid PBoC "slapping back" the market near the 2% limit.

### B. G10 Currency Pairs (Global FX Hub)
- **Definition:** FX transactions among foreign currencies (e.g., EUR/USD, USD/JPY).
- **Instrument Depth:**
    - **Spot, Forward, Swap:** Standard financing and hedging tools.
    - **Cross-Currency Swap (CCS):** Crucial for funding swaps (e.g., swapping EUR for USD).
    - **Options:** Includes Vanilla, Asian, Barrier, and Digital options, reflecting advanced technical capacity.
- **Execution Models:**
    - **ESP (Executable Streaming Prices):** Low-latency "Click-and-Deal" for smaller tickets from 30+ Liquidity Providers (LPs).
    - **RFQ (Request for Quote):** Bespoke quoting for large block trades to minimize price slippage.
- **Treasury Insight:** Centralized credit lines allow smaller banks to access top-tier liquidity from global LPs (MUFG, ANZ, etc.) by eliminating bilateral credit constraints. Traders can watch quotes for all pairs via a single log-on (FX2017).

### C. RMB/FX Regional Trading (De-dollarization Infrastructure)
- **Strategy:** Direct trading between CNY and regional currencies (IDR, MYR, RUB, KZT, KHR, MNT) to bypass the USD as a cross-currency bridge.
- **Formation:** CFETS inquires market makers before market open (9:15 AM / 10:15 AM) to calculate the average Reference Rate.
- **Plumbing Logic:** Facilitates direct BRI trade settlement, reducing conversion costs and SWIFT/USD dependency.
- **Treasury Insight:** Used to design direct hedge products (e.g., CNY/KZT Forwards) for infrastructure projects in BRI corridors.

## 3. Money Market & Currency Lending (The Liquidity Engine)

### A. Foreign Currency (FCY) Lending & Repo
- **USD Onshore Liquidity:** CFETS provides a domestic money market for USD, EUR, HKD, etc., reducing Eurodollar reliance.
- **USD CIROR (CFETS Interbank Reference Offered Rate):**
    - **Definition:** A simple-interest, unsecured wholesale rate for USD calculated from quotes of top-tier panel banks.
    - **Mechanism:** Arithmetic average of panel bank quotes at 10:00 AM (after excluding two highest and two lowest).
    - **Tenors:** 8 terms from O/N to 1-Year.
    - **Plumbing Logic:** Serves as the primary benchmark for onshore USD credit pricing. Deviations between USD CIROR and offshore SOFR indicate the efficacy of China's capital controls and local USD scarcity.
- **Lending vs. Repo:** 
    - **FCY Lending:** Unsecured short-term financing (O/N to 1Y) to adjust surplus/deficiency.
    - **FX Repo (Bridge Mechanism):** Pledging **Onshore RMB Bonds** as collateral to borrow USD. This creates a liquidity bridge between domestic bond holdings and foreign currency needs.
- **Reference Rates:**
    - **Weighted Average Rate (WAR):** Volume-weighted average updated twice daily (11:00 & 17:00).
- **Treasury Insight:** Treasurers compare **USD CIROR** with the **Implied USD Yield** from RMB/FX Swaps. If CIROR is higher, banks prefer using FX Swaps to source USD liquidity. PBoC monitors the **MA-5/MA-20 CIROR trends** to detect structural shifts in domestic foreign currency demand.

### B. RMB Money Market (Interbank Infrastructure)

#### 1. Interbank Lending (Unsecured RMB Financing)
- **Definition:** No-guarantee financing among financial institutions (Banks, Securities firms, Rural Co-ops).
- **Mechanism:** Bilateral trading with **Gross Settlement** at the trading parties' own risk (T+0 or T+1).
- **Benchmarks (DIBO):** 
    - **DIBO (Depository-institutions Interbank Offered Rate):** Weighted average rates collected from deposit-taking institutions (Banks, Rural co-ops, etc.).
    - **Data Points:** Includes Weighted Average Rate, Latest Rate, and Weighted Average Lending Days (actual maturity).
    - **Plumbing Logic:** Provides the purest view of core banking liquidity by excluding non-bank financial institutions.
- **Treasury Insight:** The **DIBO Term Structure** reveals expected liquidity shifts. An inverted DIBO curve (e.g., 1M > 3M) indicates market expectations of PBoC liquidity injections. The **Weighted Average Lending Days** metric allows Treasurers to calibrate the duration of their funding gaps.

#### 2. Pledged Repo (Secured RMB Financing)
- **Definition:** Short-term financing where bonds are used as a **Pledge of Rights**. The borrower (Positive Repo) retains ownership but pledges the bonds to the lender (Reverse Repo).
- **Mechanism:** Bilateral trading with **Gross Settlement**. Supports three settlement modes: **DVP (Delivery Versus Payment)**.
- **The DR Series (The Liquidity Pulse):**
    - **DR Series (Depository-institutions Repo):** Repo rates specifically for **Depository Institutions** (Policy banks, Commercial banks, Rural co-ops, etc.).
    - **Plumbing Logic:** Excludes non-bank players (Funds, Securities firms), making DR series the **purest gauge of core banking system liquidity**. 
    - **Treasury Insight:** Treasurers monitor the **DR007** daily as the primary liquidity anchor. A stable DR007 indicates effective PBoC liquidity management. An inverted curve within the DR series (e.g., DR021 > DR1M) signals specific liquidity demand peaks (e.g., month-end payments) rather than systemic tightness.
- **Treasury Insight:** The **R007-DR007 Spread** remains the ultimate gauge of liquidity "hoarding" by large banks. A wide spread confirms that non-bank institutions are facing funding stress while banks remain liquid.

#### 3. Outright Repo (Trading & Ownership Transfer)
- **Definition:** A transaction where ownership of bonds is **actually transferred** from the seller (Positive Repo) to the buyer (Reverse Repo), with a simultaneous agreement to buy them back at a pre-defined price on a future date.
- **Mechanism:** Bilateral trading; unlike Pledged Repo, the lender gains full disposal rights over the bond during the term.
- **Plumbing Logic:** This tool enables **Re-hypothecation** and **Short-selling**. Since the lender owns the bond, they can sell it or pledge it elsewhere, increasing collateral velocity.
- **Treasury Insight:** Essential for **Bond Arbitrage** and directional bets. While Pledged Repo is for volume-based liquidity management, Outright Repo is for specific bond-driven strategies.

### C. Bond Market (Duration & Asset Pricing)

#### 1. Cash Bond Trading
- **Definition:** Spot transaction involving the permanent transfer of bond ownership at an agreed price.
- **Instruments:** Extensive range including Treasury Bonds, Policy Bank Bonds, Corporate Bonds, and **Asset-Backed Securities (ABS)**.
- **Mechanism:** Supports Bilateral trading and **One-click Trading** (automated matching of streaming quotes).
- **Treasury Insight:** Essential for **Yield Curve Construction**. The liquidity of the cash market allows Treasurers to adjust their portfolio's **DV01** (Dollar Value of a Basis Point) risk dynamically.

#### 2. Bond Forward
- **Definition:** Binding obligation to trade specific bonds at a pre-agreed price and quantity on a future date (up to 365 days).
- **Instruments:** Treasury Bonds, Central Bank Papers, and Financial Bonds.
- **Participants:** Market Makers act as the hub. Non-financial institutions are restricted to **Hedging-only** trades via Market Makers.
- **Treasury Insight:** Used for **Duration Locking**. Treasurers use Forwards to secure current yields for future investment plans without utilizing spot cash liquidity today.

#### 3. Benchmark Bonds & Yield Curve Mechanics
- **Benchmark Classification:** A basket of bonds selected weekly (Short-term) or monthly (Med-Long term) to anchor the yield curve. Includes CGBs, Policy Bank Bonds (CDB, EIBC, ADBC), and AAA-rated notes.
- **Real-time Yield Curve Construction:**
    - **Frequency:** Updated every minute from 9:30 AM to 17:00 PM.
    - **Data Hierarchy:** Prioritizes **One-click Deal Prices** (actual trades), followed by **Broker Quotes (CFETS-ICAP)** for T+1 settlement. Historical prices are used as the final fallback.
    - **Methodology:** Uses **Linear Interpolation** to connect key rate durations (0.25Y to 30Y), generating Bid, Ask, and Mid-market curves.
- **Closing Yield Curve Construction (The Valuation Anchor):**
    - **Publication:** Released daily at 17:15 PM.
    - **Methodology:** Uses a **Linear Regression Model** to derive Yield to Maturity (YTM), Spot Rate, and Forward Rate curves for 11+ bond types (including NCDs, ABS, and PPNs).
    - **Corporate Bond Nuance:** Explicitly separates **Secured** (e.g., AAA, AA+) from **Unsecured** (e.g., AAA2, AA2) corporate bonds, reflecting the distinct credit risk profiles in the RMB interbank market.
    - **Floating Rate Spreads:** Provides spread curves against benchmarks like **LPR_1Y** and **Shibor3M**, critical for pricing floating-rate notes.
- **Selection Criteria:** Based on six metrics: credit rating, **Key Rate Duration** (from 0.083Y to 30Y), number of market makers, quotation coverage, and the **Market-making Activity Index**.
- **On-the-run Bias:** Newly issued bonds are prioritized (scoring up to 35/100 points) to ensure the benchmark reflects the most liquid sector of the market.
- **Automatic Substitution:** Initiated if a benchmark bond lacks bilateral quotes for 5 consecutive days, replacing it with the next highest-scoring newly issued or sample bond.
- **Treasury Insight:** Treasurers monitor the **Liquidity Premium** of Benchmark vs. Sample bonds and the **Bid-Ask Curve Spread**. A widening spread in the real-time curve indicates increased market volatility. The **Closing Curve** serves as the primary **End-of-Day (EoD) Valuation** engine for regulatory reporting and mark-to-market (MtM) accounting, as its regression-based scrubbing process removes noise and outliers inherent in real-time data.

#### 4. Securities Lending
- **Definition:** A transaction where a borrower borrows specific bonds from a lender, pledging other bonds or cash as collateral.
- **Plumbing Logic:** Primarily used to prevent **Settlement Fails**. It increases bond "velocity" by allowing market participants to deliver bonds they do not yet own.
- **Treasury Insight:** The primary infrastructure for **Short-selling** and **Market-neutral strategies**. Unlike Repo (which is cash-driven), Securities Lending is **security-driven**, allowing traders to profit from the relative value between different bond issues.

### D. FX Derivative Market (Risk & Expectation Management)

#### 1. RMB/FX Forward
- **Definition:** Binding obligation to buy/sell foreign currency at a contracted rate on a specific future date (min. T+2).
- **Mechanism:** Bilateral and Matching (C-Forward). Covers USD/CNY and 20+ regional pairs.
- **Treasury Insight:** Used primarily for **Hedging** commercial flows. The Forward rate reflects the market's expectation of future Spot prices combined with interest rate differentials.

#### 2. G10 Currency Pairs Forward
- **Definition:** Binding obligation to trade foreign currency pairs (e.g., EUR/USD) at a contracted rate (> T+2).
- **Mechanism:** Bilateral trading.
- **Instruments:** 13 major pairs including AUD/USD, EUR/JPY, etc.
- **Treasury Insight:** Used for hedging non-RMB currency exposures directly on the CFETS platform.

#### 3. RMB/FX Swap (Funding & Liquidity Tool)
- **Definition:** Simultaneous execution of two opposite FX transactions (Short leg vs. Long leg) at different value dates.
- **Mechanism:** Bilateral and Matching (C-Swap). 
- **Plumbing Logic:** Functions as a **Secured Funding** mechanism. Banks use FX Swaps to manage RMB liquidity without altering their net FX position.
- **Treasury Insight:** Crucial for **Funding Arbitrage**. If domestic RMB repo rates (DR007) exceed the implied cost of an FX Swap, Treasurers will use USD holdings to swap for RMB, effectively using the FX market as a secondary liquidity pool.

#### 4. G10 Currency Pairs Swap
- **Definition:** Exchange of two foreign currencies at a contracted rate (short leg) and a reverse exchange at a future date at another agreed rate (long leg).
- **Mechanism:** Bilateral trading.
- **Instruments:** 13 pairs consistent with Forward instruments.
- **Treasury Insight:** Enables domestic banks to manage non-RMB currency mismatches (e.g., funding USD assets with EUR liabilities) directly within the Chinese interbank ecosystem.

#### 5. RMB Interest Rate Swap (IRS)
- **Definition:** Financial contract where two parties exchange interest streams calculated on a pre-agreed notional principal over a specified period.
- **Mechanism:** Bilateral and One-click trading via CFETS. Off-system transactions must be reported to CFETS by 12:00 AM of the next business day.
- **Reference Rates:** Authorised benchmarks including Shibor (3M, O/N), Repo rates (FR007, FDR007, FDR001), and LPR (1Y, 5Y).
- **IRS Curve Methodology:**
    - **Fixing & Closing Curves:** Derived from X-Swap quotations. Sampling occurs every 30 seconds during specific windows (11:45-12:00 for Fixing; 16:15-16:30 for Closing).
    - **Quotes Curves:** Published every 30 minutes for high-liquidity benchmarks (Shibor3M, FR007), providing real-time market sentiment.
    - **Computation:** Uses a **Trimmed Mean** approach (removing top/bottom 25% of samples) and weights based on the reciprocal of the bid-ask spread to ensure representative pricing.
- **Plumbing Logic:** Allows banks to manage **Duration Risk** and **Basis Risk** without exchanging principal, keeping the balance sheet lean.
- **Treasury Insight:** IRS is the primary **Forward-looking indicator** for monetary policy. Treasurers monitor the **Trimmed Mean Spread** to gauge true market liquidity—a narrower spread in the sampling window indicates high execution certainty. IRS curves for **FDR007** are particularly critical as they reflect the market's bet on future core-banking funding costs.

#### 6. Forward Rate Agreement (FRA)
- **Definition:** Contract to exchange interest payments (Fixed vs. Reference Rate) on a notional principal at a future date.
- **Mechanism:** Bilateral and One-click trading. Off-system transactions must be reported to CFETS for recognition by 12:00 AM the next business day.
- **Plumbing Logic:** Allows market participants to lock in a future interest rate today. Unlike IRS (which spans a period), FRA is a single-event future contract.
- **Treasury Insight:** Used for **Forward Rate Hedging**. Treasurers use FRAs to mitigate interest rate volatility for specific future funding requirements.

#### 7. Credit Risk Mitigation (CRM) Warranty
- **Definition:** Tradable financial certificates issued by a third party to protect the holder from the credit risk of an underlying entity's debt.
- **Mechanism:** Bilateral trading.
- **Infrastructure:** Supports indicative and dialogue quoting, market statistics, and data query functions.
- **Access:** Limited to institutions that have signed the NAFMII "China Inter-bank Market Financial Derivatives Transaction Master Agreement (CRMW Edition)."
- **Treasury Insight:** Functions as a domestic **CDS (Credit Default Swap)**. Provides a critical tool for managing **Counterparty Credit Risk** on corporate bond exposures.

#### 8. RMB/FX Cross Currency Swap (CCS)
- **Definition:** Long-term obligation to exchange interest payment streams and principal amounts in different currencies.
- **Key Curves:**
    - **CNY-Fixed vs. USD-SOFR:** 1Y to 5Y tenors; uses CNY-3M Fixed Rate and USD-SOFR benchmarks.
    - **CNY-Shibor3M vs. USD-SOFR:** 1Y to 5Y tenors; uses CNY-3M Shibor and USD-SOFR benchmarks.
- **Calculation:** Quotes from market makers in the USD/CNY forward/swap market. Uses a trimmed mean (excluding highest/lowest 2 if N >= 8) to establish Bid/Ask curves.
- **Plumbing Logic:** Primarily a **Balance Sheet Hedging** tool. It allows banks to match the currency of their assets (e.g., USD loans) with their liabilities (e.g., CNY deposits).
- **Treasury Insight:** Used for **Basis Trading**. The spread over reference rates (e.g., Shibor vs. SOFR) reflects the "Cross-currency Basis," indicating the structural cost of swapping RMB for USD over long horizons.

#### 9. RMB/FX Options (Volatility & Delta Pricing)
- **Definition:** Right (not obligation) to trade FX assets at a pre-agreed rate on expiration (Vanilla European).
- **Volatility Types:** ATM, 25D/10D Call/Put, Risk Reversal (RR), and Butterfly (BF).
- **Vol Curve Construction:** Samples include CFETS transaction vol, broker quotes, and bilateral quotes. Broker quotes are preferred unless spreads are wide.
- **Delta Pricing Parameters:** Published daily at 17:00, incorporating FX Spot (Central Parity/Mean Quote), Volatility curves, and CNY/USD interest rate curves (Shibor, IRS, CIROR).
- **Plumbing Logic:** Options introduce **Delta/Gamma/Vega** management. Unlike Forwards, Options have a non-linear payoff, allowing Treasurers to hedge asymmetric risks.
- **Treasury Insight:** Treasurers use RR and Butterfly metrics to gauge market sentiment on CNY directional risk. High volatility skew (RR) indicates PBoC intervention fear or extreme directional hedging activity.

### E. Interbank Benchmarks (Policy Formation)

#### 1. Shibor (Shanghai Interbank Offered Rate)
- **Definition:** A simple, unsecured, wholesale interest rate calculated by averaging interbank RMB lending rates.
- **Panel:** 18 commercial banks with high credit ratings (OMO primary dealers or FX market makers).
- **Publication:** Released daily at 11:00 AM (Beijing Time) for 8 maturities (O/N to 1Y).
- **Mechanism:** Arithmetic average of quotations after excluding the 4 highest and 4 lowest values.

#### 2. LPR (Loan Prime Rate) — Post-2019 Mechanism
- **Mechanism:** `LPR = OMO Policy Rate (e.g., 7-day Reverse Repo) + Bank Margin`.
- **Panel:** 20 quoting banks submit quotes before 9:00 AM on the 20th of each month (0.05% step length).
- **Tiers:** 1-Year (Asset pricing) and 5-Year+ (Mortgage anchor).
- **Treasury Insight:** LPR is the "Output Price." A failure of LPR to track policy rate cuts signals a **Broken Transmission** or margin hoarding by banks.

#### 3. Interbank Fixing Repo Rates (FR & FDR)
- **Calculation Window:** 9:00 - 11:30 AM daily.
- **Methodology:** Sort all transaction rates in ascending order (N samples); the fixing rate is the interest rate at position `[N/2] + 1` (Median-based).
- **Series Distinction:**
    - **FR Series (FR001, FR007, FR014):** Based on all repo trades (R series), including non-bank institutions.
    - **FDR Series (FDR001, FDR007, FDR014):** Depository-institutions fixing repo rate. Only includes trades between banks using Treasury, Central Bank, or Policy Bank bonds as collateral.
- **Treasury Insight:** The **FDR series** is the cleanest indicator of core bank funding costs. Treasurers use the spread between FR and FDR to monitor non-bank liquidity stress.

### F. CNY Central Parity Rate (FX Anchor)
- **Definition:** The daily "Fixing" rate published by CFETS at 9:15 AM, setting the midpoint for the intraday trading band (+/- 2%).
- **Calculation Mechanism:**
    - **USD/CNY:** A **Weighted Average** of quotes from all market makers (after excluding outliers). Weights are based on transaction volume and market-making performance, giving major state-owned banks higher influence.
    - **HKD/MOP:** Calculated via **Cross-rates** with the international USD/HKD and HKD/MOP markets at 9:00 AM.
    - **Other Currencies:** Determined via a **Simple Average** of market maker quotes (after excluding outliers).
- **RMB Index (Basket-based Management):**
    - **Indices:** CFETS publishes three primary indices (CFETS RMB Index, BIS Basket, and SDR Basket) every Monday at 08:30 AM.
    - **Logic:** Uses the **Geometric Mean** method to aggregate central parity rates of component currencies, with weights derived from international trade volume.
    - **Policy Anchor:** The 31st Dec 2014 baseline (100 pts) serves as the long-term stability benchmark.
- **Historical Expansion:** The system has evolved from 4 major pairs in 2006 to over 25 pairs by 2024 (including MOP, THB, and RUB), reflecting the PBoC's RMB internationalization and BRI direct-settlement strategy.
- **Corporate Benchmarking:** CFETS provides **Monthly and Annual Average Central Parity Rates**, which are the standard benchmarks for corporate accounting, tax valuation, and long-term trade contract pricing.
- **Treasury Insight:** Treasurers monitor the gap between the **Market Spot Rate** and the **Central Parity**. If the Spot rate consistently pushes the 2% limit, it signals extreme devaluation pressure, prompting the PBoC to adjust the CCF to stabilize expectations. The deviation of current fixing from the **Monthly Average** (e.g., 6.8502 current vs. 6.8683 average) reveals the PBoC's immediate policy bias toward RMB strength or weakness. Major banks' quotes carry disproportionate weight, making their sentiment a key lead indicator for the daily fix. The **RMB Index** is used to distinguish between USD-specific moves and broad-based RMB strength; a stable Index despite USD/CNY volatility suggests the PBoC will refrain from direct intervention.

## 4. Clearing & Settlement Logic
- **Shanghai Clearing House (SHCH):** Acts as the **Central Counterparty (CCP)** for anonymous trades, triaging counterparty risk.
- **Plumbing Benefit:** Centralized clearing net out exposures, significantly reducing systemic risk and allowing high-velocity trading even during periods of market stress.

## 5. Market Data (Real-time & Analytics)

### A. RMB/FX Spot Quotes
- **Definition:** Real-time Bid/Ask quotes for major FX pairs and regional currencies against the RMB.
- **Mechanisms:**
    - **ODM (Order Driven Matching):** An order-book based matching system that reveals market depth, allowing Treasurers to assess potential slippage before executing block trades.
    - **Live Spreads:** The Bid-Ask spread serves as the primary gauge of market liquidity. Narrow spreads (e.g., 1 pip for USD/CNY) indicate deep liquidity; wide spreads signal market stress or fragmentation for non-major pairs.
- **Treasury Insight:** Treasurers monitor spreads to determine execution strategy. For pairs with thin liquidity (high spreads), **RFQ (Request for Quote)** is preferred over direct order-book matching to avoid price impact.

### B. G10 Currency Pairs Quotes
- **Definition:** Real-time indicative Bid/Ask quotes for 13+ global currency pairs (e.g., EUR/USD, USD/JPY) traded on the CFETS platform.
- **Mechanisms:**
    - **Indicative Price:** Driven by bilateral quoting from global Liquidity Providers (LPs).
    - **Zero-Spread Dynamics:** Highly competitive pairs (e.g., EUR/USD, GBP/USD) often exhibit near-zero spreads, indicating deep market liquidity and efficient local consolidation of global FX prices.
- **Treasury Insight:** Treasurers use this data to perform **Triangular Arbitrage** and manage global currency exposures locally, minimizing the need for international correspondent bank intermediation. A stable, narrow spread on USD/HKD or USD/JPY serves as a reliable liquidity proxy for global market conditions.

### C. Outright Repo Market Stats (OR Series)
- **Definition:** Real-time and weighted average rates for Outright Repo transactions.
- **Instruments:** OR001, OR007, OR014, OR3M.
- **Plumbing Logic:** Since ownership is transferred, OR rates can deviate significantly from Pledged Repo (DR) rates due to specific bond demand. 
- **Treasury Insight:** An extremely low OR rate (e.g., OR007 at 0.4% vs. 1.3% weighted average) indicates specific "special" bond demand or ownership transfer trades rather than general liquidity needs. Treasurers use the OR-DR spread to detect collateral-driven vs. cash-driven market stress.

### D. Cash Bond Market Stats
- **Definition:** Real-time transaction prices and Market Maker quotes for sovereign and corporate bonds.
- **Data Attributes:** Clean Price, Yield (%), Change (BP), and Trading Volume.
- **On-the-run Bond Liquidity:** High-volume benchmarks (e.g., current 10Y/30Y Treasuries) serve as the primary liquidity anchors for the entire RMB credit market.
- **Market Maker Quotes:** Streaming Bid/Ask yields from top-tier contributors (e.g., CITIC Securities, China CITIC Bank).
- **Treasury Insight:** The **Yield Bid-Ask Spread** reflects the liquidity premium of specific bond issues. Treasurers analyze the **30Y-10Y Treasury Spread** to gauge long-term inflation and growth expectations, positioning their portfolios to profit from curve steepening or flattening.

### E. RMB/FX Swap Quotes & Yield Curves
- **Definition:** Real-time quotes and curves for FX swap points across tenors from O/N to 5-Year.
- **FX Swap Curve (Benchmark):** Aggregates dealt prices, RFQ quotations, and money broker data. It serves as the official pricing benchmark for middle/back-office **Mark-to-Market (MtM)** valuations.
- **USD/CNY C-Swap Curve:** Based strictly on the centralized order-book system, providing high-execution-certainty swap points for tenors up to 1-Year.
- **Data Source Priority:** 
    - **Trading Prices:** Used for short-to-medium tenors (< 18M) where liquidity is high.
    - **Quotes:** Used for long tenors (2Y-5Y) where actual trades are infrequent.
- **Swap Point Logic (IRP):**
    - **Negative Points (Discount):** Reflects that RMB interest rates are lower than the foreign currency (e.g., USD/CNY 1Y at -1618 pips).
    - **All-in Rate:** The effective exchange rate for the far-leg of the swap.
- **Treasury Insight:** Treasurers monitor the **Swap Curve Slope**. A deep discount in long tenors (-7460 pips for 5Y) indicates a structural expectation of prolonged interest rate differentials between the PBoC and the Fed. Treasurers use the 2Y-5Y quotes to hedge long-term project financing (e.g., BRI infrastructure) while remaining aware of the liquidity risk inherent in "Quote-only" tenors.

### F. Implied Foreign Currency Interest Rate Curves
- **Definition:** Synthetic interest rate curves for foreign currencies derived using the **Interest Rate Parity (IRP)** theory, combining CNY interest rates and FX swap prices.
- **Parameter Combinations:** CFETS publishes 6 types of curves based on various inputs:
    - **CNY Base Rate:** Shibor (for <1Y), Shibor3M IRS, or FR007 IRS.
    - **FX Inputs:** FX Swap Pips and Spot Prices (Central Parity or Mean OTC Quote).
- **Calculation Logic:** Uses **Continuous Compounding** to derive the implied rate ($r_f$) from the domestic rate ($r_d$) and the forward/spot ratio: $r_f = r_d - \frac{1}{T} \ln(1 + \frac{Pips}{Spot})$.
- **Treasury Insight:** The **Implied Rate vs. Cash Rate Spread** is the ultimate indicator for **Funding Arbitrage**. If the implied USD rate from the curve is lower than the actual **USD CIROR** or offshore SOFR, Treasurers will choose to source USD through FX Swaps (selling CNY/buying USD forward) rather than direct borrowing, effectively lowering their overall cost of foreign currency funds.

---

## 6. Structural Mapping: CFETS as Policy Transmission Belt

```ascii
========================================================================================
|                     [1] POLICY INTENT & CENTRAL PLATFORM                             |
========================================================================================
          ( PBoC / Central Bank ) ----------------> { CFETS FX2017 Platform }
                  |                                            |
                  v                                            |
        [ Policy Tools: OMO, MLF ]                             v
                  |                                  (Market Plumbing)
==================|=====================================================================
|                 |           [2] INTERBANK BENCHMARKS LAYER                           |
==================|=====================================================================
                  v
    [LPR]     [FDR/DR007]     [Shibor]     [FIX: CNY Parity]     [CIROR]     [DIBO]
      |           |              |                 |                |          |
======|===========|==============|=================|================|==========|======
|     |           |              |  [3] CORE MARKETS (ENGINES)      |          |     |
======|===========|==============|==================================|==========|======
      |           |              |                 |                |          |
      |           |              |       +---------v---------+      |          |
      |           |              |       |     FX MARKET     |      |          |
      |           |              |       |-------------------|      |          |
      |           |              |       | - Spot RMB        |<-----+          |
      |           |              |       | - G10 Pairs       |                 |
      |           |              |       | - Regional / BRI  |                 |
      |           |              |       +-------------------+                 |
      |           |              |       +-------------------+                 |
      |           |              |       |    MONEY MARKET   |                 |
      |           +--------------------->|-------------------|                 |
      |                          |       | - Pledged Repo    |                 |
      |                          |       | - Interbank Lend  |<----------------+
      |                          |       | - FCY Lending     |
      |                          |       +-------------------+
      |                          |       +-------------------+
      |                          |       |    BOND MARKET    |
      |                          |       |-------------------|
      |                          |       | - Cash Bond       |
      |                          |       | - Yield Curves    |
      |                          |       +---------+---------+
      |                          |                 |
======|==========================|=================|==================================
|     |                          |   [4] DERIVATIVES LAYER (RISK BUFFER)             |
======|==========================|====================================================
      |                          |                 |
      |      +-------------------v---+   +---------v---------+
      |      |   RATE DERIVATIVES    |   |   FX DERIVATIVES  |
      +----->|-----------------------|   |-------------------|
             | - IRS (Interest Swap) |   | - RMB/FX Forward  |
             | - FRA (Forward Rate)  |   | - RMB/FX Swap     |
             | - CRM (Credit Deriv)  |   | - FX Options      |
             +-----------------------+   +---------+---------+
                                                   |
===================================================|==================================
|                        [5] INFRASTRUCTURE LAYER (CLEARING)                         |
======================================================================================
                                                   |
                         +-------------------------v-------------------------+
                         |   [ SHCH (Netting) ]        [ CCDC (Bonds) ]      |
                         |                 \              /                  |
                         |                  v            v                   |
                         |                [ CIPS (Payments) ]                |
                         +-------------------------+-------------------------+
                                                   |
===================================================|==================================
|                         [6] TRANSMISSION TO REAL ECONOMY                           |
======================================================================================
                                                   |
                   +-------------------------------+-------------------------------+
                   v                               v                               v
         [ Loan Pricing ]                  [ Trade Finance ]             [ Capital Flows ]
      (SMEs, Corps, Mortgages)           (BRI Direct Settlement)             (FX Hedging)
```

### Systemic Interplay Logic
1. **The Pulse (Benchmarks):** PBoC injects liquidity (OMO/MLF) which anchors **DR007** and **LPR**. These benchmarks flow into CFETS as pricing inputs.
2. **The Engines (Trading):** Real-time trading in FX, Money, and Bonds occurs on CFETS platforms (ODM/Bilateral), generating the **Weighted Average Rates (WAR)** and **Real-time Yield Curves**.
3. **The Buffer (Derivatives):** Market participants use **IRS, Options, and Swaps** to manage the duration and volatility risks generated by the primary engines.
4. **The Foundation (Infrastructure):** **SHCH (Clearing)** and **CCDC (Depository)** provide the plumbing for DVP settlement, ensuring that policy transmission is not bottlenecked by counterparty or operational risk.
5. **The Output:** The final result is a market-driven interest rate and FX structure that determines the actual financing costs for SMEs, Green projects, and international trade.
6. 
## Related Mechanisms
- [[PBOC_Monetary_Policy_Transmission]] — The macro path of policy.
- [[PBOC_FX_Management_Framework]] — Strategies for RMB stability.
- [[PBOC_Collateral_Framework]] — Assets accepted in these operations.
- [[LPR_Loan_Prime_Rate_Reform]] — Evolution of the asset pricing anchor.
