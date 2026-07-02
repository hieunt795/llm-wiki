---
title: Payment System Puts a Floor on the Fed's Balance Sheet
aliases:
- Payment System Floor
- Reserve Demand Floor
- Duffie Balance Sheet Floor
- Floor on Fed Balance Sheet
type: mechanism
tags:
- central-banking
- liquidity
- payment-systems
- fed
- monetary-operations
- central-bank-balance-sheet
status: reviewed
confidence: 4
half_life_years: 6
school: ''
superseded_by: null
superseded_date: null
expert_lens: Darrell Duffie
provenance: "[RAW-BOOK: Duffie BPEA 2026 — The Payment System Puts a Floor on the Fed's Balance Sheet]"
thesis: Luận điểm trung tâm của Duffie (BPEA 2026): quy mô tối thiểu bảng cân đối Fed bị **chốt sàn bởi nhu cầu dự trữ của hệ thống thanh toán** — lượng reserves ngân hàng cần để thanh toán đúng hạn cho nhau trong ngày (Fedwire), cộng với reserves để tuân thủ liquidity regulations. Vì GSIB ngại dùng nguồn thanh khoản của Fed (daylight overdraft, Discount Window, SRP) do stigma + chi phí vốn, Fed không thể thu nhỏ bảng cân đối dưới sàn này mà không gây gián đoạn truyền dẫn chính sách (repo spike). Muốn nhỏ hơn → phải GIẢM CẦU reserves trước.
source_refs:
- file: Duffie_BPEA_Payments_Liquidity_2026.md
created: '2026-06-27'
updated: '2026-07-02'
---

# [[Payment_System_Floor_On_Fed_Balance_Sheet]]

## Thesis

Reserves ngân hàng hiện ~$3,000B — gấp ~300 lần mức đầu 2007 (~$10B). Vì sao? Duffie lập luận: **hệ thống thanh toán đặt một sàn cứng** lên quy mô bảng cân đối Fed. Reserves tối thiểu = lượng cần để ngân hàng thanh toán đúng hạn cho nhau trong ngày qua Fedwire **mà không phải dựa vào nguồn thanh khoản của Fed** — vì GSIB coi việc chạm Fed là tín hiệu yếu (stigma) và tốn vốn. Cộng thêm reserves để đáp ứng [[Intraday_Liquidity_Regulation_Reserve_Demand]] (Reg YY). [RAW-BOOK: Duffie BPEA 2026]

> Hệ quả: Fed đang **tăng** reserves theo nhịp cầu của hệ thống thanh toán (qua [[Reserve_Management_Purchases_RMP]]). Muốn bảng cân đối nhỏ hơn, phải **giảm cầu reserves trước**, không thể chỉ cắt cung.

---

## 1. Cơ chế: vì sao cầu reserves phình ~300 lần từ 2007

Ba động lực (Duffie §I.D):
1. **Ngại daylight overdraft:** Đầu 2007, 10 ngân hàng lớn nhất overdraft trung bình ~$120B/ngày trên Fedwire. Từ 2020, **tổng peak daylight overdraft toàn hệ thống <$5B/ngày** — GSIB tránh né vì sợ bị supervisor đọc là "không tự chủ thanh khoản" (Reg YY).
2. **Mất động lực cho vay reserves dư:** Fed trả IORB ~lãi thị trường cho mọi mức reserves → không còn động lực cho vay liên ngân hàng như thời pre-GFC (khi reserves không sinh lãi). VD: JPMorgan rút ~$350B khỏi Fed từ 2023 ($409B→$63B) để mua UST.
3. **Ma sát liên ngân hàng tăng:** FDIC insurance fee tới 42bp + special assessment 13bp (hậu SVB 2023), capital/leverage requirements cao hơn.

---

## 2. Sàn này biểu hiện thế nào (the binding evidence)

- Khi reserves tụt quá sàn → một số ngân hàng **throttle thanh toán ra** ([[Receipt_Reactive_Payment_Throttling]]) → shadow price của reserves vọt → repo rate bật trên IORB.
- **29/10/2025:** FOMC tuyên bố ngừng thu hẹp bảng cân đối — kích hoạt bởi đà nới rộng SOFR–IORB (xem [[SOFR_IORB_Spread_Stress_Gauge]]).
- **10/12/2025:** Fed khởi động RMP (~$40B reserves/tháng đến 5/2026) — *"hoàn toàn tách biệt khỏi chính sách tiền tệ"* (Powell), chỉ để giữ ample reserves.

