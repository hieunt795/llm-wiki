---
title: "Treasury Bills Auction Results H1 2026 — Bid-to-Cover by Term"
source: "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/auctions_query"
label: "[RAW-OFFICIAL]"
published: 2026-06-29
created: 2026-07-02
description: "Treasury bill auction bid-to-cover ranges by term (4wk/8wk/13wk/17wk/26wk/52wk), comparing Jan-Feb 2026 vs June 2026 to test whether demand for the short end (>20% of marketable debt per TBAC) shows any deterioration."
tags:
  - clippings
  - treasury-auctions
  - bills
  - bid-to-cover
  - debt-management
---

## Bill Auction BTC Comparison: Jan–Feb 2026 vs June 2026

| Term | Jan–Feb 2026 BTC range | June 2026 BTC range | Offering size | Direction |
|------|------------------------|----------------------|----------------|-----------|
| 4-Week | 2.78–2.94 | 2.74–3.13 | $70–105B/auction | Stable/slightly wider range |
| 8-Week | 2.64–2.88 | 2.57–2.94 | $75–95B/auction | Stable |
| 13-Week | 2.71–3.30 | 2.32–2.79 | $89–92B/auction | **Softer** — top of range down ~50bp |
| 17-Week | 2.92–3.38 | 2.55–3.15 | $69–72B/auction | **Softer** — range shifted down |
| 26-Week | 3.03–3.09 | 2.51–2.76 | $77–79B/auction | **Softer** — clear downshift |
| 52-Week | 2.96 (Feb 17) | 3.34 (Jun 9) | $50B/auction | Stronger (single data point each) |

---

## Key Finding — Mild softening concentrated in intermediate bills (13–26 week), not across the curve

Unlike the note/bond auctions (BTC 2.30–2.99, no trend — see `Treasury_Auction_Results_H1_2026.md`), the **13-week, 17-week, and 26-week** bill auctions show a consistent downshift in bid-to-cover from Jan–Feb to June 2026 (roughly 30–50bp lower at both ends of the range). The very short end (4-week, 8-week) and the 52-week point are stable or stronger. This is consistent with TBAC's own May 2026 guidance [RAW-OFFICIAL: Treasury_Q2_2026_Refunding_Details.md] that bills now represent **>20% of marketable debt, above the 15–20% target range** — the intermediate-bill segment is where the oversupply from extraordinary-measures-era issuance (Jan–Apr 2026 debt ceiling episode) is landing, and where demand is showing the first (still mild) signs of price concession.

**Interpretation:** this does not contradict the note/bond finding that private absorption of $683B gross H1 supply is happening via price, not quantity distress — it locates *where* in the curve that price adjustment is most visible: the belly of the bills curve, not the long end (where ACM term premium is the operative gauge) and not the very short end (which remains supported by money-market demand for near-cash instruments).

## Data Gaps
- No explicit "tail" (high yield vs when-issued) data available via this API field set for bills, same limitation as notes/bonds
- Only Jan-Feb vs June comparison pulled — March/April/May bill-by-bill data not ingested (lower priority, trend direction already established from bookend comparison)
- 52-week bill has only one auction per period sampled — single-point comparison, weaker evidence than the weekly terms

## Cross-Reference
- Note/bond BTC → `Treasury_Auction_Results_H1_2026.md`
- Refunding strategy/TBAC bills guidance → `Treasury_Q2_2026_Refunding_Details.md`
- Flow-focused analysis → `2026-07-02_fed-balance-sheet-flow-mechanics-h1-2026.md` (06_publish)
