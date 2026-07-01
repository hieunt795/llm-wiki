---
title: Reserve Money Creation and Control
aliases:
  - Reserve Money
  - Monetary Base Creation
  - High-Powered Money
  - Reserve Money Identity
  - Monetary Policy Instruments
  - Monetization Fiscal Deficit
  - Sterilization Operations
  - Open Market Operations
  - Central Bank Discount Rate
  - Reserve Requirements Monetary Policy
type: mechanism
tags:
  - monetary-policy
  - central-banking
  - macro
  - monetary-accounts
  - reserve-money
status: verified
confidence: 4
half_life_years: 10
school: ""
superseded_by: null
superseded_date: null
expert_lens: "IMF | Ouanes | Thakur"
provenance: "IMF — Macroeconomic Accounting and Analysis in Transition Economies (1997), Ch.5"
thesis: Reserve money (the monetary base) is the sole liability of the monetary authorities that serves as the foundation for the money supply, defined by the identity RM ≡ NFA* + NCG* + CDMB* + CPS* + OIN*, and controlled through five direct instruments — foreign exchange intervention, open market operations, government deficit financing, discount window, and reserve requirements — but the monetary authorities' control is inherently incomplete because NFA responds to BOP outcomes and NCG is often adjusted passively to government financing needs.
source_refs:
  - file: "Macroeconomic Accounting and Analysis IMF.md"
    page: 163
created: "2026-07-01"
updated: "2026-07-01"
---

# [[Reserve_Money_Creation_and_Control]]

## Thesis

[RAW] The creation of high-powered money (also known as reserve money or the monetary base) is a prerogative of the monetary authorities. The control they exercise over the amount of high-powered money in the economy is the main route through which the monetary authorities control the money supply and obtain seigniorage.

## 1. Reserve Money Identity (eq. 5.1–5.2)

[RAW] Given the balance sheet constraint (assets = liabilities):

$$RM \equiv NFA^* + NCG^* + CDMB^* + CPS^* + OIN^* \tag{5.1}$$

In terms of changes in stocks:

$$\Delta RM = \Delta NFA^* + \Delta NCG^* + \Delta CDMB^* + \Delta CPS^* + \Delta OIN^* \tag{5.2}$$

**Growth rate decomposition (eq. 5.3–5.4):** The growth rate of reserve money can be expressed as a sum of weighted growth rates of asset items, where weights = relative shares of lagged asset items in the lagged reserve money stock:

$$\frac{\Delta RM_t}{RM_{t-1}} = \sum_i \frac{\Delta A^*_i}{A^*_{i,t-1}} \cdot \frac{A^*_{i,t-1}}{RM_{t-1}}$$

This decomposition reveals which asset class is the primary driver of reserve money growth in any period.

## 2. How the Central Bank Creates Reserve Money

[RAW] The central bank creates reserve money whenever it acquires assets and pays for them by creating liabilities. Examples:

- **Purchases FX from domestic resident** → pays with a check → resident deposits check at DMB → DMB deposits at CB → NFA↑, RM↑
- **Buys government securities** → CB holding of govt securities↑ (assets) → currency in circulation↑ or bank deposits↑ (RM↑)
- **Lends to government** (government runs down deposits to pay private sector) → NCG↑ net → RM↑

**The key principle:** No other entity in the economy can create money simply by writing a check against itself.

## 3. Five Instruments of Reserve Money Control

### (i) Foreign Exchange Intervention
[RAW] Purchase of FX → NFA↑, RM↑ (expansionary). Sale of FX → NFA↓, RM↓ (contractionary). FX intervention directly affects reserve money and has a direct impact on liquidity and monetary policy stance.

### (ii) Open Market Operations (OMO)
[RAW] Purchase of government securities from public → CB holdings of govt securities↑ → RM↑ (currency↑ or bank deposits with CB↑). Sale of government securities → CB holdings↓ → RM↓. Preferred method for changing reserve money stock because it is market-based and flexible.

