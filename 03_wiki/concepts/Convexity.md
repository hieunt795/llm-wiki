---
title: Convexity
aliases:
- Bond Convexity
- Tính lồi của trái phiếu
type: definition
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: Multi-source
thesis: Convexity (Độ lồi) là một thước đo về mức độ thay đổi của Thời lượng (Duration)
  khi lãi suất thay đổi. Về mặt toán học, đây là đạo hàm bậc hai của giá trái phiếu
  theo lợi suất, chuẩn hóa theo giá. [[Tuckman_Serrat_2022.md#page=114]]
source_refs:
- Tuckman_Serrat_2022.md#page=113
- file: Schofield_Trading_Fixed_Income_2011.md
  page: 1967-2018
created: '2026-04-13'
updated: '2026-04-20'
chapter: 4
---

# [[Convexity]]

## Definition

Convexity (Độ lồi) là một thước đo về mức độ thay đổi của Thời lượng (Duration) khi lãi suất thay đổi. Về mặt toán học, đây là đạo hàm bậc hai của giá trái phiếu theo lợi suất, chuẩn hóa theo giá. [[Tuckman_Serrat_2022.md#page=114]]
$$C = \frac{1}{P} \frac{d^2P}{dy^2}$$

### Ý nghĩa kinh tế
- **Đặc trưng phi tuyến:** Mối quan hệ giữa giá trái phiếu và lãi suất không phải là một đường thẳng (linear) mà là một đường cong. Convexity giúp hiệu chỉnh sai số của Duration khi có những biến động lãi suất lớn.
- **Lợi thế cho nhà đầu tư:** Một trái phiếu có convexity dương sẽ có giá tăng nhanh hơn khi lãi suất giảm và giảm chậm hơn khi lãi suất tăng (so với dự báo của Duration). Do đó, convexity được coi là một "quyền chọn miễn phí". [[Fixed_Income_Alexander_During_Ch02.md#page=16]]

## Taylor Series Approximation (2022 Formulation)

Tuckman & Serrat (2022) nhấn mạnh việc sử dụng Convexity để cải thiện độ chính xác của ước tính thay đổi giá (Second-order approximation):
$$\frac{\Delta P}{P} \approx -D \Delta y + \frac{1}{2} C (\Delta y)^2$$
Trong đó số hạng $\frac{1}{2} C (\Delta y)^2$ luôn dương cho các trái phiếu truyền thống, bù đắp cho sự sụt giảm giá thấp hơn dự kiến khi lãi suất tăng và tăng giá cao hơn dự kiến khi lãi suất giảm.

### Case Study 1: Norfolk Southern (NSC) Century Bond (2121)
Trái phiếu Century (kỳ hạn 100 năm) minh họa cực đoan cho tác động của Convexity:
- **NSC 4.10s of 2121:** Có Convexity cực cao ($C \approx 1,101$) so với trái phiếu Treasury 5 năm ($C \approx 12$).
- **Hedge Implications:** Khi lập vị thế phòng vệ DV01-neutral (ví dụ: Mua NSC 2121, Bán Treasury 30 năm), nhà đầu tư sẽ ở vị thế **Long Convexity**. Vị thế này sẽ có lãi nếu lãi suất biến động mạnh theo bất kỳ hướng nào (hình dạng "smile"). [[Tuckman_Serrat_2022.md#page=117]]

### Case Study 2: Convexity Bias (Futures vs. Forward)
[RAW] Neftci giải thích ranh giới định giá giữa Eurodollar Futures và FRA (Forward Rate Agreement) thông qua Convexity:
- **The Bias:** Do cơ chế **Marking-to-Market** hàng ngày của Futures, dòng tiền lãi (khi lãi suất giảm) được nhận sớm hơn và có thể tái đầu tư. Ngược lại, khi lãi suất tăng, trader phải nộp thêm tiền ký quỹ.
- **Result:** Vì đồ thị payoff của lãi suất là lồi, sự biến động lãi suất tạo ra một lợi thế (Convexity gain) cho bên nắm giữ vị thế mua (long) Futures so với Forward.
- **Pricing Impact:** Lãi suất kỳ hạn hàm ý trong Futures (Futures Rate) thường cao hơn lãi suất Forward (Forward Rate) một khoảng bù đắp rủi ro gọi là **Convexity Adjustment**. Khoảng cách này tăng lên theo thời gian đáo hạn và mức độ biến động lãi suất. [[Principles_of_Financial_Engineering_Neftci.md#page=93]]

## 4. Failure Conditions / Boundaries
- **Negative Convexity:** [RAW] Một số công cụ (như trái phiếu có quyền chọn thu hồi - Callable bonds hoặc Mortgage-backed securities) có thể có convexity âm khi lãi suất giảm xuống một mức nhất định. Trong trường hợp này, giá tăng chậm hơn hoặc thậm chí giảm khi lãi suất tiếp tục giảm.
- **Model Risk:** Giả định các biến động lãi suất nhỏ và đường cong lãi suất dịch chuyển song song. Trong các cú sốc lớn, xấp xỉ bậc 2 vẫn có thể có sai số đáng kể.

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch02.md#page=15-16]] — Cơ chế toán học và ý nghĩa của Convexity trong quản trị rủi ro.
- [[Tuckman_Serrat_2022.md#page=114-116]] — Công thức đạo hàm bậc hai và ví dụ thực tế về Century Bonds.
- [[Principles_of_Financial_Engineering_Neftci.md#page=93]] — Giải thích Convexity Bias giữa Futures và Forward.

## Related
- [[Modified_Duration]] — Thước đo độ nhạy bậc 1.
- [[Eurodollar_Futures]] — Ứng dụng cụ thể của Convexity Bias.
- [[Macaulay_Duration]] — Cơ sở để tính toán các tham số rủi ro.
- [[Immunization]] — Chiến lược phòng vệ thường thất bại do sai số Convexity.
