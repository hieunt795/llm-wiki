---
type: mechanism
aliases: [Lombard Lending, Repurchase Agreements]
trigger: "Ngân hàng cần mượn tiền NHTW mà không muốn bán đứt tài sản"
output: "Trung ương bơm tiền mặt qua giao dịch bán và mua lại kỳ hạn ấn định"
constraints: ["Yêu cầu tài sản thế chấp rủi ro thấp"]
sources: ["Fixed Income - Alexander During-8.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 7
---

# Repo Operations

## Cơ chế

Trong cơ chế cũ, thao tác này được gọi là **Lombard lending** (NHTW ban phát tiền vay dựa trên thế chấp giấy tờ có giá). Trong thị trường tài chính hiện đại, tương đương của chức năng này là một chu kỳ bán-rồi-mua-lại (Sale combined with simultaneous repurchase), được gọi đơn giản là **Repo trading**. [extracted] [[Fixed Income - Alexander During-8.pdf#page=2]]

Đây là phương pháp **cung cấp thanh khoản chuẩn** (standard normal provision) của ECB (Châu Âu) và Bank of Japan, trái ngược với hệ thống nghiêng về OMO của Fed. [extracted] [[Fixed Income - Alexander During-8.pdf#page=2]]

### Lợi ích

Việc sử dụng Repo cho [[Liquidity_Operations]] giúp **tách biệt (decouple)** kỳ hạn của tài sản thế chấp (maturity of securities) với kỳ hạn của thanh khoản bơm ra. NHTW có thể nhận collateral là trái phiếu chính phủ 10 năm nhưng chỉ bơm tiền cho Bank với kỳ hạn 1 tuần, với cam kết mua lại bằng giá đè trước. [extracted] [[Fixed Income - Alexander During-8.pdf#page=3]]

*Hạn chế*: Thị trường repo chỉ có độ thanh khoản tốt nhât trong bán kính tối đa là vài tháng tính từ điểm đáo hạn hợp đồng, không hữu dụng lắm để bơm vốn quá dài nếu cố định Repo terms. [extracted] [[Fixed Income - Alexander During-8.pdf#page=3]]

## Nguồn

- [[Fixed Income - Alexander During-8.pdf#page=2]] — Lombard lending vs Repurchase agreements, ECB/BoJ usage
- [[Fixed Income - Alexander During-8.pdf#page=3]] — Decoupling asset maturity with liquidity operation maturity
