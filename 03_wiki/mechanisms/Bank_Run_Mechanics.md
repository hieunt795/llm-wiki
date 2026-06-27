---
title: "Bank Run Mechanics"
aliases: [Bank Runs, Retail Depositor Runs, Wholesale Funding Runs, Self-Fulfilling Illiquidity]
type: mechanism
tags: [liquidity-crisis, systemic-risk, contagion, deposits]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil LOLR Crisis"
thesis: "Bank runs are self-fulfilling equilibria where rational depositors withdraw funds due to legitimate illiquidity risk; the threat of runs creates multiple equilibria (no-run vs run) that can tip from stability to catastrophic collapse with small changes in liquidity or equity."
source_refs:
  - file: "Bindseil LOLR"
    page: 153-160
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Bank run mechanics turn on the coordination problem between depositors: if others run, running becomes individually optimal; if others stay, staying is optimal. Banks face a two-way liquidity-equity constraint determining stability: positive equity AND sufficient liquid assets (Λ(2+E) ≥ 1) required for stable no-run equilibrium.

## 1. Core Definition and Self-Fulfilling Nature

[RAW] Per Bindseil (p.153):

"Bank runs are a common feature of banking crises, with 62% of crises experiencing momentary sharp reductions in total deposits... The particularity of bank runs is their self-fulfilling property: once a run on a bank starts, it can lead to the default of the bank, confirming the individual wisdom of those who were first in the queue to withdraw their money."

Historical examples (p.153-154):
- Northern Rock (2007): First UK retail deposit run since Victorian times
- Lehman collapse (Sep 2008): Indirect runs via banknote demand surge
- Greek banks (2011-2012): "Cold" electronic runs through deposit transfers to non-Greek euro banks; corporate+household deposits fell EUR 203B→151B (end 2010→2012)

## 2. Game-Theoretic Bank Run Model

[RAW] Bindseil (p.154-159) provides strategic game framework. Assume:
- Bank balance sheet: Liquid assets Λ(2+E), Illiquid assets (1-Λ)(2+E), Equity E
- Two depositors, each with 1 unit deposits
- Depositors choose: K (keep) or R (run)
- Transaction cost of withdrawal: ε
- Disorderly default cost: C (assumed C > E, wiping out positive equity)

### 2.1 Case A: Sufficient Liquidity, Positive Equity
Condition: 2 > Λ(2+E) ≥ 1 and E > 0

"In this case, default occurs when both depositors run, but not when only one of them runs."

Payoff matrix:
```
Depositor 2
          Keep    Run
Keep   (1,1)    (1, 1-ε)
Run    (1-ε,1)  (1-(C-E)/2, 1-(C-E)/2)
```

**Equilibrium:** Unique no-run equilibrium (K,K)
**Stability:** Social optimum achieved; no coordination failure

### 2.2 Case B: Insufficient Liquidity, Positive Equity
Condition: Λ(2+E) < 1 and E > 0

"Already the withdrawal of one depositor will lead the bank to default."

Recovery ratio: rr = [(1-Λ)(2+E) - C] / (2 - Λ(2+E)) < 1

Payoff matrix (simplified):
```
Depositor 2
                Keep                 Run
Keep   (1, rr)              (Λ(2+E)+rr(1-Λ(2+E)), rr)
Run    (rr, Λ(2+E)+rr(...))  (Λ(2+E)/2+rr(...), Λ(2+E)/2+rr(...))
```

**Equilibrium:** Two equilibria (K,K) superior; (R,R) inferior
**Stability:** Multiple equilibria; sunspot shocks trigger transition

[RAW] Bindseil (p.158-159): "In this case, two equilibria are observed—the superior, in which no depositor runs, and the inferior one, in which both run."

### 2.3 Case C: Sufficient Liquidity, Negative Equity
Condition: 2 ≥ Λ(2+E) ≥ 1 and E < 0

"It is assumed that in any case, the negative equity is discovered after the run game is played, and that the bank is then liquidated."

Default cost C materializes upon supervisor closure (not just illiquidity).

