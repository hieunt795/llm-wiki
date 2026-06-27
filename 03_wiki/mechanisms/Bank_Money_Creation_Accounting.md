---
title: Bank Money Creation Accounting
aliases:
- Inside Money Creation
- Double Entry Money Creation
- Endogenous Money
type: mechanism
tags:
- banking
- accounting
- money-creation
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: Alexander Düring - Fixed Income Trading and Risk Management (2021)
thesis: Trái ngược với quan điểm trung gian tài chính truyền thống, các ngân hàng
  thương mại hiện đại tạo ra 'Tiền Nội bộ' (Inside Money) một cách nội sinh thông
  qua kế toán kép bằng cách đồng thời ghi nhận một khoản vay (tài sản) và ghi có vào
  tài khoản của người đi vay một khoản tiền gửi mới (nợ phải trả).
source_refs:
- file: Fixed_Income_Alexander_During_Ch04.md
  page: 20
created: '2026-04-16'
updated: '2026-04-22'
---

## Thesis

A persistent macroeconomic misconception is that commercial banks operate merely as intermediaries, passively gathering pre-existing money from depositors to lend to borrowers. In reality, modern commercial banks literally create money (Inside Money/Credit Money) endogenously. Utilizing double-entry accounting, the bank manufactures a new deposit simply by extending a loan, instantly expanding the total money supply in the economy without requiring any prior transfer of central bank reserves.

## Mechanism

The essential architecture of bank money creation relies on the structure of the banking balance sheet.

When a bank approves a borrower for a loan, it does not physically hand over cash from its vault, nor does it decrement the account balance of another saver. Instead, the bank executes a simultaneous ledger expansion:

1. **Asset Creation:** The bank records the borrower's promissory note (the Loan) as a new asset on its balance sheet.
2. **Liability Creation:** At the exact same microsecond, the bank credits the borrower’s checking account for the loan amount. This creates a new demand deposit—a new liability for the bank.

**Balance Sheet Impact:**
- **Bank:** +Loan (Asset), +Customer Deposit (Liability)
- **Customer:** +Cash Deposit (Asset), +Loan (Liability)

> [!CAUTION]
> The money has been created *out of nothing but the mutual contract*. This newly manufactured deposit can immediately be used by the customer as a means of payment to buy a car or house. Because bank deposits in a modern economy are universally accepted as money, the macro money supply ($M1$/$M2$) has statistically increased.

### Boundaries / Conditions

### The Limit of Endogenous Creation

If a bank can manufacture money simply by expanding both sides of its balance sheet, what restrains infinite money creation?

1. **Interbank Settlement (The Outside Money Constraint):**
   When the borrower uses their newly created deposit to purchase a good from a seller who banks at a *different* institution, the borrower's bank must transfer the funds. This transfer between competing banks cannot be settled in the bank's own "Inside Money"—it must be settled using Central Bank Reserves (Outside Money). If a bank creates too many loans too quickly, the deposits will leak out to other banks, rapidly draining the originating bank's finite reserve of Central Bank liquidity.
2. **Regulatory Capital Constraints:**
   Basel III explicitly limits how much lending a bank can conduct relative to its hard equity via the [[Leverage_Ratio]] and [[Risk_Weighted_Assets]].
3. **Credit Risk (Profitability):**
   If the loan defaults, the asset side of the bank's balance sheet evaporates, but the deposit liability (which was likely transferred to another party) remains valid. The loss is absorbed directly by the bank's equity capital. Thus, banks only create money when they believe the borrower can mathematically service the debt.

## Evidence / Source Anchors

- Double-entry mechanics of money creation (simultaneous asset and liability generation): [[Fixed_Income_Alexander_During_Ch04.md#page=20]]
- The clarification that the nominal deposit does not need a preexisting physical equivalent: [[Fixed_Income_Alexander_During_Ch04.md#page=20]]

## Related

- [[Inside_Vs_Outside_Money]] — the framework mapping this newly created deposit against central bank reserves
- [[Reserve_Ratio_Constraint]] — the liquidity barrier limiting how wide the balance sheet can expand
- [[Bank]] — the legal architecture permitting this endogenous expansion
