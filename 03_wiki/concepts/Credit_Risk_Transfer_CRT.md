---
title: Credit Risk Transfer (CRT)
aliases:
- CRT
- Connecticut Avenue Securities
- CAS
- Structural Agency Credit Risk
- STACR
- GSE Credit Risk Transfer
type: concept
tags:
- mbs
- credit-risk
- market-infrastructure
- gse
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat"
provenance: Tuckman_Serrat_2022.md
thesis: Credit Risk Transfer (CRT) securities are debt instruments issued by GSEs
  (Fannie Mae and Freddie Mac) to shift mortgage default risk from their balance sheets
  to private investors, utilizing a synthetic structure where principal write-downs
  are tied to the performance of a reference pool.
source_refs:
- file: Tuckman_Serrat_2022.md
  page: 428
- file: Tuckman_Serrat_2022.md
  page: 429
- file: Tuckman_Serrat_2022.md
  page: 430
created: '2026-04-20'
updated: '2026-04-22'
---

## Thesis

Following the 2008 financial crisis, the GSEs were mandated to reduce taxpayer exposure to mortgage defaults. **Credit Risk Transfer (CRT)** programs—specifically **Connecticut Avenue Securities (CAS)** at Fannie Mae and **Structural Agency Credit Risk (STACR)** at Freddie Mac—allow the GSEs to sell a "vertical slice" and "horizontal tranches" of default risk to private markets while retaining the underlying mortgages or guarantees. [[Tuckman_Serrat_2022.md#page=428]]

## Structural Mechanism

### 1. The Reference Pool
Unlike standard MBS, CRT notes are not collateralized by the mortgages. Instead, they reference a pool of conforming loans. The loans remain on the GSE's balance sheet or in traditional MBS trusts. The CRT notes are debt obligations of the GSE (or a trust) whose principal repayment depends on the loss experience of this reference pool. [[Tuckman_Serrat_2022.md#page=429]]

### 2. Cash Flow Engineering
- **Issuance:** Investors buy notes at par. Proceeds are deposited into a trust.
- **Coupon:** Investors receive a spread over a short-term rate (originally LIBOR, now SOFR). This is funded by the interest on trust assets plus "g-fees" contributed by the GSE.
- **Principal Return:** Tied to the voluntary principal payments (scheduled and prepayments) of the reference pool. As the pool amortizes, the CRT notes are paid down sequentially. [[Tuckman_Serrat_2022.md#page=429]]

## Tranche Hierarchy & Loss Allocation

CRTs employ a reverse-waterfall for loss absorption, similar to [[ABS_Tranching_And_Default_Risk|CLO structures]]:

| Class | Credit Support | Role |
| :--- | :--- | :--- |
| **Class A** | High (e.g. 4%) | Senior (Fictional/Retained). Absorbs voluntary principal first. |
| **Class M1/M2** | Intermediate | Mezzanine (Sold to Investors). Bearing moderate default risk. |
| **Class B1** | Low | Junior (Sold to Investors). Bearing high default risk. |
| **Class B2** | First-Loss (0%) | Equity (Retained by GSE). Absorbs the first 20-25 bps of losses. |

- **Loss Mechanism:** If defaults in the reference pool exceed the threshold of the junior-most retained tranche (B2), the principal of the next tranche (B1) is written down. This continues up the capital stack (M2, then M1).
- **Alignment of Interest:** The GSE retains the first-loss tranche (Horizontal slice) and typically 5% of each sold tranche (Vertical slice/Skin-in-the-game) to align interests with private investors. [[Tuckman_Serrat_2022.md#page=430]]

## Risk vs. Reward Profile

- **For Investors:** Offers higher yields than standard agency MBS (which have zero credit risk for the investor). It allows specialized credit funds to take a pure view on US residential mortgage performance.
- **For GSEs:** Reduces capital requirements by transferring catastrophic credit risk to the private sector.

## Related

- [[Securitization_And_Asset_Based_Finance_ABF]] — The broader category.
- [[Residential_Mortgage_Backed_Securities_RMBS]] — The underlying asset class.
- [[ABS_Tranching_And_Default_Risk]] — The general mechanics of waterfalls.
- [[Credit_Risk_Taxonomy]] — Where CRT fits in risk management.
- [[Significant_Risk_Transfer]]
- [[Credit_Ratings_And_Migration]]
