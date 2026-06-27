---
title: Prime Broker
aliases:
- PB
- Prime Brokerage
type: definition
tags:
- hedge-funds
- securities-lending
- leverage
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Robert Kosowski | Salih N. Neftci
provenance: Neftci_Principles.md
thesis: The central intermediary providing settlement, custody, leverage, and securities
  lending infrastructure essential for hedge fund operations.
source_refs:
- file: Neftci_Principles.md
  page: 233
created: '2024-05-21'
updated: '2024-05-21'
---

## Thesis
Prime brokers (PBs) act as the backbone of the hedge fund industry, consolidating operational and financial services that allow funds to execute complex strategies, particularly those involving leverage and short selling.

## 1. Core Logic / Mechanism
[RAW] Prime brokers offer settlement, custody, and securities lending services to hedge funds. Prime brokers earn their money from commissions and by charging a premium over money market lending rates for loans. Prime brokers also provide trade execution, stock lending, leveraged finance, and other essential services to hedge funds.

[LLM] The Prime Brokerage model transforms the fragmented needs of a hedge fund into a centralized service suite.
- **Centralization**: By acting as the sole interface for settlement and custody, PBs reduce operational friction for funds dealing with multiple executing brokers.
- **Credit Intermediation**: PBs provide [[Leveraged_Finance]], allowing funds to multiply their activities (typically by a factor of 3 or more). This leverage is funded by the PB charging a spread over money market rates.
- **Information Advantage**: PBs maintain specialized securities lending divisions that track the availability of borrowable assets, which is critical for the execution of [[Short_Selling]] strategies.

## 2. Worked Example
[RAW] Such leverage can multiply a hedge fund’s activities by a factor of 3 or more, but increased capital requirements for banks mean that leverage levels are low in hedge funds, especially compared to banks where they are typically 10 times higher than for hedge funds.

[LLM] **Leverage Comparison**:
| Entity | Typical Leverage Ratio | Driver/Constraint |
|---|---|---|
| Hedge Fund (via PB) | ~3x | PB risk appetite, Bank capital requirements |
| Commercial/Investment Bank | ~30x+ (pre-crisis) / ~10-15x (post-Basel) | Regulatory capital (RWA), Internal models |

## 3. Failure Conditions / Boundaries
- **Counterparty Risk**: If a PB fails (e.g., Lehman Brothers 2008), the hedge fund's assets held in custody or as collateral may be frozen, leading to fund liquidation.
- **Regulatory Constraints**: Increased capital requirements for banks (Basel III/IV) directly limit the amount of leverage PBs can offer to hedge funds, potentially reducing market liquidity.
- **Information Leakage**: Since the PB sees all of a fund's positions, there is a theoretical risk of information leakage, though strictly managed by "Chinese Walls."

## Related
- [[Hedge_Fund_Industry]]
- [[Short_Selling]]
- [[Securities_Lending_Mechanics]]
- [[Leveraged_Finance]]
