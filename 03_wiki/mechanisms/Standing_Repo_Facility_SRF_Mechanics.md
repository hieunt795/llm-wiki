---
title: Standing Repo Facility (SRF) Mechanics
aliases:
- SRF
- Standing Repo Facility
- Fed SRF
- Money Market Backstop
type: mechanism
tags:
- central-banking
- repo
- liquidity
- fed
status: draft
confidence: 2
half_life_years: 5
expert_lens: Vítor Constâncio | Spyros Andreopoulos
provenance: "[RAW-CLIP: Constâncio (2025-11-28); RAW-CLIP: Andreopoulos (2026-04-11)]"
thesis: The Standing Repo Facility (SRF) is a permanent liquidity backstop by the Federal Reserve designed to cap overnight repo rates (SOFR) and prevent spikes by allowing primary dealers (and eventually a broader set of banks) to exchange Treasuries for cash at a fixed rate.
source_refs:
- file: ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
- file: Warsh and the Fed's Balance Sheet.md
created: '2026-05-08'
updated: '2026-05-08'
---

## Thesis

The SRF functions as the "ceiling" of the Fed's operational framework for secured markets, similar to how the Discount Window acts for unsecured markets. Its primary goal is to ensure the smooth transmission of monetary policy by keeping the SOFR-FFR spread in check, especially during periods of technical liquidity stress (e.g., month-ends, tax dates).

---

## 1. Operational Mechanism

- **Counterparties:** Initially limited to Primary Dealers; expanded to include eligible depository institutions.
- **Collateral:** Treasury securities, agency debt, and agency mortgage-backed securities (MBS).
- **Rate:** Set as a fixed rate (e.g., 5.00%), typically positioned at the top of the target range for the Fed Funds Rate.
- **The Ceiling Effect:** By offering a standing offer to lend cash against Treasuries, the Fed effectively prevents market repo rates from rising significantly above the SRF rate.

---

## 2. The "Fear of Stigma" Bottleneck

[RAW-CLIP: Constâncio (2025-11-28)] A critical constraint identified in late 2025 was that primary dealers were hesitant to use the SRF due to "stigma"—the fear that using a central bank facility would signal financial weakness.
- **Result:** This hesitation allowed SOFR to spike even when the facility was available.
- **Fed Response:** Meetings with dealers (Nov 2025) were required to encourage usage and clarify that the SRF is an "intended operational tool" rather than a crisis lender.

---

## 3. Interaction with Monetary Policy (The Warsh Bias)

[RAW-CLIP: Andreopoulos (2026-04-11)] The SRF is essential for the Fed's plan to shrink its balance sheet (Quantitative Tightening).
- **The Logic:** As reserves shrink, the risk of "money market dislocations" increases.
- **The Backstop:** The SRF provides a safety valve that allows the Fed to push reserves lower (potentially toward the 9% GDP threshold) without fearing a 2019-style repo crash.

---

## Boundaries / Failure Conditions

- **Collateral Scarcity:** If dealers lack the specific collateral required for the SRF (or if haircuts are too high), the facility cannot provide liquidity.
- **Transmission Lag:** If non-bank entities (who cannot access the SRF) are the ones needing liquidity, the "ceiling" might not hold for the entire market.

---

## Related

- [[Repurchase_Agreement_Repo_Market_Structure]] — The market context for the SRF.
- [[Repo_Event_September_2019]] — The crisis that led to the creation of the SRF.
- [[Discount_Window_Mechanism]] — The unsecured counterpart to the SRF.
- [[SOFR_Secured_Overnight_Financing_Rate]] — The rate the SRF is designed to control.
- [[Repo_Operations]]
- [[Central_Bank_Liquidity_Support_Programs]]