### (iii) Financing of Government Deficit
[RAW] When the government finances its deficit by borrowing from the CB:
1. CB claims on government↑ and government deposits with CB↑ — no initial RM change
2. Government uses deposits to pay private sector → government deposits↓ → NCG (net)↑ → RM↑

[RAW] **A fiscal deficit financed by CB borrowing produces a one-for-one increase in reserve money.** This is equivalent to financing the deficit by issuing currency — the monetization of the fiscal deficit. The CB's ability to refuse this lending is the hallmark of an independent central bank.

### (iv) Discount Window (Rediscount Policy)
[RAW] Central bank lends to DMBs at the discount rate. An increase in the discount rate → signals tighter monetary conditions → reduces bank borrowing from CB → reduces CB assets → reduces RM. Decrease in discount rate → increases bank borrowing → increases RM. The CB's lending to DMBs is in practice the most directly controllable source of reserve money.

### (v) Reserve Requirements
[RAW] Increasing the required reserve ratio forces DMBs to hold a larger level of reserves for the same level of deposits → increases RM. At the same time, it reduces DMBs' ability to create money (increases drain on reserve base). Reserve requirements affect both the supply of reserve money and the money multiplier.

## 4. Limits on MA Control Over Reserve Money

[RAW] The monetary authorities' control over reserve money is inherently incomplete:

1. **NFA:** Changes in net foreign assets reflect BOP outcomes — generally cannot be considered a fully policy-controlled variable (especially under a fixed exchange rate where CB must intervene to defend the peg).

2. **NCG:** In many countries, claims on the government are adjusted passively to the government's budgetary position, especially without an independent central bank. The CB could resist, but in practice, fiscal dominance is common in transition economies.

3. **Most controllable:** CDMB (claims on DMBs through the discount window).

## 5. Sterilization

[RAW] Sterilization = offsetting the impact of foreign exchange intervention on reserve money with an open market operation.

**Mechanism:** If CB sells FX (reducing NFA and RM) but simultaneously buys government securities (increasing NCG and RM), the net effect on RM is zero — the external drain is "sterilized."

[RAW] **Sterilization limitations:**
1. Requires a broad, well-functioning securities market (often absent in transition economies)
2. Cost: interest payments on government securities purchased escalate if sterilization is large-scale
3. Only a short-term fix — the underlying BOP imbalance persists and will eventually force adjustment

Under a fixed exchange rate with capital mobility, sterilization fails: the interest rate differential from domestic securities attracts more capital inflows, requiring more CB intervention to defend the peg, leading to more sterilization needs in a self-defeating cycle.

## 6. Treasury Insight

[LLM] The reserve money identity and the 5 instruments framework is the core of monetary programming:

1. **Monetization = automatic M expansion:** The mechanism is precise — every unit of government deficit financed by CB credit eventually increases RM by one unit once the government spends. This is why IMF programs set NDA ceilings rather than M2 targets under fixed rate regimes — the NDA ceiling limits the contribution to RM from domestic credit, leaving the NFA component to fluctuate with BOP outcomes.

2. **Passive NCG is the central bank independence diagnostic:** When NCG adjusts passively to fiscal needs, the CB is de facto providing unlimited deficit monetization. The practice can be subtle — technically the CB "lends" against government securities, but if the securities are created specifically for the CB, the distinction collapses. Looking at the NCG contribution to RM growth in eq. 5.3 over time reveals the extent of fiscal dominance.

3. **OMO requires a market:** The preferred central bank instrument (OMO) requires liquid secondary markets for government securities. In transition economies at the start of reform, this market did not exist — forcing reliance on reserve requirements and direct credit controls as first-line tools, shifting to OMO as markets developed.

4. **Sterilization cost accumulates:** When a country with a crawling peg (e.g., Poland 1994–95) attracts large capital inflows, sterilization via T-bill issuance creates a carry trade: foreign investors earn domestic T-bill yields while holding a currency that depreciates only by the crawl rate. The CB bears the interest cost. If the spread is large and inflows are sustained, sterilization costs become a significant quasi-fiscal burden. See [[Quasi_Fiscal_Operations]].
