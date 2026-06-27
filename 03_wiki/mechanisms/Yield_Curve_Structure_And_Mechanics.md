---
title: Yield Curve Structure and Mechanics
aliases:
- Term Structure of Interest Rates
- Yield Curve Representations
- Forward Rate Bridge
- Turn Premium
- Cấu trúc kỳ hạn lãi suất
type: mechanism
tags:
- fixed-income
- monetary-policy
- math
- market-infrastructure
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Perry Warjiyo | Tuckman & Serrat | Alexander Düring"
provenance: Multi-source (During, Warjiyo & Tuckman)
thesis: The yield curve is the graphical and mathematical representation of the relationship
  between interest rates and time-to-maturity, functioning as the primary transmission
  vehicle for monetary policy and the essential bridge for pricing future capital
  flows.
source_refs:
- file: During_Fixed_Income_Ch15.md
  page: 131
- file: Tuckman_Serrat_2022.md
  page: 9
- file: Perry_Central_Bank_Policy_P3.md
  page: 124
- file: During_Fixed_Income_Ch19.md
  page: 191
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 3847-3919
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Yield curve không chỉ là một đồ thị; nó là "bản đồ thời gian" của tiền tệ. Alexander Düring bóc tách ranh giới toán học (Cơ chế No-arbitrage), Perry Warjiyo giải mã cơ chế dẫn truyền chính sách, và Tuckman & Serrat (2022) cập nhật ranh giới của các mỏ neo hiện đại (**RFRs**). Một đường cong lợi suất phản ánh sự cộng hưởng giữa nhu cầu thanh khoản tức thời và niềm tin vào sự ổn định vĩ mô trong tương lai. [[During_Fixed_Income_Ch15.md#page=131]] [[Tuckman_Serrat_2022.md#page=9]]

---

## 1. The Mathematical Trinity (Düring's Lens)

Mọi đường cong lợi suất đều có thể biểu diễn qua 4 hình thái tương đương về mặt toán học:
1.  **Discount Factor ($Df$):** Mỏ neo cơ bản nhất. PV của một đơn vị tiền tệ tương lai.
2.  **Zero Rate ($z$):** Lãi suất gộp cho kỳ hạn $t$. Liên kết: $Df(t) = e^{-zt}$.
3.  **Instantaneous Forward Rate ($f$):** Lãi suất kỳ hạn tại một thời điểm cực nhỏ. Công thức: $f(t) = - \frac{\partial \ln(Df(t))}{\partial t}$.
4.  **Par Yield ($Par$):** Mức coupon khiến trái phiếu giao dịch tại giá 100. [[During_Fixed_Income_Ch19.md#page=191]]

---

## 2. Modern Benchmarks: The RFR Revolution (Tuckman 2022)

Hậu thế giới LIBOR, ranh giới rủi ro của các đường cong chuẩn đã thay đổi bản chất:

### A. SOFR Curve (USD Standard)
- **Nature:** **Secured** (Có bảo đảm).
- **Basis:** Dựa trên giao dịch Repo trái phiếu chính phủ Mỹ. Đây là mỏ neo rủi ro thấp nhất vì được đảm bảo bằng tài sản cứng.

### B. €STR Curve (EUR Standard)
- **Nature:** **Unsecured** (Không bảo đảm).
- **Basis:** Dựa trên các khoản vay qua đêm liên ngân hàng. Dù được coi là "Risk-free", nó vẫn chứa một thành phần rủi ro tín dụng ngân hàng siêu nhỏ so với SOFR. [[Tuckman_Serrat_2022.md#page=12]]

---

## 3. Macro-Transmission (Warjiyo's Lens)

NHTW điều hành đường cong qua hai mỏ neo:
- **Short-end (0-2Y):** Ghim bằng lãi suất chính sách (BI Rate, Fed Funds).
- **Long-end (10Y-30Y):** Dẫn dắt bằng **Expectations Channel**. Nếu NHTW có uy tín (Credibility), kỳ vọng lạm phát dài hạn thấp sẽ giữ cho đường cong phẳng hoặc dốc xuống ngay cả khi lãi suất ngắn hạn tăng. [[Perry_Central_Bank_Policy_P3.md#page=124]]

---

## Evidence / Source Anchors

- Mathematical identity for instantaneous forward rates: [[During_Fixed_Income_Ch19.md#page=191]]
- Analysis of SOFR as a secured rate vs €STR as unsecured: [[Tuckman_Serrat_2022.md#page=12]]
- Description of the four equivalent curve representations (Figure 19.1): [[During_Fixed_Income_Ch19.md#page=191]]
- Rationale for OIS as the primary discounting curve post-GFC: [[Tuckman_Serrat_2022.md#page=9]]

## Related

- [[Nelson_Siegel_Svensson_Curve_Models]] — The optimization of curve fitting.
- [[OIS_And_Benchmark_Reform]] — Detailed view of the RFR shift.
- [[PCA_Yield_Curve_Decomposition]] — Decomposing curve movements into factors.
- [[Yield_Curve_Carry_And_Roll_Down]] — Trading the slope of the curve.
