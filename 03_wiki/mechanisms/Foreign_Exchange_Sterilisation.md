---
title: Foreign Exchange Sterilisation
aliases:
- FX Interventions
- Currency War Mechanics
- Non-Monetary Policy Portfolios
type: mechanism
tags:
- macro
- foreign-exchange
- central-banking
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch07.md"
thesis: Because unilateral Foreign Exchange interventions to depress a domestic currency
  forcefully require the endogenous creation of new central bank base money, authorities
  must deploy rigid Sterilisation operations—algorithmically selling domestic assets
  to drain the newly printed liquidity—to prevent the FX mandate from obliterating
  domestic inflation targets.
source_refs:
- file: Fixed_Income_Alexander_During_Ch07.md
  page: 52
created: '2026-04-16'
updated: '2026-04-16'
---

## Thesis

When a sovereign authority (a Treasury or Central Bank) weaponizes its balance sheet to manipulate the external exchange value of its currency, it triggers a massive systemic paradox. Aggressively buying foreign currency to intentionally depress the domestic exchange rate inherently forces the creation of vast amounts of new domestic base money. To prevent this newly injected liquidity from triggering hyperinflation and totally destroying the central bank’s primary domestic price stability mandate, authorities must aggressively execute "Sterilisation"—rapidly selling domestic assets to manually vacuum the newly printed money back out of the financial system.

## Mechanism

### The Liquidity Injection Problem
Assume the Bank of Japan (BOJ) desires to weaken the Yen against the Dollar to support domestic exporters.
1. The BOJ aggressively buys USD in the open market.
2. To pay the counterparty for the USD, the BOJ cannot use pre-existing Yen. As a central bank, it literally prints the required Yen, infinitely expanding its short-term liabilities (creating new Base Money).
3. Result: The Yen drops in relative FX value, but the domestic Japanese banking system is now flooded with new, highly inflationary base Yen.

### The Sterilisation Operation
To surgically disconnect the FX manipulation from the domestic inflation mandate, the authority "sterilizes" the intervention.
- The Central Bank/Ministry immediately issues equivalent short-term domestic bonds (e.g., Japan’s Foreign Exchange Fund Financing Bills) and aggressively sells them to the domestic market.
- By demanding Yen from private commercial banks in exchange for these bills, the authority forcefully sucks the equivalent volume of Yen Base Money right back out of the system.
- **Net Result:** The domestic money supply ($M0$) statistically remains flat (zero inflationary impact), but the central bank's asset side has permanently swapped domestic securities for foreign currency reserves.

### Boundaries / Conditions

### The Structural Limits of Sterilisation
A sovereign possesses infinite asymmetrical firepower to depress its *own* currency because it can print infinite domestic base money to buy foreign assets. 
However, deploying interventions to *defend* a collapsing currency (e.g., selling USD to buy Yen) suffers a hard mathematical limit. You cannot print foreign currency. Interventions defending a currency are strictly bounded by the total absolute volume of finite Foreign Reserves stored on the sovereign balance sheet. Once reserves hit zero, the defense shatters entirely.

## Evidence / Source Anchors

- Operational mechanics explaining how buying foreign currency mathematically creates central bank liabilities: [[Fixed_Income_Alexander_During_Ch07.md#page=52]]
- The specific usage of Japanese Foreign Exchange Fund Financing Bills to immediately vacuum the excess liquidity: [[Fixed_Income_Alexander_During_Ch07.md#page=52]]
- The explicit clash between FX intervention operations and domestic inflation targets: [[Fixed_Income_Alexander_During_Ch07.md#page=52]]

## Related

- [[Monetary_Transmission_Mechanism]] — the inflation process that sterilization explicitly attempts to short-circuit
- [[Central_Bank_Liquidity_Provision_Mechanics]] — the inverse operations (liquidity draining mechanisms) used during sterilization
- [[Central_Bank_Definition_And_Mandates]]
- [[Central_Bank_Operational_Framework_Design]]
- [[FX_Sterilization_Mechanism]]
- [[Base_Money]]
- [[ECB_Institutional_Architecture]]
- [[Eurobond_And_Foreign_Bonds]]
- [[Financial_Repression]]
- [[Fiscal_Dominance]]
- [[Nonbank_Financial_Intermediation]]
- [[OTC_Vs_Exchange_Trading]]
- [[TED_Spread]]
- [[Exchange_Rate_Targeting_Weaknesses]]
