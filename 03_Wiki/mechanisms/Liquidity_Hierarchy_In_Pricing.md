---
type: mechanism
aliases: [Phân cấp thanh khoản định giá]
trigger: "Có tin tức kinh tế vĩ mô nổ ra (ví dụ Non-farm payrolls Mỹ)"
output: "Giá không update đồng thanh, mà đánh vào đỉnh chóp thanh khoản trước rồi nhỏ giọt lan truyền"
constraints: ["Giá chạy bằng phần mềm nội bộ của Market Maker"]
sources: ["Fixed Income - Alexander During-12.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 11
---

# Liquidity Hierarchy In Pricing

## Sự phân cấp phản ứng tin tức

Có một ảo tưởng rằng khi một tin tức vĩ mô nổ ra, toàn bộ các mã trái phiếu trên thị trường sẽ cập nhật giá ngay lập tức. Thực chất, tin tức thẩm thấu thông qua một cơ chế truyền dẫn tinh vi gọi là **Liquidity hierarchy (Phân cấp thanh khoản)**. [extracted] [[Fixed Income - Alexander During-12.pdf#page=1-2]]

1. **Điểm chóp nhọn (The tip of the spear):** Tin tức ập đến sẽ tác động ngay lập tức vào **công cụ có thanh khoản dày nhất**.
    - Tại Mỹ: Lực đánh dội thẳng vào kho bạc mới phát hành (On-the-run Treasury), theo sau là Agency Mortgages (MBS).
    - Tại Châu Âu và Nhật: Lực đánh dội thẳng vào thị trường Hợp đồng tương lai trái phiếu (Bond futures contracts).
2. **Quá trình cập nhật (Hierarchical Models):** Các ngân hàng/Market makers xây dựng mô hình thuật toán. Máy tính nhìn sự biến động giá của cái điểm chóp nhọn kia, rồi tính toán bù trừ tự động (pricing models) để nhả tỷ giá Bid-Ask mới cho những trái phiếu thanh khoản dạt (less liquid bonds). [extracted] [[Fixed Income - Alexander During-12.pdf#page=2]]

Nhờ có sự tập trung vào điềm chóp nhọn, những trái phiếu nào nắm ngôi vương benchmark (như On-the-run của Mỹ) tự nhiên sở hữu một "Liquidity premium" (Giá mắc hơn bình thường vì ai cũng muốn bâu vào nó để đánh lên đánh xuống khi có tin). [extracted] [[Fixed Income - Alexander During-12.pdf#page=2]]

## Nguồn

- [[Fixed Income - Alexander During-12.pdf#page=1-2]] — Dòng chảy rỉ giá cả từ On-the-run US/EU Futures xuống hàng tôm tép.
