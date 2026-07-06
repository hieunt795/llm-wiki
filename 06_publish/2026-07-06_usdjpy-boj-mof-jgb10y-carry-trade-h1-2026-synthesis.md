# USD/JPY, BOJ, MOF, JGB 10 Năm và Trạng Thái Carry Trade — Tổng Hợp H1 2026

*2026-07-06 | Claude (claude-sonnet-5) | Bản tổng hợp — gộp 7 node wiki liên quan (BOJ, MOF, JP10Y, carry trade) trong cluster nghiên cứu Nhật Bản H1 2026*

---

## Tóm tắt điều hành

Nửa đầu năm 2026, hệ thống chính sách Nhật Bản — BOJ, Bộ Tài chính (MOF), và thị trường JGB — vận hành dưới ba áp lực cùng lúc: đồng yên yếu kỷ lục 40 năm, lợi suất JGB 10 năm tăng nhanh vì lý do tài khóa độc lập với lãi suất chính sách, và một BOJ vừa tăng lãi suất vừa bị ràng buộc bởi chính bảng cân đối JGB khổng lồ của mình. Ba mảng dữ liệu — quyết định lãi suất BOJ, can thiệp FX của MOF, và lợi suất JGB 10 năm — không vận hành độc lập mà siết lẫn nhau: BOJ tăng lãi suất để bảo vệ đồng yên làm tăng chi phí trả nợ trên một ngân sách tài khóa 2026 kỷ lục, MOF can thiệp FX không thể thay thế cho một chênh lệch lãi suất Mỹ-Nhật hẹp hơn, và thị trường JGB đã bắt đầu định giá rủi ro tài khóa độc lập với cả hai kênh trên.

BOJ tăng lãi suất chính sách 25 điểm cơ bản lên 1,00% ngày 16/06/2026 — cao nhất từ 1995 — trong khi Thống đốc Ueda vắng mặt vì nhập viện, lần đầu tiên kể từ 1998 một cuộc họp chính sách thiếu thống đốc. Đợt tăng này không ổn định được đồng yên: USD/JPY chạm đáy 40 năm quanh 162,6-162,8 trong vòng hai tuần sau quyết định, và tính đến 06/07/2026 vẫn giao dịch quanh 161,8-162,0 — gần như không đổi so với đáy cuối tháng 6. MOF đã chi kỷ lục JPY 11.734,9 tỷ (~$73,35 tỷ) can thiệp FX trong giai đoạn 28/04-27/05/2026, nhưng đồng yên quay lại mức yếu hơn điểm khởi đầu chỉ sáu tuần sau. Từ đầu tháng 7, MOF chuyển chiến thuật từ cảnh báo bằng lời sang im lặng có chủ đích — từ chối nêu ngưỡng can thiệp cụ thể — nay được xác nhận ở cấp Bộ trưởng Tài chính Katayama, phối hợp trực tiếp với Bộ Tài chính Mỹ (Bessent).

Song song, lợi suất JGB 10 năm tăng từ khoảng 2,1% (tháng 3) lên 2,75-2,8% (đầu tháng 7) — gần mức cao nhất kể từ tháng 10/1996 — không chủ yếu do kỳ vọng lãi suất BOJ mà do một đợt đấu thầu 10 năm yếu và lo ngại về ngân sách FY2026 kỷ lục (~JPY 122,3 nghìn tỷ, tăng 6,3% so với năm trước, JPY 29,6 nghìn tỷ phát hành nợ mới) cùng kế hoạch đầu tư dài hạn JPY 370 nghìn tỷ đến 2040. Đây là một kênh rủi ro tài khóa tách biệt khỏi kênh lãi suất chính sách, và nó đặt BOJ vào thế khó: tăng lãi suất thêm để bảo vệ đồng yên đồng thời làm nặng thêm gánh nặng trả nợ trên chương trình phát hành đã mở rộng.

