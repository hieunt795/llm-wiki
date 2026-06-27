---
status: reviewed
confidence: 5
expert_lens: Tuckman & Serrat
provenance: [RAW-BOOK: Tuckman & Serrat (2022)]
half_life_years: 10
---

# Discount Factors

## Thesis
A discount factor is the present value of $1$ unit of currency to be received at a specific future date. It represents the market price of a future claim today and serves as the fundamental building block for all fixed income valuation.

## Mechanism
Discount factors, denoted as $d(t)$, are extracted from bond prices and used to value any set of future cash flows.

### RCL Skeleton:
1. **Regime Lock:**
   - Assumes **No Arbitrage** (the Law of One Price holds).
   - Typically assumes positive interest rates ($d(t) < 1$ and $d(t)$ decreases with $t$), though negative rates can invert this.

2. **Causal Chain:**
   - Bond Price ($P$) →[Bootstrap/Extraction]→ $P = \sum CF_t \cdot d(t)$ →[Solve]→ $d(t)$.
   - **Time Value of Money:** The further in the future a payment is, the lower its discount factor (usually).

3. **Quantified Anchor:**
   - [RAW-BOOK: Tuckman 2022:52] In May 2021, the US Treasury discount factor for 0.5 years was $0.999923$, and for 10 years was approximately $0.85$.

4. **Boundary Conditions:**
   - In a negative interest rate regime, $d(t)$ can exceed $1.0$, meaning $\$1$ in the future is worth more than $\$1$ today.

## Worked Example
If the discount factor for $3.0$ years is $0.99$, the present value of $\$1$ to be received in three years is $99$ cents. To find the price of a bond, multiply each coupon and the principal by its corresponding discount factor and sum the results.

## Related
- [[Law_of_One_Price]]
- [[Yield_to_Maturity_YTM]]
- [[Spot_Rates]]
- [[STRIPS_Market]]
