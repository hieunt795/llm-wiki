# Wiki Link KG²RAG — Plan nâng cấp theo từng module

> Kế hoạch triển khai chi tiết, **đơn vị thực thi = 1 module**. Mỗi module có: mục tiêu · file đụng tới · phụ thuộc · interface phải đạt · cách verify · rủi ro · ước lượng.
>
> Đi kèm: `WikiLink_KG2RAG_Module_Architecture.md` (ranh giới module) · `WikiLink_KG2RAG_System_Architecture.md` (kiến trúc tổng).
>
> Trạng thái nền (đã soi repo): `librarian.py` 1950 dòng (pattern cắm-pipeline) · 888 wiki node · 111 source `.md` · embed khóa `intfloat/multilingual-e5-base` 768-dim + prefix `passage:`/`query:` · chỉ wiki được embed (source chưa có index).
>
> Ký hiệu: ♻ giữ · ⟳ refactor · ✚ mới · 🔒 gate verify bắt buộc trước khi sang module sau.

---

## 0. Nguyên tắc thực thi xuyên suốt

1. **Không phá đường chạy cũ.** Mọi artifact mới (`.cache/source/`, `.cache/wiki/`, `.cache/kg/`) dựng **song song**; index e5 cũ (`.cache/wiki_embed.index`) giữ làm fallback tới hết Phase 1.
2. **Contract trước, engine sau.** Trong mỗi phase, làm `contracts/` xong mới viết module dùng nó.
3. **Mỗi module có test đi kèm** (mục test ghi trong từng module). Không merge module thiếu verify.
4. **Branch theo phase:** `feat/kg2rag-phase1` … `phase5`. Mỗi module = 1 commit logic.
5. **Embedding/extraction nặng chạy Colab GPU**; local chỉ build nhỏ + verify. Dùng `pull_embed_index.ps1` (đã có).
6. **Rollback đơn vị = module.** Vì artifact tách owner (mục 8 architecture), revert 1 module không kéo sập cái khác.

---

## Phase 1 — Evidence Foundation
> Mục tiêu phase: chunk layer + 2 index tách rời + migrate BGE-M3, **không đụng nội dung 888 node**. Giá trị độc lập: sửa luôn bug mtime cross-machine.

### 1.1 ✚ `contracts/` (L0)
- **Mục tiêu:** định nghĩa dataclass dùng chung trước mọi thứ.
- **File:** `contracts/{ids,source,kg,wiki,retrieval,manifest}.py` + `__init__.py`.
- **Phụ thuộc:** không (chỉ stdlib/pydantic).
- **Interface phải đạt:** `Document, SourceChunk` (source.py); `WikiNode` mở rộng *optional* `claim_refs/entity_refs/evidence_refs` (wiki.py — **không phá** frontmatter v4); `ids.chunk_id()/entity_id()/claim_id()` deterministic.
- **Verify 🔒:** unit test `chunk_id` ổn định (cùng input → cùng id; đổi 1 ký tự text → đổi id); load WikiNode từ 5 node thật trong `03_wiki/` không lỗi field.
- **Rủi ro:** field thừa/thiếu → bump version sớm. Thấp.
- **Ước lượng:** S.

### 1.2 ✚ `io/` (L1)
- **Mục tiêu:** filesystem + hashing + manifest store, thuần kỹ thuật.
- **File:** `io/{fs,hashing,manifest_store,md_frontmatter}.py`.
- **Phụ thuộc:** `contracts`.
- **Interface:** `hashing.content_hash(text)`, `corpus_hash(files)`; `md_frontmatter.parse/serialize` (round-trip không mất field); `manifest_store.load/save/diff`.
- **Verify 🔒:** round-trip 1 node v4 → parse → serialize → diff = rỗng (không drift YAML).
- **Rủi ro:** serialize làm xáo thứ tự field frontmatter → cần giữ ordered. Trung bình.
- **Ước lượng:** S–M.

