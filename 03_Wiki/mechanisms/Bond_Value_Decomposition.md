---
type: mechanism
aliases: [Chia tách cấu trúc kỳ hạn, Block Coupon PV, Principal Present Value, Convexity Distribution]
trigger: "Trái phiếu 40 năm có rủi ro Duration lớn hơn 10 năm. Nhưng tại sao nếu rớt giá thì phần Gốc 40 năm chẳng có tí phản ứng Lồi (Convexity) nào?"
output: "Do chiết khấu về Mốc số 0 (Trục hoành Hiện tại) vắt kiệt Cục tiền tít tắp 40 năm thành con số 0 tròn trĩnh"
constraints: ["Nghịch lý: Cục Gốc 40 năm rớt giá cắm đầu vì PV suy thoái, chứ không phải vì siêu lồi Convexity dồn về"]
sources: ["Fixed Income - Alexander During-17.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 16
---

# Bond Value Decomposition

## Giải Phẫu Xác Chết Mười Năm Và Bốn Mươi Năm

Người ta luôn mường tượng Trái phiếu dài hạn (Long-duration) sẽ văng vỡ mọi radar nếu biến động. Nhưng tác giả Alexander During chứng minh: Nếu bạn Cắt phân lớp 1 tờ 10 Năm, 20 Năm, 30 Năm và 40 Năm ra trên bàn mổ (Giả định mua đồng giá Par 100 và 5% Yield), sẽ xuất hiện 1 nghịch lý điên rồ của Cỗ Máy Chiết Khấu (PV). [extracted] [[Fixed Income - Alexander During-17.pdf#page=29]]

### 1. Phép Đẳng Cấu Dòng Tiền Coupon (Block PV)
**Present Value của 10 năm Coupon đầu tiên LÀ BẰNG NHAU trên mọi thời hạn trái phiếu!**
- Tại sao? Đẳng thức chiết khấu vô tâm cực độ. 10 tờ Coupon trả lãi từ năm 1 đến năm 10 của 1 thằng Bond 40Y... có chung chính xác quỹ đạo dòng tiền và chung mẫu số chiết khấu 5% như 1 thằng đáo hạn 10Y. [extracted] [[Fixed Income - Alexander During-17.pdf#page=29]]
- Giới buôn tiền (Bond Trader) nhìn 1 tờ 20Y như sau: Nó là thằng 10Y đáo hạn, rồi đầu thai (Refinance) mua một cục 10Y mới ở năm thứ $t_{10}$.

### 2. Sự Suy Đồi Của Cục Gốc Lõi (Principal PV)
- $PV$ phân rã Rủi ro Bậc 1 (PVBP): Thời gian càng dài, Rủi ro Coupon CÀNG BÀNH TRƯỚNG, nhưng Rủi ro Gốc (Principal PVBP) lại CẮM ĐẦU ĐI XUỐNG! 
- Giá trị Hiện Tại Của Gốc Càng Lúc Càng Vô Dụng. Trả 100 Củ ở năm 40 quá xa xôi, đĩa cân chiết khấu ép PV của gốc mỏng dính $\approx$ Thấp. Nếu PV gốc thấp rớt thảm dưới mặt đất, thì độ nhạy dội lên $PVBP$ của nó cũng thu hẹp dần. [extracted] [[Fixed Income - Alexander During-17.pdf#page=30]]

### 3. Cò Quay Convexity Của Bức Tường Infinity
- **Nghịch lý tột đỉnh:** Trái phiếu Zero Coupon kỳ hạn VÔ HẠN (Infinite maturity zero-coupon) không rớt giá cũng chẳng tăng giá (PVBP = 0). Tại sao? Giá trị của nó bằng con số không! Đáy của hố đen Chiết Khấu làm Convexity của Cục Gốc 40 năm rụt ngòi (THẤP HƠN cả Cục Gốc 30 năm!). [extracted] [[Fixed Income - Alexander During-17.pdf#page=30]]
- Tức là nếu bạn cược siêu biến động vĩ mô (Play Long Volatility) mà rớ vào thằng gốc tít tận năm 40, thứ cứu bạn không phải siêu cấp Convexity ở cái lõi gốc, mà là Convexity nằm ở dải dãi rớt Coupon rải rác.

## Nguồn

- [[Fixed Income - Alexander During-17.pdf#page=29-31]] — Biểu đồ điên rồ trích xuất Breakdown của Present Value, PVBP, và Convexity Blocks (Cắt lát thập kỷ).
