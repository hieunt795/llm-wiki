---
title: ITF Conceptual and Theoretical Models
aliases:
- Baseline ITF Model
- Inflation Forecast Targeting Model
- 3-Equation New Keynesian Model
type: concept
tags:
- monetary-policy
- macroeconomics
- modeling
status: reviewed
confidence: 5
half_life_years: 10
expert_lens: "Perry Warjiyo"
provenance: "[RAW-BOOK: Perry Warjiyo & Solikin M. Juhro - Central Bank Policy: Theory and Practice (2019)]"
thesis: The theoretical foundation of ITF rests on the New Keynesian and New Neoclassical Synthesis, modeling inflation dynamics as dependent on expectations and the output gap, with the central bank minimizing a quadratic loss function.
source_refs:
- "[RAW-BOOK: Perry Warjiyo & Solikin M. Juhro - Central Bank Policy: Theory and Practice (2019)], Chapter 8.2.2"
created: '2026-04-28'
updated: '2026-04-28'
---

## Thesis

ITF is not merely an "art of central banking" but a grounded science derived from optimal behavior of economic agents. The core logic is that **Inflation Dynamics** depend on expected (future) inflation and the output gap. The central bank acts as a social planner, adjusting nominal interest rates to minimize the variance of inflation around its target and the volatility of real output. [RAW-BOOK: Perry Warjiyo & Solikin M. Juhro (2019), p. 230]

## Mechanism (RCL Framework)

### 1. Regime Lock
The theoretical model assumes **Rational Expectations**, where agents are forward-looking and incorporate the central bank's reaction function into their decisions. The regime operates under the **Taylor Principle**, requiring the policy rate to respond more than one-for-one to inflation changes to ensure determinacy and stability. [RAW-BOOK: Perry Warjiyo & Solikin M. Juhro (2019), p. 231]

### 2. Causal Chain
The **Baseline 3-Equation Model** defines the transmission:
1.  **Supply Equation (NKPC):** $\pi_t = E\pi_{t+1} + \alpha x_t + \epsilon_t$
    *   Inflation today is a function of future expectations and the current output gap.
2.  **Demand Curve (IS):** $x_t = Ex_{t+1} - \delta(i_t - E\pi_{t+1}) + u_t$
    *   The output gap depends on future expectations and the real interest rate ($i_t - E\pi_{t+1}$).
3.  **Policy Rule (Taylor-type):** $i_t = \phi_\pi \pi_t + \phi_x x_t + \phi_i i_{t-1} + v_t$
    *   The central bank sets the nominal rate based on inflation, output, and interest rate smoothing.

- **Intent:** To maximize public welfare by minimizing the **Social Loss Function**:
    $L = E \sum_{t=0}^{\infty} \delta^t [(\pi_t - \bar{\pi})^2 + \lambda x_t^2]$
    where $\lambda$ represents the weight on output stability (Flexible ITF).
- **Mechanism:** Optimal policy derives a **Targeting Rule**: $\pi_t + \frac{\lambda}{\alpha} x_t = 0$.
- **Interaction:** In an **Inflation Forecast Targeting (IFT)** format (Svensson), the policy target becomes the inflation forecast itself: $E[\pi_{t+2}] = \bar{\pi}$ (for $\lambda = 0$). [RAW-BOOK: Perry Warjiyo & Solikin M. Juhro (2019), p. 231-233]

### 3. Feedback Topology
The model creates a **Self-Fulfilling Expectation Loop**. If the central bank is credible, $E\pi_{t+1}$ anchors to $\bar{\pi}$. This reduces the need for aggressive interest rate hikes ($i_t$) because agents don't bid up prices, thereby stabilizing the output gap ($x_t$). However, purely forward-looking models can trigger **Indeterminacy** (multiple equilibria) if the policy rule is not "active" ($\phi_\pi > 1$). [RAW-BOOK: Perry Warjiyo & Solikin M. Juhro (2019), p. 231]

## Dense Unpacking (4-Step)

- **INTENT:** To model the interaction between monetary policy and the macroeconomy to find the optimal path that minimizes inflation and output volatility.
- **MECHANISM:** Use of micro-founded equations (NKPC and IS) where current outcomes are heavily weighted by future expectations, controlled by a feedback-driven policy rule.
- **INTERACTIONS:** The interaction between the **Output Gap** and **Inflation** via the Phillips Curve requires the central bank to manage the trade-off (determined by $\lambda$).
- **BOUNDARY:** The model breaks down if expectations become **Backward-Looking** (High Inertia) or if the central bank faces a **Liquidity Trap** where $i_t$ hits the Zero Lower Bound.

## Worked Example: Strict vs. Flexible ITF
- **Strict ITF ($\lambda = 0$):** The central bank is an "inflation nutter." It responds aggressively to any inflation deviation, even at the cost of high output volatility. The optimal rule simplifies to ensuring the inflation forecast hits the target exactly at the policy horizon.
- **Flexible ITF ($\lambda \neq 0$):** The central bank accepts a slower return to the inflation target to cushion the blow to the real economy. This is reflected in the targeting rule where output gap deviations are allowed to offset inflation deviations temporarily. [RAW-BOOK: Perry Warjiyo & Solikin M. Juhro (2019), p. 231, 233]

## Failure Conditions
1. **Time-Inconsistency:** If the central bank deviates from its rule to gain short-term output boosts, losing credibility.
2. **Indeterminacy:** If $\phi_\pi \leq 1$, inflation can drift without a nominal anchor.
3. **Supply Shock Domination:** Large $\epsilon_t$ shocks make it impossible to stabilize both $\pi$ and $x$ simultaneously. [RAW-BOOK: Perry Warjiyo & Solikin M. Juhro (2019), p. 231]

## Related
- [[Inflation_Targeting_Framework_ITF]] — The governance framework.
- [[New_Keynesian_Phillips_Curve_NKPC]] — The supply-side component.
- [[Taylor_Rule_Interest_Rate_Rule]] — The common reaction function.
- [[Central_Bank_Loss_Function_Mechanics]] — Technical details on $L$.
- [[Inflation_Forecast_Targeting_IFT]] — Operationalizing the theoretical forecast target.
