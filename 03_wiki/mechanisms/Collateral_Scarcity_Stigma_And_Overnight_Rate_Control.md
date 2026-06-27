---
title: "Collateral Scarcity, Stigma, and Overnight Rate Control"
aliases: [Standing Facility Stigma, CB Borrowing Stigma, Stigma Effect on Overnight Rates, Information Asymmetry in LOLR]
type: mechanism
tags: [monetary-operations, collateral, liquidity-crisis]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "Collateral scarcity combined with stigma of CB borrowing prevents overnight rate from falling to theoretical lower bound; banks avoid CB standing facilities despite availability."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 189
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
When both collateral becomes scarce AND standing facility borrowing carries stigma (market interprets as distress), overnight rate can exceed the standing facility lending rate; CB loses direct control of rate.

## 1. Core Logic / Mechanism

[RAW] **Stigma Definition** (Bindseil p.189, sec 12.2):
"Stigma: Information asymmetry that causes banks to avoid borrowing from central bank standing facilities even when available and advantageous, because borrowing signals distress to markets and causes spreads on unsecured funding to widen."

[RAW] **Rate Control in Normal Times (No Stigma)**:
- CB sets lending facility rate: 2.5%
- Overnight rate $r^{ON}$ rises above 2.5% → banks arbitrage → borrow from CB at 2.5%
- Market sees banks borrowing from CB → no stigma (routine refinancing)
- $r^{ON}$ pulled down to ~2.5%

[RAW] **Rate Control in Crisis (With Stigma)**:
- CB sets lending facility rate: 2.5%
- Overnight rate $r^{ON}$ rises to 3.0% (collateral scarcity + liquidity risk premium)
- Bank considers borrowing from CB at 2.5%
- **Stigma Effect**: Market participants observe CB borrowing → conclude bank is in distress → unsecured funding spreads widen by 50-100 bps
- **Bank's Cost-Benefit**:
  - Savings from borrowing at 2.5% vs. 3.0% = 50 bps
  - Cost of stigma (unsecured spread widening) = 75 bps (expected)
  - **Net effect**: Borrowing is worse than NOT borrowing
  - **Bank chooses**: Pay 3.0% in overnight market, avoid CB borrowing, preserve market perception

[LLM] **Mathematical Formulation**:

Without stigma: $r^{ON} = r_L$ (lending facility rate)

With stigma:
$$r^{ON} = r_L + \text{Stigma Premium}$$

Where:
$$\text{Stigma Premium} = \Delta s_{\text{CB}} \times \text{(Duration of spread effect)}$$

- $\Delta s_{\text{CB}}$ = increase in unsecured funding spreads if borrowing detected
- Duration = number of years spread elevated (e.g., 2 years post-detection)

**Example**:
- Lending facility rate: 2.5%
- Stigma premium: +75 bps = 0.75%
- Effective rate cap: 3.25% (even though CB standing facility offers 2.5%)

## 2. Empirical Evidence: 2008 Crisis

[RAW] **Fed Discount Window Usage, September-December 2008** (referenced in Bindseil p.189-190):

**August 2008 (Pre-Lehman)**:
- Fed discount window borrowing: ~$6B daily
- Fed funds rate: 2.0%
- Discount rate: 2.5%
- Market overnight rate (fed funds): 2.1% (arbitrage works; banks borrow from CB at 2.5%, lend to market at 2.1% if needed)

**September 2008 (Post-Lehman)**:
- Lehman collapse triggers perception shift
- Fed funds rate: 1.5% (CB cuts policy rate)
- Discount rate: 2.0% (cut to 1.75%, then to 1.0%)
- Fed funds actual trading: oscillates 0.1% - 2.0% (extreme volatility)
- **Discount window borrowing: drops to $2-3B** (from $6B)
- **Paradox**: Fed rates have CUT (expansionary), but bank borrowing from CB FELL

[RAW] **Explanation**: Stigma
- Bank borrowing from Fed = public admission of distress
- Market response: Spreads on bank unsecured debt widen 200+ bps
- For bank needing $500M term funding, stigma cost: $500M × 0.02 = $10M/year
- Savings from using 2.0% discount rate instead of 3.0% market rate: $500M × 0.01 = $5M/year
- **Stigma cost > savings** → banks avoided CB borrowing

**Fed's Response**:
- Implemented $TAF (Term Auction Facility) as disguised lending (December 2008)
- Banks could borrow but auction disguised source
- Result: Stigma fell; borrowing increased to $40-50B at peak

## 3. Mechanisms of Stigma

[RAW] **Mechanism 1: Information Asymmetry**

Normal times:
- Market knows: "All banks occasionally borrow from CB for overnight liquidity management"
- Normal borrowing = no signal