Về carry trade, dữ liệu chính thức đến 27/06/2026 hỗ trợ trạng thái "position compression" (giảm quy mô vị thế đầu cơ) hơn là một đợt "unwind" hoàn chỉnh (đảo chiều dòng vốn cơ bản): vị thế short-yên phi thương mại theo CFTC vẫn ở mức -146.104 hợp đồng tính đến 23/06, giảm nhẹ so với tuần trước nhưng vẫn lớn; bán ròng chứng khoán Nhật của nhà đầu tư nước ngoài trong tuần 21-27/06 (JPY 4,7363 nghìn tỷ) không đi kèm đồng yên tăng giá — dấu hiệu của portfolio de-risking hơn là đóng hedge short-yên trên diện rộng. Xác nhận ở cấp tháng: nhà đầu tư nước ngoài bán ròng JGB nhiều nhất trong ba năm trong tháng 6/2026, và trái phiếu siêu dài hạn ghi nhận dòng ra ròng đầu tiên kể từ 2024 (quanh 20/05/2026) — nhưng phần lớn dòng bán này có thể được giải thích bởi rủi ro tài khóa trên JGB dài hạn, không nhất thiết là một carry unwind cổ điển.

## 1. BOJ: Lộ Trình Tăng Lãi Suất và Ràng Buộc Tín Nhiệm

[RAW-OFFICIAL:BOJ June 2026 MPM] Cuộc họp chính sách 15-16/06/2026 tăng lãi suất chính sách 25 điểm cơ bản lên khoảng 1,00%, biểu quyết 7-1 (thành viên Asada Toichiro phản đối, cho rằng rủi ro giảm đối với sản xuất/việc làm từ tình hình Trung Đông lớn hơn rủi ro tăng đối với giá cả). Thống đốc Kazuo Ueda nhập viện từ 10/06 để điều trị nhiễm trùng nang gan — lần đầu tiên kể từ khi cơ chế quyết định chính sách hiện tại của BOJ bắt đầu năm 1998 mà thống đốc vắng mặt tại một cuộc họp đã lên lịch. Phó Thống đốc Ryozo Himino chủ trì phiên xét lãi suất; Phó Thống đốc Shinichi Uchida họp báo sau cuộc họp.

[RAW-OFFICIAL:BOJ June 2026 MPM] Lý do tăng lãi suất là truyền dẫn giá dầu từ cú sốc năng lượng Trung Đông, không phải xác nhận vòng xoáy lương-giá như điều kiện quyết định tháng 4 đặt ra. PPI tháng 5 tăng 6,3% YoY (vượt dự báo 5,5%, tốc độ nhanh nhất từ tháng 3/2023), chỉ số giá nhập khẩu tính bằng yên tăng 25,5% YoY cùng tháng.

[WIKI][LLM-S] Điểm vận hành quan trọng nhất: đợt tăng lãi suất không ổn định được đồng yên. USD/JPY giao dịch quanh 160,29 ngay sau công bố, sau đó tiếp tục xu hướng tăng, vượt 162 trong hai tuần, chạm 162,6-162,8 — đáy 40 năm. Nguyên nhân: chênh lệch lãi suất Mỹ-Nhật gần như không đổi một khi 25bp được ròng trừ với một Fed dưới tân Chủ tịch Warsh giữ 3,50-3,75% và mở đầu nhiệm kỳ với lập trường diều hâu thay vì tín hiệu cắt giảm — chênh lệch vẫn ở mức 250-275bp.

[RAW-OFFICIAL:BOJ JGB Purchase Plan][LLM-S] Một căng thẳng cấu trúc song song: BOJ giảm mua JGB khoảng JPY 200 tỷ/quý cho đến Q1/2027, sau đó duy trì mua khoảng JPY 2 nghìn tỷ/tháng từ tháng 4/2027 — tức tạm dừng tốc độ thu hẹp bảng cân đối, trong khi đồng thời tăng lãi suất chính sách. Một ngân hàng trung ương nắm giữ gần một nửa JGB đang lưu hành không thể rút hỗ trợ duration nhanh mà không rủi ro chính sự bất ổn lợi suất mà đợt tăng lãi suất trên danh nghĩa nhằm giúp ổn định tỷ giá.

## 2. MOF: Can Thiệp Kỷ Lục và Chuyển Sang Chiến Thuật Im Lặng

