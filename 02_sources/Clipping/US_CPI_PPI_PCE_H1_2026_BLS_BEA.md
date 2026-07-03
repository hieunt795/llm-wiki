---
title: "US CPI, PPI, PCE — H1 2026 Data Anchors (BLS/BEA)"
source: "api.bls.gov/publicAPI/v2 (CPI series) + fred.stlouisfed.org/graph/fredgraph.csv (PCEPI, PCEPILFE — sourced from BEA)"
accessed: "2026-07-03"
tier: "RAW-OFFICIAL"
---

# US CPI, PPI, PCE — H1 2026 Data Anchors

Pulled directly from BLS public API and FRED CSV endpoint (both bls.gov and fred.stlouisfed.org HTML pages return HTTP 403 via automated fetch — Akamai edge block — but their data endpoints `api.bls.gov/publicAPI/v2/timeseries/data/<series_id>` and `fred.stlouisfed.org/graph/fredgraph.csv?id=<series_id>` are reachable directly via curl). Data confirmed through May 2026 — June CPI releases 2026-07-14, June PPI releases 2026-07-15.

## CPI (BLS — verified: computed YoY matches BLS's own published headline exactly: CPI-U May 2026 YoY 4.2%, index level 335.123)

### Headline CPI-U, SA index level (CUSR0000SA0)
| Month 2026 | Index | MoM % |
|---|---|---|
| Jan | 326.588 | — |
| Feb | 327.460 | +0.267% |
| Mar | 330.293 | +0.865% |
| Apr | 332.407 | +0.640% |
| May | 333.979 | +0.473% |

### Headline CPI-U, NSA index level (CUUR0000SA0) — for YoY
May 2026: 335.123 vs May 2025: 321.465 → **YoY +4.25%** (matches BLS-published 4.2%)

### Core CPI (less food & energy), SA (CUSR0000SA0L1E)
| Month 2026 | Index | MoM % |
|---|---|---|
| Jan | 332.793 | — |
| Feb | 333.512 | +0.216% |
| Mar | 334.165 | +0.196% |
| Apr | 335.423 | +0.376% |
| May | 336.121 | +0.208% |

### Core CPI, NSA (CUUR0000SA0L1E) — for YoY
May 2026: 336.846 vs May 2025: 327.509 → **YoY +2.85%**

### CPI Energy, NSA (CUUR0000SA0E)
| Month 2026 | Index | Cumulative vs Jan |
|---|---|---|
| Jan | 272.668 | — |
| Feb | 277.179 | +1.65% |
| Mar | 310.280 | +13.8% |
| Apr | 329.907 | +21.0% |
| May | 346.042 | **+26.9%** |

### CPI Food, NSA (CUUR0000SAF1)
Jan 345.165 → May 349.032 = +1.12% over 4 months (modest).

### CPI Shelter, NSA (CUUR0000SAH1)
Jan 421.526 → May 428.677 = +1.70% over 4 months (steady, moderate — consistent with ongoing shelter disinflation trend continuing, not reversing).

**Data gap note:** October 2025 CPI/PPI is missing from all BLS series — footnote code X, "Data unavailable due to the 2025 lapse in appropriations" (government shutdown).

## PPI Final Demand headline (BLS) — series-ID mismatch resolved via official release text

Attempted FD-ID series pulls under guessed codes (WPSFD49207, WPSFD49116, WPSFD4131, WPSFD41312) produced index levels/MoM deltas that did NOT match BLS's own published headline for May 2026 (e.g. one guessed "final demand" series computed +2.63% MoM vs. official +1.1%). Root cause: unconfirmed series-ID guesses (BLS catalog metadata disabled without a registration key; bls.gov/ppi/fd-id/ page blocked by Akamai). **Do not treat those specific raw index pulls as data anchors** — they are superseded by the verified numbers below.

Verified via BLS's own release text (bls.gov/news.release/ppi.nr0.htm, cross-confirmed via CNBC mirror), internally consistent across 5 independent figures (weighted-average cross-check: 0.33×2.8% + 0.67×0.3% ≈ 1.13% ≈ official 1.1% headline):

- **Final demand: +1.1% MoM SA** (May 2026)
- **Final demand goods: +2.8% MoM** — largest increase since the FD-ID series began (Dec 2009). **80% of this traced to final-demand energy +10.7% MoM.**
- Final demand services: +0.3% MoM
- Final demand, NSA: **+6.5% YoY** — largest 12-month rise since Nov 2022 (+7.4%)
- **Core (final demand less foods, energy, and trade services): +0.8% MoM** — largest advance since March 2022 (+0.9%)

[WEB-2026-06-11:bls.gov/news.release/ppi.nr0.htm | cnbc.com/2026/06/11]

## PPI Intermediate Demand by Production Flow — Stage 1-4 (Table D) — INDEPENDENTLY VERIFIED

