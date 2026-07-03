---
title: "PPI Stage-Differential Diagnostic (IO Cascade Detection)"
aliases:
- Stage Differential
- IO Cascade Diagnostic
- Nonlinear Inflation Stage Gap
- Benigno Stage Gap
type: mechanism
tags:
- inflation
- ppi
- supply-chain
- io-cascade
- producer-prices
- macro
status: reviewed
confidence: 3
half_life_years: 1
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Gianluca Benigno (ex-FRBNY) | BLS Table D"
provenance: "RAW-CLIP: Benigno 2026 3-part substack series; cross-verified against RAW-OFFICIAL BLS Table D (WPUID51-54) 2026-07-03"
thesis: When a supply shock exceeds production-network buffer capacity, a PPI stage
  differential (Stage-1 YoY minus Stage-4 YoY, BLS Table D) crossing an author-proposed
  threshold τ*≈+3pp flags upstream-to-downstream IO-cascade cost diffusion before
  it reaches final consumer prices — a real-time detection device, not a forecast,
  per a short-sample single-analyst framework independently verified against primary
  BLS data for the 2026 Hormuz episode.
source_refs:
- file: "Benigno_Nonlinear_Inflation_IO_Cascade_2026.md"
- file: "US_CPI_PPI_PCE_H1_2026_BLS_BEA.md"
created: '2026-07-03'
updated: '2026-07-03'
---

# [[PPI_Stage_Differential_IO_Cascade_Diagnostic]]

## Thesis
[RAW-CLIP: Benigno 2026] Large supply-chain disruptions can generate cost cascades through the production network (input-output structure), distinguishable from ordinary energy-price volatility by a stage differential that crosses an empirically-derived threshold. [RAW-OFFICIAL: BLS Table D, independently reproduced 2026-07-03] The diagnostic's headline numbers for the 2026 Hormuz episode are verified against primary BLS data, though the threshold itself and the correlation it implies remain a single-analyst, short-sample construct — a detection device, not a forecasting tool, by the author's own description.

## Transmission Chain

```
Supply-chain chokepoint (e.g. Hormuz closure)
  →[buffer capacity exceeded — top-decile disruption]→
Stage 1 upstream input cost ↑ (raw/crude extraction)
  →[IO pass-through, weeks-to-months, non-nested stage weights]→
Stage 2-3 intermediate manufacturing cost ↑
  →[cost-absorption limit reached at each node]→
Stage 4 near-final producer cost ↑
  →[qualitative, UNQUANTIFIED lag — see §5]→
CPI / PCE ↑
  →[behavioral amplifier: tight labor market + prior inflation experience]→
Core inflation persistence
```

## 1. The Stage-of-Processing System (BLS Table D)

[RAW-OFFICIAL: BLS PPI Intermediate Demand by Production Flow] BLS's "Intermediate Demand by Production Flow" table organizes producer prices into four sequential stages — Stage 1 (raw/upstream extraction) through Stage 4 (near-final goods and services producers). Each stage index tracks prices of **inputs consumed** by industries at that stage, not their outputs, forming a forward-flow model of production. [RAW-CLIP: Benigno Part II] Stages are explicitly **not nested**: individual commodities (diesel, electricity, steel) appear across multiple stages simultaneously at different weights, so the stages are not a strict subset hierarchy.

Series IDs (NSA): Stage 1 = `WPUID51`, Stage 2 = `WPUID52`, Stage 3 = `WPUID53`, Stage 4 = `WPUID54` (SA equivalents use `WPS` prefix). These were confirmed by locating BLS's own Table D documentation before pulling — an earlier attempt to guess Final-Demand/Intermediate-Demand series codes for a separate (headline PPI) analysis produced a wrong series and a materially incorrect number, corrected via BLS's official release text rather than repeated guessing. See [[US_CPI_PPI_PCE_H1_2026]] for that correction.

## 2. The Stage-Differential Diagnostic

[RAW-CLIP: Benigno Part II] Diagnostic metric: **Δ(t) = Stage-1 YoY − Stage-4 YoY**.
- **τ* ≈ +3pp** — proposed threshold above which a positive gap indicates genuine IO-cascade diffusion rather than isolated energy-price volatility. Below τ*, a positive gap "typically reflects energy price volatility rather than a genuine supply-chain cascade."
- **Author's own hedge (verbatim, near-exact):** "the sample is relatively short... indicative rather than a robust statistical test... a classification and confirmation device, not a forecasting tool."
- **GSCPI correlation:** r ≈ 0.81 between the gap and the NY Fed's Global Supply Chain Pressure Index, **conditional on gap > τ***, over a Nov 2010–Apr 2026 sample, with a 5-6 month lead/lag. This is NOT an unconditional relationship — below the threshold the correlation is weak/absent by construction of the claim.
- **Confirming pattern:** Stage 3 YoY exceeding Stage 4 YoY (intermediate manufacturing outpacing near-final producers) is treated as secondary confirmation that upstream cost pressure is actively diffusing downstream, not stalled at the energy layer.

## 3. Why Oil Futures Are an Insufficient Statistic

[RAW-CLIP: Benigno Part I & Update] Markets and forecasters treat the crude oil futures price as a sufficient statistic for the inflation implication of a supply shock. This misses: (a) cumulative production-network costs from rerouted cargo and delayed inputs, (b) geographic price differentials (e.g. European TTF gas, LNG re-routing spreads) not captured in crude benchmarks, and (c) continued cascade propagation even after the crude price itself normalizes.

