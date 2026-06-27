---
title: Bond Relative Value Valuation
aliases:
- Relative Value
- Bond RV
- RV Analysis
- Hedge-Based Benchmarking
- Giá trị tương đối trái phiếu
type: mechanism
tags:
- trading
- valuation
- fixed-income
- curve-analysis
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: During_Fixed_Income_Ch33.md
thesis: Relative value (RV) is the identification of mispriced securities within a
  curve segment, utilizing specific spread metrics that mirror the instrument's natural
  hedge to isolate idiosyncratic cheapness from broader market interest rate moves.
source_refs:
- file: During_Fixed_Income_Ch33.md
  page: 362
- file: During_Fixed_Income_Ch33.md
  page: 363
created: '2026-04-18'
updated: '2026-04-20'
---

## Thesis

Yields alone are insufficient for comparing individual bonds because they suffer from reinvestment risk and flat-curve assumptions. Alexander Düring explains that effective **Relative Value** analysis requires translating yields into curve spreads. Crucially, the "most sensible" spread for any bond is the one that reflects how that bond is usually hedged in professional trading books. [[During_Fixed_Income_Ch33.md#page=362]]

## The Valuation Matrix: Selecting the Benchmark

| Asset Class | Primary Hedge | Recommended Metric |
| :--- | :--- | :--- |
| **Government Bonds** | Other Sovereigns | **Z-spread** (against govt spline). |
| **Agencies / SSA** | Sovereigns | **Z-spread** (against sovereign spline). |
| **High-Grade Corp** | Swaps | **I-spread** or **Asset Swap Spread**. |
| **Sub-investment Grade** | CDS / Risk-free | Credit-specific Fair Value Models. |

[[During_Fixed_Income_Ch33.md#page=362-363]]

## Strategic Paradoxes

### 1. Cheap vs. Good Investment
A bond trading at a positive spline spread (meaning it is cheaper than its smooth theoretical curve) is not automatically a "Buy."
- **The Filter:** Analysts must determine if the cheapness is due to structural factors such as an upcoming surge in supply, a change in investor demand trends, or a decay in the liquidity of that specific ISIN. [[During_Fixed_Income_Ch33.md#page=363]]

### 2. The Repo Blindspot
Spline models are calibrated to **Spot Prices**, ignoring the repo market.
- **The Value:** A bond that is "Special" in the repo market (providing cheap borrowing) has a hidden value to the holder.
- **The Error:** A spline spread may label a bond as "Rich" (low yield) when it is actually trading at fair value once the repo benefit is incorporated into the forward price. [[During_Fixed_Income_Ch33.md#page=363]]

## Execution Vectors: Spread Strategies

- **Spread Tightener:** Long the bond, Pay the curve (short the benchmark). Used when a bond is relatively cheap (positive spline spread).
- **Spread Widener:** Short the bond, Receive the curve (long the benchmark). Used when a bond is relatively expensive (negative spline spread). [[During_Fixed_Income_Ch33.md#page=363-364]]

## Transmission Mechanism: Price-Yield Inverse

Sự thay đổi giá do lãi suất là nền tảng của Relative Value. Khi lãi suất biến động, giá trị của các thành phần trong danh mục RV (Bond vs. Hedge) thay đổi theo các cơ chế sau:

```ascii
LÃI SUẤT THỊ TRƯỜNG GIẢM (▼ r)
          │
          ▼
TĂNG GIÁ TRỊ HIỆN TẠI (PV) CỦA DÒNG TIỀN CỐ ĐỊNH
          │
          ▼
CẦU TRÁI PHIẾU CŨ TĂNG (▲ Demand) ───> CHI PHÍ CƠ HỘI (Opportunity Cost)
          │
          ▼
GIÁ TRÁI PHIẾU TĂNG (▲ Price)
          │
          ▼
RV ANALYSIS: So sánh mức tăng giá này với Benchmark
(Is the bond getting "richer" or "cheaper" relative to the curve?)
```

Cơ chế này đảm bảo rằng Yield luôn hội tụ về mức cân bằng thị trường thông qua sự điều chỉnh của Giá. Chi tiết về cơ chế chiết khấu và chi phí cơ hội xem tại [[Price_Yield_Inverse_Relationship]].

## Evidence / Source Anchors

- Rationale for spread selection based on professional hedge strategies: [[During_Fixed_Income_Ch33.md#page=362]]
- Analysis of SSA bond trading against French (OAT) rather than German (Bund) anchors: [[During_Fixed_Income_Ch33.md#page=363]]
- Definition of the "Cheap vs. Good" distinction in bond selection: [[During_Fixed_Income_Ch33.md#page=363]]
- Critique of spline models for neglecting repo specialness value: [[During_Fixed_Income_Ch33.md#page=363]]
- Linking spread widening/tightening to portfolio underweight/overweight decisions: [[During_Fixed_Income_Ch33.md#page=364]]

## Related

- [[Yield_Curve_Spreads_Taxonomy]] — Detailed mechanics of Z/I/Par spreads.
- [[Spread_Widener_Vs_Tightener]] — Detailed implementation strategies.
- [[Basis_Trade_Mechanics]] — Using futures as the hedge benchmark.
- [[Composite_Spline_Framework]] — How to build benchmarks for illiquid Agencies.
- [[General_Collateral_Vs_Special]] — The missing repo input for RV.
