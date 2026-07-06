---
title: Treasury Marketable Debt Duration + Buyback Mechanics — Fresh Pull H1 2026
type: raw-clip
source_tag: RAW-OFFICIAL
tags:
- treasury-debt
- wam
- tbac
- buyback
retrieved: '2026-07-06'
---

Nghiên cứu độc lập, không tham chiếu số liệu cũ trong cluster trước ngoài việc đối chiếu cuối cùng.

## 1. Nợ khả thị theo kỳ hạn (MSPD, tháng 5/2026)

Trong tổng nợ công $31.52T (nợ khả thị): Notes $15.94T (50.58%), Bills $6.76T (21.44%), Bonds $5.40T (17.14%). Tổng nợ quốc gia bruto đạt $39.20T tại 03/06/2026 (nợ do công chúng nắm $31.60T + nội bộ chính phủ $7.61T). Số liệu MSPD tháng 6/2026 (as-of 04/06) đã công bố; kỳ công bố kế tiếp 07/07/2026 (CHƯA ra tại thời điểm nghiên cứu).

Nguồn: fiscaldata.treasury.gov MSPD; JEC Monthly Debt Update [WEB-2026-06]

## 2. Weighted Average Maturity

**70 tháng (5.83 năm) tại tháng 3/2026** — giảm từ 71 tháng (3/2025), tăng từ 67 tháng (3/2021). ~33% nợ khả thị do công chúng nắm đáo hạn trong 12 tháng (Q2 FY2026). KHÔNG tìm được điểm WAM mới hơn (4/5/6-2026) — 70 tháng/tháng 3 vẫn là điểm công bố mới nhất.

Nguồn: GAO-26-107529; tổng hợp search, trang nguồn cụ thể chưa xác nhận độc lập [WEB-2026, chưa verify từng trang]

## 3. TBAC — tỷ trọng bills & Q3 2026 refunding

- **Bills = 21.7% tổng nợ tại 30/04/2026** — trên dải khuyến nghị lịch sử 15–20% (khớp hướng với ghi nhận trước, số liệu cập nhật).
- Biên bản TBAC 05/05/2026: Committee **đồng thuận tuyệt đối khuyến nghị giữ nguyên quy mô đấu thầu coupon danh nghĩa và FRN** trong ít nhất vài quý tới; đồng thuận rằng quy mô coupon + cung bill hiện tại đáp ứng nhu cầu tài trợ FY2026, nhưng dự báo trung vị của primary dealer ngụ ý **thiếu hụt tài trợ $1.3T trong FY2027-28** ở mức coupon/bill hiện tại — cờ rủi ro tương lai, KHÔNG phải sự kiện H1 2026.
- TBAC charge "Bill Purchases and the Consolidated Balance Sheet" (Q1 2026) tồn tại nhưng KHÔNG fetch được nội dung (PDF timeout 2 lần).
- **Q3 2026 refunding CHƯA công bố** — dự kiến **Thứ Tư 05/08/2026**. Gần nhất vẫn là Q2 2026 (~05/2026). Không coi bất kỳ con số Q3 nào là đã xác nhận.

Nguồn: home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding [WEB-2026-05]

## 4. Chương trình buyback của Treasury

- **Cơ chế**: hai track riêng biệt — **Liquidity support** (off-the-run, ~1-2 lần/tuần, quy mô nhỏ $300M–$2B/operation) và **Cash management** (bucket 1 tháng–2 năm, theo mùa quanh ngày quyết toán thuế — giữa tháng 4/6/9/12, quy mô lớn hơn $12–15B/operation). Công bố cùng ngày với họp báo refunding hàng quý.
- **Trần quý 05–07/2026**: tối đa $38B liquidity support (mọi bucket) + tối đa $25B cash management (1 tháng-2 năm).
- **Operations gần đây** (từ fiscaldata API, 03/06–01/07/2026, 8/208 operations 2026 được lấy mẫu): liquidity support $300M–$2.0B mỗi lần trên bucket 7Y-30Y và TIPS; cash management 04/06/2026 ($12.5B) và 11/06/2026 ($12.08B) trong bucket 1 tháng-2 năm — cả hai gần ngày quyết toán thuế giữa tháng 6. **Lưu ý: bảng này qua model tóm tắt của WebFetch trên raw JSON, không phải đọc trực tiếp — coi các con số par cụ thể là chỉ báo, cần verify lại qua API pull trực tiếp nếu dùng định lượng.**

## 5. Phát hành coupon Q3 2026

Chưa có công bố riêng cho Q3 (đến 05/08/2026). Chỉ có tín hiệu forward-looking từ khuyến nghị TBAC "giữ nguyên quy mô coupon/FRN trong vài quý tới" (họp 05/2026) — hướng đi ngang, không phải con số mới.

## Gaps đã flag, chưa lấp

- Điểm WAM chính xác tháng 4/5/6-2026 (chỉ có 70 tháng/tháng 3 xác nhận).
- Toàn văn TBAC charge Q2 2026 (fetch timeout, 2 lần).
- Tổng khối lượng buyback H1 đầy đủ (chỉ 8/208 operations 2026 xuất hiện).
