---
type: definition
aliases: [FRN, Variable-rate note, Trái phiếu lãi suất thả nổi, Lãi suất FRN]
trigger: "Ngân hàng nhận tiền gửi tiết kiệm theo lãi suất thị trường, tiền gửi này rất 'dính' (sticky) nhưng chi phí phải trả cứ trồi sụt theo Rate. Ngân hàng đem tiền đó đi mua gì để an toàn?"
output: "Mua FRN (Trái phiếu có Coupon thả nổi) để cân bằng bảng cân đối kế toán"
constraints: ["FRN không giải quyết được rủi ro tín dụng (Credit spread), nó chỉ giải quyết rủi ro Lãi suất nền"]
sources: ["Fixed Income - Alexander During-18.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 17
---

# Floating Rate Notes FRN

## Cuộc Gọi Đầu Tư Hoàn Hảo Của Ngân Hàng Thương Mại

Cấu trúc định giá cốt lõi của một viên đạn Bullet Bond (Trái phiếu lãi cố định) là:
$$f(something) = const$$

Nhưng trong đại dương Lãi suất thả nổi (Floating-Rate Notes - FRNs), hàm số Coupon biến thiên điệu nghệ theo một biến số Chỉ số gốc (Reference Index) — Cứ đến đầu mỗi kỳ trả lãi, Coupon sẽ bị gán lại (Reset) bằng Chỉ số mới. [extracted] [[Fixed Income - Alexander During-18.pdf#page=1]]

Tại sao công cụ lắt léo này lại tồn tại? Vì nó là "Liều thuốc chữa lành" cho Bảng Cân Đối Kế Toán của các Ngân hàng bán lẻ (Retail banks). 
Ngân hàng bán lẻ cạnh tranh huy động **Tiền gửi (Deposits)**. Bản chất của khoản nợ Nguồn vốn (Liability) này cực kỳ "dính" (Sticky - khách hàng rất lười chuyển bank khác), nhưng chi phí lãi suất (Deposit interest rate) thì lại chạy loạn xạ bám sát mức Lãi suất liên ngân hàng ngắn hạn.

Nếu Ngân hàng huy động Lãi thả nổi, nhưng vác tiền đi mua Trái phiếu Cố định dài hạn (Bullet bonds), khi Lãi suất trung ương tăng, Ngân hàng gãy mảng biên lợi nhuận. Do đó, FRN ra đời làm **Tài sản đối ứng (Asset side)**, thứ có khả năng tự động tăng/giảm lãi sinh lời song hành nhịp đập với chi phí huy động của Bank. [extracted] [[Fixed Income - Alexander During-18.pdf#page=1-2]]

## Nguồn

- [[Fixed Income - Alexander During-18.pdf#page=1-2]] — Khái niệm cơ bản, tập hàm số f(something), và tại sao ngân hàng (Deposit-taking institutions) lại thèm khát FRN do bản chất "sticky deposits".
