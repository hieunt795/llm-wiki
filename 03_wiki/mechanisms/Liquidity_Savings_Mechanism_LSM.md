---
title: Liquidity Savings Mechanism (LSM)
aliases:
- LSM
- Liquidity Saving Mechanism
- Payment netting queue
- Fedwire LSM
type: mechanism
tags:
- payment-systems
- liquidity
- central-banking
- market-structure
status: reviewed
confidence: 4
half_life_years: 8
school: ''
superseded_by: null
superseded_date: null
expert_lens: Darrell Duffie
provenance: "[RAW-BOOK: Duffie BPEA 2026 — The Payment System Puts a Floor on the Fed's Balance Sheet]"
thesis: LSM là cơ chế trong hệ thống thanh toán giá trị lớn cho phép ngân hàng xếp hàng (queue) các thanh toán ra lớn để được NET (bù trừ) với thanh toán vào — song phương rồi đa phương theo chu kỳ — thay vì trả từ stock reserves đầu ngày. Nhờ đó giảm mạnh lượng reserves cần để vận hành thanh toán (CHAPS/BOJ-NET/Lynx tiết kiệm ~15–30%). Fedwire — hệ thống lớn nhất thế giới — KHÔNG có LSM, nên là một đòn bẩy lớn để Fed hạ sàn cầu reserves.
source_refs:
- file: Duffie_BPEA_Payments_Liquidity_2026.md
created: '2026-06-27'
updated: '2026-06-27'
---

# [[Liquidity_Savings_Mechanism_LSM]]

## Thesis

Trong RTGS thuần (như Fedwire), mỗi thanh toán trả ngay từ reserves → cần balance đầu ngày lớn. **LSM** chèn một bước net: thanh toán ra lớn được xếp hàng, hệ thống tìm các vòng (cycle) thanh toán bù trừ lẫn nhau, chỉ cần reserves cho phần *ròng*. Đây là công cụ #3 trong menu hạ sàn của Duffie ([[Payment_System_Floor_On_Fed_Balance_Sheet]]). [RAW-BOOK: Duffie BPEA 2026]

---

## 1. Cơ chế net (ví dụ Duffie)

Bank A có balance 100, cần trả B 60. Không LSM → trả ngay, còn 40.
Với LSM: A xếp hàng khoản 60. Trong chu kỳ LSM, B đã xếp trả C 50, C đã xếp trả A 55. Thuật toán phát hiện có thể xử lý **cả 3** chỉ bằng cách giảm balance A và C mỗi bên 5, tăng B 10 → **A chỉ dùng 5 reserves thay vì 60**. Cuối ngày net không đổi, nhưng *peak intraday drawdown* (L_i) giảm mạnh → ngân hàng mở ngày với ít reserves hơn.

**BOJ-NET (minh họa):** (1) thử **net song phương** A↔B trước; (2) nếu không được, thử trả bằng balance hiện có; (3) nếu không, xếp hàng. 8 lần/ngày chạy **net đa phương** tìm chuỗi thanh toán khả thi giữa nhiều ngân hàng, cắt dần khoản infeasible.

---

## 2. Bằng chứng hiệu quả quốc tế

| Hệ thống | Tiết kiệm thanh khoản / hiệu quả |
|---|---|
| **CHAPS (BoE)** | LSM giảm ~**20%** reserves cần; payment efficiency P/L >10 (vs Fedwire ~4) |
| **BOK-Wire+ (Hàn Quốc)** | ~**20%** trong 1 tháng kể từ launch |
| **BOJ-Net (Nhật)** | ~**15%** |
| **Lynx (Canada)** | efficiency 10.2 (vs 7.6 cũ); >99% thanh toán settle trong LSM |
| **CHIPS (tư nhân, Mỹ)** | net + LSM → efficiency cao; ~$2T/ngày, 95% quốc tế |

Eurosystem, UK, Nhật, Canada đều dùng LSM. **Fedwire & Fedwire Securities thì KHÔNG** (chỉ có phí trễ $0.26/message sau 5pm ET).

---

## 3. Điều kiện hiệu quả & rào cản

- **Chỉ thanh toán LỚN mới quan trọng:** thanh toán <$100M gần như tự net (vào bù ra); LSM thiết kế để net khoản lớn của ~10 dealer bank ([[Receipt_Reactive_Payment_Throttling]]).
- **Cần incentive:** ngân hàng phải chịu nhường quyền kiểm soát thời điểm thanh toán cho LSM queue (lý thuyết Martin-McAndrews 2008; Duffie-Singh-Wang 2026: nộp tối đa là weakly-dominant). Topology Fedwire: 5 ngân hàng lớn nhất = 50% volume, 10 = 60%; 80% liên kết payor-payee (value-weighted) hoàn toàn không hoạt động.
- **Chi phí triển khai:** thay software cho hệ thống thanh toán lớn nhất thế giới = dự án nhiều năm; ngân hàng lớn phải retool hệ thống nội bộ. Duffie: nên bắt đầu bằng cost-benefit analysis.

---

## Related

- [[Payment_System_Floor_On_Fed_Balance_Sheet]] — LSM hạ sàn cầu reserves.
- [[Receipt_Reactive_Payment_Throttling]] — vấn đề LSM giải quyết (net thanh toán lớn).
- [[RTGS_Intraday_Liquidity_Mechanism]] — RTGS thuần (Fedwire) đối lập với deferred net settlement.
- [[Main_RTGS_Systems]] — bản đồ hệ thống RTGS toàn cầu.
- [[Tiered_Reserve_Remuneration]] — công cụ hạ sàn bổ trợ.
