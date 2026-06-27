---
title: "Bond Price-Yield Relationship"
aliases: [Price-Yield Mechanism, Yield Convergence]
type: mechanism
tags: [fixed-income, bond-math]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Sidney Homer | Martin L. Leibowitz"
provenance: "Homer_Leibowitz_Inside_the_Yield_Book.md"
thesis: "The inverse relationship between bond prices and yields is modulated by accrual offsets in duration-targeted portfolios, causing annualized returns to converge toward the initial yield over time."
source_refs:
  - file: "Homer_Leibowitz_Inside_the_Yield_Book.md"
    page: 11
  - file: Schofield_Trading_Fixed_Income_2011.md
    page: 352-358
    section: "Chapter 1.2.1: Bond fundamentals and price-yield relationship"
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
The inverse relationship between bond prices and yields is modulated by the mechanism of accrual offsets, where higher yields eventually compensate for capital losses in duration-targeted portfolios, leading to a "gravitational pull" toward the initial yield.

## 0. CURRENCY GATE
[⊘ skipped: half_life≥10]
**STALE_SIGNAL:** no

## 1. REGIME LOCK
Trong chế độ **Duration Targeting (DT)**, nhà quản lý duy trì một duration cố định thông qua việc tái cân bằng định kỳ (rebalancing). Channel **Accrual Offset** trở thành yếu tố chi phối (dominant) vì mọi biến động giá (price effect) do thay đổi lãi suất đều được bù đắp bởi dòng thu nhập (accrual) mới ở mức lãi suất thị trường hiện hành. Ngược lại, trong chế độ **Buy-and-Hold**, duration giảm dần theo thời gian, làm yếu đi khả năng bù đắp của accrual.

## 2. CAUSAL CHAIN
[LENSES: Sidney Homer — Bond Math; Martin L. Leibowitz — DT Dynamics; Alexander Düring — Risk Management]

Tình huống lãi suất tăng:
Lãi suất tăng $\rightarrow$ [Độ nhạy giá âm ($D$)] $\rightarrow$ Lỗ vốn (Capital Loss) $\rightarrow$ [Tái cân bằng tại Yield cao hơn] $\rightarrow$ Accrual tăng $\rightarrow$ [Thời gian nắm giữ $N \rightarrow N^*$] $\rightarrow$ Hồi phục vốn.

**Cơ chế truyền dẫn:**
1. **Price Impact:** Khi yield tăng, giá trái phiếu giảm ngay lập tức tỷ lệ với Macaulay Duration ($D$).
2. **Rebalancing:** Để duy trì $D$, trái phiếu cũ (duration ngắn lại) được bán để mua trái phiếu mới có duration dài hơn ở mức yield cao hơn.
3. **Accrual Offset:** Yield cao hơn này tạo ra mức tích lũy (accrual) lớn hơn trong các kỳ tiếp theo.
4. **Convergence:** Theo thời gian, tổng accrual tích lũy sẽ bù đắp hoàn toàn khoản lỗ vốn ban đầu.

[DENSE — Trendline Duration]:
$$D_{TL} = - \left[ \frac{D-1}{N} - \frac{N-1}{2N} \right]$$
→ INTENT: Model độ nhạy của tỷ suất sinh lời thực tế (annualized return) so với thay đổi yield trong khung thời gian $N$.
→ MECHANISM: $D_{TL}$ kết hợp cả tác động giá (vế đầu) và tác động tích lũy (vế sau).
→ INTERACTIONS: Khi $N$ tăng, vế đầu giảm dần về 0 trong khi vế sau tăng dần về 0.5.
→ BOUNDARY: Tại $N^* = 2D - 1$, $D_{TL} = 0$, triệt tiêu hoàn toàn rủi ro lãi suất đối với return mục tiêu.

## 3. FEEDBACK TOPOLOGY
**Balancing Loop:**
- Yield tăng $\rightarrow$ Price giảm (Negative Return).
- Price giảm $\rightarrow$ Reinvestment tại Yield cao $\rightarrow$ Accrual tăng (Positive Return).
- Tipping Point: **Effective Maturity ($N^*$)**. Trước điểm này, price effect thống trị; sau điểm này, accrual effect thống trị.

## 4. CHANNEL INTERACTION
Tương tác giữa **Duration Factor** và **Accrual Factor**:
- Trong ngắn hạn ($N < D$), Duration Factor chiếm ưu thế, return biến động mạnh theo giá.
- Trong dài hạn ($N > 2D$), Accrual Factor chiếm ưu thế, return có xu hướng vượt qua yield ban đầu nếu lãi suất tăng ổn định.
- Tại VN: Với các danh mục trái phiếu Chính phủ có $D \approx 5$ năm, thời gian để "miễn dịch" thực tế với biến động lãi suất là khoảng 9 năm [RAW-practitioner].

## 5. QUANTIFIED ANCHOR
[RAW] Source: Homer & Leibowitz, p. 14
- Với duration mục tiêu $D = 5$, điểm hội tụ (Effective Maturity) là $N = 9$ năm.
- Trong kịch bản lãi suất tăng 50 bps/năm, return năm thứ 5 đạt 0% excess return (bù đắp xong lỗ vốn năm đó), nhưng cần đến năm thứ 9 để annualized return hội tụ về yield ban đầu 3%.

## 6. BOUNDARY CONDITIONS
- **Duration Shift:** Cơ chế hội tụ thất bại nếu nhà đầu tư thay đổi duration mục tiêu giữa chừng (ví dụ: rút ngắn duration khi sợ lãi suất tăng).
- **Convexity Dominance:** Với biến động yield cực lớn, tính lồi (convexity) của đường cong giá có thể làm sai lệch các model tuyến tính hóa $D_{TL}$.
- **Yield Trap:** Nếu lãi suất giảm sâu và duy trì ở mức thấp, accrual offset âm sẽ kéo return xuống dưới mức yield ban đầu.

## Related
- [[Compound_Interest_Time_Value]]
- [[Macaulay_Duration]]
- [[Immunization_Strategy]]
