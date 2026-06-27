---
title: OTC Trade Lifecycle
aliases:
- Trade Lifecycle
- Quy trình vòng đời giao dịch
- Post-Trade Processing
- Front-to-Back Office Workflow
type: mechanism
tags:
- market-infrastructure
- settlement
- operations
- risk-management
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch12.md
thesis: The OTC trade lifecycle is a multi-step sequence of independent checks and
  deliberate redundancies designed to ensure that final asset transfers faithfully
  reflect the negotiated intentions of counterparties while minimizing fraud and human
  error.
source_refs:
- file: During_Fixed_Income_Ch12.md
  page: 87
- file: During_Fixed_Income_Ch12.md
  page: 88
- file: During_Fixed_Income_Ch12.md
  page: 91
- file: During_Fixed_Income_Ch12.md
  page: 93
- file: During_Fixed_Income_Ch12.md
  page: 94
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Unlike exchange trading where a central counterparty (CCP) anonymizes and automates the process, the **OTC trade lifecycle** relies on bilateral coordination across three distinct organizational layers: the Front Office (negotiation), Middle Office (verification), and Back Office/Custodian (settlement). Alexander Düring emphasizes that the "main information-theoretical tool" used to prevent errors in this fragmented system is **deliberate redundancy**. [[During_Fixed_Income_Ch12.md#page=87-90]]

## Mechanism: The 12-Step Sequence

The lifecycle typically follows these precise steps:

### Phase 1: Negotiation & Agreement (Front Office)
1.  **Inquiry (RFQ):** The customer (price taker) asks one or more market makers for a quote. [[During_Fixed_Income_Ch12.md#page=87]]
2.  **Negotiation:** Bilateral communication (chat, phone, platform) until a price is accepted or rejected.
3.  **Agreement:** The market maker confirms the trade (e.g., "Done"). This is the binding moment. [[During_Fixed_Income_Ch12.md#page=87]]
4.  **Recording:** Both parties enter the trade into their book-keeping systems. Electronic platforms use **Straight-Through Processing (STP)** for automatic entry. [[During_Fixed_Income_Ch12.md#page=91]]

### Phase 2: Enrichment & Verification (Middle Office)
5.  **Enrichment:** Adding **Standard Settlement Instructions (SSIs)**, such as custodian and account details, to the trade record. [[During_Fixed_Income_Ch12.md#page=87]]
6.  **Reporting:** Trades are reported to regulators or trade repositories (e.g., for systemic risk analysis). [[During_Fixed_Income_Ch12.md#page=92]]
7.  **Pre-confirmation:** Front offices exchange settlement instructions within seconds/minutes to spot discrepancies early. [[During_Fixed_Income_Ch12.md#page=93]]
8.  **Allocation:** For institutional managers, a single "block" trade is split and allocated to multiple legally separate sub-funds. [[During_Fixed_Income_Ch12.md#page=93]]
9.  **Confirmation:** Middle offices exchange formal messages (e.g., via S.W.I.F.T.). A failure to match here results in a **DK (Don't Know)** status. [[During_Fixed_Income_Ch12.md#page=94]]

### Phase 3: Settlement & Finality (Back Office/Custodian)
10. **Settlement Instructions:** Both parties instruct their respective custodians to transfer cash and securities.
11. **Verification/Settlement:** The custodians match instructions. Settlement only occurs if both sets of instructions agree (the final check). [[During_Fixed_Income_Ch12.md#page=88]]
12. **Reconciliation:** Post-settlement, firms compare internal books with custodian account statements to ensure zero discrepancies. [[During_Fixed_Income_Ch12.md#page=96]]

## Strategic Dynamics: Redundancy and Safety

### The "Information-Theoretical" Tool
To prevent catastrophic errors, market conventions use **Redundancy**. For instance, in a buy transaction:
- The inquiry for an *offer* price signals a buy intent.
- The use of the word *Mine* confirms a buy.
- The use of the preposition *for* (e.g., "Mine 10mio for 110.16") further confirms the buy side.
- Electronic platforms replicate this with distinct **Color Schemes** (e.g., different colors for buy vs. sell screens). [[During_Fixed_Income_Ch12.md#page=90]]

### The "DK" Rejection
If the middle office cannot find an internal record for an incoming confirmation, it issues a "Don't Know" (DK). While DK is not a "free option" to walk away from a trade, it acts as a critical filter for human error or duplicate recordings. [[During_Fixed_Income_Ch12.md#page=94]]

## Evidence / Source Anchors

- Schematic of actors and interactions (Front/Back Office/Custodian): [[During_Fixed_Income_Ch12.md#page=88]]
- The role of deliberate redundancy in trader vernacular: [[During_Fixed_Income_Ch12.md#page=90]]
- The complexity of the "Allocation" step for fund managers: [[During_Fixed_Income_Ch12.md#page=93]]
- Definition of DK (Don't Know) as a repudiation of a presumed contract: [[During_Fixed_Income_Ch12.md#page=94]]

## Related

- [[Indicative_Vs_Firm_Quotes]] — The price types used in Step 1.
- [[Settlement_Fails_And_Incentives]] — What happens when Step 11 fails.
- [[Delivery_Versus_Payment]] — The technical mechanism of Step 11.
- [[Central_Counterparty_CCP]] — The alternative (exchange) model of the lifecycle.
- [[Herstatt_Risk]] — The historical danger that this lifecycle seeks to mitigate.
