---
title: "US CPI, PPI, PCE — H1 2026"
aliases:
- US Inflation H1 2026
- CPI PPI PCE Divergence 2026
- Hormuz Oil Shock Inflation Data
type: evidence
tags:
- inflation
- cpi
- ppi
- pce
- united-states
- energy-shock
- tariffs
- macro
status: verified
confidence: 4
half_life_years: 0.1
school: ''
superseded_by: null
superseded_date: null
expert_lens: "BLS | BEA | FOMC"
provenance: "RAW-OFFICIAL: BLS API, FRED/BEA CSV, Federal Reserve FOMC minutes — pulled 2026-07-03"
thesis: US headline CPI (4.2% YoY) and PCE (4.1% YoY) in H1 2026 diverge sharply
  from core measures (2.85% / 3.4%) because a Middle East oil-supply shock (Hormuz
  closure, Feb 28) drove energy prices +27% in four months, while a separate tariff
  mechanism elevates core goods specifically and PPI data show broadening pipeline
  pressure via producer-level acceleration.
source_refs:
- file: "US_CPI_PPI_PCE_H1_2026_BLS_BEA.md"
- file: "Benigno_Nonlinear_Inflation_IO_Cascade_2026.md"
- file: "US May-26 CPI Inflation Report.md"
created: '2026-07-03'
updated: '2026-07-03'
---

# [[US_CPI_PPI_PCE_H1_2026]]

## Evidence Overview
[RAW-OFFICIAL: BLS API `api.bls.gov/publicAPI/v2`, FRED CSV mirror of BEA data, pulled 2026-07-03] Data confirmed through May 2026 (June CPI releases 2026-07-14, June PPI 2026-07-15 — H1 2026 is technically Jan-May at time of writing). Both bls.gov and fred.stlouisfed.org HTML pages return HTTP 403 to automated fetch (Akamai edge block); their underlying data endpoints (`api.bls.gov/publicAPI/v2/timeseries/data/<id>`, `fred.stlouisfed.org/graph/fredgraph.csv?id=<id>`) are reachable directly. All numbers below are independently computed from index levels and verified against BLS/BEA's own published headline percentages (exact or near-exact match in every case).

## Quantified Findings

