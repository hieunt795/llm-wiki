---
type: mechanism
trigger: "Hệ thống RTGS cần xử lý thanh toán bất đồng bộ trong ngày"
output: "Trung ương cung cấp tín dụng ngắn hạn trong ngày cho các ngân hàng"
constraints: ["Bị giới hạn với các monetary policy counterparties", "Không đóng chu kỳ âm cuối ngày"]
sources: ["Fixed Income - Alexander During-5.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 4
---

# Intraday Overdraft

## Cơ chế

Một số hệ thống thanh toán (như TARGET2 của ECB) cung cấp **intraday credit / overdraft** (thấu chi trong ngày) cho ngân hàng tham gia. Về nguyên tắc, chỉ cho phép chuyển khoản trên số dư dương, nhưng NHTW cho phép tài khoản bị âm trong ngày giao dịch. [extracted] [[Fixed Income - Alexander During-5.pdf#page=7]]

### Mục đích

Để làm hệ thống **vững chắc (robust) trước thứ tự thanh toán (reordering of transactions)**.
Giả sử A bắt đầu với số dư 100.
1. Nhận 50.
2. Cần trả 200.
3. Nhận 100.
Nếu việc trả 200 xảy ra tại bước (2), tài khoản A âm (-50) tạm thời → Overdraft giúp trơn tru quá trình. Nếu **không có overdraft**, A sẽ bị kẹt thanh toán và có động cơ **trì hoãn (delay)** chuyển tiền cho người khác đến khi tiền về tài khoản, gây tắc nghẽn toàn hệ thống. [extracted] [[Fixed Income - Alexander During-5.pdf#page=7-8]]

## Điều kiện và Rủi ro

- **Rủi ro tín dụng cuối ngày**: Ngân hàng có thể vỡ nợ khi kết thúc ngày với số dư âm. Do vậy, quyền truy cập trực tiếp thường bị giới hạn ở **monetary policy counterparties** (các đối tác chính sách tiền tệ) vì họ có quyền truy cập vào các cơ sở cấp quỹ qua đêm của NHTW. [extracted] [[Fixed Income - Alexander During-5.pdf#page=8]]
- **FedWire vs TARGET2**: FedWire (Mỹ) không thường có overdraft, buộc ngân hàng giữ cash dồi dào, phù hợp với thao tác thị trường mở (OMO) mục tiêu tỷ giá qua đêm của Fed. TARGET2 (Eurozone) cung cấp thấu chi, phù hợp cấu trúc Repo hằng tuần cũ của châu Âu. [extracted] [[Fixed Income - Alexander During-5.pdf#page=9]]

## Ví dụ số

Xem Table 4.2 trong sách (Tác động của thứ tự thanh toán lên nhu cầu tiền mặt). [extracted] [[Fixed Income - Alexander During-5.pdf#page=8]]

## Nguồn

- [[Fixed Income - Alexander During-5.pdf#page=7]] — Định nghĩa intraday credit
- [[Fixed Income - Alexander During-5.pdf#page=8]] — Ví dụ về reordering of transactions
- [[Fixed Income - Alexander During-5.pdf#page=9]] — So sánh FedWire và TARGET2
