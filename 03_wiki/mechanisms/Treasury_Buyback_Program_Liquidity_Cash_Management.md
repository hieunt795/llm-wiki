---
title: Treasury Buyback Program — Liquidity Support and Cash Management Tracks
aliases:
- Treasury Buyback Program
- Debt Buyback Liquidity Support
- Cash Management Buyback
type: mechanism
tags:
- treasury-market
- debt-management
- liquidity
- fiscal-policy
status: reviewed
confidence: 3
half_life_years: 4
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Brian Smith (Treasury) | TBAC"
provenance: "[WEB-2026: Treasury_Buyback_Duration_Fresh_H1_2026.md — home.treasury.gov press releases, fetch timeout on primary doc, content from search snippet]"
thesis: "Treasury vận hành chương trình buyback trên chính nợ đã phát hành của mình
  qua hai track tách biệt: liquidity support (tối đa $38B/quý, off-the-run, ~1
  lần/tuần — cho holders lối thoát dự đoán được) và cash management (tối đa
  $25B/quý, bucket 1 tháng-2 năm, canh theo lịch quyết toán thuế giữa tháng
  4/6/9/12 — làm mượt biến động số dư tiền mặt). Đây là công cụ của debt manager
  (Treasury) làm mượt phát hành/tiền mặt của CHÍNH mình, hoàn toàn tách biệt về
  cơ chế và mục đích với Reserve Management Purchases (RMP) của Fed — vốn là
  ngân hàng trung ương bơm reserves mới qua mua tài sản ròng."
source_refs:
- file: Treasury_Buyback_Duration_Fresh_H1_2026.md
  page: 1
created: '2026-07-06'
updated: '2026-07-06'
---

# [[Treasury_Buyback_Program_Liquidity_Cash_Management]]

## Thesis

Treasury tái khởi động chương trình buyback nợ công từ 2024 như một công cụ quản lý nợ hiện đại (không dùng từ 2002 trước đó). Chương trình vận hành qua hai track có mục đích và lịch trình khác nhau, công bố cùng ngày với họp báo refunding hàng quý.

## 1. Hai track vận hành

- **Liquidity support:** tối đa **$38B/quý** (quý 05-07/2026) trên các bucket kỳ hạn off-the-run (bao gồm coupon dài 7Y-30Y và TIPS), tần suất ~1 lần/tuần, quy mô nhỏ mỗi lần ($300M-$2B). Mục đích: cho holders nắm off-the-run securities một kênh thoát vị thế có thể dự đoán trước, giảm bid-ask spread và cải thiện độ sâu thị trường thứ cấp cho các kỳ hạn kém thanh khoản.
- **Cash management:** tối đa **$25B/quý** trong bucket 1 tháng-2 năm, quy mô mỗi lần lớn hơn ($12-15B), canh theo lịch **quyết toán thuế (giữa tháng 4, 6, 9, 12)** — thời điểm số dư TGA tăng vọt do thu thuế. Mục đích: hấp thụ một phần biến động phát hành bill/TGA ngắn hạn bằng cách mua lại nợ ngắn hạn khi tiền mặt dư thừa, thay vì để toàn bộ biến động dồn vào TGA.

## 2. Phân biệt với Reserve Management Purchases (Fed)

| Chiều | Treasury Buyback | [[Reserve_Management_Purchases_RMP]] |
|---|---|---|
| Actor | Treasury (debt manager) | Fed (central bank) |
| Tài sản mua | Nợ CHÍNH MÌNH đã phát hành | UST của thị trường thứ cấp |
| Tài trợ | Bằng phát hành mới ở kỳ hạn khác | Tạo reserves mới (liability Fed) |
| Mục đích | Làm mượt phát hành/tiền mặt của Treasury | Giữ reserves ngân hàng ở mức ample |
| Tác động bảng cân đối | Trung lập với Fed; đổi cơ cấu kỳ hạn nợ Treasury | Mở rộng/giữ phẳng bảng cân đối Fed |

Không tìm thấy cơ chế phối hợp trực tiếp nào giữa hai chương trình trong nghiên cứu này — chúng vận hành độc lập dù cùng ảnh hưởng đến thanh khoản thị trường Treasury.

## 3. Dữ liệu vận hành gần đây (H1 2026)

Ví dụ operations lấy mẫu từ fiscaldata API (03/06-01/07/2026): liquidity support $300M-$2.0B mỗi lần trên bucket 7Y-30Y và TIPS; cash management $12.5B (04/06) và $12.08B (11/06) trong bucket 1 tháng-2 năm — cả hai gần ngày quyết toán thuế giữa tháng 6. [LLM-E — bảng lấy qua model tóm tắt WebFetch trên raw JSON, không phải đọc trực tiếp; coi số liệu par cụ thể là chỉ báo, cần verify lại qua API pull trực tiếp nếu dùng định lượng].

## Ranh giới / Caveat

- Nội dung press release gốc (home.treasury.gov/news/press-releases/sb0489) chưa fetch được trực tiếp (timeout) — thông tin qua search snippet, xử lý như nguồn cấp hai.
- Tổng khối lượng buyback H1 2026 đầy đủ chưa xác định (chỉ 8/208 operations 2026 xuất hiện trong lượt research này).
- Chương trình này KHÔNG phải công cụ chính sách tiền tệ — không nên nhầm với QE hay RMP dù cùng là "Treasury mua Treasury".

## Related

- [[Reserve_Management_Purchases_RMP]] — chương trình song song của Fed, phân biệt rõ về intent
- [[Treasury_Debt_Management_Strategy]] — khung TBAC bills vs coupons, extraordinary measures
- [[US_Treasury_Balance_Sheet_H1_2026]] — snapshot nợ công + WAM + refunding
- [[Treasury_General_Account_Mechanism]] — TGA dynamics mà cash-management buyback nhắm tới làm mượt
