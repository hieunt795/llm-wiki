---
type: mechanism
aliases: [GC, Special Repo, Đặc biệt, Specific Market]
trigger: "Sự phân hóa giữa mục tiêu đi Vay Tiền hay đi Mượn Giấy hái ra tiền"
output: "Gãy đôi tỷ giá Repo giữa hàng đại trà (GC rate) và hàng nực mùi quý hiếm (Specials rate)"
constraints: ["Rates của Specials luôn luôn Sâu hơn (thấp hơn) GC Rate"]
sources: ["Fixed Income - Alexander During-15.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 14
---

# General Collateral Vs Special

## Hệ Cấp Bậc Repo

Một giao dịch [[Repurchase_Agreement]] trên thị trường bị nứt làm hai thế giới định mức, phụ thuộc vào mục đích của lòng tham: [extracted] [[Fixed Income - Alexander During-15.pdf#page=1-2]]

### 1. General Collateral (Hàng chợ GC)
- **Mục tiêu:** Kẻ đi Repo chỉ muốn có Chỗ **Giữ Tiền An Toàn**, không quan tâm rác mảng gì miễn là của một quốc gia uy tín. Tiêu chí ví dụ: "Bất cứ Trái phiếu Đức, Pháp, Hà Lan xịn nào đáo hạn 1-10 năm đem qua đây lấy tiền".
- **Lãi suất (GC Rate):** Sát rạt với rủi ro phi tín dụng, nhưng vẫn nhạt hơn một chút so với Rate đi vay mượn Unsecured liên ngân hàng. Ai cầm tiền có quyền phán xét đống mớ hỗn lộn. [extracted] [[Fixed Income - Alexander During-15.pdf#page=1]]

### 2. Specials Market (Hàng hiếm Đặc thù)
- **Mục tiêu:** Khi một mã Chứng khoán bị tơi bời nhu cầu Bán khống hoặc cần gom hàng để giao nộp cho Sàn (Futures Exchange), mã đó trở nên Quý hiếm. Kẻ đi Repo bằng mọi giá **Chỉ Muốn Tờ Giấy Đó**, đéo nhận giấy khác.
- **Lãi suất (Specials Rate):** Vô cùng tàn bạo. Kẻ có "Hàng Hiếm" sẽ nói: *"Mày muốn mượn tờ giấy này của tao? Ok đưa tiền đây tao giữ hộ, nhưng tao đéo trả mày đồng lãi GC bào đâu, tao trả cho mày lãi cực Thấp"*. 
- **Công thức nhói lòng:** Một tài sản bị gọi là "20 bp special" có nghĩa là Lãi Mượn Cash của nó đang **Rớt thấp hơn tận 20 Basis points** so với mặt bằng GC. Khi "Hàng" (Special) bùng lên đỉnh nóc ngáo giá thì việc ngâm hàng [[Settlement_Fails_And_Cures|Fail giao nhận]] có khi còn ngon hơn! [extracted] [[Fixed Income - Alexander During-15.pdf#page=2-3]]

Sự chênh lệch GC vs Special đẻ ra một nhánh thị trường **Interdealer market**, nơi các siêu môi giới đi buôn lậu tờ giấy quý hiếm ẩn trong một đống GC mục nát ra ăn chênh lệch.

## Nguồn

- [[Fixed Income - Alexander During-15.pdf#page=1-3]] — Bản cấu hình GC lấy tiền làm gốc, Specials lấy Giấy làm gốc, và ngón đòn ăn chênh lệch Lãi suất thấp của phe Găm hàng.
