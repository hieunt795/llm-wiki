---
title: Quantitative Tightening Mechanism
aliases:
- Quantitative Tightening
- QT
- Balance Sheet Normalization
type: mechanism
tags:
- central-banking
- monetary-policy
- QT
- liquidity
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: '[LLM]'
thesis: Quantitative Tightening (QT) is the reversal of Quantitative Easing, where
  the central bank shrinks its balance sheet to drain excess liquidity and tighten
  financial conditions, operating through non-linear mechanisms that risk fracturing
  market microstructures. | Quantitative Tightening (QT) là quá trình đảo ngược của
  Quantitative Easing, trong đó ngân hàng trung ương thu hẹp bảng cân đối kế toán
  nhằm rút cạn thanh khoản dư thừa và thắt chặt điều kiện tài chính, vận hành qua
  các cơ chế phi tuyến tính tiềm ẩn rủi ro đứt gãy cấu trúc vi mô thị trường.
source_refs:
- file: '[LLM — cần Raw Source: <tên sách/tài liệu dự kiến>]'
created: '2026-04-22'
updated: '2026-04-22'
---

## Thesis

[WIKI] Quantitative Tightening (QT) là quá trình đảo ngược của Quantitative Easing (QE), trong đó Ngân hàng Trung ương (NHTW) chủ động thu hẹp quy mô bảng cân đối kế toán bằng cách để trái phiếu đáo hạn mà không tái đầu tư (passive run-off) hoặc bán trực tiếp tài sản ra thị trường (active selling). Mục tiêu cốt lõi của QT là rút cạn thanh khoản dư thừa (Liquidity Drain) và thắt chặt các điều kiện tài chính tổng thể.

## 1. Cơ chế truyền dẫn và tác động vi mô (Transmission Channels)

[LLM] Khác với QE mang tính chất nới lỏng êm đềm, QT vận hành qua các cơ chế phi tuyến tính và tiềm ẩn rủi ro đứt gãy cấu trúc vi mô của thị trường. Quá trình truyền dẫn diễn ra qua ba kênh chính:

### Kênh rút cạn thanh khoản (Reserve Contraction)
Khi Kho bạc phát hành nợ mới để đảo nợ cũ mà NHTW không mua lại, khu vực tư nhân (các ngân hàng và quỹ đầu tư) buộc phải hấp thụ lượng cung này. Tiền từ tài khoản dự trữ của ngân hàng thương mại tại NHTW sẽ bị rút ra để thanh toán cho trái phiếu, làm giảm trực tiếp Base Money và lượng dự trữ (Inside Money) trong hệ thống.

### Kênh định giá lại rủi ro (Portfolio De-risking)
Trái ngược với hiệu ứng tái cân bằng danh mục của QE, QT đẩy một lượng lớn rủi ro kỳ hạn (duration risk) trở lại thị trường tư nhân. Giới đầu tư đòi hỏi phần bù rủi ro kỳ hạn (Term Premium) cao hơn để bù đắp cho việc phải hấp thụ nguồn cung tài sản này, đẩy cấu trúc lợi suất dài hạn tăng lên.

### Nghịch lý biến động (The Volatility Paradox Reversal)
[WIKI] Nếu QE triệt tiêu biến động để kích thích đầu tư, thì QT loại bỏ "lớp đệm" thanh khoản của NHTW. Khi dự trữ hệ thống mỏng đi, năng lực tạo lập thị trường (market-making capacity) của các Dealer bị thu hẹp. Bất kỳ cú sốc cung cầu nào cũng sẽ bị khuếch đại thành những đợt tăng vọt về biến động (Volatility Spikes).

## 2. Worked Example: Cơ chế dòng tiền trong QT

[LLM] Giả sử NHTW đang nắm giữ 50 tỷ USD trái phiếu chính phủ sắp đáo hạn. 

- **Trong kỷ nguyên QE:** Kho bạc trả 50 tỷ USD cho NHTW, và NHTW ngay lập tức dùng số tiền này tái đầu tư (roll-over) vào trái phiếu mới. Không có sự thay đổi ròng về mức tiền dự trữ trong hệ thống ngân hàng.
- **Trong kỷ nguyên QT (Run-off):** NHTW nhận 50 tỷ USD tiền gốc và quyết định xóa bỏ (tiêu hủy) số Base Money này khỏi bảng cân đối. Để huy động 50 tỷ USD trả cho NHTW, Kho bạc phải bán 50 tỷ USD trái phiếu mới cho khu vực tư nhân. Kết quả là 50 tỷ USD tiền gửi dự trữ (Reserve Balances) bị bốc hơi vĩnh viễn khỏi hệ thống ngân hàng thương mại.

## 3. Failure Conditions & The Stopping Point (Điểm dừng QT)

[RAW] Quá trình QT sẽ thất bại hoặc buộc phải dừng đột ngột nếu lượng Reserves rơi xuống dưới ngưỡng **"Ample Reserves Buffer"**. Theo Roc Armenter (2026), điểm dừng này được xác định bởi:

### The Napkin Math Boundary (T2 Structure)
Điểm dừng của QT không phải là một hằng số, mà phụ thuộc vào độ biến động của các yếu tố tự trị (autonomous factors):
$$B = \sigma \sqrt{\Delta} \cdot z^*$$
- **$\sigma$ (AF Volatility):** Tổng độ biến động của các yếu tố nằm ngoài kiểm soát trực tiếp của Fed (TGA, Tiền mặt). Xem chi tiết tại [[Autonomous_Factors_Framework]].
- **Risk Threshold:** Nếu Fed thắt chặt quá mức khiến lượng dự trữ giảm xuống gần mức $B$, xác suất xảy ra biến cố "No Bueno" (lãi suất Repo nhảy vọt như 9/2019) sẽ tăng lên theo hàm mũ.
- **TGA Volatility Constraint:** Hiện nay, độ biến động TGA ($\sigma$) cao buộc Fed phải dừng QT sớm hơn dự kiến (tại mức dự trữ cao hơn). Xem [[Treasury_General_Account_Mechanism]].

### Structural Fragility
- **Repo Market Freeze:** Khi thanh khoản dự trữ giảm xuống dưới ngưỡng an toàn, các ngân hàng sẽ găm giữ thanh khoản (liquidity hoarding) do Stigma của [[Discount_Window_Mechanism]].

## Evidence / Source Anchors

- [RAW] Napkin Math for stopping QT: [[Armenter_Napkin_Math_2026.md]]
- [RAW] Impact of TGA volatility on BS normalization: [[Armenter_Checking_Account_2026.md]]
- [RAW] Portfolio De-risking mechanics: [LLM — cần Raw Source xác thực thêm]

## Related

- [[Quantitative_Easing]]
- [[Central_Bank_Balance_Sheet_Trilemma]]
- [[Discount_Window_Mechanism]]
- [[Treasury_General_Account_Mechanism]]
