---
title: Private Equity Mechanism
aliases:
- PE Fund
- Leveraged Buyout
- LBO Mechanics
- Buyout Fund
type: mechanism
tags:
- private-equity
- alternative-assets
- capital-structure
- leverage
status: verified
confidence: 3
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Alexander Düring
provenance: LLM synthesis + Direct_Lending.md + NAV_Loans.md cross-reference
thesis: Private Equity tạo ra giá trị bằng cách sử dụng đòn bẩy tài chính (nợ từ Private
  Credit) để thâu tóm doanh nghiệp, sau đó tăng giá trị vận hành trong 5-7 năm và
  thoái vốn qua IPO/M&A. PE fund là 'khách hàng lớn nhất' và là lực kéo cầu cốt lõi
  của thị trường Private Credit.
source_refs: []
created: '2026-04-22'
updated: '2026-04-22'
---

# [[Private_Equity_Mechanism]]

## Thesis

[LLM] Private Equity (PE) là một loại hình đầu tư vốn cổ phần vào các doanh nghiệp không niêm yết, với mục tiêu tạo ra lợi nhuận vượt trội (IRR 15-25%) bằng cách kết hợp 3 đòn bẩy: đòn bẩy tài chính (Leverage), cải thiện vận hành (Operational Alpha), và mở rộng bội số định giá (Multiple Expansion). Không thể hiểu Private Equity mà không hiểu [[Private_Credit]] — vì nợ (debt) là nguyên liệu cốt lõi để PE phóng đại lợi nhuận equity.

---

## 1. Cấu Trúc Quỹ PE (Fund Structure)

[LLM] Một quỹ PE vận hành theo mô hình Limited Partnership:

| Bên tham gia | Vai trò | Đặc điểm |
|---|---|---|
| **GP (General Partner)** | Quản lý quỹ, ra quyết định đầu tư | Góp 1-2% vốn, nhận 20% profit (Carried Interest) |
| **LP (Limited Partner)** | Cung cấp vốn | Góp 98-99% vốn, nhận 80% profit |
| **Portfolio Company** | Doanh nghiệp được thâu tóm | Chịu toàn bộ nợ vay từ LBO |

- **Phí quản lý (Management Fee):** Thường 1.5-2% AUM/năm trong thời kỳ đầu tư.
- **Carried Interest:** GP nhận 20% lợi nhuận sau khi LP đã thu hồi vốn và hurdle rate (thường 8%).

---

## 2. Cơ Chế LBO (Leveraged Buyout)

[LLM] LBO là giao dịch trung tâm của ngành PE. Thay vì mua toàn bộ bằng equity, PE fund chỉ bỏ ra 30-40% equity và vay 60-70% còn lại từ [[Direct_Lending]] hoặc thị trường Syndicated Loans.

**Capital Stack của một LBO điển hình:**

| Tầng vốn | Nguồn cung cấp | Chi phí | Quyền ưu tiên |
|---|---|---|---|
| Senior Secured Debt | [[Private_Credit]] / Bank | SOFR + 500-650bps | Cao nhất |
| Unitranche | [[Direct_Lending]] fund | SOFR + 600bps (blended) | Cao |
| Mezzanine | Private Credit / Mezz fund | 12-15% (có thể PIK) | Trung bình |
| Equity (GP+LP) | PE Fund | IRR target 20%+ | Thấp nhất |

**Tại sao dùng đòn bẩy?** Nếu PE mua công ty trị giá 100 với 100% equity, lợi nhuận phụ thuộc hoàn toàn vào tăng giá trị doanh nghiệp. Nếu dùng 30 equity + 70 nợ, cùng tăng giá trị 20% thì equity tăng 67% (20/30). Đòn bẩy phóng đại lợi nhuận — nhưng cũng phóng đại thua lỗ.

---

## 3. Vòng Đời Quỹ & Quan Hệ với Private Credit

[LLM] Mối quan hệ PE-Private Credit không chỉ xảy ra tại thời điểm LBO. Nó kéo dài suốt vòng đời quỹ:

| Giai đoạn | Công cụ Private Credit liên quan | Mục đích |
|---|---|---|
| **Acquisition** | [[Direct_Lending]] — Senior/Unitranche | Tài trợ LBO |
| **Hold Period** | [[Payment_In_Kind_PIK]] — Mezzanine | Giảm cash drain cho portfolio company |
| **Late Stage** | [[NAV_Loans]] | Thanh khoản cho LP khi exit bị trì hoãn |
| **Exit** | [[Private_Credit_Secondary_Market_Mechanics]] | Bán khoản nợ trước khi thoái equity |

---

## 4. Failure Conditions

[LLM] Cấu trúc LBO thất bại khi:
1. **Interest Rate Shock:** Phần lớn nợ LBO là floating rate (SOFR-linked). Khi NHTW tăng lãi suất mạnh (như 2022-2023), chi phí nợ của portfolio companies tăng đột ngột, vượt khả năng EBITDA để trả lãi (Interest Coverage Ratio < 1x).
2. **Multiple Compression:** PE mua vào lúc thị trường định giá cao (EBITDA x12), nhưng exit lúc thị trường định giá thấp (EBITDA x8) — toàn bộ lợi nhuận từ Operational Alpha bị nuốt.
3. **Exit Market Freeze:** IPO market đóng băng, M&A activity giảm → PE fund phải dùng [[NAV_Loans]] để kéo dài, tạo ra double leverage nguy hiểm.

---

## Evidence / Source Anchors

- Cấu trúc PE-sponsored lending trong Direct Lending: [[Direct_Lending.md]]
- NAV Loans như công cụ PE late-stage liquidity: [[NAV_Loans.md]]
- ~70% PE-sponsored trong Private Credit: [[Private_Credit.md]]
- Double leverage risk (NAV + portfolio level): [LLM — cần Raw Source từ IMF GFSR 2024]

## Related

- [[Private_Credit]] — Nguồn cung cấp nợ cho LBO; PE là khách hàng lớn nhất.
- [[Direct_Lending]] — Công cụ tài trợ LBO chính trong Private Credit.
- [[NAV_Loans]] — Công cụ thanh khoản late-stage cho PE fund.
- [[Payment_In_Kind_PIK]] — Cấu trúc nợ linh hoạt trong mezzanine PE.
- [[Financial_Accelerator_Mechanism]] — Cơ chế khuếch đại rủi ro khi LBO gặp khủng hoảng.
- [[Nonbank_Financial_Intermediation]] — Taxonomy parent của PE trong hệ thống tài chính.
- [[Alternative_Investment_Funds]] — Node cha về loại hình quỹ đầu tư thay thế.
