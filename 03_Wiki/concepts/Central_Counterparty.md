---
type: definition
aliases: [CCP, Clearing House, Đối tác bù trừ tập trung]
sources: ["Fixed Income - Alexander During-13.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 12
---

# Central Counterparty

## Định nghĩa

**Central Counterparty (CCP)**, hay Đối tác bù trừ tập trung, là một cỗ máy trung gian giải quyết bài toán bùng nổ quan hệ tín dụng trong thị trường giao dịch. [extracted] [[Fixed Income - Alexander During-13.pdf#page=1]]

Thay vì một thị trường có $n$ người chơi phải duy trì $\frac{n(n-1)}{2}$ mạng lưới hạn mức tín dụng rối rắm với nhau (Bilateral), người ta chen một cái rốn CCP vào giữa. Lúc này thị trường chỉ còn đúng $n$ mối quan hệ: Tất cả mọi người đều chỉ nợ và đòi nợ duy nhất CCP. 

### Quy trình Give-up
Khi A và B trade xong một món hàng OTC (Thương lượng tay đôi xong xuôi), lệnh gốc bị xé bỏ và ngay lập tức được "giao bồi" (given up) cho CCP. Kể từ giây phút đó, hợp đồng đứt làm đôi: CCP nợ A (mua của A) và B nợ CCP (CCP bán cho B). [extracted] [[Fixed Income - Alexander During-13.pdf#page=1-2]]

- Lợi ích: Tối ưu hóa netting, tiết kiệm rào cản tín dụng.
- Rủi ro: CCP biến thành Single Point of Failure. Bản thân CCP đéo bao giờ tự mua bán sinh vị thế, nên nó không tự sập. Nó chỉ sập khi 1 tay to vỡ nợ diện rộng, CCP không còng lưng ra đền thay nổi cho phần còn lại. (Dẫn đến cơ chế bảo vệ [[CCP_Default_Waterfall]]). [extracted] [[Fixed Income - Alexander During-13.pdf#page=2]]

## Nguồn

- [[Fixed Income - Alexander During-13.pdf#page=1-2]] — Cơ chế n(n-1)/2 sang n, quy trình Give-up và rủi ro sập hệ thống.
