# Concept Map — US May-26 CPI Inflation Report

Source: `02_sources/Clipping/US May-26 CPI Inflation Report.md` [RAW-CLIP: Benigno, published 2026-06-10]
Pipeline: W5_secondary_ingest.md — Phase A (Pre-flight & Classification)

## Classification

- Source type: substack commentary on official BLS CPI release, single named author, source URL present, published date present, tables sourced/attributed to BLS → **[RAW-CLIP]** confirmed.

## Claims Table

| Claim | Type | Has-citation | Risk Flag |
|---|---|---|---|
| Headline CPI 4.2% YoY (May) / 3.8% (Apr) / 4.0% forecast; 0.6% MoM n.s.a. (May) / 0.9% (Apr); 0.5% MoM s.a. (May) / 0.6% (Apr) | data | BLS | VERIFY-NUMBER |
| Core CPI 2.9% YoY (May) / 2.8% (Apr) / 2.9% forecast; 0.3% MoM n.s.a. (May) / 0.4% (Apr); 0.2% MoM s.a. (May) / 0.4% (Apr) | data | BLS | VERIFY-NUMBER (2.85% vs 2.9% — reconcile against existing node's independently-computed figure) |
| Core services (ex energy) 3.4% YoY (May) / 3.3% (Apr) | data | BLS | VERIFY-NUMBER |
| Core goods (ex food/energy) 1.1% YoY (May, Apr unchanged); 0.0% MoM n.s.a. (May) / 0.1% (Apr) | data | BLS | VERIFY-NUMBER |
| Shelter (rent of shelter) 3.3% YoY (unchanged); 0.4% MoM s.a. (May) / 0.6% (Apr) [note: clip also states 0.3% MoM s.a. later in body — internal inconsistency, flagged] | data | BLS | VERIFY-NUMBER |
| Supercore services (core services ex shelter) 3.7% YoY (May) / 3.5% (Apr); 0.5% MoM (unchanged) | data | BLS | VERIFY-NUMBER |
| Rent subcomponent 2.9% YoY (May) / 2.8% (Apr); OER 3.3% YoY (unchanged) | data | BLS | VERIFY-NUMBER |
| Gasoline +40.5% YoY; +7.0% MoM s.a. / +8.6% MoM n.s.a. | data | BLS | VERIFY-NUMBER |
| Apparel +4.8% YoY (tariff pass-through) | data | BLS | VERIFY-NUMBER |
| Energy >60% of monthly all-items increase | data | BLS (author computation) | CHECK-AGREE |
| October 2025 government-shutdown shelter-CPI distortion "now largely passed through" | contextual/methodological | none named | CHECK-AGREE (new, previously undocumented) |
| Kevin Warsh's first month as Fed Chair; June FOMC framing inflation as supply-driven (energy + tariffs, not demand) | policy/interpretive | Fed communication (paraphrased) | CHECK-AGREE |
| No PPI data of any kind in this piece (CPI-only release) | absence-of-data | n/a | CHECK-AGREE |

No claims flagged `CHECK-CONFLICT` — the core-CPI precision gap (2.85% computed vs. 2.9% official) is a methodology/rounding note, not a factual contradiction.

## Phase B — Adversarial Audit Results

| Claim group | Wiki search target | Result |
|---|---|---|
| Headline CPI 4.2% | `US_CPI_PPI_PCE_H1_2026` | **AGREE** — exact match. |
| Core CPI | `US_CPI_PPI_PCE_H1_2026` | **AGREE w/ precision note** — node's independently-computed 2.85% vs. clip's BLS-published 2.9%; both are legitimate readings of the same underlying data at different rounding/computation stages. Document both, no CONTRADICTION node. |
| Core services/goods split, shelter/OER, supercore, gasoline, apparel | `librarian.py search "core services goods CPI supercore shelter May 2026"`, `"apparel tariff pass-through CPI"` | **NEW** — no existing node covers this granularity (confirmed via Explore agent search, only hit was `US_CPI_PPI_PCE_H1_2026` itself at low score, no sub-component content present). |
| Oct-2025 shutdown distortion | wiki-wide grep + search | **NEW** — not found anywhere in the wiki. |
| Warsh / June FOMC | wiki-wide search | **CHECK-AGREE** — no dedicated Warsh-June-FOMC node exists yet; closest is `Fed_Duration_Extraction_Term_Premium` (cites June 17, 2026 SEP materials but doesn't name Warsh). Cross-link only; ingesting the standalone Warsh clips (`Warsh_FOMC_PressConf_20260617_And_Sintra.md`, `Warsh and the Fed's Balance Sheet.md`) is a separate future task — out of scope here. |
| PPI absence | `PPI_Stage_Differential_IO_Cascade_Diagnostic` | **AGREE (boundary note)** — this clip is CPI-only; no interaction with the PPI stage-differential diagnostic. |

## Disposition

No SPAWN, no CONTRADICTION, no PERSPECTIVE node warranted. Writeback: **UPDATE ×1** on `US_CPI_PPI_PCE_H1_2026` (see log.md).