### 1.3 ✚ `embedding/encoder.py` (L2) — điểm khóa migrate
- **Mục tiêu:** nơi **duy nhất** load BGE-M3.
- **File:** `embedding/encoder.py`.
- **Phụ thuộc:** `contracts`.
- **Interface:** `encode(texts) -> np.ndarray` (1024-dim, `normalize_embeddings=True`, **bỏ prefix** `passage:`/`query:`).
- **Việc:** wrap `SentenceTransformer("BAAI/bge-m3")`; param baseline (max_length 1024, batch GPU 8 / CPU 2).
- **Verify 🔒:** encode 1 câu → vector 1024-dim, norm≈1; grep toàn repo chỉ còn **1** chỗ gọi `SentenceTransformer(`.
- **Rủi ro:** RAM/VRAM BGE-M3 lớn hơn e5 → batch nhỏ trên CPU. Trung bình.
- **Ước lượng:** S.

### 1.4 ⟳ `embedding/embed_wiki_index.py` (refactor từ `embed_index.py`)
- **Mục tiêu:** wiki node → `wiki_dense.index` qua BGE-M3.
- **File:** chuyển `05_scripts/embed_index.py` → `embedding/embed_wiki_index.py`.
- **Phụ thuộc:** `encoder`, `embedding_manifest`, `contracts`, `io`.
- **Việc:** bỏ hardcode e5 + 3 chỗ prefix `passage:`; output sang `.cache/wiki/wiki_dense.index` + `.meta.json` (**không** đè `.cache/wiki_embed.index` cũ).
- **Verify 🔒:** build full 888 node trên Colab; sanity search 5 query so với index e5 → top-k không tệ hơn rõ rệt.
- **Rủi ro:** đổi dim 768→1024 → mọi downstream phải đọc đúng meta. Trung bình.
- **Ước lượng:** M.

### 1.5 ✚ `embedding/embedding_manifest.py`
- **Mục tiêu:** hợp đồng rebuild.
- **Interface:** `needs_rebuild(old,new) -> bool` so `model_name/dimension/normalize/max_length/chunking_version/payload_version/corpus_hash`.
- **Verify:** đổi 1 trường bất kỳ → trả `True`; giống hệt → `False`.
- **Phụ thuộc:** `io`, `contracts`. **Ước lượng:** S.

### 1.6 ✚ `ingestion/source_manifest.py`
- **Mục tiêu:** theo dõi source bằng **content_hash, không mtime** (sửa bug cross-machine đã biết).
- **Interface:** `record(doc)`, `changed() -> list[doc_id]`.
- **Phụ thuộc:** `io.hashing`, `contracts`.
- **Verify 🔒:** copy repo sang path khác (giả lập máy 2) → `changed()` rỗng (vì hash không đổi dù mtime đổi).
- **Rủi ro:** thấp. **Ước lượng:** S.

### 1.7 ✚ `ingestion/normalize_source.py`
- **Mục tiêu:** raw → Markdown chuẩn + `document_id` + `content_hash`.
- **File:** gộp logic `normalize_ocr_md.py`; nối `extract_pdf*` (♻ giữ) ở thượng nguồn.
- **Interface:** `normalize(path) -> Document`.
- **Phụ thuộc:** `io`, `contracts`.
- **Verify:** chạy trên 5 source thật (1 OCR, 1 bảng, 1 paper) → heading/bảng giữ nguyên, header/footer lặp bị bỏ.
- **Rủi ro:** OCR bẩn → normalize sai ranh đoạn → ảnh hưởng chunk. Trung bình. **Ước lượng:** M.

### 1.8 ✚ `ingestion/chunk_sources.py` + `chunk_registry.py`
- **Mục tiêu:** adaptive chunking + stable chunk_id (nền của toàn bộ provenance).
- **Interface:** `chunk(doc) -> list[SourceChunk]` (target 400–600 tok, max 800–1024, overlap 50–100; **không cắt giữa bảng / không tách claim khỏi điều kiện / không tách mechanism khỏi transmission**); `registry.upsert(chunks) -> ChunkDiff`.
- **Phụ thuộc:** `normalize_source`, `contracts.ids`, `io`.
- **Verify 🔒:** re-chunk cùng doc 2 lần → diff rỗng (ổn định); chunk có bảng không bị cắt đôi; token trong ngưỡng.
- **Rủi ro:** **cao** — chiến lược chunk dở sẽ kéo chất lượng cả KG lẫn retrieval. Cần test trên doc có bảng/footnote.
- **Ước lượng:** L.

