---
title: "Compound Interest & Time Value"
aliases: [Power of Compounding, Interest on Interest]
type: mechanism
tags: [fixed-income, bond-math]
status: verified
confidence: 4
half_life_years: 10
expert_lens: "Sidney Homer | Martin L. Leibowitz"
provenance: "Homer_Leibowitz_Inside_the_Yield_Book.md"
thesis: "Compound interest serves as the engine of fixed-income returns, where 'interest-on-interest' grows non-linearly over time to eventually dominate initial yield and price effects."
source_refs:
  - file: "Homer_Leibowitz_Inside_the_Yield_Book.md"
    page: 12
created: 2026-04-28
updated: 2026-04-28
---

## Thesis
Compound interest serves as the engine of bond returns, where interest-on-interest (accruals) grows non-linearly over time, eventually dominating price effects in fixed-income portfolios.

## 0. CURRENCY GATE
[⊘ skipped: half_life≥10]
**STALE_SIGNAL:** no

## 1. REGIME LOCK
Trong chế độ đầu tư dài hạn (**Multi-period Investment**), lãi suất kép (Compound Interest) là channel chủ đạo. Hiệu ứng này đặc biệt mạnh mẽ trong các danh mục có tái đầu tư coupon (reinvestment) hoặc trái phiếu không coupon (zero-coupon) nơi lãi suất được tích lũy nội tại.

## 2. CAUSAL CHAIN
[LENSES: Sidney Homer — Compound Interest; Martin L. Leibowitz — Yield Book Science; Neil Schofield — Trading FI]

Vốn gốc $\rightarrow$ [Lãi suất $y$] $\rightarrow$ Coupon $\rightarrow$ [Tái đầu tư tại $y'$] $\rightarrow$ Lãi trên lãi (Interest-on-Interest) $\rightarrow$ [Tăng trưởng hàm mũ] $\rightarrow$ Tổng tài sản.

**Cơ chế truyền dẫn:**
1. **Initial Accrual:** Trong kỳ đầu tiên, lợi nhuận chỉ dựa trên yield ban đầu.
2. **Reinvestment:** Các kỳ tiếp theo, lãi nhận được được tái đầu tư, bắt đầu tạo ra "interest-on-interest".
3. **Non-linear Growth:** Tốc độ tích lũy accrual tăng dần theo thời gian, tỷ lệ thuận với bình phương thời gian nắm giữ ($N^2$) trong các model xấp xỉ tuyến tính.
4. **Dominance:** Sau một ngưỡng thời gian nhất định, phần lãi trên lãi này vượt xa giá trị coupon gốc và biến động giá ban đầu.

[DENSE — Accrual Factor]:
$$Accrual Factor = \frac{1 - 1/N}{2}$$
→ INTENT: Model tỷ lệ yield thặng dư (excess accrual) so with tổng thay đổi yield trong $N$ năm.
→ MECHANISM: Giá trị này tăng dần theo $N$, tiến tới giới hạn 0.5.
→ INTERACTIONS: Kết hợp with Duration Factor để triệt tiêu rủi ro giá (Price Risk).
→ BOUNDARY: Chỉ hold khi giả định tái đầu tư liên tục tại mức yield biên.

## 3. FEEDBACK TOPOLOGY
**Reinforcing Loop:**
- Tài sản tích lũy lớn hơn $\rightarrow$ Lãi tạo ra nhiều hơn $\rightarrow$ Cơ sở tái đầu tư lớn hơn $\rightarrow$ Tài sản tích lũy tăng tốc.
- Escape Condition: Rút vốn (withdrawal) hoặc vỡ nợ (default) của tổ chức phát hành.

## 4. CHANNEL INTERACTION
Tương tác with **Price Channel**:
- Trong các năm đầu, biến động giá do lãi suất thị trường lấn át hoàn toàn accrual.
- Qua thời gian, lãi kép tạo ra một "đệm an toàn" (buffer) chống lại các cú sốc giá.
- Đối với trái phiếu Chính phủ 30 năm, hơn 60% tổng lợi nhuận thực tế đến từ lãi trên lãi chứ không phải coupon gốc [RAW-BOOK].

## 5. QUANTIFIED ANCHOR
[RAW] Source: Homer & Leibowitz, p. 12
- Công thức giá trị tương lai: $FV = PV(1 + r)^N$.
- Trong model Trendline với $N=5$, Accrual Factor là 0.4. Nghĩa là trung bình 40% mức thay đổi yield được chuyển hóa thành lợi nhuận tích lũy thặng dư hàng năm.

## 6. BOUNDARY CONDITIONS
- **Reinvestment Risk:** Nếu lãi suất tái đầu tư ($y'$) thấp hơn đáng kể so với yield ban đầu ($y$), engine lãi kép sẽ bị "hụt hơi", không đạt được mức realized yield kỳ vọng.
- **Inflation Erosion:** Lãi suất kép có thể tạo ra con số danh nghĩa ấn tượng nhưng bị bào mòn bởi lạm phát (Real Value breakdown).
- **Taxation:** Thuế đánh trên coupon làm giảm cơ sở vốn tái đầu tư, làm chậm đáng kể loop lãi kép.

## Related
- [[Bond_Price_Yield_Relationship]]
- [[Yield_to_Maturity]]
- [[Future_Value]]
