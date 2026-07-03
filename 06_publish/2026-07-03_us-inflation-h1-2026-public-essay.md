# Khoảng Cách Không Phải Là Câu Chuyện Chính — Lạm Phát Mỹ H1 2026
> Ghi chú công khai | 2026-07-03 | Dữ liệu đến hết tháng 5/2026 — BLS, BEA, FOMC
> Bản trình bày công khai, dùng cấu trúc lập luận (header là luận điểm, dữ liệu lồng trong văn xuôi, kết thúc bằng điểm cần theo dõi thay vì kết luận đóng) tham khảo cách trình bày của Gianluca Benigno — không phải bản dịch, không trích dẫn bịa, mọi số liệu có nhãn nguồn. Phân tích nội bộ đầy đủ theo MODE DEEP: `06_publish/2026-07-03_us-cpi-ppi-nonlinear-inflation-h1-2026.md`.

CPI headline đang ở 4.2%. Core đang ở 2.85%. Phần lớn người đọc hai con số này đang nhìn nhầm chỗ — dấu hiệu đáng chú ý hơn nằm trong một bảng dữ liệu của BLS mà gần như không ai ngoài vài bàn giao dịch lãi suất mở ra xem.

Khi CPI tháng 5 công bố ở mức 4.2%, cách đọc nhanh và phần lớn đúng: cú sốc dầu đang đẩy lạm phát headline tách khỏi core, Fed sẽ bỏ qua thành phần năng lượng, và khoảng cách sẽ tự đóng lại khi năng lượng rời khỏi cửa sổ so sánh 12 tháng. Cách đọc đó không sai. Nhưng nó thiếu một phần có thể kiểm chứng cụ thể — và phần thiếu đó không nằm trong báo cáo CPI, mà nằm trong một bảng giá sản xuất mà gần như không ai ngoài vài bàn giao dịch mở ra xem. Một khi đã mở ra, kế hoạch "bỏ qua nó" khó bảo vệ hơn nhiều.

## Câu chuyện ai cũng đã biết

Bắt đầu từ phần không có gì tranh cãi. [WEB-2026-04:eia.gov | worldbank.org] Ngày 28/02, hành động quân sự ở Trung Đông dẫn đến việc đóng cửa trên thực tế eo biển Hormuz — kênh vận chuyển khoảng 35% lượng dầu thô giao thương đường biển toàn cầu. Nguồn cung toàn cầu giảm ước tính 10 triệu thùng/ngày — cú sốc cung dầu lớn nhất từng ghi nhận. Brent tăng từ $61 lên $118/thùng trong một quý — mức tăng theo quý điều chỉnh lạm phát lớn nhất kể từ 1988. [RAW-OFFICIAL: BLS] Chỉ số năng lượng trong CPI phản ứng tương ứng: tăng 26.9% trong bốn tháng. Riêng thành phần này giải thích gần như toàn bộ khoảng cách giữa CPI headline (4.2%) và core (2.85%), và cùng một khoảng cách đó xuất hiện ở thước đo Fed thực sự theo dõi — PCE headline 4.1%, core PCE 3.4%, mức core PCE cao nhất kể từ tháng 10/2023.

[RAW-OFFICIAL: FOMC minutes] Một cơ chế thứ hai, tách biệt, đang vận hành bên dưới. Biên bản FOMC nói rõ: lạm phát core goods tăng cao "phần lớn" là hiệu ứng tariff — và đang được bù trừ, không phải gây ra, bởi đà giảm tốc tiếp diễn ở nhà ở và dịch vụ. Hai cơ chế, hai basket khác nhau, trùng hợp về thời điểm. Gộp chúng thành một câu chuyện duy nhất sẽ đọc sai cả hai.

## Điều bảng giá sản xuất đã cho thấy

