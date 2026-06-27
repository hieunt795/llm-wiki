# 06_publish — Content Publishing

> Nơi lưu các notes, responses, và research đã được polish để đăng lên mạng xã hội hoặc export sang các content formats khác.

## Cách dùng

Khi bạn thấy một response hay hoặc muốn save một research note:
- Nói: "Print ra file markdown" hoặc "Lưu response này vào Publish"
- AI sẽ tạo file `.md` trong đây với format sạch, sẵn sàng copy-paste

## Naming convention

```
YYYY-MM-DD_[topic-slug]_[platform].md

Ví dụ:
  2026-04-28_financial-repression-vietnam_facebook.md
  2026-04-28_repo-spike-2019_linkedin.md
  2026-04-28_corridor-system-explainer_note.md
```

## Platform tags

| Tag | Dùng khi |
|-----|---------|
| `_facebook` | Post FB — ngắn, có hook đầu |
| `_linkedin` | Post LinkedIn — chuyên nghiệp hơn |
| `_note` | Personal note, không gắn platform cụ thể |
| `_thread` | Thread dài (Twitter/X) |
| `_export` | Export sang format khác (docx, pdf...) |

## Không phải wiki node

File trong đây **không được cite** trong wiki. Đây là content layer, không phải knowledge layer.
Nếu research note có giá trị dài hạn → ingest vào `03_wiki/` qua W2/W5 pipeline.