[RAW-OFFICIAL:MOF FEIO] Tổng chi can thiệp FX giai đoạn 28/04-27/05/2026 được xác nhận chính thức ở mức JPY 11.734,9 tỷ — lớn hơn ước tính ban đầu $34,5 tỷ và là đợt can thiệp lớn nhất từng ghi nhận. MOF báo cáo JPY 0 cho các giai đoạn tháng 1-3, 30/03-27/04, và 28/05-26/06/2026 — nghĩa là không có can thiệp bổ sung được xác nhận qua báo cáo hàng tháng cho đến cuối tháng 6.

[WIKI][LLM-S] Kết quả không khớp với kịch bản mà đợt can thiệp cần để thành công: nếu Fed cắt lãi suất ngày 15/05 như kịch bản A giả định, chênh lệch lãi suất sẽ nới rộng và carry trade mất hấp dẫn, ổn định đồng yên. Thực tế xảy ra là kịch bản B — Fed giữ nguyên/diều hâu — nên can thiệp cạn tác dụng trong sáu tuần, và USD/JPY kết thúc ở mức yếu hơn điểm khởi đầu trước can thiệp.

[WEB-2026-07-02][LLM-S] Từ đầu tháng 7, MOF chuyển chiến thuật: Phó Bộ trưởng Tài chính Mimura trong phỏng vấn ngày 02/07 từ chối bình luận về đồng yên, bỏ hẳn cụm từ "bold action" quen thuộc từng là tín hiệu tiền-can thiệp mà thị trường đã học cách định giá và fade. Việc rút bỏ tín hiệu — thay vì tiếp tục cảnh báo bằng lời — trở thành chính chiến thuật: khi không có cảnh báo cụ thể, thị trường không thể định giá một xác suất can thiệp hữu hạn trong một cửa sổ thời gian xác định, làm tăng chi phí rủi ro-đuôi không định giá được của việc giữ vị thế short-yên.

[WEB-2026-07-03:Bloomberg][WEB-2026-07-05:Eastern Herald] Chiến thuật này được nâng lên cấp Bộ trưởng Tài chính: Katayama lặp lại ngày 03/07 rằng chính quyền "sẵn sàng hành động bất cứ lúc nào cần thiết," kể cả trong các kỳ nghỉ lễ Mỹ khi thanh khoản mỏng, đồng thời xác nhận liên lạc trực tiếp với Bộ Tài chính Mỹ (Bessent) — được báo cáo từ 22/06. Phân tích ngày 05/07 khung việc Katayama nhất quán từ chối nêu ngưỡng can thiệp cụ thể là chính sách có chủ đích: một ngưỡng được xác nhận trở thành mức mà thị trường có thể kiểm định với hậu quả đã biết trước, trong khi một ngưỡng không được nêu giữ điểm kích hoạt khả dĩ như một biến số thị trường không thể định giá đầy đủ.

[WIKI][LLM-S] Chiến thuật này không thay đổi chênh lệch lãi suất cơ bản khiến đồng yên yếu — nó chỉ làm tăng phương sai và chi phí rủi ro-đuôi của việc giữ vị thế short-yên, có thể làm chậm tốc độ mất giá mà không đảo ngược hướng đi. Việc thị trường coi 162 là ngưỡng can thiệp mới (tăng từ vùng 155-160 tham chiếu trong đợt tháng 4-5) cho thấy quyết tâm hành động, không chỉ chiến thuật, đã bị định giá lại thấp hơn.

## 3. JGB 10 Năm: Tái Định Giá Rủi Ro Tài Khóa, Tách Biệt Khỏi Lãi Suất Chính Sách

[WEB-2026-07-02][WEB-2026-07-03] Lợi suất JGB 10 năm vượt 2,7% ngày 02/07/2026 — cao nhất trong ba tuần — và tiếp tục tăng lên 2,75% ngày 03/07, cao nhất từ tháng 5/2026. Nhìn trên cả nửa năm, lợi suất tăng từ khoảng 2,1% (tháng 3) lên mức tiệm cận 2,8% (đầu tháng 7), được mô tả trong một số phân tích thị trường là gần mức cao nhất kể từ tháng 10/1996.

[LLM-S] Biên độ tăng này (khoảng 60-70 điểm cơ bản trong một quý) lớn hơn nhiều so với những gì một đợt tăng lãi suất chính sách 25bp của BOJ có thể giải thích cơ học — cho thấy một thành phần phần bù kỳ hạn/rủi ro tài khóa nằm chồng lên kênh kỳ vọng lãi suất chính sách.

