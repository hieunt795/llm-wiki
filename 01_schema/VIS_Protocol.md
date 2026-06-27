# VERIFIED INSTITUTIONAL SEARCH (VIS) PROTOCOL (V1.0)

Quy trình này được thiết kế để triệt tiêu hiện tượng ảo giác (hallucination) và đảm bảo mọi dữ liệu đưa vào hệ thống Wiki Link đều có nguồn gốc từ các định chế tài chính uy tín bậc nhất.

---

## 1. Mandatory Consultation Phase (Bắt buộc hỏi User)
Trước khi thực hiện bất kỳ lệnh `google_web_search` nào, Agent **PHẢI** hỏi User 4 câu hỏi định hướng:

1.  **Timeframe (Thời gian):** Dữ liệu cần tìm thuộc năm nào? (Ví dụ: Dự báo 2026, hay dữ liệu thực tế 2024).
2.  **Institutional Focus (Nguồn ưu tiên):** Chỉ tìm trên các domain nào? (Ví dụ: `bis.org`, `imf.org`, `fed.gov`, `goldmansachs.com`).
3.  **Specific Indicators (Chỉ số cụ thể):** Cần tìm con số chính xác của biến số nào? (Ví dụ: CAR, NPL, Fiscal Deficit, Basis Trade Volume).
4.  **Evidence Type:** Cần link PDF gốc, Chart/Figure hay trích dẫn văn bản?

---

## 2. Execution Layers (Các tầng thực thi)

### Layer 1: Restricted Search (Tìm kiếm giới hạn)
Agent sử dụng toán tử nâng cao để ép kết quả vào vùng an toàn.
- **Cấu trúc:** `site:[domain] "keyword" filetype:pdf`
- **Mục tiêu:** Loại bỏ tin tức báo chí, chỉ lấy báo cáo kỹ thuật.

### Layer 2: Verification Turn (Kiểm chứng Link)
Agent không được trả về Link ngay khi thấy trên Google.
1.  Sử dụng `web_fetch` để truy cập thử vào URL.
2.  Nếu báo lỗi 404, 403 hoặc không có nội dung, Agent phải tự động tìm nguồn thay thế hoặc báo cáo lỗi.
3.  Chỉ những Link "Live" mới được đưa vào báo cáo.

### Layer 3: Deep Extraction (Trích xuất sâu)
Dữ liệu trả về phải bao gồm:
- **Reference:** Tên báo cáo, trang (nếu có), ngày phát hành.
- **Hard Data:** Con số cụ thể kèm đơn vị tính.
- **Visual Context:** Mô tả nội dung của Figure/Chart được nhắc đến trong tài liệu.

---

## 3. Data Integration (Tích hợp dữ liệu)
Mọi dữ liệu tìm được qua quy trình VIS khi đưa vào Domain Notes hoặc Chapters phải được gắn tag:
- `[WEB]` + `[VIS Verified]` + `[Link]`

---
**Trạng thái:** ACTIVE
**Vị trí lưu trữ:** `01_schema/VIS_Protocol.md`
