---
title: Settlement Fails and Fails Charges
aliases:
- Fails Disincentive
- Negative Repo Environment Fails
type: mechanism
tags:
- market-infrastructure
- repo-market
- interest-rates
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch11.md"
thesis: Because low-interest-rate environments and heavily negative 'Special' repo
  rates annihilate the natural economic penalty of failing to deliver a security,
  structural market architecture requires the manual imposition of brutal fiat 'Fails
  Charges' to deter systemic gridlock.
source_refs:
- file: Fixed_Income_Alexander_During_Ch11.md
  page: 95
created: '2026-04-16'
updated: '2026-04-16'
---

## Thesis

In the fixed income ecosystem, when a seller utterly fails to deliver a promised bond on the agreed settlement date, the transaction does not automatically cancel, nor does it immediately trigger a brutal formal "default." The trade remains mathematically frozen as an "open fail." However, the structural economic penalty built into the system to prevent these fails—which relies heavily on high natural money market interest rates—completely collapses in zero-bound or heavily "special" repo environments, demanding artificial fiat intervention to protect settlement integrity.

## Mechanism

### The Natural Disincentive (High-Rate Environments)
A settlement fail fundamentally acts as a zero-percent loan. 
If Counterparty A sells a bond to Counterparty B but fails to deliver, Counterparty B mathematically retains the purchase cash in its own account until the bond actually arrives.
- *The Penalty:* Counterparty A does not physically receive the cash, thus aggressively bleeding the opportunity cost of the overnight interest rate. Counterparty A is effectively "borrowing" the bond at a 0% Repo Rate. If the prevailing market cash rate is 5%, Counterparty A loses 5% annualized every single day they fail to deliver. The pain forces rapid resolution.

### The Breakdown (ZIRP & Special Collateral)
This elegant built-in penalty absolutely vaporizes under two conditions:
1. **Zero Interest Rate Policy (ZIRP):** If general cash interest rates are 0.00%, Counterparty A suffers exactly zero opportunity cost by not receiving the cash. The incentive to fix the fail vanishes.
2. **Special Collateral (Negative Repo):** If the specific bond is heavily shorted, it trades "Special" in the repo market, frequently carrying deeply negative financing rates (e.g., -5%). If the market rate to legally borrow the bond is -5%, but intentionally "failing to deliver" the bond carries an implicit cost of 0%, traders represent a mathematical arbitrage by intentionally choosing to fail.

### The Artificial Solution: Fails Charges
Because the natural penalty breaks, regulators constructed artificial market frictions: Fails Charges. In 2009, the US market imposed a punitive flat 3% fee (minus the Target Fed Funds Rate) explicitly levied against failing counterparties precisely to erase the arbitrage of failing in low-interest environments.

### Boundaries / Conditions

### Unwinding the Fail
If explicit Fails Charges fail to correct the behavior, the counterparty suffering the fail has access to ultimate, hyper-aggressive escalations:
- **Buy-Ins:** An incredibly destructive transaction where the aborted buyer re-enters the active open market, purchases the specific bond regardless of the extreme premium demanded by sellers, and legally forces the original failing counterparty to absorb the entire financial loss of the premium.

## Evidence / Source Anchors

- Analyzing the natural fail penalty functioning explicitly as a 0% repo loan backed by the withheld cash: [[Fixed_Income_Alexander_During_Ch11.md#page=95]]
- The failure of this penalty inside environments with extremely negative special repo rates (>5% special): [[Fixed_Income_Alexander_During_Ch11.md#page=95]]
- The historical response of implementing a flat 3% fails fee in the US, and the ultimate escalation to European CSDR mandatory buy-ins: [[Fixed_Income_Alexander_During_Ch11.md#page=95]]

## Related

- [[Delivery_Versus_Payment_DvP]] — the operational framework that enforces the withholding of cash during a fail
- [[Negative_Interest_Rate_Policy_NIRP_Mechanics]] — the macro environment that destroys the natural fails penalty