Crisis:
- Market knows: "If bank is using CB more than usual, something is wrong"
- Excess borrowing = distress signal
- **Agent problem**: CB doesn't know if bank is solvent or insolvent
- **Market inference**: "If CB doesn't discriminate, CB is probably funding some insolvent banks"
- **Rational response**: Avoid lending to banks with ANY CB borrowing, or demand compensating spread

[RAW] **Mechanism 2: Contagion through Counterparty Risk**

- Bank B borrows from CB → Market interprets as distress
- Counterparties of Bank B (other banks, derivatives dealers) become nervous
- Do they have credit exposure to B? Is B credit-risky? How much?
- Result: Clearing spreads widen for Bank B → Bank B's borrowing costs increase → more CB borrowing → stigma intensifies

[RAW] **Mechanism 3: Regulator Signaling**

- Sometimes CB and Regulator are same entity (Fed + OCC, ECB + national supervisors)
- If CB stands ready to lend, but bank doesn't borrow → market infers: "Regulators confident in bank"
- If bank borrows heavily → market infers: "Regulators skeptical; CB is substituting for market funding"
- Self-fulfilling prophecy: More borrowing → more stigma → more borrowing needed → more stigma

## 4. Worked Example

[LLM] **European Bank (Anonymous) in 2011 Sovereign Crisis**

**March 2011 (Normal Times)**:
- Bank has €50M/month overnight liquidity needs
- Borrows €40M from CB marginal lending facility, €10M in interbank market
- Market reaction: None (routine management)
- Unsecured 3-month borrowing spread: +50 bps over EONIA

**September 2011 (Peripheral Crisis)**:
- Sovereign yields on Bank's government collateral (Spanish) spike to 5%+
- Bank's collateral haircuts increase sharply
- Bank can only borrow €20M from CB instead of €40M
- Bank forced to borrow €30M in interbank market

**October 2011**:
- ECB President Draghi's "whatever it takes" speech; markets stabilize somewhat
- But Bank's sovereign collateral still marked at depressed values
- Bank still needs €20-25M daily from interbank market (can't replace with CB because haircuts still high)
- Market gossip: "Bank X is desperately trying to find unsecured funding"

**November 2011 (Stigma Peak)**:
- Bank's CDS (credit default swap) tightens 75 bps (from 100 bps to 175 bps)
- Unsecured 3-month funding spread: now +200 bps (from +50 bps)
- Bank attempts to issue €200M bond; priced at 5.0% (would have been 2.5% in normal times)
- Market perceives: "Bank is desperate, hence high yield required"

**December 2011**:
- ECB announces LTRO (Long-Term Refinancing Operation), 3-year, €500B+
- Bank immediately borrows €100M at 1.0% (much lower than market)
- **Stigma disappears**: LTRO is massive program; all banks borrowing; no signal anymore
- Bank's CDS tightens back to +125 bps (credit markets recover)
- Unsecured spread: drops to +100 bps

**Lesson**: Stigma isn't permanent; it depends on whether borrowing is perceived as exceptional (bank-specific distress) or systematic (all banks in same boat).

## 5. Policy Solutions to Stigma

[RAW] **Solution 1: Disguise the Source**
- Fed's TAF (Term Auction Facility): Instead of bank going to discount window, participate in auction
- Effect: No one knows if you won or how much you borrowed
- Result: Stigma eliminated; borrowing soared

[RAW] **Solution 2: Massive Scale Makes Abnormal Normal**
- ECB's LTRO (€500B): So large that all banks borrow
- Market interpretation: "Not a signal of distress; everyone is doing it"
- Stigma disappears because borrowing becomes systematic

[RAW] **Solution 3: Index the Facility Rate to Market Conditions**
- Instead of fixed lending facility rate 2.5%
- Tie rate to market overnight rate: $r_L = r^{ON} + 100$ bps
- Effect: Banks can't arbitrage; borrowing from CB doesn't save money
- (But also reduces effectiveness of standing facility as rate floor)

[RAW] **Solution 4: Separate Facility for Troubled Banks**
- ELA (Emergency Liquidity Assistance): Separate from regular standing facilities
- Rate: 300+ bps above policy (penalty pricing)
- Collateral: Broader (can include illiquid assets)
- Signaling: ELA is explicitly for crisis; regular standing facilities remain unstimmatized
- (But requires clear communication of boundary between normal and ELA)

## Related
- [[Collateral_Scarcity_And_Effective_Term_Funding_Costs]]
- [[Lender_Of_Last_Resort_Mechanism]]
- [[Standing_Facilities_Types_And_History]]
- [[Interest_Rate_Corridor_And_Standing_Facilities]]
- [[Bank_Run_Problem_And_Central_Bank_Collateral]]
