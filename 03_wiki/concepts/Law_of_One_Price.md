---
status: reviewed
confidence: 5
expert_lens: Tuckman & Serrat
provenance: [RAW-BOOK: Tuckman & Serrat (2022)]
half_life_years: 10
---

# Law of One Price

## Thesis
The Law of One Price (LOOP) states that in an efficient market, identical cash flows must sell for the same price, regardless of the security that delivers them. This principle forms the foundational logic for arbitrage pricing and the use of discount factors in bond valuation.

## Mechanism
The mechanism of LOOP is enforced through **arbitrage activity**. If two sets of identical cash flows trade at different prices, market participants (arbitrageurs) will simultaneously sell the expensive version and buy the cheaper version, pocketing a riskless profit until the price discrepancy is eliminated.

### RCL Skeleton:
1. **Regime Lock:**
   - Assumes **Frictionless Markets** (no transaction costs, taxes, or financing constraints) and **Perfect Liquidity**.
   - In reality, idiosyncratic factors (supply/demand, liquidity premia) can cause persistent deviations.

2. **Causal Chain:**
   - Identity →[Replication]→ Portfolio of liquid bonds replicates target bond's cash flows →[Pricing Gap]→ $P_{target} \neq \sum P_{replicating}$ →[Arbitrage]→ Sell rich/Buy cheap →[Convergence]→ Price parity restored.
   - **Confounders:** Transaction costs (bid-ask spreads), financing costs (repo/reverse repo rates), and idiosyncratic bond characteristics (e.g., high-coupon preference).

3. **Feedback Topology:**
   - **Balancing Loop:** Price discrepancy triggers arbitrage flow, which moves prices toward parity, reducing the incentive for further arbitrage.

4. **Channel Interaction:**
   - Interacts with the **STRIPS market** where P-STRIPS (principal) and C-STRIPS (coupon) of the same maturity may trade at different prices due to fungibility differences.

5. **Quantified Anchor:**
   - [RAW-BOOK: Tuckman 2022:54] In May 2021, the 7.625s of 11/15/2022 traded at $111.3969$ while its replicating portfolio cost $111.2797$, representing a $12$ cent richness ($0.11\%$).

6. **Boundary Conditions:**
   - Fails when **Market Frictions** (transaction/financing costs) exceed the potential arbitrage profit.
   - Fails under **Credit Risk** divergence (though not applicable to US Treasuries).

## Worked Example
An arbitrageur identifies that the $7.625$s of $11/15/2022$ are trading "rich" relative to a portfolio of more liquid Treasury bonds (the "bold" bonds in Tuckman's sample).
- **Action:** Short the rich bond, buy the replicating portfolio.
- **Outcome:** The net proceeds today are positive, while all future cash flows (coupons and principal) perfectly cancel out, resulting in a riskless profit.

## Failure Conditions
- **Liquidity Premia:** On-the-run bonds (most recently issued) often trade at a premium (lower yield) compared to off-the-run bonds with identical cash flows.
- **Tax Effects:** Different tax treatments for capital gains vs. interest income can drive price wedges.
- **Institutional Preferences:** Some investors may overpay for high-coupon bonds to satisfy income requirements (as seen in low-rate environments).

## Related
- [[Discount_Factors]]
- [[Arbitrage_Pricing]]
- [[STRIPS_Market]]
- [[Yield_to_Maturity_YTM]]
