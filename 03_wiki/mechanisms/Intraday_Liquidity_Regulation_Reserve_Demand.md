---
title: Intraday Liquidity Regulation & Reserve Demand (Reg YY)
aliases:
- Reg YY reserve demand
- Regulation YY liquidity
- Liquidity regulation reserve demand
- Daylight overdraft aversion
type: mechanism
tags:
- regulation
- liquidity
- central-banking
- fed
- bank-treasury
status: reviewed
confidence: 4
half_life_years: 6
school: ''
superseded_by: null
superseded_date: null
expert_lens: Darrell Duffie | Randall Quarles | Bill Nelson
provenance: "[RAW-BOOK: Duffie BPEA 2026 — The Payment System Puts a Floor on the Fed's Balance Sheet]"
thesis: Liquidity regulation hậu-GFC (Reg YY, CLAR, RLAP) buộc GSIB tự chủ thanh khoản nội ngày → giảm động lực dùng nguồn Fed (daylight overdraft, Discount Window, SRP) và tạo 'preference' của supervisor cho việc đáp ứng yêu cầu bằng RESERVES hơn là Treasuries. Hệ quả không chủ đích: cầu reserves cấu trúc tăng hàng trăm tỷ USD, nâng sàn bảng cân đối Fed. Daylight overdraft toàn hệ thống tụt từ ~$120B (10 ngân hàng lớn, 2007) còn <$5B (toàn hệ thống, 2025).
source_refs:
- file: Duffie_BPEA_Payments_Liquidity_2026.md
created: '2026-06-27'
updated: '2026-06-27'
---

# [[Intraday_Liquidity_Regulation_Reserve_Demand]]

## Thesis

Quy chế thanh khoản hậu-GFC yêu cầu GSIB chứng minh tự đáp ứng nhu cầu thanh khoản từ nguồn riêng. Tác dụng phụ: ngân hàng **ngại chạm facility Fed** (vì bị đọc là không tự chủ) và supervisor **ưu tiên reserves hơn Treasuries** trong việc thỏa mãn yêu cầu thanh khoản → **cầu reserves cấu trúc phình to**, là một trong những lý do chính của sàn [[Payment_System_Floor_On_Fed_Balance_Sheet]]. [RAW-BOOK: Duffie BPEA 2026]

---

## 1. Bộ khung quy chế

- **Reg YY (Enhanced Prudential Standards):** GSIB phải đo/quản lý gross liquidity inflow-outflow nội ngày, prioritize nghĩa vụ time-specific. Poll 2026 (Nelson): 2 yếu tố lớn nhất đẩy cầu reserves là (a) liquidity risk management và (b) đáp ứng Reg YY.
- **CLAR (Comprehensive Liquidity Analysis & Review)** + **LISCC supervision:** ưu tiên reserves vì là thanh khoản tức thì; chuyển securities thành tiền mất thời gian.
- **RLAP (Resolution Liquidity Adequacy & Positioning):** yêu cầu thanh khoản nội ngày cho kịch bản đổ vỡ — ILST giả định discount lớn trên Treasuries thanh lý khối lượng lớn → Treasuries **không** được coi cash-equivalent cho resolution.

---

## 2. "Red line" của Dimon (bằng chứng vi mô)

JPMorgan (2019, sau repo crunch): "$120B trong tài khoản Fed, xuống $60B rồi về $120B trong ngày... yêu cầu CLAR + resolution là balance không được chạm 0 dù có stress cực đoan trong ngày." → giải thích vì sao JPM **không** arbitrage repo rate cao bằng reserves: với mục đích quy chế, họ định giá reserves cao hơn hẳn Treasuries dù quy chế coi 2 thứ "tương đương HQLA" (Quarles).

> **Quarles:** chính *supervisory policy* (đặt "ngón tay nặng" lên việc ưu tiên reserves hơn Treasuries), chứ không hẳn *regulation*, là driver của disruption 2019.

---

## 3. Daylight overdraft: từ $120B xuống <$5B

- Pre-GFC: 10 ngân hàng lớn nhất overdraft ~$120B/ngày (hệ thống còn nhỏ hơn nhiều).
- 2025: peak daylight overdraft toàn hệ thống <$5B/ngày — dù reserves không dồi dào. GSIB tránh né vì sợ supervisor đọc là vi phạm tự chủ thanh khoản. Peak overdraft tương quan chặt với opening balance (R²=0.57); đạt đỉnh đúng kỳ chứa crunch 9/2019.
- Duffie (Duffie-Singh-Wang 2026): nếu ngân hàng coi daylight overdraft *bình thường, chi phí thấp* → reserves cần cho thanh toán có thể giảm mạnh (mức tăng overdraft nhỏ hơn nhiều mức giảm opening balance).

---

## 4. Cải cách & nghịch lý stigma

- **2024 clarification:** Fed cho phép GSIB tính *borrowing capacity* tại Discount Window + SRF vào nguồn thanh khoản Reg YY, tới mức HLA collateral đã ký quỹ. Nelson (2026a): mở rộng (gồm cả non-HLA collateral) sẽ giảm precautionary demand cho reserves — nhưng "cần thiết kế thận trọng".
- **Cảnh báo Nelson:** nếu ngân hàng không chịu vay Discount Window trừ khi cực kỳ căng, *tính capacity là nguồn thanh khoản sẽ phản tác dụng* (các bước tránh vay — fire-sale, rút cho vay — chính là cách lan truyền stress).
- **Chicken-or-egg stigma:** mỗi GSIB chỉ thấy stigma giảm sau khi GSIB khác đã chủ động dùng facility Fed.

---

## Related

- [[Payment_System_Floor_On_Fed_Balance_Sheet]] — reg-driven demand là cấu phần của sàn.
- [[Receipt_Reactive_Payment_Throttling]] — ngại overdraft → throttle thanh toán.
- [[Standing_Repo_Facility_SRF_Mechanics]] — facility bị stigma + ràng buộc vốn.
- [[Intraday_Overdraft]] — cơ chế daylight overdraft.
- [[Liquidity_Coverage_Ratio]] — quy chế HQLA liên quan.
- [[Supply_Driven_Vs_Demand_Driven_Reserves]] — nới reg = hạ sàn, hỗ trợ demand-driven.
