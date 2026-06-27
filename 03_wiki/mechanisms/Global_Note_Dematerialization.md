---
title: Global Note and Book-Entry System
aliases:
- Global Note
- Book-Entry System
- Dematerialization
- Central Securities Depository
- CSD
- GCSD
- LCSD
type: mechanism
tags:
- market-infrastructure
- settlement
- legal-structure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch11.md
thesis: The modern securities market operates via the dematerialization of physical
  assets into book-entry form, where a single physical 'Global Note' is held in trust
  by a central depository, enabling high-speed electronic transfer of beneficial ownership.
source_refs:
- file: During_Fixed_Income_Ch11.md
  page: 80
- file: During_Fixed_Income_Ch11.md
  page: 81
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The physical transfer of paper certificates is too slow for modern financial markets. To solve this, the industry utilizes **Global Notes** and **Central Securities Depositories (CSD)**. This architecture allows the legal structure of a security (often a bearer bond) to exist physically as a single certificate, while the actual trading occurs through electronic ledger entries. [[During_Fixed_Income_Ch11.md#page=80]]

## Mechanism: The Chain of Ownership

The transition from physical to digital ownership (Dematerialization) follows a specific legal chain:

### 1. The Global Note
A single physical certificate representing the beneficial interest in the entire issue. It is deposited with a trusted intermediary. [[During_Fixed_Income_Ch11.md#page=80]]

### 2. Central Securities Depository (CSD)
The institution (custodian) that holds the physical Global Note in trust. These are divided into:
- **Local CSD (LCSD):** Manage securities within a domestic market (e.g., *Monte dei Titoli* in Italy).
- **Global CSD (GCSD):** International firms that handle the bulk of cross-border transfers. The two dominant GCSDs are **Euroclear** (consortium-owned) and **Clearstream** (subsidiary of Deutsche Börse). [[During_Fixed_Income_Ch11.md#page=80-81]]

### 3. Book-Entry Transfer
Trading occurs through electronic transfers of records (book entries) within the CSD or a specialized security clearer.
- **The Process:** Instead of moving physical paper, the CSD simply updates its internal ledger to reflect that ownership has moved from Bank A to Bank B. The legal link is closed through trust agreements between the clearers and the custodian holding the Global Note. [[During_Fixed_Income_Ch11.md#page=81]]

## Boundaries / Conditions: Market Access
Most clearers have links with one another, allowing for seamless cross-border trading. An investor can trade German government bonds (*Bunds*) or Italian government bonds (*BTPs*) through a single clearing system regardless of where the physical Global Note is stored. [[During_Fixed_Income_Ch11.md#page=81]]

## Evidence / Source Anchors

- Definition of the Global Note and its deposit at a CSD: [[During_Fixed_Income_Ch11.md#page=80]]
- The two dominant global firms (Euroclear and Clearstream) and their ownership: [[During_Fixed_Income_Ch11.md#page=81]]
- The role of security clearers in keeping records of beneficial ownership: [[During_Fixed_Income_Ch11.md#page=80-81]]
- Example of LCSDs (Monte dei Titoli, Bundesschuldenverwaltung): [[During_Fixed_Income_Ch11.md#page=81]]

## Related

- [[Bearer_Vs_Registered_Securities]] — The underlying legal formats.
- [[ISIN_Code]] — The identifiers used to track these book entries.
- [[Settlement_Cycle]] — The timeframe within which these book entries must be finalized.
- [[Custody_Services]] — The broader financial function encompassing CSDs.
