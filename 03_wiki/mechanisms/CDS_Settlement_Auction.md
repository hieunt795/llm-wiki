---
title: CDS Settlement Auction
aliases:
- CDS Auction
- Đấu giá tất toán CDS
- Hertz 2020 Case
type: mechanism
tags:
- derivatives
- credit-risk
- auction-theory
status: verified
confidence: 5
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Tuckman & Serrat"
provenance: Multi-source
thesis: The CDS Settlement Auction is a standardized industry-run process used to
  determine the final recovery price of defaulted bonds, ensuring orderly cash or
  physical settlement and preventing market squeezes.
source_refs:
- file: Tuckman_Serrat_2022.md
  page: 380
- file: Tuckman_Serrat_2022.md
  page: 382
created: '2026-04-20'
updated: '2026-04-20'
---

## Thesis

Tại sao việc thanh lý CDS lại không thể diễn ra đơn lẻ giữa hai bên? Bruce Tuckman giải mã ranh giới của tính thanh khoản: Trong một sự kiện vỡ nợ, nguồn cung trái phiếu thường bị thao túng hoặc khan hiếm (Squeeze), khiến việc giao hàng vật chất (Physical Settlement) trở nên bất khả thi. **CDS Settlement Auction** là giải pháp trung tâm để thiết lập một "mức giá thu hồi" (Recovery Price) công bằng cho toàn thị trường.

---

## 1. The Two-Phase Auction Mechanism

Quy trình đấu giá diễn ra trong hai giai đoạn chính:

### Phase 1: Determining the IMM and NOI
- **Inside Market Midpoint (IMM):** Các Dealer gửi lệnh chào mua (Bid) và chào bán (Offer) cho các trái phiếu đủ điều kiện giao hàng (Deliverables). Mức trung bình của các lệnh này tạo ra IMM.
- **Net Open Interest (NOI):** Các Dealer đồng thời gửi yêu cầu thanh lý vật chất (Physical Settlement Requests). Sự chênh lệch giữa lượng bán và lượng mua tạo ra NOI (NOI to Sell hoặc NOI to Buy). [[Tuckman_Serrat#page=381]]

### Phase 2: Determining the Final Price
- Các bên tham gia thị trường (không chỉ Dealer) gửi các lệnh giới hạn (Limit Orders) để khớp với NOI đã xác định ở Phase 1.
- Mức giá cuối cùng được xác định theo phương thức **Đấu giá Hà Lan (Dutch Auction)** để khớp hết toàn bộ khối lượng NOI. Mức giá này sẽ được dùng làm căn cứ thanh toán tiền mặt (Cash Settlement) cho toàn bộ các hợp đồng CDS liên quan. [[Tuckman_Serrat#page=382]]

---

## 2. Case Studies: Success and Failure

### Hertz Case (June 2020) - Success
- **Bối cảnh:** Hertz nộp đơn phá sản.
- **Kết quả:** NOI là 111.5 triệu USD (Sell). Giá IMM là 25.375.
- **Final Price:** 26.375.
- **Payout:** Người mua bảo hiểm nhận được $100 - 26.375 = 73.625$ USD trên mỗi 100 USD mệnh giá. [[Tuckman_Serrat#page=380]]

### Europcar Case (January 2021) - Failure
- **Bối cảnh:** Một ví dụ về ranh giới của sự thất bại trong thiết kế đấu giá.
- **Kết quả:** NOI là €43.3 triệu (Buy). Tuy nhiên, trong Phase 2, lượng lệnh giới hạn chào bán chỉ đạt €35.9 triệu.
- **Hậu quả:** Do không đủ lệnh bán để khớp NOI mua, giá cuối cùng bị đẩy lên mức tối đa là 100.
- **Payout:** Người mua bảo hiểm nhận được 0. Đây là thảm họa cho những người hedging rủi ro tín dụng. [[Tuckman_Serrat#page=384]]

---

## 3. Strategic Considerations: Adjustment Amounts

Để khuyến khích các Dealer cung cấp báo giá trung thực, ISDA áp dụng **Adjustment Amounts** (khoản phạt). Nếu báo giá của một Dealer quá lệch so với IMM cuối cùng (off-market), họ sẽ phải trả tiền phạt. Điều này đảm bảo IMM phản ánh đúng thực tế thị trường. [[Tuckman_Serrat#page=381]]

---

## Evidence / Source Anchors

- Steps for calculating IMM and NOI: [[Tuckman_Serrat#page=381]]
- Dutch auction mechanism for Phase 2: [[Tuckman_Serrat#page=382]]
- Analysis of the Hertz and Europcar outcomes: [[Tuckman_Serrat#page=380]], [[Tuckman_Serrat#page=384]]

## Related

- [[Credit_Default_Swaps_CDS]] — Sản phẩm cơ sở.
- [[Bankruptcy_Resolution_Mechanisms]] — Bối cảnh kích hoạt đấu giá.
- [[Liquidity_Search_Problem]] — Lý do tại sao đấu giá tập trung là cần thiết.
