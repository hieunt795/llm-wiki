# WIKI SCHEMA v4.0 — Atomic Knowledge Engine (SOP Standard)
> Updated: 2026-05-02 — Adds §7 Citation Standard, §8 Thesis Standard, §9 source_refs spec, §10 Audit Checklist.
> Nodes are **atomic memory units**, prioritizing Transmission Mechanisms over surface description. Every node must follow the **Quant Macro Analyst** identity.

## 0. IMMUTABLE RULES
1. **MD-First:** Ưu tiên Markdown, dùng KaTeX cho công thức toán học.
2. **Citation-First:** Mọi luận điểm phải có `[RAW]`, `[WIKI]`, `[WEB]` hoặc `[LLM]` prefix.
3. **Expand, Don't Overwrite:** Luôn thêm section mới, giữ hạ tầng cũ (Version Persistence).
4. **Collision Prevention:** Luôn check `01_schema/alias_registry.md` trước khi tạo node.
5. **No Flattening:** Giữ nguyên các mâu thuẫn (Contradictions) giữa các nguồn.

---

## 1. NODE TAXONOMY (The 5 Core Types)

| Type | Folder | Purpose |
|---|---|---|
| `concept` | `03_wiki/concepts/` | Primitive building block, taxonomy unit, or object-level idea. |
| `definition` | `03_wiki/definitions/` | "X là gì?" — Boundary, expert lenses, properties. |
| `mechanism` | `03_wiki/mechanisms/` | "X vận hành thế nào?" — Transmission flow, worked examples. |
| `relationship` | `03_wiki/relationships/` | Node diễn tả tương tác, hierarchy, trade-off, hoặc comparative structure giữa concepts. |
| `convention` | `03_wiki/conventions/` | "Quy ước thị trường?" — Daycount, ISDA, settlement. |
| `perspective` | `03_wiki/perspectives/` | Góc nhìn của tác giả/tổ chức cụ thể. |
| `evidence` | `03_wiki/evidence/` | Numeric or case-study evidence node with limited theory load. |
| `domain` | `03_wiki/domains/` | Country/market/domain context node. |
| `glossary` | `03_wiki/glossary/` | Quick reference / terminology aggregation node. |
| `contradiction` | `03_wiki/contradictions/` | Xử lý các điểm xung đột giữa nguồn L1/L2. |
| `synthesis` | `03_wiki/syntheses/` | Kết quả tổng hợp wisdom run — cross-tag insight, hub map, tension cluster. |

---

## 2. MANDATORY FRONTMATTER (All Fields Required)

```yaml
---
title: "Human-readable title"           # REQUIRED — matches filename stem (spaces → underscores)
aliases:                                # REQUIRED — list, can be empty []
  - Alias 1
  - Alias 2
type: mechanism                         # REQUIRED — see §1 taxonomy
tags:                                   # REQUIRED — min 1 tag, lowercase-hyphenated
  - fixed-income
  - macro
status: draft                           # REQUIRED — see values below
confidence: 3                           # REQUIRED — integer 1–5, see scale below
half_life_years: 10                     # REQUIRED — see values below
school: ""                              # REQUIRED — empty string if N/A; perspective nodes: see §6
superseded_by: null                     # REQUIRED — null or "NodeName"
superseded_date: null                   # REQUIRED — null or "YYYY-MM-DD"
expert_lens: "Author1 | Author2"        # REQUIRED — pipe-separated, empty string if unknown
provenance: "Source_File.md"            # REQUIRED — short description of origin
thesis: "ONE sentence: core claim."     # REQUIRED — see §8 Thesis Standard
source_refs:                            # REQUIRED — list, can be [] if no RAW source yet
  - file: "Filename.md"                 # REQUIRED per item — source file basename
    page: 42                            # optional — page number or section
created: "YYYY-MM-DD"                   # REQUIRED
updated: "YYYY-MM-DD"                   # REQUIRED — update on every write
---
```

### Status values
| Value | Meaning |
|---|---|
| `draft` | Mới tạo, chưa review — có thể chứa [LLM] placeholders |
| `reviewed` | Đã đọc qua, nội dung hợp lý nhưng chưa có RAW backing đầy đủ |
| `verified` | Có ≥1 RAW source backing trong source_refs |
| `stale` | Outdated — half_life đã qua, cần review/update |
| `archived` | Superseded bởi node khác (điền superseded_by) |
| `conflict` | Mâu thuẫn với node khác — chờ CONTRADICTION node |

