---
type: mechanism
title: Realized Return Mechanism
tags: [returns, yields, pricing, fixed-income]
source: 
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=79]]"
  - "[[Tuckman_Serrat_Fixed_Income_2022.pdf#page=80]]"
status: active
created: 2026-04-28
---

# Realized Return Mechanism

## Overview

Realized return on a bond depends on three components: the price at which the bond is bought, the coupon payments earned over the holding period, the reinvestment of those coupon payments, and the price of the bond at the end of the horizon [extracted]. [extracted]

## Core Formula

For a bond investment over a specified horizon:

$$\text{Realized Return} = \frac{\text{Ending Value} - \text{Initial Cost}}{\text{Initial Cost}}$$

where **Ending Value** includes:
- Final bond price
- Coupon payments accumulated
- Reinvested coupon income

[extracted]

## Worked Example

**Scenario:** Investor buys $1 million face amount of US 7.625s of 11/15/2022 at 114.8765 on 11/15/2020. [extracted]

**Six-month holding period to mid-May 2021:** [extracted]

- Bond price: 111.3969
- Coupon received: $38,125 (half of 7.625% on $1,000,000)
- Gross return: 0.2898% [extracted]

**Calculation:**
$$\frac{\$1,113,969 + \$38,125 - \$1,148,765}{\$1,148,765} = 0.2898\%$$

[extracted]

## Net Returns (Financing Costs)

When a bond is purchased with borrowed funds, subtract financing costs from gross return: [extracted]

If borrowing rate = 0.05% for the 6-month period:
- Financing cost: $287 (0.05% × $1,148,765 / 2)
- **Net return: 0.2648%** [extracted]

$$\frac{\$1,113,969 + \$38,125 - \$1,148,765 - \$287}{\$1,148,765} = 0.2648\%$$

[extracted]

## Return on Capital (Leveraged Case)

If funded through repo with 98% leverage: [extracted]

- Initial cash deployed: $22,975
- Profit from trade: $3,387 (price gain plus coupon)
- **Return on capital: 13.27%** [extracted]

$$\frac{\$3,387}{\$22,975} = 13.27\%$$

[extracted]

## Key Components

1. **Price appreciation/depreciation** over horizon
2. **Coupon income** during holding period  
3. **Reinvestment rate** for intermediate cash flows
4. **Financing costs** (if borrowed)
5. **Leverage** impact on capital allocation [extracted]

## Critical Insight

Realized return differs from YTM because:
- Actual reinvestment rates may differ from YTM assumption
- Bond is sold before maturity, capturing price changes
- Intermediate cash flows reinvested at market rates (not YTM) [extracted]

## Related Nodes

[[Yield_to_Maturity_Calculation]]
[[P&L_Attribution_Components]]
[[Cash_Carry_Mechanism]]
