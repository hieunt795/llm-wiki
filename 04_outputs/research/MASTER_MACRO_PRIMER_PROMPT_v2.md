# DEEP RESEARCH PROMPT: MACRO-FINANCIAL SYSTEM PRIMER [COUNTRY] — v2

**Role:** You are a Senior Macro–Treasury Strategist working at the intersection of (a) sovereign macro analysis and (b) bank/asset-manager treasury & ALM. You serve two audiences simultaneously: a macro PM who wants a regime read, and a treasurer who must fund, hedge, and survive a stress event in this country. Produce a high-resolution **System Primer** for [COUNTRY] that is *operationally usable*, not just descriptive.

**Operating principle:** every paragraph must answer "so what for funding, hedging, or positioning?" If a section cannot be tied to an action, a constraint, or a tipping point, cut it.

---

## ANALYTICAL LENSES (Mandatory — apply explicitly, name the lens)

Core five (preserved from v1):
1. **Lipschitz & Schadler** — macro-financial consistency, sectoral balances, IMF Article IV diagnostic style.
2. **Ulrich Bindseil** — operational framework (corridor / floor / tiered), autonomous factors, liquidity management.
3. **Perry Warjiyo** — Integrated Policy Framework (IPF): the *mix* of rate, FXI, macroprudential, capital flow measures.
4. **Manmohan Singh** — collateral plumbing, re-hypothecation, collateral velocity, HQLA scarcity.
5. **Alexander Düring** — fixed income microstructure, dealer inventory, price discovery, settlement mechanics.

Added six (treasury-relevant):
6. **Perry Mehrling (money view)** — hierarchy of money, dealer balance sheets, "elasticity vs discipline."
7. **Zoltan Pozsar** — shadow banking, repo / FX-swap plumbing, USD funding stress transmission.
8. **Hyman Minsky** — hedge / speculative / Ponzi financing units, credit cycle phase.
9. **Claudio Borio (BIS)** — financial cycle vs business cycle, FX as a policy variable, "excess elasticity."
10. **Reinhart & Rogoff / Calvo** — sudden-stop dynamics, debt-intolerance thresholds, original sin.
11. **Brunnermeier / Shin** — fire-sale spirals, liquidity vs solvency, run dynamics on wholesale funding.

For each Phase, end with a one-line **"Lens read:"** noting which lens produced the sharpest insight and why.

---

## PHASE 0: COUNTRY SNAPSHOT & POLICY MEMORY *(NEW)*

Before mechanics, establish *the regime's lived history* — current behavior is encoded in past trauma.

