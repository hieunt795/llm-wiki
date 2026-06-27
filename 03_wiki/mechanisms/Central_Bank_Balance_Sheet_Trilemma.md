---
title: Central Bank Balance Sheet Trilemma
aliases:
- Balance Sheet Trilemma
- The Impossible Trinity of Operations
type: mechanism
tags:
- monetary-policy
- central-bank-balance-sheet
- liquidity-management
- fed
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Roc Armenter | Viral Acharya
provenance: Roc Armenter (Fed Philadelphia, 2026)
thesis: 'A central bank can simultaneously achieve only two of the following: (1)
  a small balance sheet, (2) low short-term rate volatility, and (3) limited intervention
  in money markets. / Một ngân hàng trung ương chỉ có thể đồng thời đạt được hai trong
  ba mục tiêu: (1) bảng cân đối kế toán nhỏ, (2) biến động lãi suất ngắn hạn thấp,
  và (3) hạn chế can thiệp vào thị trường tiền tệ.'
source_refs:
- file: Breaking Out of the Central Bank Balance Sheet Trilemma.md
- file: False Trilemmas.md
- file: Napkin Math for an Ample Reserves Buffer.md
- file: The Checking Account of the U.S. Federal Government....md
created: '2026-04-28'
updated: '2026-04-28'
---

# [[Central_Bank_Balance_Sheet_Trilemma]]

## Thesis

[RAW] Trong khung vận hành (operating framework) hiện tại, NHTW đối mặt với sự đánh đổi mang tính cấu trúc giữa quy mô tài sản, khả năng kiểm soát lãi suất và mức độ can thiệp trực tiếp. Việc duy trì một hệ thống dự trữ dư thừa (Ample Reserves) cho phép ổn định lãi suất mà không cần can thiệp thường xuyên, nhưng đổi lại bảng cân đối kế toán phải duy trì ở quy mô lớn.

## 1. Operational Trade-offs (Sự đánh đổi vận hành)

Dựa trên phân tích của Roc Armenter, cơ chế đánh đổi được bóc tách như sau:

- **Regime A: Ample Reserves (Hiện tại):**
  - **Mục tiêu đạt được:** Low Volatility + Limited Intervention.
  - **Cơ chế:** Fed duy trì lượng Reserves lớn hơn nhu cầu tối thiểu của các ngân hàng. Lãi suất thị trường được neo bởi lãi suất trả trên tiền gửi dự trữ (IORB) và cơ sở Reverse Repo (ON RRP).
  - **Hệ quả:** Bảng cân đối (BS) phình to.

- **Regime B: Scarcity (Trước 2008):**
  - **Mục tiêu đạt được:** Small BS + Limited Intervention.
  - **Cơ chế:** Lượng dự trữ được giữ ở mức tối thiểu.
  - **Hệ quả:** Bất kỳ cú sốc thanh khoản nhỏ nào (v.d nộp thuế doanh nghiệp) cũng gây ra biến động lãi suất ngắn hạn cực lớn (High Volatility).

- **Regime C: Corridors with Intervention:**
  - **Mục tiêu đạt được:** Small BS + Low Volatility.
  - **Cơ chế:** Fed phải thực hiện các hoạt động thị trường mở (OMO) hàng ngày để bơm/hút thanh khoản chính xác vào các "túi" thiếu hụt.
  - **Hệ quả:** Can thiệp thị trường thường xuyên (Heavy Intervention).

## 2. Breaking the Trilemma: Local vs. Global View

[RAW] Dựa trên triết lý **"False Trilemmas" (Roc Armenter)**, một Trilemma chỉ là sự phản ánh rằng hệ thống đang ở biên giới khả thi (Frontier). Nó có thể bị bẻ gãy nếu ta thay đổi các biến số "Global" nằm ngoài bộ ba (X, Y, Z) ban đầu.

### 2.1 The "Local" Truth (Sự thật tại chỗ)
Trong bối cảnh quy định hiện tại (các công cụ và hệ thống hiện hành), Trilemma là có thật (locally true). NHTW không thể giảm BS mà không gây biến động lãi suất nếu không can thiệp sâu. Đây là bối cảnh mà các đồng nghiệp Fed (Bump-Kahn) đã đúng.

