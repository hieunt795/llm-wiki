---
title: Macroeconomic Accounting Identities
aliases:
  - Absorption Approach to BOP
  - Saving Investment Identity
  - GNDI Absorption Identity
  - S-I Equals CAB
  - Resource Gap Identity
type: mechanism
tags:
  - macro
  - national-accounts
  - balance-of-payments
  - real-sector
  - BOP
status: verified
confidence: 4
half_life_years: 10
school: ""
superseded_by: null
superseded_date: null
expert_lens: "Ouanes | Thakur | IMF"
provenance: "IMF — Macroeconomic Accounting and Analysis in Transition Economies (1997), Ch.2"
thesis: Two fundamental ex-post accounting identities link the national accounts to the balance of payments: (1) GNDI − A = CAB (absorption approach — excess absorption over income equals the current account deficit) and (2) S − I = CAB (saving-investment approach — excess investment over saving must be financed by foreign saving), and these identities always hold regardless of behavioral causation.
source_refs:
  - file: "Macroeconomic Accounting and Analysis IMF.md"
    page: 17
created: "2026-07-01"
updated: "2026-07-01"
---

# [[Macroeconomic_Accounting_Identities]]

## Thesis

[RAW] The national income accounting framework yields two important relations that lie at the heart of macroeconomic analysis. These key relations are derived from the identity linking GDP with its expenditure counterparts.

## 1. Identity Chain (Full Derivation)

[RAW] Starting from the expenditure definition of GDP:

$$GDP = C + I + (X - M) = A + (X - M) \tag{1}$$

Adding net factor income from abroad:
$$GNI = GDP + Y_f = A + (X - M + Y_f) \tag{2}$$

Adding net current transfers:
$$GNDI = GNI + TR_f = A + (X - M + Y_f + TR_f) \tag{5}$$

Therefore:
$$GNDI - A = X - M + Y_f + TR_f = CAB \tag{7}$$

Since $S = GNDI - C$ by definition:
$$S - I = CAB \tag{9}$$

## 2. The Absorption Identity: GNDI − A = CAB

[RAW] The current account balance (CAB) is, ex post, identical to the gap between GNDI and absorption (A):

$$GNDI - A = CAB \tag{2.8}$$

**Interpretation:** A current account deficit occurs whenever a country spends beyond its means — absorbs more than it produces. To reduce a current account deficit, the country's income must be increased and/or absorption must be reduced.
- Increasing output in the **short term** requires unused production capacity.
- In the **medium term**, requires adequate structural policies.
- Domestic absorption can be reduced by contracting $C$ and/or $I$.

**Limitation:** This is an accounting relationship, not a behavioral theory. Other factors (exchange rates, interest rates, exogenous shocks) must be introduced to explain current account behavior.

## 3. The Saving-Investment Identity: S − I = CAB

[RAW] The current account of the balance of payments is, ex post, equivalent to the gap between economywide saving and investment:

$$S - I = CAB \tag{2.9}$$

Or equivalently:
$$\text{Economywide saving} - \text{Investment} = \text{Current account} = \text{Use of foreign saving}$$

**In a closed economy:** Ex-post aggregate saving necessarily equals aggregate investment ($S = I$).

**In an open economy:** The difference between aggregate saving and investment is the current account balance. Any economywide excess of investment over saving must be covered ex post by foreign saving. Therefore a current account deficit can be reduced by:
- Increasing saving, or
- Reducing investment.

**Key caveat:** [RAW] These relationships are ex post identities that always hold, but they do not provide an explanation of any imbalances in the economy, the underlying behavior of economic agents, or the desirability of a particular imbalance.

## 4. Private Sector Resource Gap

[RAW] For the nongovernment sector (households + enterprises = private sector), the budget constraint links its income-expenditure gap and its financing:

Private sector saving:
$$S_p = GNDI_p - C_p \tag{2.11}$$

Private sector absorption:
$$A_p = C_p + I_p$$

Private sector financing gap:
$$F_p = -(S_p - I_p) \tag{2.13}$$

This gap is covered by:
$$F_p = FDI_p + NFB_p + \Delta NDC_p - \Delta M2 - NB \tag{2.14}$$

where:
- $FDI_p$ = foreign direct investment to private sector
- $NFB_p$ = net foreign borrowing by private sector
- $\Delta NDC_p$ = net credit from banking system to private sector
- $\Delta M2$ = increase in currency holdings and deposits (private sector lending to banking system)
- $NB$ = nonbank borrowing of government from private sector

Therefore:
$$S_p - I_p + FDI_p + NFB_p + \Delta NDC_p - \Delta M2 - NB = 0 \tag{2.15}$$

This paves the way for fuller **flow-of-funds analysis** across all sectors. See: [[Chapter_6_Flow_of_Funds]].

## 5. Sector-Level Accounting Structure

[RAW] All variables in Box 2.2:

| Symbol | Definition |
|---|---|
| $A$ | Domestic absorption ($C + I$) |
| $X$ | Exports of goods and nonfactor services |
| $M$ | Imports of goods and nonfactor services |
| $Y_f$ | Net factor income from abroad |
| $TR_f$ | Net transfers from abroad |
| $C$ | Final consumption |
| $I$ | Gross investment (including inventory changes) |
| $S$ | Gross national saving |
| $CAB$ | Current account balance |

## 6. Treasury Insight

[LLM] These identities are the analytical anchor for IMF program design and BOP analysis. When a country has a large current account deficit, the S-I identity forces the analyst to identify which sector is the net borrower — government, private, or both — and how that borrowing is financed (domestic credit, foreign debt, FDI). The absorption identity is particularly useful for policy design: if the CAB must narrow, either output must rise (supply-side reform, structural adjustment) or absorption must fall (fiscal consolidation, credit tightening). The private sector resource gap equation (eq. 2.14-2.15) is the direct precursor to monetary programming frameworks, where $\Delta NDC_p$ becomes a key policy target. Understanding this chain allows the practitioner to trace any macroeconomic imbalance back to its sectoral origin.
