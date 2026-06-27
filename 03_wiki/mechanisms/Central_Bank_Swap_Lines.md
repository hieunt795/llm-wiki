---
title: Central Bank Swap Lines
aliases:
- Central Bank Liquidity Swaps
- USD Liquidity Swap Lines
- FX Swap Lines
- Đường dây hoán đổi tiền tệ
type: mechanism
tags:
- central-banking
- liquidity-management
- fx
- monetary-policy
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Federal Reserve | BIS | Alexandru-Stefan Goghie [RAW-CLIP]
thesis: Central Bank Swap Lines are standing or temporary facilities between central
  banks designed to provide foreign currency liquidity (primarily USD) to local financial
  systems during periods of market stress, functioning as a systemic stabilizer to
  prevent forced asset liquidations and maintain global financial stability.
source_refs:
- file: I need a dollar (through your swap line).md
  label: '[RAW-CLIP]'
- file: Perry_Central_Bank_Policy_P3.md
  page: 250
created: '2026-04-28'
updated: '2026-04-28'
---

## Thesis

Beyond providing liquidity to foreign banks, USD swap lines function as a **systemic stabilizer for the US Treasury (UST) market**. By providing an alternative to selling liquid assets, the Fed prevents a feedback loop where global dollar shortages force foreign central banks to dump Treasuries, which would spike US yields and destabilize domestic financial conditions. [RAW-CLIP: Goghie]

---

## 1. Mechanism: The "Collateralized" Exchange

A swap line is structured as a two-legged transaction between the Federal Reserve and a Foreign Central Bank (FCB):

1.  **Leg 1 (Spot):** The Fed provides USD to the FCB in exchange for an equivalent amount of the FCB's currency (e.g., EUR, JPY) at the prevailing market exchange rate.
2.  **Lending:** The FCB then lends these dollars to its domestic commercial banks through local repo or auction facilities.
3.  **Leg 2 (Forward):** On a predetermined date, the transaction is reversed at the **same exchange rate** used in Leg 1. The FCB returns the USD plus interest, and the Fed returns the foreign currency.

**Key Feature:** The Fed bears no exchange rate risk, as the reversal rate is fixed at the start. The FCB assumes the credit risk of its domestic commercial banks.

---

## 2. Strategic Logic: Preventing Forced Asset Sales

A critical insight from the 2020 COVID-19 shock and the 2026 analysis [RAW-CLIP: Goghie] is the link between **FX Swap Markets** and the **UST Market**:

- **The Problem:** When the [[Cross_Currency_Basis]] becomes extremely negative, foreign banks cannot fund their USD assets through private swaps.
- **The Forced Move:** Without swap lines, foreign central banks must draw down reserves to provide USD. This often requires selling their most liquid assets—**US Treasuries**.
- **The Contagion:** Mass selling of Treasuries by foreign official institutions spikes yields, increasing borrowing costs for the US government and private sector, effectively importing global instability into the US domestic core.
- **The Solution:** Swap lines allow FCBs to obtain USD without selling USTs, acting as a "synthetic repo" facility for the global dollar system.

---

## 3. Geopolitical Dimension: Petroyuan vs. Petrodollar

In the modern context (2026), swap lines are part of the **institutional integration** of the dollar system:
- **Selectivity:** The Fed maintains standing swap lines with a "core" group (ECB, BoJ, BoE, BoC, SNB).
- **The UAE Case:** Expanding swap lines to strategic partners like the UAE signals a commitment to mutual financial stability and anchors these economies to the USD infrastructure, counteracting the rise of the **Petroyuan** and commodities cooperation with China. [RAW-CLIP: Goghie]

---

## 4. Comparison: Swap Lines vs. FIMA Repo Facility

| Feature | Swap Lines | FIMA Repo Facility |
| :--- | :--- | :--- |
| **Counterparty** | Select Central Banks | Wide range of Foreign Official Institutions |
| **Collateral** | Foreign Currency | US Treasuries |
| **Credit Risk** | Shared / Reciprocal | None (fully collateralized by UST) |
| **Signaling** | Strong institutional integration | Purely operational liquidity tool |

## Evidence / Source Anchors

- [RAW-CLIP] Swap lines as UST market stabilizers: [[I_need_a_dollar_through_your_swap_line.md]]
- [RAW-BOOK] Mechanics of standing facilities: [[Perry_Central_Bank_Policy_P3.md#page=250]]
- [RAW-CLIP] Geopolitical anchor against Petroyuan: [[I_need_a_dollar_through_your_swap_line.md]]

## Related

- [[Cross_Currency_Basis]] — The market signal that triggers swap line activation.
- [[Petroyuan_Vs_Petrodollar]] — The geopolitical competition for currency dominance.
- [[Treasury_General_Account_Mechanism]] — Impact of global flows on US fiscal accounts.
- [[Lender_Of_Last_Resort]] — The Fed's role in the global dollar system.
