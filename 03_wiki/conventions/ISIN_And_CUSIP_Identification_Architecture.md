---
title: ISIN and CUSIP Identification Architecture
aliases:
- ISIN Code
- CUSIP Code
- ISIN Algorithm
- CUSIP Algorithm
- Security Identifiers
- WKN
- Meigara Code
type: convention
tags:
- market-infrastructure
- settlement
- automation
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch11.md
thesis: Securities identification systems like ISIN and CUSIP utilize standardized
  alphanumeric codes with built-in check-digit algorithms to enable automated settlement
  and eliminate human error in global trading.
source_refs:
- file: During_Fixed_Income_Ch11.md
  page: 81
- file: During_Fixed_Income_Ch11.md
  page: 82
- file: During_Fixed_Income_Ch11.md
  page: 83
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

For automated settlement, it is vital that securities are identified in a way that does not require human interpretation. This is achieved through fixed-length, alphanumeric identifiers like the **ISIN** (Global standard) and **CUSIP** (US domestic standard). These codes are not just random strings but have internal structures and mathematical check-digits to prevent transmission errors. [[During_Fixed_Income_Ch11.md#page=81]]

## 1. ISIN (International Securities Identification Number)

Governed by ISO standard 6166:2013, the ISIN is a 12-character alphanumeric code divided into three blocks.

### The Structure
- **Block 1 (2 chars):** Country code of issuance (ISO 3166-1). Example: US (United States), JP (Japan), DE (Germany). The special code **XS** is used for Eurobonds.
- **Block 2 (9 chars):** National Securities Identification Number (NSIN). Often padded with zeros if shorter than 9 characters (e.g., German WKNs start with DE000).
- **Block 3 (1 char):** Check digit calculated from the first 11 characters. [[During_Fixed_Income_Ch11.md#page=82]]

### The ISIN Algorithm
1. Convert all letters to numbers (A=10, B=11, etc.).
2. Double every other number, starting with the second. If a result is two digits, replace it with the sum of its digits or treat them as two separate digits in a sequence.
3. Sum all the resulting digits.
4. Calculate the 10s modulus and subtract it from 10 to find the check digit. [[During_Fixed_Income_Ch11.md#page=83]]

## 2. CUSIP (Committee on Uniform Security Identification Procedures)

Used primarily in the US and Canada, the CUSIP is a 9-character code.

### The Structure
- **Block 1 (6 chars):** Identifies the issuer (e.g., 912796 for US Treasury bills).
- **Block 2 (2 chars):** Identifies the individual issue (contains at least one letter for debt securities).
- **Block 3 (1 char):** Check digit. [[During_Fixed_Income_Ch11.md#page=83]]

### The CUSIP Algorithm
The CUSIP check digit is calculated similarly to the ISIN but with a "subtly different" method. The primary difference is how the alphanumeric values are translated and summed. [[During_Fixed_Income_Ch11.md#page=83-84]]

## 3. The "Tap and Funge" Process

Issuers often issue new tranches (Taps) of existing securities.
- **Temporary ISIN:** To handle non-standard settlement dates of the new tranche, it is initially issued with a new, temporary ISIN.
- **Funging:** After a set period, the new ISIN is merged (**funged**) into the existing ISIN. The temporary identifier ceases to exist, and the new position's ID is changed to the master ISIN. [[During_Fixed_Income_Ch11.md#page=82]]

## Evidence / Source Anchors

- Definition of ISIN structure (ISO 6166): [[During_Fixed_Income_Ch11.md#page=82]]
- Usage of the 'XS' code for Eurobonds: [[During_Fixed_Income_Ch11.md#page=82]]
- Structure of CUSIP (Issuer id + Issue code): [[During_Fixed_Income_Ch11.md#page=83]]
- Logic of Tap and Funge ISIN management: [[During_Fixed_Income_Ch11.md#page=82]]
- Technical difference between ISIN and CUSIP algorithms: [[During_Fixed_Income_Ch11.md#page=83-84]]

## Related

- [[Global_Note_Dematerialization]] — The system that tracks these codes.
- [[Bearer_Vs_Registered_Securities]] — Why identification is needed (to verifybeneficial interest).
- [[Settlement_Cycle]] — How ISINs help automate T+2 settlement.
- [[CUSIP_Issuer_Id_Glossary]] — Specific mapping of common Treasury IDs.
- [[Herstatt_Risk]]
- [[Rolling_Vs_Fixed_Settlement]]
- [[Delivery_Versus_Payment]]
- [[OTC_Trade_Lifecycle]]
- [[Settlement_Fails_And_Cures]]
- [[Settlement_Fails_And_Incentives]]
