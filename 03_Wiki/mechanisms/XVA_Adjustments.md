---
type: mechanism
aliases: [CVA, FVA, DVA, Điều chỉnh giá trị định giá phi tập trung]
trigger: "Tranh cãi rằng chuẩn IFRS 39 Fair Value là rác vì nó giả định phi ma sát"
output: "Giá của một tài sản phải bị bẻ cong tùy thuộc vào việc bạn là ai, chi phí vốn và rủi ro đối tác hiện tại của bạn là gì"
constraints: ["Không có cái gọi là Arm's length price giữa hai người mua bán vô danh"]
sources: ["Fixed Income - Alexander During-13.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 12
---

# XVA Adjustments

## Cánh bướm của Kế toán vs Dữ kiện thực

Các chuẩn mực kế toán (như IFRS 39 định nghĩa giá trị Fair Value / Mark-to-market) giả định rất thơ mộng về các giao dịch tay bo: "Giá được định trong một giao dịch sòng phẳng cánh tay dài (arm's length) giữa bên mua tự nguyện và bên bán tự nguyện".
Giới Phái sinh (Derivatives/Quant) vạch trần câu này là vô nghĩa. Giá giao dịch của một tài sản ở chợ đen phụ thuộc đẫm máu vào **Túi tiền và Hệ sinh thái nợ nần riêng** của hai kẻ đang đứng đối mặt. Do đó đẻ ra hệ phái bù trừ XVA: [extracted] [[Fixed Income - Alexander During-13.pdf#page=8]]

### 1. Credit Value Adjustment (CVA)
Dùng khi trade không qua CCP (mù mờ tin tưởng). Nếu tài sản đang xanh (Lãi), bạn có rủi ro thằng hứa trả tiền cho bạn vỡ nợ. Bạn phải lập quỹ phòng hờ hao tổn dựa trên mức xếp hạng tín nhiệm của nó. CVA tàn khốc ở chỗ: Nếu bạn nợ nó nhiều hơn nó nợ bạn, CVA sẽ bị giảm đi gánh bớt. Thế là giá của món hàng vừa bị bẻ cong theo *Mối quan hệ đôi lứa* thay vì là "Arm's length transactions"! [extracted] [[Fixed Income - Alexander During-13.pdf#page=8-9]] (Thường Hedge bằng thị trường CDS).

### 2. Funding Value Adjustment (FVA)
Dùng khi lệnh đã qua lưới CCP. Lúc này CVA biến mất, nhưng có [[Variation_Margin_Vs_Initial_Margin|Ký quỹ VM]]. Nếu lệnh của bạn Đỏ (Lỗ), CCP bắt bạn nộp thẳng Tiền mặt mỗi ngày. Bạn đi mượn tiền mặt từ sếp với lãi gắt (Funding cost), nhưng CCP chỉ trả lại bạn lãi 0 đằng thẳng (Overnight cash returns). Khoản lủng bù chênh lãi vay tàn sát ví tiền của bạn, và nó được bù vào giá giao dịch bằng cục cựa FVA. Đau đớn là FVA làm các bank chết cứng vì mismatch giữa cách đóng hụi margin chết và rủi ro. [extracted] [[Fixed Income - Alexander During-13.pdf#page=9]]

### 3. Debit Value Adjustment (DVA)
Kỳ cục nhất thế kỷ. Trong một số hợp đồng sòng phẳng, nếu Xếp hạng tín nhiệm (Credit rating) của chính Bản Thân Bạn bị giám đốc tín dụng đánh rớt hạng, bạn phải tự mang thêm Margin chêm vào quỹ. Nghĩa là bạn đang tàn tạ mà còn mang gánh cước phí thù oán tự sát. DVA là khoản phản hồi chết chóc ép Bank phải tự đi hedge lại Credit Risk của...chính nó (điều bất khả thi vĩ đại). [extracted] [[Fixed Income - Alexander During-13.pdf#page=10]]

## Nguồn

- [[Fixed Income - Alexander During-13.pdf#page=8-10]] — Lỗ hổng Arm's length valuation của IFRS 39, cơ chế ma mị của CVA, FVA và DVA.
