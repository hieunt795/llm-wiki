---
title: Stock vs. Flow Distinction
aliases:
  - Stock Flow Distinction
  - Flow Variable
  - Stock Variable
  - Other Changes in Assets
  - OCA
  - Opening Closing Balance Sheet
  - Valuation Effect
  - Stock Flow Bridge
  - Accumulation Identity
type: concept
tags:
  - macro
  - national-accounts
  - accounting
  - monetary-accounts
  - balance-of-payments
  - fiscal-policy
status: verified
confidence: 5
half_life_years: 20
school: ""
superseded_by: null
superseded_date: null
expert_lens: "IMF | Ouanes | Thakur | SNA 1993"
provenance: "IMF — Macroeconomic Accounting and Analysis in Transition Economies (1997), Ch.2, Ch.4, Ch.5"
thesis: A flow variable measures a transaction or quantity per unit of time (recorded during a period); a stock variable measures a quantity at a point in time; the two are connected by the three-part accumulation identity — Stock(t) = Stock(t-1) + Net Flows(t) + Other Changes in Assets(t) — where the OCA term (valuation effects, write-offs, volume changes) is the component most frequently omitted in practice, causing systematic mismeasurement of stock trajectories from flow data alone.
source_refs:
  - file: "Macroeconomic Accounting and Analysis IMF.md"
    page: 12
  - file: "Macroeconomic Accounting and Analysis IMF.md"
    page: 129
  - file: "Macroeconomic Accounting and Analysis IMF.md"
    page: 172
created: "2026-07-01"
updated: "2026-07-01"
---

# [[Stock_Flow_Distinction]]

## Thesis

[RAW] The SNA 1993 structures all macroeconomic accounts into two complementary layers: **flow accounts** (recording transactions during a period) and **balance sheets** (recording stocks of assets and liabilities at a point in time). The bridge between the two is not simply accumulation of flows — it also includes **Other Changes in Assets (OCA)**, which captures valuation effects and volume changes that alter stock positions without any corresponding transaction.

---

## 1. Core Definitions

| Concept | Definition | SNA Account |
|---|---|---|
| **Flow** | Quantity per unit of time — measured over a period. Records transactions between sectors. | Current, Capital, Financial accounts |
| **Stock** | Quantity at a point in time — measured at the beginning or end of a period. | Opening / Closing Balance Sheets |
| **OCA (Other Changes in Assets)** | Changes in stocks that are **not** flows (transactions): revaluations from price/FX changes, natural disaster destruction, reclassification, write-offs. | Other Changes in Assets Account (SNA) |

---

## 2. The Three-Part Accumulation Identity (Bridge Equation)

$$\underbrace{S_{t-1}}_{\text{Opening stock}} + \underbrace{F_t}_{\text{Net flows (transactions)}} + \underbrace{OCA_t}_{\text{Other changes}} = \underbrace{S_t}_{\text{Closing stock}}$$

**OCA has two sub-components:**
1. **Other changes in volume** — non-transaction, non-price changes (e.g., natural disasters destroy capital stock; reclassification of an entity across sectors)
2. **Revaluations (holding gains/losses)** — changes in the market value of existing assets/liabilities due to price or exchange rate movements, with no transaction occurring

**Why OCA is analytically critical:**  
Stock(t) ≠ Stock(t−1) + ΔFlows alone. In periods of significant exchange rate movement or asset price change, OCA can dominate the flow term — meaning stock trajectories derived purely from flow data will be systematically wrong.

---

## 3. Applications Across the Four Macro Accounts

### 3a. External Debt (Ch.4)

[RAW] The simplified debt stock equation:
$$D_t = D_{t-1} + B_t - A_t \tag{eq. 4.5}$$
where $B_t$ = disbursements (flow), $A_t$ = amortization (flow).

Full equation including OCA:
$$D_t = D_{t-1} + B_t - A_t + \underbrace{\Delta V_t}_{\text{Valuation (FX)}} + \underbrace{IA_t}_{\text{Interest capitalized}} - \underbrace{WO_t}_{\text{Write-offs}}$$

[RAW] "Debt at end of a given year is broadly equal to debt at end of previous year, augmented by net debt-creating flows — but this is only a rough approximation." The three OCA components frequently cause actual stock evolution to diverge materially from the flow-only estimate.

**Example:** A country with USD-denominated debt; domestic currency depreciates 10% → no new borrowing flow → but debt stock in domestic currency terms increases 10% through pure valuation (OCA).

### 3b. Monetary Survey (Ch.5)

[RAW] The monetary survey stock identity:
$$M2_t = NFA_t + NDA_t$$

Flow version:
$$\Delta M2 = \Delta NFA + \Delta NDA$$

**OCA in the monetary survey = OINb (Other Items Net of banking system):**

[RAW] *"ΔNFA should exclude valuation adjustments from exchange rate changes — these are recorded in OINb; NFA components in the monetary survey should be held at constant exchange rates to isolate transaction flows."*

Consequence: When the exchange rate depreciates, the domestic-currency value of foreign reserve assets rises. This is **not a flow** — it is OCA recorded in OINb. If not separated, ΔNFA will show a spurious increase, causing ΔNDA to appear negative (implying domestic credit contraction) when no such contraction occurred.

