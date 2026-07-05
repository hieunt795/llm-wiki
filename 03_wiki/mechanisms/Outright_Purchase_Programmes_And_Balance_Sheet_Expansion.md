---
title: "Outright Purchase Programmes and Balance Sheet Expansion"
aliases: [Quantitative Easing, QE, Outright Asset Purchases, Large-Scale Asset Purchases, LSAP, Balance Sheet Policy]
type: mechanism
tags: [monetary-operations, quantitative-easing, unconventional-policy]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "Outright purchase programmes expand central bank balance sheet; they differ from credit operations (repos) in that CB retains assets permanently, creating monetary base expansion and signaling commitment to sustained accommodation."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 219
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Outright asset purchases (QE) expand the monetary base permanently; they serve both balance sheet effects (increase system liquidity) and signaling effects (communicate extended accommodation when policy rates at zero lower bound).

## 1. Core Logic / Mechanism

[RAW] **Definition & Distinction** (Bindseil p.219, sec 13.3):
"Outright Purchase Programmes" = Central bank purchases financial assets (bonds, securities, equities) and retains them as permanent assets, financed by issuing banknotes or reserves.

**Key Distinction from Repos**:
- **Repo**: Temporary exchange; CB lends cash against collateral; bank retains ownership; CB must return securities after term
- **Outright**: Permanent purchase; CB retains ownership; bank receives permanent cash injection

[LLM] **Balance Sheet Mechanics**:

**Before QE**:
```
Central Bank                    Banking System
Assets:         Liabilities:    Assets:           Liabilities:
Discount Loans (100)  Banknotes (100)    Securities (100)      Deposits (90)
Repos (50)            Reserves (50)      Loans (200)           CB Reserve Bal (60)
Total (150)           Total (150)        Total (300)           Total (150)
```

**After €50M Outright Bond Purchase**:
```
Central Bank                    Banking System
Assets:                Liabilities:    Assets:           Liabilities:
Discount Loans (100)   Banknotes (100)    Securities (50)       Deposits (140)
Repos (50)             Reserves (100)     Loans (200)           CB Reserve Bal (60)
Securities (50)        [NEW]              [Bonds Sold (50)]
Total (200)            Total (200)        Total (300)           Total (200)
```

**Key Effect**: 
- CB balance sheet expands: €150M → €200M
- System reserves injected: €50M (appears as bank deposits at CB)
- Banks hold only €50M securities (not €100M); have €50M cash buffer

[RAW] **Money Creation Mechanism** (Bindseil p.219-220):
Banks sell securities to CB; receive cash (banknotes or reserve deposits).
- If banks hold excess cash → deposit in deposit facility at policy rate
- If banks hold excess cash → invest in other assets (stocks, foreign bonds, real estate)
- Either way: monetary base has expanded; M3 (broad money) increases

**Transmission Channels**:
1. **Portfolio Rebalancing**: Reduction in securities supply → demand for alternative assets rises → portfolio prices increase → wealth effect on consumption
2. **Signaling**: Large QE program signals commitment to low rates for extended period → expectations of future rates fall → current long-term rates fall
3. **Liquidity Injection**: Immediate increase in reserves → supports bank lending capacity → credit supply increases

## 2. Worked Example

[LLM] **ECB Securities Markets Programme (SMP) 2010-2011**

**Context**: Sovereign debt crisis; government bond yields spiking (Greece, Ireland, Portugal)

**May 2010 - August 2011: SMP Program**
- ECB committed: €210 billion outright purchases of government and agency bonds
- Monthly pace: €1-2 billion / week
- Focus: Portuguese, Irish, Greek, Spanish government bonds (most distressed yields)

**Transmission Path**:

**Week 1**: 
- ECB announces €100M purchase of Portuguese 10-year bonds
- Market: Expected yield = 3.5%, offered at 3.8%
- ECB buys at offered price (3.8%)
- **Immediate effect**: Price floor established; dealers willing to mark positions closer to ECB bid price

**Week 2-4**:
- Repeated ECB purchases establish clear floor
- Portfolio managers: "No more yield compression downside risk"
- Real money investors (pension funds, insurers): "Portuguese bonds @ 3.5% now reasonable"
- **Result**: Natural demand returns; ECB purchases needed less frequently

