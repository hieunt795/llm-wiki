# Wiki Link — Atomic Knowledge Engine

Wiki Link là hệ thống quản trị tri thức chuyên sâu, thiết kế để biến tài liệu thô (sách, báo cáo, clipping) thành đồ thị kiến thức nguyên tử (Atomic Knowledge Graph) phục vụ phân tích tài chính kỹ thuật cao. AI agents (Claude, Gemini) vận hành qua `librarian.py` làm entry point duy nhất.

---

## Cấu trúc thư mục

```
Wiki Link/
├── CLAUDE.md                  ← Agent config cho Claude (load đầu tiên)
├── GEMINI.md                  ← Agent config cho Gemini (load đầu tiên)
├── system.md                  ← SOP toàn hệ thống: rules, modes, checklist, pointer map
│
├── 01_schema/                 ← Định nghĩa vận hành
│   ├── hot.md                 ← Session context hiện tại (đọc mỗi session)
│   ├── memory.md              ← Persistent state index
│   ├── schema.md              ← Node frontmatter spec
│   ├── templates/
│   │   └── T_MODE_DEEP.md     ← Template phân tích 5 lenses (MODE DEEP)
│   ├── protocols/             ← P1 Temporal · P2 Epistemic · P3 Mechanistic · P4 Output
│   ├── workflows/             ← W1 Query · W2 Ingest · W3 Research · W4 Memory · W5 Secondary
│   └── registry/             ← Alias, definition, concept registries
│
├── 02_sources/                ← Tài liệu thô, phân theo loại nguồn
│   ├── books/                 → [RAW-BOOK] Sách học thuật/practitioner
│   ├── official_reports/      → [RAW-OFFICIAL] CB, IMF, BIS, FSB reports
│   ├── academic/              → [RAW-ACADEMIC] Working papers, journal articles
│   ├── Clipping/              → [RAW-CLIP] Web articles, Substack, financial press
│   ├── deep-research/         → [RAW-DR-LLM] LLM deep research output (cần verify)
│   └── Inbox/                 → Staging area cho source chưa phân loại
│
├── 03_wiki/                   ← Atomic Knowledge Nodes (trái tim hệ thống)
│   ├── concepts/
│   ├── definitions/
│   ├── mechanisms/
│   ├── evidence/
│   ├── perspectives/
│   ├── relationships/
│   └── contradictions/
│
├── 04_outputs/                ← Output nội bộ
│   ├── research/              ← Wisdom reports, synthesis
│   ├── drafts/                ← Node drafts từ deepdive
│   ├── audits/                ← Audit reports
│   ├── calibration/           ← Calibration logs
│   └── temp/                  ← Scratch space (không cite, không commit)
│
├── 05_scripts/                ← Python pipeline scripts
├── 06_publish/                ← Content đã polish để export/publish
└── memory/                    ← Persistent memory files (rules, plans, logs)
```

---

## Agent Config: Load Order

Mỗi agent đọc theo thứ tự sau khi bắt đầu session:

```
CLAUDE.md / GEMINI.md  →  01_schema/hot.md  →  01_schema/memory.md
→  system.md  →  protocols / workflows on-demand
```

**CLAUDE.md / GEMINI.md** — Agent-specific: mandate 5 lenses, search escalation, read discipline.
**system.md** — SOP đầy đủ: BLOCK 0 Hard Rules · BLOCK 1 Identity · BLOCK 2 Output Modes · BLOCK 3 Session Checklist · BLOCK 4 Pointer Map.

---

## Khung phân tích: 5 Lenses

Mọi phân tích MODE DEEP phải đi đủ 5 lenses theo thứ tự:

| Lens | Vai trò |
|------|---------|
| **Top-down** | Đặt khung câu hỏi, xác định asset/currency/scope |
| **Macro** | Regime lock, policy anchor, institutional constraint |
| **Plumbing** | T-account tracing, transmission chain, stakeholder impact, liquidity choke points |
| **Treasury** | Practitioner logic — "so what for the desk?" |
| **Timing** | Past / Present / Future cross-cutting synthesis |

Template đầy đủ: `01_schema/templates/T_MODE_DEEP.md`

---

## Read Discipline: Two-Pass Pattern

Áp dụng cho mọi file read để tiết kiệm token:

**Pass 1 — Locate** (chạy search, không đọc file):
- BM25/Keyword: `librarian.py search` hoặc `Grep` → file path + line number + thesis line
- Semantic: `librarian.py search --semantic` → ranked list với title + thesis + score
- Nếu thesis line đã đủ → dừng, không cần Pass 2

**Pass 2 — Expand** (tối đa 2 nodes/cycle, ưu tiên WIKI score cao nhất):
- Keyword hit → wiki: `Read(file, offset=line-3, limit=40)`
- Keyword hit → raw: `Read(file, offset=line-3, limit=40)` — không đọc cả chapter
- Semantic hit → wiki: `Read(file, limit=60)` — từ đầu node
- Semantic hit → raw: Grep locate section → Read đoạn match, không đọc từ đầu file

---

## Librarian.py: Lệnh cốt lõi

```bash
python librarian.py status                        # overview đầu session
python librarian.py search "<query>"              # BM25 search
python librarian.py search "<query>" --deep       # BM25 + semantic
python librarian.py search "<query>" --semantic   # semantic only
python librarian.py sync                          # sau khi edit file
python librarian.py embed --incremental           # sau khi tạo node mới
python librarian.py ingest                        # post-ingest sync
python librarian.py wisdom "<tag>"                # synthesis sau ingest chapter
python librarian.py audit <file>                  # 9-point quality check
python librarian.py health                        # orphans + stale + missing thesis
```

---

## Node Quality Gates

Mỗi wiki node (03_wiki/) phải có:
- `thesis` — 1 câu core transmission claim (bắt buộc)
- `confidence` — 1–5, theo số nguồn độc lập xác nhận
- `source_refs` — array, append khi có nguồn mới (không overwrite)
- `status` — draft / reviewed / verified / stale / archived / conflict

Source labels trên mỗi đoạn body: `[WIKI]` · `[RAW-BOOK]` · `[RAW-CLIP]` · `[WEB-YYYY-MM-DD]` · `[LLM-D]` · `[LLM-E]` · `[LLM-S]`

---

## Hard Rules (tóm tắt)

1. Đọc `system.md` trước khi bắt đầu bất kỳ tác vụ nào
2. `librarian.py` là entry point duy nhất — không thao tác file trực tiếp
3. Chạy `wiki_search` trước khi tạo node mới (Rule 0 — prevent duplicates)
4. `embed --incremental` sau mỗi lần tạo/sửa node — không dùng full rebuild
5. Linguistic Sobriety — không dùng gaming framing, combat metaphor, journalistic labels (xem system.md Rule 11)
6. Mọi số cụ thể cần source label; quote trực tiếp cần `[RAW]` hoặc `[WEB-URL]`

Chi tiết đầy đủ: `system.md` BLOCK 0.

---

*system.md v1.0 — May 2026 | librarian.py v2.1*
