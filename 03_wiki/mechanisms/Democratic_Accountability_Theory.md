---
title: Democratic Accountability Theory
aliases:
- Lý thuyết trách nhiệm giải trình dân chủ
- Rejection Cost Model of Accountability
type: mechanism
tags:
- central-banking
- accountability
- game-theory
- independence
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Perry Warjiyo
provenance: synthesized
thesis: Democratic accountability in central banking centers on the 'rejection cost'—the
  political cost incurred by a government when it overrides a central bank's policy
  proposal.
source_refs:
- file: Perry_Central_Bank_Policy_P4.md
  page: 331
- file: Perry_Central_Bank_Policy_P4.md
  page: 332
- file: Perry_Central_Bank_Policy_P4.md
  page: 333
- file: Perry_Central_Bank_Policy_P4.md
  page: 334
- file: Perry_Central_Bank_Policy_P4.md
  page: 335
- file: Perry_Central_Bank_Policy_P4.md
  page: 336
- file: Perry_Central_Bank_Policy_P4.md
  page: 337
created: '2024-04-24'
updated: '2024-04-24'
chapter: 11
---

# [[Democratic_Accountability_Theory]]

## Thesis
[WIKI/LLM] The Eijffinger et al. (1998) model demonstrates that central bank independence is not absolute but determined by the government's willingness to bear the political cost of rejecting central bank proposals. Transparency reduces the degree of uncertainty in central bank preferences, thereby lowering inflation expectations.

## Mechanism

### 1. The Rejection Cost Model
[RAW] The model assumes a scenario where the government delegates policy to a conservative central bank with stochastic preferences $x$. The government minimizes a loss function $L_G$ that includes a dummy variable $\delta$ and a rejection cost $c$:
$L_G = \frac{1}{2} \pi^2 + \frac{1}{2} (y - y^*)^2 + \delta c$ [[Perry_Central_Bank_Policy_P4.md#page=333]]
Where:
- $y = \pi - \pi^e + \epsilon$: Lucas-type supply function.
- $c$: political cost of rejecting the central bank's proposal.
- $\delta = 1$ if rejected, $0$ if accepted.

### 2. Independence vs. Accommodation
[RAW] The central bank is independent if the cost of rejecting its proposal outweighs the government's perceived benefits from its own preferred inflation target. Mathematically, the central bank is independent if:
$c > \frac{(x - f)^2}{4(x - 2 - f)^2} (y^* + \pi^e - \epsilon)^2$ [[Perry_Central_Bank_Policy_P4.md#page=334]]
If this condition is not met, the central bank must take **accommodative** actions, setting an inflation target that is a weighted average of its own and the government's preferences. [[Perry_Central_Bank_Policy_P4.md#page=334]]

### 3. Impact of Accountability and Transparency
[RAW] Accountability can be improved by shifting the burden of responsibility from the central bank to the government (reducing $c$). This results in:
1. **Weakened Independence:** A narrower range of independent action for the central bank.
2. **Higher Inflation Expectations:** As the government's influence increases.
3. **Better Shock Stabilization:** Since the government is typically less inflation-averse than a conservative central bank. [[Perry_Central_Bank_Policy_P4.md#page=335]] [[Perry_Central_Bank_Policy_P4.md#page=336]]

[RAW] Conversely, **Transparency** (reducing the uncertainty $h$ of the central bank's preferences) makes the central bank appear more conservative, lowering inflation expectations without necessarily undermining the core range of independence. [[Perry_Central_Bank_Policy_P4.md#page=336]] [[Perry_Central_Bank_Policy_P4.md#page=337]]

## Evidence / Source Anchors
- [[Perry_Central_Bank_Policy_P4.md#page=331]] — Introduction to democratic accountability and De Haan's characteristics.
- [[Perry_Central_Bank_Policy_P4.md#page=333]] — Definition of the government and central bank loss functions.
- [[Perry_Central_Bank_Policy_P4.md#page=334]] — Derivation of the independence condition based on cost $c$.
- [[Perry_Central_Bank_Policy_P4.md#page=335]] — Comparison of policy behavior in independent vs. accommodative zones (Fig 11.2).
- [[Perry_Central_Bank_Policy_P4.md#page=336]] — Effects of lowering rejection cost $c$ and preference uncertainty $h$.

## Related
- [[Central_Bank_Accountability_Characteristics]]
- [[Dimensions_of_Central_Bank_Independence]]
- [[Barro-Gordon_Model_of_Policy_Credibility]]
