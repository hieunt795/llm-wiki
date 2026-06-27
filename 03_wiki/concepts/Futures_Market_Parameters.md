---
title: Futures Market Parameters
aliases:
- Open Interest
- Volume
- Front Month
- Prompt Month
- Nearby Contract
- Back Month
type: concept
tags: []
status: verified
confidence: 4
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: "Salih Neftci"
provenance: "Neftci_Principles.md"
thesis: Các tham số cốt lõi định nghĩa một hợp đồng tương lai (Futures), áp dụng cho
  cả tài chính và hàng hóa, nhấn mạnh vào tính thanh khoản và các loại rủi ro basis.
source_refs:
- file: Neftci_Principles.md
  page: 1
created: '2026-04-16'
updated: '2026-04-16'
---

# Futures Market Parameters

## Overview
Hợp đồng Tương lai (Futures) là công cụ chuẩn hóa được giao dịch trên các sàn tập trung (CME, ICE, NYMEX). Khác với Forward (OTC), Futures yêu cầu sự chuẩn hóa nghiêm ngặt về khối lượng, phẩm cấp và thời gian giao hàng. [[Neftci_Principles#page=212]]

## Key Parameters

### 1. Volume vs. Open Interest
Hai chỉ số này thường bị nhầm lẫn nhưng phản ánh các khía cạnh khác nhau của thanh khoản và cam kết thị trường:
- **Volume (Khối lượng giao dịch):** Tổng số hợp đồng được khớp lệnh trong một phiên giao dịch. Phản ánh mức độ hoạt động tức thời.
- **Open Interest (OI - Hợp đồng mở):** Tổng số hợp đồng đang lưu hành (chưa được thanh lý hoặc tất toán) vào cuối ngày.
    - Mỗi hợp đồng OI đại diện cho một cặp (1 Người mua + 1 Người bán). Để tính tổng OI, chỉ cần cộng dồn từ một phía (hoặc người mua, hoặc người bán).
    - OI phản ánh lượng rủi ro (risk) đang được giữ trên thị trường. [[Neftci_Principles#page=213]]

### 2. Contract Months (Kỳ hạn)
- **Front Month (Tháng gần) / Prompt Month / Nearby / Nearest:** Hợp đồng có ngày đáo hạn gần nhất với hiện tại. Thường là hợp đồng có thanh khoản cao nhất.
- **Back Months (Các tháng xa):** Các hợp đồng có ngày đáo hạn xa hơn. Thanh khoản thường thấp hơn và chi phí giao dịch (transaction costs) cao hơn.
- **Liquidity Selection:** Các trader tìm kiếm chi phí giao dịch thấp nhất thường chọn Front Month. Các mục đích khác (như phòng hộ dài hạn) mới chọn Back Months. [[Neftci_Principles#page=214]]

## Case Study: WTI Crude Oil Contract (CME NYMEX/Globex)
Hợp đồng Dầu thô WTI là một trong những chuẩn benchmark quan trọng nhất toàn cầu, minh họa 11 tham số kỹ thuật cốt lõi:

| Tham số | Chi tiết (WTI) |
| :--- | :--- |
| **1. Contract Size** | 1000 barrels (bbl) (~42,000 US gallons). |
| **2. Units of Trading** | Bội số của 1000 bbl. |
| **3. Minimum Fluctuation** | $0.01 per bbl. |
| **4. Price Quote** | US Dollars và cents per bbl. |
| **5. Contract Months** | Niêm yết 9 năm tới: các tháng liên tiếp cho 5 năm đầu; sau đó là tháng 6 & 12. |
| **6. Delivery** | FOB tại Cushing, Oklahoma (hub lưu trữ/đường ống chính). |
| **7. Delivery Grades** | Light sweet crude oil (Sulfur < 0.42%). Bao gồm WTI, Brent (chiết khấu)... |
| **8. Last Trading Day** | Ngày làm việc trước ngày 15 của tháng hợp đồng. |
| **9. Last Delivery Day** | Từ ngày 1 đến ngày cuối cùng của tháng giao hàng. |
| **10. Trading Hours** | Open outcry ( Chicago time) & Electronic (Globex). |
| **11. Daily Price Limit** | ±$10.00 per bbl so với giá settlement ngày hôm trước. |

[[Neftci_Principles#page=213]]

## Basis Risk in Commodities
Rủi ro Basis (chênh lệch giữa giá giao ngay S và giá tương lai F) trong hàng hóa phức tạp hơn tài chính do tính hữu hình:
1.  **Locational Basis Risk:** Chênh lệch giá do khoảng cách địa lý giữa điểm sản xuất và điểm giao hàng chuẩn.
2.  **Product/Quality Basis Risk:** Chênh lệch do phẩm cấp hàng hóa thực tế khác với chuẩn của sàn.
3.  **Calendar (Spread) Basis Risk:** Chênh lệch do sự khác biệt giữa thời điểm cần hàng vật chất và ngày đáo hạn hợp đồng. [[Neftci_Principles#page=214]]

## Evidence / Source Anchors
- [[Neftci_Principles.md#page=212-214]] — Định nghĩa chi tiết về các tham số Futures và rủi ro Basis.


## Related

- [[Money_Market_Futures_And_Convexity]]
- [[Bond_Futures_Contract_Design]]