Đây là phần không xuất hiện trong bất kỳ báo cáo CPI nào. [RAW-OFFICIAL: BLS PPI Table D] BLS duy trì một bảng — Table D, chuỗi "intermediate demand by production flow" — theo dõi giá sản xuất tại bốn giai đoạn liên tiếp của chuỗi cung ứng, từ khai thác nguyên liệu thô (Stage 1) đến đầu vào gần sát thành phẩm (Stage 4). [RAW-CLIP: Benigno] Nhà kinh tế Gianluca Benigno, từng làm việc tại NY Fed, đang chạy một chỉ báo cụ thể trên bảng này: stage differential — Stage 1 YoY trừ Stage 4 YoY. Vượt ngưỡng khoảng +3 điểm phần trăm — ngưỡng ông đề xuất, gọi là τ* — một khoảng cách dương không còn giống biến động năng lượng thông thường nữa, mà giống một chi phí đang thực sự lan qua mạng lưới sản xuất.

Số liệu này không được chấp nhận theo lời ông nói suông. [RAW-OFFICIAL: BLS API, độc lập tái tính toán 2026-07-03] Tự lấy chuỗi gốc từ BLS — `WPUID51` đến `WPUID54`, xác nhận qua tài liệu chính thức của BLS sau khi một lần đoán sai mã một chuỗi PPI khác cho ra con số không khớp với văn bản công bố của chính cơ quan này — rồi tái dựng khoảng cách theo từng tháng. Kết quả khớp với số Benigno công bố trong phạm vi vài phần mười điểm phần trăm ở mọi mốc ông nêu.

**Khoảng cách stage (Stage 1 YoY trừ Stage 4 YoY), BLS Table D, tái dựng độc lập:**

| Jan | Feb | Mar | Apr | May |
|---|---|---|---|---|
| +0.16pp | +0.63pp | +2.07pp | **+3.53pp** (vượt τ*) | **+5.73pp** |

Khoảng cách vượt ngưỡng vào tháng 4 và tiếp tục nới rộng sang tháng 5, khi Stage 3 (7.20%) vượt Stage 4 (6.53%) lần đầu tiên kể từ 2022 — áp lực chi phí thượng nguồn xuất hiện ở sản xuất trung gian nhanh hơn xuất hiện ở gần thành phẩm. Đây không phải một bậc thang bốn nấc gọn gàng: tháng 5, Stage 2 (12.49%) nhích qua Stage 1 (12.26%), và điểm gãy rõ nhất nằm giữa Stage 2 và Stage 3, không trải đều qua cả bốn giai đoạn. Điều này khớp với chi tiết theo ngành: [RAW-CLIP: Benigno] áp lực tập trung ở hành lang năng lượng-hóa dầu-vận tải (nhựa resin, hóa chất công nghiệp, cước xe tải — đều tăng hai chữ số theo năm), không phải gián đoạn lan tỏa toàn hệ thống như 2021. Hẹp hơn COVID. Nhưng không phải không đáng kể.

## Giá và vật lý đã tách rời

Đây là phần đáng lo với bất kỳ ai coi giá dầu futures là toàn bộ câu chuyện. Brent đã giảm 18% từ đỉnh tháng 3. Nếu giá là thước đo đúng cho mức độ gián đoạn, đó sẽ là tin tốt. Nhưng [RAW-CLIP: Benigno] lưu lượng tàu qua Hormuz đã giảm từ khoảng 80 chuyến/ngày xuống 4 chuyến/ngày, trọng tải từ 4 triệu xuống 0.1 triệu tấn/ngày — và cả hai con số này đã đi ngang ở mức đó suốt ba tháng. Giá đã phục hồi. Điểm nghẽn thì không mở lại.

[RAW-CLIP: Benigno] lập luận rằng giá dầu futures là điều kiện cần nhưng không đủ để đọc cú sốc này — futures bỏ sót chi phí tích lũy từ việc chuyển hướng vận chuyển và trì hoãn đầu vào, và bỏ sót việc chuỗi chi phí tiếp tục lan truyền ngay cả sau khi giá giao ngay đã đảo chiều.

Suy ra tiếp: bất kỳ dự báo nào dựa trên đường cong futures năng lượng sẽ tự động thể hiện giảm phát khi dầu rời khỏi cửa sổ so sánh 12 tháng — đúng lúc eo biển vẫn đóng và chuỗi chi phí vẫn đang lan. Đây gần với sai lầm năm 2021, khi việc thiếu chip bán dẫn lan chậm qua sản xuất xe hơi thể hiện ra ngoài như một cú sốc xe cũ "riêng lẻ", trong khi thực chất đó là điểm cuối có thể nhìn thấy của một chuỗi cascade nhiều giai đoạn đã tích lũy suốt nhiều tháng.

