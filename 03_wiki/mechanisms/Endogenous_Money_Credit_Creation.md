---
title: "Endogenous Money & Credit Creation: Loans Create Deposits"
aliases: [Loans Create Deposits, Endogenous Credit, Bank Lending Mechanism, Inside Money Creation, Credit-Driven Money Supply]
type: mechanism
tags: [macro, mmt, banking, money-supply, heterodox, credit-markets]
status: reviewed
confidence: 4
half_life_years: 10
school: "MMT | Post-Keynesian"
expert_lens: "Wray, Mitchell, Watts"
provenance: "Watts_Wray_Macroeconomics.md"
thesis: "Banks create money endogenously (deposits) when making loans to creditworthy borrowers, independent of their reserve positions. The quantity of credit is demand-determined by creditworthy applications, not supply-constrained by central bank reserves."
source_refs:
  - file: "Watts_Wray_Macroeconomics.pdf"
    page: 356
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
The transmission of credit creation is **demand-driven and endogenous:** banks lend to creditworthy borrowers seeking profitable loans regardless of reserve position; deposits are created simultaneously with loans as bank liabilities; reserves are sourced post-hoc from interbank markets or central bank. This inverts the neoclassical "money multiplier" narrative where central bank base money constrains lending.

## 1. Core Logic / Mechanism: Loans Create Deposits

[RAW] "The neoclassical characterisation of the credit creation process, which is driven by fractional reserve requirements, is not an accurate depiction of the way banks operate in a modern monetary economy characterised by a fiat currency and a flexible exchange rate."

[RAW] "Far from waiting for deposits before they create loans, banks in the real world expand their balance sheets by lending as described below. Loans create deposits that are then backed by reserves after the fact."

**The sequence (not the mythical "money multiplier"):**

```
Creditworthy borrower applies for loan
    ↓ (bank evaluates creditworthiness)
Bank approves $100,000 loan
    ↓ (accounting entry)
Bank credits borrower's deposit account (+$100,000 demand deposit)
Bank liability created: borrower owes $100,000 promissory note
    ↓ (borrower draws down deposit)
Borrower spends: writes check or transfers funds
    ↓ (interbank settlement)
Receiving bank's reserves rise, sending bank's reserves fall
    ↓ (reserve shortfall at sending bank)
Sending bank sources reserves from: interbank market, Fed window, or asset sales
    ↓
Reserves obtained post-hoc; lending never constrained by reserves
```

[RAW] "The process of extending loans (credit), which creates new bank liabilities, is unrelated to the reserve position of the bank."

## 2. Three Essential Conditions for Credit Creation

[RAW] "First, a necessary condition for credit creation is that there are non-bank firms and/or households who are seeking loans to finance their planned spending on goods, services or assets. Second, some of these entities must be considered creditworthy by the banks, so that there is a high probability that the loan will be repaid in full. What constitutes creditworthiness varies over the business cycle and lending standards tend to become more lax in boom times as banks chase market share. Third, the banks must anticipate that there is profit to be made by making these loans."

**Constraint hierarchy:**
1. **Profit motive:** Spread (lending rate - borrowing cost) must be positive
2. **Creditworthiness signal:** Expected repayment probability sufficient to justify the risk
3. **Demand:** Borrowers seeking loans (shifts over business cycle)

[RAW] "The only thing that constrains the bank loan desks from expanding credit is a lack of creditworthy applicants, which can be due to banks raising the qualifying standards in times of pessimism, or can occur if creditworthy customers are loath to seek loans because of future uncertainty."

**Reserve position is NOT a constraint:** [RAW] "Banks make loans independently of their reserve positions (that is, their holdings of reserves, relative to their liabilities). After originating loans they will borrow additional reserves if required by law or for clearing purposes. Bank managers generally neither know, nor care, about the aggregate level of reserves in the banking system. Certainly, no loan officer ever checks the individual bank's reserve position before approving a loan."

## 3. Reserve Sourcing: Post-Hoc, Not Pre-Hoc

