---
title: Lucas Aggregate Supply Function
aliases:
- Lucas Island Model
- Unanticipated Money Shock
- Lucas Paradox
- Phillips Curve (Lucas version)
type: mechanism
tags:
- macroeconomics
- monetary-policy
- expectations
- information-asymmetry
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo"
provenance: Perry Warjiyo - Central Bank Policy (2019)
thesis: The Lucas aggregate supply function asserts that real output only responds
  to unanticipated changes in the money supply, as imperfect information leads producers
  to mistake aggregate price level shifts for changes in the relative demand for their
  specific products.
source_refs:
- file: Perry_Central_Bank_Policy_P3.md
  page: 57
- file: Perry_Central_Bank_Policy_P3.md
  page: 58
- file: Perry_Central_Bank_Policy_P3.md
  page: 59
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

The Lucas Island Model (1973) provides a Neoclassical explanation for why money is not neutral in the short run. Alexander Düring bóc tách ranh giới của kỳ vọng hợp lý, trong khi Perry Warjiyo giải mã cơ chế tại sao **Thông tin bất đối xứng** lại biến một cú shock tiền tệ thành một cú hích sản lượng. Theo Lucas, các nhà cung cấp (suppliers) sống trên các "hòn đảo" thông tin riêng biệt và không thể ngay lập tức phân biệt được giữa lạm phát chung và nhu cầu tăng cao cho riêng sản phẩm của họ. [[Perry_Central_Bank_Policy_P3.md#page=57-58]]

## Mechanism: The Extraction Problem

The supplier's decision to increase output $y_i$ depends on the perceived price difference:
$$y_{i,t} = \beta(p_{i,t} - E[p_t | I_{i,t}])$$

### 1. The Information Set ($I_{i,t}$)
Suppliers know the specific price of their own goods ($p_i$) but only have a "prior" expectation of the general price level ($E[p]$). [[Perry_Central_Bank_Policy_P3.md#page=58]]

### 2. The Signal vs. Noise Filter
Using **Bayes Rule**, suppliers attempt to extract the "relative demand signal" from the "aggregate price noise."
- **The Signal:** If local prices rise, is it because my product is popular (relative shock $z_i$)?
- **The Noise:** Or is it because the central bank printed too much money (aggregate shock)?
- **The Error:** Because information is imperfect, suppliers attribute part of the aggregate inflation to local demand, leading them to increase production ($y \uparrow$). [[Perry_Central_Bank_Policy_P3.md#page=58]]

### 3. The Unanticipated Requirement
The most critical conclusion of the model is that **anticipated money changes have zero effect on output**.
- If the central bank announces a 5% increase in money supply, $E[m|I]$ adjusts immediately, $E[p]$ adjusts, and the supplier is not "tricked" into increasing output.
- Only the **unanticipated** part $(m - E[m|I])$ drives the real economy. [[Perry_Central_Bank_Policy_P3.md#page=59]]

## Strategic Implications: Policy Ineffectiveness

The Lucas Supply Function is the foundation of the **Policy Ineffectiveness Proposition**.
- It suggests that central banks cannot systematically "engineer" growth through monetary expansion, as the public will eventually learn the reaction function and incorporate it into their expectations ($E[p]$), restoring long-term neutrality. [[Perry_Central_Bank_Policy_P3.md#page=59]]

## Evidence / Source Anchors

- Analysis of the decentralized 'Island' market model and imperfect information: [[Perry_Central_Bank_Policy_P3.md#page=57-58]]
- Mathematical derivation of the Lucas aggregate supply function (Equation 20): [[Perry_Central_Bank_Policy_P3.md#page=59]]
- Proof that output only responds to unanticipated money disturbances (Equation 22): [[Perry_Central_Bank_Policy_P3.md#page=59]]
- Discussion on the weighted average of prior mean and special price shocks via Bayes rule: [[Perry_Central_Bank_Policy_P3.md#page=58]]

## Related

- [[Neutrality_Of_Money]] — The long-term state that Lucas attempts to reconcile with short-term data.
- [[Lucas_Critique]] — The logical extension: why historical correlations fail when policy rules change.
- [[Expectations_Hypothesis_In_Yield_Curves]] — How these unanticipated shocks are priced into the curve.
- [[Phillips_Curve_Expectations_Augmented]] — The empirical curve that the Lucas function explains.
