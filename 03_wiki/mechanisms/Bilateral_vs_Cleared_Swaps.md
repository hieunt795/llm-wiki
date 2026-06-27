---
title: Bilateral vs. Cleared Swaps
aliases:
- Cleared Swap Permutations
- Figure 13.6 Logic
type: mechanism
tags:
- market-infrastructure
- clearing-and-settlement
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat"
provenance: Tuckman_Serrat_2022_Ch13.md
thesis: The transition from bilateral to cleared swaps transforms direct counterparty relationships into centralized structures, redistributing default risk from individual firms to a central counterparty (CCP) and its membership.
source_refs:
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 340
created: '2026-04-29'
updated: '2026-04-29'
---

## Thesis

Cleared swaps replace the complex web of bilateral exposures with a hub-and-spoke model. This simplifies operations through netting but introduces new layers of backstopping (Figure 13.6).

## Permutations (Figure 13.6)

### 1. Bilateral Swap
- **Structure:** Counterparty A $\leftrightarrow$ Counterparty B.
- **Risk:** Each bears all of the risk should the other default.
- **Operations:** VM, interest payments, and due diligence are handled directly between the two. Complexity grows geometrically with the number of counterparties.

### 2. Cleared Swap (Member-to-Member)
- **Structure:** Member 1 $\rightarrow$ CCP $\rightarrow$ Member 2.
- **Mechanism:** The original trade is canceled and replaced by two swaps facing the CCP.
- **Risk:** Each member legally faces the CCP.
- **Backstop:** Losses from a member default are backstopped by the **CCP and the broader membership** (via the [[CCP_Default_Waterfall]]).

### 3. Cleared Swap (Member-to-Client)
- **Structure:** Member 1 $\rightarrow$ CCP $\rightarrow$ Client (sponsored by Member 1).
- **Mechanism:** The client is sponsored by a member to face the CCP.
- **Risk Hierarchy:**
    - A default by the **Client** is backstopped **first by Member 1** (sponsoring member).
    - If Member 1 defaults as well, losses are then backstopped by the **CCP and the broader membership**.

## Netting Efficiencies
- **Bilateral:** Netting is only possible between the same two counterparties.
- **Cleared:** Netting occurs across all trades facing the same CCP, regardless of the original counterparty.
- **Trade-off:** Clearing nets within a product class but sacrifices netting across product classes (e.g., IRS vs. Repo) that might have been possible bilaterally.

## Related
- [[Central_Counterparty_CCP]] — The hub in the cleared model.
- [[CCP_Default_Waterfall]] — The backstop mechanism for member defaults.
- [[LSOC_Mechanism]] — Protection for client collateral in the cleared model.
