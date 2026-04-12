---
type: mechanism
trigger: "Nhu cầu kiểm soát lãi suất liên ngân hàng trong điều kiện bình thường"
output: "Lãi suất bị khóa trong dải hành lang giữa vay khẩn cấp và lợi gửi trần"
constraints: ["Hệ thống ngân hàng phải có tính tự cân đối thiếu hụt tự nhiên"]
sources: ["Fixed Income - Alexander During-7.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 6
---

# Symmetric Interest Rate Corridor

## Cơ chế

Bên ngoài các thời kỳ khủng hoảng kinh tế, các [[Central_Bank]] vận hành cấu trúc mỏ neo lãi suất gọi là **Hành lang lãi suất đối xứng (Symmetric corridor system)**.
Trong cấu trúc này, thanh khoản mà trung ương bơm ra là **rất tối thiểu**, chỉ để bù trừ đủ nhu cầu vật chất từ lượng rút tiền, dữ trữ pháp định pháp lý. Lãi suất thị trường sẽ dao động đập lên đập xuống giữa một đường hầm. [extracted] [[Fixed Income - Alexander During-7.pdf#page=8]]

### Cấu trúc 3 công cụ (Three Tools)

1. **Công cụ định hình biên dưới (Lower bound)**: Cơ sở vật chất gửi tiền qua đêm hấp thụ dòng tiền rảnh rỗi. Lãi suất tiền gửi này giữ các ngân hàng không ném tiền phá giá thị trường (Ví dụ: ECB's Deposit Facility, Fed's Interest on Excess Reserves).
2. **Công cụ định hình biên trên (Upper bound)**: Cơ sở cho vay cứu cạn ngân hàng. Lãi suất này ép trần mức rủi ro (Ví dụ: ECB's Marginal Lending Facility, Fed's Discount Window).
3. **Cơ chế thanh khoản chủ lưu trung tâm**: Buộc hệ thống phải nợ NHTW một cách cấu trúc (thông qua [[Reserve_Ratio]]) bằng các phiên auction cung tiền truyền thống (Open market operations). Nó giữ lãi suất bình quân chạy vòng giữa hành lang. [extracted] [[Fixed Income - Alexander During-7.pdf#page=8-9]]

## Rủi ro kẹt thị trường (Stigma)

Việc ngân hàng "chạm trần" (đi gõ cửa vay Discount Window) đem lại **Sự kỳ thị (Stigmatisation)**. Các ngân hàng lo sợ nếu tiếp cận nó, thị trường sẽ đồn thổi họ đang mất thanh khoản vì bị các ngân hàng ngang hàng đuổi cửa. Đó là lý do hệ thống này đảm bảo giới tư bản tìm cách vay mượn/chuyển khoản giúp đỡ nhau hơn là gặp trung ương. [extracted] [[Fixed Income - Alexander During-7.pdf#page=9]]

## Phân biệt với

- **[[Asymmetric_Lending_Corridor]]**: Sau khủng hoảng thanh khoản 2008 do bơm tiền thả cửa, hệ thống đối xứng bị giáng cập vì tiền quá nhiều.

## Nguồn

- [[Fixed Income - Alexander During-7.pdf#page=8-9]] — Mechanics, Lower/Upper bounds, Reserve deficit
