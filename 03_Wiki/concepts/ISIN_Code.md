---
type: definition
aliases: [ISIN]
sources: ["Fixed Income - Alexander During-11.pdf"]
confidence: medium
provenance: extracted
created: 2026-04-13
chapter: 10
---

# ISIN Code

## Định nghĩa mã ISIN

**International Securities Identification Numbers (ISINs)** là hệ thống định danh chứng khoán 12 ký tự (chữ hoặc số) chuẩn hóa toàn cầu theo khung ISO 6166:2013. [extracted] [[Fixed Income - Alexander During-11.pdf#page=5]]

*Chú ý:* Không phải chứng khoán nào cũng có ISIN (chỉ khi issuer chịu trả tiền cống nạp tạo mã), và cẩn thận, không phải ISIN nào cũng là chứng khoán (nó được dùng để gác cho cả Future Contracts hay Rổ chỉ số index iBoxx). [extracted] [[Fixed Income - Alexander During-11.pdf#page=6]] Giới trader cần tỉnh táo khi soi dòng đời ISIN thông qua nghiệp vụ gộp xác [[Bond_Tap_Funging]].

## Cấu trúc 3 hộp của ISIN (12 Ký tự)

1. **[2 Ký tự đầu] Country code:** Mã quốc gia 2 chữ cái (US, JP, DE). *Bí thuật:* Mã quốc gia này là nơi của cái kho [[Book_Entry_Securities_System|CSD]] chứa tờ giấy, chứ đéo phải nơi đóng đô của công ty phát hành! Ví dụ Eurobonds thì dùng mã "XS". [extracted] [[Fixed Income - Alexander During-11.pdf#page=6]]
2. **[9 Ký tự tiếp theo] National identifier:** Hốt nguyên xi cái mã nội địa của quốc gia đó rồi nhét thêm số 0 ở đầu cho đủ 9 ô. Ví dụ Đức xài WKN 6 số -> thêm 3 ngòi nổ "000" ở trước. Hoặc Mỹ xài [[CUSIP_Code]] 9 số thì ném ốp vào vừa khít. (Tuy nhiên lũ Nhật bản chơi trội lại sáng tạo một bộ luật biến hóa khác không lấy nguyên xi từ meigara code). [extracted] [[Fixed Income - Alexander During-11.pdf#page=6]]
3. **[1 Ký số cuối] Check Digit:** Dùng thủ thuật Double-Add modulus 10 phức tạp. Bất kỳ sự hoán đổi nghịch vị trí gõ chữ nào sai tay cũng sẽ vỡ Check Digit, phần mềm báo lỗi lòi le ngăn cản Settlement fail. [extracted] [[Fixed Income - Alexander During-11.pdf#page=6-7]]

## Nguồn

- [[Fixed Income - Alexander During-11.pdf#page=5-7]] — Cấu trúc ISIN, modulus 10 calculation, country of CSD origin.
