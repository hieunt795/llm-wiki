---
title: Money Multiplier — IMF Framework
aliases:
  - Money Multiplier IMF
  - Money Multiplier Three Agents
  - Money Multiplier Instability
  - Currency-Deposit Ratio
  - Reserve-Deposit Ratio
  - Money Supply Function
  - Fractional Reserve Money Creation
  - Money Multiplier Transition Economy
type: mechanism
tags:
  - monetary-policy
  - banking
  - macro
  - monetary-accounts
  - money-supply
status: verified
confidence: 4
half_life_years: 10
school: ""
superseded_by: null
superseded_date: null
expert_lens: "IMF | Ouanes | Thakur"
provenance: "IMF — Macroeconomic Accounting and Analysis in Transition Economies (1997), Ch.5"
thesis: The money multiplier — the ratio of broad money to reserve money — is determined by three agents (monetary authorities setting reserve requirements, commercial banks deciding excess reserve holdings, and the public choosing the currency-to-deposit ratio and deposit mix), meaning the multiplier is not constant but varies with interest rates, inflation expectations, and the efficiency of the payments system; under this formulation, money supply can increase either because reserve money increases or because the multiplier rises, and the authorities must account for multiplier instability when setting reserve money targets to achieve M2 objectives.
source_refs:
  - file: "Macroeconomic Accounting and Analysis IMF.md"
    page: 178
created: "2026-07-01"
updated: "2026-07-01"
---

# [[Money_Multiplier_IMF_Framework]]

## Thesis

[RAW] Under the fractional reserve system, an initial increase in reserve money serves as a base for financing subsequent monetary expansion by the banking system. Banks use their deposits to make loans, keeping only a fraction as reserves.

## 1. Simple Money Multiplier (eq. 5.13–5.15)

[RAW] Starting with definitions:
- $RM = CY + R$ (reserve money = currency + bank reserves)
- $M = CY + DD$ (money = currency + demand deposits)

The multiplier $mm$ is simply the ratio of money stock to base money:

$$mm = \frac{M}{RM} = \frac{CY + DD}{CY + R} \tag{5.13}$$

Dividing numerator and denominator by DD, and defining:
- $c$ = currency-deposit ratio ($CY/DD$)
- $r$ = reserve-deposit ratio ($R/DD$)

$$M = \frac{c+1}{c+r} \cdot RM \tag{5.14}$$

The factor $(c+1)/(c+r)$ is the **money multiplier** — how much money is created by one unit of reserve money. The money supply function:

$$M = mm \cdot RM \tag{5.15}$$

In terms of changes:

$$\Delta M_t \approx \Delta mm_t \cdot RM_{t-1} + mm_{t-1} \cdot \Delta RM_t \tag{5.16}$$

**Money supply can increase either because reserve money increases or because the multiplier rises.** An increase in the money multiplier for the same reserve money target loosens monetary conditions.

**Multiplier is larger when:**
1. The reserve requirement ratio ($r$) is **smaller**
2. The currency-to-deposit ratio ($c$) is **smaller** (public keeps less cash, more deposits)

## 2. General Money Multiplier (M2) — eq. 5.17–5.18

[RAW] For broad money M2 (including time and savings deposits TD), redefine:

$$M2 = CY + DD + TD$$
$$RM = CY + r_d DD + r_t TD + r_e DD$$

where:
- $r_d$ = required reserve ratio on demand deposits
- $r_t$ = required reserve ratio on time and savings deposits
- $r_e$ = excess reserve ratio (excess reserves as ratio to demand deposits)

The M2 multiplier:

$$mm = \frac{M2}{RM} = \frac{CY + DD + TD}{CY + r_d DD + r_t TD + r_e DD} \tag{5.17}$$

Dividing by DD and defining:
- $c$ = $CY/DD$ (currency-deposit ratio)
- $b$ = $TD/DD$ (time deposit-to-demand deposit ratio)

$$mm = \frac{c + 1 + b}{c + r_d + b \cdot r_t + r_e} \tag{5.18}$$

## 3. Three Agents Determining the Multiplier

[RAW] Equation 5.18 reveals that the money multiplier is determined by three different types of economic agents:

