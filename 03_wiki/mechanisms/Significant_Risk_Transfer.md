---
title: Significant Risk Transfer
aliases:
- SRT
- Synthetic Risk Transfer
- Capital Relief Trades
- CRT
type: mechanism
tags:
- basel-iii
- private-credit
- risk-transfer
- rwa-optimization
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: '**Significant Risk Transfer (SRT)** là một kỹ thuật quản lý vốn pháp quy,
  trong đó ngân hàng chuyển giao rủi ro tín dụng của một danh mục tài sản (thường
  là các khoản vay doanh nghiệp, mortgage, hoặc tài sản cốt lõi) sang cho các nhà
  đầu tư tư nhân (thường là các quỹ Private Credit hoặc Hedge Funds)'
source_refs: []
created: '2026-04-13'
updated: '2026-04-16'
source: https://www.bis.org/publ/qtrpdf/r_qt2409b.htm
---

# Significant Risk Transfer

## Mechanism

**Significant Risk Transfer (SRT)** là một kỹ thuật quản lý vốn pháp quy, trong đó ngân hàng chuyển giao rủi ro tín dụng của một danh mục tài sản (thường là các khoản vay doanh nghiệp, mortgage, hoặc tài sản cốt lõi) sang cho các nhà đầu tư tư nhân (thường là các quỹ Private Credit hoặc Hedge Funds).

Bằng cách chuyển giao rủi ro này, ngân hàng được phép giảm tài sản có trọng số rủi ro (RWA) tương ứng, từ đó giải phóng vốn CET1 mà không cần phải bán đứt tài sản vật lý hay làm đứt đoạn mối quan hệ với khách hàng.

> [!IMPORTANT]
> SRT bản chất là một "Hợp đồng bảo hiểm rủi ro tín dụng" được cấu trúc theo dạng chứng khoán hóa tổng hợp (Synthetic Securitisation). [extracted]

### Cấu trúc hoạt động
1. **Danh mục tham chiếu (Reference Pool)**: Ngân hàng chọn một nhóm các khoản vay hiện có trên bảng cân đối.
2. **First-loss Tranche**: Ngân hàng thường giữ lại một phần nhỏ rủi ro đầu tiên.
3. **Mezzanine Tranche**: Đây là phần rủi ro được bán cho các nhà đầu tư Private Credit. Họ nhận được lợi suất cao (coupon) để đổi lấy việc gánh chịu khoản lỗ nếu danh mục tham chiếu bị vỡ nợ quá một ngưỡng nhất định. [inferred]
4. **Capital Relief**: Cơ quan quản lý (ECB/Fed) công nhận việc rủi ro đã được chuyển giao "đáng kể" và cho phép ngân hàng hạ thấp hệ số rủi ro của danh mục đó. [extracted]

### Động lực (Incentives)
- **Ngân hàng**: Tối ưu hóa bảng cân đối kế toán trong bối cảnh Basel III Endgame đẩy RWA lên cao (đặc biệt là do Output Floor). 
  > ⚠️ **[UPDATED 2026-03-20]:** Bản Re-proposal tại Mỹ đã hạ **Securitization Floor từ 20% xuống 15%**. Điều này tạo động lực khổng lồ cho các ngân hàng thực hiện SRT. Thay vì bán đứt khoản vay, họ chứng khoán hóa, giữ lại phần Prime (RWA thấp) và bán phần Mezzanine/Equity cho Private Credit để nhận Capital Relief tối đa.
- **Quỹ Private Credit**: Tiếp cận lợi nhuận từ các danh mục tài sản chất lượng của ngân hàng (thường là rủi ro thấp hơn các khoản vay direct lending trực tiếp) với mức lợi suất hấp dẫn (10-15% ROE). [researched]

### Hình ảnh minh họa (Idea)
> **Piston Giảm Áp**: Vẽ một bảng cân đối ngân hàng đang bị nén bởi khối "Basel Requirements". Một chiếc van xả tên "SRT" mở ra, đẩy khối rủi ro (Risk) sang một bình chứa bên cạnh tên "Private Credit Fund". Kết quả là bảng cân đối ngân hàng được "giải nén" và trở nên nhẹ nhàng hơn (Capital Relief).

## Evidence / Source Anchors
- [extracted] [BIS Quarterly Review, "The global drivers of private credit", March 2025](https://www.bis.org/publ/qtrpdf/r_qt2503b.htm)
- [extracted] [BIS Quarterly Review, "Synthetic Risk Transfer", Sep 2024](https://www.bis.org/publ/qtrpdf/r_qt2409b.htm)
- [researched] [PwC UK, "Capital Relief Transactions", 2025](https://www.pwc.co.uk/financial-services/assets/pdf/capital-relief-transactions.pdf)
ttps://www.pwc.co.uk/financial-services/assets/pdf/capital-relief-transactions.pdf)
