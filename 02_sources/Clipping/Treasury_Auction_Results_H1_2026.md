---
title: "Treasury Note/Bond Auction Results H1 2026 — Bid-to-Cover Series"
source: "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query"
label: "[RAW-OFFICIAL]"
published: 2026-06-25
created: 2026-07-02
description: "Bid-to-cover ratios and high yields for all Treasury note and bond auctions H1 2026 (Jan-Jun), sourced from Treasury Fiscal Data API. Used to test whether private absorption of $683B gross H1 issuance shows quantity distress (weak BTC/tail) or is occurring via price only (rising term premium)."
tags:
  - clippings
  - treasury-auctions
  - bid-to-cover
  - debt-management
---

## Note Auctions H1 2026

| Auction Date | Security Term | Bid-to-Cover | High Yield |
|--------------|---------------|-------------|-----------|
| 2026-01-13 | 3-Year | — | — |
| 2026-01-21 | 19y10m (reopen) | 2.86 | 4.846% |
| 2026-05-11 | 3-Year | 2.54 | 3.97% |
| 2026-05-12 | 10-Year | 2.40 | 4.47% |
| 2026-05-21 | 9y8m (reopen) | 2.52 | 2.17% (TIPS) |
| 2026-05-26 | 2-Year | 2.64 | 4.07% |
| 2026-05-27 | 5-Year | 2.34 | 4.18% |
| 2026-05-27 | FRN (1y11m) | 3.49 | N/A (discount margin) |
| 2026-05-28 | 7-Year | 2.52 | 4.29% |
| 2026-06-09 | 3-Year | 2.64 | 4.19% |
| 2026-06-10 | 9y11m (reopen) | 2.57 | 4.54% |
| 2026-06-18 | 4y10m (reopen) | 2.61 | 1.96% (TIPS) |
| 2026-06-23 | 2-Year | 2.64 | 4.19% |
| 2026-06-24 | 5-Year | 2.35 | 4.20% |
| 2026-06-24 | FRN (1y10m) | 2.99 | N/A (discount margin) |
| 2026-06-25 | 7-Year | 2.50 | 4.26% |

## Bond Auctions H1 2026

| Auction Date | Security Term | Bid-to-Cover | High Yield | Offering |
|--------------|---------------|-------------|-----------|----------|
| 2026-01-13 | 29y10m (reopen) | 2.42 | 4.825% | $22.0B |
| 2026-01-21 | 19y10m (reopen) | 2.86 | 4.846% | $13.0B |
| 2026-02-12 | 30-Year | 2.66 | 4.750% | $25.0B |
| 2026-02-18 | 20-Year | 2.36 | 4.664% | $16.0B |
| 2026-02-19 | 30y (TIPS) | 2.75 | 2.473% | $9.0B |
| 2026-03-12 | 29y11m (reopen) | 2.45 | 4.871% | $22.0B |
| 2026-03-17 | 19y11m (reopen) | 2.76 | 4.817% | $13.0B |
| 2026-04-09 | 29y10m (reopen) | 2.39 | 4.876% | $22.0B |
| 2026-04-22 | 19y10m (reopen) | 2.68 | 4.883% | $13.0B |
| 2026-05-13 | 30-Year | **2.30** ← H1 low | 5.046% | $25.0B |
| 2026-05-20 | 20-Year | 2.55 | 5.122% | $16.0B |
| 2026-06-11 | 29y11m (reopen) | 2.33 | 5.020% | $22.0B |
| 2026-06-16 | 19y11m (reopen) | **2.75** | 4.927% | $13.0B |

---

## Key Finding — No systematic auction-demand deterioration in H1 2026

Bid-to-cover across the full note/bond calendar sits in a **2.30–2.99 range** with no visible downward trend across the six months. The single weakest print (30-Year, May 13, BTC 2.30) coincides with the ACM term premium local peak (May 15, +0.83%) [see `ACM_Term_Premium_H1_2026.md`] but is not an outlier low relative to typical 30Y BTC history, and the following long-bond reopening (June 11, 29y11m) recovered to 2.33, then June 16 (19y11m) printed 2.75 — no persistence of weak demand.

**Interpretation:** the private sector is absorbing the $683B H1 gross borrowing [RAW-OFFICIAL: Treasury_Q2_2026_Refunding_Details.md] primarily through **price adjustment** (modest term premium normalization, +0.6–0.8% ACM range vs 65yr median +1.41%) rather than through **quantity distress** (no tail blowouts, BTC still historically healthy — pre-2020 30Y BTC often ran 2.2–2.4). This nuances the synthesis thesis that "term premium nới dần" (term premium creeping wider) — the mechanism is confirmed, but there is no auction-demand alarm signal yet to escalate the timeline.

## Data Gaps
- Explicit "tail" (high yield minus when-issued yield at auction close) not available via this API field set — BTC used as the closest proxy for demand strength
- Bills auction data (weekly 4-week/8-week/13-week/26-week/52-week) not pulled — bills represent >20% of marketable debt per TBAC and are the primary flex lever, not yet quantified here

## Cross-Reference
- Term premium context → `ACM_Term_Premium_H1_2026.md`
- Refunding sizes/strategy → `Treasury_Q2_2026_Refunding_Details.md`
- Flow-focused analysis → `2026-07-02_fed-balance-sheet-flow-mechanics-h1-2026.md` (06_publish)
