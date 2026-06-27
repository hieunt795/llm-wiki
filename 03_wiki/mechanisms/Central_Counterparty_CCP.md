---
title: Central Counterparty (CCP)
aliases:
- Central Clearing
- CCP
- Default Waterfall
- Clearing House
- Novation
type: mechanism
tags:
- market-infrastructure
- risk-management
- clearing-and-settlement
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring; Tuckman & Serrat"
provenance: During_Fixed_Income_Ch13.md; Tuckman_Serrat_2022_Ch13.md
thesis: A Central Counterparty (CCP) is a financial institution that interposes itself
  between the counterparties to a trade, becoming the buyer to every seller and the
  seller to every buyer, thereby transforming bilateral counterparty credit risk into
  centralized liquidity risk managed through a multi-layered defense waterfall.
source_refs:
- file: During_Fixed_Income_Ch13.md
  page: 101-105
- file: Tuckman_Serrat_Fixed_Income_2022.md
  page: 339-344
created: '2026-04-13'
updated: '2026-04-29'
---

## Thesis

In an un-cleared bilateral market of $n$ participants, there are $n(n-1)/2$ possible relationships. **Central Clearing** mathematically collapses this geometric complexity into $n$ relationships—each between a participant and the CCP. While this creates massive operational and netting efficiency, it concentrates 100% of the systemic risk onto the CCP. To survive a major member default without triggering a global collapse, the CCP uses a rigid multi-layered defense mechanism known as the **Default Waterfall**. [[During_Fixed_Income_Ch13.md#page=101]]; [[Tuckman_Serrat_Fixed_Income_2022.md#page=339]]

## Mechanism: Novation and Risk Transformation

Immediately after a trade is negotiated bilaterally (e.g., via open-outcry or electronic matching), it is "given up" to the CCP through a legal process called **Novation**.
- **The "Ticket Stamped" Logic:** [RAW] Neftci mô tả rằng cho đến trước khi phiếu lệnh (deal ticket) được đóng dấu, hai bên giao dịch vẫn là đối tác trực tiếp của nhau. Ngay khi lệnh được đóng dấu và ghi nhận bởi hệ thống bù trừ, CCP sẽ chính thức tiếp quản vai trò đối tác trung tâm.
- **The Result:** The original bilateral contract is canceled and replaced by two new contracts: (1) Buyer vs. CCP and (2) Seller vs. CCP.
- **Risk Transformation:** The CCP transforms counterparty credit risk into **Liquidity Risk**. By requiring daily cash payments (**Variation Margin**), the CCP ensures that no credit exposure builds up over time, but this forces clearing members to have immediate access to cash even in volatile markets. [[During_Fixed_Income_Ch13.md#page=101-103]]

### Clearing Permutations (Figure 13.6)
1.  **Bilateral Swap:** A pays fixed to B. Each bears the other's full default risk.
2.  **Cleared Swap (Members):** A and B (both members) trade. Contract is replaced by A-vs-CCP and B-vs-CCP. Backstopped by the CCP and its broader membership.
3.  **Cleared Swap (Client):** A client of Member 1 trades. The trade is backstopped **first by Member 1**, and then by the CCP and membership. [[Tuckman_Serrat_Fixed_Income_2022.md#page=340]]

## Netting Trade-offs: Efficiency vs. Scope
Clearing confers significant advantages but at an opportunity cost:
- **Product-Class Netting:** CCPs net positions within a single product class (e.g., all IRS).
- **Cross-Product Sacrifice:** Unlike bilateral house-netting (where a dealer nets IRS vs. Repo vs. CDS with a single client), clearing requirements outlaw this in-house netting, forcing margin to be posted separately at different CCPs. [[Tuckman_Serrat_Fixed_Income_2022.md#page=341]]

## The CCP Default Waterfall (Thác vỡ nợ)

If a clearing member defaults, the CCP defends its solvency through a strictly sequential "Waterfall" of capital:

1.  **Defaulter's Initial Margin (IM):** First source of funds.
2.  **Defaulter's Default Fund Contribution:** The member's skin in the game.
3.  **CCP's Own Capital (Skin-in-the-game):** Typically small relative to total member contributions, but acts as an incentive for proper risk management.
4.  **Surviving Members' Default Fund Contributions:** Mutualized loss sharing.
5.  **(Unfunded) Member Assessments:** Additional calls for funds (not held in reserve, potentially hard to collect in a crisis).
6.  **VM Haircutting:** Pro-rata reduction of Variation Margin owed to non-defaulting participants.
7.  **Voluntary Actions & CCP Close:** Last recourse before the CCP ceases operations.
[[Tuckman_Serrat_Fixed_Income_2022.md#page=341-343]]

## Systemic Risks & Public Policy Issues

### 1. Concentration Risk ("Eggs in one basket")
Clearing has reduced systemic risk in some ways but concentrated it in very few entities.
- **LCH (London Clearing House):** Dominates clearing for GBP, USD (majority), and EUR-denominated IRS.
- **JSCC:** Dominates JPY swaps.
Legislators have effectively decided to "put all eggs in one basket and watch that basket." [[Tuckman_Serrat_Fixed_Income_2022.md#page=343]]

### 2. Margin Procyclicality
Reducing counterparty credit risk increases **Liquidity Risk**. Raising IM during market volatility (to protect the CCP) can exacerbate financial stress as members struggle to meet margin calls while maintaining other obligations. [[Tuckman_Serrat_Fixed_Income_2022.md#page=343]]

### 3. Customer Protection (LSOC)
In the IRS market, the margin of non-defaulting customers is protected via **LSOC (Legally Separated Operationally Commingled)**. This prevents "fellow customer risk" common in the futures market, where a clearing house might tap non-defaulting customer margin to cover a member's obligation. [[Tuckman_Serrat_Fixed_Income_2022.md#page=341]]

## Evidence / Source Anchors
- Mathematical collapse of relationships from $n(n-1)/2$ to $n$: [[During_Fixed_Income_Ch13.md#page=101]]
- Novation and the "give-up" mechanism: [[During_Fixed_Income_Ch13.md#page=101-102]]
- Analysis of risk transformation (credit into liquidity): [[During_Fixed_Income_Ch13.md#page=103]]
- Detailed Default Waterfall (8 layers): [[Tuckman_Serrat_Fixed_Income_2022.md#page=342]]
- LSOC vs. Fellow Customer Risk: [[Tuckman_Serrat_Fixed_Income_2022.md#page=341]]
- Concentration risk and LCH dominance: [[Tuckman_Serrat_Fixed_Income_2022.md#page=343]]

## Related

- [[Margining_IM_Vs_VM]] — The first line of defense.
- [[Margin_Procyclicality]] — The liquidity trade-off.
- [[LSOC_Mechanism]] — Customer margin protection.
- [[Agency_Vs_Principal_Clearing_Models]] — How non-members access the CCP.
- [[Valuation_Adjustments_xVA]] — How central clearing (or the lack thereof) affects price.
- [[Repurchase_Agreement_Mechanism]] — A primary market that is now pervasive in central clearing.
