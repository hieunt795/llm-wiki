---
title: Fed Duration Extraction and Term Premium
aliases:
- Duration Extraction
- Supply Channel QE
- Term Premium Suppression
- QE Duration Channel
type: mechanism
tags:
- monetary-policy
- QE
- term-premium
- yield-curve
- federal-reserve
status: verified
confidence: 3
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Krishnamurthy-Vissing-Jorgensen | Gagnon | D'Amico-King"
provenance: "Multi-source (LLM-ref: KVJ 2011/2013, Gagnon 2011, D'Amico-King 2013; RAW-OFFICIAL: H.4.1 24/06/2026)"
thesis: Khi Fed mua notes/bonds quy mô lớn, Fed hút duration risk ra khỏi thị trường
  tư nhân (supply channel), nén ACM term premium xuống khoảng -100bp ở đỉnh QE.
  Với stock đóng băng H1 2026 và cung Kho bạc tích lũy, term premium đang đảo ngược
  cấu trúc mà không cần hành động Fed.
source_refs:
- file: During_Fixed_Income_Ch21.md
  page: 212
created: '2026-06-29'
updated: '2026-07-03'
---

## Thesis

Cơ chế duration extraction là kênh truyền dẫn đầu dài của QE: Fed mua notes/bonds → hút duration risk ra khỏi bảng cân đối tư nhân → cung duration khan hiếm → nhà đầu tư chấp nhận mức bù đắp thấp hơn để nắm duration còn lại → ACM term premium bị nén. Hiệu ứng kéo dài miễn là Fed giữ danh mục (stock effect), không chỉ trong thời gian mua chủ động (flow effect). [LLM-ref: D'Amico-King 2013]

## Mechanism

### 1. Supply Channel — Portfolio Arithmetic

Khi Fed mua một trái phiếu 10 năm:
- Fed hút DV01 tương ứng ra khỏi tay khu vực tư nhân
- Người bán nhận dự trữ (zero duration, no rate risk)
- Tổng tồn kho duration tư nhân giảm xuống
- Với cung giảm và cầu ổn định (preferred habitat) → cạnh tranh giá → term premium giảm

Ước tính học thuật [LLM-ref]: ~91–100bp giảm trong lợi suất 10Y trên mỗi $1T hút duration ròng (Gagnon et al. 2011; Krishnamurthy-Vissing-Jorgensen 2011, 2013).

### 2. Preferred Habitat Amplification

Nhà đầu tư tổ chức (bảo hiểm nhân thọ, quỹ hưu trí theo quy định) có cầu bắt buộc cho các kỳ hạn cụ thể và không thể thay thế bằng kỳ hạn khác [RAW-BOOK: During_Fixed_Income_Ch21.md]. Khi Fed hút 10–30Y duration, các nhà đầu tư preferred habitat cạnh tranh cho lượng còn lại → khuếch đại nén term premium vượt mức tính theo cung đơn thuần. [[Preferred_Habitat_Market_Distortions]]

### 3. Stock vs Flow Effect

**Flow effect** — tạm thời, chỉ khi Fed đang mua chủ động (thị trường tạm thời mỏng xung quanh các đợt mua).

**Stock effect** — kéo dài miễn là Fed giữ duration ra khỏi thị trường tư nhân. Khi Fed nắm giữ $4,487.9B UST với WAM ~7–8 năm [LLM-E], tương đương ~31–36 nghìn tỷ dollar-year duration bị giữ ngoài tay tư nhân [LLM-E].

### 4. Đo lường — Mô hình ACM

NY Fed công bố ACM (Adrian-Crump-Moench) term premium 10Y hàng ngày: phân tách lợi suất 10Y = kỳ vọng đường đi + term premium. [[ACM_Curve_Decomposition]]

Lịch sử [LLM-E]:
- 2010: ~+150bp (tiền-QE bình thường)
- 2020–2021 đỉnh QE: ~-100bp (âm, cầu vượt cung)
- H1 2026: ~+30 đến +60bp (phục hồi cấu trúc từ từ)

## H1 2026 — Hiện Trạng và Hàm Ý

Fed giữ $4,487.9B UST [RAW-OFFICIAL: H.4.1 24/06/2026], bảng cân đối phẳng từ 10/12/2025 (RMP trung lập: MBS runoff → mua UST tương đương). Stock effect đóng băng. Nhưng Kho bạc vay gộp $683B H1 2026 (+$249B YoY) [RAW-OFFICIAL: Treasury Q2 2026 Refunding] cộng cung tư nhân mỗi tuần.

Kết quả: tỷ lệ Fed-held duration / tổng thị trường giảm cơ học → term premium nới rộng từ từ mà không cần hành động Fed.

## Kịch Bản Warsh Bills-Only

Nếu RMP chuyển sang chỉ mua T-bill: notes/bonds chạy off theo WAM ~7–8 năm mà không có thay thế → đảo ngược toàn bộ stock effect trong ~7 năm → term premium hội tụ về +150–200bp (mức tiền-QE) [LLM-E] → lợi suất 10Y tăng cấu trúc độc lập với lộ trình lãi suất chính sách. [[QE_Transmission_Channels]]

## Ranh Giới Phân Tích

Kênh cung là độc lập với kênh kỳ vọng (forward guidance). Nếu Fed pivot sang nới lỏng, kỳ vọng đường đi giảm có thể bù đắp term premium nới rộng, giữ tổng 10Y yield ổn định. Phân tách ACM là cần thiết để tách biệt hai lực này.

## Cập Nhật 2026-07-03 — Driver Đã Xác Định Cho Kỳ Vọng Đường Đi

Nghiên cứu yield curve trước đó (xem `06_publish/2026-06-29_us-treasury-balance-sheet-yield-curve-h1-2026.md`) đã ghi nhận bear-flattening H1 2026 (2s10s thu hẹp +72bp→+31-35bp, front-end dẫn dắt) và ACM term premium tăng, nhưng chưa xác định rõ nguyên nhân kỳ vọng đường đi thay đổi. [RAW-OFFICIAL: FOMC minutes 2026-01/03/04, SEP 2026-06-17] Fed đã bỏ tín hiệu cắt lãi suất trước đó, chuyển sang ngôn ngữ "deliver price stability" sau 5 năm trên mục tiêu 2%, và phát tín hiệu khả năng tăng lãi suất — được kích hoạt bởi cú sốc năng lượng Trung Đông (Hormuz, headline CPI 4.2%/PCE 4.1% YoY) và bằng chứng broadening ở cấp độ producer (PPI core +0.8% MoM, Stage-1/Stage-4 gap nới rộng). Xem [[US_CPI_PPI_PCE_H1_2026]] và [[PPI_Stage_Differential_IO_Cascade_Diagnostic]] — kênh kỳ vọng (hawkish pivot) và kênh cung (duration extraction đảo ngược) đang cùng chiều trong H1 2026, khuếch đại thay vì bù trừ lẫn nhau.

## Evidence / Source Anchors

- ACM model và phân tách lợi suất: [[ACM_Curve_Decomposition]] [RAW-BOOK: During_Fixed_Income_Ch21.md]
- Preferred habitat khuếch đại supply channel: [[Preferred_Habitat_Market_Distortions]] [RAW-BOOK: During_Fixed_Income_Ch21.md]
- QE transmission channels — channel (D) relative pricing, (E) portfolio effect: [[QE_Transmission_Channels]]
- Term premium là "price of surrendered options": [[Term_Risk_Premium_Mechanics]]
- Supply channel estimates ~91–100bp/$1T: [LLM-ref: Gagnon et al. 2011; KVJ 2011, 2013; D'Amico-King 2013] — raw source ingest pending
- Fed UST holdings $4,487.9B: [RAW-OFFICIAL: H.4.1 24/06/2026]
- Treasury gross H1 2026 $683B: [RAW-OFFICIAL: Treasury Q2 2026 Refunding]
- Research note đầy đủ: `06_publish/2026-06-29_fed-duration-extraction-term-premium.md`

## Related

- [[ACM_Curve_Decomposition]] — Khung đo lường term premium hàng ngày
- [[Term_Risk_Premium_Mechanics]] — Định nghĩa cơ bản
- [[Preferred_Habitat_Market_Distortions]] — Bộ khuếch đại phía cầu
- [[QE_Transmission_Channels]] — 8 kênh truyền dẫn QE, trong đó supply channel = channel (D)
- [[Unconventional_Monetary_Policy_Taxonomy]] — Vị trí QE trong bức tranh UMP
- [[Quantitative_Tightening_Mechanism]] — QT đảo ngược supply channel: trả duration về thị trường
- [[Fed_Deferred_Asset_2022_2026]] — P&L mismatch: chi phí tài khóa của duration extraction
- [[US_CPI_PPI_PCE_H1_2026]] — Dữ liệu lạm phát xác định driver cho hawkish pivot H1 2026
- [[PPI_Stage_Differential_IO_Cascade_Diagnostic]] — Chỉ báo broadening ở cấp độ producer, tiền đề cho kỳ vọng lãi suất
