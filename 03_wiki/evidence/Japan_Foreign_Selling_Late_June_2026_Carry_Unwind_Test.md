---
title: Japan Foreign Selling Late June 2026 Carry-Unwind Test
aliases:
  - Late June 2026 Japan foreign selling
  - Japan carry unwind test 2026
  - Foreign selling Japan June 2026
type: evidence
tags:
  - japan
  - foreign-exchange
  - capital-flows
  - carry-trade
  - current-events
status: verified
confidence: 4
half_life_years: 0.1
school: ""
superseded_by: null
superseded_date: null
expert_lens: "Ministry of Finance Japan | TQN"
provenance: "[RAW-OFFICIAL: MOF International Transactions in Securities weekly and monthly releases]"
thesis: "When late-quarter foreign selling in Japanese securities is not matched by yen appreciation, it indicates portfolio de-risking rather than a completed yen carry unwind because hedge closures would require spot or forward yen buying."
source_refs:
  - file: "MOF_International_Transactions_In_Securities_Week_2026-06-21_27.md"
  - file: "MOF_FEIO_H1_2026_Official_Releases.md"
  - file: "CFTC_Japanese_Yen_Futures_COT_2026-06-23.md"
  - file: "WEB_Japan_JGB10Y_Fiscal_CarryTrade_H1_2026_2026-07-06.md"
created: '2026-07-05'
updated: '2026-07-06'
---

# [[Japan_Foreign_Selling_Late_June_2026_Carry_Unwind_Test]]

## Thesis

[RAW-OFFICIAL:MOF Securities Flows][LLM-S] When late-quarter foreign selling in Japanese securities is not matched by yen appreciation, it indicates portfolio de-risking rather than a completed yen carry unwind because hedge closures would require spot or forward yen buying.

## 1. Observed Flow

[RAW-OFFICIAL:MOF Securities Flows] MOF's weekly release for June 21-27, 2026 shows nonresident net disposition of Japanese securities totaling JPY 4.7363 trillion, split into JPY 1.8165 trillion of equity and investment fund shares, JPY 493.7 billion of long-term debt securities, and JPY 2.4261 trillion of short-term debt securities.

[RAW-OFFICIAL:MOF Securities Flows] MOF's monthly release for May 2026 showed the opposite aggregate sign: nonresidents recorded net acquisition of JPY 3.1058 trillion across Japanese securities, including JPY 2.9272 trillion of equity and investment fund shares and JPY 894.5 billion of long-term debt securities, partly offset by JPY 716.0 billion of short-term debt net disposition.

[LLM-S] The data therefore supports a late-June foreign-selling episode, not a uniform H1 2026 foreign-exit regime.

## 2. Carry-Unwind Diagnostic

[WIKI] A completed yen carry unwind should reduce short-yen exposure, either through spot JPY buying or through forward/hedge closure that has the same directional implication for yen demand.

[LLM-S] The late-June flow data does not by itself prove a carry unwind, because MOF securities-flow tables record purchases and sales of securities but do not separate unhedged asset liquidation from currency-hedged equity packages.

[LLM-S] If a foreign investor sells unhedged Japanese securities and converts the JPY proceeds into USD, the transaction creates JPY selling pressure and can weaken the yen.

[LLM-S] If a foreign investor sells a currency-hedged Japanese equity position and closes the short-JPY hedge at the same time, the hedge closure creates JPY buying pressure and can strengthen the yen.

[WIKI] USD/JPY remaining near the 162 area after the late-June selling is more consistent with portfolio de-risking and USD demand than with a completed short-JPY carry unwind; see [[BOJ_June_2026_Rate_Hike_Ueda_Absence]] and [[Japan_FX_Intervention_May_2026_Event]].

## 2b. Futures-Positioning Cross-Check

[RAW-OFFICIAL:CFTC COT] The CFTC CME futures-only report available on 2026-07-05 lists Japanese Yen futures positions as of June 23, 2026: open interest was 431,030 contracts, non-commercial longs were 113,698 contracts, non-commercial shorts were 259,802 contracts, and non-commercial spreading positions were 17,748 contracts.

[RAW-OFFICIAL:CFTC COT] Non-commercial net position was therefore -146,104 contracts, calculated as 113,698 long contracts minus 259,802 short contracts.

