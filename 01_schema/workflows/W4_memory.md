# W4 — MEMORY MANAGEMENT
> Load khi: cần ghi nhớ kết quả session, cập nhật context, quản lý hot cache.

## hot.md — Session Buffer
**Cập nhật khi:** Context của session thay đổi đáng kể (focus mới, hot nodes mới, workflow state mới).
```
Cấu trúc hot.md:
  ## 0. Graph God Nodes Cache     ← top nodes by edge count
  ## 1. Current Session Context   ← Primary Goal + Workflow State
  ## 2. Active Focus Nodes        ← Hot Nodes hiện tại
  ## 3. Temporary Logic           ← Sync rules, gap notes
  ## 4. Raw Source Index          ← L2 Cross-Check Registry
```
**Quy tắc:** Clear hoặc compact khi chuyển sang macro-topic mới.

## memory.md — Operational Memory
**Cập nhật khi:** Sau mỗi cụm tác vụ thành công hoặc resolve lỗi kỹ thuật phức tạp.
```
Cấu trúc memory.md:
  ## 1. User Preferences          ← Response standard, visuals, search logic
  ## 2. Technical Fixes           ← Windows/CLI workarounds, encoding issues
  ## 3. Analytical Truths         ← Validated logics đã cross-checked
  ## 4. Active Debt               ← Tasks còn pending
```

## Writeback Type Reference

> 7 loại writeback — dùng nhất quán trong W2, W5, log.md, và writeback_queue.md.

### Group A — Node Operations

| Type | Khi nào | Audit yêu cầu | Folder đích |
|------|---------|--------------|-------------|
| `SPAWN` | Concept chưa có node nào trong wiki | Kiểm tra alias_registry trước | `03_wiki/[type]/` |
| `UPDATE` | Node tồn tại, bổ sung source/section/example mới — KHÔNG thay thế nội dung cũ | Đọc node cũ, confirm nội dung cũ đúng | existing node |
| `REPLACE` | Node tồn tại nhưng nội dung SAI hoặc OUTDATED — thay thế có kiểm soát | Đọc node cũ, ghi rõ lý do replace | existing node |
| `BRIDGE` | Hai node liên quan chưa có wikilink 2 chiều | Confirm cả 2 node tồn tại | existing nodes |
| `CONTRADICTION` | Hai nguồn mâu thuẫn — không merge, tạo node riêng | Xác định trục mâu thuẫn (số liệu/cơ chế/kết luận) | `03_wiki/contradictions/` |

### Group B — Synthesis Operations

| Type | Khi nào | Audit yêu cầu | Folder đích |
|------|---------|--------------|-------------|
| `SYNTHESIS` | Wisdom run tạo hub map / tension cluster có giá trị dài hạn | Tag + N nodes + M tensions phải ghi rõ | `03_wiki/syntheses/` |
| `PERSPECTIVE` | Analyst view / school of thought từ Clipping — không phải mechanism claim | Ghi author + school tag, dùng attributed thesis | `03_wiki/perspectives/` |

### Decision Tree

```
Node đã tồn tại?
  YES → Nội dung cũ đúng?
          YES → Thêm thông tin mới? → UPDATE
                Tìm thấy link thiếu? → BRIDGE
                Nguồn mới mâu thuẫn? → CONTRADICTION
          NO  → Nội dung sai/outdated → REPLACE (ghi lý do)
  NO  → Source là opinion/perspective? → PERSPECTIVE
         Source là mechanism/definition? → SPAWN
         Là wisdom run output? → SYNTHESIS
```

### Confidence Rules

```
SPAWN:        confidence: 1 (RAW-BOOK) | 1 (RAW-CLIP, không tăng)
UPDATE:       confidence +1 nếu source là [RAW-BOOK/OFFICIAL/ACADEMIC] và independent
              confidence không đổi nếu source là [RAW-CLIP/DR-LLM/OPINION]
REPLACE:      confidence reset về source mới, ghi superseded_by nếu archive node cũ
BRIDGE:       không thay đổi confidence của node gốc
CONTRADICTION: confidence: 1, status: conflict
SYNTHESIS:    confidence: 3 (cross-validated từ graph)
PERSPECTIVE:  confidence: 2 (analyst view, không phải evidence)
```

---

## log.md — Audit Trail

**Ghi mỗi khi:** Bất kỳ writeback nào được thực hiện.

```
Format:
[YYYY-MM-DD] SPAWN       — NodeName — source [RAW-TYPE]
[YYYY-MM-DD] UPDATE      — NodeName — what added — source
[YYYY-MM-DD] REPLACE     — NodeName — reason — old claim → new claim
[YYYY-MM-DD] BRIDGE      — NodeA ↔ NodeB — rationale
[YYYY-MM-DD] CONTRADICTION — NodeA vs NodeB — axis (data/mechanism/conclusion)
[YYYY-MM-DD] SYNTHESIS   — tag — N nodes, M tensions
[YYYY-MM-DD] PERSPECTIVE — NodeName — author/school
[YYYY-MM-DD] FIX         — ScriptName — issue and fix
[YYYY-MM-DD] SYNC        — graph sync, N nodes
```

## Commit Protocol
```
IF (tác vụ thành công) → cập nhật memory.md § Analytical Truths
IF (lỗi kỹ thuật resolved) → cập nhật memory.md § Technical Fixes
IF (node mới tạo/sửa) → ghi log.md
IF (session kết thúc) → cập nhật hot.md § Workflow State
```

## Active Debt Cleanup Protocol

```
Debt items trong memory.md § Active Debt:
  → Nếu không touched trong 90 ngày → move sang 01_schema/archive/debt_archive.md
  → Format khi archive: [ARCHIVED YYYY-MM-DD] <original debt line>

Quarterly review (đầu mỗi quý):
  → Scan memory.md § Active Debt
  → Items resolved → xóa hoặc mark [DONE YYYY-MM-DD]
  → Items > 90 ngày chưa touched → archive
  → Items urgent nhưng bị block → note blocker rõ ràng
```

**Lệnh manual archive:**
```
python librarian.py staleness --auto-mark   # auto-set status:stale nếu quá half_life
```