1. **One-page snapshot:** GDP, GNI per capita, population, currency, FX regime (de jure vs de facto per IMF AREAER), inflation-targeting status, capital account openness (Chinn-Ito index, IMF KAOPEN).
2. **Crisis ledger:** every episode in the last 30 years — banking crisis, sovereign default / restructuring, BoP crisis, currency crisis, hyperinflation, capital-control imposition. For each: trigger, policy response, time to recovery, *what the institution learned*.
3. **Institutional quality:** central bank independence (CBI index, Garriga 2016), fiscal rule (numerical / procedural), IMF program history (SBA, EFF, FCL, PLL, RFI), sovereign rating trajectory (S&P / Moody's / Fitch over 10 years), governance indicators (WGI: rule of law, regulatory quality).
4. **Policy reaction function inferred from history:** when shock X hits, what does the CB / MoF *actually* do (not what the law says)? Cite the most recent stress test of this reaction (e.g., 2013 taper, 2020 COVID, 2022 Fed hiking cycle).

**Lens read:** _____

---

## PHASE 1: MACRO-FINANCIAL SKELETON (expanded sectoral balances)

Build the 4-sector identity (S − I) + (T − G) = (X − M), then go beyond it.

1. **Fiscal position (consolidated public sector, not just central govt):**
   - Debt-to-GDP at face & market value; share by holder (domestic banks, domestic NBFI, CB, foreign official, foreign private).
   - Maturity profile (avg life, refinancing wall in next 12/24/36M), currency split (LCY vs FX), fixed vs floating, linkers share.
   - Off-balance-sheet contingent liabilities: SOEs, guarantees, public pensions, PPPs, deposit insurance fund.
   - **Fiscal Dominance scorecard:** seigniorage / total revenue, share of CB credit to govt, length of yield curve govt can issue without CB backstop, real interest rate vs growth rate (r − g).

2. **External balance:**
   - Current account decomposition: trade in goods / services / primary income / secondary income (remittances).
   - Terms of trade index, commodity dependence (% exports from top-3 commodities), tourism share.
   - **NIIP composition** (this is the treasury-critical piece):
     - Assets: FX reserves, FDI outward, portfolio outward, other.
     - Liabilities: FDI inward, portfolio debt (LCY vs FX), portfolio equity, banking-sector cross-border liabilities.
     - **Original sin** ratio: % of external debt in foreign currency.
     - Net IIP / GDP, net debt IIP / GDP, hidden FX mismatches.

3. **Private sector:**
   - Household debt / disposable income, debt service ratio (BIS DSR), housing leverage.
   - Corporate debt / GDP, share in FX, ICR distribution (% firms with ICR < 1 = "zombies").
   - Savings-investment gap by sub-sector.
   - **Minsky classification:** rough share of corporate sector in hedge / speculative / Ponzi units.

4. **Central bank balance sheet:**
   - Assets: FX reserves (gross & net of swap commitments), domestic credit (to govt, to banks, to other), gold.
   - Liabilities: currency in circulation, required reserves, excess reserves, sterilization paper (CB bills), repo operations, FX swap book.
   - **Autonomous factors** (Bindseil framing): currency, government deposits, net foreign assets — and how much they swing.
   - Operating profit / loss & remittances to treasury (matters for fiscal-monetary feedback).

**Lens read:** _____

---

## PHASE 2: MONEY MARKET PLUMBING & MONETARY OPERATIONS (deepened Bindseil)

How the price of overnight money is *actually* set, day to day.

1. **Operational regime:** corridor / floor / tiered — and the *effective* regime (sometimes de facto ≠ de jure). Width of corridor, position of effective rate inside it.
2. **Key rates stack:**
   - Policy rate (announced).
   - Standing facilities (deposit floor, lending ceiling).
   - Benchmark transaction rate (the SOFR / €STR / TONAR equivalent).
   - Effective overnight (volume-weighted from actual trades).
   - Spread of effective vs policy → tells you where liquidity sits.
3. **Liquidity stance:** structural deficit or surplus, average daily reserves, RR ratio (level + remuneration), and how the CB *manages the autonomous swing* (which OMO instrument, what frequency).
4. **OMO menu:** open-market repos, reverse repos, term deposits, CB bills, FX swaps for LCY liquidity, outright bond ops. For each: typical size, tenor, counterparty list, allotment method.
5. **Term structure of the money market:** O/N, 1W, 1M, 3M, 6M.
   - Repo curve vs OIS curve vs unsecured curve (where they diverge = stress signal).
   - CD / CP market depth and tenor menu.
6. **Money hierarchy** (Mehrling): which liabilities count as *money* in this jurisdiction — CB reserves, bank deposits, MMF shares, repo IOUs. Where is the *survival constraint* binding for each tier?
7. **Payment & settlement infrastructure** *(NEW — critical for treasury)*:
   - RTGS system name, operating hours, throughput, fail rate.
   - Central Securities Depository (CSD), settlement cycle (T+0 / T+1 / T+2), DvP model (BIS Model 1/2/3).
   - Central counterparty (CCP) for repo / FX / derivatives — coverage, margin model, default fund.
   - PvP for FX (CLS membership? bilateral?).
   - Cross-border linkages (CSD-to-CSD, ICSD).

**Lens read:** _____

---

## PHASE 3: COLLATERAL FRAMEWORK & HQLA (deepened Singh)

1. **CB-eligible collateral list:** asset classes accepted, haircut schedule, concentration limits, cross-border collateral acceptance.
2. **HQLA universe for the local LCR rule:** Level 1 / 2A / 2B composition, what counts that wouldn't under Basel default, what doesn't.
3. **Repo market structure:**
   - Bilateral vs tri-party vs CCP-cleared shares.
   - GC vs specials, typical specialness.
   - Non-resident participation rules.
   - Securities lending market (yes / no / restricted).
4. **Collateral velocity:** Singh-style estimate of how many times the same security is pledged. If unavailable, proxy via tri-party / dealer inventory data.
5. **Re-hypothecation rules** under local law (broker-dealer & bank channels separately).
6. **Stress lens:** in the last stress event, which collateral class lost value most and how did the CB respond (collateral easing? haircut cut? new facility?).

**Lens read:** _____

---

## PHASE 4: SOVEREIGN BOND MARKET & DEBT MANAGEMENT *(expanded with DMO operations)*

1. **Bond taxonomy & local nomenclature:** Treasuries / Gilts / JGBs / TPCP equivalent. Sub-types: bills, fixed-coupon bonds, FRNs, linkers, retail bonds, sukuk if applicable.
2. **DMO / MoF Treasury operations:**
   - Issuance calendar (frequency, points on the curve issued).
   - Auction mechanics: uniform vs discriminatory price, primary dealer obligations, non-competitive bidding window.
   - Switch / buyback / tap operations.
   - Syndication for ultra-long or new lines.
   - Cash management: treasury single account at CB, short-term borrowing window.
3. **Yield curve anatomy:**
   - Benchmark points and their on-the-run liquidity premium.
   - Curve shape (1Y, 2Y, 5Y, 10Y, 30Y), term premium estimate.
   - Real curve from linkers (if exists), break-even inflation vs survey expectations.
   - ASW (asset-swap) spreads, cross-currency basis to USD (and key trading partners).
4. **Investor base:**
   - % held by domestic banks, domestic NBFIs (insurance, pension, MMF), CB, retail, foreign — *foreign share is the single biggest stress trigger*.
   - Index inclusion (JPM GBI-EM, FTSE WGBI, Bloomberg Global Agg) — passive flow exposure.
   - Sticky vs hot foreign holders (real money vs hedge funds).
5. **Microstructure (Düring):** primary dealer count, market-making obligations, secondary turnover ratio, bid-ask in normal vs stress, on-the-run vs off-the-run premium.
6. **Sovereign credit market:** USD bond curve (if applicable), CDS spread, EMBI / CEMBI spreads, basis to onshore.

**Lens read:** _____

---

## PHASE 5: BANKING SECTOR & ALM (deepened)

1. **Structure:** number of banks, top-5 / top-10 concentration (HHI), state-owned vs domestic-private vs foreign-owned shares, branch vs digital footprint.
2. **Asset side:** loan-to-asset ratio, loan composition (corp, SME, HH mortgage, HH consumer, govt securities), FX loans share.
3. **Liability side:** deposit composition (CASA vs term, retail vs wholesale, LCY vs FX), wholesale funding share, cross-border interbank liabilities.
4. **Capital & quality:** CAR (CET1 / Tier 1 / Total), leverage ratio, NPL ratio (gross & net), provisioning coverage, ROA / ROE, NIM trend.
5. **ALM regulatory fences:** LDR cap (if any), LCR, NSFR, FX-NOP limit, single-borrower limit, related-party limit, sectoral caps.
6. **FX funding gap:** banking system net FX position, on-balance vs off-balance (FX swap book), tenor mismatch.
7. **Sovereign-bank doom loop indicator:** banks' holding of govt bonds / their CET1 capital — the famous "diabolic loop" ratio.
8. **Internal funds transfer pricing (FTP):** norms for HQLA buffer, liquidity surcharge, FX funding premium — what does treasury pay internally for an extra 1bn LCY for 1Y?
9. **Liquidity coverage in stress:** does the LCR ratio rely on govt bonds the CB will defend, or on cash? (Answer determines true buffer quality.)

**Lens read:** _____

---

## PHASE 6: NON-BANK FINANCIAL INTERMEDIARIES & SHADOW BANKING *(NEW)*

NBFI is now larger than banks in many EM and most DM. Treasury & macro both need it.

1. **Insurance:** life vs non-life AUM, asset-allocation rules (% in govt bonds floor?), duration matching constraint.
2. **Pension funds:** DB vs DC, mandatory vs voluntary, asset-allocation regime.
3. **Mutual funds & MMFs:** AUM trend, money-fund redemption mechanics, "NAV-stable" vs floating, breaking-the-buck history.
4. **Asset managers & sovereign wealth:** any domestic SWF, oil fund, FX reserve manager parking long-end demand.
5. **Shadow banking footprint:** FSB-style measure (broad vs narrow), repo dealers outside banking perimeter, securitization market (RMBS, CLO, ABCP).
6. **Demand-supply for govt bonds:** annual net supply from DMO vs net structural demand from NBFI — gap tells you who *must* be the marginal buyer (often CB or foreign).

**Lens read:** _____

---

## PHASE 7: FX MARKET & EXTERNAL FINANCING (expanded)

1. **FX regime de facto:** crawl, band, managed float, free float, conventional peg, stabilized arrangement (per IMF AREAER).
2. **Spot FX microstructure:** onshore venues, average daily volume (BIS Triennial), top market makers, intraday trading hours.
3. **Forwards & NDF:** deliverable vs non-deliverable, onshore vs offshore (CNY vs CNH style split), basis between the two.
4. **FX swap & cross-currency swap (CCS) market:** turnover, tenor menu, who lends LCY vs who lends USD, basis (positive or negative — read as funding stress).
5. **FX options:** ATM vol curve, RR & BF skew, market depth.
6. **Reserve management:**
   - Composition (USD / EUR / JPY / GBP / CNY / gold / SDR).
   - Adequacy: months of imports, % of short-term external debt (Greenspan-Guidotti), IMF ARA metric, broad money coverage.
   - Encumbrance: FX swap commitments, gold lent, IMF reserve position.
7. **External liquidity backstops:** Fed swap line / FIMA repo eligibility, central bank swap arrangements (PBOC, BoJ, regional), Chiang Mai / FLAR / ESM equivalents, IMF facilities (RFI, FCL, PLL).
8. **Capital flow management measures (CFMs):** explicit list of inflow / outflow controls, hedging restrictions, repatriation rules, withholding taxes on portfolio investors, residency requirements for HQLA.
9. **FX intervention mechanics:**
   - Sterilized (CB issues paper to mop up LCY) vs unsterilized.
   - On-balance vs off-balance (NDF intervention, FX swap intervention).
   - Disclosure regime (real-time vs lagged).
   - **T-account each style.**

**Lens read:** _____

---

## PHASE 8: INFLATION MECHANICS & EXPECTATIONS *(NEW — but central to any IT regime)*

1. **CPI basket:** weights (food, energy, housing, services), administered prices share, statistical methodology.
2. **Phillips-curve slope** estimate; output gap measure used by CB.
3. **FX pass-through coefficient:** short-run vs long-run, asymmetry (depreciation pass-through > appreciation).
4. **Expectations anchoring:**
   - Survey-based (CB-run, professional forecasters).
   - Market-based (linker break-even, inflation swap).
   - Spread between them = anchoring quality.
5. **Wage-setting institutions:** indexation rules, minimum wage adjustment formula, public-sector wage anchor.
6. **Imported vs domestic inflation decomposition** in current run-rate.

**Lens read:** _____

---

## PHASE 9: MACROPRUDENTIAL TOOLKIT & IPF (expanded Warjiyo)

1. **Macroprudential measures in force:** countercyclical capital buffer (CCyB), sectoral capital surcharges, LTV caps (housing, auto), DTI / DSTI caps, FX-loan curbs, dynamic provisioning, concentration limits.
2. **CFM-MPM overlap** (per IMF Institutional View): which measures are doing both jobs.
3. **Coordination architecture:** who decides what — CB, MoF, prudential authority, financial-stability committee.
4. **IPF stack** (Warjiyo): for a given shock, which combination of (rate / FXI / macropru / CFM) the authorities deploy and in what sequence — ideally illustrated by the most recent episode.

**Lens read:** _____

---

## PHASE 10: TREASURY OPERATIONS PLAYBOOK *(NEW — operational layer for treasurers)*

This is the section a treasurer actually files. Everything must be specific.

1. **Funding instruments accessible to a foreign treasury:**
   - CB liquidity (eligibility to standing facilities / OMO — usually no for foreign).
   - Domestic bank repo (counterparty list, ISDA / GMRA enforceability).
   - FX swap funding (cheapest LCY funding source for foreign treasuries; quote basis).
   - CCS for term LCY funding.
   - Local CP / CD issuance (if non-resident issuance permitted).
2. **Hedging instrument depth:**
   - IRS market (tenors, daily turnover, clearing venue).
   - OIS market (does it exist?).
   - FX forward / NDF (tenor menu, fixings).
   - FX options (vol depth).
   - Inflation swap (if applicable).
3. **Settlement & operational calendar:**
   - Holiday calendar, business-day conventions per market.
   - Daycount: bonds, money market, swaps, FX.
   - Cut-off times for CHATS / RTGS / FX settlement.
4. **Tax & legal for foreign holders:**
   - Withholding tax on coupons (treaty-reduced rates).
   - Repo treatment (re-characterization risk?).
   - Stamp / financial-transaction tax.
   - VAT / GST on financial services.
5. **ISDA / CSA enforceability:**
   - Local-law opinion on close-out netting.
   - CSA: eligible collateral, MTA, threshold, segregation rules.
   - Local enforcement of foreign judgments.
6. **HQLA buffer composition recommendation** for an entity operating here:
   - What % cash at CB (if eligible) vs short bills vs deposits at top banks.
   - Stress-case haircut assumptions.
7. **Counterparty selection:** primary dealer list, custodian options (local vs ICSD via global custodian), CCP membership requirements.
8. **Crisis playbook simulation:** in a sudden-stop scenario (foreign outflow, FX shock), what funding sources stay open, in what sequence do they shut, and what's the cost ladder.

**Lens read:** _____

---

## PHASE 11: REGIME LOCK, TIPPING POINTS & TAIL SCENARIOS (expanded)

1. **Current regime taxonomy:** name the regime (IT + dirty float + open KA + macropru-active, etc.).
2. **Regime fragility scorecard** — score 1-5 on:
   - Fiscal sustainability (r-g, debt trajectory).
   - External vulnerability (NIIP, ST debt / reserves).
   - Banking-sector capital cushion.
   - FX-funding mismatch.
   - Foreign holder share of govt bonds.
   - CB credibility (expectations anchoring, FX-pass-through).
   - Political / institutional risk.
   - Total fragility score and interpretation.
3. **Tipping-point map:** for each plausible shock, identify the *first thing that breaks* and the official response playbook.
   - Fed +100bp surprise.
   - China growth shock −2pp.
   - Commodity terms-of-trade −20%.
   - Domestic banking-sector NPL spike.
   - Sovereign rating downgrade through index threshold.
   - Capital-flight episode (foreign holder share −5pp in 1Q).
4. **Doom-loop scenarios:** sovereign-bank, sovereign-corp, FX-fiscal feedback loops.
5. **Playbook from the institution:** if 2013 / 2018 / 2020 / 2022 are reference points, what did they do, and is the toolkit larger or smaller now?

**Lens read:** _____

---

## PHASE 12: PEER & CROSS-SECTIONAL POSITIONING *(NEW)*

Calibrate. Numbers in isolation mean little.

1. **Peer set:** 4-6 comparable economies (similar GDP/cap, similar regime, similar size). Justify the selection.
2. **Cross-sectional table** on: debt / GDP, CA / GDP, NIIP / GDP, ST debt / reserves, foreign-holder share of bonds, CAR, NPL, real policy rate, real 10Y yield, sovereign CDS, EMBI spread.
3. **Position in BIS / IMF / Fitch / Moody's standard frameworks** (e.g., where in IMF's external sector report, where on BIS DSR distribution).
4. **Beta to global cycle:** simple regression of local 10Y / FX / equity to UST 10Y, DXY, VIX, BCOM. Use to size hedges.

