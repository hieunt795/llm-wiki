# Inbox — Staging Area for Unclassified Sources

> **Mục đích:** Nơi drop file tạm thời khi chưa biết phân loại vào đâu.
> Sau khi drop vào đây, nhờ AI chạy **Inbox Triage** để phân loại và route đúng folder.

## Cách dùng

1. Drag & drop file (.md, .pdf) vào thư mục này
2. Trong chat: "Phân loại file trong Inbox" hoặc "Triage Inbox"
3. AI sẽ chạy W5 Phase 0-T (Triage) → đề xuất label + folder đích
4. Bạn confirm → AI move file + bắt đầu ingest

## Labels có thể được gán

| Label | Folder đích |
|-------|-------------|
| `[RAW-BOOK]` | `books/` |
| `[RAW-OFFICIAL]` | `official_reports/` |
| `[RAW-ACADEMIC]` | `academic/` |
| `[RAW-CLIP]` | `Clipping/` |
| `[RAW-DR-LLM]` | `deep-research/` |
| `[RAW-OPINION]` | `Clipping/` |
| `[UNVERIFIED]` | Giữ ở Inbox, cần review thủ công |

## Không ingest trực tiếp từ Inbox

File trong Inbox KHÔNG được cite trực tiếp trong wiki nodes cho đến khi đã được triage và move ra folder đúng.
