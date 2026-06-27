---
title: Bond Pricing Formula
type: mechanism
status: verified
confidence: 5
expert_lens: Sidney Homer; Martin L. Leibowitz
provenance: "[RAW-BOOK: Homer & Leibowitz (2013)] Inside the Yield Book, Ch 11-13"
half_life_years: 50
---

## Thesis
The price of a bond is mathematically defined as the **Present Value (PV)** of its future cash flows—comprising periodic coupon payments and the final redemption value—discounted at a specific rate (the Yield to Maturity). In the [RAW-BOOK: Inside the Yield Book] framework, this formula is the foundation for all relative value analysis and yield-to-price conversions.

## Mechanism

### 1. The Core Present Value Identity
The value of a bond is the sum of the present values of each individual cash flow. For a standard fixed-rate bond with face value $F$, annual coupon rate $C$, and $T$ semiannual periods to maturity, discounted at a semiannual rate $R$ (where $R = YTM / 2$):

$$PV = \frac{F}{(1+R)^T} + \sum_{t=1}^T \frac{C \cdot F / 2}{(1+R)^t}$$

### 2. The Simplified "Annuity + Bullet" Form
Homer & Leibowitz express this as a combination of a level payment flow (annuity) and a single lump sum (the "tail" or redemption payment):

$$PV = \frac{5C}{R} + \frac{1000 - \frac{5C}{R}}{(1+R)^T}$$
*(Assuming $F = 1000$ and $5C$ is the semiannual coupon payment in dollars)*

### 3. Causal Chain of Pricing Dynamics
The interaction between yield and price is governed by the following transmission:
Yield Rise ($R \uparrow$) $\rightarrow$ [Discounting Effect] $\rightarrow$ Denominator in PV formula increases $\rightarrow$ Present Value of fixed future cash flows decreases $\rightarrow$ Price Falls ($PV \downarrow$).

### 4. Components of Market Price
*   **Principal Value (Dollar Price):** The percentage of face value, typically quoted "clean" (excluding accrued interest).
*   **Accrued Interest (AI):** The interest earned but not yet paid since the last coupon date.
    $$AI = \frac{C \cdot F}{2} \times \frac{\text{Days since last coupon}}{\text{Days in coupon period}}$$
*   **Market Value (Dirty Price):** The actual cash paid for the bond.
    $$\text{Market Value} = \text{Principal Value} + \text{Accrued Interest}$$

## Worked Example
A 30-year bond with a 4% coupon is purchased to yield 6.50%.
*   $5C = \$20$ (Semiannual coupon)
*   $T = 60$ (Semiannual periods)
*   $R = 0.0325$ (6.50% / 2)
*   $PV_{\text{redemption}} = \frac{1000}{(1.0325)^{60}} \approx \$148.91$
*   $PV_{\text{coupons}} = \frac{20}{0.0325} \times (1 - \frac{1}{(1.0325)^{60}}) \approx \$522.91$
*   **Total Price (PV):** $\$148.91 + \$522.91 = \$671.82$ (Matches Table 70 in [RAW-BOOK])

## Failure Conditions
*   **Reinvestment Rate Risk:** The formula assumes all coupons are reinvested at the same YTM. If the reinvestment rate $r$ differs from YTM, the *Realized Compound Yield* will diverge from the initial YTM.
*   **Odd-Day Interpolation:** When a bond is sold between coupon dates, standard linear interpolation may introduce slight deviations from the true exponential growth of value (though conventional market practice uses the 30/360 or Actual/Actual day counts).
*   **Negative Rates:** In a negative yield environment, the denominator becomes $(1 - |R|)^T$, causing the PV to potentially exceed the sum of nominal cash flows (undiscounted).

## Related
*   [[Compound_Interest_Mechanics]] — The mathematical engine for discounting.
*   [[Yield_to_Maturity_Concept]] — The internal rate of return implied by the price.
*   [[Duration_Targeting_Mechanism]] — How price sensitivity interacts with time.