**End August 2011** (program peak):
- ECB total purchases: €210 billion
- System reserves injected: ~€200 billion
- Portuguese 10-year yield: Fell from 5.8% (pre-SMP) to 4.2% (end SMP)
- Irish, Spanish yields similarly stabilized
- **ECB balance sheet**: Expanded from €1.9T to €2.2T

[LLM] **Counterfactual (No SMP)**:
- Portuguese yields likely continued upward; reached 8-10% (level of late 2011 periphery crisis)
- Bank deleveraging accelerated (banks couldn't fund at such yields)
- Credit supply collapsed
- Recession deepened beyond observed 2012 contraction

## 3. Failure Conditions / Boundaries

[RAW] **"Dangers of Too Accommodating Policies"** (Bindseil p.228, sec 13.4):

1. **Moral Hazard**: Large-scale QE signals "CB will always step in" → incentivizes excessive private risk-taking
   - Banks make longer-dated loans without proper risk premium
   - Investors reach for yield; buy riskier assets at lower spreads
   - Eventually: asset bubbles form in equities, real estate, emerging markets

2. **Asset Bubble Formation**: With policy rates at zero and QE ongoing
   - Excess liquidity seeks return
   - Competition for yield-bearing assets → prices spiral
   - Bubbles in equities (2013), emerging markets (2014), credit (2016-2019)

3. **Inflation Overshoot Risk**: Extended QE → monetary base explosion
   - If velocity (M × V = P × Y) normalizes, inflation can surge
   - Central bank credibility at risk
   - Example: 2021-2022 post-pandemic inflation surge (partly attributable to 2020 QE overhang)

4. **Financial Stability Distortions**: 
   - Yield compression creates "TINA" (There Is No Alternative) mindset
   - Structured products, credit derivatives proliferate
   - When correction comes, feedback loops amplify losses

5. **Exit Problem**: 
   - Large QE position on CB balance sheet means large portfolio loss if rates rise
   - Fed 2022: QE portfolio marked significant losses as rates rose
   - Creates political pressure on CB independence ("Why is your balance sheet underwater?")

6. **Effectiveness Decline**: 
   - First €100B QE purchases have multiplied impact on yields
   - Marginal €100B in 5th year of QE has minimal impact (expectations already anchored)
   - Bindseil: "Diminishing returns to successive rounds of QE"

## 4. When Outright Purchases Dominate

[RAW] **Fed 2007-2015 Example** (referenced by Bindseil):
- Pre-2007: Fed balance sheet ~€800B; mostly short-term operations
- Post-2008 peak: €2.3T; mostly long-term securities (MBS, Treasuries)
- **Duration**: MBS 5-7 year average; Treasuries 5-10 year average
- **Effect**: CB became largest holder of long-term securities; set duration curve from inside the market

## 5. Policy Alternatives to QE

[RAW] **Bindseil Framework** (p.220-230):
If policy rates at zero and accommodation needed, alternatives:
1. **Negative Rates**: Cut policy rate below zero (NIRP); penalize reserves
2. **Forward Guidance**: Commitment to keep rates low → moves expectation
3. **Credit Lending**: Targeted loans to specific sectors (banks, SMEs, infrastructure)
4. **FX Intervention**: Depreciate currency → boost exports
5. **Fiscal Policy**: Government spending (outside CB remit but complementary)

**Ranking**: By effectiveness in non-crisis (normal) regime
1. Forward guidance + negative rates (least distortive)
2. Credit lending targeted (preserves market function)
3. Broad QE (large balance sheet risk)
4. FX intervention (may trigger retaliation)

## Related
- [[Quantitative_Easing_And_Zero_Lower_Bound]]
- [[Central_Bank_Balance_Sheet_Structure]]
- [[Monetary_Financing_Prohibition_Rationale]]
- [[Financial_Accelerator_Mechanism]]
- [[Forward_Guidance_Strategic_Implementation]]
- [[Autonomous_Factors_In_Central_Bank_Balance_Sheet]]
- [[Balance_Sheet_Transmission_Channel]]
- [[Central_Bank_Balance_Sheet_Trilemma]]
- [[EM_Balance_Sheet_Crisis_Mechanism]]
- [[US_Treasury_Balance_Sheet_H1_2026]]
- [[Payment_System_Floor_On_Fed_Balance_Sheet]]
- [[QE_Balance_Sheet_Mechanics]]
- [[Reserve_Management_Purchases_RMP]]
- [[BOP_Framework_and_Conventions]]
