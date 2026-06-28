# 05_scripts — Layered Engine

> `05_scripts/` hiện đã được module hóa theo tầng. Các file ở root được giữ lại như **compatibility wrappers** để không làm gãy SOP cũ, còn implementation thật nằm trong các thư mục domain bên dưới.

## Layout hiện tại

```text
05_scripts/
├── retrieval/    # search, BM25, semantic, hybrid, deepdive
├── ingestion/    # extract, ingest, inbox, raw scouting, OCR normalization
├── governance/   # audit, bridge, rename, organize, registry maintenance
├── synthesis/    # wisdom, suggestions, daily workflows, visualization helpers
├── graph/        # graph build + index generation
├── ops/          # utility scripts, debug tools, SLA helpers
├── common/       # shared layout/runtime helpers
└── *.py          # wrappers tương thích cho path cũ
```

## Nguyên tắc dùng

- Ưu tiên entrypoint chuẩn: `python librarian.py ...`
- Nếu cần gọi script trực tiếp theo SOP cũ, path root vẫn dùng được:
  - `python 05_scripts/wiki_search.py ...`
  - `python 05_scripts/auto_ingest.py ...`
  - `python 05_scripts/_build_wiki_graph.py`
- Không import logic mới từ wrapper root nếu đang viết code mới. Với code mới, import từ layer thật:
  - `retrieval.wiki_search`
  - `ingestion.auto_ingest`
  - `governance.claim_auditor`
  - `synthesis.auto_synthesis`
  - `graph.gen_index`

## Mapping theo tầng

### `retrieval/`

- `wiki_search.py`
- `semantic_search.py`
- `hybrid_search.py`
- `deepdive_search.py`
- `fts5_engine.py`
- `search_utils.py`

### `ingestion/`

- `auto_ingest.py`
- `extract_pdf.py`
- `extract_pdf_docling.py`
- `exact_extractor.py`
- `inbox_processor.py`
- `raw_scout.py`
- `cleanup_books.py`
- `normalize_ocr_md.py`
- `count_pages.py`

### `governance/`

- `auto_bridge.py`
- `claim_auditor.py`
- `find_orphans.py`
- `organize_nodes.py`
- `rename_node.py`
- `sync_registry.py`
- `sync_synonyms.py`
- `migrate_schema_v4.py`

### `synthesis/`

- `auto_synthesis.py`
- `suggest_ideas.py`
- `daily_quest.py`
- `vis_protocol.py`

### `graph/`

- `_build_wiki_graph.py`
- `gen_index.py`

### `ops/`

- `system_tools.py`
- `debug_page.py`
- `sla_controller.py`
- `sla_logic.py`

## Librarian

```bash
python librarian.py help
python librarian.py search "X"
python librarian.py wisdom "tag"
python librarian.py sync
```

## Colab embedding

Đường chạy Colab một-file:

```bash
python 05_scripts/colab_embed_pipeline.py
```

Script này sẽ:
- cài dependency embedding trên Colab
- chạy `embed_index.py --build`
- zip `wiki_embed.index`, `wiki_embed.meta.json`, `wiki_embed.manifest.json`
- tải `wiki_embed_artifacts.zip` về máy

Sau khi tải về local Windows:

```powershell
powershell -ExecutionPolicy Bypass -File 05_scripts\pull_embed_index.ps1 -Zip "$env:USERPROFILE\Downloads\wiki_embed_artifacts.zip"
```

Script pull sẽ backup artifact cũ sang `.bak`, rồi giải nén ghi đè bộ index hiện tại trong `.cache/`.

## Temp output

Artifacts tạm vẫn phải đi vào `04_outputs/temp/`, `.cache/`, hoặc `graphify-out/` tùy loại; không dùng root repo làm scratch space.