[RAW-OFFICIAL:CFTC COT] Compared with June 16, 2026, non-commercial shorts fell by 7,705 contracts while non-commercial longs fell by 3,677 contracts, so net short exposure declined by 4,028 contracts.

[LLM-S] This supports position compression, not a completed unwind: speculative short-JPY futures exposure was reduced, but the non-commercial account remained materially net short yen as of June 23.

## 2c. June Aggregate Confirmation and Super-Long-Tenor Detail (2026-07-06 update)

[WEB-2026-07-02:Bloomberg] Bloomberg reported on July 2, 2026 that overseas investors sold the largest net amount of Japanese government bonds in three years during June 2026, after the debt's return trailed most global sovereign peers. This corroborates the June 21-27 weekly disposition already recorded in Section 1 by confirming the weekly episode was part of a month-level pattern, not an isolated week.

[WEB-2026-05-20:Bloomberg] A separate release around May 20, 2026 recorded foreign investors' first net outflow from Japan's super-long-maturity government bonds since 2024 — a tenor-specific data point that pre-dates the June episode and indicates the foreign-selling pattern in longer maturities began building before late June.

[WIKI] The June aggregate sale coincides with the fiscal-driven long-end yield repricing documented in [[Japan_JGB_10Y_Yield_Fiscal_Repricing_H1_2026]]: a weak 10-year JGB auction and concern over the Takaichi government's record FY2026 budget issuance plan gives foreign holders of long-tenor JGBs an additional, fiscal-risk reason to reduce exposure that is independent of the currency-hedge classification question raised in Section 2.

[LLM-S] This does not resolve the Section 2 hedge-classification ambiguity — a bond sale driven by fiscal-risk repricing can still be paired with either an open or closed FX hedge — but it does add a second, non-carry-related driver (duration/fiscal-risk aversion on JGBs) that can produce foreign net selling independent of any carry-unwind dynamic, which is a further reason not to label the June episode a completed yen carry unwind on securities-flow data alone.

## 3. T-Account Logic

[LLM-S] Unhedged foreign sale of Japanese securities:

```text
Foreign investor:
  Assets: - Japanese equity/JGB
          + JPY cash
          - JPY cash
          + USD cash

FX dealer / bank:
  Assets/Liabilities: + JPY received
                      - USD paid

Market implication:
  JPY supply rises against USD demand -> USD/JPY upward pressure
```

[LLM-S] Hedged foreign sale with hedge closure:

```text
Foreign investor:
  Assets: - Japanese equity
  Hedge:  close short-JPY forward
          buy JPY / sell USD in hedge leg

Market implication:
  JPY demand rises through hedge closure -> USD/JPY downward pressure
```

## 4. Boundary Conditions

[RAW-OFFICIAL:MOF FEIO] MOF reported JPY 0 foreign exchange intervention operations for May 28-June 26, 2026, while the exact daily execution dates for April-June 2026 are scheduled for release in August 2026.

[LLM-S] The carry-unwind diagnosis should be revised if the August daily FEIO release shows late-June intervention, or if futures/forward-position data shows that the June 21-27 securities outflow coincided with large short-JPY hedge closure.

[LLM-S] The diagnosis should also be revised if the next CFTC report after June 23 shows a discontinuous collapse in non-commercial JPY shorts or a flip from net short to net long yen exposure.

## Treasury Insight

[LLM-S] For a treasury desk, the late-June foreign-selling data is a hedge-classification problem, not a simple risk-off signal: the same securities outflow can weaken or strengthen JPY depending on whether the FX hedge leg is left open, reduced, or fully closed.

[LLM-S] The operating rule is to pair MOF securities-flow data with USD/JPY spot response, cross-currency basis, and JPY forward points before labeling the episode as carry unwind.

## Related

- [[BOJ_June_2026_Rate_Hike_Ueda_Absence]]
- [[Japan_FX_Intervention_May_2026_Event]]
- [[FX_Intervention_Ambush_Tactic]]
- [[Japan_FX_Intervention_MOF_BOJ_Framework]]
- [[Foreign_Capital_Flows_Determinants]]
- [[Japan_JGB_10Y_Yield_Fiscal_Repricing_H1_2026]]
