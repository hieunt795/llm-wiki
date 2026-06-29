---
title: Fed Deferred Asset 2022–2026
aliases:
- Fed Deferred Asset
- Fed Operating Loss
- Central Bank P&L Mismatch
- Fed Remittance Suspension
type: evidence
tags:
- federal-reserve
- monetary-policy
- fiscal-monetary
- QE
- balance-sheet
status: verified
confidence: 3
half_life_years: 3
school: ''
superseded_by: null
superseded_date: null
expert_lens: "John H. Cochrane | Darrell Duffie"
provenance: "Cochrane (2026-02-17) RAW-CLIP; LLM-E for magnitudes"
thesis: "Khi Fed nâng lãi suất từ mid-2022, chi phí IORB trên reserves (~4–5% thả nổi)
  vượt thu nhập coupon từ danh mục QE-era (~2–3% cố định). Fed hạch toán khoản chênh
  lệch này là 'deferred asset' — lợi nhuận tương lai nợ lại cho chính mình trước khi
  có thể remit cho Kho bạc. Đây là dấu vết bảng cân đối của duration extraction: Fed
  hút rủi ro kỳ hạn của Treasury trong QE, và đang trả giá khi rates đảo chiều."
source_refs:
- file: "RAW-CLIP: Cochrane (2026-02-17)"
  page: 1
created: '2026-06-29'
updated: '2026-06-29'
---

## Thesis

Deferred asset của Fed không phải bất thường kế toán — đó là bằng chứng tài khóa của cơ chế duration extraction. Khi Fed mua $4.5T+ trái phiếu dài hạn trong QE, Fed thay thế nợ cố định dài hạn của Treasury bằng nợ floating overnight (reserves tại IORB). Trong môi trường lãi suất thấp (2009–2021), cơ cấu này có lợi: Fed thu coupon ~2–3% và trả IORB gần 0% → lợi nhuận lớn → remit cho Treasury. Khi rates tăng từ 2022, phương trình đảo ngược: Thu nhập coupon cố định < Chi phí IORB thả nổi → lỗ vận hành → deferred asset tích lũy.

## Timeline và Ước Tính

| Mốc | Sự kiện | Deferred Asset (ước tính) [LLM-E] |
|-----|---------|-----------------------------------|
| Q3 2022 | Fed bắt đầu thua lỗ vận hành khi IORB vượt coupon yield | $0 → tích lũy bắt đầu |
| Q4 2022 | $0 remittance to Treasury lần đầu tiên | ~$20–30B |
| 2023 | Tỷ lệ thua lỗ ~$100B/năm [LLM-E] | ~$100–150B |
| 2024 (đỉnh) | Tích lũy tối đa trước khi lãi suất bắt đầu giảm | ~$170–200B [LLM-E] |
| H1 2026 | Fed cắt lãi suất → IORB giảm; RMP thêm bonds mới với coupon cao hơn | Đang giảm dần; $0 remittance vẫn tiếp tục [LLM-E] |

**Lưu ý confidence**: Các con số trên là [LLM-E] ước tính — Fed công bố deferred asset trong H.4.1 footnotes và trong báo cáo tài chính hàng năm, nhưng chuỗi thời gian chính xác chưa được ingest vào wiki.

## Cơ Chế Kế Toán

Fed không giống corporation — không có cổ đông yêu cầu biện minh. Khi lỗ:

1. **Không ghi nhận vốn âm** — Fed giữ cấu trúc vốn danh nghĩa bình thường
2. **Tạo "deferred asset"** — tương đương "tài sản tương lai sẽ thu hồi từ lợi nhuận"
3. **$0 remittance** — cho đến khi deferred asset được thu hồi hoàn toàn bằng lợi nhuận tương lai, không có đồng nào được chuyển cho Treasury

Về mặt kinh tế, đây tương đương Treasury bị hoãn nhận khoản thu seigniorage thường niên (~$60–100B/năm trong thời bình thường). Đây là chi phí tài khóa vô hình của QE — không xuất hiện trong bảng ngân sách, nhưng là tiền thực mà Treasury không nhận được.

