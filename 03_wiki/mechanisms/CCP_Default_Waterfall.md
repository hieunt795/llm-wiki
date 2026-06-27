---
title: CCP Default Waterfall
aliases:
- Default Waterfall
- Thác vỡ nợ CCP
type: mechanism
tags:
- risk-management
- clearing-and-settlement
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat; Alexander Düring"
provenance: Tuckman_Serrat_2022_Ch13.md
thesis: The CCP Default Waterfall is a strictly sequential hierarchy of financial resources used to cover losses resulting from a clearing member's default, designed to protect the CCP's solvency and mutualize extreme losses among survivors.
source_refs:
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 341-343
- file: During_Fixed_Income_Ch13.md
  page: 104-105
created: '2026-04-29'
updated: '2026-04-29'
---

## Mechanism: The 8-Layer Waterfall

When a clearing member defaults (fails to pay Variation Margin), the CCP follows this sequence (Figure 13.7 in Tuckman):

1.  **Defaulter's Initial Margin (IM):** The first line of defense. Seized to cover losses during position close-out.
2.  **Defaulter's Default Fund Contribution:** The defaulter's specific contribution to the mutualized fund.
3.  **CCP Capital (Skin-in-the-Game):** Capital contributed by the CCP itself. Relative to member contributions, this is typically small but critical for aligning the CCP's risk-management incentives with its shareholders' profits.
4.  **Surviving Members' Default Fund Contributions:** Mutualization begins here. Surviving members' contributions are tapped pro-rata.
    - **Sizing Rule:** Total default fund is typically sized to withstand the simultaneous default of the **two largest members** (Cover 2).
5.  **(Unfunded) Member Assessments:** Surviving members are legally obligated to provide additional funds if the pre-funded default fund is exhausted.
    - *Risk:* In a systemic crisis, these assessments might not be honored promptly or in full.
6.  **VM Haircutting:** The CCP reduces the Variation Margin payments owed to non-defaulting participants.
7.  **Voluntary Actions:** Members may take voluntary steps to save the CCP.
8.  **CCP Closes:** The point of total failure; the CCP ceases operations.

## Worked Example: Auction and Replacement
The CCP's model is to take zero market risk. When a member defaults, the CCP must:
- Make VM/STM payments to the non-defaulting side.
- Replace the defaulting swap with an identical swap.
- Funds for this replacement come from the waterfall layers above.

## Failure Conditions: Margin Exhaustion
The waterfall is designed to handle all but "record-breaking financial tsunamis." If market moves exceed the IM and the mutualized fund (Cover 2), the system moves into the "unfunded" and "haircutting" stages, which significantly increase systemic instability.

## Related
- [[Central_Counterparty_CCP]] — The institution managing the waterfall.
- [[Margining_IM_Vs_VM]] — The components of the first layer.
- [[Margin_Procyclicality]] — How waterfall protections can exacerbate crises.
