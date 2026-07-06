# USD/JPY Carry Overhang vs. Carry Unwind — Research Note

**MODE DEEP | 2026-07-05**

**Thesis:** H1 2026 chưa cho thấy một yen carry-trade unwind hoàn chỉnh; dữ liệu chính thức phù hợp hơn với trạng thái carry overhang: short-JPY positioning vẫn lớn, foreign selling cuối tháng 6 là portfolio de-risking, và MOF intervention risk làm giảm risk-adjusted carry nhưng chưa triệt tiêu chênh lệch lợi suất Mỹ-Nhật.

---

## CURRENTLY — 2026-07-05

[RAW-OFFICIAL:CFTC COT] CFTC CME futures-only report available on 2026-07-05 shows Japanese Yen futures as of 2026-06-23: non-commercial longs 113,698 contracts, shorts 259,802 contracts, net short -146,104 contracts, and open interest 431,030 contracts.

[RAW-OFFICIAL:CFTC COT] Compared with 2026-06-16, non-commercial shorts fell by 7,705 contracts, longs fell by 3,677 contracts, and open interest fell by 89,795 contracts.

[RAW-OFFICIAL:MOF Securities Flows] MOF data for 2026-06-21 to 2026-06-27 shows nonresident net disposition of Japanese securities totaling JPY 4.7363 trillion, with JPY 1.8165 trillion in equities/investment funds, JPY 493.7 billion in long-term debt, and JPY 2.4261 trillion in short-term debt.

[WEB-2026-07-02:MarketWatch] Market commentary frames the main risk as a renewed yen carry overhang under a strong dollar, with intervention or a rate-gap shift as the potential unwind trigger.

---

## Top-Down Entry

[LLM-S] The core distinction is between **position compression** and **carry unwind**. Position compression means gross or speculative exposure is reduced while the directional regime remains in place. Carry unwind means the funding currency is bought back at scale, risk assets funded by that currency are sold, and spot/forward yen demand becomes the dominant price impulse.

[RAW-OFFICIAL:CFTC COT][LLM-S] CFTC data supports position compression: non-commercial shorts fell by 7,705 contracts over the week to June 23, but the account still held a net short of 146,104 Japanese Yen futures contracts.

[RAW-OFFICIAL:MOF Securities Flows][LLM-S] MOF data supports late-quarter portfolio de-risking: foreign investors sold Japanese securities in the week ending June 27, but securities-flow data does not identify whether the FX hedge leg was closed.

## Macro Layer

[WIKI] [[BOJ_June_2026_Rate_Hike_Ueda_Absence]] establishes that BOJ raised the uncollateralized overnight call rate guideline to around 1.00% on June 16 while the U.S. policy-rate range remained materially higher.

[LLM-S] The carry regime remains mechanically viable when the interest-rate differential is still positive after realized volatility, hedge cost, and intervention tail risk are deducted.

[WEB-2026-07-01:Business Insider] Market commentary identifies the wide U.S.-Japan rate gap and dollar-asset demand as the primary driver of yen weakness, while also warning that reserve-funded intervention could transmit into the U.S. Treasury market.

## Plumbing Layer

[LLM-S] Yen carry exposure can sit in at least three locations: futures/FX speculative shorts, foreign investors' currency-hedged Japanese equity positions, and yen-funded purchases of U.S. or global higher-yielding assets.

[RAW-OFFICIAL:CFTC COT] The futures leg still showed a large non-commercial short yen position as of June 23.

[RAW-OFFICIAL:MOF Securities Flows] The Japanese-securities leg showed foreign selling in the week ending June 27.

[LLM-S] These two facts do not mechanically net against each other. A foreign investor can sell Japanese equity and still keep a short-JPY hedge open; that weakens JPY. A different investor can close a short-JPY futures position while keeping foreign assets unchanged; that strengthens JPY. A completed unwind requires the second channel to dominate the first.

```text
Carry-overhang state:
  Rate differential remains positive
  + CFTC non-commercial JPY net short still large
  + Foreign selling does not force hedge closure
  -> USD/JPY pressure remains upward or unstable near intervention thresholds

Unwind state:
  Rate differential narrows or intervention shock hits
  + JPY shorts covered through spot/forward/futures
  + Funded risk assets sold to repay yen liabilities
  -> JPY appreciates, risky assets sell off, volatility rises
```

## Treasury Layer

[LLM-S] For a treasury desk, the correct label is **carry-overhang with intervention convexity**, not completed unwind.

[LLM-S] The operating hedge rule is to treat short-JPY as still carry-positive but discontinuous: carry accrues daily, while MOF intervention can impose a one-session mark-to-market loss and force stop-loss or VAR deleveraging.

[LLM-S] The key dashboard should combine five variables: USD/JPY spot relative to 162-165, CFTC non-commercial JPY net short, MOF weekly foreign securities flow, U.S.-Japan 2-year yield differential, and one-month USD/JPY implied volatility.

## Timing Layer

| Date / Window | Signal | Interpretation |
|---|---|---|
| 2026-06-16 | BOJ raises call-rate guideline to around 1.00% | Narrows rate differential only marginally |
| 2026-06-23 | CFTC non-commercial JPY net short = -146,104 contracts | Position compression but still large short-JPY exposure |
| 2026-06-21 to 2026-06-27 | MOF weekly securities flow: nonresident net disposition JPY 4.7363tn | Late-quarter foreign de-risking, not sufficient proof of carry unwind |
| 2026-07-01 to 2026-07-03 | USD/JPY near 162-163 in market reports | Carry regime still active near MOF intervention threshold |
| 2026-07-31 / 2026-08-03 to 07 | MOF next monthly and daily FEIO releases scheduled | Exact intervention-date test remains open |

## Boundary Conditions

[LLM-S] This research note should be revised if the next CFTC report shows a large collapse in non-commercial yen shorts, if MOF daily FEIO confirms late-June intervention not yet visible in monthly windows, or if USD/JPY falls sharply while Japanese-equity foreign selling continues.

[LLM-S] A full unwind diagnosis requires at least two of three confirmations: yen appreciation, falling short-JPY positioning, and simultaneous selling of funded risk assets.

## Conclusion

[LLM-S] The evidence supports **compression without completion**. CFTC shows fewer non-commercial short contracts than the prior week, but the net short remains large. MOF shows foreign selling of Japanese securities, but the data does not specify hedge closure. USD/JPY remaining near intervention thresholds implies the rate-differential and dollar-demand channel still dominates.

## Next Steps

1. Update [[Japan_Foreign_Selling_Late_June_2026_Carry_Unwind_Test]] when CFTC publishes the next COT file after 2026-06-23.
2. Re-run the carry-unwind test after MOF releases the July 31 monthly FEIO and August 3-7 daily FEIO for April-June 2026.
3. Add a dedicated node for `Carry_Overhang_With_Intervention_Convexity` if the next CFTC report still shows large short-JPY positioning.
