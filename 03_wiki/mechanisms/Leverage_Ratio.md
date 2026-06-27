---
title: Leverage Ratio
aliases:
- Basel III Leverage Ratio
- Non-risk-based Leverage Ratio
type: mechanism
tags:
- basel-iii
- capital-adequacy
- bank-leverage
status: reviewed
confidence: 4
half_life_years: 1
expert_lens: "BCBS | BIS | ICMA"
provenance: "Basel Committee Leverage Ratio Framework 2014.pdf"
thesis: The Basel III Leverage Ratio acts as an absolute, non-risk-weighted backstop
  to bank balance sheet expansion, effectively capping overall nominal exposure and
  penalizing balance sheet-intensive but 'low-risk' activities like repo dealing and
  subscription line lending, further driving systemic footprint compression.
source_refs:
- file: Basel Committee Leverage Ratio Framework 2014.pdf
  page: 1
created: '2026-04-13'
updated: '2026-04-28'
---

## Thesis

The Basel III Leverage Ratio acts as a brute-force, non-risk-weighted backstop to bank balance sheet expansion. By stripping away intricate risk-weight adjustments, it caps overall nominal exposure regardless of asset safety. This mechanism prevents algorithmic gaming of internal risk models but simultaneously penalizes heavily balance-sheet-intensive yet mathematically low-risk activities (such as repo intermediation and private credit subscription lines), effectively capping the physical liquidity volume a regulated bank can provide to the shadow banking system.

## Mechanism

**The Leverage Ratio** is a non-risk-based capital requirement definitively introduced following the 2008 Global Financial Crisis (GFC). Prior to Basel III, global banks artificially suppressed their regulatory capital requirements by exploiting aggressive Internal Ratings-Based (IRB) models to drive their [[Risk_Weighted_Assets]] (RWA) down to extreme lows, allowing them to amass colossal nominal leverage. 

To prevent this internal model arbitrage and safeguard against model uncertainty, regulators instituted a rigid, supplemental restriction based strictly on sheer volume:

$$\text{Leverage Ratio} = \frac{\text{Tier 1 Capital}}{\text{Total Exposure Measure}} \ge 3\%$$

*(Note: Globally Systemically Important Banks or G-SIBs face an additional supplementary leverage buffer, frequently pushing the minimum operational requirement to 5% or more)*

### Defining The Components

1. **Tier 1 Capital:** The core, loss-absorbing equity of the financial institution (Common Equity Tier 1 + Additional Tier 1).
2. **Total Exposure Measure:** The unweighted, un-mitigated sum of the entire bank's footprint. Crucially, a AAA-rated domestic Treasury bond consumes the exact same physical balance sheet capacity (100% nominal value) as a distressed subprime corporate loan. The encompassing exposure includes:
   - All on-balance-sheet assets.
   - Derivative exposures (typically calculated via the Standardised Approach for Counterparty Credit Risk, SA-CCR).
   - Securities Financing Transactions (SFTs, notably Repo/Reverse Repo markets).
   - **Off-balance-sheet items** (e.g., undrawn corporate credit lines, liquidity facilities) converted via strict Credit Conversion Factors (CCFs).

> [!WARNING]
> Because it intentionally ignores risk profiling, the Leverage Ratio inherently penalizes the safest, highest-volume, lowest-margin banking businesses. If a bank acts as a clearing member holding deep pools of sovereign debt or engages in massive matched-book repo intermediation, its RWA remains negligible, but its Total Exposure Measure explodes, directly breaching the Leverage Ratio limit and forcing deleveraging.

### Boundaries / Conditions

### Transmission into Private Credit and NBFIs

The constraining physical volume limit of the Leverage Ratio ripples directly into the structuring and functioning of the shadow banking framework ([[Nonbank_Financial_Intermediation]]):

1. **Subscription Lines and Fund Finance:** Private Credit and Private Equity funds rely heavily on multi-billion dollar subscription credit/capital call lines provided by prime banks to smooth their cash flows. Even if these lines are deeply overcollateralized by LP capital commitments (and thus incredibly low credit risk), they consume massive unweighted amounts of the bank's finite Leverage Ratio capacity.
2. **Return on Equity (ROE) Margin Compression:** Because "balance sheet space" has become a hard constraint rather than an infinite elastic resource, banks must charge increasingly higher yields for these low-risk liquidity lines to adequately return on the physical space consumed, tightening the operating margins of the private funds reliant upon them.
3. **Repo Market Constriction:** By making basic matched-book repo trading balance-sheet intensive, the Leverage Ratio drastically reduces the willingness of banks to intermediate short-term liquidity during acute stress periods, driving NBFIs to either seek central clearing alternatives or creating systemic liquidity voids.

## 4. Systemic Fragility: Repo & FX Swap Disruptions

[LLM] Hệ số đòn bẩy (Leverage Ratio) là nguyên nhân chính dẫn đến sự đứt gãy của các thị trường phái sinh và tài trợ vốn quy mô lớn:

- **The Repo Spike (2019):** Do Leverage Ratio không phân biệt mức độ rủi ro, việc nắm giữ Trái phiếu Kho bạc (Treasuries) hoặc cho vay Repo (có đảm bảo) tốn diện tích bảng cân đối tương đương với cho vay rủi ro. Khi thanh khoản thắt chặt, các ngân hàng lớn (G-SIBs) ngừng cung cấp thanh khoản Repo để bảo vệ hệ số đòn bẩy, khiến lãi suất Repo vọt xê.
- **FX Swap & Cross-Currency Basis:** Trong các giai đoạn USD khan hiếm, nhu cầu vay USD qua FX Swap tăng vọt. Tuy nhiên, các ngân hàng trung gian không thể mở rộng bảng cân đối để thực hiện Arbitrage (vay nội tệ - cho vay USD) do vướng trần Leverage Ratio. Điều này khiến **[[Cross_Currency_Basis|Negative Basis]]** bị kéo dài và không thể tự điều chỉnh về 0 theo lý thuyết CIP.

---

## Evidence / Source Anchors

- Framework formulation, justification, and the minimum 3% backstop definitions: [[Basel Committee Leverage Ratio Framework 2014.pdf#page=1]]
- Liquidity and leverage transmission interaction during market stress events: [[ICMA Liquidity & Leverage Overview 2025.pdf#page=1]]
- Constraint impact on wholesale subscription and fund finance line provisioning constraining fund leverage: [[BIS Quarterly Review, March 2025.pdf#page=1]]

## Related

- [[Risk_Weighted_Assets]] — the highly optimized, risk-sensitive metric that the leverage ratio specifically backstops and overrides
- [[Basel_III_Impact_On_Private_Credit]] — the broader framework shift altering bank ROE logic
- [[Repurchase_Agreement]] — the high-volume cash/collateral market explicitly constricted by these leverage limits
- [[Nonbank_Financial_Intermediation]] — the shadow entities entirely reliant on bank leverage capacity for their operational efficiency