[WEB-2026-07] Nguyên nhân trực tiếp là một đợt đấu thầu JGB 10 năm yếu, phản ánh khả năng hấp thụ giảm ở mức lợi suất hiện hành. Nguyên nhân cấu trúc bên dưới: chính quyền Thủ tướng Sanae Takaichi lên kế hoạch ngân sách ban đầu FY2026 kỷ lục khoảng JPY 122,3 nghìn tỷ (~$786 tỷ), tăng khoảng 6,3% so với JPY 115,2 nghìn tỷ năm trước, một phần được tài trợ qua khoảng JPY 29,6 nghìn tỷ phát hành JGB mới. Chiến lược kinh tế dài hạn của chính quyền còn đặt mục tiêu huy động hơn JPY 370 nghìn tỷ (~$2,29 nghìn tỷ) đầu tư công-tư đến tài khóa 2040 cho các ngành chiến lược — nhà đầu tư đọc kế hoạch này như hàm ý phát hành nợ tương lai lớn hơn nhiều so với quy mô đấu thầu hiện tại.

[LLM-S] Cơ chế này khác một đợt tái định giá thắt chặt tiền tệ chuẩn: ở đây, đầu dài bán tháo vì kỳ vọng cung JGB ròng tăng nhanh hơn kỳ vọng cầu, độc lập với việc BOJ có tăng lãi suất tiếp hay không — một kênh phần bù rủi ro tài khóa, không phải kênh kỳ vọng lãi suất chính sách.

[WIKI][LLM-S] Kênh này khép lại một vòng phản hồi với ràng buộc BOJ đã nêu ở Mục 1: nếu BOJ tăng lãi suất chính sách thêm để bảo vệ đồng yên hoặc kiềm chế lạm phát nhập khẩu, điều này cộng thêm một lực tăng lợi suất dài hạn lên trên đợt tái định giá tài khóa đang diễn ra, đồng thời làm tăng chi phí trả nợ trên chương trình phát hành FY2026 đã mở rộng cùng lúc. Điều này tạo động cơ để BOJ thận trọng hơn với các đợt tăng tiếp theo so với những gì mục tiêu ổn định tỷ giá riêng lẻ gợi ý — một căng thẳng giữa lý do bảo vệ tỷ giá (ủng hộ tăng lãi suất) và lý do bền vững tài khóa (ủng hộ thận trọng).

[WEB-2026-07-01:CNBC][LLM-S] Một ranh giới cần phân biệt rõ: sau khi hedge rủi ro tỷ giá về đô la, lợi suất JGB 10 năm và 30 năm đạt khoảng 5,6% và 6,8% — cao hơn trái phiếu Kho bạc Mỹ tương đương — vì phần hedge FX gắn kèm chênh lệch lãi suất ngắn hạn Mỹ-Nhật như một khoản carry cho nhà đầu tư gốc đô la. Đây là một kênh khác với carry short-yên không hedge: cầu JGB hedge-về-đô la tạo dòng mua vào trái phiếu và bán yên kỳ hạn ở chân hedge, không tự nó tạo áp lực tăng giá giao ngay của đồng yên. Một lợi suất JGB hedge tăng có thể cùng tồn tại với bán ròng offshore chưa hedge và đồng yên giao ngay yếu — hai dòng vốn phản ứng với các nhóm nhà đầu tư và các đoạn đường cong khác nhau.

## 4. Carry Trade và Bán Ròng Offshore: Position Compression, Chưa Phải Unwind Hoàn Chỉnh

[RAW-OFFICIAL:CFTC COT][LLM-S] Báo cáo CFTC CME futures-only tính đến 23/06/2026: vị thế phi thương mại short yên ròng ở mức -146.104 hợp đồng (long 113.698, short 259.802, open interest 431.030). So với 16/06, short phi thương mại giảm 7.705 hợp đồng, long giảm 3.677 hợp đồng — short ròng giảm 4.028 hợp đồng. Đây là bằng chứng cho nén vị thế (position compression), không phải đảo chiều hoàn chỉnh: vị thế đầu cơ short-yên giảm quy mô nhưng tài khoản phi thương mại vẫn giữ short ròng lớn tính đến 23/06.