## Vì sao ngưỡng này không giải quyết được gì

Không nên đọc toàn bộ phần trên như một điều chắc chắn hơn thực tế. [RAW-CLIP: Benigno, tự nhận] Ngưỡng τ* được suy ra từ mẫu ngắn, chia theo độ lớn khoảng cách chứ không phải ước tính bằng phương pháp thống kê chặt chẽ — theo mô tả của chính tác giả, đây là "công cụ phân loại và xác nhận, không phải công cụ dự báo". Luận điểm rộng hơn — rằng cú sốc lớn tạo ra động lực lạm phát phi tuyến tính, không chỉ tỷ lệ thuận — dựa trên một nghiên cứu 22 quốc gia mà tác giả nhắc đến nhưng không trích dẫn — không có tên bài báo, không có link working paper, không có gì để kiểm chứng độc lập. Và luận điểm hay được nhắc lại nhất — PPI dẫn trước CPI 6-12 tháng — không được đo lường ở bất kỳ đâu trong framework này. Đó là một khẳng định định tính, minh họa một lần bằng ca xe cũ 2021, và không có gì chính xác hơn thế.

Trong khi đó, thị trường lẽ ra phải định giá rủi ro này vẫn chưa làm vậy. Breakeven TIPS 10 năm đã đi ngang trong biên độ 2.20%–2.48% suốt cả năm, ngay cả khi giá sản xuất core tăng tốc lên mức nhanh nhất trong ba năm. Hoặc thị trường đúng khi hoài nghi rằng chuỗi cascade này sẽ chạm tới người tiêu dùng, hoặc thị trường đang định giá thấp một rủi ro đuôi mà nó chưa bị buộc phải nhìn vào.

**Điều hai kỳ công bố tiếp theo cần cho thấy — điểm cần theo dõi, không phải kết luận:**

- **CPI tháng 6, 14/07.** Headline có bắt đầu hội tụ về core, hay thành phần năng lượng vẫn ở mức cao lâu hơn mức toán học base-effect gợi ý?
- **PPI tháng 6, 15/07.** Stage 3 có tiếp tục vượt Stage 4 tháng thứ ba liên tiếp? Một lần đảo chiều là một điểm dữ liệu; ba lần là một mô hình.
- **Lưu lượng vận chuyển qua Hormuz.** Toàn bộ lập luận về tính bền vững của cú sốc dựa trên việc điểm nghẽn tiếp tục đóng. Nếu lưu lượng bắt đầu phục hồi, luận điểm cascade mất đi cơ sở vật lý.
- **Breakeven 10 năm.** Vẫn đi ngang. Đáng kiểm tra lại sau kỳ công bố PPI tháng 6 — nếu khoảng cách stage tiếp tục nới rộng mà breakeven vẫn không nhúc nhích, chính khoảng cách định giá đó trở thành điều đáng chú ý.

Tàu vẫn chưa di chuyển trở lại. Mọi thứ còn lại ở đây chỉ là câu hỏi về việc điều đó còn đúng trong bao lâu.

---

**[RAW-OFFICIAL]** Số liệu CPI, PPI, và Table D: BLS public API và FRED mirror, lấy ngày 03/07/2026, đã xác minh khớp với phần trăm headline BLS công bố chính thức. Số liệu PCE: BEA qua FRED, đã xác minh khớp với YoY BEA công bố. Đặc điểm FOMC: biên bản tháng 1, 3, 4/2026 và Summary of Economic Projections 17/06/2026.

**[RAW-CLIP]** Framework stage-differential, ngưỡng τ*, tương quan GSCPI, và Hormuz Transit Stress Index lấy từ loạt 3 bài Substack của Gianluca Benigno về nonlinear inflation. Nguồn đơn lẻ, tác giả tự nhận mẫu ngắn; số liệu stage-gap headline đã được tái xác nhận độc lập từ dữ liệu BLS gốc, ngưỡng diễn giải thì chưa.
