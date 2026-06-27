---
title: Liquidity Operations
aliases:
- Central Bank Operations
- Monetary Policy Tools
- Standing Facilities
type: mechanism
tags:
- central-banking
- implementation
- monetary-policy
- risk-management
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch01.md"
thesis: The operational framework of a central bank is a predefined set of liquidity
  providing and absorbing operations that signal the monetary policy stance and provide
  a backstop for financial stability.
source_refs:
- file: Fixed_Income_Alexander_During_Ch01.md
  page: 50
- file: Fixed_Income_Alexander_During_Ch01.md
  page: 46
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

The success of monetary policy depends on the predictability of central bank actions. Alexander Düring explains that by pre-defining their operational tools, central banks allow market participants (particularly commercial banks) to form stable expectations, thereby minimizing unintended side effects. These operations are the mechanical levers used to expand or contract [[Base_Money]] to guide market interest rates toward the central bank's target.

## Mechanism

A central bank's operational framework is typically structured into three functional sets of operations:

1. **Standard Operations:**
   - **Purpose:** Used on a regular basis (e.g., weekly or bi-weekly).
   - **Function:** Signals the general monetary policy stance in normal economic times.
   - **Tools:** Main Refinancing Operations (ECB), Open Market Operations (Fed). [[Fixed_Income_Alexander_During_Ch01.md#page=50]]
2. **Emergency Operations (LOLR):**
   - **Purpose:** Used only in situations of extreme market stress or individual bank failure.
   - **Function:** To prevent systemic contagion and bank runs.
   - **Tools:** Emergency Liquidity Assistance (ELA), Discount Window. [[Fixed_Income_Alexander_During_Ch01.md#page=50]]
3. **Non-Standard Operations:**
   - **Purpose:** Used broadly but only during times of particular economic exigency (e.g., the 2008 crisis or the 2020 pandemic).
   - **Function:** Directly managing the yield curve or providing term liquidity.
   - **Tools:** Large-scale asset purchases (QE), Targeted longer-term refinancing operations (TLTROs). [[Fixed_Income_Alexander_During_Ch01.md#page=50]]

### Liquidity Directionality
Every operation in this framework falls into one of two directions:
- **Liquidity Providing:** Increases the central bank's liabilities (injects cash). Includes purchases, loans, and rediscounting.
- **Liquidity Absorbing:** Reduces the central bank's liabilities (pulls cash back). Includes asset sales and reverse repos. [[Fixed_Income_Alexander_During_Ch01.md#page=50]]

### Boundaries / Conditions

### 1. Hysteresis and Stability
Central bank frameworks exhibit strong **Hysteresis**—they tend to change slowly because the side effects of adjusting established plumbing can be unpredictable. Stability in these frameworks is a key desideratum for efficient transmission. [[Fixed_Income_Alexander_During_Ch01.md#page=46-50]]

### 2. Collateral Requirement
Central banks never lend "naked." To mitigate moral hazard and protect their own balance sheets, all liquidity provision is done against **Collateral**. 
- **Rationale:** If central banks provided uncollateralized loans, banks could socialise their losses by lending to risky related parties and then defaulting on their central bank obligation. [[Fixed_Income_Alexander_During_Ch01.md#page=51]]

## Evidence / Source Anchors

- Classification of operations (Standard, LOLR, Non-standard): [[Fixed_Income_Alexander_During_Ch01.md#page=50]]
- Directionality of liquidity (Providing vs. Absorbing): [[Fixed_Income_Alexander_During_Ch01.md#page=50]]
- Desiderata for frameworks (Parsimony, Stability): [[Fixed_Income_Alexander_During_Ch01.md#page=46]]
- Discussion on the necessity of collateral to prevent moral hazard: [[Fixed_Income_Alexander_During_Ch01.md#page=51]]
- Note on hysteresis in operational design: [[Fixed_Income_Alexander_During_Ch01.md#page=50]]

## Related

- [[Base_Money]] — The liabilities that these operations are designed to control.
- [[Operational_Framework_Principles]] — The design rules used to choose between these operations.
- [[Lender_Of_Last_Resort]] — The emergency set of operations mentioned here.
- [[Symmetric_Interest_Rate_Corridor]] — The standard pre-crisis way these operations were combined.
- [[Asymmetric_Lending_Corridor]] — The post-crisis framework resulting from non-standard operations.
- [[Bank_Money_Creation]] — The process that these operations indirectly attempt to stimulate or restrain.