[RAW-OFFICIAL:MOF Securities Flows][LLM-S] Dữ liệu tuần 21-27/06/2026: nhà đầu tư nước ngoài bán ròng chứng khoán Nhật JPY 4,7363 nghìn tỷ (JPY 1,8165 nghìn tỷ cổ phiếu/quỹ đầu tư, JPY 493,7 tỷ nợ dài hạn, JPY 2,4261 nghìn tỷ nợ ngắn hạn) — trái ngược với báo cáo tháng 5 (mua ròng JPY 3,1058 nghìn tỷ). Việc bán ròng cuối quý này không đi kèm đồng yên tăng giá — USD/JPY vẫn quanh vùng 162 — nhất quán hơn với de-risking danh mục và nhu cầu đô la hơn là một đợt unwind carry short-yên hoàn chỉnh, vì đóng hedge sẽ đòi hỏi mua giao ngay hoặc kỳ hạn đồng yên.

[WEB-2026-07-02:Bloomberg] Xác nhận ở cấp tháng: nhà đầu tư nước ngoài bán ròng JGB nhiều nhất trong ba năm trong tháng 6/2026, sau khi lợi suất trái phiếu Nhật kém hiệu suất so với hầu hết trái phiếu chính phủ toàn cầu khác — củng cố dữ liệu tuần đã ghi ở trên là một phần của mô hình cấp tháng, không phải một tuần đơn lẻ.

[WEB-2026-05-20:Bloomberg] Riêng biệt, khoảng 20/05/2026 ghi nhận dòng ra ròng đầu tiên của nhà đầu tư nước ngoài khỏi JGB siêu dài hạn kể từ 2024 — một điểm dữ liệu theo kỳ hạn cụ thể cho thấy mô hình bán ròng ở các kỳ hạn dài đã bắt đầu hình thành trước episode cuối tháng 6.

[WIKI][LLM-S] Điểm quan trọng: đợt bán JGB tháng 6 trùng với đợt tái định giá lợi suất dài hạn do nguyên nhân tài khóa nêu ở Mục 3 — một đợt đấu thầu 10 năm yếu và lo ngại ngân sách FY2026 kỷ lục cho nhà đầu tư nước ngoài nắm giữ JGB dài hạn thêm một lý do độc lập để giảm nắm giữ, tách biệt khỏi câu hỏi phân loại hedge ở trên. Một đợt bán trái phiếu do tái định giá rủi ro tài khóa vẫn có thể đi kèm hedge FX mở hoặc đóng — nghĩa là dữ liệu tháng 6 bổ sung thêm một động lực phi-carry cho việc bán ròng, thêm một lý do nữa để không gán nhãn episode này là một đợt carry unwind hoàn chỉnh chỉ dựa trên dữ liệu dòng chứng khoán.

```text
Cấu trúc T-Account — bán chứng khoán Nhật không hedge (tạo áp lực yên yếu):
  Nhà đầu tư nước ngoài: - Cổ phiếu/JGB Nhật, + tiền yên, - tiền yên, + tiền đô la
  Ngân hàng FX dealer:   + yên nhận vào, - đô la trả ra
  => Cung yên tăng so với cầu đô la -> áp lực USD/JPY tăng

Cấu trúc T-Account — bán có hedge kèm đóng hedge (tạo áp lực yên mạnh lên):
  Nhà đầu tư nước ngoài: - Cổ phiếu Nhật; đóng forward short-yên (mua yên/bán đô la ở chân hedge)
  => Cầu yên tăng qua đóng hedge -> áp lực USD/JPY giảm
```

## 5. Tổng Hợp: Ba Vòng Phản Hồi Siết Lẫn Nhau

