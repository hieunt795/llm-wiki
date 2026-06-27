# Chapter 1 Evidence-Fit Audit

Audit date: 2026-04-23

Scope: Re-opened and read the current Chapter 1 source URLs to check whether each source supports the nearby paragraph/chart claim, rather than merely checking whether the URL is reachable.

## Findings

| Line | Source | Evidence fit | Reason |
|---:|---|---|---|
| 15 | CBO 2026 Budget and Economic Outlook PDF | Direct support | CBO states FY2026 deficit is $1.9 trillion and 5.8% of GDP; tables also provide historical/projected deficit data. |
| 18 | Bloomberg rates landing page | Proxy only | Supports public rates context, but does not verify Magnificent 7 free-cash-flow yield or the exact spread chart. |
| 21 | Morningstar research landing page | Proxy only | Relevant source family for fund flows, but no exact market-cap-tier inflow table was verified. |
| 24 | S&P 500 index page | Proxy only | Supports index data, but not the exact rolling breadth/outperformer statistic. |
| 41 | FactSet earnings research page | Proxy only | Correct source family for earnings estimates, but the exact 24.6% vs 15.9% claim needs a dated FactSet note. |
| 44 | PitchBook reports page | Proxy only | Relevant source family for private credit/leveraged finance, but no direct chart was verified. |
| 47 | Goldman Sachs insights page | Proxy only | Relevant source family for AI capex commentary, but no exact capex run-rate table was verified. |
| 50 | SIFMA Treasury securities statistics | Direct support for Treasury issuance/outstanding | SIFMA reports YTD 2026 Treasury issuance/trading/outstanding; T-bill share still requires using the downloadable table. |
| 67 | CBO 2026 Budget and Economic Outlook PDF | Direct support | CBO figure/table data covers total deficits, net interest outlays, and primary deficits. |
| 70 | Fed Financial Stability Report page | Proxy only | Official source family for financial-stability vulnerabilities, but not the exact SLR-headroom-vs-Treasury-market chart. |
| 73 | Preqin insights page | Weak proxy | Page is JavaScript-gated in audit environment and does not verify exact BDC liquidity-buffer claim. |
| 76 | BIS Quarterly Review March 2026 | Proxy only | Official source family for market plumbing/NBFI topics, but exact Cayman basis-trade leverage chart was not verified. |
| 93 | PGPF analysis page | Proxy only | Relevant for debt/interest commentary; CBO is stronger direct support for net interest and defense outlays. |
| 96 | FRED search page | Constructed proxy | No single direct series verifies r-minus-g; chart must combine CBO/FRED series. |
| 99 | Cboe VIX page | Proxy only | Supports VIX product/index context, not the asserted structural floor or volatility surface. |
| 102 | NY Fed reference rates | Partial direct support | Supports SOFR/reference rates, but not OIS spread or repo margin haircuts. |
| 119 | FRED RRPONTSYD | Direct support | FRED reports ON RRP at $0.538 billion on 2026-04-22, consistent with near-zero depletion. |
| 122 | Federal Reserve H.4.1 | Partial direct support | Supports reserve balances; LCLoR estimate needs separate research support. |
| 125 | DTCC data services | Proxy only | Relevant DTCC source family, but exact sponsored-vs-bilateral repo volume series was not verified. |
| 128 | Bloomberg rates landing page | Proxy only | Supports public market-rate context, but exact 10Y-vs-SOFR depletion chart should be reconstructed from public series. |

## Resulting Edits

- Added `Evidence fit` notes below every Chapter 1 chart source.
- Renamed charts whose previous titles implied an exact verified dataset when only a proxy source was available.
- Preserved direct claims where CBO, SIFMA, FRED, or Fed sources directly support them.
- Flagged constructed/proxy charts explicitly so they are not mistaken for exact sourced charts.

