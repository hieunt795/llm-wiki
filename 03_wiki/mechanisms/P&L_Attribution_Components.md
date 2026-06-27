---
type: mechanism
title: P&L Attribution Components
tags: [p&l, attribution, returns, carry, rates, spreads]
source: 
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=94]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=97]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=98]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=100]]"
status: active
created: 2026-04-28
---

# P&L Attribution Components

## Overview

P&L attribution breaks down bond returns and losses into component sources, enabling traders and asset managers to understand where profits originated and diagnose performance [extracted].

The critical division separates what happens due to:
1. **Passage of time** (carry and roll-down)
2. **Changes in rates and spreads** (rate risk, spread risk)

[extracted]

## Four Primary Components

### 1. Cash Carry

Cash carry captures interim cash flows from coupon payments and financing arrangements. It is **positive when the bond yields more than financing costs** [extracted].

**Formula:**
$$\text{Cash Carry} = \frac{\text{Coupon Income} - \text{Financing Costs}}{\text{Initial Position Value}}$$

**Example:** US Treasury 7.625s of 11/15/2022, held 6 months [extracted]

- Coupon received (May 2021): $38,125
- Financing cost (0.05% repo rate): $287
- Position value: $1,148,765
- **Cash carry: 3.81250%** [extracted]

This represents the direct income earned from holding the position without any market price movement.

### 2. Carry-Roll-Down

Carry-roll-down captures P&L from the bond's price movement due to the passage of time alone, assuming **rates and spreads remain constant** [extracted].

**Mechanism:** As time passes:
- The bond moves down the yield curve to shorter maturities
- If the curve is upward sloping, yields fall and prices rise (**roll down gain**)
- If the curve is inverted or flat, yields may rise and prices fall

[extracted]

**Example Scenario (Unchanged Term Structure):** [extracted]

Starting position: 6-month forward loan from November 13, 2020  
Forward rate (from Table 3.4): 0.1746%  
Six months later (May 14, 2021): The forward rate becomes the new spot rate  

**P&L:** Bond valued at the new spot (now one-year forward) vs. original forward price  
**Result:** Carry-roll-down = **-3.76099%** (negative in this scenario) [extracted]

**Interpretation:** Because forward rates fell from November 2020 to May 2021, rolling down the curve was not favorable.

### 3. Rates Component

Rate changes reflect P&L from movements in the yield curve, beyond simple roll-down [extracted].

**Calculation:** 
- Price change from realized forward scenario (rates evolved as expected)
- Compare to unchanged term structure scenario
- Difference = rates component of P&L

[extracted]

**Example:** [extracted]
- Price change due to rate movements: 0.18292%
- This captures yield curve steepening, flattening, or parallel shifts

### 4. Spread Component

Spread P&L arises from changes in the bond's valuation relative to the benchmark curve [extracted].

**Formula:**
$$\text{Spread P&L} = \frac{\Delta \text{Spread} \times \text{Spread Duration}}{\text{10,000}}$$

**Example:** [extracted]
- Bond spread moved from -1.16 bp to -7.27 bp  
- Spread widened by -6.11 bp (bond became richer)
- Spread P&L: 0.09843% (positive; bond price rose)

[extracted]

## P&L Attribution Example: US Treasury 7.625s

**Position:** $1,000,000 face of 7.625s of 11/15/2022  
**Holding period:** November 13, 2020 to May 14, 2021  
**Market prices:** 114.87654 → 111.3969  

### Detailed Attribution Table

| Component | P&L |  Return |
|-----------|-----|---------|
| **Cash Carry** | $3,812.50 | 3.31880% |
| **Carry-Roll-Down** | -$3,760.99 | -3.27390% |
| **Rates** | $1,829.20 | 0.13920% |
| **Spread** | $984.30 | 0.08570% |
| **Total** | **$3,328.60** | **0.28980%** |

[extracted]

**Total return:** 0.2898%, decomposed as:
- Strong coupon income (3.82%)
- Partially offset by carry-roll-down (-3.27%)
- Small gains from rate and spread movements (+0.22%)

[extracted]

## Realized Forwards vs. Unchanged Term Structure

The attribution framework relies on two key scenarios: [extracted]

**Scenario A: Realized Forwards**
- Use forward rates that actually prevailed at the start
- These forward rates evolved into spot rates as time passed
- Compares actual outcome against "locked-in" forward scenario

[extracted]

**Scenario B: Unchanged Term Structure**
- Assume the entire forward curve remains constant
- Rates don't change from the beginning of the period
- Isolates carry and roll-down from rate movements

[extracted]

## Critical Insight: Causation vs. Correlation

Attribution reveals causation: [extracted]

1. **Carry/roll-down** = deterministic (given term structure and time)
2. **Rates** = driven by macro factors, curve repricing, expectations
3. **Spread** = driven by supply, credit events, liquidity shifts

[extracted]

A trader expecting rates to remain stable can profit from carry-roll-down. A trader betting on rates will move uses rates attribution to quantify that bet's impact.

## Related Nodes

[[Realized_Return_Mechanism]]
[[Cash_Carry_Mechanism]]
[[Yield_Curve_Dynamics]]
[[Bond_Spread_Framework]]