### 3c. Balance of Payments (BOP)

BOP is entirely a **flow account** — it records transactions between residents and nonresidents during a period. But it must reconcile with the International Investment Position (IIP), which is a **stock account** (analogous to balance sheet for the external sector):

$$IIP_t = IIP_{t-1} + \text{Financial account flows}_t + \text{Valuation changes}_t + \text{Other adjustments}_t$$

The reconciliation between the BOP financial account (flows) and the IIP (stock) is a standard data quality check.

### 3d. Government Fiscal (GFS)

GFS cash-basis framework records **flows**: revenues, expenditures, net lending/borrowing.  
But fiscal **stock** = public debt outstanding.

[RAW from Quasi_Fiscal_Operations] When the government assumes bank debt (recapitalization):
- **GFS cash basis:** No expenditure recorded at time of assumption — only future interest payments appear as flow expenditures.
- **Stock perspective:** The full present value of assumed liabilities immediately worsens the net worth of government (stock of liabilities rises) even though no fiscal flow is recorded in the current year.

→ True fiscal deterioration only visible through balance sheet (stock) analysis, not cash-flow (flow) analysis.

---

## 4. Analytical Priority Rules

| Question | Read which layer | Why |
|---|---|---|
| "How much deficit this year?" | **Flow** (GFS) | Period transaction |
| "Is debt sustainable?" | **Stock** (debt/GDP ratio) | Accumulated position |
| "Is CB expanding money?" | **Flow** (ΔNDA this period) | Transaction-based expansion |
| "Is the banking system liquid?" | **Stock** (M2, reserves at date) | Position at a point |
| "Did FX depreciation worsen debt?" | **OCA** (valuation, not flow) | No transaction — pure revaluation |
| "Did fiscal consolidation help?" | **Both**: flow (deficit fell) + stock (debt/GDP trajectory) | Flow improvement ≠ stock improvement if interest > primary surplus |

---

## 5. The Sustainability Trap — When Flow Looks Good but Stock Deteriorates

[LLM] The most common analytical error: reading flow improvement as stock improvement.

**Scenario:** Primary fiscal surplus = +1% GDP (flow improving). But:
- Interest on existing debt = 4% GDP (flow expenditure)
- GDP growth = 2%
- Overall deficit = 3% GDP → debt/GDP ratio still rising

The **flow** (primary balance) improved. The **stock** (debt/GDP) deteriorated. Sustainability requires comparing interest rate $r$ vs. growth rate $g$:

$$\Delta (D/Y) \approx (r - g) \cdot (D/Y) - \text{Primary Surplus (\% GDP)}$$

If $(r - g) > 0$ and Primary Surplus insufficient → stock grows despite flow improvement. This is the debt dynamics trap.

**Monetary analogue:** Sterilization improves the flow (ΔNDA reduced). But the CB balance sheet stock continues to expand (FR asset + T-bill liability both on balance sheet). Partial sterilization → stock of base money creeps up each cycle.

---

## 6. Treasury Insight

[LLM]

1. **OCA is where macro surprises hide.** Flow forecasts (deficit, credit growth, BOP) are manageable. But OCA is residual and frequently large — particularly in EMEs with managed exchange rates and foreign-currency debt. A 10% FX move in VN can shift the NFA stock by $8–10B without a single transaction flow.

2. **The S-I = CAB identity (flow) constrains but does not determine sustainability.** Sustainability is the stock question: can the accumulated current account deficit (= accumulated NFA outflows = IIP deterioration) be serviced? The flow identity says ex-post balance is guaranteed; it says nothing about whether the resulting stock trajectory is viable.

3. **For QFO analysis:** Never trust headline fiscal flow (GFS cash deficit) alone. Add: (a) CB quasi-fiscal losses (recurring), (b) contingent stock liabilities (guarantees, bank recaps), (c) unfunded pension obligations. The augmented fiscal deficit = flow + annualized OCA from hidden stock deterioration.

4. **The NDA ceiling in IMF programs operates on flows** (ΔNDA per quarter). But its purpose is to stabilize stocks (NFA, reserves). The chain: control the flow (NDA) → stabilize the stock (NFA) → support the peg. If OCA disrupts NFA (e.g., FX valuation) without any NDA flow change, the ceiling may appear compliant while the stock target is being breached.

---

## Related

- [[Monetary_Survey_Identity]] — stock and flow versions of M2 = NFA + NDA
- [[External_Debt_Stocks_and_Flows]] — debt stock equation with full OCA decomposition
- [[System_of_National_Accounts_SNA]] — SNA account structure (flow accounts + balance sheets)
- [[Flow_of_Funds_Framework]] — all-flow matrix; links to stocks through opening/closing balance sheets
- [[Macroeconomic_Accounting_Identities]] — S-I=CAB flow identity
- [[Quasi_Fiscal_Operations]] — QFO creates stock deterioration invisible in flow accounts
- [[GFS_Fiscal_Deficit_Measures]] — GFS cash basis is flow; debt stock is separate
- [[Money_Multiplier_IMF_Framework]] — multiplier affects flow (ΔNDA) but stock target (M2) is what matters
