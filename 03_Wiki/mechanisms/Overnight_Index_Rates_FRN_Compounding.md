---
type: mechanism
aliases: [OIS FRN, SOFR compound FRN, Không ghép lãi margin, P(t) Intermediate Rate]
trigger: "Trái phiếu FRN đào thải LIBOR để đu bám SOFR/OIS. Nếu mỗi đêm cộng Lãi Overnight rồi Compound tịnh tiến, tính Accrued Interest kiểu quái gì?"
output: "Đẻ ra cái biến Rate mồi $\rho(t)$ bằng Hàm Compounded qua các điểm bù trừ, nhưng bứng nguyên xi cái Quoted Margin ($\mu$) KHÔNG TÍNH LÃI KÉP!"
constraints: ["Bắt buộc phải xài Độ lag móp méo Lookback kịch kim lên tới 5 Ngày thay vì 2 Ngày"]
sources: ["Fixed Income - Alexander During-18.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 17
---

# Overnight Index Rates FRN Compounding

## Gọng Kích Bóp Bụng Dân Kế Toán

Sau cuộc Đại thanh trừng [[OIS_And_Benchmark_Reform]], LIBOR chết bất đắc kỳ tử. Dân phát hành Trái phiếu FRN bị buộc phải lùa dòng thác Coupon bám theo Lãi suất qua đêm (Overnight Rates như SOFR, ESTR).

Nhưng Cơn ác mộng Toán học trỗi dậy: Nếu lãi vay cộng dồn từng đêm một, Tổng nợ cuối hẻm chỉ Lộ Sáng vỡ lẽ tại Điểm Đo Đoán Rút Thanh Toán (End of Coupon Period). Vậy trong 3 tháng đó, dân cày bán xới Bond trên Secondary Market giao dịch bốc hơi... Chả thằng nào biết Accrued Interest (Lãi Cộng dồn kẹt ở giữa) là bao nhiêu tiền mà tính giá! [extracted] [[Fixed Income - Alexander During-18.pdf#page=4]]

Vấn đề thứ 2, Lưới Ghép Lãi Kép cắn nát cái Quoted Margin $\mu$. Việc rưới Compound lên phần Margin cẩu thả làm rách nát chuẩn mực Tỷ Suất Sinh Lời so với kỷ nguyên Libor. [extracted] [[Fixed Income - Alexander During-18.pdf#page=4]]

### Phép Thánh Sáng Chế $\rho(t)$
Họ phẫu thuật cắt não công thức FRN OIS thành một Hợp chất phi nhân tính:
1. Đập Lãi Kép ĐÊM (Compounded Overnight $\prod_{t=t_0}^d [1 + R \times DCF] - 1$) dập lại thành Một Tỷ Tỷ giá Chốt Lõi Đại Diện Gọi là $\rho(t-1)$
2. Rút thẳng Margin $\mu$ ra CẮM KHÔNG GHÉP KÉP song song với nó! [extracted] [[Fixed Income - Alexander During-18.pdf#page=4]]
3. Bẻ cong Không/Thời Gian: Chuyển Lookblack Logarith Observation (Độ chễ quan sát) lùi hẳn ra khỏi mặt phản đồ $T-2$ truyền thống đập lạch bạch thành $5 Business Days$ dãn cách (Bóp nghẹt ở Châu Âu). Độ trễ kinh hồn này ép Lãi của Ngày Bốc Hơi phải nạp sẳn để Accrued Interest nở rộp phình lỳ lên biểu đồ y hệt cách làm của Trái phiếu trơn tuồn tuột! [extracted] [[Fixed Income - Alexander During-18.pdf#page=4]]

## Nguồn

- [[Fixed Income - Alexander During-18.pdf#page=4]] — Khắc phục khuyết điểm OIS so với kỳ hạn chốt sống (Term-rate), Lãi Lõi $\rho$ và độ lag 5 ngày dị biệt của Euro.
