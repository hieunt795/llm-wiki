---
title: Bearer vs Registered Securities
aliases:
- Bearer Securities
- Registered Securities
- Chứng khoán vô danh
- Chứng khoán ký danh
type: definition
tags:
- market-infrastructure
- securities-law
- fixed-income
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch11.md
thesis: The legal architecture of securities ownership is divided between Bearer Securities
  (possession equals ownership) and Registered Securities (ledger entry equals ownership),
  a distinction that dictates the velocity, anonymity, and risk profile of the instrument.
source_refs:
- file: During_Fixed_Income_Ch11.md
  page: 79
- file: During_Fixed_Income_Ch11.md
  page: 80
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

At the foundational layer of fixed income markets, the legal methodology of proving ownership determines how an asset can trade. The market is divided into two primary physical implementations: Bearer Securities and Registered Securities. While modern markets have largely moved to electronic book-entry forms, these original legal structures still underpin the rights of the beneficial owner. [[During_Fixed_Income_Ch11.md#page=79]]

## Definition

### 1. Bearer Securities (Chứng khoán vô danh)
A bearer security represents the ultimate physical representation of value: ownership of the beneficial interest is evidenced solely by **physical possession** of the certificate.
- **Mechanism:** Transferring the asset simply requires handing the paper to the counterparty. No central registration is required.
- **Advantages:** Extremely high-velocity trading and absolute anonymity for the holder.
- **Disadvantages:** Significant risk of destruction, theft (e.g., the plot of the movie *Die Hard*), and counterfeiting. Because there is no audit trail, they are prone to money laundering and tax evasion.
- **Denomination Limit:** Printing highly secure, anti-counterfeit certificates in small denominations is economically unfeasible, restricting bearer bonds to larger denominations. [[During_Fixed_Income_Ch11.md#page=79-80]]

### 2. Registered Securities (Chứng khoán ký danh)
In a registered security, the ultimate legal proof of ownership is an entry on a **central registrar** (an agent of the issuer), not the possession of a certificate.
- **Mechanism:** Physical certificates may exist as evidence, but they do not prove beneficial interest on their own. Each transaction must be reported to the registrar for the new owner to be registered.
- **Advantages:** Immune to physical theft or loss. They allow for trading in any denomination (even very small) because the record is digital or ledger-based.
- **Disadvantages:** Cumbersome transaction speeds. The requirement for registration slows down secondary market trading compared to bearer forms. [[During_Fixed_Income_Ch11.md#page=80]]

## The Hybrid Case: Schuldschein
German law recognizes a mixed form called the **Schuldschein** (transferable loan). It is evidenced by a physical certificate (like a bearer security) but ownership is still registered, and the number of transfers is typically limited (usually to three).
- **The Accounting Arbitrage:** Because its transferability is restricted, the Schuldschein is not considered to have a liquid market. This allows holders (banks/insurers) to carry the asset at **amortized cost** rather than using mark-to-market accounting, shielding them from daily price volatility. [[During_Fixed_Income_Ch11.md#page=80]]

## Evidence / Source Anchors

- Beneficial interest in bearer securities derived from possession: [[During_Fixed_Income_Ch11.md#page=79]]
- Risks of bearer securities (theft, counterfeiting, 'Die Hard'): [[During_Fixed_Income_Ch11.md#page=79]]
- Requirement for reporting transactions to the registrar for registered securities: [[During_Fixed_Income_Ch11.md#page=80]]
- The Schuldschein as a hybrid tool for accounting arbitrage: [[During_Fixed_Income_Ch11.md#page=80]]

## Related

- [[Global_Note_Dematerialization]] — The modern system that combines both formats into book-entry systems.
- [[Schuldschein]] — Detailed mechanism of the German promissory note.
- [[Bilateral_Contracts_Vs_Securities]] — The broader classification of debt claims.
- [[CSD_Central_Securities_Depository]] — The institution that manages modern registered ownership.
