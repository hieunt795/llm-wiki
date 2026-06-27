---
title: Tiered Remuneration of Reserves
aliases:
- Tiered reserve remuneration
- Two-tier IORB
- Reserve remuneration tiering
- Quota reserve remuneration
type: mechanism
tags:
- central-banking
- monetary-operations
- liquidity
- interest-rates
status: reviewed
confidence: 4
half_life_years: 8
school: ''
superseded_by: null
superseded_date: null
expert_lens: Darrell Duffie | Roc Armenter
provenance: "[RAW-BOOK: Duffie BPEA 2026 — The Payment System Puts a Floor on the Fed's Balance Sheet]"
thesis: Tiering trả lãi reserves theo quota — lãi cao (≈policy rate) cho balance đến quota, lãi thấp cho phần vượt quota — nhằm khôi phục động lực cho ngân hàng dư reserves cho vay ngân hàng thiếu, bất chấp ma sát (capital, FDIC fee). Lý thuyết (Duffie-Sornwanee-Spizzuocco 2026): two-tier tối thiểu hóa interest expense của NHTW; thực nghiệm (Na Uy, New Zealand): tăng mạnh volume liên ngân hàng và cho phép thu nhỏ bảng cân đối mà giữ lãi ổn định. Là công cụ #4 trong menu hạ sàn cầu reserves của Duffie.
source_refs:
- file: Duffie_BPEA_Payments_Liquidity_2026.md
created: '2026-06-27'
updated: '2026-06-27'
---

# [[Tiered_Reserve_Remuneration]]

## Thesis

Khi có ma sát liên ngân hàng (capital requirement, FDIC fee tới 42bp + 13bp hậu SVB), ngân hàng dư reserves thà giữ kiếm IORB còn hơn cho ngân hàng thiếu vay → reserves phân bổ sai → đẩy cầu tổng reserves lên. **Tiering** sửa điều này: lãi cao đến quota, lãi thấp vượt quota, với chênh hai bậc ≥ tổng ma sát cho vay → ngân hàng dư reserves lại có động lực cho vay. [RAW-BOOK: Duffie BPEA 2026]

---

## 1. Lý thuyết (Duffie-Sornwanee-Spizzuocco 2026)

- NHTW chọn target lãi liên ngân hàng `i`, rồi chọn tổng reserves `b` + biểu lãi `ρ(x)` sao cho thị trường clear ở `i`.
- **Kết quả:** với ràng buộc biểu lãi không tăng, **two-tier** chính là phương án **tối thiểu hóa tổng interest expense** của NHTW (gần bằng phương án unrestricted, tốt hơn hẳn one-tier).
- Đánh đổi: để đạt cùng mức liquidity benefit, chuyển one-tier → two-tier giảm đáng kể reserves cần + interest expense + tăng volume liên ngân hàng. Chuyển two-tier → unrestricted lợi thêm ít.

---

## 2. Bằng chứng thực nghiệm

- **Na Uy (Norges Bank, 10/2011):** đổi single→two-tier → **volume liên ngân hàng overnight tăng vọt** (Akram-Findreng 2021; Baughman-Carapella 2019: tiering tăng interbank lending).
- **New Zealand (RBNZ, 2007):** tiering để "chỉ thỏa mãn cầu balance cho mục đích thanh toán, không cho đầu cơ" → **giảm tổng settlement balance mà giữ lãi overnight ổn định** (Bowman-Gagnon-Leahy 2010).
- **Mỹ (2008, ngắn ngủi):** Fed từng áp two-tier (required vs excess) trong 2008 dưới luật hiện hành → cho thấy **không cần luật mới**; nhưng đến 12/2008, qua ZLB+QE, gộp về một bậc và giữ vậy đến nay.

---

## 3. Rào cản triển khai (Duffie §VIII)

- **Xác định quota cho từng loại ngân hàng:** cách "voluntary reserves targeting" (Interest on Reserves Workgroup 2008) cho ngân hàng tự chọn quota với incentive chống gian lận — nhưng chưa được kiểm chứng.
- **Thuyết phục các bên:** ngành ngân hàng sẽ tham gia mạnh vì ảnh hưởng lợi nhuận (lãi reserves là pass-through từ Treasury qua ngân hàng — Waller 2025).
- Là **dự án nhiều năm**, khó truyền thông; xếp sau TOMO và nới liquidity reg trong thứ tự ưu tiên.

---

## Related

- [[Payment_System_Floor_On_Fed_Balance_Sheet]] — tiering hạ sàn cầu reserves.
- [[Supply_Driven_Vs_Demand_Driven_Reserves]] — tiering hỗ trợ demand-driven.
- [[Liquidity_Savings_Mechanism_LSM]] — công cụ hạ sàn song song.
- [[Optimal_Interest_Rate_Corridor_Width]] — quan hệ administered rates ↔ thị trường.
- [[Demand_for_Central_Bank_Reserves]] — khung cầu reserves (Bindseil).
