---
title: Treasury General Account Mechanism
aliases:
- TGA
- Tài khoản kho bạc
type: mechanism
tags:
- central-banking
- liquidity
- money-market
- fiscal-policy
status: reviewed
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: Roc Armenter | Spyros Andreopoulos
provenance: Web Synthesis (BlackRock, MacroMicro); [RAW-OFFICIAL: Fed H.4.1 (2026-06-24)]; [RAW-OFFICIAL: Treasury Q2 2026 Refunding]
thesis: TGA (Treasury General Account) là tài khoản thanh toán của Kho bạc Nhà nước
  đặt tại Fed. Sự biến động của TGA tỷ lệ nghịch 1:1 với khối lượng Dự trữ Ngân hàng
  (Bank Reserves), đóng vai trò là một biến số thanh khoản độc lập trọng yếu (autonomous
  liquidity factor) và có thể gây áp lực lên thị trường Repo nếu thu hồi quá nhanh.
source_refs: []
created: '2026-04-22'
updated: '2026-06-27'
---

## Thesis

TGA (Treasury General Account) là tài khoản thanh toán của Kho bạc Nhà nước (Chính phủ) đặt tại Ngân hàng Trung ương (Fed). Trong kiến trúc vĩ mô, biến động của TGA tỷ lệ nghịch 1:1 với khối lượng Dự trữ (Bank Reserves) của hệ thống ngân hàng thương mại, do đó nó hoạt động như một kênh rút/bơm thanh khoản trực tiếp.

---

## 1. The Mechanics (Cơ chế Kế toán Vi mô)

Để hiểu TGA, ta phải nhìn vào phương trình Bảng cân đối của Fed:
`Tài sản (Bonds) = Nợ phải trả (Dự trữ Ngân hàng + TGA + ON RRP + Tiền mặt)`

Giả định Tài sản của Fed đứng yên (không có QE/QT), bất kỳ sự gia tăng nào của TGA bắt buộc phải được bù trừ bằng sự sụt giảm của một khoản Nợ phải trả khác (thường là Dự trữ Ngân hàng).

- **Cơ chế Hút (TGA Rebuild - Liquidity Drain):** Khi chính phủ thu thuế hoặc phát hành trái phiếu mới, nhà đầu tư dùng tiền trong tài khoản ngân hàng để mua. Fed sẽ ghi nợ (trừ tiền) tài khoản dự trữ của ngân hàng đó và ghi có (cộng tiền) vào TGA. **Kết quả:** Thanh khoản của hệ thống ngân hàng bốc hơi tương ứng.
- **Cơ chế Bơm (TGA Drawdown - Liquidity Injection):** Khi chính phủ chi tiêu (trả lương, hưu trí, thanh toán thầu), tiền từ TGA chảy ngược lại vào tài khoản của người dân tại các ngân hàng thương mại. **Kết quả:** Dự trữ của hệ thống ngân hàng tăng lên, thanh khoản dồi dào.

---

## 2. T-Account Transmission

(Ví dụ: Kho bạc phát hành 100 tỷ USD trái phiếu, được các Ngân hàng mua bằng Dự trữ)

```text
          FEDERAL RESERVE (NHTW)                     COMMERCIAL BANKS (Primary Dealers)
    Assets          │      Liabilities             Assets          │      Liabilities
────────────────────┼────────────────────      ────────────────────┼────────────────────
(Không đổi)         │ (1) Bank Reserves      (1) Reserves at Fed   │ (Không đổi)
                    │     [-$100B]                 [-$100B]        │
                    │                        (2) Treasury Bonds    │
                    │ (2) TGA                      [+$100B]        │
                    │     [+$100B]                                 │
```

=> **Truyền dẫn:** Tiền di chuyển từ [Reserves] sang [TGA] trên bảng cân đối của Fed. Thanh khoản hệ thống bị thắt chặt.

---

