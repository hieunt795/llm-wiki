---
title: Seigniorage and Inflation Tax
aliases:
  - Seigniorage
  - Inflation Tax
  - Monetary Financing of Deficit
  - Money Creation Revenue
  - Monetary Correction
  - Inflation Tax Base
type: mechanism
tags:
  - fiscal-policy
  - monetary-policy
  - inflation
  - macro
  - government-finance
status: verified
confidence: 4
half_life_years: 10
school: ""
superseded_by: null
superseded_date: null
expert_lens: "IMF | Blanchard | Fischer | Cagan | Ouanes | Thakur"
provenance: "IMF — Macroeconomic Accounting and Analysis in Transition Economies (1997), Ch.3"
thesis: Seigniorage — revenue from money creation — decomposes into pure seigniorage (growth in real money demand) and the inflation tax (inflation rate times real cash balances held by the public), and follows an inverted-U relationship with the inflation rate because rising inflation erodes the real money demand that constitutes the tax base, ultimately causing total seigniorage revenue to fall as the inflation rate increases beyond the revenue-maximizing level.
source_refs:
  - file: "Macroeconomic Accounting and Analysis IMF.md"
    page: 62
created: "2026-07-01"
updated: "2026-07-01"
---

# [[Seigniorage_and_Inflation_Tax]]

## Thesis

[RAW] A government can finance spending by raising tax revenue from the public, by borrowing, or simply by printing money. Revenue raised through the printing of money is called seigniorage. It arises because of the government's monopoly power to supply fiat or paper money to the economy. Since the cost to the government of printing a currency note is negligible, but it acquires purchasing power over resources equivalent to the face value of the banknote, it gains revenue simply by providing money to the economy.

## 1. Formal Decomposition

[RAW] Total seigniorage ($S$) — the total amount of real resources appropriated by all money-issuing entities — is:

$$S = \frac{\dot{M}}{P} = \mu m \tag{1}$$

where:
- $\mu = \dot{M}/M$ = percentage growth in nominal money stock
- $m = M/P$ = real money stock (cash balances held by the public)

**Government-specific seigniorage ($S_g$)** — reflects only the government's issuance of reserve money (high-powered money $H$):

$$S_g = \frac{\dot{H}}{P} = \beta \cdot \frac{H}{P} \tag{2}$$

where $\beta = \dot{H}/H$ = percentage growth in reserve money.

**Decomposition into components:**

$$S = \dot{m} + \pi \cdot m \tag{3}$$

$$S = \underbrace{\dot{m}}_{\text{pure seigniorage}} + \underbrace{\pi m}_{\text{inflation tax}} \tag{4}$$

where $\pi$ = inflation rate.

- **Pure seigniorage** = change in real cash balances ($\dot{m}$); arises from real growth in the economy or a favorable shift in money demand.
- **Inflation tax** = inflation rate × stock of real cash balances; the inflation rate acts as the "tax rate," real cash balances constitute the "tax base."

## 2. Key Properties

[RAW]

1. **Banks also collect seigniorage.** In a modern economy, banks create money and hence also get seigniorage. In many countries, banks "redistribute" their share by making loans at below-market interest rates — so borrowers also effectively receive a portion.

2. **The inflation tax is highly inefficient.** The cost inflicted on the public by the inflation tax is considerably more than the real resources appropriated by the government: the "tax paid" by the public significantly exceeds what the government "collects."

3. **Base erosion.** As inflation accelerates, the demand for real cash balances falls, as the public substitutes the heavily taxed national currency for foreign currency (dollarization). This shrinkage of the tax base means the government must accept a higher inflation rate to collect the same nominal revenue.

4. **Inverted-U revenue curve (Laffer curve for seigniorage).** Revenue from seigniorage follows an inverted-U as inflation increases — rising initially, reaching a maximum, then declining as the base erodes faster than the "tax rate" rises.

[RAW] In most industrial countries, the maximum seigniorage has been estimated in the range of **1–2% of GDP**; in some developing countries and transition economies, the maximum has fluctuated in the range of **5–10% of GDP**.

## 3. Seigniorage Equals Inflation Tax: The Special Case

[RAW] Seigniorage equals the inflation tax whenever the public keeps its demand for real cash balances constant (i.e., when $\dot{m} = 0$, meaning pure seigniorage is zero). In the absence of inflation, the inflation tax is zero, but seigniorage can still be collected if real cash balances are growing (pure seigniorage).

## 4. Monetizing the Deficit

[RAW] Government borrowing from the central bank is equivalent to the creation of high-powered money. Creating money at a rate that exceeds demand at the current price level creates excess cash balances and eventually drives up the overall price level.

[RAW] In many transition economies, a high proportion of government deficits are monetized and are therefore the principal source of inflation. A government's ability to control real resources by printing money is known as **seigniorage**.

**Note:** Seigniorage accrues **not just to the government** — it is shared between the government (via the central bank's reserve money monopoly) and the banking sector. The public sector's actual capture depends on the institutional framework.

## 5. Seigniorage vs. Inflation Tax: Practical Formula

[RAW] For discrete data:

$$S_t = \Delta m_t + \frac{\Delta P_t}{P_t} \cdot m_{t-1}$$

Seigniorage as a ratio of GDP:
$$s_t = \Delta M_t / GDP_t$$

where $GDP_t$ is nominal GDP.

## 6. Link to Fiscal Sustainability

[WIKI] Seigniorage enters the government's temporal budget constraint as one of three sources of debt stabilization. When real interest rates exceed real growth, the government must run a primary surplus OR generate sufficient seigniorage to prevent the debt-to-GDP ratio from rising explosively. See [[Fiscal_Sustainability_Debt_Dynamics]].

[RAW] Since the amount of seigniorage is limited (the Laffer curve maximum is bounded), it eventually becomes necessary for the government to run a primary surplus when (r > g).

## 7. Treasury Insight

[LLM] For fixed income and macro practitioners in EM/transition contexts, seigniorage dynamics signal two risks:

1. **Monetization risk** — if the government's financing needs exceed the noninflationary seigniorage ceiling (pure seigniorage = $g \times m$), the excess must either be met by debt financing or by accepting higher inflation. Monitoring the fiscal deficit vs. the seigniorage ceiling gives an early warning of monetization pressure.

2. **Currency substitution feedback loop** — as inflation rises and people dollarize, $m$ shrinks, reducing the seigniorage base. The government must increase $\pi$ further to collect the same revenue, which accelerates dollarization further. This is the hyperinflationary spiral mechanism: the inflation tax becomes increasingly inefficient as the tax base collapses, ultimately forcing the government to either default, externally finance, or execute a currency reform.

For monetary programming: the equation $S_g = \beta \cdot H/P$ directly links the IMF's NDA (Net Domestic Assets) ceiling on the central bank to the government's seigniorage capacity — keeping NDA below the ceiling limits the government's money-printing access.
