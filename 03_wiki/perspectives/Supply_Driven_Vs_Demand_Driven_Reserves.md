---
title: Supply-Driven vs Demand-Driven Ample Reserves
aliases:
- Supply-driven reserves
- Demand-driven reserves
- Reserve ampleness approaches
- BoE STR demand-driven
type: perspective
tags:
- central-banking
- liquidity
- monetary-operations
- fed
- comparative
status: reviewed
confidence: 4
half_life_years: 6
school: ''
superseded_by: null
superseded_date: null
expert_lens: Darrell Duffie | Isabel Schnabel | Roberto Perli
provenance: "[RAW-BOOK: Duffie BPEA 2026 — The Payment System Puts a Floor on the Fed's Balance Sheet]"
thesis: Hai cách đạt 'ample reserves'. SUPPLY-DRIVEN giữ cung reserves dư an toàn để ngân hàng không phải chạm facility Fed → lãi ổn định nhưng bảng cân đối lớn. DEMAND-DRIVEN giữ cung nhỏ hơn, chấp nhận biến động repo, buộc ngân hàng dùng facility Fed (SRP) như công cụ thanh khoản hàng ngày → bảng cân đối nhỏ hơn nhưng cần stigma tan biến. Fed H1 2026 đang ở giữa hai cực; BoE (STR) thành công với demand-driven; ECB dự định demand-driven.
source_refs:
- file: Duffie_BPEA_Payments_Liquidity_2026.md
created: '2026-06-27'
updated: '2026-06-27'
---

# [[Supply_Driven_Vs_Demand_Driven_Reserves]]

## Thesis

Cả hai đều nhắm "ample reserves" (lãi thị trường chủ yếu do administered rates dẫn dắt), nhưng khác về **ai cấp thanh khoản biên**. [RAW-BOOK: Duffie BPEA 2026]

| | **Supply-driven** | **Demand-driven** |
|---|---|---|
| Cung reserves | Dư, thận trọng | Nhỏ hơn, sát nhu cầu |
| Biên thanh khoản từ | Stock reserves sẵn có | Facility Fed (SRP) dùng hàng ngày |
| Repo volatility | Thấp, mượt | Chấp nhận biến động từng đợt |
| Bảng cân đối Fed | Lớn | Nhỏ hơn |
| Điều kiện cần | — | **Stigma phải tan** (Schnabel: facility là công cụ quản lý thanh khoản hằng ngày, được supervisor công nhận) |
| Rủi ro | Interest expense lớn, ratchet effect, footprint | Liquidity crunch từng đợt nếu stigma còn |

---

## 1. Quan điểm các bên

- **Gagnon-Sack (2020):** ủng hộ supply-driven — ngân hàng arbitrage IORB↔repo trơn tru, gần như không rủi ro crunch; ngân hàng khỏi "đào ghế sofa tìm tiền" (ẩn dụ Waller 2/2026).
- **Schnabel (ECB, 11/2025):** demand-driven — operations "không phải backstop, mà để ngân hàng dùng hằng ngày"; dealer bank càng kết nối nhiều với facility → repo càng ít spike.
- **Perli / Remache (NY Fed):** "một chút biến động repo là không sao, thậm chí có ích để thị trường phát tín hiệu" — nhưng nếu funding cost quá biến động → nguy cơ forced liquidation các vị thế UST financed bằng repo → bất ổn thị trường UST.

---

## 2. Bằng chứng so sánh quốc tế

- **BoE (demand-driven, thành công):** QT giảm sterling reserves từ đỉnh ~£1,000B (cuối 2021) còn **£646B (1/2026)**; repo gilt cao/biến động hơn nhưng draw từ **Short Term Repo (STR)** tăng vọt — lớn hơn nhiều (cả tuyệt đối) so với SRP của Fed. STR: full-allotment, kỳ hạn **1 tuần** ở Bank Rate (ít stigma hơn overnight IORB+10bp của Fed).
- **ECB:** vẫn dồi dào nhưng kế hoạch thu hẹp theo demand-driven.
- **Fed (hybrid H1 2026):** vừa khuyến khích dùng SRP, vừa dùng [[Reserve_Management_Purchases_RMP]] để kìm biến động. SRP cuối 2025: $50B (31/10) và $75B (31/12) — "cơ sở để lạc quan" rằng demand-driven khả thi.

---

## 3. Công cụ chuyển tiếp: TOMO

Duffie đề xuất **temporary open market operations (TOMO)** sterilize cú sốc cung reserves (TGA, FIMA reverse repo pool, FBO window-dressing cuối quý) như cầu nối: cho phép đường reserves *thấp và trơn hơn*, bổ trợ cả hai cách tiếp cận. Nhược điểm: TOMO làm giảm biến động → giảm động lực dùng SRP → có thể trì hoãn việc stigma tan. Giải pháp: kết hợp TOMO với hạ dần đường reserves trung bình.

> **Nghịch lý demand-driven:** để stigma tan cần dùng SRP nhiều; để dùng SRP nhiều cần chấp nhận biến động repo; nhưng biến động có thể bùng thành crunch khiến Fed buộc phải bơm reserves lại → phá cam kết demand-driven.

---

## Related

- [[Payment_System_Floor_On_Fed_Balance_Sheet]] — sàn quyết định cung reserves tối thiểu.
- [[Standing_Repo_Facility_SRF_Mechanics]] — SRP là công cụ biên của demand-driven.
- [[Reserve_Management_Purchases_RMP]] — Fed hybrid: bơm trend kìm biến động.
- [[Tiered_Reserve_Remuneration]] — công cụ giảm cầu reserves, hỗ trợ demand-driven.
- [[Central_Bank_Balance_Sheet_Trilemma]] — đánh đổi vol/footprint/intervention.
