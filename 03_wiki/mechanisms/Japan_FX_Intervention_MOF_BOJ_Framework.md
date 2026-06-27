---
title: Japan FX Intervention — MOF/BOJ Framework
aliases:
- Japan FX Intervention
- MOF BOJ FX
- Foreign Exchange Fund Special Account
- FEFSA
- Financing Bills Japan
- MoF Agent BOJ
- Nhật Bản can thiệp tỷ giá
type: mechanism
tags:
- japan
- foreign-exchange
- central-banking
- fiscal-monetary-coordination
- sterilization
status: verified
confidence: 5
half_life_years: 5
school: ''
superseded_by: null
superseded_date: null
expert_lens:
- "Bank of Japan (Institutional)"
- "Ministry of Finance Japan (Institutional)"
- "Federal Reserve Bank of San Francisco"
provenance:
- "BOJ — Outline of FX Intervention Operations (official)"
- "BOJ Act, Article 40(2)"
- "Foreign Exchange and Foreign Trade Act, Article 7(3)"
- "FRBSF Economic Letter — Japanese FX Intervention (2003)"
- "Federal Reserve IFDP 824 — Assessment of Japanese FX Intervention 1991–2004 (2005)"
thesis: Nhật Bản là trường hợp đặc biệt — quyền lực FX intervention nằm hoàn toàn
  ở Bộ Tài chính (MoF), không phải BOJ. BOJ chỉ hoạt động như đại lý thực thi theo
  lệnh MoF thông qua Foreign Exchange Fund Special Account (FEFSA). Cơ chế Financing
  Bills tạo ra automatic sterilization by design, tách biệt FX operation khỏi base
  money — nhưng tạo ra tension cấu trúc khi FX policy và monetary policy đẩy ngược
  chiều nhau.
source_refs:
- url: https://www.boj.or.jp/en/intl_finance/outline/expkainyu.htm
- url: https://www.boj.or.jp/en/about/education/oshiete/intl/g19.htm
- url: https://www.mof.go.jp/english/policy/international_policy/fefsa/index.html
- url: https://www.frbsf.org/wp-content/uploads/el2003-36.pdf
- url: https://www.federalreserve.gov/pubs/ifdp/2005/824/ifdp824.htm
- url: https://people.ucsc.edu/~hutch/IEEP2005.pdf
created: '2026-05-04'
updated: '2026-05-04'
---

# Japan FX Intervention — MOF/BOJ Framework

## Điểm then chốt: BOJ không có quyền tự quyết FX

Đây là khác biệt cơ bản so với hầu hết NHTW khác. Tại Nhật, **Bộ Tài chính (MoF)** là chủ thể pháp lý duy nhất có thẩm quyền can thiệp tỷ giá. BOJ chỉ là **đại lý thực thi (agent)** — không có quyền tự khởi xướng, điều chỉnh, hay từ chối lệnh.

---

## 1. Khung pháp lý

> *Nguồn: BOJ official, Foreign Exchange and Foreign Trade Act, BOJ Act*

**Foreign Exchange and Foreign Trade Act, Article 7(3):**
> "Bộ trưởng Tài chính có nghĩa vụ ổn định tỷ giá đồng Yên thông qua các biện pháp cần thiết bao gồm mua bán ngoại hối."

**Bank of Japan Act, Article 40(2):**
> BOJ chỉ được mua bán ngoại hối **"với tư cách đại lý của chính phủ... khi mục đích là ổn định tỷ giá quốc gia."**

So sánh với các NHTW khác — ECB, SNB, Bank Indonesia — đều có mandate FX trong điều lệ riêng và quyền tự quyết can thiệp. Nhật Bản là ngoại lệ rõ ràng nhất trong G7.

---

## 2. Luồng quyết định: MoF → BOJ

> *Nguồn: BOJ — What is FX intervention? (official)*

```
Thị trường JPY biến động mạnh
          ↓
MoF Forex Division đánh giá, cung cấp cho BOJ thông tin thị trường
          ↓
Bộ trưởng Tài chính ra quyết định can thiệp
          ↓
MoF Forex Division → chỉ thị cụ thể → BOJ Forex Division
          ↓
BOJ thực thi lệnh trên thị trường giao ngay (spot market)
```

**Vai trò thông tin của BOJ:** BOJ cung cấp dữ liệu biến động thị trường và bối cảnh cho MoF, nhưng **không có quyền khuyến nghị can thiệp hay không**. Quyết định là của Bộ trưởng Tài chính.

Goldman Sachs (2022) xác nhận: MoF đưa **chỉ thị cụ thể (specific instructions)** cho BOJ — không phải tham vấn, không phải phối hợp, mà là lệnh chính thức.

---

## 3. Foreign Exchange Fund Special Account (FEFSA)

> *Nguồn: MoF — FEFSA official page*

FEFSA là tài khoản đặc biệt **thuộc MoF** — không phải tài sản của BOJ. Đây là nơi chứa toàn bộ dự trữ ngoại hối của Nhật (~$1.2 nghìn tỷ USD, lớn thứ 2 thế giới sau Trung Quốc).

BOJ thực hiện giao dịch **sử dụng FEFSA** theo ủy quyền — nhưng tài sản không nằm trên bảng cân đối của BOJ.

---

## 4. Cơ chế tài chính: Automatic Sterilization by Design

