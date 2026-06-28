# Wiki Link — Cấu trúc hệ thống (chi tiết)

> Tài liệu mô tả kiến trúc · vận hành · yêu cầu của repo Wiki Link.
> Sinh ngày: 2026-06-27 · Snapshot: 888 wiki nodes · 293 raw sources · graph.json ~14MB · FAISS index ~75MB.

---

## 1. Hệ thống này là gì

Một **knowledge base nguyên tử (atomic knowledge graph)** chuyên về macro / fixed-income / plumbing tiền tệ, vận hành theo mô hình **"Semantic Cache"**:

- **Mode SYNTHESIS** — ăn (ingest) sách/paper thô → chưng cất thành các *wiki node* (definition / mechanism / relationship…).
- **Mode DEEP** — phân tích hệ thống tài chính theo logic "Treasury-First plumbing", bắt buộc đi qua **5 Lenses**: `Top-down → Macro → Plumbing → Treasury → Timing`.

Mọi thao tác đi qua **một entry point duy nhất: `librarian.py`** (76KB, v2.1). Source-of-truth là các file `.md`; mọi thứ khác (FAISS index, graph.json, db) là **artifact phái sinh, regenerable**.

---

## 2. Bản đồ thư mục (layout vật lý)

```
D:\AI\Wiki Link\
│
├── librarian.py            ★ ENTRY POINT — CLI điều phối mọi pipeline (StepRunner)
├── CLAUDE.md / GEMINI.md   ← system prompt cho từng agent (load order, 5 Lenses)
├── system.md               ← SOP đầy đủ: BLOCK 0 hard rules → BLOCK 4 pointer map
├── Readme.md / Hard rule for writing.md
│
├── 01_schema/              ── "Hiến pháp" của hệ thống (luật, không phải dữ liệu)
│   ├── hot.md              · L0 hot cache — session context, god-nodes (đọc mỗi session)
│   ├── memory.md           · index trạng thái bền vững
│   ├── schema.md (v4.0)    · spec frontmatter node + 11 taxonomy types
│   ├── alias_registry.md   · chống trùng node (Rule 0 pre-check)
│   ├── protocols/          · P1_awareness · P2_epistemic · P3_mechanistic · P4_output
│   ├── workflows/          · W1_query · W2_ingest · W3_research · W4_memory · W5_secondary_ingest
│   ├── templates/          · T_MODE_DEEP.md (khung 8-block + 5 Lenses)
│   ├── registry/           · registry_*.md + router_rules.yml + synonyms.yml
│   ├── index/              · index_concepts/mechanisms/… (auto-gen)
│   └── Audit_Protocol.md · SPEC_SEARCH_V1.md · VIS_Protocol.md · Mermaid_Guidelines.md
│
├── 02_sources/  (293 files)── RAW: sách/paper trích xuất ra .md  ⚠️ private (bản quyền)
│   ├── books/  academic/  bindseil/  Clipping/  deep-research/  Inbox/
│
├── 03_wiki/    (888 nodes) ── KNOWLEDGE GRAPH — đơn vị tri thức nguyên tử
│   ├── mechanisms/   481   ← "X vận hành thế nào" (lõi của hệ thống)
│   ├── concepts/     137   definitions/ 101   perspectives/ 43   domains/ 37
│   ├── relationships/ 30   evidence/ 23   conventions/ 19   contradictions/ 11
│   └── syntheses/      4   glossary/ 2
│
├── 04_outputs/             ── Sản phẩm trung gian / nghiên cứu
│   ├── staged_nodes/       · node ứng viên CHƯA merge (refined/batch_*)
│   ├── research/  reports/  audits/  drafts/  calibration/  temp/
│
├── 05_scripts/  (~40 .py)  ── Engine layer mà librarian.py gọi
│   ├── wiki_search · hybrid_search · semantic_search · deepdive_search · fts5_engine
│   ├── embed_index · _build_wiki_graph · gen_index · auto_bridge · find_orphans
│   ├── auto_ingest · auto_synthesis · claim_auditor · rename_node · raw_scout
│   ├── extract_pdf(_docling) · exact_extractor · inbox_processor · organize_nodes
│   └── colab_embed_index.ipynb + COLAB_EMBED_README + pull_embed_index.ps1
│
├── 06_publish/             ── Bản thảo công bố cuối (note/draft theo ngày)
│
├── .cache/                 ── ARTIFACT phái sinh (gitignored, regenerable)
│   ├── wiki_embed.index    · FAISS IndexFlatIP, e5-base 768-dim (~75MB)
│   ├── wiki_embed.meta/manifest.json · metadata + mtime tracking (incremental)
│   ├── wiki_index.db       · SQLite FTS5 (BM25)
│   └── wiki_search_cache.pkl · ingest_queue_state.json
│
├── graphify-out/           · graph.json (14MB) · graph.html · GRAPH_REPORT.md · detect cache
└── memory/                 · workflow_triad_analysis.md (memory bền vững)
```

