---
title: Treasury Debt Management Strategy
aliases:
- Debt Management
- TBAC
- Bills vs Coupons
- WAM Targeting
- Regular and Predictable
- Debt Management Office
type: mechanism
tags:
- fiscal-policy
- treasury-market
- yield-curve
- debt-management
status: verified
confidence: 4
half_life_years: 5
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Darrell Duffie | John H. Cochrane"
provenance: "TBAC framework; Cochrane (2026-02-17); LLM-E for H1 2026 specifics"
thesis: "Quản lý nợ Kho bạc là quy trình tối ưu hóa chi phí tài chính dài hạn thông qua
  lựa chọn kỳ hạn (bills vs coupons), quy mô đấu thầu, và tần suất phát hành. Nguyên
  tắc cốt lõi là 'regular and predictable' nhằm duy trì thanh khoản thị trường. Trong
  H1 2026, Bessent đang cân bằng giữa ổn định coupon sizes và linh hoạt bills trong
  bối cảnh OBBBA mở rộng dư địa vay và Warsh áp lực phân quyền maturity risk."
source_refs:
- file: "RAW-CLIP: Cochrane (2026-02-17)"
  page: 1
created: '2026-06-29'
updated: '2026-06-29'
---

## Thesis

Quản lý nợ của Treasury là độc lập với chính sách tiền tệ về mặt pháp lý nhưng không thể tách rời về mặt thị trường. Quyết định phát hành bills hay bonds xác định ai gánh rủi ro lãi suất (rollover risk với bills; duration risk với bonds), và gián tiếp ảnh hưởng đến cả reserve supply (qua TGA) lẫn term premium (qua cung duration). Đây là lý do Cochrane-Warsh lập luận rằng Treasury, không phải Fed, nên sở hữu maturity structure decision.

## 1. Mục Tiêu và Khung Hoạt Động

### Mục tiêu TBAC (Treasury Borrowing Advisory Committee)

TBAC là hội đồng tư vấn tư nhân (primary dealers, asset managers) gặp hàng quý trước mỗi refunding announcement. Khuyến nghị cốt lõi:

- **Regular and predictable**: Auction sizes thay đổi chậm và được thông báo trước — giảm bất định, duy trì thanh khoản thị trường
- **Bills target**: 15–20% tổng nợ khả thị — đủ linh hoạt ngắn hạn nhưng không quá nhiều rollover risk
- **WAM target**: Không cố định nhưng ngầm định >6 năm để giảm refinancing risk dài hạn
- **Diversification**: Duy trì TIPS (lạm phát hedge), FRNs (floating demand), CMBs (cash management flexibility)

### Bốn loại phát hành

| Loại | Kỳ hạn | Tần suất | Vai trò |
|------|--------|----------|---------|
| **T-bills** | 4W / 8W / 13W / 26W / 52W | Hàng tuần | Thanh khoản ngắn hạn; money market anchor |
| **CMBs** (Cash Mgmt Bills) | Ad hoc <4W | Khi cần | Bù peak cash needs; extraordinary measures |
| **Notes** | 2Y / 3Y / 5Y / 7Y / 10Y | Hàng tháng (mid-month settle) | Bulk of financing; institutional demand |
| **Bonds** | 20Y / 30Y | Hàng tháng | Long-duration; pension/insurance habitat |
| **TIPS** | 5Y / 10Y / 20Y / 30Y | Hàng quý | Inflation hedge; broadens investor base |
| **FRNs** | 2Y (floating) | Hàng quý | Floating-rate demand; SOFR-linked since 2014 |

### Lịch refunding (Quarterly Cycle)

Tháng 2 (Q1) → Tháng 5 (Q2) → Tháng 8 (Q3) → Tháng 11 (Q4): Treasury công bố sizes cho các coupon auctions quý tiếp theo. Đây là event lớn nhất cho đường cong — surprise về sizes gây bear/bull move tức thì.

## 2. Bills vs Coupons — Trade-off Cốt Lõi

### Bills-heavy: Ưu và Nhược

**Ưu:**
- Rollover linh hoạt: điều chỉnh nhanh theo cash needs
- Cung cao → Fed có thể mua T-bills qua RMP (neutral)
- Tương đối ít ảnh hưởng term premium (không có duration)

**Nhược:**
- Rollover risk: $5.5–6T/năm phải rollover trong <1 năm [LLM-E]
- Nhạy cảm với SOFR spike: bills settle qua Fedwire → TGA thu tiền → reserves hút
- Nếu SOFR tăng đột ngột, chi phí rollover tăng ngay