**Cập nhật thực nghiệm (weekly H.4.1, 23 điểm, 2026-07-02):** Đáy reserves thực tế của H1 2026 là **$2,901.8B (22/04/2026)** [RAW-OFFICIAL: Fed_H41_Weekly_Flow_H1_2026.md] — **thấp hơn ~$100B** so với mốc "~$3,000B" thường được trích dẫn làm sàn ample [WEB-2026-04-11: Andreopoulos]. Đáy này rơi đúng vào mùa quyết toán thuế cá nhân (15/04): hai tuần 08/04→22/04, TGA tăng $310.1B trong khi reserves giảm $214.4B — một thí nghiệm tự nhiên khép kín xác nhận trực tiếp identity ΔReserves≈RMP−ΔTGA (residual "other factors" chỉ +$62.9B). Đối chiếu SOFR–IORB tháng 4/2026: trung bình -11bp, không có tín hiệu stress [RAW-OFFICIAL: SOFR_IORB_Spread_H1_2026.md]. Tức là sàn "binding" thực sự (nơi payment throttling bắt đầu kích hoạt) **vẫn chưa được test** dù đã hấp thụ cú sốc tài khóa lớn nhất H1 — $3,000B nên được coi là ước tính biên trên, không phải ngưỡng kích hoạt chính xác. Cần một cú sốc TGA lớn hơn $310B/2 tuần hoặc trùng FBO cuối quý để xác định sàn thật.

---

## 3. Menu chính sách để HẠ sàn (giảm cầu reserves)

Duffie đề xuất 4 công cụ cho phép Fed thu nhỏ bảng cân đối mà không phá truyền dẫn:
1. **TOMO sterilization** — dùng temporary open market operations bù các cú sốc cung reserves (TGA, FIMA reverse repo pool, FBO window-dressing cuối quý). Cho phép đường reserves *trơn hơn và thấp hơn*.
2. **Diễn giải lại liquidity regulation** — cho phép collateral non-HLA tại facility Fed tính vào yêu cầu thanh khoản; bớt ưu tiên reserves hơn Treasuries; bình thường hóa daylight overdraft. Xem [[Intraday_Liquidity_Regulation_Reserve_Demand]].
3. **Thêm Liquidity Savings Mechanism vào Fedwire** — [[Liquidity_Savings_Mechanism_LSM]]: net thanh toán ra/vào → giảm reserves cần để vận hành thanh toán.
4. **Tiering remuneration** — [[Tiered_Reserve_Remuneration]]: trả IORB cao đến quota, thấp hơn vượt quota → ngân hàng cho vay reserves thừa.

**Ưu tiên (Duffie §VIII):** TOMO trước (không cần luật/quy chế mới) → nới liquidity reg → LSM/tiering (dự án nhiều năm).

---

## 4. Ranh giới / Phản biện (Boundary)

- **Ratchet effect:** reserves dồi dào khiến ngân hàng "nghiện" reserves (Acharya-Rajan 2022) → cầu tự tăng theo thời gian; chi phí tuyệt đối của bảng cân đối lớn dần dù tỷ lệ nhỏ.
- **Chi phí vs lợi ích chưa kết luận:** Duffie KHÔNG đưa ra kết luận cost-benefit về quy mô tối ưu; chỉ liệt kê đánh đổi. Bảng cân đối lớn = kiểm soát lãi suất ổn định nhưng "structural footprint" lớn + interest expense lớn (nhạy cảm chính trị — Warsh 2025, Miran 2025).
- **Khác biệt fiscal:** nếu Fed back reserves bằng T-bills → ít tác động tài khóa; nếu bằng UST dài hạn rồi thu nhỏ → tư nhân phải hấp thụ thêm UST dài hạn → chính phủ trả lãi cao hơn (Krishnamurthy–Vissing-Jorgensen).

---

## Related

- [[Receipt_Reactive_Payment_Throttling]] — cơ chế vi mô khiến sàn "binding".
- [[Intraday_Liquidity_Regulation_Reserve_Demand]] — Reg YY đẩy cầu reserves lên.
- [[Liquidity_Savings_Mechanism_LSM]] — công cụ hạ sàn (giảm reserves cần cho thanh toán).
- [[Tiered_Reserve_Remuneration]] — công cụ hạ sàn (kích cho vay liên ngân hàng).
- [[Supply_Driven_Vs_Demand_Driven_Reserves]] — hai cách tiếp cận "ample".
- [[Poole_Curve_Reserve_Demand]] — đường cầu reserves & điểm "ample".
- [[Reserve_Management_Purchases_RMP]] — Fed bơm reserves theo trend để giữ trên sàn.
- [[Treasury_General_Account_Mechanism]] — cú sốc TGA rút reserves xuống sàn.
- [[Demand_for_Central_Bank_Reserves]] — khung cầu reserves (Bindseil).
