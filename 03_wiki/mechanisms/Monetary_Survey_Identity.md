---
title: Monetary Survey Identity and Money Aggregates
aliases:
  - Monetary Survey Identity
  - M1 M2 Definition
  - Broad Money Identity
  - NFA NDA Money
  - Monetary Approach BOP Identity
  - M2 NFA NDA
  - Domestic Credit Expansion BOP
  - NDA Ceiling IMF
  - Money Aggregates M1 M2 M3
type: mechanism
tags:
  - monetary-policy
  - banking
  - macro
  - monetary-accounts
  - balance-of-payments
status: verified
confidence: 4
half_life_years: 10
school: ""
superseded_by: null
superseded_date: null
expert_lens: "IMF | Ouanes | Thakur"
provenance: "IMF — Macroeconomic Accounting and Analysis in Transition Economies (1997), Ch.5"
thesis: The monetary survey identity M2 ≡ NFA + NDC + OINb (eq. 5.7) — expressing broad money as the sum of net foreign assets and net domestic assets of the banking system — is the definitional bridge between monetary accounts and the BOP, with the key corollary ΔNFA = ΔM2 − ΔNDA = CAB + ΔFI = −ΔRES (eq. 5.9) establishing that any excess of domestic credit expansion over money demand growth is reflected in a balance-of-payments deficit, which is the theoretical foundation for NDA ceilings in IMF adjustment programs.
source_refs:
  - file: "Macroeconomic Accounting and Analysis IMF.md"
    page: 172
created: "2026-07-01"
updated: "2026-07-01"
---

# [[Monetary_Survey_Identity]]

## Thesis

[RAW] The monetary survey — the consolidated balance sheet for the entire banking system — presents data on monetary and credit developments for the entire banking system. Its asset-liability identity expresses the stock of money as the sum of its external (NFA) and domestic (NDA) origins.

## 1. Money Aggregate Definitions

[RAW]

### Narrow Money (M1)

$$M1 = CY + DD$$

where:
- $CY$ = currency in circulation outside banks
- $DD$ = demand deposits in the banking system

### Broad Money (M2)

$$M2 = CY + DD + QM \tag{5.5}$$

where $QM$ = quasi-money = time and savings deposits (TD) + foreign currency deposits of residents. Formally:

$$M2 = CY + DD + TD$$

M2 covers the liabilities of the banking system, including foreign currency deposits of residents, certificates of deposit, and security repurchase agreements.

### Broader Aggregates

| Aggregate | Adds to M2 |
|---|---|
| **M3** | Wider range of instruments and issuing institutions (travelers checks, commercial papers, money market mutual funds) |
| **M4** | Liquid government securities, negotiable bonds, liabilities of other financial intermediaries |
| **L (Liquidity)** | Treasury bills, government bonds, mortgage bonds, some corporate bonds |

[RAW] The choice of monetary aggregate for policy is influenced by: (1) stability and predictability of the relationship between the aggregate and nominal aggregate demand; (2) degree to which the monetary authorities control the aggregate.

## 2. Monetary Survey Identity (eq. 5.6–5.8)

[RAW] The identity between assets and liabilities of the banking system implies:

$$M2 = NFA + NDA \tag{5.6}$$

Since $NDA = NDC + OIN_b$:

$$M2 = NFA + NDC + OIN_b \tag{5.7}$$

In terms of changes:

$$\Delta M2 = \Delta NFA + \Delta NDC + \Delta OIN_b \tag{5.8}$$

where:
- $NFA$ = net foreign assets of the banking system (valued in domestic currency)
- $NDA$ = net domestic assets = $NDC$ + $OIN_b$
- $NDC$ = net domestic credit = claims on government (net) + claims on private sector
- $OIN_b$ = other items net of banking system

**Growth rate decomposition (analogous to eq. 5.3–5.4 for reserve money):**

$$\frac{\Delta M2}{M2} = \frac{\Delta NFA}{NFA} \cdot \frac{NFA}{M2} + \frac{\Delta NDC_G}{NDC_G} \cdot \frac{NDC_G}{M2} + \frac{\Delta CPS}{CPS} \cdot \frac{CPS}{M2} + \frac{\Delta OIN_b}{OIN_b} \cdot \frac{OIN_b}{M2}$$

**For purposes of monetary analysis:** ΔNFA should exclude valuation adjustments from exchange rate changes — these are recorded in OINb; NFA components in the monetary survey should be held at constant exchange rates to isolate transaction flows.