**Equilibrium:** Unique inferior (R,R) equilibrium (prisoner's dilemma)
**Dynamics:** Running strictly dominant strategy; no run equilibrium unstable

## 3. Liquidity-Equity Trade-off Constraint

[RAW] Bindseil (p.159):

"Only if the bank has positive equity and sufficient liquidity to sustain at least one depositor running (i.e. E ≥ 0 and Λ(2+E) ≥ 1) will the social optimum be achieved."

However, competitive forces push toward minimum stability:

[RAW] (p.159): "In principle, it could be assumed that banks have themselves an interest in respecting this constraint... However, competition is likely to force banks to go to the limit in terms of asset-liability structure, i.e. banks will choose liquid assets to be equal to exactly 1, and not hold more liquid assets and more equity than necessary to sustain a single no-run equilibrium."

**Key insight:** Banks profit-maximize by holding Λ(2+E) = 1 exactly, placing themselves on knife-edge stability.

## 4. Asset Liquidity Deterioration and Contagion

[RAW] Bindseil (p.159-160):

"If banks implement the profit-maximizing asset-liability structure for a given asset liquidity, the problem arises that if asset liquidity deteriorates, in the sense that a part of the assets that were formerly liquid are no longer liquid... then what was formerly a stable no-run equilibrium will suddenly turn into a vulnerable situation with two equilibria, and a significant probability of a bank run."

**Mechanism:** Decline in asset quality (Λ↓) or asset value (E↓) creates:
- Smooth transition from Case A → Case B → Case C
- Threshold effects triggering run probability jump
- Fire-sale spillovers amplifying contagion

## 5. Wholesale Funding Runs and Investor Strikes

[RAW] Bindseil (p.159-160):

"In principle, the logic of bank runs also applies to the roll-over of debt securities issued, even if the potential dynamics are different, and may be more limited if the maturity dates of debt are well distributed and average duration of liabilities is high... The best protection against such runs, called sometimes 'investor strikes', is to issue longer-term paper."

**2007-2008 Example:** Special Purpose Vehicles (SPVs) holding long-term assets but issuing short-term Asset Backed Commercial Paper (ABCP):

[RAW] (p.159-160): "The pre-2007 practice of setting up special purpose vehicles ('SPVs') holding long-term assets and issuing short-term (say three months) Asset Backed Commercial Papers ('ABCPs') was going in the opposite direction, and was one of the triggers of the 2007/2008 liquidity crisis."

Cost of ABCP funding surged from 10-15 bps to 100+ bps post-Aug 2007, cutting off SPV rollover and forcing central bank liquidity assistance.

## 6. Information Asymmetry and Disclosure Trade-offs

[RAW] Bindseil (p.160):

"Regulators would therefore sometimes face a trade-off: while enhancing transparency may be useful to strengthen market discipline, it could also increase the probability of a destabilization of liabilities."

**Mechanism:** More information enables depositors to distinguish weak from strong banks; if weak banks known, runs discriminate; if opaque, uncertainty creates indiscriminate contagion risk.

[RAW] (p.160): "Others have argued that more information can reduce the probability of bank runs, e.g. Schotter and Yorulmazer (2009)... The intuition is that as weak banks would fail anyway, expected welfare would be higher with disclosure as it is likely to prevent runs on strong banks."

## 7. Policy Implications and LOLR Response

Bank run mechanics justify:

1. **Deposit Insurance:** Break information contagion by guaranteeing depositor recovery
2. **Liquidity Regulation:** Impose Λ', E' buffers preventing easy transition to multiple-equilibria cases
3. **LOLR Function:** Central bank provides secured funding, effectively converting illiquid assets to liquid collateral
4. **Orderly Resolution:** Supervisor closure stops run by converting deposits to insurance claim (removes uncertainty)

## 8. Boundary Conditions and Failure Cases

Bank runs avoid catastrophe when:
- Deposit insurance credible and quickly paid
- Central bank LOLR available at penalty rate (Bagehot rule)
- Market information sufficient to distinguish solvency from illiquidity
- Resolution/bankruptcy swift and transparent

Runs become systemic when:
- Deposit insurance exhausted (large bank failures)
- LOLR unavailable or stigmatized (ECB ELA reputational concerns)
- Information opacity prevents good/bad discrimination
- Contagion via interconnectedness spreads to solvent institutions

## Related
- [[Asset_Fire_Sales_Mechanism]]
- [[Financial_Interconnectedness_Networks]]
- [[Lender_Of_Last_Resort_Mechanism]]
- [[Emergency_Liquidity_Assistance]]
- [[Financial_System_Stability_FSS_Concept]]