### 1.9 ✚ `embedding/embed_source_index.py`
- **Mục tiêu:** SourceChunk → `source_dense.index` (index thứ 2, hoàn toàn mới).
- **Interface:** `build(chunks, mode) -> EmbeddingManifest`.
- **Phụ thuộc:** `encoder`, `chunk_registry`, `embedding_manifest`.
- **Verify 🔒:** build trên 111 source; query semantic trả về chunk có heading_path đúng ngữ cảnh.
- **Rủi ro:** chi phí embed lần đầu (Colab). Trung bình. **Ước lượng:** M.

### 1.10 ⟳ `retrieval/semantic_search.py` + `hybrid_search.py`
- **Mục tiêu:** trỏ `encoder` BGE-M3; RRF thêm nhánh `source_dense`.
- **File:** `retrieval/semantic_search.py` (⟳), `hybrid_search.py` (⟳: BM25 ⊕ source_dense ⊕ wiki_dense).
- **Phụ thuộc:** `encoder`, 2 index, `fts5_engine` (♻).
- **Verify 🔒:** golden set ~20 query (exact/semantic/multi-hop) → **Recall@K ≥ baseline e5**. Đây là gate quyết định có giữ BGE-M3 không.
- **Rủi ro:** nếu thua e5 → điều tra prefix/normalize trước khi kết luận. Trung bình. **Ước lượng:** M.

### 1.11 ⟳ `librarian.py` — pipeline Phase 1
- **Việc:** thêm hàm `cmd_source_ingest`, sửa `cmd_embed` (route `--source`/`--wiki`), `cmd_status` đọc manifest mới. **Không sửa dispatch.**
- **Verify:** `python librarian.py source ingest <f>` chạy full chain; `status` hiển thị chunks/source index version.
- **Ước lượng:** M.

> **🔒 GATE PHASE 1:** Recall@K (BGE-M3, 2 index) ≥ e5 trên golden set · chunk_id ổn định · `changed()` không nhầm vì mtime · index e5 cũ vẫn còn. Đạt mới sang Phase 2.

---

## Phase 2 — Evidence Knowledge Graph
> Mục tiêu: dựng graph `Document–Chunk–Entity–Relation–Claim`. Phần đắt nhất (LLM extraction). Net-new toàn bộ.

### 2.1 ✚ `01_schema/kg/` ontology (LUẬT, làm trước code)
- **File:** `entity_types.yaml`, `relation_types.yaml`, `claim_schema.yaml`, `graph_schema.yaml`, `extraction_rules.md`, `resolution_rules.md`.
- **Verify 🔒:** review thủ công — entity types (Institution/Country/Currency/Sector/Indicator/PolicyInstrument/BalanceSheetItem/MarketInstrument/Mechanism/Event) + relation whitelist (drains/funds/transmits_to/…) đủ phủ domain macro plumbing.
- **Rủi ro:** ontology thiếu → extraction phải làm lại. Cao → đầu tư kỹ. **Ước lượng:** M.

### 2.2 ✚ `kg/extract_entities.py`
- **Interface:** `extract(chunk) -> list[Entity]` theo ontology.
- **Phụ thuộc:** ontology, `contracts.kg`, `chunk_registry`.
- **Verify:** trên 10 chunk vàng → precision entity ≥ ngưỡng đặt trước; entity ngoài ontology bị loại.
- **Rủi ro:** LLM bịa entity. Cao → cần few-shot + validate. **Ước lượng:** L.

### 2.3 ✚ `kg/extract_relations.py`
- **Interface:** `extract(chunk) -> list[Relation]` — **mỗi relation BẮT BUỘC `evidence_chunk_id`**.
- **Verify 🔒:** không relation nào thiếu evidence; relation type ∈ registry.
- **Rủi ro:** **cao nhất phase** — relation sai bơm nhiễu vào graph expansion. Cần human-in-loop review. **Ước lượng:** L.

### 2.4 ✚ `kg/extract_claims.py`
- **Interface:** `extract(chunk) -> list[Claim]` (text/scope/conditions/evidence/confidence + valid_from/to).
- **Verify:** causal claim phải có scope+condition; claim có evidence_chunk_ids.
- **Ước lượng:** L.

### 2.5 ✚ `kg/resolve_entities.py` + `resolve_relations.py`
- **Interface:** `resolve(entities) -> list[Entity]` (alias→canonical, ví dụ Fed/Federal Reserve/US central bank → 1).
- **File state:** `.cache/kg/resolution_cache.json`; registry `01_schema/registry/entity_registry.yaml`.
- **Verify 🔒:** bộ alias vàng → đúng canonical; unresolved entity **không** vào graph.
- **Rủi ro:** over-merge (gộp nhầm 2 entity khác nhau). Cao. **Ước lượng:** M–L.