## 3. Link to Balance of Payments (eq. 5.9)

[RAW] From the monetary survey: $\Delta NFA = \Delta M2 - \Delta NDA$.
From the BOP accounting identity: $CAB + \Delta FI + \Delta RES = 0$, and $\Delta NFA = -\Delta RES$ (increase in reserves = decrease in negative-sign ΔRES).

Therefore:

$$\Delta NFA = \Delta M2 - \Delta NDA = CAB + \Delta FI = -\Delta RES \tag{5.9}$$

[RAW] **Key implication:** Any excess of domestic credit expansion (ΔNDA) over the increase in money stock (ΔM2) is reflected in a **decline in net foreign assets** (ΔNFA < 0), i.e., a balance of payments deficit. This relation constitutes the basis of the **monetary approach to the balance of payments** and provides the theoretical justification for setting **ceilings on net domestic assets** in IMF-supported programs.

The change in NFA is positive (BOP surplus) if ΔM2 > ΔNDA — if the money stock grows faster than domestic credit, foreign assets accumulate.

## 4. Links Between Monetary Survey and Other Accounts

[RAW] The monetary survey highlights three essential links:

### Link to BOP (External)
As derived above (eq. 5.9): banking system NFA = BOP overall balance financing. Under fixed exchange rate (all banking system transactions below the line): the overall balance is financed by changes in the banking system's net international reserves.

### Link to Government Accounts (Fiscal)
Banking system net claims on the government (asset side of monetary survey) = banking system's net lending to finance government deficits. When the fiscal deficit is monetized (financed through CB credit), it has a direct impact on the money stock. See [[Reserve_Money_Creation_and_Control]] for the mechanism.

### Link to Real Sector
Banking system credit to the private sector (asset side) = credit provided to the real economy for investment and production. The private sector's desire to hold the cash balances generated by the banking system = the "reaction function" determining the rate of inflation (private sector money demand).

## 5. NDA Ceiling as IMF Program Instrument

[RAW] Starting with the monetary survey identity and incorporating a demand function for money that links changes in real money balances to real income and inflation, the IMF financial programming framework posits:

$$\text{If } \Delta NDA > \Delta M2 \text{ (money demand growth)} \Rightarrow \Delta NFA < 0 \text{ (BOP deficit)}$$

Therefore, to achieve a target change in NFA (i.e., a target BOP outcome), given a projected growth in money demand, the IMF sets a ceiling on NDA: the maximum domestic credit expansion consistent with the BOP target. The target path:

$$\Delta NDA^{max} = \Delta M2^{target} - \Delta NFA^{target}$$

where $\Delta M2^{target}$ is derived from the money demand function (growth + inflation targets) and $\Delta NFA^{target}$ is the reserve accumulation objective.

## 6. Treasury Insight

[LLM] The monetary survey identity is the analytical backbone of financial programming:

1. **NDA ceiling logic:** Under a fixed exchange rate, the CB cannot control M2 directly (money supply is endogenous). But it can control NDA (limit domestic credit). Given money demand growth (determined by real growth + inflation targets), NDA ceilings translate into BOP outcomes. This is why all IMF programs include an NDA ceiling — it is the only lever available when the exchange rate is fixed.

2. **M2 vs. M1 vs. broader aggregates — targeting dilemma:** With financial innovation, the relationship between M2 and nominal spending weakens (financial assets outside M2 become substitutes). Moving to broader aggregates (M3, M4) reduces the CB's control. In practice, most programs retain M2/NDA as the operational target while using broader indicators as crosschecks. In transition economies, the NDA approach is more robust than M2 targeting because it addresses the causality directly (domestic credit → money → prices/BOP).

3. **Valuation adjustment discipline:** When the exchange rate changes, the domestic-currency value of NFA changes without any transaction. If NFA is not adjusted for valuation, ΔM2 from eq. 5.8 will reflect currency movements, not actual monetary expansion. This is a common source of measurement error in monetary programming — the IMF standard requires valuation adjustments to be isolated in OINb.

4. **Credit to government as the key lever in transition:** Poland's data (Table 5.1) show that claims on general government were the dominant driver of NDA growth (282 trillion zlotys out of 372 trillion NDA in 1993). Private sector credit was secondary. Monitoring NCG growth is therefore the first-order analytical priority in countries with large fiscal financing needs — changes in NCG feed directly into money growth with tight precision.