[RAW] "If the spread between the rate of return on an asset (a security or a loan) and the cost of borrowing reserves is wide enough, even a bank that is already deficient in reserves will purchase the asset or make a loan and cover the reserves needed by purchasing (borrowing) reserves in the interbank market."

**Reserve cost determination:**

[RAW] "Bank lending decisions are affected by the price of reserves and expected returns, not by reserve positions. The interbank market (called the federal funds market in the US) functions to shuffle the reserve balances that the member (private) banks keep with the central bank to ensure that each of these banks can meet its reserve targets."

[LLM] The interbank overnight lending rate becomes the transmission channel:
- If overall system has excess reserves → rate falls → banks borrow cheap → lending expands
- If overall system has reserve shortage → rate rises → borrowing costs rise → lending contracts
- But central bank can support rate with "standing rate" (interest paid on reserves)

## 4. Banks Do NOT "Lend Out" Reserves

[RAW] "Banks do not loan out reserves, which raises the question of what role do bank reserves actually play? Banks must hold reserve balances with the central bank as part of the payments system. The reserves are used to make interbank payments."

**Bank reserve roles:**
1. **Interbank settlement:** Facilitate daily transactions between banks
2. **Regulatory requirement:** Meet minimum reserve ratio (if mandated)
3. **Profitability factor:** If central bank charges penalty rate for reserve deficiency, cost affects spread calculation (not constraint)

[RAW] "Each day millions of transactions are reconciled (settled) through these interbank payments."

## 5. Why Credit Contracts (and Monetary Policy Loses Traction)

[RAW] "Bank lending decisions are affected by the price of reserves and expected returns, not by reserve positions."

**In recession/pessimism:**
- Creditworthy applicants dry up (demand falls)
- Banks raise lending standards (expected losses rise)
- Even low interest rates don't stimulate lending
- Central bank can add reserves indefinitely → no effect on credit if demand is absent

[LLM] This is why post-2008 "quantitative easing" (adding $4 trillion in reserves) failed to spark lending: the demand side was broken (households deleveraging, firms uncertain about future). Reserves hit banks' balance sheets but didn't reach the real economy (trapped in asset markets instead).

## 6. Failure Conditions / Boundaries

**When does endogenous credit creation fail?**

1. **Credit crunch:** Banks drastically raise creditworthiness standards (post-GFC 2008), applicants absent
2. **Insolvency trap:** If banks themselves are insolvent (bad assets exceed capital), lending stops regardless of reserve availability
3. **Financial instability:** Interbank market freezes (Lehman 2008), banks cannot source reserves even at penalty rates
4. **Regulatory restriction:** Loan-to-deposit ratio caps or capital requirements become binding (rare in modern systems)

## Worked Example: $100K Auto Loan

**Day 1: Loan Origination**
- Borrower applies for $100K car loan, credit score 750, expects income $120K/year → creditworthy
- Bank profit spread: 6% loan rate vs 2% deposit cost = 4% margin on $100K = $4K gross profit
- Bank approves, creates deposit account, credits $100,000
  - Bank asset: $100K auto loan promissory note
  - Bank liability: $100K demand deposit (customer's checking account)

**Day 2: Borrower Spends**
- Borrower withdraws $100K (check to dealership)
- Dealership banks at Chase; borrower's bank is BofA
- BofA sends $100K Fed wire to Chase via Fed system (BofA reserves down $100K)
- Chase receives $100K (Chase reserves up $100K)

**Day 3: BofA Reserve Shortfall**
- BofA reserve balance drops; if below regulatory minimum, must source reserves
- Borrows $100K in Fed Funds (interbank overnight market) at 0.45% rate from Wells Fargo
- Cost: $100K × 0.45% ÷ 365 ≈ $123 one-day interest
- Loan was never constrained by reserve availability — only by creditworthiness & spread

**Result:** Credit created endogenously; reserves sourced post-hoc; central bank never involved in the lending decision.

## Related
- [[MMT_Operational_Reality]]
- [[Sovereign_Currency_Definition]]
- [[Bank_Money_Creation_Accounting]]
- [[Functional_Finance_vs_Sound_Finance]]
- [[Monetary_Financing_Mechanism]]