| Agent | Decision | Parameters |
|---|---|---|
| **Monetary authorities** | Set reserve requirements | $r_d$, $r_t$ |
| **Commercial banks** | Decide how much to hold in excess reserves | $r_e$ |
| **Nonbank public** | Choose currency vs. deposit ratio; choose demand vs. time deposit ratio | $c$, $b$ |

[RAW] The monetary authorities therefore do not fully control the money stock — the public's preference for cash vs. deposit and DMBs' desire to hold excess reserves also contribute to the determination of the money stock.

## 4. Multiplier Instability

[RAW] Equation 5.17 indicates that the value of the multiplier may not be constant over time, weakening the predictability of the relationship between reserve money and the money supply. Multiplier changes reflect:

1. **Changes by the MA:** Adjustments to reserve requirements ($r_d$, $r_t$)
2. **Changes by commercial banks:** DMBs adjust excess reserves ($r_e$) based on:
   - The exact nature of the reserve requirement (end-of-period vs. period average)
   - Penalty imposed for violation of requirement
   - Opportunity cost of holding excess reserves (interest rate level)
3. **Changes by the public:** The public adjusts $c$ and $b$ based on:
   - Structure of interest rates (higher deposit rates → lower $c$)
   - Inflation level (high inflation → higher $c$ as deposit trust erodes)
   - Other variables

**Implication:** If the multiplier is constant or at least predictable, the CB can achieve a target money supply by setting RM accordingly (eq. 5.15). If the multiplier is unstable, this strategy fails — the CB may hit its RM target but miss its M2 target.

## 5. Money Supply Function Summary

[RAW] The money supply function (M = mm·RM) takes into account the behavior of three actors:
- The **public's preference** for cash vs. deposits
- The **banking system's** desired excess reserve ratio
- The **monetary authorities'** reserve requirements and credit to DMBs

[RAW] Under a fractional reserve system:
- When DMBs lend, borrowers gain purchasing power and incur a debt obligation to the bank
- Loans do **not** increase the net worth of the borrower (assets↑ = liabilities↑)
- Money created by the fractional reserve system increases the economy's **liquidity**, but not its **wealth**

## 6. Poland Case (Table 5.2 Data)

[RAW] Poland's money multiplier rose steadily:
- 1992: 3.0 (M2/RM = 411.1/135.5)
- 1993: 3.5
- 1994: 3.9

Rising multiplier contributed to M2 growth alongside reserve money expansion — a rising $b$ ratio (public shifted more savings into time deposits as inflation fell and real deposit rates improved).

## 7. Treasury Insight

[LLM] The three-agent multiplier framework has important practical implications:

1. **Reserve requirement changes are blunt tools:** Raising reserve requirements (increases $r_d$) reduces the multiplier and contracts credit — but simultaneously reduces bank profitability (reserves earn below-market returns), creates incentive to disintermediate to institutions outside the required reserve system, and may push activity to the informal sector. The net effect on total money-equivalent claims can be smaller than the direct mechanical impact.

2. **Multiplier instability is the main risk in monetary programming:** If the CB sets an RM target consistent with the M2 objective at multiplier = 3.5, but the multiplier rises to 4.0 (because the public shifts to deposits or banks reduce excess reserves), M2 overshoots the target without any change in RM. This is why financial programming monitors both RM and M2 as performance criteria, not just one.

3. **In transition economies, multiplier evolution is structural:** As the banking system matures (competition increases, payment systems improve, trust in banks rises), $c$ naturally falls and $b$ rises — both of which increase the multiplier. A CB that sets RM targets based on the current multiplier will systematically undershoot M2 as the economy deepens financially. The multiplier expansion itself is non-inflationary (it reflects deeper financial intermediation, not monetary expansion per se) but adds noise to standard monetary programming.

4. **Excess reserves in transition economies ($r_e$):** High excess reserves (state banks not lending aggressively) mean the actual multiplier is well below the theoretical maximum ($1/r_d$). As excess reserves decline (banks lend out the excess), the multiplier rises without any MA action — an endogenous monetary easing. Monitoring changes in $r_e$ provides early warning of money supply acceleration.