## Liên Hệ với Duration Extraction (Cochrane Framework)

Pillar I trong Cochrane-Warsh New Accord [RAW-CLIP: Cochrane 2026-02-17] giải thích chuỗi nhân quả:

```
Treasury phát hành bond 30 năm, coupon 2%
→ Fed mua (QE) → Fed nắm bond 30Y fixed
→ Fed phát hành reserves overnight floating (IORB)
→ Treasury "tiết kiệm" được: không cần rollover long-term debt trong 30 năm

NHƯNG khi rates tăng lên 5%:
→ Fed trả IORB 5% nhưng thu coupon 2%
→ Lỗ ~3%/năm trên stock QE
→ Deferred asset tích lũy
→ Treasury không nhận remittance

Kết quả ròng: Treasury đã "bán" rủi ro kỳ hạn cho Fed trong QE.
Fed đang gánh rủi ro đó khi rates đảo chiều.
```

Đây là lý do Cochrane lập luận Treasury nên kiểm soát maturity structure của chính mình: nếu Treasury muốn bảo hiểm lãi suất, Treasury nên trả thẳng cho thị trường (rollover risk), không để Fed làm proxy.

## Lộ Trình Thoát (Recovery Path)

Deferred asset giảm khi:

1. **IORB giảm** — Fed cắt lãi suất → chi phí thả nổi giảm (đang xảy ra H1 2026)
2. **RMP thêm bonds coupon cao hơn** — mỗi tháng RMP mua ~$40B UST mới với coupon thị trường (~4–5%), dần thay thế bonds QE-era coupon ~2%; thu nhập portfolio tăng dần
3. **QE-era bonds đáo hạn** — WAM ~7–8 năm [LLM-E]; bonds QE1 (2008–2010) đang đáo hạn nhanh nhất; mỗi bond đáo hạn xóa fixed-low-coupon exposure

Timeline ước tính [LLM-E]: Deferred asset có thể về 0 và remittance nối lại trong khoảng 2026–2028, tùy tốc độ cắt lãi suất và RMP composition.

## Hàm Ý Chính Sách

Nếu Warsh triển khai "bills-only RMP":
- RMP mua T-bills (coupon ~3.5–4.5% floating-ish) thay vì notes/bonds (coupon ~4–5% fixed)
- Net interest margin cải thiện (floating income vs floating expense → spread nhỏ hơn nhưng ổn định)
- Deferred asset thu hồi nhanh hơn
- Đổi lại: Fed dừng hút duration → term premium tăng cấu trúc (xem [[Fed_Duration_Extraction_Term_Premium]])

## Evidence / Source Anchors

- P&L mismatch mechanism (Cochrane Pillar I): [[Fed_Treasury_Accord_1951_And_Warsh_Proposal]] [RAW-CLIP: Cochrane 2026-02-17]
- Duration extraction → term premium connection: [[Fed_Duration_Extraction_Term_Premium]]
- QE transmission channels — bank capital formation, portfolio effect: [[QE_Transmission_Channels]]
- Helicopter money — profit remittance concept (bình thường): [[Helicopter_Money_Mechanism]]
- Fed balance sheet H1 2026 data: [RAW-OFFICIAL: H.4.1 24/06/2026]
- Magnitude ước tính: [LLM-E] — cần ingest Fed Annual Report 2022–2025 để xác nhận

## Related

- [[Fed_Treasury_Accord_1951_And_Warsh_Proposal]] — Cochrane framework: Treasury nên sở hữu maturity risk
- [[Fed_Duration_Extraction_Term_Premium]] — Duration extraction là nguyên nhân gốc của P&L mismatch
- [[Reserve_Management_Purchases_RMP]] — RMP đang dần đổi composition portfolio, tăng income
- [[Unconventional_Monetary_Policy_Taxonomy]] — QE là nguồn gốc của deferred asset
- [[TOMO_Reserve_Supply_Sterilization]] — Công cụ vận hành không liên quan đến P&L