[LLM-S] Đọc bốn mảng trên cùng nhau cho một cấu trúc nhất quán hơn là bốn sự kiện rời rạc. BOJ tăng lãi suất (Mục 1) không đủ để thu hẹp chênh lệch lãi suất Mỹ-Nhật một khi Fed dưới Warsh giữ lập trường diều hâu, nên MOF phải chuyển từ can thiệp bằng dự trữ (Mục 2, đã cạn hiệu quả trong sáu tuần) sang chiến thuật tâm lý (im lặng có chủ đích) — một công cụ không tốn dự trữ nhưng cũng không thay đổi cơ chế cơ bản. Đồng thời, thị trường JGB (Mục 3) đã bắt đầu định giá một rủi ro hoàn toàn khác — rủi ro cung-cầu tài khóa từ ngân sách Takaichi — độc lập với cả ba kênh trên, và rủi ro này giới hạn không gian hành động của BOJ: tăng lãi suất thêm để hỗ trợ đồng yên đồng nghĩa với tăng chi phí trả nợ trên một chương trình phát hành đã lớn hơn. Ở tầng vị thế (Mục 4), cả hai kênh carry — short-yên chưa hedge và JGB hedge-về-đô la — vẫn đang hoạt động song song mà không kênh nào thay thế kênh còn lại, khiến dữ liệu dòng vốn tổng hợp (bán chứng khoán, bán JGB) không đủ để kết luận một đợt unwind hoàn chỉnh đã xảy ra.

```text
BOJ tăng lãi suất (25bp, 16/06)
   |
   v
Chênh lệch Mỹ-Nhật gần như không đổi (Fed diều hâu dưới Warsh)
   |
   v
USD/JPY không ổn định -> MOF chuyển từ can thiệp dự trữ (đã cạn tác dụng)
   sang im lặng có chủ đích (Mimura 02/07 -> Katayama 03/07, phối hợp Bessent)
   |
   v
Đồng thời: JGB 10 năm tái định giá vì rủi ro tài khóa (ngân sách JPY 122,3 nghìn tỷ,
   phát hành mới JPY 29,6 nghìn tỷ) -- kênh độc lập, không phải kỳ vọng lãi suất BOJ
   |
   v
Ràng buộc ngược lên BOJ: tăng lãi suất thêm = tăng chi phí trả nợ trên ngân sách
   đã mở rộng -> giới hạn dư địa hành động của BOJ ngay khi đồng yên cần bảo vệ nhất
   |
   v
Vị thế carry (short-yên CFTC, bán JGB nước ngoài) nén dần nhưng chưa đảo chiều
   -> chưa đủ điều kiện gọi là carry unwind hoàn chỉnh
```

## 6. Điều Kiện Biên và Các Mốc Cần Theo Dõi

[LLM-S] Chẩn đoán trên cần được xem lại nếu: (a) báo cáo CFTC tiếp theo sau 23/06 cho thấy sụp đổ đột ngột trong short-yên phi thương mại hoặc đảo chiều sang long ròng; (b) báo cáo FEIO hàng ngày tháng 4-6/2026 (dự kiến công bố 03-07/08/2026) tiết lộ can thiệp cuối tháng 6 chưa xuất hiện trong báo cáo tháng; (c) cuộc họp BOJ 30-31/07/2026 (Ueda dự kiến quay lại) hoặc tăng tốc giảm mua JGB (tín hiệu thắt chặt tài khóa) hoặc tạm dừng tăng lãi suất viện dẫn lo ngại lợi suất dài hạn/tài khóa; (d) một đợt đấu thầu JGB 10/20/30 năm tiếp theo cho thấy bid-to-cover phục hồi mạnh, cho thấy đợt tái định giá rủi ro tài khóa đã ổn định.

| Ngày / Cửa sổ | Tín hiệu | Diễn giải |
|---|---|---|
| 16/06/2026 | BOJ tăng 25bp lên 1,00% | Không đủ thu hẹp chênh lệch lãi suất Mỹ-Nhật |
| 23/06/2026 | CFTC short-yên ròng -146.104 hợp đồng | Nén vị thế, chưa đảo chiều |
| 21-27/06/2026 | MOF bán ròng chứng khoán JPY 4,7363 nghìn tỷ | De-risking cuối quý, không xác nhận đóng hedge |
| Tháng 6/2026 | Bán ròng JGB nước ngoài lớn nhất 3 năm | Một phần do tái định giá rủi ro tài khóa, không chỉ carry |
| 02-03/07/2026 | JGB 10 năm 2,7-2,75% | Cao nhất từ tháng 5/2026, động lực tài khóa |
| 02-03/07/2026 | Mimura/Katayama từ chối nêu ngưỡng can thiệp | Chiến thuật im lặng nâng lên cấp Bộ trưởng |
| 06/07/2026 | USD/JPY quanh 161,8-162,0 | Giữ gần đáy 40 năm, chưa phá thêm mức mới |
| 29/07/2026 | FOMC | Quyết định lãi suất Mỹ dưới Warsh — kiểm định lại chênh lệch lãi suất |
| 30-31/07/2026 | Họp chính sách BOJ | Ueda dự kiến quay lại; kiểm định căng thẳng lãi suất-tài khóa |
| 03-07/08/2026 | MOF FEIO báo cáo hàng ngày (04-06/2026) | Kiểm định trực tiếp ngày can thiệp cuối tháng 6 |

