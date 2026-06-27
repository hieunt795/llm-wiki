---
title: Margin Procyclicality
aliases:
- Procyclical Margin
- Tính chu kỳ nghịch của ký quỹ
type: concept
tags:
- risk-management
- liquidity-risk
- systemic-risk
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat"
provenance: Tuckman_Serrat_2022_Ch13.md
thesis: Margin Procyclicality refers to the phenomenon where central counterparty (CCP) margin requirements increase during periods of market stress or high volatility, thereby reducing counterparty credit risk at the expense of exacerbating systemic liquidity risk.
source_refs:
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 343
created: '2026-04-29'
updated: '2026-04-29'
---

## Thesis

The shift to central clearing has moved systemic risk from **counterparty credit risk** to **liquidity risk**. While raising Initial Margin (IM) in a crisis is a necessary risk management tool for a CCP, it forces members to scramble for cash precisely when it is most expensive and scarce, potentially worsening the overall financial stress.

## Mechanism: The Liquidity-Credit Tradeoff

1.  **Volatility Trigger:** When market volatility increases, the CCP's risk models (e.g., VaR-based) demand higher IM to cover potential future exposure.
2.  **Cash Drain:** Members and their clients must post more collateral (typically cash or high-quality liquid assets) to meet these calls.
3.  **Deleveraging Spiral:** To raise cash, participants may be forced to sell other assets, further depressing prices and increasing volatility, which triggers even higher margin calls.
4.  **Crowding Out:** Meeting margin obligations to the CCP may leave members unable to meet non-derivative obligations or continue lending, spreading stress to the broader economy.

## Policy Dilemma
There are no easy solutions to margin procyclicality.
- **Under-margining:** Risking CCP solvency.
- **Over-margining:** Risking systemic liquidity collapse.
Regulators seek "anti-procyclical" (APC) measures, such as margin floors or buffers, to smooth the increase in margin during stress, but these are challenging to calibrate.

## Related
- [[Central_Counterparty_CCP]] — The entity setting margin requirements.
- [[CCP_Default_Waterfall]] — IM is the first layer of the waterfall.
- [[Margining_IM_Vs_VM]] — The difference between change-based VM and risk-based IM.
