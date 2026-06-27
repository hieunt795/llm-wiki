---
title: Margining (IM vs VM)
aliases:
- Margining
- Variation Margin
- Initial Margin
- Variation Margin vs Initial Margin
- Cash Margin
- Independent Amount
type: mechanism
tags:
- risk-management
- market-infrastructure
- liquidity
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch13.md
thesis: Margining is the frequent exchange of collateral to reset the exposure of
  a trade to zero, transforming counterparty credit risk into liquidity risk through
  the bifurcation of Variation Margin (revaluation) and Initial Margin (close-out
  protection).
source_refs:
- file: During_Fixed_Income_Ch13.md
  page: 102
- file: During_Fixed_Income_Ch13.md
  page: 103
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

At the core of central clearing lies the frequent exchange of cash and securities known as **Margining**. Alexander Düring explains that while margining protects against credit losses, it creates a new "tax" on liquidity. By settling profits and losses (P&L) daily, the system ensures that no large exposures build up, but it forces market participants to have ready access to central bank cash even during periods of extreme market volatility. [[During_Fixed_Income_Ch13.md#page=102]]

## Mechanism: The Two-Layer Protection

### 1. Variation Margin (VM)
- **Purpose:** To settle the daily change in market value of a position.
- **Mechanism:** Every trade is revalued daily using a universally agreed pricing methodology. The losing party must pay the change in value to the winning party in **cash**.
- **Finality:** Payments are made in cash to make them immediately final and reset the current exposure of the CCP to zero.
- **Strategic Impact:** VM transforms counterparty risk into daily **Liquidity Risk**. A member may be solvent (on paper) but default if they cannot raise sufficient cash for a VM call. [[During_Fixed_Income_Ch13.md#page=102-103]]

### 2. Initial Margin (IM)
- **Purpose:** To protect against market movements *after* a member defaults but *before* their positions are closed out.
- **Mechanism:** Calibrated relative to expected market movements over a specific time window (the time assumed necessary to close out a defaulter).
- **Toán học (The Simple Model):** $IM = \rho \sqrt{t}$
  - where $\rho$ is the one-day expected variance.
  - $t$ is the number of days needed to close positions.
- **Collateral Type:** Unlike VM, clearing houses typically accept **non-cash collateral** (like government bonds) for IM. This ensures that the more permanent IM does not act as an undue drag on the member's income. [[During_Fixed_Income_Ch13.md#page=103]]

## Strategic Dynamics: Correlation and Offsetting

CCPs compete on the efficiency of their margining systems. A CCP that can realistically reflect the risks of a given portfolio through **Netting** (offsetting a paid 11-year swap with a received 12-year swap) will be more attractive to users. However, regulators restrict cross-position netting to prevent artificially low margin requirements during periods where correlations might break down. [[During_Fixed_Income_Ch13.md#page=103]]

## Evidence / Source Anchors

- Analysis of variation margin transforming credit risk into liquidity risk: [[During_Fixed_Income_Ch13.md#page=103]]
- The rationale for paying VM in cash for immediate finality: [[During_Fixed_Income_Ch13.md#page=103]]
- Calibration logic of initial margin ($\rho \sqrt{t}$): [[During_Fixed_Income_Ch13.md#page=103]]
- Discussion on cash VM vs. non-cash IM collateral: [[During_Fixed_Income_Ch13.md#page=103]]
- The role of stable correlations as a precondition for risk offsets: [[During_Fixed_Income_Ch13.md#page=103]]

## Related

- [[Central_Counterparty_CCP]] — The entity that mandates these margin payments.
- [[Variation_Margin_Vs_Initial_Margin_Accounting]] — The accounting treatment of these flows.
- [[Repurchase_Agreement_Mechanism]] — Used by non-bank entities to transform non-cash IM into cash VM.
- [[Valuation_Adjustments_xVA]] — Specifically MVA (Margin Value Adjustment), the cost of providing IM.
