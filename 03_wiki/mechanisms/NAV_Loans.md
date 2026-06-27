---
title: NAV Loans
aliases:
- NAV Financing
- NAV Lines
- Fund-level Debt
type: mechanism
tags:
- private-credit
- fund-finance
- leverage
- liquidity
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: '**NAV Loans (Vay dựa trên giá trị tài sản ròng)** là một hình thức tín dụng
  cấp cho các quỹ đầu tư (Private Equity hoặc Private Credit), trong đó tài sản bảo
  đảm là toàn bộ danh mục tài sản hiện có của quỹ (Net Asset Value - NAV), thay vì
  từng tài sản riêng lẻ.'
source_refs: []
created: '2026-04-13'
updated: '2026-04-16'
source: https://www.pwc.com/gx/en/financial-services/assets/pdf/nav-loans-private-equity-debt.pdf
---

# NAV Loans

## Mechanism

**NAV Loans (Vay dựa trên giá trị tài sản ròng)** là một hình thức tín dụng cấp cho các quỹ đầu tư (Private Equity hoặc Private Credit), trong đó tài sản bảo đảm là toàn bộ danh mục tài sản hiện có của quỹ (Net Asset Value - NAV), thay vì từng tài sản riêng lẻ.

Khác với [[Subscription_Lines]] (vốn dựa trên cam kết chưa giải ngân của LPs), NAV Loans được sử dụng khi quỹ đã giải ngân phần lớn vốn và muốn tối ưu hóa thanh khoản từ các tài sản đang nắm giữ.

> [!IMPORTANT]
> **LTV (Loan-to-Value)** của NAV Loans thường rất thấp, dao động dưới **20%**, nhằm tạo ra một lớp đệm an toàn lớn cho bên cho vay trước sự biến động của giá trị tài sản cơ sở. [extracted]

### Mục đích sử dụng
- **Liquidity for LPs**: Tạm ứng tiền mặt để phân phối cho nhà đầu tư (LPs) khi thị trường thoái vốn (exit) bị chậm lại.
- **Follow-on Investment**: Cung cấp vốn bổ sung để hỗ trợ hoặc thâu tóm thêm cho các công ty trong danh mục mà không cần gọi vốn mới.
- **M&A at Fund Level**: Thực hiện các thương vụ mua lại ở cấp độ quỹ. [researched]

### Rủi ro và Tranh cãi
- **Double Leverage**: Tạo ra đòn bẩy kép (đòn bẩy tại công ty mục tiêu + đòn bẩy tại cấp độ quỹ), làm gia tăng rủi ro hệ thống.
- **Transparency**: Các LPs (nhà đầu tư hạn hữu) thường lo ngại về việc thiếu minh bạch trong việc sử dụng NAV Loans để "làm đẹp" chỉ số IRR hoặc trì hoãn việc nhận diện thua lỗ. [extracted]

### Hình ảnh minh họa (Idea)
> **Mỏ neo thanh khoản**: Vẽ một rổ trái cây (Portfolio Assets). Một sợi dây thừng (NAV Loan) buộc vào rổ này để kéo một chiếc thuyền (Fund Liquidity) đi lên. Chú thích: "Cấp vốn dựa trên giá trị rổ tài sản hiện hữu".

## Evidence / Source Anchors
- [extracted] [PwC, "Global Private Equity Powerhouse", 2024](https://www.pwc.com/gx/en/financial-services/assets/pdf/nav-loans-private-equity-debt.pdf)
- [researched] [BlackRock, "NAV Lending Trends", 2025](https://www.blackrock.com/institutions/en-zz/insights/synthetic-risk-transfer-srt-guide)
- [researched] [SVB, "The Rise of NAV Financing", 2024](https://www.svb.com/insights/advisory-services/nav-financing)

## Related

- [[Private_Equity_Mechanism]] — PE funds sử dụng NAV Loans để tạo thanh khoản late-stage mà không phải gọi vốn mới.
- [[Direct_Lending]] — Kết nối cấp độ: Direct Lending tài trợ công ty trong danh mục; NAV Loan tài trợ chính quỹ PE dựa trên tài sản đó.
- [[Private_Credit]] — NAV Loans là một phân khúc đang tăng trưởng trong hệ sinh thái Private Credit.
- [[Subscription_Lines]] — Công cụ thanh khoản early-stage (dựa trên LP commitments), đối ngược với NAV Loans (late-stage, dựa trên assets).
- [[Private_Credit_Systemic_Risk_Loop]] — Double leverage tạo ra bởi NAV Loans là một vector rủi ro hệ thống.
