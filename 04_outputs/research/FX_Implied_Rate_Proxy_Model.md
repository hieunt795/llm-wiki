# GUIDE: FX Implied Rate Proxy Model
> Thiết lập bộ đo lường khan hiếm thanh khoản từ dữ liệu Swap Points.

## 1. Mục tiêu (Objective)
Khi không có quyền truy cập vào dữ liệu **Cross-currency Basis** (thường yêu cầu Terminal Bloomberg/Reuters đắt tiền), nhà phân tích có thể sử dụng dữ liệu **FX Swap Points** công khai để xây dựng một bộ đo lường (Proxy) cho sự khan hiếm thanh khoản USD.

## 2. Quy trình tính toán (Step-by-Step)

### Bước 1: Thu thập dữ liệu đầu vào
- **Spot Rate ($S$):** Tỷ giá giao ngay hiện tại (e.g., USD/VND).
- **Swap Points:** Điểm kỳ hạn niêm yết (thường là kỳ hạn 1 tháng hoặc 3 tháng).
- **Domestic Rate ($r_d$):** Lãi suất thị trường tiền mặt nội tệ (e.g., VNIBOR 3M).
- **Market Foreign Rate ($r_f^{mkt}$):** Lãi suất thị trường ngoại tệ quốc tế (e.g., SOFR 3M).

### Bước 2: Tính toán Lãi suất ngầm định (Implied Rate)
Sử dụng công thức biến đổi từ CIP:
$$r_f^{implied} = \left[ \frac{S + \text{Swap Points}}{S} \times (1 + r_d \times \delta) \right] - 1$$

### Bước 3: Xác định Liquidity Gap (The Proxy Basis)
$$\text{Liquidity Gap} = r_f^{implied} - r_f^{mkt}$$

---

## 3. Giải mã kết quả (Interpretation)

| Kết quả (Gap) | Ý nghĩa kỹ thuật | Hành động của Quant |
| :--- | :--- | :--- |
| **Gap $\approx 0$** | Thị trường cân bằng. CIP được duy trì. | Không có tín hiệu bất thường. |
| **Gap $> 50$ bps** | Bắt đầu có dấu hiệu thắt chặt thanh khoản ngoại tệ. | Theo dõi sát sao các phiên Repo của NHTW. |
| **Gap $> 150$ bps** | **USD Funding Squeeze.** | Cảnh báo rủi ro hệ thống. Khả năng cao có sự can thiệp của NHTW (bán ngoại tệ hoặc bơm Repo). |

---

## 4. Mental Model: Tại sao mô hình này hoạt động?
Mô hình này hoạt động dựa trên nguyên tắc **No-arbitrage**. Nếu ranh giới giữa lãi suất ngầm định và lãi suất thực tế bị giãn ra quá rộng mà không có ai nhảy vào thu lợi nhuận, điều đó chứng tỏ có **Rào cản (Frictions)**. Rào cản đó chính là sự khan hiếm thanh khoản hoặc rủi ro đối tác khiến các ngân hàng không thể/không muốn cho vay tiền mặt.

---
**Tham chiếu Wiki:**
- [[FX_Swap_Engineering]]
- [[Interest_Rate_Parity]]
- [[Cross_Currency_Basis]]
