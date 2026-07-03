# Concept Map — Japan May-26 CPI Inflation Report

Source: `02_sources/Clipping/Japan May-26 CPI Inflation Report.md` [RAW-CLIP: Benigno, published 2026-06-19]
Pipeline: W5_secondary_ingest.md — Phase A (Pre-flight & Classification)

## Classification

- Source type: substack commentary on official Japan MIC/e-Stat CPI release, single named author, source URL present, published date present, no footnote citations beyond "e-Stat" table attribution → **[RAW-CLIP]** confirmed.

## Claims Table

| Claim | Type | Has-citation | Risk Flag |
|---|---|---|---|
| Headline CPI 1.5% YoY (May) / 1.4% (Apr) / 1.6% forecast; 0.5% MoM (May) / 0.3% (Apr) | data | e-Stat (implied) | VERIFY-NUMBER |
| Core CPI (ex fresh food) 1.4% YoY (May, Apr, forecast all match); 0.5% MoM (May) / 0.3% (Apr) | data | e-Stat | VERIFY-NUMBER |
| Core-core (ex fresh food & energy) 1.8% YoY (May) / 1.9% (Apr); 0.2% MoM (May) / −0.1% (Apr) | data | e-Stat | VERIFY-NUMBER |
| HICP-equivalent (ex imputed rents) 1.7% YoY (May) / 1.5% (Apr) | data | e-Stat | VERIFY-NUMBER |
| Energy −2.5% YoY (May) / −3.9% (Apr); +3.4% MoM (May) | data | e-Stat | VERIFY-NUMBER |
| Goods 2.0% YoY (May) / 1.7% (Apr); 0.7% MoM (May) / 0.9% (Apr) | data | e-Stat | VERIFY-NUMBER |
| Services 1.0% YoY (May) / 0.9% (Apr); 0.2% MoM (May) / −0.5% (Apr) | data | e-Stat | VERIFY-NUMBER |
| Services ex-imputed-rents 1.3% YoY (May) / 1.2% (Apr), vs >3% late-2023 peak | data | e-Stat | VERIFY-NUMBER |
| Food 3.5% YoY (unchanged May/Apr); Fresh food 3.5% (May) / 0.3% (Apr); Rice −4.9% (May) / +0.6% (Apr) | data | e-Stat | VERIFY-NUMBER |
| Imputed rents 0.4% YoY (unchanged), ~16% CPI weight | data | e-Stat | VERIFY-NUMBER |
| "Three forces" framework (food fading / energy pass-through / wage-price channel) + BOJ weighting statement | mechanism/interpretive | author's own synthesis, no BOJ verbatim quote | CHECK-AGREE |
| Wage figures: base-pay mid-2%, scheduled wages high-2%-3% | data | uncited primary series (MHLW/Rengo Shunto implied, not named) | CHECK-AGREE |
| June 15-16 hike to 1.00%, 7-1 vote, rationale (underlying inflation toward 2%, declining ME downside risk, avoid falling behind curve) | policy fact | public BOJ decision | CHECK-AGREE |
| BOJ Outlook: core CPI to "accelerate clearly above 2%" then fade; target achievement H2 FY2026–FY2027 | forward-looking | BOJ Outlook Report (paraphrased) | CHECK-AGREE |
| Next checkpoint: July 30-31 meeting + July Outlook Report | forward-looking | public calendar | CHECK-AGREE |
| No PPI/wholesale numeric data given (only qualitative "wholesale prices" mention) | absence-of-data | n/a | CHECK-AGREE |

No claims flagged `CHECK-CONFLICT`.

## Phase B — Adversarial Audit Results

| Claim group | Wiki search target | Result |
|---|---|---|
| All CPI/sectoral YoY numbers | `Japan_May_2026_CPI_Report` | **AGREE** — exact match; node built from a derived summary of the same figures, now confirmed against primary text. MoM figures were NOT previously captured — enrichment, not conflict. |
| Three-forces framework | `Japan_Inflation_Three_Force_Decomposition` | **AGREE** — node already models this; primary text supplies the verbatim paragraph the node previously cited only via paraphrase. Confirms (does not change) the node's critical assessment that this is author-inferred BOJ reasoning, not a quoted BOJ statement. |
| Hike details | `BOJ_June_2026_Rate_Hike_Ueda_Absence` | **AGREE** — matches existing node exactly. |
| No-PPI-data observation | `Japan_Inflation_Three_Force_Decomposition` §3 | **AGREE** — confirms existing Failure-Conditions note; no change needed there. |

## Disposition

No SPAWN, no CONTRADICTION, no PERSPECTIVE node warranted — all content is enrichment of two existing nodes. Writeback: **UPDATE ×2** (see log.md).