### Confidence scale
| Score | Meaning | Typical source |
|---|---|---|
| 1 | Very low | [LLM] only, no RAW backing |
| 2 | Low | [LLM] + partial RAW, or WIKI cross-ref only |
| 3 | Medium | [WIKI] — node backed by internal cross-references |
| 4 | High | [RAW] — single RAW source (book/paper/official) |
| 5 | Verified | [RAW] multi-source — ≥2 independent RAW files agree |

### half_life_years values
| Content type | Value | Rationale |
|---|---|---|
| Mechanism / Theory | `10` | Slow-changing financial logic |
| Regulatory / Policy | `1` | Basel, ISDA, CB rules change |
| Market data / Rates | `0.1` | Prices stale within weeks |
| Synthesis / Wisdom | `0.5` | Derived — re-run when inputs change |
| Domain context | `3` | Country macro shifts moderately |

---

## 3. NODE STRUCTURE (The Skeleton)

### 3.1 Standard Template
```markdown
---
[frontmatter as above]
---

# [[Node_Title]]

## Thesis
[WIKI/RAW] One-sentence core essence — identical to frontmatter `thesis` field.

## 1. Core Logic / Mechanism
[RAW-BOOK:Source p.X] Trích dẫn nội dung gốc đầy đủ.
[LLM-S] Phân tích cơ chế truyền dẫn: X →[điều kiện A]→ Y →[điều kiện B]→ Z.

## 2. Worked Example
[RAW-BOOK:Source p.X / WEB-YYYY-MM-DD:url] Ví dụ lượng hóa, số liệu thực tế.
> **MANDATORY:** Khi ingest tài liệu mới có ví dụ chi tiết hơn → MUST EXPAND phần này.

## 3. Failure Conditions / Boundaries
Khi nào cơ chế này thất bại? (Liquidity trap, Regime switch, Regulatory change).

## Related
- [[Wikilink_1]]
- [[Wikilink_2]]
```

### 3.2 Type-specific structure additions

**`mechanism`** — thêm sau Thesis:
```markdown
## Transmission Chain
X →[điều kiện kích hoạt]→ Y →[cơ chế trung gian]→ Z
```

**`perspective`** — thêm sau Thesis:
```markdown
## Author / Source
[RAW-CLIP:source] Tên tác giả, tổ chức, ngày, URL nếu có.

## Claim
[RAW-CLIP] Luận điểm cụ thể, không diễn giải.

## Counter-argument
[WIKI/LLM-S] Quan điểm đối lập nếu có.
```

**`contradiction`** — template riêng:
```markdown
## Claim A
[RAW-X] Source A nói gì.

## Claim B
[RAW-Y] Source B nói gì, mâu thuẫn tại điểm nào.

## Resolution Status
UNRESOLVED | RESOLVED: [giải thích] | REGIME-DEPENDENT: [điều kiện]
```

**`synthesis`** — output từ auto_synthesis.py, không viết thủ công.

---

## 4. STANDARD INGEST PROCESS (Surgical Ingest)

1. **Phase A (Mapping):** Convert Source → `.md` vào `02_sources/`. Tạo concept map tại `04_outputs/`.
2. **Phase B (Extraction):** Check Wiki (`python librarian.py search "<query>"`). Nếu có node cũ → Audit toàn bộ nội dung cũ. Chọn writeback type theo Decision Tree (xem W4_memory.md):
   - Nội dung cũ đúng, thêm thông tin mới → **UPDATE**
   - Nội dung cũ sai/outdated → **REPLACE** (ghi lý do)
   - Tìm link còn thiếu → **BRIDGE**
   - Nguồn mới mâu thuẫn → **CONTRADICTION**
   - Node chưa tồn tại → **SPAWN**
   - Output từ wisdom run → **SYNTHESIS**
   - Analyst view / opinion → **PERSPECTIVE**
3. **Phase C (Merge):** Tạo/cập nhật node theo schema. Cập nhật `01_schema/log.md` với writeback type rõ ràng. Xem format chuẩn tại W4_memory.md § log.md.

---

## 5. TECHNICAL STANDARDS
- **Math:** Dùng KaTeX `$...$` hoặc `$$...$$`.
- **Filenames:** `Title_Case_Underscores.md` — khớp với `title` field.
- **Wikilinks:** `[[Node_Stem]]` — dùng file stem, không extension.
- **Heading:** H1 luôn là `# [[Node_Title]]`.

---

