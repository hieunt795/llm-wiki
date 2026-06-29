---
title: TOMO Reserve Supply Sterilization
aliases:
- TOMO
- Temporary Open Market Operations
- Reserve Supply Smoothing
- Autonomous Factor Sterilization
type: mechanism
tags:
- monetary-operations
- federal-reserve
- reserves
- liquidity-management
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Ulrich Bindseil | Darrell Duffie"
provenance: "Duffie BPEA 2026 §VIII; Bindseil_Monetary_Policy_Operations.md"
thesis: "TOMO (Temporary Open Market Operations) là nghiệp vụ repo/reverse repo ngắn hạn
  của Fed để bù đắp các cú sốc cung dự trữ từ autonomous factors (TGA swing, FBO window-dressing)
  theo sự kiện. Khác với QE/QT (POMO — thay đổi stock vĩnh viễn), TOMO chỉ thay đổi
  cung dự trữ tạm thời rồi tự đảo ngược. Duffie xếp TOMO là ưu tiên chính sách số một
  để Fed có thể duy trì đường dự trữ thấp hơn mà không tái diễn cú sốc repo 2019."
source_refs:
- file: Bindseil_Monetary_Policy_Operations.md
  page: 24
created: '2026-06-29'
updated: '2026-06-29'
---

## Thesis

TOMO giải quyết vấn đề bất đối xứng nhịp trong hệ thống dự trữ Mỹ H1 2026: RMP bơm ~$40B/tháng đều đặn (trend), TGA hút $100–200B/tuần theo lịch auction (event), FBO window-dressing rút ≥$200B cuối quý. Khi ON RRP = $2.3B (không còn đệm), mọi sự kiện đổ thẳng vào dự trữ 1:1. TOMO không thay đổi bức tranh structural nhưng triệt tiêu spike ngắn hạn — và quan trọng hơn, cho phép Fed duy trì mức reserves trung bình thấp hơn mà không cần buffer dày, vì các cú sốc sẽ được hấp thụ theo sự kiện thay vì bằng stock đệm vĩnh viễn.

## Mechanism

### 1. TOMO vs POMO — Hai loại OMO khác nhau về bản chất

| Chiều | TOMO | POMO (QE/QT/RMP) |
|-------|------|-----------------|
| **Kỳ hạn** | Qua đêm đến vài tuần (repo/reverse repo) | Mua/bán vĩnh viễn (outright) |
| **Tác động lên stock** | Tạm thời — tự đảo ngược khi đáo hạn | Vĩnh viễn — thay đổi bảng cân đối lâu dài |
| **Mục đích** | Bù sốc autonomous factors | Thay đổi lượng reserves cơ sở hoặc rút/bơm duration |
| **Tín hiệu chính sách** | Không có — hoàn toàn vận hành | Có — được thị trường đọc là signal nới/thắt |
| **Nguồn gốc lý thuyết** | Bindseil framework autonomous factors [RAW-BOOK: Bindseil §2.5] | Keynes → Friedman → Bernanke QE |

### 2. Cơ chế vận hành trong H1 2026

Khi TGA hút reserves xuống dưới mức vận hành thoải mái (ví dụ auction settle tuần coupon refunding mid-month), Fed có thể:

1. **Repo overnight/term**: Fed mua tạm thời UST/MBS từ dealer → dealer nhận reserves → reserves hệ thống tăng ngay trong ngày → Fed đảo ngược repo sau 1–14 ngày
2. **Reverse repo (drain)**: Khi TGA xả tiền ra (tax refund, coupon payment đến dân) → Fed bán tạm thời UST → hút dự trữ tạm thời dư thừa → tự đảo ngược

Kết quả: đường dự trữ được làm phẳng quanh target, loại bỏ các spike và hố sâu không có liên quan đến stance chính sách.

### 3. Tại sao TOMO là ưu tiên số một (Duffie BPEA 2026 §VIII)

Duffie [RAW-BOOK: Duffie BPEA 2026] sắp xếp menu chính sách theo thứ tự khả thi:

1. **TOMO (số một)** — không cần luật mới, Fed đã có quyền theo Section 14 Federal Reserve Act; có thể triển khai ngay; hiệu quả tức thì cho autonomous factor volatility
2. Nới lỏng Regulation YY (normalization daylight overdraft) — cần diễn giải lại quy định
3. LSM (Liquidity Saving Mechanism) cho Fedwire — cần đầu tư hạ tầng nhiều năm
4. Tiered IORB — cần quyết định chính trị + thiết kế phức tạp

**Logic số một**: Nếu TOMO thành công làm phẳng đường reserves, Fed có thể chứng minh rằng mức reserves thấp hơn (ví dụ $2.5T thay vì $3T) là đủ an toàn với điều kiện sốc autonomous được hấp thụ kịp thời. Điều này mở đường cho balance sheet nhỏ hơn mà không tăng rủi ro dislocation.

### 4. Giới hạn của TOMO

TOMO giải quyết **volatility** của cung reserves, không giải quyết **level** của cầu reserves. Nếu cầu reserves cao do cấu trúc (GSIB ngại daylight OD, FDIC fee cao, preferred-safety regulations), thì TOMO chỉ làm phẳng sóng trên một đường cầu cao — không hạ được đường cầu. Để hạ level cầu, cần kết hợp với:

- Nới lỏng Regulation YY (giảm ngại daylight overdraft)
- Bình thường hóa daylight OD cost (hiện tính theo đường toán học mức phí không khuyến khích)
- Thay đổi CLAR/RLAP framework để UST được tính gần với cash-equivalent hơn

Ngoài ra, TOMO có giới hạn khi sốc quá lớn và kéo dài (ví dụ FBO window-dressing ≥$400B trong 2 quý gần đây [RAW-BOOK: Duffie §III.C]) — repo ngắn hạn sẽ rollover nhiều lần, làm phức tạp bảng cân đối tạm thời.

## Autonomous Factors Liên Quan Đến H1 2026

| Factor | Tác động lên reserves | Frequency | Quy mô |
|--------|----------------------|-----------|--------|
| **TGA auction settle** | Hút (TGA nhận tiền từ dealer) | Hàng tuần | $100–200B/lần |
| **TGA coupon/principal payment** | Bơm (Treasury trả cho người nắm trái phiếu) | Mid-month + hàng quý | $50–150B |
| **FBO window-dressing** | Hút (ngân hàng nước ngoài rút từ Fed) | Cuối quý | ≥$200B (15 quý); ≥$400B (2 quý) [RAW-BOOK: Duffie §III.C] |
| **Currency in circulation** | Hút (dân rút tiền mặt) | Seasonal | $5–20B/tháng |
| **FIMA reverse repo** | Hút (nước ngoài gửi vào Fed) | Variable | $0–50B |

Với ON RRP = $2.3B, không còn tầng đệm trung gian — TOMO là công cụ duy nhất có thể offset các factors này trong thời gian thực.

## Evidence / Source Anchors

- Autonomous factors definition và balance sheet identity: [[Autonomous_Factors_In_Central_Bank_Balance_Sheet]] [RAW-BOOK: Bindseil §2.5]
- TOMO as priority #1 policy: [RAW-BOOK: Duffie BPEA 2026 §VIII]
- FBO window-dressing quy mô: [RAW-BOOK: Duffie §III.C, citing Crandall]
- ON RRP $2.3B = đệm đã cạn: [RAW-OFFICIAL: H.4.1 24/06/2026]
- Bất đối xứng nhịp RMP/TGA: [RAW-OFFICIAL: H.4.1 24/06/2026; RAW-OFFICIAL: Perli NY Fed 26/03/2026]

## Related

- [[Autonomous_Factors_In_Central_Bank_Balance_Sheet]] — Framework Bindseil về autonomous factors
- [[Payment_System_Floor_On_Fed_Balance_Sheet]] — Cầu dự trữ cấu trúc mà TOMO không giải quyết được
- [[Reserve_Management_Purchases_RMP]] — POMO trend-based, khác với TOMO event-based
- [[Receipt_Reactive_Payment_Throttling]] — Khi TOMO không kịp can thiệp, cơ chế này kích hoạt
- [[Standing_Repo_Facility_SRF_Mechanics]] — Van an toàn ex-post (rò rỉ), khác với TOMO ex-ante
- [[Treasury_General_Account_Mechanism]] — Nguồn autonomous factor lớn nhất H1 2026
