---
type: mechanism
aliases: [DvP, Giao tiền nhận phiếu]
trigger: "Cần chặn đứng việc vỡ nợ một chân (Settlement risk/ Herstatt Risk) khi giao dịch"
output: "Trung gian thứ 3 phong tỏa tài sản và chỉ giải ngân cùng lúc chéo cánh cho 2 bên khi đủ hàng đủ tiền"
constraints: ["Tốn phí lưu kho tại trung gian (Warehousing costs), nên gom xử lý theo mẻ thay vì Real-time"]
sources: ["Fixed Income - Alexander During-12.pdf"]
confidence: high
provenance: extracted
created: 2026-04-13
chapter: 11
---

# Delivery Versus Payment

## Cơ chế giao nhận an toàn (DvP)

**Delivery versus payment (DvP)** là giải pháp kỹ thuật diệt gọn hoàn toàn [[Herstatt_Risk]]. Cơ chế này mô phỏng y hệt các "Tài khoản bảo chứng (Escrow accounts)" trong giao dịch bất động sản truyền thống. [extracted] [[Fixed Income - Alexander During-12.pdf#page=15]]

### Quy trình Vận hành
Một nhà băng/tổ chức lưu ký khổng lồ và đáng tin cậy (như [[Book_Entry_Securities_System|GCSD]]) đứng ở giữa cầm cán:
1. Tiếp nhận lệnh chuyển tiền và chuyển chứng khoán của cả A và B.
2. Neo giữ chờ đợi. Chỉ khi nào hệ thống càn quyét xác minh đủ cả Tiền (từ A) và Chứng khoán (từ B) đã đút túi GCSD thì lệnh **Swap chéo mới được thực thi và Finalize đồng thời trong một chớp mắt**. [extracted] [[Fixed Income - Alexander During-12.pdf#page=15]]
3. Nếu 1 bên khuyết, giao dịch bị xé bỏ và ai đem tài sản gì về nhà nấy (Unwind), né được cảnh dở khóc dở cười bị quỵt tiền chân đơn.

### Trade-off
Sự an toàn đẻ ra chi phí. Việc dồn tiền và giấy tờ chết dí vào trung tâm lưu ký DvP đẻ ra chi phí lưu rác (Warehousing). Do đó, thanh toán bù trừ trái phiếu trên thế giới thường không chơi Live (continuous) mà chọn cách gộp sổ theo mẻ gọi là **Settlement cycles**: Đợi đến một giờ cố định trong ngày quét khớp tay 3 tay 4 chéo cánh để bù trừ ròng (Netting benefit), dập tắt mọi đường dây nợ đọng dây chuyền. [extracted] [[Fixed Income - Alexander During-12.pdf#page=15]]

## Nguồn

- [[Fixed Income - Alexander During-12.pdf#page=15]] — Cơ chế khóa Escrow của DvP và sự đánh đổi qua Settlement cycles.
