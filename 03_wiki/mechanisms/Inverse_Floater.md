---
title: Inverse Floater
aliases:
- Trái phiếu FRN nghịch đảo
- Nghịch đảo thả nổi
- Reverse Floater
- max(0, mu - R)
type: mechanism
tags:
- bonds
- structured-finance
- interest-rates
- leverage
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Howard Corb | Alexander Düring"
provenance: Multi-source
thesis: An Inverse Floater is a structured debt instrument where the coupon moves
  in the opposite direction of the reference benchmark rate, significantly magnifying
  interest rate sensitivity (duration) through embedded leverage and optionality.
source_refs:
- file: Fixed_Income_Alexander_During_Ch17.md
  page: 171
- file: Howard_Corb_Swaps.md
  page: 312
- file: Howard_Corb_Swaps.md
  page: 321
created: '2026-04-13'
updated: '2026-04-20'
---

## Thesis

Trong khi các công cụ lãi suất nổi (FRN) truyền thống bảo vệ nhà đầu tư khỏi lãi suất tăng, **Inverse Floater** được thiết kế để đặt cược vào kịch bản lãi suất giảm. Bằng cách nhúng một vị thế Short vào công cụ lãi suất nổi, nó phóng đại Duration và độ nhạy của trái phiếu, biến nó thành một công cụ đầu cơ mạnh mẽ nhưng cực kỳ rủi ro.

---

## 1. Mechanism: The Inverse Formula

Công thức Coupon ($C_i$) cơ bản:
$$C_i = \max(0, \mu - L \times R)$$

Trong đó:
- $\mu$: Mức lãi suất cố định (Cap), thường là một con số lớn (VD: 15-20%) để bù đắp cho phần bị trừ.
- $L$: Hệ số đòn bẩy (Leverage factor). Nếu $L > 1$, đây được gọi là **Leveraged Inverse Floater**.
- $R$: Chỉ số tham chiếu (Benchmark) như LIBOR, SOFR.

**Đặc điểm kinh tế:**
- **Lãi suất giảm:** Coupon tăng. Giá trái phiếu tăng mạnh do tác động kép: dòng tiền (Cash flow) tăng và tỷ lệ chiết khấu (Discount rate) giảm.
- **Lãi suất tăng:** Coupon giảm. Nếu $L \times R \geq \mu$, Coupon sẽ chạm mức sàn (thường là 0%). [[Corb_Swaps#page=312]]

---

## 2. Technical Decomposition

Howard Corb giải mã cấu trúc của một Inverse Floater (với mệnh giá 100) thành một danh mục bao gồm:
1.  **Long Fixed Rate Bonds:** Nắm giữ $L+1$ đơn vị trái phiếu lãi suất cố định với Coupon $\mu / (L+1)$.
2.  **Short Floating Rate Notes:** Bán khống $L$ đơn vị FRN.
3.  **Long Caps:** Mua $L$ đơn vị Cap với Strike $K = \mu / L$ để bảo vệ khỏi Coupon âm. [[Corb_Swaps#page=319]]

---

## 3. Risk Profile: Magnified Duration

Inverse Floater có **Effective Duration** cực kỳ cao, thường vượt xa kỳ hạn thực tế của nó. 
- **Lý do:** Khi lãi suất tăng 1%, giá trị hiện tại bị trúng "đòn kép": (1) Tỷ lệ chiết khấu tăng và (2) Dòng tiền coupon kỳ vọng giảm.
- **Ví dụ:** Một Leveraged Inverse Floater kỳ hạn 4 năm có thể có Duration lên tới 10 năm trong môi trường lãi suất thấp. [[Corb_Swaps#page=316]]

---

## 4. Case Study: The Orange County Bankruptcy (1994)

Vụ phá sản của Orange County là minh chứng điển hình cho ranh giới của việc lạm dụng đòn bẩy:
- **Chiến lược:** Bob Citron (Treasurer) đầu tư mạnh vào Leveraged Inverse Floaters và tiếp tục dùng chúng làm tài sản thế chấp trong các giao dịch Repo để vay tiền mua thêm (Double Leverage).
- **Cú sốc:** Năm 1994, Fed tăng lãi suất từ 3% lên 5.5%. 
- **Hậu quả:** 
    1. Coupon của Inverse Floaters lao dốc về 0.
    2. Giá trị tài sản thế chấp (Bond Price) sụp đổ do Duration quá cao.
    3. Các Dealer gọi ký quỹ (Margin Call), dẫn đến việc thanh lý cưỡng bức và khoản lỗ 1.7 tỷ USD. [[Corb_Swaps#page=321]]

---

## Evidence / Source Anchors

- General formula and leverage factor: [[Corb_Swaps#page=312]]
- Decomposition into Fixed/Floating/Cap: [[Corb_Swaps#page=319]]
- Analysis of effective duration sensitivity: [[Corb_Swaps#page=316]]
- Historical account of Orange County bankruptcy: [[Corb_Swaps#page=321]]

## Related

- [[Floating_Rate_Notes_FRN]] — Công cụ nền tảng.
- [[Structured_Notes]] — Lớp tài sản bao hàm.
- [[Interest_Rate_Risk_Duration_Convexity]] — Để hiểu về sự phóng đại rủi ro.
- [[Repurchase_Agreements_Repo]] — Cơ chế đòn bẩy bổ sung trong vụ Orange County.
