---
title: Reserve Demand Curve — Scarce, Ample, Abundant Regime (NY Fed Time-Varying Model)
aliases:
- Scarce Ample Abundant Reserves
- Reserve Demand Curve NY Fed
- Afonso Giannone La Spada Williams Model
type: mechanism
tags:
- central-banking
- liquidity
- reserves
- monetary-operations
- fed
- central-bank-balance-sheet
status: reviewed
confidence: 3
half_life_years: 5
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Gara Afonso, Domenico Giannone, Gabriele La Spada, John Williams (NY Fed)"
provenance: "[WEB-2025-11: NY Fed Staff Report No. 1019, fetch 403 — figure from search snippet, not independently verified against PDF]"
thesis: "NY Fed Staff Report 1019 mô hình hóa đường cầu reserves theo 3 chế độ liên tục
  (không phải 3 điểm rời rạc) dựa trên độ dốc: scarce (dốc, lãi suất nhạy cung),
  ample (thoải hơn nhưng vẫn dốc xuống — một dải, không phải một số), abundant
  (phẳng, lãi suất không phản ứng cung). Ngưỡng định lượng được báo cáo: reserves
  vượt ~12-13% tổng tài sản ngân hàng đưa hệ thống vào chế độ abundant. Đây là
  ngưỡng định lượng gần nhất với nguồn nghiên cứu chính thức của Fed, khác về bản
  chất proxy so với các ước tính học thuật bên ngoài (Duffie daylight-overdraft,
  Andreopoulos $3,000B/9% GDP) — đo theo tổng tài sản ngân hàng thay vì GDP."
source_refs:
- file: Fed_Ample_Reserves_Official_Framework_2026.md
  page: 1
created: '2026-07-06'
updated: '2026-07-06'
---

# [[Reserve_Demand_Curve_Scarce_Ample_Abundant_Regime]]

## Thesis

Bản thân FOMC không công bố ngưỡng số cho "ample" — statement 17/06/2026 chỉ dùng ngôn ngữ định tính "maintaining ample reserves in the banking system" [RAW-OFFICIAL: Fed_Ample_Reserves_Official_Framework_2026.md]. Nguồn định lượng gần nhất với chính thức đến từ nghiên cứu nội bộ NY Fed: **Staff Report No. 1019** (Afonso, Giannone, La Spada, Williams — bản gốc 05/2022, sửa đổi mới nhất 11/2025), mô hình hóa đường cầu reserves theo một tham số thời gian biến đổi thay vì giả định độ dốc cố định.

## 1. Ba chế độ theo độ dốc đường cầu

- **Scarce:** độ dốc đường cầu dốc — thay đổi nhỏ trong cung reserves dịch chuyển lãi suất thị trường tiền tệ đáng kể. Đây là chế độ tiền-2008, khi reserves không sinh lãi và ngân hàng tối thiểu hóa nắm giữ.
- **Ample:** độ dốc thoải hơn scarce nhưng vẫn dốc xuống — quan trọng: đây là **một dải liên tục**, không phải một điểm cố định. Lãi suất chỉ nhạy cảm nhẹ với biến động cung reserves ngắn hạn trong dải này.
- **Abundant:** đường cầu phẳng — reserves vượt mức cần để kiểm soát lãi suất; fed funds rate không phản ứng khi cung thay đổi.

## 2. Ngưỡng định lượng

Report cho một ngưỡng cụ thể: **reserves vượt khoảng 12–13% tổng tài sản ngân hàng** đưa hệ thống vào chế độ abundant; dưới ngưỡng này, độ dốc tăng dần liên tục về phía scarce (không có bước nhảy rời rạc). [WEB-2025-11 — con số lấy từ search snippet, CHƯA verify trực tiếp với văn bản PDF gốc do newyorkfed.org chặn 403 cả WebFetch và curl.]

## 3. Khác biệt với các mỏ neo định lượng khác trong wiki

Hai proxy khác đã dùng trong cluster nghiên cứu Fed balance sheet H1 2026 đo theo cơ sở khác:
- [[Payment_System_Floor_On_Fed_Balance_Sheet]] (Duffie): sàn xuất phát từ nhu cầu thanh toán vi mô (daylight overdraft avoidance) — không cho một con số cố định, chỉ mô tả cơ chế binding.
- Mốc "~$3,000B ≈ 9% GDP" (Andreopoulos, [WEB-2026-04-11]): đo theo GDP danh nghĩa — một proxy vĩ mô.
- SR1019 (node này): đo theo **tổng tài sản ngân hàng** — một proxy vi mô/hệ thống ngân hàng.

Ba proxy không nhất thiết di chuyển cùng nhau: nếu tổng tài sản ngân hàng tăng nhanh hơn GDP danh nghĩa (ví dụ do tăng trưởng tín dụng hoặc thay đổi cấu trúc bảng cân đối ngân hàng), ngưỡng 12-13% và ngưỡng $3,000B/9%GDP có thể phân kỳ theo thời gian dù cùng mô tả một hiện tượng.

## 4. Đối chiếu thực nghiệm H1 2026

Tại 01/07/2026, reserves = $3,077.0B [RAW-OFFICIAL: Fed_H41_July2026_Balance_Sheet_Update.md], phục hồi từ đáy mùa thuế $2,901.8B (22/04), gần đỉnh dải H1 ($3,129.6B). Không có tính toán tỷ lệ reserves/tổng tài sản ngân hàng độc lập trong nghiên cứu này — cần dữ liệu H.8 (Assets and Liabilities of Commercial Banks) để tính tỷ lệ này và xác định vị trí thực tế trên đường cong scarce-ample-abundant của SR1019.

## Ranh giới / Caveat

- Ngưỡng 12-13% chưa được verify trực tiếp với văn bản gốc — xử lý như [WEB, chưa xác nhận đầy đủ] cho đến khi ingest được toàn văn PDF.
- Report là nghiên cứu học thuật nội bộ NY Fed, không phải chính sách hay cam kết chính thức của FOMC — không nên trích dẫn như "ngưỡng chính thức của Fed" mà chỉ như ước tính nghiên cứu có trọng lượng thể chế cao hơn ước tính bên ngoài.

## Related

- [[Payment_System_Floor_On_Fed_Balance_Sheet]] — sàn từ góc nhìn nhu cầu thanh toán (Duffie)
- [[Reserve_Management_Purchases_RMP]] — công cụ giữ reserves trong dải ample
- [[Supply_Driven_Vs_Demand_Driven_Reserves]] — hai cách tiếp cận khái niệm "ample"
- [[Poole_Curve_Reserve_Demand]] — đường cầu reserves cổ điển (Poole 1968), tiền thân lý thuyết
- [[Demand_for_Central_Bank_Reserves]] — khung cầu reserves (Bindseil)
- [[US_Treasury_Balance_Sheet_H1_2026]]
