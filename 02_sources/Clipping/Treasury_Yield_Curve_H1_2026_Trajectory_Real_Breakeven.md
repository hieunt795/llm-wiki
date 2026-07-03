---
title: "US Treasury Par Yield Curve + Real Yield Curve — Full H1 2026 Biweekly Trajectory"
source: "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/ (daily-treasury-rates.csv, type=daily_treasury_yield_curve and type=daily_treasury_real_yield_curve)"
label: "[RAW-OFFICIAL]"
published: 2026-07-02
created: 2026-07-03
description: "Direct CSV pull from Treasury.gov daily par yield curve (nominal) and daily real yield curve (TIPS) for the full H1 2026 window (Jan 2 - Jul 2, 2026). Replaces prior [LLM-E] estimates for 10Y real yield and 10Y breakeven inflation. Resolves gap flagged in 2026-06-29_us-treasury-balance-sheet-yield-curve-h1-2026.md Next Steps #4."
tags:
  - clippings
  - yield-curve
  - treasury
  - tips
  - real-yield
  - breakeven
  - h1-2026
---

## Method

Pulled full-year 2026 daily CSV directly from Treasury.gov (not FRED — FRED's `fredgraph.csv` returned HTTP 403 to automated fetch; Treasury.gov's own CSV endpoint worked without blocking):
- Nominal: `daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026`
- Real (TIPS): `daily-treasury-rates.csv/2026/all?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026`

126 rows each (one per business day, Jan 2 – Jul 2, 2026). Table below samples ~biweekly checkpoints. Breakeven inflation computed as nominal 10Y − real 10Y (standard approximation; note Treasury's real/nominal curves use slightly different underlying security sets, so this differs marginally from the official T10YIE FRED series, but is directionally reliable).

## H1 2026 Biweekly Trajectory

| Date | 2Y nom | 5Y nom | 10Y nom | 20Y nom | 30Y nom | 2s10s | 2s30s | 10Y real (TIPS) | 10Y breakeven (nom−real) |
|------|--------|--------|---------|---------|---------|-------|-------|------------------|---------------------------|
| 01/02/2026 | 3.47 | 3.74 | 4.19 | 4.81 | 4.86 | +72bp | +139bp | 1.94 | 2.25 |
| 02/02/2026 | 3.57 | 3.83 | 4.29 | 4.85 | 4.90 | +72bp | +133bp | 1.94 | 2.35 |
| 02/17/2026 | 3.43 | 3.63 | 4.05 | 4.63 | 4.68 | +62bp | +125bp | 1.79 | 2.26 |
| 03/02/2026 | 3.47 | 3.62 | 4.05 | 4.64 | 4.70 | +58bp | +123bp | 1.76 | 2.29 |
| 04/01/2026 | 3.81 | 3.97 | 4.33 | 4.91 | 4.91 | +52bp | +110bp | 2.02 | 2.31 |
| 05/01/2026 | 3.88 | 4.02 | 4.39 | 4.96 | 4.97 | +51bp | +109bp | 1.91 | 2.48 |
| 06/01/2026 | 4.05 | 4.18 | 4.47 | 4.99 | 4.99 | +42bp | +94bp | 2.07 | 2.40 |
| 06/26/2026 | 4.07 | 4.12 | 4.38 | 4.87 | 4.87 | +31bp | +80bp | 2.18 | 2.20 |
| 07/02/2026 | 4.14 | 4.23 | 4.49 | 4.99 | 4.98 | +35bp | +84bp | 2.26 | 2.23 |

## Key Findings

**1. 2s10s NARROWED through H1, it did not widen.** From +72bp (early Jan) to +31–35bp (late June/July) — a ~40bp compression. The existing draft's Timing-layer placeholder ("Bear steepening moderate: 2s10s ~+40-60bp [LLM-E]" as "Present H1 2026") is **superseded**: confirmed 2s10s at H1 close is *below* that estimated range, and the direction of travel within H1 was flattening, not steepening.

**2. The flattening is front-end-led, not long-end-led.** H1 moves: 2Y +67bp (3.47→4.14), 10Y +30bp (4.19→4.49), 30Y +12bp (4.86→4.98). The front end sold off roughly 2x the 10Y move and 5x the 30Y move. This reads as the market pricing OUT previously-expected Fed rate cuts (hawkish repricing of the front end) rather than a long-end-led term-premium widening. Fed funds target held at 3.50–3.75% throughout (no cut delivered in H1 per existing doc) — 2Y yield rising toward/through the top of that range while the target itself was static is the signature of receding cut expectations, not a policy move.

**3. Breakeven inflation was flat/rangebound all H1 (2.20–2.48%), no trend.** The entire nominal 10Y increase (+30bp for H1) decomposes almost entirely into real yield (+32bp: 1.94%→2.26%), with breakeven essentially unchanged (2.25%→2.23%, net ~0). This corroborates the ACM decomposition already in the wiki (Fed_Duration_Extraction_Term_Premium, term premium +0.67→+0.83% May 2026): both decompositions (real/breakeven AND ACM expected-path/term-premium) agree the yield level increase is a **real-rate story**, not an inflation-expectations story.

**4. 30Y was nearly flat across H1** (4.86% Jan 2 → 4.98% Jul 2, +12bp only, with a local peak ~5.12-5.14% mid-May coinciding with the Q2 refunding announcement, then retracing). The long end is the most stable point on the curve in H1 2026, not the most volatile — contradicts a naive "term premium is driving everything" read; term premium recovery matters for the LEVEL of 30Y (elevated vs 2021-2023) but was not the marginal H1 mover.

## Boundary / Confidence

- TIER: RAW-OFFICIAL, Treasury.gov direct CSV — highest confidence source in the cluster for this data.
- Breakeven computed as a simple nominal−real spread, not the official Treasury/FRED T10YIE methodology (which uses a slightly different curve-fitting approach) — good enough for directional/magnitude conclusions, not for precise basis-point arbitrage-style claims.
- Did not pull 5Y breakeven or 5Y5Y forward breakeven (would sharpen "when did inflation expectations move" — not attempted this round).
