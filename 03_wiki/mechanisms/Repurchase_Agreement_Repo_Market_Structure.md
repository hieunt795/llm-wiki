---
title: Repurchase Agreement (Repo) Market Structure
aliases:
- Repo
- Repurchase Agreement
- GC Repo
- Specials Repo
- Hợp đồng mua lại
type: mechanism
tags:
- money-market
- repo
- liquidity
- collateral
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch15.md
thesis: The repo market is the primary infrastructure for secured interbank lending,
  functioning as a dual-purpose machine for both cash management (General Collateral)
  and securities sourcing (Specials).
source_refs:
- file: During_Fixed_Income_Ch15.md
  page: 126
- file: During_Fixed_Income_Ch15.md
  page: 127
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

A **Repurchase Agreement (Repo)** is a simultaneous sale and agreement to buy back the same security at a future date. While legally documented as a sale, it is economically a **secured deposit**. Alexander Düring highlights that repo has effectively superseded unsecured interbank lending due to increased risk awareness and regulatory capital incentives. The market is fundamentally bifurcated into GC (General Collateral) for cash-driven trades and Specials for security-driven trades. [[During_Fixed_Income_Ch15.md#page=126]]

## Mechanism: The Two Market Segments

### 1. General Collateral (GC) - The Cash Sourcing Machine
- **Objective:** To borrow or place cash in a secure way.
- **Collateral:** Any security from a broadly defined set (e.g., "German government bonds 1-10Y").
- **Discretion:** The party accepting the cash chooses which specific bonds to deliver.
- **The Rate:** GC repo rates are generally lower than unsecured rates, reflecting the safety of the collateral. [[During_Fixed_Income_Ch15.md#page=126]]

### 2. Specials (Specific) - The Security Sourcing Machine
- **Objective:** To borrow a specific security (e.g., for delivery to a futures exchange or to cover a short sale).
- **The Mechanism:** When demand for a specific bond is high, cash lenders are willing to accept a repo rate **below the GC rate** just to hold that bond.
- **The Spread:** A bond is said to be "20bp special" if its repo rate is 20 basis points below the GC rate. In extreme cases, repo rates can turn negative even when GC rates are positive. [[During_Fixed_Income_Ch15.md#page=127]]

## Strategic Functions of Repo

- **Short Selling Support:** Repo is the only way a dealer can sell a security they do not own. They "buy the bond in repo" (borrow it), deliver it to the customer, and hope to buy it back cheaper later to return it to the repo counterparty. [[During_Fixed_Income_Ch15.md#page=127]]
- **Monetary Policy Implementation:** Central banks (like the ECB and BoJ) use repo as their primary tool to inject or absorb liquidity. [[During_Fixed_Income_Ch15.md#page=129]]
- **Market Dominance (US Context):** [RAW-CLIP: Constâncio (2025-11-28)] Quy mô thị trường repo đã vượt xa thị trường không đảm bảo (unsecured). Tại Mỹ, thị trường repo qua đêm đạt quy mô khoảng $3.200 tỷ, trong khi thị trường không đảm bảo (Fed Funds) chỉ duy trì ở mức khoảng $160 tỷ. Điều này lý giải tại sao các biến số thanh khoản (SOFR) ngày càng trở nên quan trọng hơn lãi suất chính sách truyền thống (FFR).

## Boundaries / Conditions: Clearing and Costs
Repo rates are not uniform; they depend heavily on the clearing mechanism:
- **Centrally Cleared Repo:** Lower balance sheet costs lead to structurally lower rates.
- **Tri-party Repo:** Collateral is held by a third-party (custodian/CCP), eliminating the need for physical transfer and reducing operational costs. [[During_Fixed_Income_Ch15.md#page=127-128]]

## Evidence / Source Anchors

- Definition of Repo as a temporary exchange of cash for collateral: [[During_Fixed_Income_Ch15.md#page=126]]
- Distinction between cash-driven (GC) and security-driven (Specials) markets: [[During_Fixed_Income_Ch15.md#page=126-127]]
- Analysis of how "Specials" rates are quoted (basis points below GC): [[During_Fixed_Income_Ch15.md#page=127]]
- Role of repo in enabling short selling in the fixed income world: [[During_Fixed_Income_Ch15.md#page=127]]
- Description of the tri-party repo mechanism: [[During_Fixed_Income_Ch15.md#page=128]]

## Related

- [[General_Collateral_Vs_Special]] — Detailed dynamics of the repo spread.
- [[Collateral_Haircut_And_Wrong_Way_Risk]] — The technical protection for the cash lender.
- [[Rehypothecation_Mechanism_And_Risks]] — The danger of reusing collateral.
- [[Collateral_Transformation_And_TSLF]] — How repo facilities upgrade asset quality.