**2026 evidence of price/physical decoupling:** Brent crude fell ~18% from its March 2026 peak, yet the "Hormuz Transit Stress Index" [RAW-CLIP: Benigno's own construction, methodology not detailed] sits at +3.7σ — an all-time high in the sample. Vessel transits through the strait collapsed from ~80/day to 4/day, tonnage from ~4M to ~0.1M tonnes/day, and **both have been flatlined for three months** even as the spot oil price partially reversed. Price and physical disruption have decoupled.

## 4. 2026 H1 Verification — Independently Reproduced Against Primary BLS Data

[RAW-OFFICIAL: BLS API `api.bls.gov/publicAPI/v2`, FRED mirror `fredgraph.csv`, pulled 2026-07-03] Recomputed the stage-gap trajectory directly from `WPUID51`/`WPUID54` (BLS API for Jan-Mar, FRED mirror for all months after the BLS daily query quota was exhausted mid-session):

| Month 2026 | Stage 1 YoY | Stage 4 YoY | Gap (computed) | Gap (Benigno's reported) |
|---|---|---|---|---|
| Jan | 4.22% | 4.05% | +0.16pp | — |
| Feb | 5.05% | 4.43% | +0.63pp | — |
| Mar | 6.54% | 4.47% | **+2.07pp** | "+2.0pp" |
| Apr | 8.92% | 5.39% | **+3.53pp** | "+3.5pp" (crosses τ*) |
| May | 12.26% | 6.53% | **+5.73pp** | "+5.8pp" |

The computed trajectory matches his cited reference points within ~0.1-0.3pp at every checkpoint he names — the headline diagnostic is confirmed from primary data, not taken on faith from a single substack. Stage 1 May month-on-month (+3.23% computed vs. his "+3.2%, largest since BLS began") and Stage 3 May YoY (7.20% computed vs. his "7.2%") match almost exactly.

**Discrepancy noted:** his reported April Stage 2 figure (7.1% YoY) diverges from the computed value (9.02% YoY) by ~1.9pp — plausibly a revision-timing artifact, since BLS revises PPI sub-indexes for up to 4 months after initial publication and he was writing on less-revised April data in early June. Not independently resolved.

**Nuance the framework doesn't surface:** the computed series is not a clean monotonic staircase (Stage1 > Stage2 > Stage3 > Stage4). In May, Stage 2 (12.49%) slightly exceeds Stage 1 (12.26%), and the sharpest break sits between Stage 2 (~12%) and Stage 3 (~7%) rather than a smooth four-step decay. This is consistent with — not contradictory to — the "narrow but deep" sectoral finding (§5 of the companion evidence node): the cascade is concentrated in the energy-petrochemical-freight corridor rather than diffusing evenly across all four stages.

## 5. The PPI→CPI Lag Claim — Explicitly Unquantified

[RAW-CLIP: Benigno Part I] "PPI moves first, fastest, and most significantly... CPI follows... core inflation responds last, most slowly, and most persistently" is asserted as a stylized fact with **no quantified lag estimate anywhere in the three-part series** and **no direct CPI data cited in Parts II or the Update** (both are PPI-internal only). The only illustration given is the 2021 used-car cascade (semiconductor shortage → vehicle production → CPI), which is an anecdote, not a measured lag. Do not cite a "6-12 month PPI-to-CPI lag" as an empirical finding of this framework — it is a generic prior, separate from the (independently verified) stage-differential diagnostic in §§2 and 4.

**Backing claim flagged as uncited:** the general "large shocks produce nonlinear, not proportional, dynamics" claim is attributed to unpublished research with two named former FRBNY colleagues and one University of Lausanne economist, covering 22 advanced economies 2000-2024 — no paper title, journal, or link is given anywhere in the series. This cannot be independently verified and should be treated as an asserted claim of the author's own prior work, not a citable external study.

## Failure Conditions / Boundaries

- **Single-source risk** [P2 red flag]: the interpretive framework (τ* threshold, GSCPI correlation, sectoral read) comes from one analyst; only the underlying BLS numbers are independently corroborated.
- **Short-sample threshold**: τ*≈+3pp was derived by splitting a short sample by gap size, not formal econometric estimation — author's own caveat.
- **Magnitude caveat**: 2026 episode remains well below COVID extremes (gap +5.8pp vs. 2021's +11.0pp; GSCPI <2σ vs. 4.47σ) and is sectorally narrower (energy-petrochemical-freight corridor vs. 2021's broad-based shock).
- **Explicit falsification conditions** (Benigno's own): the thesis weakens if Stage 3 stops outpacing Stage 4, or if Hormuz transit volumes resume — both should be monitored monthly per the 5-point protocol in the companion clipping.

## Evidence / Source Anchors

- Full data trajectory + BLS/BEA CPI/PCE anchors: [[US_CPI_PPI_PCE_H1_2026]]
- Raw clip (all 3 Benigno pieces, verbatim caveats): `02_sources/Clipping/Benigno_Nonlinear_Inflation_IO_Cascade_2026.md`
- Raw BLS/BEA data pull: `02_sources/Clipping/US_CPI_PPI_PCE_H1_2026_BLS_BEA.md`
- Fed hawkish-pivot linkage: [[Fed_Duration_Extraction_Term_Premium]]

## Related

- [[US_CPI_PPI_PCE_H1_2026]] — quantified CPI/PPI/PCE data this diagnostic sits alongside
- [[Headline_vs_Core_Inflation_Targeting]] — conceptual headline/core framework this episode stress-tests
- [[Fed_Duration_Extraction_Term_Premium]] — the hawkish pivot this cascade evidence helps explain
- [[GDP_Deflator_vs_CPI]] — adjacent price-index measurement-choice node
