# Fed Duration Extraction → Term Premium: Cơ chế và Hàm ý H1 2026

**MODE DEEP | 2026-06-29**

**Thesis:** Các chương trình QE của Fed (2008–2021) đã hút duration risk ra khỏi thị trường tư nhân ở quy mô lớn, nén ACM 10Y term premium xuống khoảng -100bp ở đỉnh. Với QT kết thúc 01/12/2025 và RMP giữ bảng cân đối phẳng, hiệu ứng "stock" bị đóng băng tại mức hiện tại — nhưng phát hành trái phiếu Kho bạc H1 2026 đạt $683B ($+249B so với cùng kỳ) đang cộng thêm cung duration vào thị trường tư nhân mỗi tuần mà không có Fed bù đắp. Kết quả cấu trúc là quá trình đảo ngược từ từ của kênh truyền dẫn chủ đạo trong QE: term premium nới rộng dần khi hiệu ứng kìm nén nhân tạo thoái lui.

## Top-Down Entry

Đường cong lãi suất Mỹ H1 2026 đứng ở giao điểm của hai lực cấu trúc song hành. Ở đầu ngắn, sàn cứng của hệ thống thanh toán (~$3T dự trữ, Andreopoulos 11/04/2026) [WEB-2026-04-11] xác định mức tối thiểu bảng cân đối Fed; nhịp bất đối xứng RMP/TGA tạo biến động dự trữ gần hạn. Ở đầu dài, một lực ít được chú ý hơn nhưng có trọng lượng tương đương đang vận hành: quá trình đảo ngược của một thực nghiệm kéo dài một thập kỷ, trong đó Fed đã hút rủi ro kỳ hạn (duration risk) của thị trường trái phiếu về bảng cân đối của mình ở quy mô hàng nghìn tỷ đô la.

Duration risk — độ nhạy giá trị danh mục trái phiếu với biến động lãi suất — là sản phẩm cốt lõi mà nhà đầu tư trái phiếu được trả để gánh chịu. Khi Fed hút sản phẩm đó ở quy mô lớn qua nhiều chương trình tổng cộng trên $4.5T UST và ~$1.8T MBS, khoản bù đắp yêu cầu — term premium — giảm và chạm vùng âm. Sự đảo ngược của quá trình hút đó, đang diễn ra trong H1 2026 qua cơ chế "stock đóng băng + cung tư nhân tích lũy", là cơ chế mà phân tích này kiểm tra.

Khung phân tích: đây không phải chủ yếu là phân tích chính sách tiền tệ — đây là phân tích cung-cầu về việc ai đang nắm giữ rủi ro lãi suất trên thị trường trái phiếu, và ở mức giá nào.

---

## Macro Layer

Chế độ chính sách H1 2026 là Ample Reserves Regime A (Armenter): Fed neo lãi suất qua sàn IORB, dự trữ dồi dào, không có QE. Cơ chế kiểm soát lãi suất và cơ chế hút duration hiện đã tách rời. IORB kiểm soát SOFR/EFFR; term premium được xác định bởi cung-cầu duration trên thị trường tư nhân.

Khung đo lường là mô hình ACM (Adrian, Crump, Moench), do NY Fed công bố hàng ngày [RAW-BOOK: During_Fixed_Income_Ch21.md]. ACM phân tách lợi suất 10Y quan sát được thành hai thành phần không quan sát trực tiếp: (1) kỳ vọng lộ trình lãi suất ngắn hạn trong 10 năm tới; (2) term premium — phần bù còn lại cho việc chịu đựng bất định duration. Kỳ vọng phản ánh kỳ vọng chính sách tiền tệ (hiện tại: ~4.0-4.5% hành lang). Term premium phản ánh cung-cầu duration risk và khẩu vị rủi ro của thị trường.

Lịch sử chế độ theo ước tính ACM [LLM-E]:
- 2010: term premium 10Y ~+150bp
- 2013 (sau QE3): ~+50bp, bị nén nhờ stock effect
- 2020–2021 (đỉnh QE): ~-100bp, âm khi Fed chiếm ưu thế tuyệt đối trên thị trường duration
- H1 2026: phục hồi dần về +30 đến +60bp khi cung tư nhân tích lũy không có Fed bù đắp