> *Nguồn: During_Fixed_Income_Ch08.md | FRBSF Economic Letter 2003*

### Kịch bản A: Yên mạnh quá → Bán Yên, mua USD

```
MoF phát hành Financing Bills (FBs) → hút Yên từ thị trường
          ↓
Dùng Yên đó mua USD thông qua BOJ (agent)
          ↓
USD vào FEFSA
```

**Kết quả:** Lượng Yên tung ra mua USD = lượng Yên đã hút qua FB issuance → **base money không thay đổi**. Sterilization xảy ra tự động ở bước 1, không cần BOJ làm bước riêng.

### Kịch bản B: Yên yếu quá → Bán USD, mua Yên (2022)

```
MoF lấy USD từ FEFSA bán ra thị trường (qua BOJ)
          ↓
Yên thu về → base money giảm
          ↓
(Tùy chọn) BOJ bơm thanh khoản bù qua OMO
          — nhưng đây là quyết định ĐỘCLẬP của BOJ về monetary policy
```

Kịch bản B phức tạp hơn vì không tự động sterilized và tạo ra tension với monetary stance của BOJ.

---

## 5. Tension cấu trúc: Fiscal vs. Monetary Independence

> *Nguồn: UCSC — FX Intervention and Monetary Policy in Japan | Fed Reserve IFDP 824*

**Vấn đề cốt lõi:** MoF kiểm soát FX, nhưng FX intervention có thể xung đột trực tiếp với mục tiêu monetary của BOJ.

**Case 2022:** MoF can thiệp bán USD ~$60 tỷ để bảo vệ Yên (hút Yên về) trong khi BOJ vẫn duy trì YCC (Yield Curve Control) với lãi suất cực thấp → hai chính sách đẩy ngược chiều nhau hoàn toàn. MoF bảo vệ tỷ giá, BOJ giữ lãi suất thấp → Carry trade vẫn hấp dẫn → áp lực Yên yếu tiếp tục.

**Giải pháp thực tế:** BOJ "trung lập hóa" tác động qua OMO, giữ nguyên monetary stance về lý thuyết. Nhưng khi quy mô intervention lớn, ranh giới nhòe dần.

**Lý do lịch sử thiết kế như vậy:** Sau WWII, Allied Occupation tách quyền kiểm soát ngoại hối khỏi NHTW để ngăn BOJ tài trợ thâm hụt ngân sách qua in tiền. MoF nắm FEFSA = kiểm soát FX reserves mà không cần qua BOJ — một giải pháp thể chế độc đáo mà Nhật Bản vẫn duy trì đến nay.

---

## 6. Hệ quả thị trường dài hạn

> *Nguồn: During_Fixed_Income_Ch08.md*

Vì Nhật có thặng dư tài khoản vãng lai lớn và liên tục tích lũy FX reserves qua FEFSA, dòng tiền nước ngoài đổ về tìm tài sản nội địa làm **lãi suất ngắn hạn bị nén xuống**. Düring chỉ ra đây là lý do Nhật có lãi suất âm trên JGB ngắn hạn *trước khi* BOJ chính thức cắt lãi suất xuống 0 — sterilization liên tục tạo ra dư thừa thanh khoản cấu trúc trong hệ thống.

---

## Evidence / Source Anchors

- Khung pháp lý — MoF là chủ thể, BOJ là agent: [BOJ Outline of FX Intervention](https://www.boj.or.jp/en/intl_finance/outline/expkainyu.htm)
- Phân công quyết định MoF/BOJ: [BOJ — What is FX intervention?](https://www.boj.or.jp/en/about/education/oshiete/intl/g19.htm)
- FEFSA structure và Financing Bills: [MoF FEFSA](https://www.mof.go.jp/english/policy/international_policy/fefsa/index.html)
- Automatic sterilization qua FB issuance: [[During_Fixed_Income_Ch08.md]] | [FRBSF EL 2003](https://www.frbsf.org/wp-content/uploads/el2003-36.pdf)
- Tension FX/monetary và hiệu quả intervention 1991–2004: [Fed Reserve IFDP 824](https://www.federalreserve.gov/pubs/ifdp/2005/824/ifdp824.htm)
- Conflict giữa FX intervention và monetary policy: [UCSC Hutchison 2005](https://people.ucsc.edu/~hutch/IEEP2005.pdf)
- Hệ quả lãi suất dài hạn từ tích lũy reserves: [[During_Fixed_Income_Ch08.md]]

## Related

- [[FX_Sterilization_Mechanism]] — Cơ chế sterilization tổng quát; Nhật là case study automatic sterilization
- [[Foreign_Exchange_Sterilisation]] — Node liên quan về sterilization dynamics
- [[Japan_Debt_Puzzle_Mechanism]] — BOJ/MoF coordinated carry trade ở cấp vĩ mô
- [[Financial_Repression_Japan_Model]] — Hệ quả lãi suất thấp từ chính sách FX/monetary kết hợp
- [[JP_Domain]] — Domain profile tổng quan Nhật Bản
- [[Central_Bank_Independence_Typology]] — Vì sao BOJ "độc lập về monetary" nhưng không độc lập về FX
- [[Monetary_Policy_Trilemma]] — Framework lý thuyết giải thích trade-off MoF phải đối mặt