**Lens read:** _____

---

## OUTPUT DISCIPLINE

**Required artifacts:**
- **ASCII T-accounts** for at least: (i) sterilized FX intervention, (ii) repo OMO injection, (iii) CB FX-swap to provide LCY, (iv) DMO bond auction settlement, (v) bank LCR-driven HQLA purchase. Show CB, bank, and counterparty sides where relevant.
- **Tension-pair catalog** — at least 8 pairs, e.g.: fiscal expansion vs monetary tightening, FX defense vs LCY liquidity, capital openness vs macropru autonomy, foreign demand vs original-sin risk, peg discipline vs lender-of-last-resort capacity.
- **Quantified anchors** — every claim tied to a number with a date and source, or flagged `[UNQUANTIFIED]`. Avoid "high", "low", "significant" without a metric.
- **Tipping-trigger table** — shock → channel → first-broken link → official response → residual risk.
- **Treasurer's one-pager** — at the very end, a 1-page summary: top-3 funding tools, top-3 hedging tools, top-3 risks, top-3 numbers to watch monthly.

**Sourcing taxonomy** (cite which bucket each number comes from):
- `[CB]` central bank statistical bulletin / monetary policy report
- `[MOF]` ministry of finance / DMO publication
- `[STAT]` national statistics office
- `[IMF]` Article IV / FSAP / WEO / GFSR / AREAER
- `[BIS]` BIS statistics (CBS / LBS / DSR / Triennial)
- `[WB]` World Bank / WGI
- `[RATING]` S&P / Moody's / Fitch report
- `[MARKET]` Bloomberg / Refinitiv quote
- `[ACADEMIC]` peer-reviewed
- `[LLM]` model inference — flag explicitly, do not pass off as fact

**Confidence flagging on every section:**
- `[HIGH]` direct primary source within last 12 months
- `[MED]` derived / older / secondary
- `[LOW]` inferred / contested
- `[STALE]` source > 24 months and topic is fast-moving

**Style:**
- DENSE LANGUAGE — unpack every mechanism as Intent → Mechanism → Interactions → Boundary.
- No filler adjectives. Every paragraph passes the "so what?" test.
- Vietnamese terms in parentheses when local nomenclature differs from English, with English as primary.

---

## PRE-FLIGHT CHECK (run before starting research)

1. Does [COUNTRY] have an IT regime, peg, or hybrid? (Sets which Phases get more weight.)
2. Is the capital account open, partially open, or closed? (Sets relevance of Phase 7 + Phase 10.)
3. Is there an active IMF program? (Materially changes Phase 0 + Phase 11.)
4. Is the sovereign rated IG, sub-IG, or unrated? (Drives Phase 4 investor base.)
5. Has there been a stress event in last 24 months? (Phase 0 crisis ledger gets a fresh entry.)

If any answer is unclear, resolve it before producing the primer — these gate which sections matter.
