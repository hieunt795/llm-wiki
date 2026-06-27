---
title: Currency Swap Engineering
aliases:
- Cross-Currency Swap
- XCCY Swap
- Hoán đổi tiền tệ
type: mechanism
tags:
- fx
- swaps
- long-term-funding
- multi-asset
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: Salih Neftci - Principles of Financial Engineering (2008)
thesis: Hoán đổi tiền tệ (Currency Swap) là một thỏa thuận trao đổi các khoản thanh
  toán gốc và lãi bằng hai loại tiền tệ khác nhau, về mặt chức năng là tái lập việc
  trao đổi hai trái phiếu lãi suất thả nổi (FRNs) hoặc trái phiếu định danh bằng các
  loại tiền tệ khác nhau.
source_refs:
- file: Principles_of_Financial_Engineering_Neftci.md
  page: 198
created: '2026-04-21'
updated: '2026-04-22'
---

## Thesis

[RAW] Khác với FX Swap (vốn dĩ là công cụ vay ngắn hạn có tài sản đảm bảo), Currency Swap là một công cụ dài hạn (1-30 năm) được thiết kế để tài trợ các dự án nước ngoài hoặc phòng vệ rủi ro tỷ giá cho các khoản nợ dài hạn. Salih Neftci định nghĩa Currency Swap là việc trao đổi các dòng tiền của hai công cụ nợ (như FRNs) khác đồng tiền. [[Principles_of_Financial_Engineering_Neftci.md#page=198]]

---

## 1. Mechanics and Structure

Một Currency Swap tiêu chuẩn (e.g., USD Floating vs. EUR Floating) bao gồm 3 giai đoạn:

1.  **Giai đoạn 1 (t=0):** Trao đổi gốc (Principal). Người trả USD đưa $N_{USD}$ và nhận lại lượng EUR tương ứng theo tỷ giá giao ngay ($e_{t0} \cdot N_{USD}$).
2.  **Giai đoạn 2 (Interim):** Trao đổi lãi định kỳ. Bên nhận USD trả lãi USD (e.g., $LIBOR_{USD}$) và nhận lãi EUR ($LIBOR_{EUR} + Spread$). Lưu ý: Các khoản thanh toán lãi không bù trừ (no netting) vì khác đồng tiền.
3.  **Giai đoạn 3 (t=n):** Trao đổi lại gốc tại thời điểm đáo hạn với **cùng một tỷ giá** $e_{t0}$ đã sử dụng ở t=0.

### Timeline & Cash Flows

Trục thời gian (3-period example):
   t=0 (Start)          t=1 (Interim)         t=2 (Interim)         t=n (Maturity)
    │─────────────────────│─────────────────────│────────...──────────│
[Leg 1] Nhận Principal N    -Interest L1_1       -Interest L1_2        -Interest L1_n
                                                                       -Principal N
[Leg 2] Trả Principal M     +Interest L2_1       +Interest L2_2        +Interest L2_n
                                                                       +Principal M

---

## 2. FX Swap vs. Currency Swap (Neftci Nuance)

| Đặc điểm | FX Swap | Currency Swap (XCCY) |
| :--- | :--- | :--- |
| **Bản chất kinh tế** | Trao đổi 2 trái phiếu zero-coupon. | Trao đổi 2 trái phiếu lãi suất thả nổi (FRNs). |
| **Kỳ hạn (Maturity)** | Ngắn hạn (< 1 năm). | Dài hạn (1-30 năm). |
| **Dòng tiền giữa kỳ** | Không có (Lãi được gộp vào chân 2). | Có trao đổi lãi định kỳ. |
| **Tỷ giá đáo hạn** | Tỷ giá kỳ hạn $F_{t0}$. | Tỷ giá giao ngay gốc $e_{t0}$. |
| **Quy mô thị trường** | Chiếm 42% doanh số FX toàn cầu. | Chỉ chiếm ~1% doanh số FX. |

[[Principles_of_Financial_Engineering_Neftci.md#page=202]]

---

## 3. The "Cost of Carry" Logic

[RAW] Tại sao Currency Swap lại trao đổi gốc ở tỷ giá cũ ($e_{t0}$)?
- **Logic:** Do các bên đã thanh toán chênh lệch lãi suất định kỳ trong suốt đời swap, nên họ không cần phải điều chỉnh tỷ giá ở cuối đời. Mọi biến động lãi suất đã được phản ánh qua các dòng tiền interim. [[Principles_of_Financial_Engineering_Neftci.md#page=201]]

---

## 4. Strategic Uses: Funding New Issues

Nhà phát hành (Issuers) sử dụng Currency Swaps để "nhập khẩu" lợi thế chi phí từ các thị trường nước ngoài. Salih Neftci trình bày một quy trình tính toán **All-in-cost** điển hình:

### Case Study: Swapping USD Issue to GBP
Một tổ chức tại Anh phát hành 100 triệu USD trái phiếu kỳ hạn 2 năm, coupon 6% để chuyển sang GBP.

1.  **Net Proceeds:** Giá phát hành 100.75, phí 1.25%, chi phí khác 75k USD -> Thực nhận 99.425 triệu USD.
2.  **Effective Cost ($yt_0$):** Giải IRR cho dòng tiền: `-99.425M (nhận) | +6M (năm 1) | +106M (năm 2)`. Kết quả: $yt_0 = 6.315%$. (Cao hơn coupon 6% do chi phí phát hành).
3.  **The Swap Execution:**
    - **Bước 1 (Fixed to Float USD):** Issuer trả USD LIBOR và nhận 5.46% (Swap rate). Net cost USD = $LIBOR + (6.315\% - 5.46\%) = LIBOR + 85.5$ bps.
    - **Bước 2 (Currency Swap):** Issuer trả GBP LIBOR (+ spread) và nhận lại USD LIBOR.
- **Result:** Tổng chi phí cuối cùng là GBP LIBOR + spread + 85.5 bps. Nếu tổng này < chi phí phát hành GBP trực tiếp (e.g., 6.5%), chiến lược này thành công. [[Principles_of_Financial_Engineering_Neftci.md#page=205]]

---

## 5. Risks and Market Dynamics

- **Regulatory Advantage:** Sau GFC, các cơ quan quản lý (US Treasury, EU) đã miễn trừ FX swaps và forwards khỏi các yêu cầu bù trừ tập trung (CCP) và ký quỹ ban đầu (Initial Margin). Điều này giúp các sản phẩm FX giữ được chi phí thấp và tính linh hoạt cao hơn so với Interest Rate Swaps. [[Principles_of_Financial_Engineering_Neftci.md#page=203]]
- **Basis Risk:** Rủi ro nằm ở việc Spread của Currency Swap (XCCY Basis) có thể thay đổi, ảnh hưởng đến chi phí vay thực tế (all-in cost).
- **GFC Impact:** Trong khủng hoảng, nhu cầu USD cực lớn từ các ngân hàng Châu Âu đẩy XCCY Basis xuống mức âm sâu (Negative Basis), nghĩa là việc vay USD qua Swap đắt hơn nhiều so với Libor trực tiếp. [[Principles_of_Financial_Engineering_Neftci.md#page=203]]

---

## Evidence / Source Anchors

- Core mechanics of currency swap principal and interest exchange: [[Principles_of_Financial_Engineering_Neftci.md#page=199]]
- Comparison with FX Swap functionality and risks: [[Principles_of_Financial_Engineering_Neftci.md#page=201]]
- Market liquidity and maturity statistics: [[Principles_of_Financial_Engineering_Neftci.md#page=202]]

## Related

- [[FX_Swap_Engineering]] — Phiên bản ngắn hạn.
- [[Floating_Rate_Note_FRN]] — Các chân giao dịch cấu thành.
- [[Covered_Interest_Parity]] — Cơ sở cho định giá cơ bản (không tính Basis).