**Nguyên tắc phân tầng:**
`01_schema` = LUẬT · `02_sources` = INPUT thô · `03_wiki` = TRI THỨC chưng cất · `04_outputs` = nháp · `05_scripts` = ENGINE · `.cache`+`graphify-out` = ARTIFACT.

---

## 3. Kiến trúc điều khiển — `librarian.py` + StepRunner

`librarian.py` không tự làm logic nặng; nó là **orchestrator** điều phối các script trong `05_scripts/` theo từng *pipeline* gồm các *step* (qua class `StepRunner`, hỗ trợ `--skip` / `--only`).

```
                         ┌───────────────────────────────────────┐
   python librarian.py → │  main() argparse → cmd dispatch        │
        <cmd> <targets>  │  StepRunner(skip_set, only_set)        │
                         └───────────────────────────────────────┘
                                          │  gọi run_script(...)
        ┌─────────────┬─────────────┬─────┴───────┬─────────────┬──────────────┐
        ▼             ▼             ▼             ▼             ▼              ▼
   [QUẢN TRỊ]    [TÌM KIẾM]     [INGEST]     [TỔNG HỢP]     [BẢO TRÌ]      [EMBED]
   status        search         stage        wisdom         health         embed
   sync          deepdive       review       audit          staleness      (--incremental
   ingest        scout          extract                     rename          / --build)
   daily         section        inbox                       validate
   batch                                                    writeback
```

### Các pipeline chính (từ `PIPELINE_HELP`)

| Lệnh | Chuỗi step | Dùng khi |
|---|---|---|
| `status` | thống kê hệ thống | đầu session |
| `sync` | build_graph → gen_index → staleness | sau khi sửa node / thêm wikilink |
| `ingest` | build_graph → gen_index → **auto_bridge** → staleness | sau khi SPAWN/EXPAND node mới |
| `health` | find_orphans → missing_thesis → staleness → suggest_ideas | định kỳ |
| `daily` | suggest_ideas → orphans → staleness → missing_thesis | đầu ngày |
| `search` | wiki_search (RRF) · `--semantic` · `--deep` heatmap | trước khi tạo node / khi viết |
| `deepdive` | detect (node mỏng) → drill raw → draft proposal | node confidence thấp / có `[LLM]` |
| `wisdom <tag>` | staleness_check → auto_synthesis (hub map + tension pairs + LLM essay) | trước/sau khi ingest topic |
| `audit <file>` | claim_audit **F.I.T.S.E.R.B.V.L** 9 điểm | trước khi merge node |
| `stage`/`review` | auto_ingest: scan books → coverage → stage drafts → accept | bán-tự-động W2 |
| `extract` | extract_pdf (PDF→MD) | thêm source PDF mới |
| `embed` | embed_index `--incremental` (track mtime) | sau khi tạo node |
| `rename` | heal `[[wikilinks]]` → rename file → sync | đổi tên node an toàn |

---

## 4. Vòng đời dữ liệu (data flow end-to-end)

```
 ┌──────────┐   extract     ┌──────────────┐  W2/W5 ingest   ┌─────────────┐
 │  PDF/     │ ───────────►  │ 02_sources/   │ ─────────────►  │ 04_outputs/  │
 │  Clipping │ extract_pdf   │  *.md (RAW)   │ auto_ingest     │ staged_nodes │
 │  / Inbox  │ (+docling)    │  293 files    │ stage           │ (ứng viên)   │
 └──────────┘               └──────────────┘                 └──────┬───────┘
                                   │                                 │ review / audit
                                   │ raw_scout / deepdive drill      │ (F.I.T.S.E.R.B.V.L)
                                   ▼                                 ▼  accept
                            (Rule 0: alias_registry check)   ┌──────────────────┐
                                                             │  03_wiki/ (888)   │
                                                             │  atomic nodes     │
                                                             │  + [[wikilinks]]  │
                                                             └───┬──────────┬────┘
                              librarian.py sync / ingest         │          │
                  ┌───────────────────────────────────────┐     │          │
                  ▼                    ▼                    ▼     ▼          ▼
            _build_wiki_graph    gen_index          embed_index    auto_bridge
            → graph.json/html    → index/*.md       → FAISS+FTS5   → link orphans
                  │                                       │
                  └────────────┐         ┌───────────────┘
                               ▼         ▼
                        ┌────────────────────────────┐    auto_synthesis (wisdom)
                        │   SEARCH / SYNTHESIS LAYER   │ ──► 04_outputs/research
                        └────────────────────────────┘    MODE DEEP analysis
                                                            └──► 06_publish/
```

---

## 5. Tầng tìm kiếm (search stack — escalation 3 nấc)

