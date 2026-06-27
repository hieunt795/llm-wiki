---
title: "Endogenous Risk in LOLR Operations"
aliases: [Endogenous Risk, Moral Hazard Risk, Central Bank Risk-Taking]
type: mechanism
tags: [lolr, moral-hazard, risk-taking, central-bank]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Ulrich Bindseil"
provenance: "Bindseil LOLR Crisis"
thesis: "Endogenous risk in LOLR refers to increased risk-taking behavior by banks in anticipation of central bank rescue; the availability of LOLR creates moral hazard where institutions take excessive liquidity risk or leverage, expecting government/CB backstop, thereby increasing the probability of crises."
source_refs:
  - file: "Bindseil LOLR"
    page: 252
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Endogenous risk is behaviorally induced: banks respond to LOLR availability by increasing leverage, shortening funding maturity, and holding illiquid assets; equilibrium risk level endogenously rises with LOLR scope, offsetting some welfare gains from crisis prevention.

## 1. Core Definition

[RAW] Per Bindseil (Ch. 15, p.252):

"Endogenous Risk" in LOLR context describes the second-order effect where the central bank's commitment to provide crisis liquidity assistance changes bank incentives and behavior, increasing equilibrium risk-taking.

**Mechanism:** LOLR availability → reduces funding cost for risky behavior → banks extend leverage and shorten maturity → increases crisis probability → LOLR more frequently invoked

## 2. Moral Hazard Transmission

**Behavioral channel:**

### Ex-Ante Risk-Taking Incentive
Banks rationally calculate: LOLR availability reduces downside risk of illiquidity
- Funding cost benefit: Can use short-term, cheaper funding knowing LOLR backstop
- Leverage benefit: Can leverage further without matching equity, knowing rescue available
- Asset quality benefit: Can hold less liquid assets (higher yield) with LOLR collateral safety net

### Rational Bank Behavior
Bank manager maximizes: Profit = (Yield spread on assets) × Leverage - (Funding cost) - (Risk premium for remaining solvency risk)

With LOLR: Funding cost ↓ → Leverage ↑ → Profit ↑ (until marginal solvency risk equals risk premium decline)

**Result:** Equilibrium leverage and liquidity risk rise until expected cost of insolvency equals welfare from additional risk-taking

## 3. Mechanisms of Endogenous Risk Elevation

[RAW] Per Bindseil (p.252) and implicit in macro-financial literature:

### 3.1 Maturity Mismatch Endogenization
**Without LOLR:** Bank avoids short-term funding due to rollover risk → longer maturity liabilities
**With LOLR:** Bank shifts to cheaper short-term funding → LOLR provides maturity insurance → higher systemic fragility

**Example:** European banks pre-2008 relied heavily on short-term wholesale funding (repo, ABCP) because ECB Standing Facilities and ELA availability reduced rollover risk

### 3.2 Leverage Escalation
**Without LOLR:** Bank capital/asset ratio = f(liquidation value at stress, required ROE)
**With LOLR:** Bank can achieve same required ROE with lower capital because liquidity backstop reduces tail risk

**Quantification example:** If LOLR reduces 1-in-20-year loss probability from 20% to 5%, bank can support 10% ROE with:
- Without LOLR: 20% Tier-1 capital ratio required
- With LOLR: 10% Tier-1 capital ratio sufficient (double leverage)

### 3.3 Asset Quality Degradation
**Without LOLR:** Bank focuses on liquid, high-quality collateral (repo eligible, investment-grade)
**With LOLR:** Bank holds illiquid, lower-quality assets (higher yield) if eligible under broader LOLR collateral framework

**Example:** Pre-2008, European banks accumulated US subprime mortgages and ABSs; ECB's broad collateral acceptance reduced incentive for liquidity caution

### 3.4 Herding and Systemic Concentration
**Without LOLR:** Bank avoids highly correlated risk exposure (common asset holdings)
**With LOLR:** Bank willing to hold concentrated exposure if others do, betting LOLR can rescue all simultaneously

**Result:** Systemic concentration risk increases; multiple institutions fail simultaneously rather than sequentially

## 4. Quantified Example: LOLR Moral Hazard

**Scenario:** Two-period bank model

