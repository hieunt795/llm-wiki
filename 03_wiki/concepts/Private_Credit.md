---
title: Private Credit
aliases:
- Private Debt
- Direct Private Lending
- Non-bank Corporate Lending
type: definition
tags:
- private-credit
- fixed-income
- alternative-assets
- shadow-banking
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: Private credit is non-bank corporate lending lacking a robust secondary market—a
  fundamental feature determining its return premium and risk profile, structurally
  positioned to fill the financing gap left by post-crisis bank retrenchment.
source_refs:
- file: Deep Dive_ Private Credit.md
  page: 1
- file: IMF GFSR Chapter 2, April 2024.pdf
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
---

## Thesis

Private credit encompasses debt financing negotiated directly between a non-bank lender and a borrower, bypassing public markets and syndication mechanisms. The lack of a robust secondary market is not an incidental flaw but the defining structural feature of this asset class. This illiquidity is the primary source of its yield premium and fundamentally dictates its valuation (mark-to-model) and systemic risk profile.

## Definition

Rather than a simple alternative investment, private credit is best understood mathematically and macroeconomically as the product of the **intersection of post-GFC financial repression and bank capital constraints**. ZIRP (Zero Interest Rate Policy) compressed yields across the public bond stack, while Basel III increased the shadow price of bank balance sheets for speculative corporate credit. The combination created a systemic supply-demand gap that non-bank lenders systematically exploited.

### BIS Taxonomy

| Category | Characteristic | Default Risk Profile |
|---|---|---|
| **Direct Lending** | Cash-flow lending, covenant-heavy, floating-rate | Lowest (typically senior secured) |
| **Mezzanine** | Junior/subordinated debt + equity participation | Medium–High |
| **Asset-Based Lending** | Collateral-driven (hard assets) | Dependent on collateral value |
| **Distressed** | Secondary market purchases of distressed debt | Highest |

> [!NOTE]
> This stratification is critical: asset-based lending unwinds differently than cash-flow lending during a crisis; mezzanine tranches will not behave like senior secured debt when sponsor support evaporates.

### Boundaries / Conditions

### Operating Characteristics & Risks

1. **Mark-to-Model Valuation:** Unlike public markets, private credit lacks daily secondary market price discovery. Valuations rely on internal models executed infrequently, masking volatility and allowing non-linear risk accumulation.
2. **Floating-Rate Mechanics:** Most loans are floating. Cash flows and borrower debt-service burdens are directly sensitive to central bank policy rates, removing duration risk for the lender but amplifying credit risk.
3. **Borrower Profile:** Typically mid-market, highly leveraged entities—structurally riskier than public high-yield issuers but too small to access broad capital markets.

> [!CAUTION]
> **The Macro-critical Paradox:** Basel III made the banking system safer but pushed risk into a less transparent sector. IMF (2024) warns that private credit's opaque interconnectedness could amplify future macroeconomic shocks.

### Necessary and Sufficient Conditions for Growth

**Necessary Conditions (The Drivers):**
1. **Regulatory Shock (Basel III/IV):** Forced banks to retreat from capital-intensive, lower-margin segments. See [[Basel_III_Impact_On_Private_Credit]].
2. **Persistent Credit Demand:** Middle-market capital needs persisted despite bank retreat, creating a massive financing gap.

**Sufficient Conditions (The Enablers):**
1. **Search for Yield:** During ZIRP, long-tail capital allocators (Pension Funds, Insurers) explicitly substituted liquidity for yield spread.
2. **Institutionalization:** The emergence of mega-managers (e.g., Blackstone, Apollo) capable of industrial-scale origination and distribution.

## Evidence / Source Anchors

- **Global Size (2023):** ~$2.1 trillion (including dry powder), growing ~20% annualized over 5 years: [[IMF GFSR Chapter 2, April 2024.pdf#page=1]]
- **Regional Breakdown:** North America ~$1.6T; Europe ~$460B; Asia ~$114B: [[IMF GFSR Chapter 2, April 2024.pdf#page=1]]
- **US Market Share:** Accounts for ~7% of non-financial corporate credit, rivaling syndicated loans and high-yield bonds: [[Deep Dive_ Private Credit.md#page=1]]
- **Concentration:** ~70% of deals are PE-sponsored; major PE managers hold >75% of private credit AUM: [[IMF GFSR Chapter 2, April 2024.pdf#page=1]]

## Related

- [[Direct_Lending]] — Largest sub-category
- [[Business_Development_Company]] — Primary public wrapper
- [[Financial_Repression]] — Macro regime driving demand
- [[Nonbank_Financial_Intermediation]] — Parent taxonomy
- [[Private_Credit_Reflexive_Loop]] — Self-reinforcing mechanics
- [[Search_For_Yield_Channel]] — Institutional capital flow mechanism
- [[Basel_III_Impact_On_Private_Credit]] — Bank retreat causation
- [[Fiscal_Dominance]] — Structural macro condition generating persistent negative real rates.
