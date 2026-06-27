---
title: "Autonomous Factors in Central Bank Balance Sheet"
aliases: [Autonomous Central Bank Factors, Banknotes, Government Deposits, Foreign Reserves, Net Autonomous Factors, Sterilization Need]
type: mechanism
tags: [monetary-operations, balance-sheet, liquidity]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: "Autonomous central bank balance sheet factors (banknotes, government deposits, foreign reserves, investment portfolios) reduce reserve availability for banking system and create sterilization demand."
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 24
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Autonomous factors are all central bank balance sheet items not under direct control of implementation function; they affect bank reserve availability and determine required monetary operations scale.

## 1. Core Logic / Mechanism

[RAW] **Definition** (Bindseil p.24, sec 2.5):
"Autonomous factors may be defined as all those central bank balance sheet items which are neither monetary policy operations nor the deposits of banks with the central bank. They are factors that are not under direct control of the monetary policy implementation function, although they may have an impact on the amount of deposits of banks with the central bank."

[RAW] **Primary Autonomous Factors**:
1. **Banknotes in Circulation** (B): Non-interest-bearing central bank liability; driven by public demand, not implementation officers
2. **Government Deposits** (G): Volatile; driven by tax collection/disbursement timing
3. **Foreign Reserves** (FR): Driven by FX intervention and external flows
4. **Investment Portfolios** (I): CB purchases of assets for investment, not policy, purposes
5. **Other Liabilities**: IMF credit lines, international facility withdrawals

[LLM] **Balance Sheet Identity**:
$$\text{Bank Deposits} = \text{Monetary Policy Operations} - \text{Net Autonomous Factors}$$

Where:
$$\text{Net Autonomous Factors} = B + G - FR - I$$

**Transmission Mechanism**:
- If banknotes increase (holiday cash demand) → autonomous liabilities rise → bank deposits fall unless CB injects liquidity through OMOs
- If government collects large tax inflow → government deposits rise → automatic drain on banking system liquidity
- If CB accumulates foreign reserves (BoP surplus) → autonomous assets rise → sterilization needed to maintain reserve targets

## 2. Worked Example

[LLM] **Scenario: Tax Collection Day**

Start of day: Bank deposits = 100 (target)

Government collects taxes: 25 million in public accounts (autonomous increase in G)

Net effect: Bank deposits = 100 - 25 = 75 (unintended drain)

CB response: Conduct repo/outright purchase operations to inject 25 million liquidity back into banking system

End of day: Bank deposits = 100 (target maintained)

This is routine autonomous factor management, distinct from policy rate steering.

[LLM] **Crisis Example: Capital Flight + BOP Pressure**

- Steady banknote withdrawal (public loses confidence): +5 autonomous
- FX intervention to support currency: +10 foreign reserves purchased
- Combined autonomous factors increase: -15 to bank deposits
- Without operational response: system would be severely reserve-deficient
- CB must expand OMOs substantially to maintain operational target

## 3. Failure Conditions / Boundaries

- **Forecast Uncertainty**: Some autonomous factors are highly unpredictable (e.g., holiday cash demand, government spending timing)
- **Liquidity Deficit Emergence**: If autonomous drain exceeds CB's operational capacity, system becomes illiquid → forced fire sales
- **Coordination Failure**: Lack of government-CB coordination on deposit management creates unnecessary volatility
- **Interest Rate Volatility**: Large autonomous shocks can overwhelm OMO adjustments, causing rate spikes if CB lacks sufficient counterparties
- **Policy Transmission Impairment**: Intraday autonomous shocks can cause overnight rate to deviate significantly from target between implementation sessions

## Related
- [[Liquidity_Management_Operations]]
- [[Central_Bank_Balance_Sheet_Structure]]
- [[Reserve_Requirements_Mechanics]]
- [[Interbank_Money_Market_Mechanism]]
- [[Open_Market_Operations_And_Instruments]]
- [[Central_Bank_Balance_Sheet_Trilemma]]
- [[Central_Bank_Operational_Frameworks]]