### Headline vs. core divergence (May 2026 YoY)
| Measure | Headline | Core |
|---|---|---|
| CPI-U | **4.2%** | 2.85% |
| PCE (Fed's target gauge) | **4.1%** | **3.4%** (highest since Oct 2023) |

[RAW-OFFICIAL: BLS] CPI energy index (NSA) rose from 272.668 (Jan) to 346.042 (May) — **+26.9% in four months**, the dominant arithmetic driver of the headline-core gap. CPI food (+1.1%) and shelter (+1.7%) moved modestly over the same window (this is cumulative Jan→May index-level change, not a YoY rate) — shelter disinflation trend continuing, not reversing.

**Reconciliation note on core CPI precision:** this node's 2.85% core-CPI figure is independently computed from BLS index levels; [RAW-CLIP: Benigno 2026-06-10] reports BLS's own published, rounded release figure of **2.9% YoY** for the same May 2026 print. Both are correct readings of the same underlying data at different rounding stages — not a contradiction.

### CPI Component Breakdown (May 2026, per [RAW-CLIP: Benigno 2026-06-10])

This granularity is not otherwise captured above; the headline/core numbers agree with this node's independent BLS computation (see reconciliation note).

| Measure | May YoY | April YoY | May MoM | April MoM |
|---|---|---|---|---|
| Core services (ex energy) | 3.4% | 3.3% | — | — |
| Core goods (ex food/energy) | 1.1% | 1.1% | 0.0% (n.s.a.) | 0.1% (n.s.a.) |
| Shelter (rent of shelter) | 3.3% | 3.3% | 0.3-0.4% (s.a.)* | 0.6% (s.a.) |
| Supercore services (core services ex shelter) | 3.7% | 3.5% | 0.5% | 0.5% |
| Rent subcomponent | 2.9% | 2.8% | — | — |
| Owners' equivalent rent (OER) | 3.3% | 3.3% | — | — |
| Gasoline | +40.5% (level vs. year-ago) | — | +7.0% (s.a.) / +8.6% (n.s.a.) | — |
| Apparel (tariff-sensitive) | +4.8% | — | — | — |

*Source inconsistency, not resolved in this pass: the clip's "Key takeaways" section states May shelter MoM at 0.4% (s.a.), while its body text states 0.3% (s.a.) for the same figure — both cite April at 0.6%. Flagged, not adjudicated; do not cite a single precise May shelter MoM value from this source without checking BLS directly.

[RAW-CLIP: Benigno 2026-06-10] Energy contributed over 60% of the May monthly all-items increase — consistent with this node's energy-shock driver (see Three Distinct Drivers §1). Apparel's tariff-linked acceleration is the clearest goods-side confirmation of driver §2 (tariff pass-through) at the sub-category level. Core services and shelter/OER/rent remain "substantially below their post-pandemic highs," per the source, functioning as a disinflationary offset to the goods/energy pressure — this is new sub-component evidence for the "narrower, not broad-based" reading already implicit in this node's three-driver framing.

**New context — October 2025 shutdown distortion:** [RAW-CLIP: Benigno 2026-06-10] "Temporary shelter-related distortions associated with the October 2025 government shutdown have now largely passed through the CPI calculation process" by the May 2026 release — not previously documented anywhere in this wiki. This means shelter/OER readings from earlier in H1 2026 (Jan-Apr) may carry a shutdown-related artifact not yet audited in this node; treat pre-May H1 2026 shelter figures with that caveat until independently checked against BLS methodology notes.

**Policy context — Warsh's first CPI report as Fed Chair:** [RAW-CLIP: Benigno 2026-06-10] This was the first CPI release of Kevin Warsh's tenure as Fed Chair, ahead of the June FOMC meeting. The source describes Fed communication as framing the inflation overshoot as "primarily a supply-driven phenomenon" (energy + tariffs, not demand), consistent with the "deliver price stability" hawkish-but-non-demand-driven framing already documented below in Policy Response Linkage. No dedicated wiki node yet exists for Warsh's June FOMC/Sintra communication specifically — see [[Fed_Duration_Extraction_Term_Premium]] for the closest existing treatment; ingesting the Warsh-specific clips is a separate task.

### PPI (headline, verified via BLS release text after a series-ID correction — see below)
[WEB-2026-06-11:bls.gov/news.release/ppi.nr0.htm] Final demand +1.1% MoM SA (May), +6.5% YoY NSA (largest since Nov 2022). Final demand goods +2.8% MoM — largest since the FD-ID series began (Dec 2009), **80% traced to final-demand energy +10.7% MoM**. Core (ex food/energy/trade services) **+0.8% MoM — largest since March 2022**, a genuine broadening signal beyond pure energy pass-through.

### PPI stage-of-processing (Table D, independently pulled — see [[PPI_Stage_Differential_IO_Cascade_Diagnostic]])
Stage-1 (upstream) YoY accelerated from 4.22% (Jan) to 12.26% (May); Stage-4 (near-final) moved 4.05%→6.53% over the same window — the widening gap (+0.16pp → +5.73pp) is the empirical basis for the IO-cascade diagnostic in the companion mechanism node.

## Three Distinct Drivers — Not One Story

1. **Energy/Hormuz shock** [WEB-2026-04:eia.gov | worldbank.org] — Middle East military action Feb 28, 2026 → de facto Strait of Hormuz closure (~35% of global seaborne crude) → ~10mb/d initial supply reduction → Brent $61→$118/bbl in one quarter (largest inflation-adjusted quarterly move since 1988). This is the near-entire explanation for headline running ~1.3-1.4pp above core on both CPI and PCE — a single identifiable supply event, not broad-based demand inflation.
2. **Tariff pass-through** [RAW-OFFICIAL: FOMC minutes 2026-01-28, 2026-03-18, 2026-04-29] — FOMC staff explicitly attribute elevated **core goods** inflation "largely" to tariff effects, while core services/housing inflation declined over the same period, partially offsetting. Narrower and separate from the energy channel.
3. **Producer-level broadening** [WEB-2026-06-11:bls.gov] — core PPI (ex food/energy/trade) accelerating to +0.8% MoM (fastest in 3+ years) and the Stage-1/Stage-4 gap widening independently of the CPI/PCE core measures, which remain comparatively moderate (+0.2-0.4% MoM range). This is a leading-indicator divergence, not yet visible in final consumer prices — see [[PPI_Stage_Differential_IO_Cascade_Diagnostic]] for the diagnostic built around it.

## Methodological Note — Series-ID Correction

An initial attempt to reconstruct PPI final-demand MoM directly from guessed FD-ID series codes (WPSFD49207 and related) produced a materially wrong number (+2.63% vs. the official +1.1%) because the guessed codes did not correspond to BLS's actual "Final Demand" aggregation series. This was caught by cross-checking against BLS's own published release text rather than trusting an unconfirmed series pull — the corrected, verified numbers are used throughout this node. The same discipline (confirm the series documentation before pulling, cross-check against a second source) was applied successfully to the Table D stage-of-processing codes used in [[PPI_Stage_Differential_IO_Cascade_Diagnostic]].

## Policy Response Linkage

[RAW-OFFICIAL: FOMC minutes + June 17, 2026 SEP materials] The Fed dropped its previously-indicated rate cut and adopted "deliver price stability" language after 5 years above the 2% target, signaling possible hike risk. This is the mechanism-level explanation for the H1 2026 bear-flattening (2s10s narrowing, front-end-led) and rising ACM term premium already documented in [[Fed_Duration_Extraction_Term_Premium]] — the yield-curve research had the empirical move but not the causal driver; this inflation data supplies it.

## Related

- [[PPI_Stage_Differential_IO_Cascade_Diagnostic]] — the leading-indicator diagnostic built on this node's PPI stage data; note the May-26 CPI clip contains no PPI content, so it doesn't interact with this diagnostic directly
- [[Fed_Duration_Extraction_Term_Premium]] — the H1 2026 hawkish pivot and term-premium move this data helps explain; also the closest existing treatment of the June FOMC that Warsh chaired as new Fed Chair
- [[Headline_vs_Core_Inflation_Targeting]] — the general credibility/controllability trade-off this episode is a live case of
- [[GDP_Deflator_vs_CPI]] — adjacent price-index measurement-choice node
- [[Japan_May_2026_CPI_Report]]
- [[Japan_Inflation_Three_Force_Decomposition]]
- [[Currency_Substitution_Dollarization]]
- [[Inflation_Taxonomy]]
- [[US_Treasury_Balance_Sheet_H1_2026]]
