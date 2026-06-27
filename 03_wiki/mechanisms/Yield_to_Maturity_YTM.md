---
status: reviewed
confidence: 5
expert_lens: Tuckman & Serrat
provenance: [RAW-BOOK: Tuckman & Serrat (2022)]
half_life_years: 10
---

# Yield to Maturity (YTM)

## Thesis
Yield to Maturity (YTM) is the internal rate of return (IRR) of a bond, representing the single discount rate that equates the present value of all future cash flows to the bond's current market price. While convenient for quoting and trading, it is a poor predictor of realized holding-period returns due to unrealistic assumptions.

## Mechanism
YTM collapses the entire term structure of interest rates into a single number for a specific bond.

### RCL Skeleton:
1. **Regime Lock:** 
   - Assumes **Reinvestment at YTM** (all coupons are reinvested at the same yield) and **Hold-to-Maturity** (or constant yield at horizon).
   - In a multi-curve framework, YTM is seen as a "summary statistic" rather than a pricing primitive.

2. **Causal Chain:**
   - Market Price ($P$) →[Iterative Solving]→ $\sum \frac{CF_t}{(1+y/2)^t} = P$ →[Output]→ Yield ($y$).
   - **Couponeffect:** Upward-sloping term structure → high-coupon bonds have lower YTM because more cash flow is weighted toward shorter, lower-rate periods.
   - **Pull to Par:** As a bond matures, its price converges toward face value (par) if the yield remains constant.

3. **Feedback Topology:** 
   - **Inverse Relationship:** Price and Yield move in opposite directions.
   - **Convexity:** The price-yield function is convex; prices rise more for a given yield decrease than they fall for an equivalent yield increase.

4. **Channel Interaction:** 
   - Interacts with the **Spot Rate Curve**: YTM is an average of spot rates weighted by the bond's cash flows.

5. **Quantified Anchor:** 
   - [RAW-BOOK: Tuckman 2022:82] The 7.625s of 11/15/2022 priced at 111.3969 in May 2021 had a YTM of $0.0252\%$.

6. **Boundary Conditions:** 
   - **Realized Return Failure:** If reinvestment rates differ from the initial YTM, the actual return will diverge (e.g., a 30-year bond with 2.343% YTM returns only 1.778% if coupons are reinvested at 0%).

## Worked Example
A 10-year Treasury bond with a 2.5% coupon trades at 100 (par). Its YTM is exactly 2.5%. If the market yield rises to 3%, the bond's price must fall below 100 to compensate the buyer for the below-market coupon.

## Failure Conditions
- **Reinvestment Risk:** Most market participants cannot reinvest coupons at the bond's YTM (especially in extreme rate environments).
- **The Coupon Effect:** Two bonds with the same maturity but different coupons will have different YTMs even if they are both "fairly priced" according to the spot curve.
- **Negative Yields:** YTM calculations can result in negative values (as seen in European markets in the early 2020s), which reverses the normal relationship where discount factors fall with term.

## Related
- [[Discount_Factors]]
- [[Law_of_One_Price]]
- [[Spot_Rates]]
- [[Convexity]]
