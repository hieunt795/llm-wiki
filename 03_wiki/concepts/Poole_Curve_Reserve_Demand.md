---
title: Poole Curve (Reserve Demand Curve)
aliases:
- Poole Curve
- Reserve demand curve
- Reserve demand function
- Ample reserves kink
type: concept
tags:
- central-banking
- liquidity
- monetary-operations
- fed
status: reviewed
confidence: 4
half_life_years: 8
school: ''
superseded_by: null
superseded_date: null
expert_lens: Darrell Duffie | Randall Quarles
provenance: "[RAW-BOOK: Duffie BPEA 2026 — The Payment System Puts a Floor on the Fed's Balance Sheet]"
thesis: "'Poole Curve' (cách dùng hiện đại) là đường cầu reserves: ánh xạ tổng reserves → spread lãi thị trường so với administered rate. Phẳng khi reserves abundant (lãi do IORB dẫn), dốc xuống dần khi reserves giảm về 'ample', dốc đứng khi 'scarce'. Vấn đề cốt lõi: độ dốc KHÔNG trượt mượt — có thể nhảy đột ngột (self-fulfilling) như 17/09/2019 khi reserves chạm ~$1.4T và SOFR–IORB vọt 315bp. Lưu ý: KHÁC với [[Poole_Model]] (Poole 1968, chọn công cụ tiền/lãi theo biến động IS-LM)."
source_refs:
- file: Duffie_BPEA_Payments_Liquidity_2026.md
created: '2026-06-27'
updated: '2026-06-27'
---

# [[Poole_Curve_Reserve_Demand]]

## Thesis

> ⚠️ **Disambiguation:** "Poole Curve" ở đây là **đường cầu reserves hiện đại** (Afonso et al; Duffie 2026), không phải mô hình chọn công cụ chính sách của Poole (1968) — xem [[Poole_Model]]. Cùng tên Poole, hai khái niệm khác nhau.

Đường cầu reserves ánh xạ **tổng reserves → spread lãi thị trường vs administered rate** (vd SOFR–IORB). Ba vùng: **Abundant** (phẳng, lãi do IORB dẫn, không cần quản lý cung) → **Ample** (dốc xuống vừa phải) → **Scarce** (dốc đứng). FOMC nhắm "ample" = mức tối thiểu mà lãi vẫn chủ yếu do administered rates dẫn dắt. [RAW-BOOK: Duffie BPEA 2026; Poole 1968; Afonso et al 2025]

---

## 1. Vấn đề: đường cong không trượt mượt

Lý tưởng: khi reserves giảm dần về ~$1.4T (9/2019), SOFR–IORB tăng mượt theo Poole curve → tín hiệu cho FOMC biết đã chạm "ample" để dừng QT. **Thực tế:** khi reserves chạm $1.4T → **liquidity crunch**. 17/09/2019, SOFR–IORB vọt **315bp** (interdealer repo ~+1000bp) gần như không báo trước.

- Cơ chế: dealer bank rơi vào **kỳ vọng tự thỏa mãn** rằng thanh toán vào sẽ trễ → shadow cost reserves nhảy bậc → đường cong "nhảy" lên một segment cao hơn ở mức balance <$1.4T (xem [[Receipt_Reactive_Payment_Throttling]]).
- 5bp (11/09/2019) → 315bp (17/09/2019): minh chứng độ dốc/đuôi cực kỳ nhạy với reserves, nhất là balance của các dealer lớn nhất.

---

## 2. Hệ quả chính sách

- **Không thể dựa vào độ dốc làm tín hiệu** "đã đến ample" — vì nó có thể không trượt đủ chậm.
- **Quarles:** sau 2019, FOMC chuyển từ "thu nhỏ đến sát kink" sang "giữ đệm dày, đừng bao giờ đến gần kink nữa" → thiên về supply-driven, bảng cân đối lớn hơn.
- **Duygan-Bump & Kahn (2026):** độ nhạy của repo spread theo reserves (chuẩn hóa theo Treasuries outstanding) **thay đổi đột ngột**; có nhiều ngày độ nhạy cao → giảm reserves đến khi độ dốc "vừa phản ứng" thực ra đã **overshoot**; khi overshoot, volatility của spread cũng tăng vọt.

---

## 3. Liên hệ

Poole Curve là biểu diễn đồ thị của [[Payment_System_Floor_On_Fed_Balance_Sheet]]: "sàn" chính là vùng balance nơi đường cong bắt đầu dốc/nhảy. ONRRP đóng vai **subfloor** ở phía abundant (hút reserves thừa khi lãi rơi quá xa dưới IORB); SRP/SRF đóng vai trần ở phía scarce.

---

## Related

- [[Poole_Model]] — ⚠️ khác: mô hình chọn công cụ Poole (1968), không phải đường cầu reserves.
- [[Payment_System_Floor_On_Fed_Balance_Sheet]] — đường cong là biểu diễn của sàn này.
- [[Receipt_Reactive_Payment_Throttling]] — cơ chế khiến đường cong "nhảy".
- [[SOFR_IORB_Spread_Stress_Gauge]] — trục tung của đường cong.
- [[Repo_Spike_September_2019_Case_Study]] — cú nhảy đường cong điển hình.
- [[Demand_for_Central_Bank_Reserves]] — khung cầu reserves (Bindseil).