**Period 1:** Bank chooses maturity profile
- Short-term funding cost: 1% if no crisis
- Long-term funding cost: 3% (no rollover risk)
- Crisis probability if short-term: p_short = 20%
- Crisis probability if long-term: p_long = 5%

**Period 2:** If crisis → need LOLR or fail

**Case A: No LOLR available**
- Expected cost of short-term = 1% × (1-0.2) + Bankruptcy cost × 0.2
- Expected cost of long-term = 3% × (1-0.05) + Bankruptcy cost × 0.05
- If bankruptcy cost large: long-term dominates; bank chooses long-term funding

**Case B: LOLR available at penalty rate (5%)**
- Expected cost of short-term = 1% × (1-0.2) + [LOLR 5% + penalty] × 0.2
- If penalty small: short-term becomes cheaper than long-term!
- **Endogenous effect:** Bank chooses short-term; crisis probability becomes p_short = 20% equilibrium

## 5. Empirical Evidence of Endogenous Risk

[RAW] Implicit in post-2008 literature discussed by Bindseil:

**Pre-2008 period:** ECB's acceptably broad collateral framework for LOLR/standing facilities
- European banks accumulated illiquid assets (mortgage-backed securities, ABSs)
- Reliance on short-term wholesale funding (overnight repo, ABCP) increased dramatically
- Basel I/II capital standards permitted leverage multiples of 30-40x

**Result:** When subprime shock occurred, multiple institutions faced simultaneous funding crises

**Post-2008 period:** Regulatory response to endogenous risk
- Capital requirements increased (Basel III: 10.5% CET1 with buffer)
- Liquidity regulation (LCR, NSFR) constrained maturity mismatch
- **Effect:** Leverage has not returned to pre-2008 levels despite CB LOLR availability

## 6. Central Bank Risk-Taking Response Options

Bindseil (Ch.15-16) implies central banks face choice:

### 6.1 Strict Collateral Framework (High Endogenous Risk Control)
- Only accept highly liquid, high-quality collateral in LOLR
- Narrow asset class eligibility
- High haircuts on marginal collateral

**Benefit:** Limits bank incentive to hold illiquid assets
**Cost:** LOLR less effective in true liquidity crises; market-wide collateral freezes

### 6.2 Broad Collateral Framework (Low Endogenous Risk Control)
- Accept wide range of collateral, including less liquid/lower-quality assets
- Low/zero haircuts during crisis
- Rapid disbursement with minimal documentation

**Benefit:** LOLR effective in liquidity crises; prevents fire sales
**Cost:** Encourages bank asset concentration in LOLR-eligible illiquids

### 6.3 Supervisory Coordination Approach (Balanced)
- Broad LOLR collateral framework
- But coupled with macroprudential regulation limiting leverage/maturity mismatch
- Capital buffer requirements prevent profiting from LOLR insurance

**Logic:** Regulation sets incentives; CB provides tools

## 7. Time-Consistency Problem in Endogenous Risk

**Time-consistency logic:**

**Pre-crisis:** CB announces "LOLR for solvent, illiquid institutions"
- Banks believe commitment credible
- Banks increase leverage, shorten maturity
- Risk rises endogenously

**Crisis arrives:**
- CB faces choice: allow bank failure (costly, contagious) or provide LOLR
- Politically/economically, LOLR provision optimal ex-post
- But ex-post provision validates ex-ante risk-taking expectations
- Reinforces moral hazard for next cycle

**Result:** Multiple equilibrium problem; high-risk equilibrium becomes self-fulfilling

## 8. Related Policy Trade-offs

Endogenous risk creates tension between:

1. **Stability vs Efficiency:** LOLR stability requires constraining risky behavior ex-ante, reducing lending efficiency
2. **Crisis Prevention vs Moral Hazard:** Visible, credible LOLR prevent crises but induce excessive risk
3. **Regulation vs LOLR:** Macroprudential regulation and LOLR operate in tension; both necessary

## Related
- [[Exogenous_Risk_LOLR]]
- [[Moral_Hazard_Liquidity_Regulation]]
- [[Lender_Of_Last_Resort_Mechanism]]
- [[Financial_Procyclicality_Mechanism]]
- [[Bank_Run_Mechanics]]
