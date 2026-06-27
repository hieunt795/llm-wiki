---
title: DV01 Risk Management
type: mechanism
status: reviewed
confidence: 5
expert_lens: ["Bruce Tuckman", "Angel Serrat", "Schofield"]
provenance: ["RAW-BOOK: Tuckman & Serrat (2022) Ch 4", "Schofield_Trading_Fixed_Income_2011.md"]
half_life_years: 10
tags: ["fixed-income", "risk-management", "trading"]
source_refs:
  - file: Tuckman_Serrat_2022.md
    page: 115
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 2019-2038
---

## Thesis
DV01 (Dollar Value of an '01) is the bedrock of fixed-income trading risk management, quantifying the absolute currency impact of a one-basis-point (0.01%) shift in interest rates. It allows traders to normalize risk across diverse instruments to construct precise hedges.

## Mechanism

### 1. Definition and Calculation
DV01 represents the change in the price of a bond for a 1 basis point (0.01%) change in rates. It is the dollar-denominated equivalent of duration.
- **Formula (Numerical)**: $DV01 \approx -\frac{1}{10,000} \frac{\Delta P}{\Delta y}$
- **Formula (Derivative)**: $DV01 = -\frac{1}{10,000} \frac{dP}{dy}$
- **Relation to Duration**: $DV01 = \frac{P \times D_{mod}}{10,000}$

### 2. Hedging Logic (The '01 Match)
To hedge a position in Bond A using Bond B, the face amount ($F_B$) must be chosen such that the net DV01 of the combined position is zero.
- **Hedge Ratio**: $F_B = -F_A \times \frac{DV01_A}{DV01_B}$
- **Transmission**: $Yield Shift \rightarrow [DV01] \rightarrow \Delta Value$. If $DV01_{Net} = 0$, then small yield shifts result in zero P&L impact.

### 3. Additive Property
The DV01 of a portfolio is the simple sum of the DV01s of its component instruments. This allows for complex "risk aggregation" where a trader can see the total dollar risk to a 1bp shift across a desk or fund.

### 4. Regime Dependence
DV01 is a **local measure**. Because of convexity, the DV01 of a bond changes as the level of interest rates changes. 
- **Regime**: Low Rates $\rightarrow$ High Price $\rightarrow$ High DV01.
- **Regime**: High Rates $\rightarrow$ Low Price $\rightarrow$ Low DV01.

## Worked Example
A market maker buys $10 million face of a Century Bond ($DV01 = 0.241$ per 100 face) and wants to hedge with a 30-year Treasury ($DV01 = 0.199$ per 100 face).
- **Century Bond Risk**: $(10,000,000 / 100) \times 0.241 = \$24,100$ per bp.
- **Treasury Hedge Amount**: $F_{Treasury} = -10,000,000 \times (0.241 / 0.199) = -\$12,110,553$.
- **Outcome**: Selling $\$12.11M$ of Treasuries offsets the $\$24,100$ risk, creating a "DV01-neutral" hedge.

## Failure Conditions
- **Convexity Risk**: DV01-neutral hedges are only delta-neutral for very small moves. Large moves will create P&L due to convexity differences (the "convexity bias").
- **Spread Risk**: Treasury-hedged corporate bonds are exposed to "Basis Risk" or "Spread Risk." If the corporate-treasury spread widens while benchmark rates are stable, the hedge fails.
- **Curve Risk**: Standard DV01 assumes parallel shifts. If the 30-year rate moves 1bp but the 100-year rate moves 1.5bp, the DV01 match will not protect the portfolio.

## Related
- [[Macaulay_and_Modified_Duration]]
- [[Convexity_Mechanics]]
- [[Key_Rate_Duration]]
- [[Basis_Risk]]
