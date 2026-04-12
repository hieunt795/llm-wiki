---
type: mechanism
trigger: "Trung ương muốn in tiền mua ngoại tệ neo tỷ giá mà không muốn gây lạm phát nội địa"
output: "Phát hành giấy tờ nợ ngắn hạn nội địa để cân bằng lượng tiền cơ sở"
constraints: ["Có thể làm sụt giảm yield ở quốc gia sở hữu ngoại tệ (ví dụ Fed) do spillover"]
sources: ["Fixed Income - Alexander During-8.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 7
---

# FX Sterilisation

## Cơ chế

Khi [[Central_Bank]] tham gia thị trường ngoại hối (FX Market) để đè giá bản tệ, họ phải in tiền mặt (base money) để mua ngoại tệ từ thị trường. Lượng tiền vừa in này tạo dòng dư cung khổng lồ, đi ngược lại với các target kiểm soát lạm phát (điển hình như [[Monetary_Policy_Targeting]]). [extracted] [[Fixed Income - Alexander During-8.pdf#page=3]]

Để hóa giải mâu thuẫn này, nhà điều hành thực hiện **Tiệt trùng ngoại hối (Sterilisation of FX interventions)**.
Họ thực hiện [[Liquidity_Operations]] ở vế Absorption (Hút thanh khoản), hoán đổi tài sản có độ thanh khoản cao (Tiền) thành một tài sản thanh khoản kém hơn nhiều ở trong tay khu vực tư nhân. [extracted] [[Fixed Income - Alexander During-8.pdf#page=3]]

### Ví dụ Nhật Bản (BoJ & MoF)
Bộ Tài chính Nhật (MoF) quản lý ngoại hối (không phải BoJ). Khi MoF gom đồng ngoài nước, họ tạo ra lượng Cung Yên khổng lồ. Để tiệt trùng lượng Yên này, MoF phát hành *Foreign Exchange Fund Financing Bills* ra ngoài thị trường. Tư bản lấy yên đắp vào mua cái Bill này, vớt gọn lượng Yên thặng dư vừa đẻ ra ở nghiệp vụ FX đi biến mất. Bản chất là **neutralise** sự bành trướng của Base Money. [extracted] [[Fixed Income - Alexander During-8.pdf#page=3-4]]

## Spillover rủi ro

Vì FX là 2 ngả tiền tệ, nếu ECB (châu Âu) in Euro để mua USD và tiệt trùng lượng Euro ngay tại nhà thành công, số lượng USD đang lọt thỏm sẽ làm cạn cung đồng USD, tác động vòng ngược lại thanh khoản của Fed Mỹ. [extracted] [[Fixed Income - Alexander During-8.pdf#page=4]]
Trường hợp Nhật với thặng dư tài khoản vãng lai bự (nhiều USD tràn vào), họ gặp khủng hoảng dư dật nguồn cấp Yên/USD chéo, đè bẹp hệ số lãi suất ngắn hạn chính phủ Nhật đến **mức âm (negative yield)** ngay cả trước khi BoJ chính thức cắt lãi suất dính sàn âm! [extracted] [[Fixed Income - Alexander During-8.pdf#page=4]]

## Nguồn

- [[Fixed Income - Alexander During-8.pdf#page=3]] — Cơ chế hút máu ngược thanh khoản (Sterilisation)
- [[Fixed Income - Alexander During-8.pdf#page=4]] — Ví dụ spillover của MoF Nhật, BoJ Negative yield
