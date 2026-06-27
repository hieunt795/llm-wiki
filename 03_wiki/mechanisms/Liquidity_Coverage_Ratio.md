---
title: Liquidity Coverage Ratio
aliases:
- LCR
- Basel III Liquidity
type: mechanism
tags:
- basel-iii
- liquidity-risk
- cash-management
status: reviewed
confidence: 4
half_life_years: 1
expert_lens: "BCBS | BIS"
provenance: "BCBS (2013) | BIS Quarterly Review (2025)"
thesis: '**LCR** là chỉ số thanh khoản ngắn hạn của Basel III, yêu cầu ngân hàng nắm
  giữ một lượng tài sản thanh khoản chất lượng cao (High-Quality Liquid Assets - HQLA)
  đủ để bù đắp cho dòng tiền chi trả ròng (Net Cash Outflows) trong kịch bản căng
  thẳng cực độ kéo dài 30 ngày.'
source_refs: []
created: '2026-04-13'
updated: '2026-04-28'
source: https://www.bis.org/publ/bcbs238.pdf
---

# Liquidity Coverage Ratio

## Mechanism

**LCR** là chỉ số thanh khoản ngắn hạn của Basel III, yêu cầu ngân hàng nắm giữ một lượng tài sản thanh khoản chất lượng cao (High-Quality Liquid Assets - HQLA) đủ để bù đắp cho dòng tiền chi trả ròng (Net Cash Outflows) trong kịch bản căng thẳng cực độ kéo dài 30 ngày.

LCR được thiết kế để đảm bảo ngân hàng có đủ "bình oxy" để vượt qua một cuộc tháo chạy vốn hoặc cú sốc thanh khoản ngắn hạn mà không cần phụ thuộc vào sự trợ giúp của Ngân hàng Trung ương.

$$LCR = \frac{\text{Stock of HQLA}}{\text{Total Net Cash Outflows over the next 30 calendar days}} \ge 100\%$$ [extracted]

### Điều kiện
- **HQLA (Tài sản thanh khoản chất lượng cao)**: Bao gồm tiền mặt, dự trữ tại NHTW và các trái phiếu chính phủ rủi ro thấp. Các tài sản rủi ro hơn (như trái phiếu doanh nghiệp) bị áp dụng hệ số Haircut (chiết khấu) cao hoặc bị giới hạn tỷ trọng. [extracted]
- **Dòng tiền ra ròng (Net Outflows)**: Được tính dựa trên giả định về tỷ lệ tháo chạy vốn của tiền gửi (run-off rates) và nhu cầu thanh khoản ngoại bảng (như các hạn mức tín dụng cam kết cho các quỹ Private Credit). [extracted]

### Tác động đến Private Credit
Việc LCR siết chặt yêu cầu giữ HQLA khiến ngân hàng phải thu hẹp các cam kết thanh khoản ngoại bảng (Subscription lines) hoặc tăng phí dịch vụ đối với các quỹ Private Credit để bù đắp cho chi phí "giam giữ" tài sản thanh khoản. [inferred]

### Hình ảnh minh họa (Idea)
> **Bình Oxy 30 ngày**: Vẽ một bình chứa (HQLA) cung cấp khí cho một người (Ngân hàng) đang đi qua một đường hầm tối (30-day stress). Nếu lượng khí trong bình ít hơn nhu cầu tiêu thụ, đồng hồ báo động "Solvency Crisis" sẽ xuất hiện ở cuối đường hầm.

## Evidence / Source Anchors
- [extracted] [Basel Committee on Banking Supervision, "Basel III: The Liquidity Coverage Ratio and liquidity risk monitoring tools", 2013](https://www.bis.org/publ/bcbs238.htm)
- [researched] [BIS Quarterly Review, March 2025](https://www.bis.org/publ/qtrpdf/r_qt2503b.htm)
