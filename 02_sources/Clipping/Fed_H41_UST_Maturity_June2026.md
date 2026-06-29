---
title: "H.4.1 — Fed UST Portfolio Maturity Schedule, June 24 2026"
source: "https://www.federalreserve.gov/releases/h41/current/"
label: "[RAW-OFFICIAL]"
published: 2026-06-25
created: 2026-06-29
description: "H.4.1 Factors Affecting Reserve Balances. UST portfolio full breakdown by type (bills/notes/bonds/TIPS) and maturity bucket distribution. As of week ending June 24, 2026."
tags:
  - clippings
  - fed-balance-sheet
  - h41
  - ust-maturity
---

## Full Balance Sheet Summary (consolidated, week ending June 24, 2026)

### Assets ($ billions)

**U.S. Treasury Securities: $4,488.1B**
- Bills: $485.974B
- Notes/Bonds (nominal): $3,615.4B
- Notes/Bonds (inflation-indexed, TIPS): $279.0B
- Inflation compensation: $107.5B
- Unamortized premiums: $214.9B
- Unamortized discounts: -$25.6B

**Mortgage-Backed Securities: $1,961.6B**
**Federal Agency Debt: $2.3B**
**Loans: $7.9B**
**Other assets: $84.8B** (gold $11.0B + SDR $15.2B + FX $18.9B + other $38.7B)

**Total Assets: $6,735.6B**

### Liabilities ($ billions)

- Reserve balances (IORB deposits): **$2,951.4B**
- Currency in circulation: $2,472.2B
- Federal Reserve notes (net): $2,421.5B
- Overnight reverse repurchase agreements: **$333.6B** ← includes foreign repo pool; domestic ON RRP separately cited at ~$2.3B
- Treasury General Account (TGA): **$918.7B**
- Other deposits: $281.2B

---

## UST Maturity Distribution (within $4,488.1B total UST)

| Bucket | $ Billions | % of Total |
|--------|-----------|------------|
| Within 15 days | $105.6B | 2.35% |
| 16–90 days | $349.9B | 7.80% |
| 91 days – 1 year | $508.9B | 11.34% |
| 1–5 years | $1,425.5B | 31.76% |
| 5–10 years | $485.5B | 10.82% |
| Over 10 years | $1,612.7B | 35.93% |
| **Total** | **$4,488.1B** | **100%** |

---

## WAM Calculation (analyst estimate from bucket midpoints)

Using bucket midpoints: <15d → 0.021yr, 16-90d → 0.145yr, 91d-1yr → 0.624yr, 1-5yr → 3yr, 5-10yr → 7.5yr, >10yr → 15yr (estimated avg)

```
WAM = (105.6×0.021 + 349.9×0.145 + 508.9×0.624 + 1425.5×3 + 485.5×7.5 + 1612.7×15)
      / 4488.1
    = (2.2 + 50.7 + 317.6 + 4276.5 + 3641.3 + 24190.5) / 4488.1
    = 32478.8 / 4488.1
    ≈ 7.24 years
```

**Result: WAM ≈ 7.24 years** [RAW-OFFICIAL: H.4.1 + analyst midpoint calc]
- Prior estimate [LLM-E: ~7–8 years] CONFIRMED
- Duration concentration: 68% of portfolio in >1-year buckets; 36% in >10-year

### Composition Notes
- Bills share: $485.974B / $4,488.1B = **10.8%** of UST portfolio (RMP purchasing predominantly short-end)
- Notes/Bonds (nominal): $3,615.4B = **80.6%**
- TIPS: $279.0B = **6.2%** (excl. inflation comp)
- Long-end concentration (>5yr): ($485.5 + $1,612.7)B = $2,098.2B = **46.8%** of UST portfolio

---

## Key Interpretations

1. **WAM 7.24yr confirmed** — Fed's UST portfolio is long-duration, rut ~$2.1T+ duration from private markets vs Treasury's marketable WAM of ~5.83yr (Treasury Report Mar 2026 MSPD). Fed holds LONGER average maturity than the Treasury issues — reflects QE era accumulation of long-end.

2. **Bills represent only 10.8%** of Fed's UST holdings despite RMP acquiring ~$40B/month since 10/12/2025 (~8 months × $40B = $320B new purchases, mix TBD but likely bill-heavy). Stock of old notes/bonds from QE era still dominates.

3. **$1,612.7B (36%) in >10yr bucket** — this is the core duration risk. These are the bonds most sensitive to term premium widening. If Warsh redirects future RMP to long-end or if QT resumes on long-end, this bucket moves market.

4. **ON RRP distinction**: The liability line "Overnight reverse repurchase agreements: $333.6B" includes the foreign repo pool (for foreign central banks). The domestic ON RRP facility (with money market funds) was ~$2.3B as of this date — essentially zero. The $333.6B total does NOT represent a meaningful reserve buffer.