## 6. SCHOOL VALUES (perspective nodes)
`Monetarist` | `Post-Keynesian` | `MMT` | `Austrian` | `New-Keynesian` | `Practitioner` | `Institutional` | `Market Transparency / Fiscal Realism` | `""` (empty if N/A)

---

## 7. CITATION STANDARD (Inline Labels)

> **Rule:** Mọi claim trong body text PHẢI có citation label ở đầu câu/đoạn. Không có label = không publish.

### Label hierarchy (trust order)
```
[RAW-BOOK:SourceName p.X]    Trích từ sách đã ingest vào 02_sources/books/
[RAW-OFFICIAL:SourceName]    Báo cáo chính thức: BIS, IMF, ISDA, MAS, SBV
[RAW-ACADEMIC:AuthorYYYY]    Peer-reviewed paper
[RAW-CLIP:source]            Clipping/article đã lưu vào 02_sources/Clipping/
[RAW-DR:SourceName]          Deep research report đã lưu vào 02_sources/deep-research/
[WIKI]                       Cross-reference từ node khác trong 03_wiki/
[WEB-YYYY-MM-DD:url]         Web search result — ephemeral, cite ngày
[LLM]                        LLM-generated, không có source backing — PHẢI có explicit label
[LLM-S]                      LLM synthesis/reasoning từ các sources đã cite trước đó
```

### Trust order by claim type
| Claim type | Order |
|---|---|
| Cơ chế / Lý thuyết | RAW-BOOK > RAW-ACADEMIC > WIKI > RAW-CLIP > LLM-S > WEB |
| Số liệu thị trường | WEB-dated > RAW-OFFICIAL-recent > RAW-BOOK > LLM |
| Chính sách hiện hành | WEB-official > RAW-OFFICIAL > RAW-BOOK > WIKI > LLM |
| Perspective / Opinion | RAW-CLIP > RAW-DR > LLM |

### Citation format examples
```markdown
[RAW-BOOK:Tuckman_Serrat p.45] The DV01 of a bond equals the negative of the first derivative...
[RAW-OFFICIAL:BIS_Basel3_2017] The LCR minimum requirement is 100% as of 2019.
[WEB-2026-05-01:ft.com] Fed held rates unchanged at 4.25–4.50% in May 2026 meeting.
[LLM-S] Therefore, when fiscal dominance activates, the CB's reaction function shifts from...
[LLM] Placeholder — mechanism not yet sourced from RAW. Confidence: 1.
```

### Forbidden patterns (will fail claim_auditor.py)
```
❌ "X ảnh hưởng Y qua nhiều kênh"         → vague, no mechanism
❌ "phụ thuộc nhiều yếu tố"               → vague, no conditions
❌ "thường hoạt động theo hướng..."       → vague, no specificity
❌ Claim without any [...] label           → missing source
❌ [LLM] without explicit placeholder note → hide LLM origin
```

---

## 8. THESIS STANDARD

> The `thesis` field is the **single most important field** — it drives search ranking (×4 weight) and graphify node labeling.

### Rules
1. **One sentence only** — no bullet points, no conjunctions joining two separate claims.
2. **Mechanism, not description** — state WHAT happens, not just WHAT it is.
3. **Condition + Effect** — include at least one trigger condition.
4. **Language:** English preferred for thesis field (bilingual OK for perspective nodes, format: `EN / VI`).
5. **Minimum length:** 20 words. Maximum: 60 words.
6. **Must differ from title** — thesis = core claim, title = label.

### Good vs Bad thesis examples
```yaml
# BAD — too short, no mechanism
thesis: "Fiscal dominance is when government needs override central bank."

# BAD — description without mechanism
thesis: "LCR is a regulatory ratio requiring banks to hold high-quality liquid assets."

# GOOD — condition + mechanism + effect
thesis: "Fiscal dominance is the condition in which sovereign financing needs override
  central bank independence, forcing monetary policy to protect fiscal solvency instead
  of fully defending price stability."

# GOOD — mechanism with transmission
thesis: "The LCR forces banks to hold ≥100% liquid asset buffer against 30-day net
  outflows; under stress, this creates pro-cyclical asset fire-sales when the ratio
  approaches the floor."
```

### Thesis for each node type
| Type | Thesis should answer |
|---|---|
| `concept` | "X is [definition] + [key property that distinguishes it]" |
| `mechanism` | "Under [condition], X operates via [transmission] → [outcome]" |
| `definition` | "X is [precise boundary] where [key distinguishing property holds]" |
| `relationship` | "[A] and [B] interact via [mechanism] creating [tension/amplification]" |
| `perspective` | "[Author] claims [X] because [reasoning], contrasting with [mainstream view]" |
| `evidence` | "[Quantified claim] observed [where/when], consistent with [mechanism]" |
| `synthesis` | "Canonical synthesis of [domain] — key tension: [X] vs [Y]" |

