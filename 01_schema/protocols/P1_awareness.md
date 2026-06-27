# P1 — TEMPORAL & CONCEPTUAL AWARENESS
> Load khi: dùng khái niệm tài chính và cần kiểm tra CURRENT/LEGACY/DEPRECATED.

## Phân loại 3 trạng thái

| Trạng thái | Định nghĩa | Cách xử lý |
|-----------|-----------|-----------|
| 🟢 CURRENT | Đang dùng chính thức trên thị trường | Dùng trực tiếp |
| 🟡 LEGACY | Tồn tại song song, đang bị thay thế | Ghi: `[LEGACY — đang thay bởi X]` |
| 🔴 DEPRECATED | Đã ngừng dùng chính thức | Ghi: `[DEPRECATED — thay bởi X từ năm Y]`; chỉ dùng để so sánh lịch sử |

## Ví dụ chuẩn
- `LIBOR` 🔴 → `SOFR` (USD) / `SONIA` (GBP) / `€STR` (EUR) từ 2023
- `Basel II` 🔴 → `Basel III / CRR3` (đang triển khai) 🟡
- `Bretton Woods` 🔴 → chỉ dùng khi phân tích lịch sử

## Quy tắc
1. User dùng khái niệm DEPRECATED → trả lời bằng CURRENT, giải thích chuyển dịch.
2. So sánh cơ chế → trình bày song song OLD vs NEW, nêu điểm khác biệt cấu trúc.
3. Không chắc → gắn `[TEMPORAL: VERIFY]`, tìm [WEB] trước khi kết luận.
4. **Semantic Connection Awareness**: Khi tạo node mới, PHẢI chạy `auto_bridge.py --report` hoặc tự kiểm tra: "Có ai link đến node này chưa?". Nếu chưa, PHẢI tìm node cha/liên quan để đặt link ngược lại.


## Ví dụ output
> ❌ "LIBOR + 200bps là spread thông thường..."
> ✅ "SOFR + 200bps [CURRENT]. LIBOR [DEPRECATED 2023] đã thay thế theo ARRC fallback."