Sự thay đổi chế độ vĩ mô: Fed chuyển từ người mua ròng (QE, +$120B/tháng ở đỉnh) → người bán ròng thụ động (QT, -$95B/tháng) → trung lập (RMP, bảng cân đối phẳng từ 10/12/2025). Mỗi chuyển đổi chế độ có tác động duration khác nhau: QE nén term premium; QT nới rộng; bảng cân đối phẳng đóng băng hiệu ứng stock trong khi cung tư nhân tích lũy.

## Plumbing Layer

Kênh cung (supply channel) vận hành qua một phép tính danh mục đơn giản nhưng mạnh. Khi Fed mua một trái phiếu 10 năm, Fed hút $100 DV01 (dollar value of one basis point) ra khỏi tay khu vực tư nhân và ghi có dự trữ vào tài khoản ngân hàng của người bán. Người bán giờ nắm giữ không còn rủi ro duration và $100 dự trữ qua đêm. Tổng tồn kho duration của khu vực tư nhân giảm xuống. Đồng thuận học thuật (Gagnon et al. 2011; Krishnamurthy-Vissing-Jorgensen 2011, 2013; D'Amico-King 2013) [LLM-ref] ước tính tác động nén này ở mức xấp xỉ 91–100 basis points giảm trong lợi suất 10Y trên mỗi $1T hút duration ròng — kênh truyền dẫn đơn lẻ lớn nhất của QE, vượt cả kênh tín hiệu và kênh tái cân bằng danh mục về quy mô. Cơ chế không cần truyền dẫn qua spread tín dụng, không cần kênh cho vay ngân hàng, không cần dịch chuyển kỳ vọng lạm phát: đây là định giá khan hiếm duration thuần túy.

Lớp preferred habitat khuếch đại phép tính số học đó. Nhà đầu tư tổ chức — công ty bảo hiểm nhân thọ quản lý các khoản nợ phải trả có sàn lợi suất bảo đảm, quỹ hưu trí theo quy định phải khớp duration với nợ phải trả, quỹ tài sản quốc gia với ủy quyền dài hạn — không thể thay thế trái phiếu 30 năm bằng T-bill 2 năm [RAW-BOOK: During_Fixed_Income_Ch21.md]. Nhu cầu của họ có tính cấu trúc và không thể phân tán qua các kỳ hạn. Khi Fed hút duration 10–30 năm ở quy mô lớn, những nhà đầu tư theo preferred habitat này cạnh tranh cho lượng còn lại trong thị trường, chấp nhận lợi suất thấp hơn so với mức thuần túy bù đắp rủi ro. ACM term premium chạm vùng âm chính là kết quả này: cầu preferred habitat vượt cung sau khi trừ đi phần Fed đang hút, ngụ ý nhà đầu tư trả phí bảo hiểm (thay vì nhận) để nắm giữ trái phiếu dài hạn.

Phân biệt "flow effect" và "stock effect" của D'Amico-King (2013) [LLM-ref] là yếu tố then chốt để đọc H1 2026. Flow effect là tạm thời — nó chỉ tồn tại khi Fed đang mua chủ động (thị trường tạm thời loãng xung quanh các đợt mua). Stock effect kéo dài miễn là Fed giữ duration ra khỏi thị trường. Tại 24/06/2026, Fed nắm giữ $4,487.9B UST [RAW-OFFICIAL: H.4.1 24/06/2026] với WAM ước tính ~7–8 năm [LLM-E], tương đương khoảng 31–36 nghìn tỷ dollar-year duration bị giữ ngoài thị trường tư nhân [LLM-E]. Stock effect đóng băng ở mức này — Fed không hút thêm (QT đã kết thúc) cũng không mở rộng để hấp thụ phát hành mới (RMP là trung lập: bù MBS chạy off bằng mua UST tương đương). Nhưng mẫu số đang tăng: vay mượn gộp Kho bạc H1 2026 đạt $683B (+$249B YoY) [RAW-OFFICIAL: Treasury Q2 2026 Refunding] cộng thêm duration vào tay tư nhân mỗi tuần phát hành mà không có Fed hấp thụ. Tỷ lệ duration Fed nắm giữ / tổng thị trường đang giảm theo cơ học, và theo đó, phần bù kìm nén nhân tạo cũng dần thoái lui.

## Treasury Layer

Với người thực hành quản lý duration trong H1 2026, sự đảo ngược term premium có ba hàm ý vận hành riêng biệt theo từng chân trời thời gian.

Ở chân trời gần, rủi ro là đọc nhầm mức lợi suất thành bằng chứng của thành phần lợi suất. Lợi suất 10Y ở 4.5% với term premium +50bp và kỳ vọng đường đi +4.0% là một trạng thái vị thế rất khác với 4.5% với term premium -20bp (kỷ nguyên QE) và kỳ vọng đường đi +4.7% (mong đợi cắt giảm mạnh). Cả hai cùng mang lại P&L giống nhau trên mỗi đơn vị DV01, nhưng một trạng thái có hỗ trợ cấu trúc từ kỳ vọng chính sách trong khi trạng thái kia sẽ mean-revert khi kỳ vọng cắt giảm lãi suất điều chỉnh. Đầu ra mô hình ACM từ NY Fed cung cấp phân tách hàng ngày — theo dõi thành phần term premium độc lập với kỳ vọng lãi suất là thông tin nhiều hơn so với chỉ xem 10Y yield tuyệt đối trong các quyết định vị thế duration.

Ở chân trời trung hạn, kịch bản "New Accord" của Warsh-Cochrane (tháng 02/2026) [WEB-2026-02-17] là rủi ro đuôi cho term premium. Theo kịch bản RMP chỉ mua T-bill, Fed sẽ ngừng mua notes/bonds, để notes/bonds chạy off khi đáo hạn. WAM hiện tại của danh mục UST của Fed ~7–8 năm [LLM-E]. Chính sách bills-only duy trì trong 5–7 năm sẽ trả lại toàn bộ stock duration 10–30 năm cho thị trường tư nhân mà không có bù đắp — đảo ngược cấu trúc hoàn toàn hiệu ứng hút duration thời QE. Term premium sẽ hội tụ về mức cơ sở lịch sử tiền-QE (~+150–200bp so với kỳ vọng lãi suất ngắn hạn) [LLM-E].

- **Thiếu dữ liệu — ACM daily H1 2026**: NY Fed công bố ACM 10Y term premium ở tần suất ngày; phân tích này dùng ước tính [LLM-E]; cần ingest chuỗi thời gian NY Fed ACM H1 2026 để xác nhận mức hiện tại và làm cơ sở cho quan điểm giao dịch term premium cụ thể
- **Bộ khuếch đại convexity**: Khi danh mục MBS của Fed chạy off, hoạt động phòng hộ convexity của Fed (mua trái phiếu dài khi lãi suất tăng để duy trì duration-neutral) giảm đi — bộ khuếch đại phụ cho biến động term premium trong các kịch bản lãi suất tăng
- **Kênh P&L mismatch**: Deferred asset của Fed [LLM-E: đỉnh ~$200B, 2023–2024] từ việc trả IORB > thu nhập coupon phản ánh số học tài khóa của duration extraction — Kho bạc tiết kiệm được chi phí vay dài hạn trong thời QE trong khi Fed hấp thụ chi phí khi lãi suất tăng; deferred asset là dấu vết bảng cân đối của chuyển giao này, hiện đang dần thoái lui khi các trái phiếu kỷ nguyên QE đáo hạn

---

## Timing Layer

**Quá khứ — Duration bị hút, term premium bị nén (2008–2021):** QE1 qua QE∞ hút ~$4.5T UST duration cộng ~$1.8T MBS duration ra khỏi thị trường tư nhân [LLM-E]. Hiệu ứng stock đỉnh vào 2020–2021: ACM 10Y term premium chạm -100bp [LLM-E], có nghĩa nhà đầu tư chấp nhận bù đắp âm cho việc nắm giữ duration 10 năm thay vì lăn vị thế qua đêm. Điều này là hệ quả trực tiếp của thị phần Fed trên thị trường duration: ở đỉnh, Fed nắm giữ khoảng 25% tổng Kho bạc đang lưu hành. Các nhà đầu tư preferred habitat cạnh tranh cho 75% còn lại, tạo ra cầu dư thừa cấu trúc cho sản phẩm duration.

**Hiện tại — Stock đóng băng, cung tư nhân tích lũy (H1 2026):** Stock effect đóng băng ở $4,487.9B UST [RAW-OFFICIAL: H.4.1 24/06/2026]. QT (giữa 2022 đến 01/12/2025) đã phần nào trả duration về thị trường; RMP từ 10/12/2025 là trung lập (MBS chạy off → mua UST tương đương, tổng không đổi, thành phần thay đổi). Sự nới rộng cấu trúc được dẫn dắt bởi khoảng cách: phát hành gộp Kho bạc H1 $683B thêm cung tư nhân, nhưng danh mục Fed không mở rộng để hấp thụ. Sự phục hồi term premium [LLM-E: ~+30–60bp đến H1 2026] vẫn còn xa dưới mức cơ sở lịch sử tiền-QE, cho thấy hiệu ứng stock (Fed giữ $4.5T) vẫn cung cấp kìm nén đáng kể — nhưng ít hơn mỗi quý khi tỷ lệ cung tư nhân tăng lên.

**Tương lai — Ba đường phân kỳ:** Đường A (cơ sở): Fed duy trì bảng cân đối phẳng hiện tại, Kho bạc tiếp tục phát hành khối lượng lớn theo trần nợ $41.1T (One Big Beautiful Bill Act). Term premium nới rộng từ từ: quỹ đạo 12–24 tháng hướng về +80–120bp [LLM-E]. Đường B (Warsh bills-only): RMP chỉ mua T-bill được ban hành; notes/bonds chạy off mà không có thay thế trả duration về thị trường theo lịch WAM; đảo ngược toàn bộ hiệu ứng stock trong ~7 năm; term premium hội tụ về +150–200bp [LLM-E]; lợi suất 10Y tăng về cấu trúc độc lập với lộ trình lãi suất chính sách. Đường C (QE mới): Nếu suy thoái kích hoạt mua tài sản mới, duration lại bị hút → term premium lại bị nén → đường A/B bị hoãn lại; nhưng điều này tạo ra vấn đề P&L mismatch tiếp theo với kỳ hạn kéo dài hơn.

## Feedback và Ranh giới

Hai vòng phản hồi đang vận hành. Vòng thứ nhất là phản hồi convexity preferred habitat: term premium tăng → giá trái phiếu dài giảm → lỗ mark-to-market cho quỹ hưu trí và công ty bảo hiểm có ủy quyền duration dài → buộc bán (các ngưỡng LCR/solvency theo quy định) → giá tiếp tục giảm và term premium tiếp tục nới rộng. Đây là analog phía duration của động học tự-thỏa mãn về thiếu hụt dự trữ trong hệ thống thanh toán. Vòng thứ hai là phản hồi tài khóa: term premium tăng → chi phí tái cấp vốn của Kho bạc tăng → thâm hụt mở rộng trên lãi suất ròng (hiện đã ~$900B/năm) [LLM-E] → áp lực chính trị lên Fed để nối lại QE hoặc YCC → bất định chế độ → thêm phí rủi ro term premium.

Ranh giới phân tích này là kênh cung. Kênh kỳ vọng (forward guidance về lãi suất Fed tương lai) vận hành độc lập và có thể chiếm ưu thế trong ngắn hạn. Một Fed pivot đáng tin cậy hướng tới nới lỏng có thể nén kỳ vọng lãi suất ngắn hạn nhanh hơn tốc độ tích lũy cung, giữ tổng lợi suất 10Y ổn định ngay cả khi term premium nới rộng và kỳ vọng đường đi giảm xuống. Phân tách ACM là cần thiết để tách biệt hai lực này và tránh gán nhầm sự nới rộng do cung cho kỳ vọng.

---

## Diagram

```
FED DURATION EXTRACTION & TERM PREMIUM — STOCK EFFECT (H1 2026)
══════════════════════════════════════════════════════════════════

KỶ NGUYÊN QE (2008–2021)
─────────────────────────────────────────────
  Fed mua UST/MBS ($4.5T+ ròng)
           │
           ▼
  Tồn kho duration tư nhân ↓
           │
           ▼
  Preferred habitat cầu > cung ở 10–30Y
           │
           ▼
  ACM term premium 10Y → -100bp [LLM-E]
  (nhà đầu tư trả để nắm duration)


H1 2026 — STOCK ĐÓNG BĂNG, CUNG TƯ NHÂN TÍCH LŨY
─────────────────────────────────────────────────────
  Fed giữ $4,487.9B UST (phẳng)           Kho bạc phát hành $683B H1
  [RAW-OFFICIAL: H.4.1 24/06/2026]        [RAW-OFFICIAL: Treasury Q2 2026]
           │                                        │
  RMP: MBS runoff → UST mua                        ▼
  (trung lập, không hút duration mới)     Cung duration tư nhân ↑ mỗi tuần
           │                                        │
           └────────────────────┬───────────────────┘
                                ▼
                  Tỷ lệ Fed/tổng thị trường duration ↓
                                │
                                ▼
                  ACM term premium ↑ dần (+30 → +60 → +100bp+)


KỊCH BẢN ĐUÔI WARSH BILLS-ONLY
─────────────────────────────────────────────────────
  RMP chỉ mua T-bill → Notes/bonds chạy off không thay thế
  WAM ~7–8 năm → Đảo ngược hoàn toàn stock trong ~7 năm
  Term premium → +150–200bp (mức lịch sử tiền-QE) [LLM-E]
  Lợi suất 10Y tăng CẤU TRÚC bất kể lộ trình lãi suất chính sách


BỘ KHUẾCH ĐẠI
─────────────────────────────────────────────────────
  [+] Giới hạn sức chứa preferred habitat (quỹ hưu trí / bảo hiểm)
  [+] Cầu phòng hộ convexity MBS giảm khi danh mục MBS Fed chạy off
  [+] ON RRP = $2.3B → căng thẳng đầu ngắn cộng hưởng với rủi ro đầu dài
  [−] Forward guidance (nếu Fed pivot sang nới lỏng → kỳ vọng đường đi giảm)
  [−] Cầu ngoại tệ dự trữ cho UST (chức năng safe-haven của USD)
```

---

## Kết luận

**Mức tin cậy: TIER C** — cơ chế được xác lập tốt trong tài liệu học thuật [LLM-ref]; mức term premium H1 2026 là ước tính [LLM-E]; chuỗi thời gian ACM hàng ngày, ước tính thực nghiệm KVJ, và phân tích kỳ hạn chi tiết danh mục UST của Fed chưa có trong nguồn gốc thô của wiki.

Cơ chế duration extraction là kênh truyền dẫn đầu dài của QE không có đối ứng trong chính sách tiền tệ thông thường. Sự đảo ngược của nó — đang diễn ra trong H1 2026 qua stock Fed đóng băng đối mặt với cung Kho bạc đang tăng — là một quá trình cấu trúc vận hành trong nhiều năm, không phải nhiều tháng. Đối với người thực hành Treasury desk, hàm ý thực tế là bất đối xứng: giai đoạn kìm nén mất một thập kỷ và nhiều chương trình để thiết lập; sự đảo ngược đang xảy ra một cách thụ động, không cần hành động của Fed, thuần túy qua phép tính của cung tư nhân tích lũy đối mặt với danh mục Fed cố định. Kịch bản Warsh thúc đẩy quá trình này từ thụ động sang chủ động, nhưng chiều hướng là như nhau trong cả hai trường hợp.

Liên kết với phân tích hệ thống thanh toán: cả căng thẳng dự trữ đầu ngắn (SOFR-IORB) và nới rộng term premium đầu dài đều là biểu hiện tài khóa-tài chính của cùng một sự chuyển dịch cấu trúc cơ bản — Kho bạc Mỹ đang vay mượn khối lượng lớn, và thị trường tư nhân đang hấp thụ nhiều hơn cả rủi ro thanh khoản (đầu ngắn) lẫn rủi ro duration (đầu dài) so với bất kỳ thời điểm nào kể từ 2008.

## Next Steps

1. **Ingest raw source** — NY Fed ACM 10Y term premium daily H1 2026 (newyorkfed.org/research/data_indicators/term_premia); xác nhận ước tính [LLM-E] và hình thành quan điểm giao dịch dựa trên dữ liệu
2. **Ingest raw source** — Krishnamurthy-Vissing-Jorgensen (2011, 2013); Gagnon et al. (2011); D'Amico-King (2013); định lượng hệ số kênh cung cho wiki
3. **Tạo node** — `03_wiki/mechanisms/Fed_Duration_Extraction_Term_Premium.md` — đưa nghiên cứu này vào định dạng wiki node
4. **Cập nhật cross-link** — `03_wiki/mechanisms/ACM_Curve_Decomposition.md` → thêm tham chiếu đến duration extraction là driver chính của hành vi term premium H1 2026
5. **Liên kết với phân tích sàn thanh toán** — `2026-06-29_fed-balance-sheet-synthesis.md` → cross-reference: căng thẳng dự trữ đầu ngắn và đảo ngược duration đầu dài là biểu hiện đồng thời của cùng một chuyển dịch chế độ tài khóa-tài chính

---

*Note thuộc publish layer. Node wiki tổng hợp: `03_wiki/mechanisms/Fed_Duration_Extraction_Term_Premium.md` (pending creation). Phân tích bổ sung bảng cân đối Fed: xem `2026-06-29_fed-balance-sheet-synthesis.md`.*
