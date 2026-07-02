---
title: "ACM 10Y Term Premium — H1 2026 Data and Regime Analysis"
source: "https://eco3min.fr/en/term-premium-decomposition-1961-2026/ | https://www.newyorkfed.org/research/data_indicators/term-premia | https://fred.stlouisfed.org/series/THREEFYTP10"
label: "[RAW-OFFICIAL]"
published: 2026-05-15
created: 2026-06-29
description: "ACM (Adrian-Crump-Moench) 10Y term premium data for 2024-2026. First sustained positive regime since 2014. Current level May 2026: +0.83%. Historical context and regime analysis."
tags:
  - clippings
  - term-premium
  - acm
  - yield-curve
  - treasury
---

## ACM 10Y Term Premium — Key Data Points H1 2026

| Date | ACM 10Y TP | Note |
|------|-----------|------|
| End-Sep 2024 | -0.10% | Near zero, approaching positive |
| End-Jan 2025 | +0.49% | **First turn positive after multi-year negative regime** |
| ~Q1 2026 | ~+0.60–0.70% [interpolated] | Continued normalization |
| April 30, 2026 | **+0.73%** | Confirmed positive |
| May 15, 2026 | **+0.83%** | H1 peak so far |
| May 28, 2026 | **+0.67%** | Pullback from May 15 peak |

**Most recent sourced value: +0.67% (May 28, 2026)** [WEB-2026-06: MacroMicro/streetstats citing NY Fed ACM series]. June 2026 daily/monthly value not obtained — NY Fed direct page (403) and secondary aggregators did not surface a June print as of this ingest (2026-07-02).

**Revised H1 2026 pattern:** not a monotonic climb — ACM 10Y oscillates in a **+0.6% to +0.8% band**, peaking mid-May then pulling back. Still well below the 65-year median (+1.41%).

---

## Historical Context

| Regime | Period | ACM 10Y TP Range | Driver |
|--------|--------|-----------------|--------|
| Pre-GFC | 1990s–2008 | +1.5%–3.0% | Normal risk compensation |
| QE era | 2009–2013 | +0.5%–1.5% | Fed demand suppressing premium |
| Negative regime | 2014–2024 | -0.8%–+0.2% | Global safe-haven demand; QE globally |
| Normalization | Late 2024– | -0.10% → +0.83% | Fed tightening; supply pressure; fiscal |
| **Current H1 2026** | **2026** | **+0.73%–+0.83%** | Bear steepening; OBBBA supply trajectory |

**Historical benchmarks:**
- 65-year median (1961–2026): **+1.41%**
- Great Moderation avg: **+1.65%**
- Current +0.83% = **35th percentile** of 65-year distribution
- "Partial normalization" — not yet at historical norms

---

## Regime Significance

1. **First sustained positive regime since 2014** — decade-long negative/near-zero era ended. The 2014–2024 negative period reflected: global QE (ECB, BoJ, Fed), flight-to-safety demand, pension/insurance regulatory preference for UST duration.

2. **Cross-zero signal was late 2024** — as QE era bond purchases age and mature, the structural "captive demand" for duration diminishes. Term premium recovery = private market asking for proper compensation.

3. **Current +0.83% vs median +1.41%** — still 58bp below historical norm. If full normalization occurs, 10Y yield has structural upward pressure from TP alone (assuming flat rate expectations).

4. **OBBBA trajectory** — If CBO projections of +$3–3.9T additional deficit materialize, supply pressure sustains or increases TP. TBAC noted "a need may arise for increased coupon issuance in 2027." If TP reverts to median (+1.41%), 10Y yield would be ~5.0–5.2% (vs current 4.40%).

---

## ACM Decomposition Framework

**10Y nominal yield = Expected short rate path + Term premium (ACM)**

Using June 25, 2026 data:
- 10Y nominal yield: 4.40% (H.15)
- ACM term premium (May): ~+0.73–0.83%
- **Implied expected rate path component: ~3.57–3.67%**
  - Consistent with: current EFFR 3.63% + modest cuts priced over 10yr horizon
  - Market not pricing major easing cycle; just gradual normalization

---

## Data Gap Note

NY Fed publishes ACM data daily at newyorkfed.org/research/data_indicators/term-premia. Direct fetch was blocked (HTTP 403) — data obtained via eco3min.fr which cites NY Fed ACM series. The FRED series THREEFYTP10 (Kim-Wright model, different methodology) also available; KW and ACM generally directionally consistent but differ in level.

**Recommended follow-up:** Download NY Fed ACM Excel file from term-premia-tabs page for full daily H1 2026 timeseries to replace [LLM-E] citations in synthesis report.
