---
type: mechanism
trigger: "Các công ty thương mại xuất/chấp nhận hóa đơn thanh toán chậm"
output: "Giao dịch tạo ra nguồn cho vay (lending) trong nền kinh tế"
constraints: ["Thời hạn và đơn vị tiền tệ tự do đàm phán"]
sources: ["Fixed Income - Alexander During-5.pdf"]
confidence: low
provenance: extracted
created: 2026-04-13
chapter: 4
---

# Trade Credit

## Cơ chế

**Trade credit** (Tín dụng thương mại thông qua buôn bán) thường bị bỏ qua trong phân tích vĩ mô, nhưng nó là một **nguồn cung cấp khoản vay quy mô lớn**. Khi hàng hóa/dịch vụ được giao và được thanh toán trả sau (in arrears), nó tương đương với việc nhà cung cấp đang **cấp một khoản vay doanh nghiệp** cho người mua. [extracted] [[Fixed Income - Alexander During-5.pdf#page=9]]

### Quản lý Bảng cân đối Kế toán

Các bộ phận ngân quỹ doanh nghiệp (corporate treasuries) có thể tích cực quản lý **accounts payable** (phải trả) và **accounts receivable** (phải thu) thay vì chỉ tuân theo tập quán thị trường. 
Ví dụ: Trả nhanh ngoại tệ A nhưng kéo dài thu nợ ngoại tệ B → Bản chất tạo **vị thế short A, long B**, một trạng thái rất khó phát hiện trong hồ sơ kế toán thông thường. [extracted] [[Fixed Income - Alexander During-5.pdf#page=10]]

## Công thức: Collection Period

Đo lường thời gian trung bình giữa lúc hoàn thiện đơn hàng và lúc thực sự được thanh toán: [extracted] [[Fixed Income - Alexander During-5.pdf#page=9]]

$$ \text{Collection period} = \frac{\text{Accounts receivable}}{\text{Total sales}} $$

*(Phương trình 4.1 trong nguyên tác)*

> Do báo cáo tài chính là định kỳ, công ty thường có động lực thu tiền sớm hoặc trì hoãn ngay trước thời điểm "chốt sổ" để làm đẹp collection period. [extracted] [[Fixed Income - Alexander During-5.pdf#page=9]]

## Nguồn

- [[Fixed Income - Alexander During-5.pdf#page=9]] — Trade làm kho cho tín dụng, Equation 4.1
- [[Fixed Income - Alexander During-5.pdf#page=10]] — FX replication via account payable/receivable timing
