---
type: mechanism
aliases: [Turn, Phần bù qua năm, Cú nảy quy chế]
trigger: "Lãi suất 3 tháng vay qua đêm bất ngờ nhảy dựng đứng từ 2% lên 6% chỉ trong vài ngày cuối tháng 3 hoặc tháng 12"
output: "Do các nhà băng ngoan cố thu hẹp bảng cân đối ngay trước mặt regulator để giấu rủi ro, gây khát thanh khoản cục bộ"
constraints: ["Không có ý nghĩa dự báo chính sách, phải lọc bỏ noise này ra khỏi đường cong trước khi phân tích"]
sources: ["Fixed Income - Alexander During-16.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 15
---

# Turn Premium

## Lời nói dối chân thật cuối năm

**Turn Premium** (Phần bù qua năm/qua ranh giới Báo cáo) là một dị tật lãi suất mang tính thời vụ tàn khốc nhất trên thị trường tiền tệ (Money Market), hoàn toàn bị chi phối bởi quy chế Kế toán và Giám sát. [extracted] [[Fixed Income - Alexander During-16.pdf#page=3-4]]

### Cơ chế vắt chanh bỏ vỏ
Các Ngân hàng có toàn quyền vung tay thao túng bảng cân đối hàng ngày, nhưng họ sẽ phải nộp **"Ảnh chụp sổ" (Snapshot)** cho cơ quan quản lý (Regulator) vào các ngày chốt sổ (ví dụ: ngày 31 tháng 12, hoặc ngày 1 tháng 4 tại Nhật Bản). Động thái này gọi là "The Turn".

Gần đến ngày The Turn, các ngân hàng nảy sinh động cơ sinh tồn mãnh liệt: **Thu hẹp (shrink) bảng cân đối kế toán** và vứt bỏ những tài sản có trọng số rủi ro cao để khiến mình trông ngoan ngoãn, an toàn trên giấy tờ báo cáo. Họ trở nên cực kì nín nhịn trong việc mở rộng tín dụng Liên ngân hàng nếu khoản vay đó vắt ngang qua mốc Giao Thừa. [extracted] [[Fixed Income - Alexander During-16.pdf#page=4]]

### Hậu quả hệ thống
- Những giao dịch vay mượn 3 tháng (3M deposit) kí vào cuối tháng 9 sẽ đáo hạn vào cuối tháng 12 → Vẫn OK.
- Nhưng giao dịch 3 tháng kí vào rạng sáng tháng 10 sẽ đáo hạn vắt qua tháng 1 của năm sau → **Bắt đầu gánh The Turn**. Lãi suất chào bán liền dựng đứng (có thể nhảy vài percent). Lực ép Repo đặc biệt ác liệt vì áp lực của tỷ lệ đòn bẩy (Leverage Ratio regulation). [extracted] [[Fixed Income - Alexander During-16.pdf#page=4]]

Chỉ những biến cố khổng lồ (bơm tiền xoa dịu Y2K, chuyển đổi Eurocash 2001) mới khiến Turn Premium giãn ra. Đối với một dân Quant, Turn Premium là rác (*Noise*), và tuyệt đối phải được nhận diện và Gọt Sạch khỏi đồ thị khi làm nội suy đường cong lãi suất (Curve fitting) vì nó chẳng phản ánh tí triển vọng chính sách vĩ mô nào cả. [extracted] [[Fixed Income - Alexander During-16.pdf#page=4]]

## Nguồn

- [[Fixed Income - Alexander During-16.pdf#page=3-4]] — Tác động bóp méo bảng cân đối kì báo cáo và sự dựng đứng của lãi suất vay vắt ngang qua turn.
