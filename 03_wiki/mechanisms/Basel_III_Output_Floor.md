---
title: Basel III Output Floor
aliases:
- Output Floor
- Basel 3.1 Floor
- RWA Standardized Backstop
type: mechanism
tags:
- basel-iii
- rwa
- bank-capital
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: BIS - Basel III Finalising Post-crisis Reforms (2017)
thesis: Output Floor là cơ chế 'chốt chặn' trong Basel III quy định rằng tổng RWA
  tính theo mô hình nội bộ không được thấp hơn 72.5% so với phương pháp chuẩn hóa;
  cơ chế này triệt tiêu lợi thế của các mô hình nội bộ phức tạp, buộc các ngân hàng
  lớn phải tăng vốn đáng kể cho các danh mục rủi ro cao và thúc đẩy sự dịch chuyển
  tài sản sang khu vực phi ngân hàng.
source_refs:
- file: https://www.bis.org/bcbs/publ/d424.pdf
  page: 1
created: '2026-04-13'
updated: '2026-04-22'
---

# Basel III Output Floor

## Mechanism

**Output Floor** là một thành phần cốt lõi của gói cải cách Basel III (Endgame), đặt ra mức trần (backstop) cho lợi ích mà các ngân hàng nhận được từ việc sử dụng các mô hình nội bộ (Internal Models) để tính toán tài sản có trọng số rủi ro (RWA).

Cụ thể, tổng RWA tính theo mô hình nội bộ không được thấp hơn **72.5%** so với RWA tính theo phương pháp chuẩn hóa (Standardised Approach).

$$RWA_{Internal} \ge 72.5\% \times RWA_{Standardised}$$ [extracted]

> [!IMPORTANT]
> Đây là "chốt chặn" cuối cùng nhằm đảm bảo tính so sánh và ngăn chặn các ngân hàng lớn sử dụng mô hình nội bộ cực kỳ phức tạp để giảm yêu cầu vốn xuống mức không an toàn. [researched]

> ⚠️ **[UPDATED 2026-03-20]:** Bản dự thảo Re-proposal tại Mỹ tuy giữ khung rủi ro nhưng đã cắt giảm **-4.8%** vốn CET1 cho các G-SIBs (đảo ngược mốc tăng 19% năm 2023), làm dịu đi áp lực của Output Floor tại thị trường Mỹ. Tuy nhiên, Output Floor vẫn đang có hiệu lực rất chặt tại Châu Âu (EU).

### Điều kiện
- Áp dụng cho các ngân hàng được cấp phép sử dụng phương pháp IRB (Internal Ratings-Based) hoặc các mô hình nội bộ khác.
- Được thực hiện theo lộ trình (phase-in) cho đến khi đạt mức 72.5%. [extracted]

### Ví dụ số
Nếu một danh mục cho vay có $RWA_{Standardised} = 100$ triệu USD, nhưng mô hình nội bộ của ngân hàng tính ra $RWA_{Internal} = 50$ triệu USD.
Dưới quy định Output Floor, ngân hàng bắt buộc phải sử dụng con số $72.5$ triệu USD để tính toán tỷ lệ vốn CET1. [inferred]

### Hình ảnh minh họa (Idea)
> **Cột Backstop**: Vẽ hai cột RWA. Cột A (Standardised) đầy 100%. Cột B (Model-based) chỉ cao 50%. Một vạch đỏ ngang "Floor" ở mức 72.5% cột A ngăn không cho cột B xuống thấp hơn, buộc ngân hàng phải "đắp" thêm vốn cho khoảng trống giữa 50% và 72.5%.

## Evidence / Source Anchors
- [extracted] [Basel Committee on Banking Supervision, "Basel III: finalising post-crisis reforms", 2017](https://www.bis.org/bcbs/publ/d424.htm)
- [researched] [BIS Quarterly Review, "Basel III monitoring highlights", Dec 2024](https://www.bis.org/bcbs/publ/d599_highlights.htm)
