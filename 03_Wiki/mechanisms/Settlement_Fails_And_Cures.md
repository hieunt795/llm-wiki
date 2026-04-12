---
type: mechanism
aliases: [Thất tín giao nhận, Buy-ins, Partial fail]
trigger: "Tới ngày Settlement (T+2) nhưng người bán vẫn đéo lo được đủ đống trái phiếu để giao cho người mua"
output: "Giao dịch bĩ hoãn, sinh ra chuỗi cho vay miễn phí (0% repo), nếu không thì phạt Fails charges"
constraints: ["Không bao giờ bị ghép tội vỡ nợ (Default) mà chỉ chịu phạt tài chính vì thiếu hàng là quá phổ thông"]
sources: ["Fixed Income - Alexander During-12.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 11
---

# Settlement Fails And Cures

## Hiện tượng Thất tín giao nhận (Fails)

**Fails** xảy ra khi bên Bán không moi ra được chứng khoán để giao cho bên Mua vào ngày thanh toán. Trong ngành Fixed income, hiếm khi chém đầu tuyên bố Mặc định (Default) cho một vụ Fail vì đa phần nguyên nhân là do Kế toán lóng ngóng (tắc đường ở bộ phận mượn Repo) chứ không phải do hết tiền. [extracted] [[Fixed Income - Alexander During-12.pdf#page=11]]

### Sự tinh tướng của hình phạt (0% Repo Logic)
Truyền thống xử phạt Fails cực kỳ tao nhã: Cấu trúc kinh tế của cái lệnh Mua đó bị Đông cứng! Người Bán vẫn không giao hàng, và dĩ nhiên người Mua sẽ giữ lại cục tiền thảnh thơi. **Nhưng, người Bán vừa đánh rơi hoàn toàn lãi suất tiền mặt lẽ ra họ nhặt được nếu lấy tiền từ hôm qua.** Lỗ hổng này ngang bằng với việc Người bán cung cấp một lệnh Vay Repo (lấy chứng khoán thế chấp) ở mức Lãi suất 0% cho người Mua trong thời gian khất nợ.
*Nhưng khi lãi suất chạm 0 âm (ZLB) hoặc trái phiếu quá cực cực hãn (Trade xả special cực hạn), âm với âm bù trừ khiến ngón đòn răn đe này vứt sọt rác!* Buộc khu vực phải sinh ra đòn phạt tiền tươi **Fails charges** đay nghiến (Mỹ ấn định 3% fee kể từ 05/2009). [extracted] [[Fixed Income - Alexander During-12.pdf#page=11]]

## Các phác đồ chữa bệnh (Cures)

1. **Fails mitigation lending:** Các kho lưu ký CSD tự xòe danh mục cứu bồ, cho bên Bán mượn tạm hàng với cái giá cắt cổ để vá lỗ thủng. [extracted] [[Fixed Income - Alexander During-12.pdf#page=11]]
2. **Bilateral O/N và T/N repos:** Người Bán hốt hoảng đi vay Overnight hoặc Tomorrow-Next để rước phiếu về đáp đúng hạn T+2. [extracted] [[Fixed Income - Alexander During-12.pdf#page=12]]
3. **Buy-ins:** Người Mua giận dỗi gọi thẳng ra sàn mua đại giá market, rồi bắt Người bán (thất hứa) cắn răng bồi thường hóa đơn thiệt hại. Khổ cái nhiều khi đồ độc lạ quá (special), thằng Mua và thằng Bán cùng chạy lên sàn giằng xé giành nhau tìm 1 lô duy nhất (buy-in agent đụng đầu original seller), đẩy giá vỡ nát. [extracted] [[Fixed Income - Alexander During-12.pdf#page=12]] (Từ CSDR 2021, EU biến Buy-in thành lệnh bắt buộc bất chấp bị phản đối).

## Nguồn

- [[Fixed Income - Alexander During-12.pdf#page=11-12]] — Logic răn đe 0% repo của Fails, các đòn trừng phạt Fails charges và danh mục Cures trị bệnh.