### 2.6 ✚ `kg/kg_validate.py` (gate)
- **Interface:** `validate(objects) -> GateReport`.
- **Verify 🔒:** gate chặn: relation thiếu evidence · entity chưa resolve · relation ngoài ontology · confidence dưới ngưỡng.
- **Ước lượng:** M.

### 2.7 ✚ `kg/build_evidence_graph.py`
- **Interface:** `build(objects) -> GraphManifest` → `.cache/kg/evidence.db` + `evidence_graph.json`.
- **Phụ thuộc:** tất cả extract + resolve + validate.
- **Verify 🔒:** traverse `WikiNode→synthesizes→Claim→supported_by→Chunk→belongs_to→Document` thông suốt trên 1 node thật.
- **Ước lượng:** M.

### 2.8 ⟳ `kg/build_wiki_graph.py` (từ `_build_wiki_graph.py`)
- **Việc:** giữ logic, đổi output `graphify-out/wiki_graph.json`; nối thêm cạnh `WikiNode→synthesizes→Claim`.
- **Verify:** graph cũ vẫn dựng + có cạnh claim mới. **Ước lượng:** S.

### 2.9 ✚ `governance/provenance_auditor.py` + `contradiction_auditor.py`
- **Interface:** `provenance.check()` (claim→chunk→doc còn sống?); `contradiction.classify()` (contradiction thật vs khác regime/thời kỳ/scope).
- **Verify:** cặp claim mâu thuẫn vàng → phân loại đúng; chunk bị xóa → provenance báo gãy.
- **Ước lượng:** M.

### 2.10 ⟳ `librarian.py` — `cmd_kg_build`, `cmd_kg_publish`, mở rộng `cmd_audit`, `cmd_sync`
- **Verify:** `kg build <doc>` → staged_kg; `kg publish` → evidence.db; `audit` chạy 3 auditor.
- **Ước lượng:** M.

> **🔒 GATE PHASE 2:** mọi relation có evidence · entity resolution chính xác trên bộ vàng · provenance chain traverse được · Evidence Coverage đạt ngưỡng. (Khuyến nghị: pilot trên **1 source** trọn vẹn trước khi chạy cả 111.)

---

## Phase 3 — KG²RAG Query
> Mục tiêu: seed → graph expansion → rerank → context organization. Biến retrieval 3-nấc thành 6-nấc.

### 3.1 ✚ `retrieval/kg_expand.py`
- **Interface:** `expand(seeds, policy) -> list[Candidate]` — seed→entity→relation→claim→chunk, ≤2 hop.
- **Phụ thuộc:** `evidence.db`, policy YAML (max_hops 2, min_relation_confidence 0.70, require_evidence, exclude_stale/superseded).
- **Verify 🔒:** không expand qua relation thiếu evidence / entity chưa resolve / edge stale; số candidate ≤ max_total.
- **Rủi ro:** expansion bơm nhiễu nếu Phase 2 ẩu → đó là lý do Phase 2 gate kỹ. **Ước lượng:** L.

### 3.2 ✚ `retrieval/candidate_union.py`
- **Interface:** `merge(*pools) -> list[Candidate]` — union BM25 ⊕ source ⊕ wiki ⊕ graph, dedup, loại stale/superseded.
- **Verify:** trùng ref_id bị gộp; superseded claim bị loại (hoặc cảnh báo).
- **Ước lượng:** M.

### 3.3 ✚ `retrieval/rerank.py`
- **Interface:** `rank(query, candidates) -> list[Candidate]` qua `BAAI/bge-reranker-v2-m3` (cross-encoder).
- **File state:** `.cache/query/rerank_cache/`.
- **Verify 🔒:** trên golden query → nDCG/MRR cải thiện so với chỉ RRF (không rerank).
- **Rủi ro:** latency cross-encoder. Trung bình → cache + giới hạn pool. **Ước lượng:** M.

### 3.4 ✚ `retrieval/context_organizer.py`
- **Interface:** `organize(ranked) -> RankedContext` — sắp Observation→Direct mechanism→Second-order→Supporting→Counter→Boundary; gắn citation `answer→claim_id→chunk_id→document_id`.
- **Verify 🔒:** Context Redundancy dưới ngưỡng; mọi section có citation map về chunk.
- **Ước lượng:** M.

