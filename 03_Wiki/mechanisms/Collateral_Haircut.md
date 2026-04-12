---
type: mechanism
aliases: [Chiết khấu tài sản thế chấp, Wrong-way risk, Repo Margin]
trigger: "Trái phiếu cầm cố có nguy cơ rớt giá cực mạnh trong đêm nếu có sấm chớp giang hồ"
output: "Đập thẳng Haircut 1-50% vào mệnh giá để dư ra một cục thịt bảo kê rủi ro thanh lý"
constraints: ["Ngân hàng thương mại chết chung chùm nếu nhận Trái phiếu từ Kẻ vay là anh em thân thiết (Wrong-way risk)"]
sources: ["Fixed Income - Alexander During-15.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 14
---

# Collateral Haircut

## Lưỡi chém đề phòng trượt giá

Trong giao kèo [[Repurchase_Agreement]], nếu bạn ôm tới $\yen 10$ tỷ (Mark-to-market value) trái phiếu Nhật tới gõ cửa nhà băng vay tiền, họ đéo bao giờ ói ra cho bạn đúng $\yen 10$ tỷ tiền mặt. Họ sẽ vụt một tỉ lệ hao hụt gọt đầu gọi là **Haircut**. [extracted] [[Fixed Income - Alexander During-15.pdf#page=3]]

- Với Haircut 1% trên 10 tỷ Yên, bạn chỉ cầm về túi mớ tiền rẻ mạt 9.9 tỷ. Phần 100 triệu Yên lòi ra đó là đệm an toàn.
- Haircut cho rác chính phủ mượt dao động tầm 0-1%. Nhưng với Cổ phiếu (Equity) trồi sụt loạn xì ngầu, nó giật lên tới đàng hoàng 50%! [extracted] [[Fixed Income - Alexander During-15.pdf#page=3]]

## Wrong-way Risk (Rủi ro điêu đứng kép)
Đối với dân Ngân hàng Trung Ương (Central Banks), Haircut là con dao đồ tể mang hình hài công lý. Bất cứ con bank tư nhân nào rón rén ôm Trái Phiếu lên nộp đòi bơm tiền, NHTW hoàn toàn có quyền chém Haircut trên trời do một thế cờ gọi là **Wrong-way Risk** khét lẹt. [extracted] [[Fixed Income - Alexander During-15.pdf#page=3]]

- Đám Ngân hàng rất hay mang nộp trái phiếu Của Những Công Ty Mà Chúng Nó Cho Vay (Collateral that is correlated with their own stability). 
- Khi đại khủng hoảng nổ, Trái phiếu này rớt phịch xuống cống, kéo theo Con Ngân Hàng cầm nợ tàn lụi theo. Hai quả mìn đó phát nổ *CÙNG MỘT LÚC*, biến đống tài sản cầm cố của NHTW (người đang giải cứu) thành mớ giẻ lau hư hỏng! 

## Nguồn

- [[Fixed Income - Alexander During-15.pdf#page=3]] — Cơ năng phòng ngự của Haircut trên giá trị MTM, và hội chứng Wrong-way risk ám ảnh giới chức ban hành chính sách.