Correct series IDs found and confirmed (learning from the FD-ID mis-fire above — searched for BLS's own Table D documentation before pulling, then cross-checked BLS API against FRED mirror):
- Stage 1 NSA: `WPUID51` — Stage 4 NSA: `WPUID54` — confirmed via both api.bls.gov and fred.stlouisfed.org (identical values)
- Stage 2 NSA: `WPUID52` — Stage 3 NSA: `WPUID53` — pulled via FRED mirror only (BLS API daily quota exhausted mid-session)

### YoY by stage, NSA
| Month 2026 | Stage 1 | Stage 2 | Stage 3 | Stage 4 | Gap (S1−S4) |
|---|---|---|---|---|---|
| Jan | 4.22% | — | — | 4.05% | +0.16pp |
| Feb | 5.05% | — | — | 4.43% | +0.63pp |
| Mar | 6.54% | — | — | 4.47% | **+2.07pp** |
| Apr | 8.92% | 9.02% | 5.37% | 5.39% | **+3.53pp** |
| May | 12.26% | 12.49% | 7.20% | 6.53% | **+5.73pp** |

Stage 1 May MoM: +3.23% (167.147 vs 161.922 April).

**Cross-check against Gianluca Benigno's substack series** (see companion clipping `Benigno_Nonlinear_Inflation_IO_Cascade_2026.md`): his reported gap figures were March "+2.0pp", April "+3.5pp", May "+5.8pp" — matches this independently-computed series within ~0.1-0.3pp at every checkpoint. His Stage 1 May MoM figure ("+3.2%, largest since BLS began") matches the computed +3.23% almost exactly. His Stage 3 May YoY ("7.2%") matches exactly (7.20%). His April Stage 2 figure (7.1%) diverges more from the computed 9.02% — likely a revision-timing difference (BLS revises PPI up to 4 months after initial publication; he wrote in early June on less-revised April data, this pull is from July with two more months of revision applied).

**Nuance not in his framing:** the computed series shows the cascade is not perfectly monotonic (S1 > S2 > S3 > S4) — in May, Stage 2 (12.49%) slightly exceeds Stage 1 (12.26%), and the sharpest break sits between Stage 2 (~12%) and Stage 3 (~7%) rather than a clean four-step staircase. This is consistent with his own "narrow but deep" sectoral-concentration finding (energy-petrochemical-freight corridor specifically), not a contradiction of it.

## Oil / energy shock context (EIA, World Bank, Yahoo Finance — WEB, cross-corroborated)

- Middle East military action Feb 28, 2026 → de facto closure of the Strait of Hormuz (handles ~35% of global seaborne crude trade)
- Initial global oil supply reduction: ~10 million barrels/day (largest oil supply shock on record)
- Brent crude: $61/bbl (Jan 1, 2026) → $118/bbl (end Q1 2026) — largest inflation-adjusted quarterly oil price increase in data back to 1988 [WEB-2026-04:eia.gov/todayinenergy]
- Iraq, Saudi Arabia, UAE shut in production in response to disrupted navigation
- US retail gasoline $3.99/gal, diesel $5.40/gal on March 30, 2026 — highest in real terms in over 2 years
- Brent down ~18% from March peak by June 2026 (partial price mean-reversion, per Benigno Part II Update)
- World Bank (April 2026 Commodity Markets Outlook): energy prices projected +24% for the year, highest since the 2022 Russia/Ukraine shock

## Fed policy reaction (Federal Reserve FOMC minutes — RAW-OFFICIAL)

- FOMC minutes (Jan 27-28, Mar 17-18, Apr 28-29 2026): both headline and core inflation noted "further above the 2 percent target"
- Core goods inflation elevated — staff attributed "largely" to tariff effects; core services (incl. housing) inflation declining over the same period (partial offset)
- FOMC dropped previously-indicated rate cut; adopted "deliver price stability" language after 5 years above 2% target; signaled possible rate hike (per June 17, 2026 SEP materials + minutes)
- Source: federalreserve.gov/monetarypolicy/fomcminutes20260128.htm, fomcminutes20260318.htm, fomcminutes20260429.htm, fomcprojtabl20260617.htm [RAW-OFFICIAL]

## PCE (BEA, via FRED CSV — verified: computed YoY exactly matches BEA's own published 4.1%/3.4%)

### Headline PCE price index (PCEPI, 2017=100)
| Month 2026 | Index | MoM % |
|---|---|---|
| Jan | 129.023 | — |
| Feb | 129.539 | +0.400% |
| Mar | 130.403 | +0.667% |
| Apr | 130.938 | +0.410% |
| May | 131.527 | +0.450% |

May 2026 YoY: 131.527 / 126.380 (May 2025) − 1 = **+4.07%** (matches BEA-published "4.1%")

### Core PCE price index, excl. food & energy (PCEPILFE, 2017=100)
| Month 2026 | Index | MoM % |
|---|---|---|
| Jan | 128.455 | — |
| Feb | 128.961 | +0.394% |
| Mar | 129.343 | +0.296% |
| Apr | 129.667 | +0.250% |
| May | 130.082 | +0.320% |

May 2026 YoY: 130.082 / 125.790 (May 2025) − 1 = **+3.41%** (matches BEA-published "3.4%", highest since Oct 2023)