### Coupons-heavy: Ưu và Nhược

**Ưu:**
- Refinancing risk giảm: khóa lãi suất dài hạn
- WAM tăng → ít re-pricing risk trong ngắn hạn

**Nhược:**
- Mỗi coupon auction thêm supply duration → term premium tăng
- Chi phí coupon cố định cao hơn bills trong môi trường thắt chặt

**Điểm cân bằng Bessent H1 2026:** Duy trì coupon sizes ổn định (không ramp mạnh), dùng bills linh hoạt cho nhu cầu incremental. Phù hợp TBAC principle nhưng tổng supply vẫn tăng $249B YoY [RAW-OFFICIAL: Treasury Q2 2026 Refunding].

## 3. Extraordinary Measures và Giai Đoạn Bình Thường Hóa

Khi tiếp cận trần nợ, Treasury dùng "extraordinary measures" — hoán đổi kế toán nội bộ để tạo dư địa vay tạm thời. Hệ quả với thị trường:

1. **Bills bị hạn chế**: Treasury không thể net-issue bills mới → supply giảm → bill yields tạm thời giảm bất thường
2. **Coupon sizes frozen**: Không thể tăng coupon auction sizes dù nhu cầu vốn lớn
3. **Post-ceiling normalization**: Khi OBBBA nâng ceiling $41.1T, Treasury phải:
   - Rebuild TGA từ thấp về target (~$750-850B)
   - Ramp bill issuance trở lại
   - Dần tăng coupon sizes
   → Cú "flood" supply sau hạn hẹp là đặc trưng của post-extraordinary-measures periods

H1 2026 là giai đoạn bình thường hóa này: $683B gross H1 (+$249B YoY) [RAW-OFFICIAL] là hệ quả trực tiếp.

## 4. Warsh "New Accord" — Phân Quyền Maturity Structure

Cochrane-Warsh (Feb 2026) [WEB-2026-02-17: Cochrane] lập luận: Treasury nên chủ động sở hữu maturity structure, không để Fed làm proxy qua QE duration extraction. Hàm ý:

- Nếu Treasury muốn bảo hiểm lãi suất (refinancing risk thấp) → tự phát hành bonds dài hạn, không dựa vào Fed mua bonds để giữ long yields thấp
- Nếu Fed chuyển sang bills-only RMP → duration extraction chấm dứt → Treasury không thể tiếp tục phát hành bonds kỳ vọng Fed hỗ trợ term premium thấp
- Kết quả: buộc Treasury rethink maturity structure decision trên cơ sở chi phí thị trường thực sự

Đây là sự thay đổi framework quan trọng nếu được triển khai: Treasury chịu trách nhiệm hoàn toàn cho đường cong, không còn chia sẻ với Fed qua danh mục QE.

## 5. Buyback Program

Treasury re-launched buyback program (2024, tiếp tục 2026 [LLM-E]) với hai mục tiêu:
1. **Thanh khoản**: Mua lại off-the-run securities → tập trung thanh khoản vào on-the-run → cải thiện bid-to-cover các phiên tiếp theo
2. **Cash management**: Buyback coupon bonds bằng tiền từ new bill issuance → WAM điều chỉnh linh hoạt

Quy mô nhỏ ($3–5B/phiên) nhưng signal quan trọng về Treasury's liquidity management intentions.

## Evidence / Source Anchors

- TBAC recommendation framework: [LLM-ref: TBAC quarterly reports — cần ingest]
- Maturity structure ownership — Warsh/Cochrane framework: [[Fed_Treasury_Accord_1951_And_Warsh_Proposal]] [WEB-2026-02-17]
- Gross H1 borrowing $683B: [RAW-OFFICIAL: Treasury Q2 2026 Refunding]
- Extraordinary measures mechanics: [LLM-E — cần ingest Treasury MSPD]
- H1 2026 yields, WAM estimates: [LLM-E — cần ingest FRED + MSPD]

## Related

- [[Treasury_General_Account_Mechanism]] — TGA là outcome của issuance strategy
- [[Fed_Treasury_Accord_1951_And_Warsh_Proposal]] — Institutional framework Warsh
- [[Fed_Duration_Extraction_Term_Premium]] — Fed's historical role offsetting Treasury supply
- [[TOMO_Reserve_Supply_Sterilization]] — Fed's response to TGA-driven reserve volatility
- [[Term_Risk_Premium_Mechanics]] — Term premium = market cost of Treasury's duration supply
- [[Preferred_Habitat_Market_Distortions]] — Who absorbs Treasury supply by maturity
