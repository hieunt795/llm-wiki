---
title: Financial Accelerator Mechanism
aliases:
- Procyclicality Amplifier
- External Finance Premium
- Collateral Constraint Feed-back
type: mechanism
tags:
- monetary-policy
- systemic-risk
- macro-financial
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The financial accelerator is a feedback loop where shocks to the economy (e.g.,
  interest rate changes) are amplified by their impact on borrower balance sheets
  and collateral values, resulting in larger-than-expected fluctuations in credit
  supply and real output.
source_refs:
- file: Perry_Central_Bank_Policy_P3.md
  page: 133
- file: Perry_Central_Bank_Policy_P3.md
  page: 134
- file: Perry_Central_Bank_Policy_P3.md
  page: 136
created: '2026-04-18'
updated: '2026-04-18'
---

## Thesis

Traditional models assume that a 1% rate hike has a linear 1% effect on demand. The **Financial Accelerator** (Bernanke, Gertler, and Gilchrist, 1999) proves this is false. Because market imperfections (asymmetric information) exist, interest rates affect the **External Finance Premium**—the difference between internal and external funding costs.

## Mechanism: The Procyclical Loop

### 1. In an Upswing (Ease)
- **CB lowers rates:** Economic activity improves, pushing up asset prices.
- **Wealth Effect:** Net worth of borrowers increases, raising the value of their **Collateral**.
- **Risk Mitigation:** Banks see lower risk (lower NPLs), reducing the **External Finance Premium**.
- **Expansion:** Lower premium and higher collateral allow for even more borrowing, further inflating asset prices.
- **Amplification:** The final increase in output ($Y$) is far larger than the original interest rate cut would suggest.

### 2. In a Downswing (Tighten)
- **CB raises rates:** Cash flow declines, asset prices drop.
- **Collateral Collapse:** Borrowers hit their **Collateral Constraints** (Equations 18 & 23 in Perry).
- **Credit Crunch:** Banks raise the external finance premium due to higher risk perception.
- **Deleveraging:** Massive contraction in credit leads to a recession deeper than the interest rate hike alone would explain.

## Mathematical Representation: Collateral Constraints
Perry represents the binding constraint as:
$$x_1 = [p_0 y_0 - (1+r)L_0] + \frac{qW_1}{\alpha(1+r)}$$
Where $x_1$ (investment) is limited by the market value of collateral $qW_1$ and the inverse of the LTV ratio $\alpha$.

## Evidence / Source Anchors

- Bernanke, Gertler, and Gilchrist (1999) external finance premium model: [[Perry_Central_Bank_Policy_P3.md#page=133]]
- Definition of the financial accelerator in corporate and household sectors: [[Perry_Central_Bank_Policy_P3.md#page=133]]
- Figure 5.3: Impact of binding collateral constraints on output: [[Perry_Central_Bank_Policy_P3.md#page=135]]

## Related

- [[Monetary_Policy_Transmission_Mechanism_MPTM]] — The context of these amplifiers.
- [[Stiglitz_Monetary_Paradigm_Credit_Matters]] — The theoretical basis for credit importance.
- [[Risk_Taking_Channel_Mechanism]] — How this accelerator interacts with investor psychology.
