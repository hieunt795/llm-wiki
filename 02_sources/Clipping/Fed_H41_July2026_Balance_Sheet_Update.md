---
title: Fed H.4.1 Balance Sheet — July 2026 Update (Release 2026-07-02, as-of 2026-07-01)
type: raw-clip
source_tag: RAW-OFFICIAL
tags:
- fed-balance-sheet
- h41
- reserves
- rmp
retrieved: '2026-07-06'
---

Nguồn: federalreserve.gov/releases/h41/current/ — release Thursday 2026-07-02, số liệu as-of Wednesday 2026-07-01. Điểm dữ liệu kế tiếp sau baseline 24/06/2026 đã ghi nhận trong cluster trước.

## Bảng cân đối tổng quan (triệu USD)

| Khoản mục | 01/07/2026 | Δ so với 24/06/2026 |
|---|---|---|
| Tổng tài sản | 6,724,564 | ~ đi ngang (baseline $6,735,564) |
| UST tổng | 4,492,235 | +4,129 (tuần) |
| — Bills | 489,293 | |
| — Notes/Bonds (nominal) | 3,611,801 | |
| — TIPS | 282,634 | |
| MBS | 1,948,398 | giảm từ 1,961,600 — tiếp tục runoff |
| Reserve balances | 3,077,019 | **+122,554** so với 24/06 |
| TGA | 807,359 | **−111,341** so với 918,700 (24/06) |
| Reverse repo tổng | 338,438 | |
| — Foreign official/quốc tế | 336,715 | |
| — Khác | 8,063 | ghi chú: 336,715+8,063=344,778 ≠ 338,438 công bố — không khớp nội bộ, không tự ý điều chỉnh, giữ nguyên số liệu nguồn |

## Bảng 2 — Phân bố kỳ hạn UST, 01/07/2026 (triệu USD)

| Kỳ hạn còn lại | Nắm giữ | Δ tuần |
|---|---|---|
| ≤15 ngày | 81,609 | −23,993 |
| 16–90 ngày | 343,382 | −6,491 |
| 91 ngày–1 năm | 531,768 | +22,853 |
| >1–5 năm | 1,431,865 | +6,388 |
| >5–10 năm | 490,590 | +5,099 |
| >10 năm | 1,613,020 | +272 |
| **Tổng** | **4,492,235** | +4,129 |

**Giới hạn:** Fed không công bố WAM trực tiếp trong H.4.1; bucket ">10 năm" không có kỳ hạn trung bình công bố nên KHÔNG thể recompute WAM đáng tin cậy chỉ từ bảng này — cùng giới hạn đã ghi nhận khi tính con số 7.24 năm (24/06) trước đó.

## RMP pace — cần đối chiếu

Từ WebSearch (Bloomberg 2026-06-11 + NY Fed operating policy statements, KHÔNG fetch trực tiếp được do newyorkfed.org 403):
- Chu kỳ tháng 7 (kết thúc 13/07/2026): ~$10B bill purchases mới (không đổi so với chu kỳ trước) + ~$16.5B reinvestment cùng kỳ.
- Quy đổi ≈ $26–29B/tháng — **KHÔNG khớp** với trend +$42B/tháng UST net đã CONFIRMED trong cluster trước (tính bằng endpoint method Dec–June từ H.4.1).
- Chưa rõ đây là: (a) pace chậm lại thật vào tháng 7, (b) khác biệt định nghĩa (net UST change trên H.4.1 vs gross RMP+reinvestment operational sizing công bố theo lịch), hay (c) cần thêm điểm dữ liệu để đối chiếu. Flag mở, chưa resolve.

## Không tìm được / bị chặn

- newyorkfed.org: 403 trên WebFetch trực tiếp (operating_policy_260701) — nhất quán với các lần chặn trước.
- Không có ngôn ngữ RMP pace/composition trong chính văn bản h41.htm (xác nhận vắng mặt).
- Không lấy được toàn văn FOMC statement tháng 7/2026 trong lượt này.