## Kết luận

[LLM-S] Bằng chứng đến 06/07/2026 hỗ trợ một trạng thái phức hợp hơn là một câu chuyện đơn tuyến "đồng yên yếu, BOJ tăng lãi suất, MOF can thiệp." Bốn cơ chế đang vận hành song song và ràng buộc lẫn nhau: (1) một BOJ tăng lãi suất nhưng không đủ để thu hẹp chênh lệch với Fed diều hâu; (2) một MOF đã chuyển từ can thiệp bằng dự trữ sang chiến thuật tâm lý sau khi công cụ đầu cạn hiệu quả; (3) một thị trường JGB tái định giá rủi ro tài khóa độc lập với cả hai kênh trên, giới hạn ngược lại dư địa hành động của BOJ; và (4) một cấu trúc carry hai kênh (short-yên chưa hedge và JGB hedge-về-đô la) đang nén dần nhưng chưa đảo chiều thành một đợt unwind hoàn chỉnh. Không có dữ liệu chính thức nào tính đến đầu tháng 7 xác nhận một điểm chuyển pha rõ ràng ở bất kỳ cơ chế nào trong bốn cơ chế trên.

## Confidence Tier

**Tier 2 (Reviewed, đa nguồn WEB + RAW-OFFICIAL, chưa full RAW-verified cho toàn bộ JP10Y/fiscal thread).** Dữ liệu BOJ/MOF/CFTC dựa trên RAW-OFFICIAL (BOJ MPM, MOF FEIO/ITS, CFTC COT) — confidence cao. Dữ liệu JGB 10 năm/ngân sách Takaichi dựa trên tổng hợp WEB đa nguồn (Bloomberg, AInvest, Yahoo Finance, Oxford Economics, CNBC), chưa có RAW-OFFICIAL trực tiếp từ MOF/Bộ Tài chính Nhật hoặc BOJ về chi tiết đấu thầu — cần bổ sung khi có báo cáo đấu thầu chính thức.

## Next Steps

1. Theo dõi FOMC 29/07/2026 và họp BOJ 30-31/07/2026 để kiểm định lại căng thẳng lãi suất-tài khóa nêu ở Mục 3 và 5.
2. Cập nhật [[Japan_JGB_10Y_Yield_Fiscal_Repricing_H1_2026]] khi có kết quả đấu thầu JGB 10/20/30 năm tiếp theo hoặc chi tiết ngân sách FY2026 chính thức từ MOF.
3. Cập nhật [[Japan_Foreign_Selling_Late_June_2026_Carry_Unwind_Test]] khi CFTC công bố báo cáo COT tiếp theo sau 23/06/2026 và khi MOF công bố FEIO hàng ngày (03-07/08/2026).
4. Cân nhắc SPAWN node riêng cho chiến lược ngân sách/đầu tư Takaichi (JPY 122,3 nghìn tỷ FY2026 + JPY 370 nghìn tỷ kế hoạch 2040) nếu chi tiết chính thức được công bố — hiện chỉ có trong node JP10Y dưới dạng bối cảnh, chưa phải node độc lập.

## Related Wiki Nodes

- [[BOJ_April_2026_Rate_Decision]]
- [[BOJ_June_2026_Rate_Hike_Ueda_Absence]]
- [[Japan_FX_Intervention_May_2026_Event]]
- [[Japan_FX_Intervention_MOF_BOJ_Framework]]
- [[FX_Intervention_Ambush_Tactic]]
- [[Japan_JGB_10Y_Yield_Fiscal_Repricing_H1_2026]]
- [[Japan_Foreign_Selling_Late_June_2026_Carry_Unwind_Test]]
