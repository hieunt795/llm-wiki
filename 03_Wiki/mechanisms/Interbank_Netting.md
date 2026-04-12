---
type: mechanism
trigger: "Khách hàng chuyển tiền giữa các ngân hàng khác nhau"
output: "Giảm lượng tín dụng liên ngân hàng phải thanh toán"
constraints: ["Cần thỏa thuận song phương hoặc đa phương"]
sources: ["Fixed Income - Alexander During-5.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 4
---

# Interbank Netting

## Cơ chế

Khi khách hàng chuyển khoản liên ngân hàng, họ thực chất yêu cầu ngân hàng nhận **chấp nhận rủi ro tín dụng của ngân hàng gửi**. Lượng interbank credit này có thể được giảm thiểu thông qua **gù trừ (netting)**. [extracted] [[Fixed Income - Alexander During-5.pdf#page=3]]

Có hai hình thức chính:

1. **Bilateral Netting**: Ngân hàng A và B tính toán **luồng ròng (net flow)** giữa họ. Nếu A nợ B 100 và B nợ A 80, A chỉ đơn giản thanh toán net là 20 cho B. [extracted] [[Fixed Income - Alexander During-5.pdf#page=3]]
2. **Multilateral Netting**: Hiệu quả hơn. Tính toán luồng ròng qua nhiều bên trung gian (sử dụng ma trận các luồng thanh toán, tính tổng Gross Inflows và Gross Outflows để ra Net Amount cuối cùng). [extracted] [[Fixed Income - Alexander During-5.pdf#page=3-4]] (Xem Figure 4.3 trong sách).

Netting hiệu quả hơn nếu được thực hiện với **khối lượng thanh toán lớn hơn**, dẫn đến xu hướng **giữ các khoản thanh toán trong một thời gian** trước khi bù trừ. [extracted] [[Fixed Income - Alexander During-5.pdf#page=4]]

## Điều kiện

- Dù sau khi bù trừ, số dư ròng cuối ngày **vẫn không phải là 0**. Do đó, vẫn cần cơ chế thanh toán ròng (qua [[Nostro_Account]] hoặc Central Bank). [extracted] [[Fixed Income - Alexander During-5.pdf#page=4]]
- Thời gian giữ thanh toán dài hơn (longer netting period) hiệu quả hơn nhưng cũng **làm tăng rủi ro hệ thống** do build-up mất cân bằng. [extracted] [[Fixed Income - Alexander During-5.pdf#page=4]]

## Nguồn

- [[Fixed Income - Alexander During-5.pdf#page=3]] — Logic credit risk liên ngân hàng
- [[Fixed Income - Alexander During-5.pdf#page=4]] — Figure 4.3 và Multilateral Netting