### 2.2 The "Global" Solution (Giải pháp tổng thể)
Trilemma có thể trở thành **"False Trilemma"** (globally false) nếu NHTW thay đổi cấu hình hệ thống (biến số bên ngoài):
- **Variable A: De-stigmatizing the [[Discount_Window_Mechanism]].** Nếu DW trở thành một công cụ vay mượn bình thường (không bị định kiến), ngân hàng sẽ không cần găm giữ lượng Reserves khổng lồ để tự bảo hiểm. Đây là chìa khóa để đạt được **Small BS + Low Volatility**.
- **Variable B: TGA Stabilization.** Thay đổi cơ chế phối hợp với Bộ Tài chính để giảm độ biến động của TGA ($\sigma$), từ đó giảm quy mô dự trữ đệm (Buffer). Theo Armenter, việc ổn định TGA có thể giúp giảm quy mô bảng cân đối khoảng **2 điểm phần trăm (pp) GDP danh nghĩa**. Xem [[Treasury_General_Account_Mechanism]].
- **Variable C: Implementation Framework.** Thay đổi sang cơ chế mục tiêu dự trữ tự nguyện (như BoE) hoặc sử dụng term repos để quản lý BS size một cách linh hoạt hơn.

---

## 3. The "Ample Reserves Buffer" (Napkin Math)

[RAW] Lượng dự trữ đệm cần thiết để duy trì tính ổn định (Low Volatility) được tính toán dựa trên độ biến động của các yếu tố tự trị (chủ yếu là TGA):

$$B = \sigma \sqrt{\Delta} \cdot z^*$$

- **$\sigma$:** Độ lệch chuẩn của thay đổi TGA (hiện tại ~$100B/2 tuần).
- **$\Delta$:** Khoảng thời gian giữa các phiên can thiệp của Fed.
- **$z^*$:** Khẩu vị rủi ro (critical value).
- **Surgical Insight:** Buffer hiện nay cần khoảng $300-400B do $\sigma$ cao. Nếu đưa TGA về mức biến động trước 2020 ($\sigma \approx 50B$), Buffer có thể giảm xuống còn $100-150B, giải phóng đáng kể quy mô bảng cân đối.

---

## 4. The "Ratchet Effect" of Reserves (Viral Acharya)

[WIKI] Một trở ngại lớn của việc thu hẹp BS là hiệu ứng **Ratchet (Bánh răng)**:
- Khi NHTW cung cấp quá nhiều dự trữ trong thời gian dài, các ngân hàng thương mại sẽ tái cấu trúc tài sản và quy định nội bộ dựa trên sự dư thừa đó.
- Nhu cầu dự trữ trở thành một biến số "tự tạo ra chính nó" (Self-fulfilling demand), khiến việc quay lại bảng cân đối nhỏ trở nên cực kỳ rủi ro.

---

## 5. Japan Case Study: The "Negative Resilience" Model

[WIKI] Nhật Bản cung cấp một ví dụ cực đoan về việc lựa chọn biên giới trong Trilemma:
- **Lựa chọn:** Bảng cân đối cực lớn (BS > 120% GDP) + Lãi suất cực thấp (Low Volatility) + Can thiệp sâu (Heavy Intervention qua YCC).
- **The Trade-off (Sự đánh đổi):** Để duy trì mô hình này, BoJ và Chính phủ Nhật Bản đã chấp nhận hy sinh hoàn toàn yếu tố **Resilience (Khả năng chống chịu)**.
- **Cơ chế bẻ gãy:** Thay vì coi bảng cân đối lớn là một gánh nặng, Nhật Bản biến nó thành một **Sovereign Wealth Fund** khổng lồ vay vốn ngắn hạn để đầu tư tài sản rủi ro dài hạn. Xem chi tiết tại [[Japan_Debt_Puzzle_Mechanism]].

**Surgical Insight:** Mô hình Nhật Bản cho thấy Trilemma có thể bị "vô hiệu hóa" tạm thời nếu NHTW chuyển trạng thái từ **Người điều hành (Regulator)** sang **Người đầu cơ (Speculator)** trên quy mô toàn cầu. Tuy nhiên, điều này tạo ra một "Duration Gap" khổng lồ giữa tài sản và nợ phải trả, khiến toàn bộ hệ thống trở nên cực kỳ nhạy cảm với cú sốc lãi suất thực.

## Evidence / Source Anchors

- [RAW] Definition of the trilemma: [[Breaking Out of the Central Bank Balance Sheet Trilemma.md]]
- [RAW] Logic of False Trilemmas: [[False Trilemmas.md]]
- [RAW] TGA impact and Napkin Math: [[Napkin Math for an Ample Reserves Buffer.md]]
- [RAW] Ratchet effect of reserves: [[Acharya_Jackson_Hole_2022.pdf]]
- [RAW] Japan as a Consolidated SWF: [[Japan_Debt_Puzzle_Mechanism]]

## Related

- [[Treasury_General_Account_Mechanism]]
- [[Quantitative_Tightening_Mechanism]]
- [[Japan_Debt_Puzzle_Mechanism]]
- [[Blue_Bond_Mechanism]]
- [[ESBies_Mechanism]]
- [[Monetary_Policy_Trilemma]]
