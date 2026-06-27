---
title: Compound Interest Mechanics
type: mechanism
status: verified
confidence: 5
expert_lens: Sidney Homer; Martin L. Leibowitz
provenance: "[RAW-BOOK: Homer & Leibowitz (2013)] Inside the Yield Book, Ch 8-10"
half_life_years: 100
---

## Thesis
Compound interest is the foundational mechanic of fixed-income mathematics where interest is earned on both the initial principal and the accumulated interest from prior periods. In the [RAW-BOOK: Inside the Yield Book] framework, the "Power of Compound Interest" is identified as the primary driver of long-term bond returns, specifically through the mechanism of **interest-on-interest**.

## Mechanism

### 1. The Fundamental Growth Formula
Unlike simple interest ($P(1 + TR)$), compound interest creates exponential growth by raising the growth factor to the power of the number of periods ($T$):

$$FV = P(1 + R)^T$$

*   **P:** Principal amount.
*   **R:** Interest rate per period (as a decimal).
*   **T:** Number of compounding periods.

### 2. Semiannual Compounding (Bond Market Standard)
Fixed income markets typically use semiannual compounding because coupon payments are distributed twice a year. This "capitalization of interest" allows the investor to reinvest the first half-year's payment to earn additional interest in the second half.

$$FV = P \left(1 + \frac{y}{2}\right)^{2N}$$

where $y$ is the nominal annual yield and $N$ is the number of years.

### 3. Causal Chain: The "Interest-on-Interest" Multiplier
Initial Investment $\rightarrow$ [Passage of Time] $\rightarrow$ Receipt of Coupon $\rightarrow$ [Reinvestment at Rate $R$] $\rightarrow$ Generation of Interest-on-Interest $\rightarrow$ **Exponential Accumulation**.

In long-term bonds (e.g., 20+ years), the interest-on-interest component can exceed the total sum of the nominal coupon payments themselves.

### 4. Future Value of a Cash Flow (Annuity)
The accumulation of a series of level payments (like coupons) is governed by the Future Value of an Annuity formula:
$$FV_{\text{annuity}} = A \times \frac{(1+R)^T - 1}{R}$$
The "Interest-on-Interest" component is specifically: $FV_{\text{annuity}} - (A \times T)$.

## Worked Example
A $1,000 investment for 2 years at a 7% annual rate:
*   **Simple Interest:** $1000 + (2 \times 0.07 \times 1000) = \$1,140$
*   **Annual Compounding:** $1000(1.07)^2 = \$1,144.90$
*   **Semiannual Compounding:** $1000(1.035)^4 = \$1,147.50$ (Note the \$7.50 "bonus" from compounding).

## Failure Conditions
*   **Reinvestment Rate Volatility:** The theory of Compound Interest (and YTM) assumes a constant reinvestment rate. If the market rate falls below the purchase yield, the realized future value will be lower than projected (reinvestment risk).
*   **Liquidity Constraints:** Compounding assumes the immediate reinvestment of every cent of coupon income. In reality, transaction costs, minimum investment sizes, and timing delays can erode the "Power of Compound Interest."
*   **Inflation Erosion:** While nominal value compounds, real purchasing power may decline if the inflation rate exceeds the reinvestment rate.

## Related
*   [[Bond_Pricing_Formula]] — The inverse application (discounting) of compounding.
*   [[Realized_Compound_Yield]] — The measure of a bond's actual compounded growth.
*   [[Time_Value_of_Money_Framework]] — The broader economic principle.
