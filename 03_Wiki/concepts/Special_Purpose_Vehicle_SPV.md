---
type: definition
aliases: [SPV, Special Purpose Vehicle, ABS, Asset-Backed Securities, Tách vỏ tài sản]
trigger: "Ngân hàng ôm một đống khoản vay muốn đẩy đi nhưng không muốn chịu trách nhiệm chung nợ nần"
output: "Lập một con rùa ma (SPV) trên giấy tờ, bốc tài sản ném vào rùa, rồi cho rùa phát hành trái phiếu (ABS)"
constraints: ["SPV thường đóng quân ở các thiên đường thuế miễn nhiễm phá sản (Bankruptcy remote)"]
sources: ["Fixed Income - Alexander During-17.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 16
---

# Special Purpose Vehicle SPV

## Vỏ Bọc Ma Thuật Của ABS

Sẽ có lúc, việc phát hành trái phiếu từ chính Bản Thể Tập đoàn (Corporate Entity) gặp khó khăn do xếp hạng tín dụng yếu hoặc Rủi ro phá sản của mảng kinh doanh cốt lõi quá cao. Lúc này, công nghệ Kỹ thuật tài chính sinh ra thủ thuật phân rã: Lập một pháp nhân siêu chân không gọi là **SPV (Special-Purpose Vehicle / Entity)**. [extracted] [[Fixed Income - Alexander During-17.pdf#page=8]]

### Cơ chế hoạt động
SPV thường là một công ty rỗng ruột nằm ở các thiên đường thuế. Nhiệm vụ duy nhất của SPV là:
1. Mua lại dứt điểm Độc quyền thụ hưởng Dòng tiền (Cashflow) từ một tài sản cụ thể của Ngân hàng mẹ (ví dụ: bọc nợ thẻ tín dụng, cho vay mua xe...).
2. Lấy chính Cụm dải sản vừa mua đó làm bệ phóng, Phát hành Trái phiếu bán cho nhà đầu tư gọi là **Chứng Khoán Đầu Tư Có Tài Sản Đảm Bảo (ABS - Asset-Backed Securities)**.

Việc này biến SPV trở thành Cỗ máy nhai nợ (Phái sinh cấu trúc). Cái dở của nhà đầu tư là nếu SPV có tàng trữ rác xà bần trong tài sản, khi ABS vỡ nợ, nhà đầu tư KHÔNG THỂ quắp lại công ty mẹ để đòi bồi thường, do đặc tính Phân ly phá sản (Bankruptcy remoteness). [extracted] [[Fixed Income - Alexander During-17.pdf#page=8]]

## Nguồn

- [[Fixed Income - Alexander During-17.pdf#page=7-8]] — Giới thiệu tổng quan Issuer Types: Corporate, Banks, SPVs và khái niệm ABS sơ khai.
