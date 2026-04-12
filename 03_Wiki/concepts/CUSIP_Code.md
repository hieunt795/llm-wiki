---
type: definition
aliases: [CUSIP]
sources: ["Fixed Income - Alexander During-11.pdf"]
confidence: medium
provenance: extracted
created: 2026-04-13
chapter: 10
---

# CUSIP Code

## Định nghĩa

**CUSIP** là mã định danh chứng khoán nội địa Mỹ dài đúng **9 Ký tự** (Thường bế nguyên xi chuỗi này để nhét thẳng vào lõi 9 chữ của mã [[ISIN_Code]] quốc tế). CUSIP đứng tên cho tên tổ chức tạo ra nó: Committee on Uniform Security Identification Procedures. [extracted] [[Fixed Income - Alexander During-11.pdf#page=5-7]]

## Cấu trúc CUSIP

1. **[6 Ký tự đầu] Issuer Code:** Ký hiệu công ty/tổ chức lôi tờ giấy ra. 3 ô đầu tiên mặc định phải là số, 3 ô sau tùy hỉ alphanumeric. Các chính quyền khủng như Nhà nước Mỹ (US Fed) được bao trọn nhiều dải dải issuer id (ví dụ bills xài 912796, bonds xài 912810). [extracted] [[Fixed Income - Alexander During-11.pdf#page=7]]
2. **[2 Ký tự tiếp] Issue Code:** Chỉ định cho một lô phát hành cục bộ. Đối với Cổ phiếu (Equity) thì 2 ô này thuần số (numeric). Đối với công cụ Thu nhập cố định (Debt securities), 2 ô này bắt buộc chứa ít nhất 1 Chữ cái. **Mẹo lọc nhiễu:** Họ loại bỏ tắp các vần O, I và số 0, 1 để tránh nhìn nhầm mẹ Cổ phiếu tưởng Trái phiếu. Nhờ luật cứng này, liếc CUSIP phát biết ngay đâu là Equity đâu là FI. [extracted] [[Fixed Income - Alexander During-11.pdf#page=7]]
3. **[1 Ký cuối] Check Code:** Check sum Modulus 10, cách chia biến đổi ngầm hơi đo hơi khác biệt lươn lẹo so với của ISIN. [extracted] [[Fixed Income - Alexander During-11.pdf#page=7-8]]

## Nguồn

- [[Fixed Income - Alexander During-11.pdf#page=7-8]] — US Ticker systems, cấu trúc nhận diện nợ vs cổ phiếu thông qua quy tắc lọc 2 ký tự Issue code.
