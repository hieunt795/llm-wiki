---
title: Receipt-Reactive Payment Throttling
aliases:
- Payment Throttling
- Receipt-Reactive Payments
- Self-fulfilling Payment Delay
- Payment Gridlock Feedback
type: mechanism
tags:
- payment-systems
- liquidity
- fed
- money-market
- repo
status: reviewed
confidence: 4
half_life_years: 6
school: ''
superseded_by: null
superseded_date: null
expert_lens: Darrell Duffie
provenance: "[RAW-BOOK: Duffie BPEA 2026 — The Payment System Puts a Floor on the Fed's Balance Sheet]"
thesis: Khi reserves khan, ngân hàng lớn 'throttle' (làm chậm) thanh toán ra để chờ thanh toán vào — hành vi receipt-reactive. Vì nhiều ngân hàng cùng làm, phát sinh kỳ vọng tự thỏa mãn về độ trễ → shadow price của reserves vọt → repo rate bật trên IORB, có thể đột ngột (gridlock). Đây là cơ chế vi mô biến nhu cầu thanh toán thành sàn cứng cho bảng cân đối Fed, và là predictor định lượng của SOFR–IORB spread.
source_refs:
- file: Duffie_BPEA_Payments_Liquidity_2026.md
created: '2026-06-27'
updated: '2026-06-27'
---

# [[Receipt_Reactive_Payment_Throttling]]

## Thesis

Trên Fedwire (RTGS), thời điểm thanh toán ra của ngân hàng lớn **nhạy với thanh toán vào gần đây** (receipt-reactive). Khi GSIB lo không đủ reserves để vừa thanh toán ra vừa đáp ứng yêu cầu thanh khoản nội ngày, họ **làm chậm** thanh toán ra để chờ tiền vào. Nhiều ngân hàng cùng chờ → **gridlock** + kỳ vọng tự thỏa mãn rằng tiền vào sẽ còn trễ hơn → shadow cost của reserves nhảy vọt. [RAW-BOOK: Duffie BPEA 2026; Bech-Garratt 2003; McAndrews-Potter 2002]

---

## 1. Bằng chứng định lượng (Duffie / Copeland-Duffie-Yang 2025)

- **Reaction function (Tobit, Afonso et al 2022):** lượng thanh toán vào trong 15 phút trước dự báo lượng thanh toán ra phút kế tiếp; **độ phụ thuộc này CAO hơn hẳn khi tổng reserves của ngân hàng lớn thấp**.
- **Payment-delay → repo spread:** với 10 "dealer bank" hoạt động repo nhất, khi opening balance thấp + thanh toán vào đến trễ hơn thường → họ chỉ cho vay ở repo rate cao. Tăng 1 độ lệch chuẩn *trailing payment delay* → **+7bp SOFR–IORB** (OLS).
- **Chỉ thanh toán LỚN mới gây stress:** thanh toán <$100M gần như tự net (vào bù ra); LSM thiết kế để net các thanh toán lớn. Xem [[Liquidity_Savings_Mechanism_LSM]].

---

## 2. Các đỉnh lịch sử (payment delay khớp với repo spike)

| Ngày | Payment delay | SOFR–IORB |
|---|---|---|
| **17/09/2019** | lớn nhất mẫu 10 năm; reserves chạm đáy | **+315bp** (interdealer ~+1000bp) |
| **17/03/2020 (COVID)** | đỉnh thứ nhì | **+44bp** |

Payment-delay metric biến thiên ~250 phút (đỉnh–đáy) giữa 2015–2/2026, **tăng có hệ thống trong cả 2 chu kỳ QT** (9/2017–9/2019 và 6/2022–12/2025).

---

## 3. Vì sao điều này tạo sàn cho bảng cân đối Fed

GSIB **ngại daylight overdraft** (sợ supervisor đọc là vi phạm tự chủ thanh khoản — xem [[Intraday_Liquidity_Regulation_Reserve_Demand]]) → cầu reserves **kém co giãn** tới mức opening balance + thanh toán vào đủ để xử lý thanh toán ra mà không chạm Fed. Dưới mức đó, dealer chỉ cấp vốn ở lãi cao hơn IORB → đây chính là sàn của [[Payment_System_Floor_On_Fed_Balance_Sheet]].

---

## 4. Ranh giới (Boundary)

- **Phi tuyến, đuôi dày:** spike có thể đến "với rất ít cảnh báo" (17/09/2019) — Poole curve không trượt mượt (xem [[Poole_Curve_Reserve_Demand]]).
- **Giảm nhẹ bằng:** LSM (net thanh toán), TOMO (làm trơn cung reserves), hoặc đơn giản là giữ reserves dồi dào hơn (đánh đổi với bảng cân đối lớn).

---

## Related

- [[Payment_System_Floor_On_Fed_Balance_Sheet]] — sàn mà cơ chế này làm "binding".
- [[SOFR_IORB_Spread_Stress_Gauge]] — output đo được của throttling.
- [[Liquidity_Savings_Mechanism_LSM]] — giải pháp net thanh toán lớn.
- [[Intraday_Credit_and_Liquidity_Gridlock]] — khung gridlock tổng quát.
- [[RTGS_Intraday_Liquidity_Mechanism]] — cơ chế RTGS nền.
- [[Repo_Spike_September_2019_Case_Study]] — case minh họa cực đoan.
