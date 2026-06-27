---
title: "Standing Facilities Types and History"
aliases: [Discount Facility, Borrowing Facility, Deposit Facility, Lombard Facility, Standing Facility Evolution, Central Bank Standing Facilities]
type: mechanism
tags: [monetary-operations, standing-facilities, history]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "Three modern standing facility types (discount, borrowing, deposit) evolved from 19th-century rediscount practice; each serves specific liquidity provision/absorption function."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 70
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Standing facilities are central bank operations initiated by banks under pre-announced terms; three variants exist: two liquidity-providing (discount, borrowing) and one liquidity-absorbing (deposit facility).

## 1. Core Logic / Mechanism

[RAW] **Definition & Classification** (Bindseil p.70, sec 6.1):
Standing facilities = "central bank operations at the initiative of banks, on the basis of a commitment of the central bank to allow such operations under certain conditions."

Three variants:

### 1A. Discount Facility (Liquidity-Providing)
[RAW] "Banks can sell certain short-term paper to the central bank at any time, whereby the discount rate specified by the central bank is applied to calculate the price on the basis of the securities' cash-flows."

**Mechanism**:
- Bank presents eligible short-term debt instrument (bill of exchange, T-bill, commercial paper)
- CB applies **discount rate** $r_d$ to calculate present value
- PV = Face Value / (1 + $r_d$ × days/360)
- Bank receives cash immediately; CB acquires income-yielding instrument

**Historical Role**: 
- Predominant tool until mid-20th century (pre-1914 Bank of England, Reichsbank, early Fed)
- Fed still calls its borrowing facility "Discount Window" (legacy nomenclature)
- Now largely obsolete in modern central banking (banks prefer OMO repos)

### 1B. Overnight Borrowing Facility (Liquidity-Providing)
[RAW] "Banks can borrow at any time against the provision of eligible collateral at some rate specified by the central bank."

**Mechanism**:
- Bank pledges eligible collateral (bonds, bank guarantees)
- CB lends amount = Collateral Value × (1 - Haircut)
- Overnight maturity (usually); rolled daily
- Rate $r_L$ posted by CB; banks can access at will

**Modern Implementation**:
- ECB: Marginal Lending Facility (MLF) at rate $i^* + 100$ bps
- Fed: Discount Window with various term lengths and rates
- BoE: Standing Lending Facility

**Advantage over Discount Facility**: 
- Doesn't require specific eligible paper (any collateral eligible)
- More flexible for diverse portfolios
- Enables continuous access without paper supply constraint

### 1C. Deposit Facility (Liquidity-Absorbing)
[RAW] "Banks can deposit at any time funds with the central bank on a specific account where it gets remunerated at a specific rate."

**Mechanism**:
- Bank holds excess reserves; places them in deposit facility
- Rate $r_D$ (lower than policy rate $i^*$)
- Overnight maturity; can withdraw freely
- De facto floor for overnight rate

**Modern Implementation**:
- ECB: Deposit Facility rate at $i^* - 50$ bps
- Fed: Overnight Reverse Repo (ORR) facility post-2013; Interest on Excess Reserves (IORR) 2008-present
- Effect: Prevents overnight rate from falling below deposit facility rate (no arbitrage)

## 2. Worked Example

[LLM] **Day 1: Bank Facing Liquidity Needs**

Bank balance sheet at noon:
- Cash: 50
- Eligible collateral: 200
- Required reserves: 100
- Current reserve balance: 60 (short by 40)

**Option A**: Use Discount Facility
- If CB offers discount rate 2.0% on eligible bills
- Bank sells $40 face value of 90-day commercial paper
- Proceeds: $40 / (1 + 0.02 × 90/360) = 40 / 1.005 = $39.8
- Bank short-funded by $39.8, needs alternative

**Option B**: Use Borrowing Facility
- Bank pledges $200 collateral
- Haircut: 10%
- Available borrowing: $200 × 0.9 = $180
- Bank borrows exactly $40 at rate 2.5%
- Cost: $40 × 0.025 × 1/365 = $0.0027 (daily cost)

**Option C**: Hold excess deposits in Deposit Facility
- Bank has $50 in cash, rate 1.5% (lower than 2% borrowing cost)
- Bank leaves $50 on deposit facility
- Cost: Foregone return vs. investing elsewhere
- Result: Deficient in reserves by 40, but has liquidity buffer

[LLM] **Day 1 Reality**: Bank likely uses combination
- Borrows $40 from CB at 2.5% (borrowing facility)
- Holds $50 excess at 1.5% (deposit facility)
- Net cost: Borrow $40 × 0.025 × 1/365 - $50 × 0.015 × 1/365 ≈ $0.0014 per day

## 3. Historical Evolution

[RAW] **Pre-1914: Rediscount Dominant**
- Discount facilities only mechanism for liquidity provision
- Banks discounted commercial paper with CB
- Rediscount rate = monetary policy signal (Thornton 1802, Bagehot 1873)
- No deposit facility (surplus liquidity deployed elsewhere, not with CB)

[RAW] **1914-1980: Discount + Borrowing Facilities**
- Borrowing facilities added (more flexible, broader collateral)
- Discount facilities declined in use
- Some CBs maintained both for redundancy

[RAW] **1980-Present: All Three**
- Modern symmetric corridor framework requires all three
- Deposit facility essential for rate floor
- Borrowing facility essential for rate ceiling
- Discount facilities largely historical remnant

**ECB Structure** (established 1999):
- Marginal Lending Facility (borrowing): $i^* + 100$ bps
- Deposit Facility: $i^* - 50$ bps
- No formal discount facility
- Classic symmetric 150 bps corridor

## 4. Failure Conditions / Boundaries

- **Collateral Constraint**: If bank exhausts eligible collateral, borrowing facility becomes unavailable (see [[Collateral_Constraints_In_Monetary_Operations]])
- **Stigma**: Regular use of standing facilities signals distress → market spreads widen → bank forced to pay premium or ration credit
- **Intraday Gridlock**: If multiple banks hit collateral limits simultaneously, standing facilities insufficient → asset fire sales
- **Counterparty Risk**: Bank bankruptcy risk may cause CB to restrict facility access (BoPI principle: "wide but not deep")

## Related
- [[Interest_Rate_Corridor_And_Standing_Facilities]]
- [[Standing_Facilities_Optimal_Width_In_Symmetric_Corridor]]
- [[Central_Bank_Collateral_Frameworks]]
- [[Lender_Of_Last_Resort_Mechanism]]
- [[One_Directional_Standing_Facility_Implementation]]
