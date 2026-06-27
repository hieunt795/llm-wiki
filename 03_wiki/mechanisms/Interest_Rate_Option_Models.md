---
title: Interest Rate Option Models
aliases:
- Black Model vs Normal Model
- Lognormal Model
- Normal Model
- Volatility Skew
- Basis Point Vol
- Howard Corb Perspective on Option Models
type: mechanism
tags:
- derivatives
- quantitative-finance
- interest-rates
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Howard Corb"
provenance: Howard_Corb_Swaps.md
thesis: The choice between lognormal (Black) and normal models for interest rate options
  is driven by the empirical behavior of rate volatility and the market-observed skew,
  where the normal model better captures the absolute basis-point movements characteristic
  of modern rate environments.
source_refs:
- file: Howard_Corb_Swaps.md
  page: 181
- file: Howard_Corb_Swaps.md
  page: 184
- file: Howard_Corb_Swaps.md
  page: 185
- file: Howard_Corb_Swaps.md
  page: 198
created: '2026-04-20'
updated: '2026-04-22'
---

## Thesis

Trong thị trường quyền chọn lãi suất, việc lựa chọn mô hình phân phối là một ranh giới kỹ thuật sinh tử đối với các Dealer. Howard Corb bóc tách sự chuyển dịch từ **Mô hình Black (Lognormal)** sang **Mô hình Normal (Gaussian)**. Trong khi Black giả định biến động tỷ lệ thuận với mức lãi suất, mô hình Normal giả định biến động là tuyệt đối (basis points), điều này phù hợp hơn với thực tế thị trường khi lãi suất ở mức thấp hoặc âm. [[Howard_Corb_Swaps.md#page=181]]

---

## 1. The Lognormal vs. Normal Conflict

### A. Black-Scholes/Black Model (Lognormal)
- **Assumption:** Lãi suất không bao giờ âm. Biến động ($ \sigma $) được tính theo tỷ lệ phần trăm (Relative Volatility).
- **The Problem:** Nếu lãi suất là 1%, một biến động 10% chỉ là 10 bps. Nếu lãi suất là 10%, biến động 10% là 100 bps. Thực tế cho thấy các cú sốc lãi suất thường có biên độ basis point tương đối ổn định bất kể mức lãi suất nền (High vs Low rate environment). [[Howard_Corb_Swaps.md#page=182]]

### B. The Normal Model (Absolute/Basis Point Vol)
- **Assumption:** Lãi suất có thể âm. Biến động ($ \sigma_N $) được tính bằng Basis Points (Annualized BP Vol).
- **The Reality:** Howard Corb chỉ ra rằng biểu đồ thay đổi lãi suất hàng ngày không thay đổi đáng kể khi lãi suất nền thay đổi, ủng hộ giả định của mô hình Normal hơn là Lognormal. [[Howard_Corb_Swaps.md#page=183]]

---

## 2. Volatility Skew Dynamics

Howard Corb giải mã tại sao "Skew" lại là mỏ neo của trading logic:
- **Definition:** Mối quan hệ giữa Implied Volatility và Strike Price.
- **Downward Skew:** Hiện tượng các quyền chọn có Strike thấp giao dịch ở mức Lognormal Vol cao hơn các quyền chọn Strike cao.
- **Normal Model Advantage:** Mô hình Normal tự động tạo ra một đường cong "Downward Skew" khi được quy đổi ngược lại sang mô hình Black. Điều này khớp với dữ liệu thực tế hơn là giả định "Flat Skew" của mô hình Black truyền thống. [[Howard_Corb_Swaps.md#page=187]]

---

## 3. Supply and Demand Drivers (Corb's Lens)

Tại sao Skew tồn tại?
- **Net Demand for Low-Strike Options:** Các Mortgage Servicers thường mua các quyền chọn Strike thấp (Receivers/Floors) để phòng vệ rủi ro trả trước (Prepayment Risk). Nhu cầu này đẩy Vol của Strike thấp lên cao.
- **Supply of High-Strike Options:** Các công ty và Agency phát hành trái phiếu Callable thường bán các quyền chọn Strike cao cho Dealer thông qua các cấu trúc hoán đổi (Cancelable Swaps), làm giảm Vol của Strike cao. [[Howard_Corb_Swaps.md#page=191]]

---

## 4. Normal Model ATMF Straddle

Công thức "ngón tay cái" (Rule of Thumb) phổ biến nhất trong ngành:
$$\text{Straddle Value} \approx \sqrt{T} \cdot \sqrt{\frac{2}{\pi}} \cdot \sigma_N \cdot A \approx \sqrt{T} \cdot 0.8 \cdot \sigma_N \cdot A$$
- Trong đó $ \sigma_N $ là Normal Vol tính bằng Basis Points.
- Giá trị này **tuyến tính** với Normal Vol và căn bậc hai của thời gian, giúp các Trader tính toán nhanh rủi ro mà không cần máy tính phức tạp. [[Howard_Corb_Swaps.md#page=196]]

---

## Evidence / Source Anchors

- Empirical critique of lognormality for interest rates: [[Howard_Corb_Swaps.md#page=182]]
- Comparison of Daily Changes in high vs low rate environments: [[Howard_Corb_Swaps.md#page=183]]
- Analysis of Downward Skew and its relationship to the Normal Model: [[Howard_Corb_Swaps.md#page=187]]
- Supply/Demand map for interest rate options (Figure 5.11): [[Howard_Corb_Swaps.md#page=191]]
- Normal ATMF Straddle pricing formula: [[Howard_Corb_Swaps.md#page=196]]

## Related

- [[Caps_And_Floors]] — Primary instruments using these models.
- [[Swaptions]] — The swaption matrix follows these dynamics.
- [[Negative_Convexity]] — Relevant for low-strike demand logic.
- [[Mortgage_Prepayment_Drivers]] — The underlying reason for skew demand.
