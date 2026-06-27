---
title: Unified Ledger Concept
aliases:
- Unified Ledger
- Common Venue Platform
type: mechanism
tags:
- monetary-system
- infrastructure
- tokenization
status: verified
confidence: 1
half_life_years: 10
school: ''
superseded_by: null
superseded_date: null
expert_lens: ''
provenance: TBD
thesis: '**Unified Ledger (Sổ cái hợp nhất)** là một loại cơ sở hạ tầng thị trường
  tài chính (FMI) mới, nơi tiền tệ của ngân hàng trung ương, tiền gửi ngân hàng thương
  mại và các tài sản được mã hóa cùng tồn tại trên một nền tảng lập trình chung.'
source_refs: []
created: '2026-04-13'
updated: '2026-04-16'
source: https://www.bis.org/publ/arpdf/ar2023e3.htm
---

# Unified Ledger Concept

## Mechanism

**Unified Ledger (Sổ cái hợp nhất)** là một loại cơ sở hạ tầng thị trường tài chính (FMI) mới, nơi tiền tệ của ngân hàng trung ương, tiền gửi ngân hàng thương mại và các tài sản được mã hóa cùng tồn tại trên một nền tảng lập trình chung.

Thay vì dựa trên các cơ sở dữ liệu silo (tách biệt) được kết nối qua hệ thống gửi tin nhắn (messaging), sổ cái hợp nhất cho phép tất cả các thành phần tương tác trực tiếp trong một môi trường thực thi duy nhất.

> [!IMPORTANT]
> Mục tiêu không phải là "một sổ cái thống trị tất cả", mà là tạo ra các "Common Venues" (Địa điểm chung) cho các ứng dụng cụ thể như tài trợ chuỗi cung ứng, thanh toán xuyên biên giới hoặc chứng khoán hóa nợ tư nhân. [extracted]

### Thành phần cấu tạo
- **Data Environment (Môi trường dữ liệu)**: Chứa các biểu diễn kỹ thuật số của tiền và tài sản trong các phân vùng (partitions) riêng biệt, đảm bảo tính bảo mật và quyền sở hữu.
- **Execution Environment (Môi trường thực thi)**: Nơi các hợp đồng thông minh (smart contracts) thực hiện các lệnh chuyển giao dựa trên các điều kiện thực tế (ví dụ: giao hàng thành công -> tự động thanh toán).
- **Common Governance (Quản trị chung)**: Khung quy tắc xác định cách các thành phần tương tác, tiêu chuẩn bảo mật và quyền truy cập. [extracted]

### Lợi ích đối với Private Credit
Việc đưa các khoản vay [[Private_Credit]] lên một sổ cái hợp nhất cho phép:
1. **Minh bạch hóa dòng tiền**: Nhà đầu tư có thể theo dõi thời gian thực việc trả nợ của doanh nghiệp.
2. **Atomic Payout**: Lợi tức được phân phối ngay lập tức cho các bên liên quan khi doanh nghiệp thanh toán, giảm rủi ro đọng vốn tại các khâu trung gian.
3. **Data Control**: Sử dụng công nghệ mã hóa (Encryption) để chia sẻ dữ liệu thẩm định (due diligence) mà không làm lộ bí mật kinh doanh. [inferred]

### Hình ảnh minh họa (Idea)
> **Phân vùng Bảo mật**: Vẽ một vòng tròn lớn (Unified Ledger). Bên trong chia thành nhiều ô vuông nhỏ (Partitions). Giữa các ô vuông có các tia sét (Smart Contracts) kết nối chúng lại khi có giao dịch. Một vạch khóa (Lock) ở mỗi ô vuông tượng trưng cho việc chỉ chủ sở hữu mới có quyền truy cập dữ liệu bên trong.

## Evidence / Source Anchors
- [extracted] [BIS Annual Economic Report 2023, "Blueprint for the future monetary system", 2023](https://www.bis.org/publ/arpdf/ar2023e3.htm)
- [researched] [BIS Quarterly Review, March 2026](https://www.bis.org/publ/qtrpdf/r_qt2603.pdf)


## Related

- [[Tokenized_Monetary_System]]
- [[Interest_Rate_Swap_Plain_Vanilla]]
