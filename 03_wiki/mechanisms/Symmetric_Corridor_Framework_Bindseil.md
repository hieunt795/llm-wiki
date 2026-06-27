---
title: Symmetric Corridor Approach with OMO Volume Set by the Central Bank
aliases:
- Hệ thống hành lang đối xứng
- Mid-point targeting
type: mechanism
tags:
- monetary-policy
- interest-rate-corridor
- OMO
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Ulrich Bindseil
provenance: "Bindseil_Monetary_Policy_Operations.md"
thesis: The central bank targets the middle of a corridor formed by two standing facilities
  by managing reserve scarcity such that the expected interbank rate is the weighted
  average of the facility rates, gimbaled by the probability of being short or long
  at day-end.
source_refs:
- file: Bindseil_Monetary_Policy_Operations.md
  page: 55
created: '2026-04-26'
updated: '2026-04-26'
chapter: 4
---

# [[Symmetric_Corridor_Approach]]

## Thesis
[WIKI] In a symmetric corridor system, the central bank sets a borrowing rate ($i_B$) and a deposit rate ($i_D$) around a target rate ($i^*$). By calibrating the supply of reserves ($S$) to match expected autonomous factors and required reserves ($B + RR$), the central bank ensures the market rate stays near the midpoint.

## Mechanism

### The Arbitrage Condition
[RAW] For risk-neutral banks, arbitrage requires that the overnight interbank market rate is equal to the expected end-of-day marginal value of reserves, which itself is a weighted average of the two standing-facility rates. [[Bindseil_Monetary_Policy_Operations.md#page=56]]

[LLM] The transmission mechanism is defined by the following equation:
$$i = P(\text{"short"})i_B + P(\text{"long"})i_D$$
Where $P(\text{"short"})$ is the probability that the banking system will end the day in a deficit and need to use the borrowing facility.

### Steering via Scarcity
[RAW] If $d$ (autonomous factor shock) is symmetrically distributed around zero, and the central bank sets $S = B + RR$ in the morning, then $P(\text{"short"}) = 0.5$ and:
$$i = (i_B + i_D) / 2$$ [[Bindseil_Monetary_Policy_Operations.md#page=56]]

[LLM] If the central bank provides more liquidity ($S > B + RR$), the probability of being "long" increases, pulling the market rate $i$ toward the deposit floor $i_D$. Conversely, under-provision pulls $i$ toward the borrowing ceiling $i_B$.

### Parallel Shifts
[RAW] Central banks using a corridor approach have almost always preferred to implement changes of $i^*$ through parallel shifts of $[i_D, i_B]$ without any adjustment of $S$. [[Bindseil_Monetary_Policy_Operations.md#page=58]]

[LLM] This allows the central bank to decouple the "interest rate signal" (the level of the corridor) from the "liquidity condition" (the scarcity of reserves).

## Transmission Flow (ASCII)
```mermaid
graph TD
    A[CB sets S = B + RR] --> B{Daily Shock d}
    B -->|d > 0: Deficit| C[Banks use Borrowing Facility i_B]
    B -->|d < 0: Surplus| D[Banks use Deposit Facility i_D]
    E[Interbank Market] -->|Arbitrage| F[Rate i = E[marginal value of reserves]]
    F -->|Symmetry| G[Target Rate i*]
```

## Evidence / Source Anchors
- [[Bindseil_Monetary_Policy_Operations.md#page=55]] — Basic logic of symmetric corridor.
- [[Bindseil_Monetary_Policy_Operations.md#page=56]] — Mathematical derivation of the market rate $i$.
- [[Bindseil_Monetary_Policy_Operations.md#page=58]] — Preference for parallel shifts over liquidity adjustments.

## Related
- [[One-directional_Standing_Facility]]
- [[Full_Allotment_OMO]]
- [[Autonomous_Factors]]
- [[Full_Allotment_OMO_Mechanics]]
- [[Central_Bank_Coordination_Framework]]