### 3.5 ⟳ `librarian.py` — `cmd_search` thêm `--kg`
- **Verify:** `search --kg <q>` chạy hybrid→expand→union→rerank→organize; query trace ghi `.cache/query/traces/`.
- **Ước lượng:** S–M.

> **🔒 GATE PHASE 3:** Graph Expansion Precision · Citation Accuracy 100% map về chunk · Context Redundancy < ngưỡng · nDCG(rerank) > nDCG(RRF).

---

## Phase 4 — Analytical Debate
> Mục tiêu: chèn tầng phản biện trước MODE DEEP synthesis.

### 4.1 ✚ `synthesis/hypothesis_builder.py`
- **Interface:** `propose(context) -> list[Hypothesis]` (giả thuyết cạnh tranh, không nhảy kết luận).
- **Template:** `01_schema/templates/T_HYPOTHESIS.md`.
- **Verify:** ≥2 giả thuyết/câu hỏi causal; mỗi cái có evidence + counterevidence slot.
- **Ước lượng:** M.

### 4.2 ✚ `synthesis/analytical_review.py`
- **Interface:** `red_team(h)` (reverse causality/omitted var/regime change/data revision/overclaim) + `cross_review(out)` (consistency/completeness/provenance/scope/time/contradiction).
- **Template:** `T_KG_REVIEW.md`.
- **Verify 🔒:** MODE DEEP output có Alternative explanation + Invalidation triggers + Confidence + Treasury Insight.
- **Ước lượng:** M.

### 4.3 ⟳ `librarian.py` — `search --kg --deep` + template `T_MODE_DEEP`
- **Việc:** nối `…--kg → hypothesis_builder → analytical_review → MODE DEEP (5 Lenses)`; cập nhật `T_MODE_DEEP.md` chèn block Hypothesis/Counterevidence/Red-Team/Cross-Review **trước** 5 Lenses.
- **Verify:** 1 phân tích thật (vd Fed/Treasury balance sheet) chạy full chain, giữ kỷ luật ngôn ngữ BLOCK 0.
- **Ước lượng:** M.

> **🔒 GATE PHASE 4:** mỗi MODE DEEP có competing hypotheses + counterevidence + invalidation trigger + claim-level provenance.

---

## Phase 5 — Continuous Update
> Mục tiêu: source đổi → chỉ rebuild phần bị ảnh hưởng (incremental đúng nghĩa).

### 5.1 ✚ `kg/kg_staleness.py`
- **Interface:** `affected(doc_id) -> AffectedSet{chunks, claims, relations, nodes, indexes}`.
- **Phụ thuộc:** `source_manifest`, `evidence.db`.
- **Verify 🔒:** sửa 1 source → chỉ đúng các object hạ nguồn bị đánh stale, không hơn.
- **Ước lượng:** M.

### 5.2 ⟳ partial rebuild trong `embedding_manifest` + `librarian.py status`
- **Việc:** rebuild từng phần theo AffectedSet; `status` hiển thị documents changed/chunks stale/entities unresolved/claims without evidence/index & graph version/failed jobs.
- **Verify 🔒:** đổi 1 doc → rebuild bộ phận < full rebuild rõ rệt; manifest version nhảy đúng.
- **Ước lượng:** M.

> **🔒 GATE PHASE 5:** source change → partial rebuild đúng & rẻ hơn full · `status` phản ánh đầy đủ state model.

---

## Bảng tổng hợp & thứ tự