---

## 9. SOURCE_REFS STANDARD

> `source_refs` is machine-read by `wiki_search.py` (score boost ×1.5) and `claim_auditor.py`. Format must be exact.

### Correct format
```yaml
source_refs:
  - file: "Perry_Central_Bank_Policy_P4.md"   # basename of file in 02_sources/
    page: 283                                  # page number (integer) or section string
  - file: "Fixed_Income_Alexander_During_Ch10.md"
    page: "§10.3"                              # section reference OK
  - file: "Are high UK yields good or bad_.md" # clipping filename
    # page omitted → OK for clippings/web
```

### Rules
- `file`: always the **basename** of a file that exists in `02_sources/` (any subdirectory).
- `page`: integer or string. Omit entirely if not applicable (not `null`, not `0`).
- Empty list `[]` is valid for `draft` nodes — but confidence must be ≤ 2.
- `null` is **NOT valid** — use `[]` for empty.
- Each item MUST have `file` key — bare strings are invalid.

### Common errors
```yaml
# BAD — null instead of empty list
source_refs: null

# BAD — bare string instead of dict
source_refs:
  - "Perry_Central_Bank_Policy.md"

# BAD — file key missing
source_refs:
  - page: 45

# GOOD — empty draft
source_refs: []

# GOOD — full
source_refs:
  - file: "Bindseil_Monetary_Policy_Operations.md"
    page: 112
```

---

## 10. AUDIT CHECKLIST (Pre-Publish)

Run before merging any new or updated node:

```
[ ] Title matches filename stem (spaces → underscores)
[ ] All mandatory frontmatter fields present and non-null
[ ] type is in valid taxonomy list
[ ] confidence integer 1–5
[ ] status is a valid value
[ ] half_life_years matches content type
[ ] thesis: ≥20 words, ≤60 words, contains condition + mechanism
[ ] source_refs: list (not null), each item has 'file' key
[ ] If confidence ≥ 4: source_refs has ≥1 entry
[ ] All body claims have [...] citation label
[ ] No forbidden vague patterns ("nhiều yếu tố", "phụ thuộc vào" without conditions)
[ ] H1 heading = # [[Node_Stem]]
[ ] Related section has ≥1 wikilink
[ ] updated field = today's date
[ ] log.md entry added with writeback type
```

---

## 11. RESEARCH FLOW v1.1 (Deep Research Standard)

> Quy trình tạo Research Report từ Wiki + Raw + Web. Nếu Prompt có Framework riêng, ưu tiên dùng Framework đó.

### PHASE R0 — PROMPT PARSING & THESIS LOCK
- **R0.1 Parsing:** Extract Framework, Output Format, Writing Style, Data Requirements và Constraints từ Prompt.
- **R0.2 Thesis Lock:** Chốt **Core Thesis** (1 câu), **Null Hypothesis** và các lựa chọn Framework/Format. Thesis KHÔNG thay đổi sau bước này.

### PHASE R1 — INTERNAL RESEARCH (Wiki + Raw)
- `python librarian.py search "<query>"` → fast BM25.
- `python librarian.py search "<query>" --deep` → Graphify + BM25 + Heatmap.
- `python librarian.py deepdive "<query>"` → thin-node detection + RAW drill + draft.
- Map nodes vào framework. Lập **GAP LIST**: những dữ liệu/phân tích còn thiếu.

### PHASE R2 — EXTERNAL RESEARCH (Web Search)
- Chỉ tìm kiếm để lấp đầy **GAP LIST**.
- Ưu tiên: Central Bank, IMF, BIS, World Bank, Academic Papers, Financial Press.
- **MANDATORY:** Label `[WEB-YYYY-MM-DD:source]`. Nếu giá trị dài hạn → `[INGEST CANDIDATE]`.

### PHASE R3 — SYNTHESIS & OUTPUT
- Enforce Writing Style và Constraints từ R0.
- Ghi nhãn **CONFIDENCE TIER** cho báo cáo.
- Đảm bảo có mục **TRANSITION** sang nội dung tiếp theo.

### PHASE R4 — POST-REPORT WRITEBACK
- Xử lý **Writeback Queue** vào Wiki/Schema.
- Cập nhật `01_schema/log.md`. Giới hạn 3 writebacks/session.
