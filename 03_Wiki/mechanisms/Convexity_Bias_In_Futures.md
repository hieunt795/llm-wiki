---
type: mechanism
aliases: [Bất cân xứng Ký quỹ, Convexity chênh lệch futures]
trigger: "So sánh một khoản tiền gửi thẳng (Deposit) và việc giữ một Futures contract gánh Variation Margin"
output: "Giá trị kỳ vọng của Future bị bẻ cong lệch pha, sinh ra cước phạt Convexity Adjustment"
constraints: ["Nợ và Mức lãi mới gồng tỷ giá bục túi do phải Vay tiền mỗi tối để nộp"]
sources: ["Fixed Income - Alexander During-14.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 13
---

# Convexity Bias In Futures

## Điểm mù của Phái Sinh ký quỹ hằng ngày

Xét về toán học ngây thơ (đạo hàm bậc 2 bằng không), [[Money_Market_Futures]] theo nguyên lý chẳng có một mẩu Độ lồi (Convexity) nào. Khác hẳn món tiền gửi/trái phiếu thường mang Convexity siêu việt dương tính (do cái mẫu số chia chiết khấu cong như vỏ sò). [extracted] [[Fixed Income - Alexander During-14.pdf#page=14]]

Vậy nhưng, đời đéo như mơ. Khi bạn đánh Future trên sàn ném vỡ [[Variation_Margin_Vs_Initial_Margin|Ký quỹ VM mỗ tối]], con thủy quái Kế toán ngoi lên: [extracted] [[Fixed Income - Alexander During-14.pdf#page=14]]
1. Lãi suất thị trường tăng mẹ lên => Vị thế Hợp đồng Long của bạn Lỗ máu rơi.
2. Sở giao dịch gào lên bắt bạn **Nạp thêm Variation Margin (Tiền tươi!)**
3. Trong bóng đêm hoảng loạn, bạn phải đi cắm sổ đỏ *Vay Nóng* mớ tiền mặt đó đập cho sàn húp, khốn nạn thay bạn sặc nước phải mượn đắp đúng cái lúc "Lãi Vay đang nhảy lên đỉnh nóc nhọn". [extracted] [[Fixed Income - Alexander During-14.pdf#page=14]]
4. Cuối chu kỳ lật ngược lại: Nếu Lãi rớt cắm mỏ, Sàn trả tiền cho bạn đi. Nhưng đi nhặt tiền đó múc đi gửi ngân hàng thì gặm đúng cái Lãi Suất héo hon rớt mồng tơi!

### Gánh thuế lồi: The Adjustment
Vòng luẩn quẩn của cỗ máy hạch toán ép rên rỉ người mua. Không một tay gác trọ chép số đề Futures nảo ngớ ngẩn mà cược một cái Lãi Sát nút với kỳ vọng cả. Anh ta nhét một cái nệm phao bảo hiểm (Convexity bias) để bóp ngạt đối thủ:
$$
\Delta r = - \frac{1}{2}\sigma^2t^2
$$
Với $\sigma$ là dao động volatility. Thâm thủng này tăng siêu cấp theo hệ bình phương thời gian kéo màng $t^2$, lý giải vì sao chơi Futures Eurodollar càng dài càng phải tróc nã trừ gồng lỗ chiết khấu chênh lệch! [extracted] [[Fixed Income - Alexander During-14.pdf#page=14-15]]

## Nguồn

- [[Fixed Income - Alexander During-14.pdf#page=14-15]] — Hiện tượng tống tiền Variation Margin bẻ cong cái tương lai phẳng lặng của Option, vẽ ra công thức Bias chấn động.