| # | Module | Loại | Phase | Phụ thuộc chính | Rủi ro | Quy mô |
|---|---|---|---|---|---|---|
| 1.1 | contracts/* | ✚ | 1 | — | thấp | S |
| 1.2 | io/* | ✚ | 1 | contracts | TB | S–M |
| 1.3 | encoder | ✚ | 1 | contracts | TB | S |
| 1.4 | embed_wiki_index | ⟳ | 1 | encoder | TB | M |
| 1.5 | embedding_manifest | ✚ | 1 | io | thấp | S |
| 1.6 | source_manifest | ✚ | 1 | io | thấp | S |
| 1.7 | normalize_source | ✚ | 1 | io | TB | M |
| 1.8 | chunk_sources/registry | ✚ | 1 | normalize | **cao** | L |
| 1.9 | embed_source_index | ✚ | 1 | encoder, chunk | TB | M |
| 1.10 | semantic/hybrid_search | ⟳ | 1 | encoder, 2 index | TB | M |
| 1.11 | librarian P1 | ⟳ | 1 | tất cả P1 | thấp | M |
| 2.1 | ontology kg/ | ✚ | 2 | — | **cao** | M |
| 2.2–2.4 | extract entity/rel/claim | ✚ | 2 | ontology, chunk | **cao** | L×3 |
| 2.5 | resolve entities | ✚ | 2 | extract | cao | M–L |
| 2.6 | kg_validate | ✚ | 2 | extract+resolve | TB | M |
| 2.7 | build_evidence_graph | ✚ | 2 | validate | TB | M |
| 2.8 | build_wiki_graph | ⟳ | 2 | evidence graph | thấp | S |
| 2.9 | provenance/contradiction auditor | ✚ | 2 | evidence db | TB | M |
| 2.10 | librarian P2 | ⟳ | 2 | tất cả P2 | thấp | M |
| 3.1 | kg_expand | ✚ | 3 | evidence db | **cao** | L |
| 3.2 | candidate_union | ✚ | 3 | expand | TB | M |
| 3.3 | rerank | ✚ | 3 | union | TB | M |
| 3.4 | context_organizer | ✚ | 3 | rerank | TB | M |
| 3.5 | librarian P3 | ⟳ | 3 | tất cả P3 | thấp | S–M |
| 4.1 | hypothesis_builder | ✚ | 4 | context | TB | M |
| 4.2 | analytical_review | ✚ | 4 | hypothesis | TB | M |
| 4.3 | librarian P4 | ⟳ | 4 | P4 | thấp | M |
| 5.1 | kg_staleness | ✚ | 5 | manifest, evidence | TB | M |
| 5.2 | partial rebuild | ⟳ | 5 | staleness | TB | M |

**Đường găng (critical path):** `contracts → encoder → chunk_sources → embed_source → hybrid_search` (Phase 1) → `ontology → extract_relations → resolve → evidence_graph` (Phase 2) → `kg_expand → rerank` (Phase 3). Các module S khác chạy song song quanh đường này.

---

## Checklist khởi động (làm ngay khi bắt đầu Phase 1)

- [ ] Tạo branch `feat/kg2rag-phase1`.
- [ ] Tạo bộ **golden query set** (~20 câu: exact/semantic/multi-hop/causal/contradiction/temporal) + đo baseline Recall@K trên index e5 hiện tại → mốc so sánh BGE-M3.
- [ ] Dựng `05_scripts/contracts/` + `io/` (1.1–1.2) — nền không phụ thuộc gì.
- [ ] Viết import-lint script (kiểm layer + 1-điểm-load-model) chạy trong CI/pre-commit.
- [ ] Xác nhận hạn mức Colab GPU + cập nhật `colab_embed_index.ipynb` sang BGE-M3.

---

## Quyết định cần chốt trước khi code (open questions)

1. **Retrofit 888 node cũ tới mức nào?** Backfill `claim_refs/evidence_refs` cho toàn bộ (đắt) hay chỉ cho node mới + node hot? → đề xuất: chỉ node mới; backfill dần theo `health`.
2. **LLM cho extraction (Phase 2):** model nào, chạy local hay API, ngân sách token cho 111 source? → ảnh hưởng trực tiếp lịch Phase 2.
3. **Pilot scope Phase 2:** chốt **1 source đại diện** (đề xuất: 1 chương Bindseil hoặc IMF macro accounting) để hiệu chỉnh extraction trước khi scale.
4. **Giữ song song bao lâu:** mốc gỡ index e5 cũ (đề xuất: sau khi Phase 1 gate xanh + 1 tuần dùng thực tế).

> **Tóm tắt một câu:** Plan đi tuần tự 5 phase, đơn vị giao việc là module có gate verify riêng; Phase 1 (chunk + dual index + BGE-M3) là phần contained sửa luôn bug mtime và không đụng nội dung node; Phase 2 (Evidence KG) là khoản đắt và rủi-ro-cao nhất nên pilot 1 source trước; mọi artifact dựng song song để rollback theo module mà không phá đường chạy cũ.
