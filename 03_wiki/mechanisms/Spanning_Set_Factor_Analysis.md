---
title: Spanning Set Factor Analysis
aliases:
- Spanning Set
- Factor Analysis
- Lagrange optimiser in tracking errors
type: mechanism
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Alexander Düring"
provenance: "Fixed_Income_Alexander_During_Ch36.md"
thesis: Khi số lượng mã Trái phiếu trong Index lên tới hàng nghìn, mô phỏng toàn phần
  (Full replication) là tự sát tài chính do phí giao dịch. Các rổ quỹ mô phỏng bán
  phần (Partial replication) vận dụng mô hình tối ưu Lagrange để thiết lập Tập Giăng
  (Spanning Set) đa chiều. [extracted] [[Fixed_Income_Alexan
source_refs:
- file: Fixed_Income_Alexander_During_Ch36.md
  page: 1
created: '2026-04-13'
updated: '2026-04-16'
chapter: 35
---

# Spanning Set [[Spanning_Set_Factor_Analysis|factor analysis]]

## Mechanism

Khi số lượng mã Trái phiếu trong Index lên tới hàng nghìn, mô phỏng toàn phần (Full replication) là tự sát tài chính do phí giao dịch. Các rổ quỹ mô phỏng bán phần (Partial replication) vận dụng mô hình tối ưu Lagrange để thiết lập Tập Giăng (Spanning Set) đa chiều. [extracted] [[Fixed_Income_Alexander_During_Ch36.md#page=5]]

**Khái quát Toán học:**
Nếu thị trường có $k$ cội nguồn rủi ro (Risk factors), nhà quản lý chỉ cần tìm cất vó vừa đúng $N$ mã tài sản đầu tầu ($N \ge k$) sao cho sự nhạy cảm của chúng vươn rễ bám đủ (spanning) được trọn vẹn bề rộng không gian rủi ro k-chiều đó. 
Thông qua Hàm Lagrange ($\mathcal{L}$) giới hạn chặt (hard constraints):
1. **Với Cổ phiếu:** Chạy hồi quy véc-tơ quá khứ.
2. **Với Trái phiếu:** Rủi ro cũ kỹ theo thời gian, nên đạo hàm chạy dựa theo Độ nhảy cảm Nhóm Kì hạn ($Duration$ $D_i^*$). Hàm tối ưu ép Tổng Trọng số Duration của rổ $N$ mã mạo danh bám chặt vào Tổng Duration kỳ vọng của Toàn thị trường $D_m^*$, qua đó loại bỏ phần lớn Tracking Error với mức phí giao dịch rẻ mạt nhất. [extracted] [[Fixed_Income_Alexander_During_Ch36.md#page=6-7]]

## Evidence / Source Anchors
- [[Fixed_Income_Alexander_During_Ch36.md#page=5-7]] — Ứng dụng mô hình Spanning Set và Lagrange rào hãm Tracking Error trong đầu tư định lượng.