## 3. Ranh giới rủi ro (Failure Conditions & The ON RRP Buffer)
- **Draining Shock (Cú sốc cạn kiệt):** Khi chính phủ giải quyết xong trần nợ công (Debt Ceiling), họ thường ồ ạt phát hành T-Bills để nạp lại TGA trong thời gian cực ngắn. Nếu tốc độ hút tiền quá gắt, Dự trữ Ngân hàng sẽ rớt xuống dưới ngưỡng "Lowest Ample Reserves".
- **The 9% GDP Boundary (Update May 2026):** [RAW-CLIP: Andreopoulos (2026-04-11)] Các phân tích mới nhất xác định ngưỡng **9% GDP (tương đương khoảng $3.000 tỷ hiện nay)** là mức dự trữ tối thiểu để duy trì sự ổn định. Nếu biến động TGA đẩy dự trữ xuống dưới ngưỡng này, các dislocations trên thị trường tiền tệ (như SOFR spike) sẽ xảy ra ngay lập tức do nhu cầu dự trữ cấu trúc của các ngân hàng.

### Live Snapshot — H1 2026 (Fed H.4.1 as-of 2026-06-24)
[RAW-OFFICIAL: Fed H.4.1; Treasury Q2 2026 Refunding] Cấu hình liability side của Fed đã chạm đúng điểm căng mà ngưỡng 9% GDP cảnh báo:

| Khoản mục | Giá trị (24/06/2026) | Hệ quả |
|---|---|---|
| Reserve Balances | **$2,951.4B** | ≈ ngay tại floor ~$3,000B → biên an toàn ≈ 0 |
| TGA | **$918.7B** | giảm từ đỉnh ~$1,025B (cuối 4/2026, mùa thuế) |
| ON RRP ("others") | **$2.3B** | **buffer đã cạn** — không còn hấp thụ swing TGA |
| RRP foreign official | $331.4B | structural, không phải biến đệm |
| Total Assets | $6,735.6B | phẳng (QT kết thúc 01/12/2025) |

**Khác biệt cấu trúc 2026 vs 2023:** Năm 2023 ON RRP >$2T làm đệm — cú nạp TGA rút từ ON RRP trước, reserves gần như không động (xem identity `dTGA = -dReserves` chỉ áp dụng *sau khi* ON RRP cạn). Năm 2026 ON RRP cạn → **mọi cú nạp TGA đổ thẳng vào reserves**. Marginal absorber duy nhất bây giờ là reserves.

**Bối cảnh phát hành:** Trần nợ nâng lên **$41.1T** (One Big Beautiful Bill Act) → Treasury thoát "extraordinary measures", vay ~$683B trong 2 quý (1–6/2026, +$249B YoY). Lực hút TGA cấu trúc vẫn còn dù drawdown mùa thuế 5–6/2026 tạm giảm tải.

**Lực bù phía Fed:** Sau QT, Fed bơm reserves qua [[Reserve_Management_Purchases_RMP]] — nhưng theo *trend* (trễ), bất đối xứng với cú rút TGA theo *sự kiện*. Khe hở nhịp này là nguồn nới rộng **SOFR–IORB spread** từng đợt (gauge stress chính, không phải EFFR). Van xử lý spike là [[Standing_Repo_Facility_SRF_Mechanics]].

---

## 3. Ranh giới rủi ro (Failure Conditions & The ON RRP Buffer)
[RAW] Cơ chế vận hành của TGA không phải là một "định luật vật lý" bất biến mà là một sự lựa chọn về mặt quản trị:
- **Pre-2008:** Kho bạc duy trì phần lớn số dư tại các ngân hàng thương mại tư nhân (TT&L accounts). Điều này giúp ổn định Reserves tại Fed.
- **Post-2015:** Kho bạc duy trì một mức tối thiểu khổng lồ ($150B+) tại TGA ở Fed. Hiện nay, con số mục tiêu thường xuyên ở mức $750B - $850B.

### The Identity (T2 Structure)
Trong ngắn hạn, mọi giao dịch của Kho bạc tuân thủ phương trình:
$$dTGA = -dReserves$$
(Trừ khi được hấp thụ bởi cơ sở ON RRP).

