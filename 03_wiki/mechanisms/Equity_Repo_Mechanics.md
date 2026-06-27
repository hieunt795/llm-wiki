---
title: Equity Repo Mechanics
aliases:
- Repo cổ phiếu
- Stock Repo
type: mechanism
tags:
- equity
- repo
- microstructure
- derivatives
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Salih Neftci
provenance: Principles_of_Financial_Engineering_Neftci.md
thesis: Equity repos are repurchase agreements using stocks as collateral, which face
  higher operational complexity than bond repos due to non-homogeneous corporate actions
  and significantly higher price volatility.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 160
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis
[RAW] Việc sử dụng cổ phiếu làm tài sản đảm bảo trong Repo (Equity Repo) mang lại lợi suất (yield) cao hơn cho người cho vay nhưng đồng thời yêu cầu một hạ tầng quản trị rủi ro và pháp lý khắt khe hơn so với trái phiếu chính phủ.

## 1. Technical Hurdles (Ranh giới kỹ thuật)
[RAW] Neftci bóc tách 4 khó khăn cốt lõi khiến Equity Repo kém lỏng hơn Bond Repo:
1.  **Non-homogeneous Payouts:** Trái phiếu trả coupon đồng nhất và dễ dự báo. Cổ phiếu có cổ tức (dividends), quyền mua (rights issues), và các sự kiện M&A phức tạp đòi hỏi sự điều chỉnh hợp đồng liên tục.
2.  **Portfolio Aggregation:** Rất khó để tìm đủ khối lượng lớn (e.g., $100 triệu) của một mã cổ phiếu duy nhất để repo. Thay vào đó, người ta phải gom một danh mục (portfolio), làm tăng tính tùy biến và giảm tính thanh khoản của hợp đồng.
3.  **High Volatility:** Cổ phiếu biến động mạnh hơn trái phiếu, dẫn đến việc gọi ký quỹ (Margin Calls) diễn ra thường xuyên hơn.
4.  **Lack of Standardization:** Chưa có một chuẩn mực toàn cầu như GMRA cho trái phiếu. Thông thường phải sử dụng "Equity Annex" đi kèm.

## 2. Worked Example: Yield Advantage
[RAW] Dữ liệu thực tế cho thấy sự chênh lệch lợi suất:
- **Agency Repos (Trái phiếu chính phủ):** Lãi suất khoảng 11 bps.
- **Equity-backed Repos:** Lãi suất có thể lên tới 35 bps.
- **Haircuts:** Mức chiết khấu (discount) cho cổ phiếu thường ổn định ở khoảng 8%, cao hơn nhiều so với mức 0-1% của trái phiếu chính phủ, để bù đắp cho rủi ro biến động giá đột ngột.

## 3. Boundary Conditions & Risks
- **Fire Sale Risk:** Trong điều kiện thị trường hoảng loạn, việc Dealer vỡ nợ có thể kích hoạt làn sóng bán tháo (fire-sales) cổ phiếu cầm cố, gây sụp đổ thanh khoản dây chuyền.
- **Liquidity Mismatch:** Trong khi tiền mặt là thanh khoản tức thời, tài sản đảm bảo cổ phiếu có thể trở nên không thể thanh lý (illiquid) ngay khi cần.

## Related
- [[Repurchase_Agreement_Mechanism]] — Nền tảng Repo chung.
- [[Short_Selling_Market_Microstructure]] — Ứng dụng chính của mượn cổ phiếu.
- [[Equity_Swap_Engineering]] — Giải pháp thay thế phi tiền mặt.
- [[Futures_Basis_And_Implied_Repo_Rate]]
- [[Basis_Trade_Mechanics]]
- [[Cross_Currency_Repo]]
- [[Repo_Market_Crisis_Dynamics]]