```
 Query
   │
   ├─ Nấc 1  wiki_search        → BM25/FTS5 (SQLite) + boost   ← lookup nhanh, mặc định RRF
   │         fts5_engine.py        .cache/wiki_index.db
   │
   ├─ Nấc 2  semantic_search    → FAISS IndexFlatIP, cosine    ← truy vấn ngữ nghĩa
   │         (--semantic)          model: multilingual-e5-base (768-dim, VI+EN)
   │
   ├─ Nấc 2b hybrid_search      → Fuzzy + Heatmap + Parallel   ← tổng hợp sâu (raw heatmap)
   │         (--deep)              RRF fusion BM25 ⊕ semantic
   │
   └─ Nấc 3  deepdive_search    → detect node mỏng → drill raw → draft expansion
             (deepdive)            cho node confidence thấp / có [LLM] placeholder
```

Đọc theo **Two-Pass** (CLAUDE.md): Pass 1 chỉ đọc thesis line/score để quyết định; Pass 2 đọc tối đa 2 node/cycle, ưu tiên `type=WIKI`.

---

## 6. Lược đồ node (schema v4.0) — đơn vị nguyên tử

11 loại node, frontmatter bắt buộc đầy đủ:

```yaml
title · aliases[] · type · tags[] · status · confidence(1-5) · half_life_years
school · superseded_by/date · expert_lens · provenance · thesis(1 câu, BẮT BUỘC)
source_refs[{file,page}] · created · updated
```

5 luật bất biến: **MD-First · Citation-First (`[RAW]`/`[WIKI]`/`[WEB]`/`[LLM]`) · Expand-not-Overwrite · Collision-Prevention · No-Flattening** (giữ nguyên mâu thuẫn giữa nguồn).

Phân bố nghiêng mạnh về **mechanisms (481/888 ≈ 54%)** — đúng triết lý "ưu tiên cơ chế vận hành hơn mô tả bề mặt".

---

## 7. Tầng phân tích — 5 Lenses / MODE DEEP

```
Top-Down Entry  →  Macro Layer  →  Plumbing Layer  →  Treasury Layer  →  Timing Layer
(đặt khung)        (Regime +        (T-account +        (so-what cho      (Past/Present/
                    Policy Anchor)   4-Component*)        desk thực tế)     Future, cross-cut)
                                          │
            * Plumbing 4-Component: (1) Entity+Flow Tracing (2) Stakeholder Matrix
                                    (3) Liquidity Narrative (4) Asset-Price Mechanical Linkage

→ Feedback/Boundary → ASCII Diagram → Conclusion → Next Steps   (8 blocks)
```

Kỷ luật ngôn ngữ (BLOCK 0): **cấm tuyệt đối** văn phong giật tít/ẩn dụ/game ("Kill", "vũ khí", "tipping point", "in real time"…) — chỉ mô tả cơ chế. Bắt buộc có mục **"Treasury Insight"** + ưu tiên lens **TQN (Trần Quang Nghĩa)** truy vết T-account.

---

## 8. Đặc thù vận hành: tách Local (CPU) ↔ Colab T4 (GPU)

Vì embedding nặng, compute được tách:

```
┌─ LOCAL (Claude Code, CPU) ─────────────┐        ┌─ COLAB T4 (GPU) ───────────────┐
│ đọc 02_sources → sinh/sửa .md          │        │ git clone --depth 1            │
│ librarian.py sync  (graph/link only)   │ ─push─► │ pip install st+faiss           │
│ KHÔNG chạy embed local                 │  .md   │ embed_index.py --build (GPU)    │
│ pull_embed_index.ps1 → .cache/         │ ◄─zip─ │ zip wiki_embed.* → download     │
└─────────────────────────────────────────┘        └─────────────────────────────────┘
```

- Transport `.md` = Git/GitHub (`hieunt795/llm-wiki`, **private** vì chứa full-text sách).
- Artifact index (~90MB) = kênh riêng (browser download / Drive), **không commit** (.gitignore).
- Trên Colab dùng `--build` (full), KHÔNG `--incremental` (mtime đổi sau clone → incremental cross-machine sai).
- Cùng model `multilingual-e5-base` 2 máy → index tương thích.

---

## 9. Tóm tắt một câu

> **Wiki Link** = một *atomic knowledge graph* macro/fixed-income (888 node, lõi là 481 mechanism), source-of-truth là `.md`, điều phối qua một CLI duy nhất `librarian.py` (orchestrator StepRunner gọi ~40 script engine), tìm kiếm 3-nấc BM25→semantic→deepdive trên FAISS+FTS5, ingest có quality-gate (Rule 0 chống trùng + audit F.I.T.S.E.R.B.V.L), phân tích bắt buộc qua **5 Lenses Treasury-First**, và tách compute embedding sang Colab GPU để giữ máy local nhẹ.