### BS Growth Driver (T3 Philosophy)
Về dài hạn, để giữ Reserves ở mức "Ample", Fed buộc phải điều chỉnh tài sản theo TGA:
$$dTGA = dAssets$$
**Hệ quả:** Sự phình to của bảng cân đối Fed hiện nay có một phần nguyên nhân quan trọng đến từ **lựa chọn cấu trúc** của Bộ Tài chính trong việc duy trì số dư TGA lớn và biến động.

---

## 5. TGA Stabilization & BS Optimization
[WIKI] Xem [[Central_Bank_Balance_Sheet_Trilemma]] để biết chi tiết về công thức **Napkin Math** tính toán dự trữ đệm dựa trên độ biến động TGA ($\sigma$). Tối ưu hóa TGA có thể giải phóng khoảng 2% GDP Danh nghĩa cho bảng cân đối Fed.

---

## Evidence / Source Anchors

- [RAW] TGA as a liability and dTGA = -dReserves: [[The Checking Account of the U.S. Federal Government....md]]
- [RAW] Napkin Math for TGA volatility buffer: [[Napkin Math for an Ample Reserves Buffer.md]]
- [WEB] Tác động tỷ lệ nghịch của TGA lên Bank Reserves: [Nguồn: BlackRock](https://www.blackrock.com/us/individual/insights/the-treasury-general-account)

## Related
- [[Reserve_Management_Purchases_RMP]] — Lực bù reserves đối nghịch phía Fed (bơm theo trend).
- [[Repurchase_Agreement_Mechanism]] — Nơi trực tiếp chịu ảnh hưởng khi thanh khoản dự trữ cạn kiệt.
- [[Quantitative_Tightening_Mechanism]] — QT cộng hưởng với TGA Rebuild sẽ khuếch đại rủi ro thanh khoản.
- [[Autonomous_Factors_Framework]] — Khung lý thuyết tổng quát về các yếu tố tự trị (bao gồm TGA).
- [[Zero_Lower_Bound_ZLB]] — Khi lãi suất ở ZLB, sự dịch chuyển giữa ON RRP và TGA trở nên quan trọng hơn.

---

## 4. International Taxonomy (Sự phân hóa toàn cầu)

Cơ chế TGA không đồng nhất trên toàn cầu. Khái niệm cốt lõi ở các quốc gia khác thường được gọi là **Treasury Single Account (TSA)**:

| Khía cạnh | U.S. TGA (Mỹ) | Eurosystem (ECB) | Emerging Markets (EMEs - TSA) |
| :--- | :--- | :--- | :--- |
| **Cấu trúc** | Tập trung duy nhất tại Fed. | Phân tán tại các NHTW quốc gia (Bundesbank, Bank of France...). | Đang trong quá trình tập trung hóa (Rút tiền từ NHTM về NHTW). |
| **Mục tiêu cốt lõi** | Quản lý thanh toán & Dự phòng cho rủi ro Trần nợ công (Debt Ceiling). | Quản lý ngân khố quốc gia riêng lẻ. | Hợp nhất các tài khoản phân mảnh, tối ưu hóa chi phí vốn của chính phủ. |
| **Tác động Thanh khoản** | Tác động trực tiếp và đáng kể đến Bank Reserves và Repo Market do quy mô lớn. | Được ECB giám sát và bù trừ chéo (netting) trên bình diện toàn khối Eurozone. | Độ nhạy cảm cao do thị trường nội địa thiếu chiều sâu (Shallow Market). |
| **Rủi ro đứt gãy** | Sự sụt giảm dự trữ quá nhanh có thể gây áp lực thanh khoản (như sự kiện repo 2019). | Xung đột mục tiêu tài khóa giữa các nước thành viên. | Việc tập trung hóa TSA làm giảm thanh khoản hệ thống của các NHTM nhỏ (Tier 2), có thể hạn chế nguồn cung tín dụng. |
