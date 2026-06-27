# 05_scripts — Pipeline Tools

> Tất cả script Python của Wiki Link system.
> Chạy từ root Wiki Link: `python 05_scripts/<script>.py`

## Scripts

| File | Mục đích |
|------|---------|
| `wiki_search.py` | Tìm kiếm trong wiki nodes |
| `hybrid_search.py` | Hybrid search v2.5 (Fuzzy + Heatmap + Parallel) |
| `exact_extractor.py` | Trích xuất đoạn văn từ raw sources |
| `auto_synthesis.py` | Wisdom Engine — hub map + tension pairs |
| `_build_wiki_graph.py` | Build knowledge graph từ wiki nodes |
| `gen_index.py` | Sinh index.md cho wiki |
| `claim_auditor.py` | Audit claim quality trong nodes |
| `auto_bridge.py` | Tự động phát hiện và tạo bridge giữa nodes |
| `deepdive_search.py` | Deep dive search kết hợp wiki + raw |
| `find_orphans.py` | Tìm node không có wikilink |
| `rename_node.py` | Đổi tên node + update tất cả wikilinks |
| `raw_scout.py` | Scout raw sources cho concepts |
| `extract_pdf.py` | Extract text từ PDF |
| `auto_ingest.py` | Auto ingest pipeline |
| `suggest_ideas.py` | Đề xuất node mới từ gaps |
| `daily_quest.py` | Daily learning quest |
| `system_tools.py` | Utilities dùng chung |
| `vis_protocol.py` | Visualization helpers |

## Librarian (entry point chính)

```bash
python librarian.py help          # xem tất cả commands
python librarian.py search "X"    # tìm kiếm
python librarian.py wisdom "tag"  # chạy synthesis
python librarian.py sync          # sync graph + index
```

## Temp output

Scripts tạo file tạm → lưu vào `04_outputs/temp/` (không cite, không commit).
