# Wiki Link KG²RAG — Cấu trúc hệ thống (chi tiết)

> Tài liệu mô tả kiến trúc · vận hành · yêu cầu nâng cấp repo Wiki Link thành hệ thống **Wiki-LLM + KG²RAG**.
>
> Mục tiêu: giữ nguyên nền tảng Wiki Link hiện tại, bổ sung evidence graph, chunk-level provenance, graph-guided retrieval, reranking và context organization.
>
> Embedding engine: **BAAI/bge-m3**.

---

## 1. Hệ thống này là gì

Một **knowledge system nguyên tử có kiểm chứng bằng nguồn** chuyên về macro / fixed-income / monetary plumbing, kết hợp bốn lớp:

- **Wiki-LLM** — ingest sách, paper, báo cáo và nguồn thô → chưng cất thành các wiki node nguyên tử.
- **Evidence Knowledge Graph** — biểu diễn `Document → Chunk → Entity → Relation → Claim → WikiNode`.
- **KG²RAG** — semantic retrieval tạo seed → graph expansion → evidence join → rerank → context organization.
- **Analytical Harness** — điều phối phân tích, phản biện, review và tổng hợp theo 5 Lenses.

Hệ thống vận hành theo hai mode chính:

- **Mode SYNTHESIS** — ingest source → chunk → extract entity/relation/claim → tạo hoặc cập nhật wiki node.
- **Mode DEEP** — truy xuất tri thức và evidence → xây giả thuyết → phản biện → tổng hợp theo:

```text
Top-down → Macro → Plumbing → Treasury → Timing
```

Mọi thao tác đi qua một entry point duy nhất:

```text
librarian.py
```

Source-of-truth tiếp tục là các file `.md` và registry có version control. FAISS index, SQLite FTS5, graph database và query cache là các artifact phái sinh, có thể tái tạo.

---

## 2. Bản đồ thư mục (layout vật lý)

```text
D:\AI\Wiki Link\
│
├── librarian.py             ★ ENTRY POINT — orchestrator + lifecycle harness
├── CLAUDE.md / GEMINI.md    ← system prompt cho từng agent
├── system.md                ← SOP đầy đủ + hard rules + pointer map
├── Readme.md
│
├── 01_schema/               ── "Hiến pháp" của hệ thống
│   ├── hot.md               · L0 session context
│   ├── memory.md            · persistent state index
│   ├── schema.md            · wiki node schema
│   ├── alias_registry.md    · chống trùng node
│   │
│   ├── kg/                  ── ontology và schema cho Evidence KG
│   │   ├── entity_types.yaml
│   │   ├── relation_types.yaml
│   │   ├── claim_schema.yaml
│   │   ├── graph_schema.yaml
│   │   ├── extraction_rules.md
│   │   └── resolution_rules.md
│   │
│   ├── protocols/
│   │   ├── P1_awareness.md
│   │   ├── P2_epistemic.md
│   │   ├── P3_mechanistic.md
│   │   ├── P4_output.md
│   │   ├── P5_evidence.md
│   │   └── P6_contradiction.md
│   │
│   ├── workflows/
│   │   ├── W1_query.md
│   │   ├── W2_ingest.md
│   │   ├── W3_research.md
│   │   ├── W4_memory.md
│   │   ├── W5_secondary_ingest.md
│   │   ├── W6_kg_build.md
│   │   └── W7_kg_query.md
│   │
│   ├── templates/
│   │   ├── T_MODE_DEEP.md
│   │   ├── T_CLAIM.md
│   │   ├── T_HYPOTHESIS.md
│   │   └── T_KG_REVIEW.md
│   │
│   ├── registry/
│   │   ├── entity_registry.yaml
│   │   ├── relation_registry.yaml
│   │   ├── synonyms.yml
│   │   └── router_rules.yml
│   │
│   └── index/
│       └── index_concepts/mechanisms/relationships/...
│
├── 02_sources/              ── RAW source layer
│   ├── books/
│   ├── academic/
│   ├── reports/
│   ├── bindseil/
│   ├── clipping/
│   ├── deep-research/
│   └── inbox/
│
├── 03_wiki/                 ── WIKI KNOWLEDGE layer
│   ├── mechanisms/
│   ├── concepts/
│   ├── definitions/
│   ├── perspectives/
│   ├── domains/
│   ├── relationships/
│   ├── evidence/
│   ├── contradictions/
│   ├── conventions/
│   ├── syntheses/
│   └── glossary/
│
├── 04_outputs/              ── Sản phẩm trung gian / staged artifacts
│   ├── staged_nodes/
│   ├── staged_kg/
│   │   ├── entities/
│   │   ├── relations/
│   │   ├── claims/
│   │   ├── conflicts/
│   │   └── resolution_candidates/
│   ├── research/
│   ├── reports/
│   ├── audits/
│   ├── drafts/
│   ├── query_traces/
│   ├── calibration/
│   └── temp/
│
├── 05_scripts/              ── Engine layer
│   ├── ingestion/
│   │   ├── normalize_source.py
│   │   ├── chunk_sources.py
│   │   ├── chunk_registry.py
│   │   └── source_manifest.py
│   │
│   ├── embedding/
│   │   ├── embed_source_index.py
│   │   ├── embed_wiki_index.py
│   │   └── embedding_manifest.py
│   │
│   ├── kg/
│   │   ├── extract_entities.py
│   │   ├── extract_relations.py
│   │   ├── extract_claims.py
│   │   ├── resolve_entities.py
│   │   ├── resolve_relations.py
│   │   ├── build_evidence_graph.py
│   │   ├── build_wiki_graph.py
│   │   ├── kg_validate.py
│   │   └── kg_staleness.py
│   │
│   ├── retrieval/
│   │   ├── wiki_search.py
│   │   ├── fts5_engine.py
│   │   ├── semantic_search.py
│   │   ├── hybrid_search.py
│   │   ├── deepdive_search.py
│   │   ├── kg_expand.py
│   │   ├── candidate_union.py
│   │   ├── rerank.py
│   │   └── context_organizer.py
│   │
│   ├── synthesis/
│   │   ├── auto_ingest.py
│   │   ├── auto_synthesis.py
│   │   ├── hypothesis_builder.py
│   │   └── analytical_review.py
│   │
│   └── governance/
│       ├── claim_auditor.py
│       ├── provenance_auditor.py
│       ├── contradiction_auditor.py
│       ├── find_orphans.py
│       ├── auto_bridge.py
│       └── rename_node.py
│
├── 06_publish/              ── Sản phẩm cuối
│
├── .cache/                  ── Artifact phái sinh, regenerable
│   ├── source/
│   │   ├── source_dense.index
│   │   ├── source_dense.meta.json
│   │   └── source_manifest.json
│   │
│   ├── wiki/
│   │   ├── wiki_dense.index
│   │   ├── wiki_dense.meta.json
│   │   └── wiki_manifest.json
│   │
│   ├── sparse/
│   │   └── wiki_index.db
│   │
│   ├── kg/
│   │   ├── evidence.db
│   │   ├── graph.json
│   │   ├── graph_manifest.json
│   │   └── resolution_cache.json
│   │
│   └── query/
│       ├── rerank_cache/
│       └── traces/
│
├── graphify-out/
│   ├── wiki_graph.json
│   ├── evidence_graph.json
│   ├── graph.html
│   └── GRAPH_REPORT.md
│
└── memory/
    ├── workflow_triad_analysis.md
    ├── workflow_plumbing_analysis.md
    └── ingest_plan.md
```

**Nguyên tắc phân tầng:**

```text
01_schema   = LUẬT + ONTOLOGY
02_sources  = INPUT THÔ
03_wiki     = TRI THỨC CHƯNG CẤT
04_outputs  = STAGING + REVIEW
05_scripts  = ENGINE
.cache      = RETRIEVAL ARTIFACT
graphify    = GRAPH ARTIFACT
memory      = STATE BỀN VỮNG
```

---

## 3. Kiến trúc điều khiển — `librarian.py` + StepRunner

`librarian.py` tiếp tục là orchestrator duy nhất. Nó không trực tiếp thực hiện logic nặng mà gọi các engine script trong `05_scripts/`.

```text
                         ┌────────────────────────────────────────┐
   python librarian.py → │ main() argparse → command dispatch      │
        <cmd> <targets>  │ StepRunner(skip_set, only_set)          │
                         └──────────────────┬─────────────────────┘
                                            │
       ┌──────────────┬──────────────┬──────┴───────┬─────────────┬──────────────┐
       ▼              ▼              ▼              ▼             ▼              ▼
  [QUẢN TRỊ]     [SOURCE]         [KG]          [SEARCH]      [SYNTHESIS]     [EMBED]
  status         normalize        extract       keyword       stage           source
  health         chunk            resolve       semantic      review          wiki
  sync           manifest         validate      hybrid        ingest          stats
  daily          audit            publish       kg            wisdom          rebuild
  batch                                          kg-deep       deep
```

### Các pipeline chính

| Lệnh | Chuỗi step | Dùng khi |
|---|---|---|
| `status` | source status → chunk status → KG status → index status | đầu session |
| `source ingest` | normalize → manifest → chunk → source embed | thêm source mới |
| `kg build` | entity → relation → claim → resolve → stage | xây Evidence KG |
| `kg publish` | review → validate → graph build → version | publish KG |
| `wiki ingest` | Rule 0 → stage node → audit → accept → sync | thêm wiki node |
| `sync` | wiki graph → evidence graph → index → staleness | sau thay đổi |
| `search` | BM25 → semantic → RRF | lookup thông thường |
| `search --kg` | hybrid seeds → KG expansion → rerank → organize | query KG²RAG |
| `search --kg --deep` | KG retrieval → hypothesis → counterevidence → MODE DEEP | phân tích sâu |
| `health` | orphan → missing thesis → unresolved entity → missing evidence → stale | định kỳ |
| `audit` | claim → provenance → contradiction → quality gate | trước publish |
| `embed` | source/wiki incremental hoặc full rebuild | sau thay đổi corpus |

---

## 4. Vòng đời dữ liệu (data flow end-to-end)

```text
Raw Source
   ↓
Normalize
   ↓
Adaptive Chunking
   ├───────────────────────────────┐
   ↓                               ↓
Source Dense / BM25 Index     Entity Extraction
                              Relation Extraction
                              Claim Extraction
                                      ↓
                               Entity Resolution
                                      ↓
                               Evidence KG
                                      ↓
                           Wiki Node Generation
                                      ↓
                              Review / Publish
                                      ↓
                                Wiki Index
```

---

## 5. Giải thích từng step của luồng ingest

### 5.1 Raw Source

Nguồn đầu vào ban đầu gồm PDF, paper học thuật, báo cáo, Markdown, clipping và ghi chú nghiên cứu. Đầu ra được lưu tại `02_sources/`.

### 5.2 Normalize

Đưa mọi nguồn về Markdown chuẩn: UTF-8, heading nhất quán, giữ bảng và page marker, bỏ header/footer lặp, chuẩn hóa metadata, gắn `document_id` và tính `content_hash`.

### 5.3 Source Manifest

Theo dõi `document_id`, file path, content hash, source version, chunking version và embedding state. Dùng content hash thay vì chỉ dùng `mtime`.

### 5.4 Adaptive Chunking

Chia tài liệu theo:

```text
heading
→ paragraph
→ table/list boundary
→ semantic coherence
→ token limit
```

Baseline:

```text
target: 400–600 tokens
maximum: 800–1.024 tokens
overlap: 50–100 tokens
```

### 5.5 Stable Chunk Registry

Mỗi chunk có ID ổn định:

```text
chunk_id = hash(document_id + heading_path + normalized_text)
```

Registry lưu document, heading, vị trí, token count, text hash và trạng thái.

### 5.6 Source Embedding bằng BGE-M3

```text
SourceChunk
→ BAAI/bge-m3
→ source_dense.index
```

Payload gồm document title, heading path, tags và chunk text.

### 5.7 Entity Extraction

Nhận diện entity theo ontology: Institution, Country, Currency, Sector, EconomicIndicator, PolicyInstrument, BalanceSheetItem, MarketInstrument, Mechanism và Event.

### 5.8 Relation Extraction

Trích xuất quan hệ như:

```text
TGA
→ drains
Bank reserves
```

Mỗi relation bắt buộc có evidence chunk.

### 5.9 Claim Extraction

Trích xuất mệnh đề có thể kiểm chứng, gồm claim text, scope, conditions, evidence và confidence.

### 5.10 Entity Resolution

Hợp nhất các alias về canonical entity, ví dụ `Fed`, `Federal Reserve`, `Federal Reserve System` và `US central bank`.

### 5.11 Stage KG Objects

Entity, relation và claim mới được đưa vào `04_outputs/staged_kg/` ở trạng thái `proposed`.

### 5.12 Validate Evidence

Kiểm tra relation có evidence, claim có source chunk, entity đã resolve, relation thuộc ontology, source chunk còn active và confidence đạt ngưỡng.

### 5.13 Build Evidence Knowledge Graph

Graph gồm Document, Chunk, Entity, Relation, Claim và WikiNode với các cạnh `contains`, `mentions`, `supports`, `contradicts`, `causes`, `depends_on`, `derived_from` và `synthesizes`.

### 5.14 Wiki Node Generation / Update

LLM tổng hợp claim và evidence thành wiki node có thesis, mechanism, conditions, counterevidence, claim refs, entity refs và evidence refs.

### 5.15 Rule 0 Pre-check

Trước khi tạo node, hệ thống tìm node hiện có, kiểm tra alias và quyết định `SPAWN`, `EXPAND` hoặc `LINK`.

### 5.16 Wiki Audit

Kiểm tra thesis, provenance, scope, contradiction, confidence và claim-level evidence.

### 5.17 Review / Accept

Node chỉ được chuyển vào `03_wiki/` sau review.

### 5.18 Wiki Embedding bằng BGE-M3

```text
WikiNode
→ BAAI/bge-m3
→ wiki_dense.index
```

Payload gồm title, aliases, tags, thesis, mechanism summary và key claims.

### 5.19 Wiki Graph Build

Xây navigation graph:

```text
WikiNode
→ links_to
WikiNode
```

và kết nối wiki với claim:

```text
WikiNode
→ synthesizes
Claim
```

### 5.20 Staleness Check

Khi source thay đổi, hệ thống xác định các chunk, claim, relation, wiki node và index bị ảnh hưởng.

---

## 6. Tầng tìm kiếm — KG²RAG escalation 6 nấc

```text
Query
  │
  ├─ Nấc 1  lexical retrieval
  │         SQLite FTS5 / BM25
  │
  ├─ Nấc 2  source semantic retrieval
  │         BGE-M3 → source_dense.index
  │
  ├─ Nấc 3  wiki semantic retrieval
  │         BGE-M3 → wiki_dense.index
  │
  ├─ Nấc 4  hybrid fusion
  │         BM25 ⊕ source dense ⊕ wiki dense → RRF
  │
  ├─ Nấc 5  KG-guided expansion
  │         seed → entity → relation → claim → evidence chunk
  │
  └─ Nấc 6  rerank + context organization
            cross-encoder → organized analytical context
```

---

## 7. Giải thích từng step của luồng query KG²RAG

### 7.1 Query Understanding

Phân tích entity, intent, geography, time scope, question type và causal/descriptive intent.

### 7.2 BM25 Retrieval

Tìm exact term bằng SQLite FTS5/BM25, phù hợp với tên chính sách, mã chỉ báo, từ viết tắt và thuật ngữ chuyên biệt.

### 7.3 Source Dense Retrieval

```text
Query
→ BGE-M3
→ source_dense.index
```

Tìm source chunk gần về ngữ nghĩa.

### 7.4 Wiki Dense Retrieval

```text
Query
→ BGE-M3
→ wiki_dense.index
```

Tìm wiki node phù hợp về concept và mechanism.

### 7.5 RRF Fusion

Hợp nhất BM25, source dense và wiki dense thành seed ranking thống nhất.

### 7.6 Seed-to-Entity Mapping

Map seed chunk/wiki node về entity trong graph. Đây là bước chuyển từ vector retrieval sang graph retrieval.

### 7.7 KG-Guided Expansion

Mở rộng 1–2 hops theo relation whitelist, confidence threshold, time filter và max candidates.

### 7.8 Evidence Join

Từ relation/claim truy ngược về:

```text
relation
→ claim
→ evidence chunk
→ source document
```

### 7.9 Candidate Union

Hợp nhất BM25 candidates, source dense candidates, wiki candidates và graph-expanded candidates, sau đó deduplicate và loại stale/superseded objects.

### 7.10 Cross-Encoder Reranking

```text
Candidate pool
→ BAAI/bge-reranker-v2-m3
```

Reranker chấm trực tiếp cặp `query + candidate`.

### 7.11 Context Organization

Context được sắp theo:

```text
Observation
→ Direct mechanism
→ Second-order transmission
→ Supporting evidence
→ Counterevidence
→ Boundary conditions
```

### 7.12 Hypothesis Generation

Tạo các giả thuyết cạnh tranh thay vì nhảy ngay đến một kết luận.

### 7.13 Supporting Evidence Retrieval

Tìm evidence ủng hộ từng giả thuyết.

### 7.14 Counterevidence Retrieval

Tìm evidence phản bác hoặc làm yếu từng giả thuyết.

### 7.15 Red-Team Review

Kiểm tra alternative explanation, reverse causality, omitted variable, regime change, data revision và overclaim.

### 7.16 Cross-Review

Kiểm tra consistency, completeness, provenance, scope, time alignment và contradiction coverage.

### 7.17 MODE DEEP Synthesis

Tổng hợp theo:

```text
Top-down
→ Macro
→ Plumbing
→ Treasury
→ Timing
```

Output gồm Main conclusion, Mechanism, Supporting evidence, Counterevidence, Alternative explanation, Confidence, Boundary conditions, Invalidation triggers và Treasury Insight.

### 7.18 Answer with Claim-Level Provenance

Mỗi kết luận quan trọng truy được:

```text
answer sentence
→ claim_id
→ chunk_id
→ document_id
```

---

## 8. Hai lớp index

### Source index

```text
02_sources/*.md
→ adaptive chunks
→ BGE-M3
→ source_dense.index
```

Đơn vị retrieval: `SourceChunk`.

### Wiki index

```text
03_wiki/*.md
→ title + aliases + thesis + mechanism summary + claims
→ BGE-M3
→ wiki_dense.index
```

Đơn vị retrieval: `WikiNode`.

Không trộn SourceChunk và WikiNode trong cùng một index logic.

---

## 9. Evidence Knowledge Graph

### Node types

```text
Document
Chunk
WikiNode
Entity
Claim
Hypothesis
Event
Indicator
Mechanism
```

### Edge types

```text
contains
mentions
supports
contradicts
qualifies
causes
increases
decreases
drains
adds
funds
constrains
transmits_to
amplifies
offsets
depends_on
valid_under
precedes
lags
synthesizes
derived_from
supersedes
links_to
```

### Provenance chain

```text
WikiNode
   ↓ synthesizes
Claim
   ↓ supported_by
SourceChunk
   ↓ belongs_to
SourceDocument
```

---

## 10. Chunking strategy

```text
Markdown heading
   ↓
Paragraph / table boundary
   ↓
Semantic coherence
   ↓
Token limit
```

Baseline:

```text
target: 400–600 tokens
maximum: 800–1.024 tokens
overlap: 50–100 tokens
```

Nguyên tắc:

- không cắt giữa bảng;
- không tách claim khỏi điều kiện;
- không tách mechanism khỏi transmission;
- giữ heading path;
- giữ line/offset;
- bỏ TOC và boilerplate;
- dùng content hash cho chunk ID.

---

## 11. Embedding và reranking

### Dense embedding engine

```text
Model: BAAI/bge-m3
Framework: sentence-transformers
Embedding dimension: 1.024
Normalization: true
Similarity: cosine
Vector index: FAISS IndexFlatIP
```

Không sử dụng prefix `query:` hoặc `passage:`.

### Index separation

```text
.cache/source/source_dense.index
.cache/wiki/wiki_dense.index
```

### Cấu hình baseline

```yaml
embedding:
  engine: BGE-M3
  model_name: BAAI/bge-m3
  framework: sentence-transformers
  dimension: 1024
  normalize_embeddings: true
  similarity: cosine
  faiss_index: IndexFlatIP
  max_length: 1024
  batch_size_gpu: 8
  batch_size_cpu: 2
```

### Reranker

```text
Model: BAAI/bge-reranker-v2-m3
Type: multilingual cross-encoder
```

### Retrieval flow

```text
BM25 candidates
+ BGE-M3 source candidates
+ BGE-M3 wiki candidates
        ↓
RRF seed fusion
        ↓
KG-guided expansion
        ↓
candidate union + deduplication
        ↓
BGE reranker
        ↓
organized context
```

### Manifest

```yaml
engine: BGE-M3
model_name: BAAI/bge-m3
model_revision:
embedding_dimension: 1024
normalization: true
similarity: cosine
max_length: 1024
chunking_version:
payload_version:
corpus_hash:
build_time:
```

Thay đổi model, dimension, normalization, max length, chunking hoặc payload version phải kích hoạt full rebuild.

---

## 12. KG-guided expansion policy

```yaml
max_hops: 2
max_neighbors_per_seed: 20
max_total_candidates: 100
min_relation_confidence: 0.70
min_claim_confidence: 0.65
require_evidence: true
exclude_stale: true
exclude_superseded: true
```

Không cho phép:

- expand toàn bộ neighbor;
- dùng relation không có evidence;
- dùng entity chưa resolve;
- dùng stale edge mặc định;
- dùng superseded claim mà không cảnh báo.

---

## 13. MODE DEEP sau nâng cấp

```text
Top-Down Entry
→ Macro Layer
→ Plumbing Layer
→ Treasury Layer
→ Timing Layer
→ Feedback / Boundary
→ Diagram
→ Conclusion
→ Next Steps
```

Trước synthesis phải có:

```text
Observation
   ↓
Competing Hypotheses
   ↓
Evidence Retrieval
   ↓
Counterevidence Retrieval
   ↓
Red-Team Review
   ↓
Cross-Review
   ↓
Synthesis
```

---

## 14. Contradiction management

```text
Claim A
   ↓ contradicts
Claim B
```

Mỗi claim có thể gắn `valid_under`, `applies_to`, `depends_on`, `valid_from`, `valid_to` và `superseded_by`.

Hệ thống phải phân biệt contradiction thực sự với khác thời kỳ, regime, phạm vi, định nghĩa, cấp độ phân tích hoặc điều kiện giả định.

---

## 15. State model

### Object lifecycle

```text
new
→ extracted
→ proposed
→ staged
→ reviewed
→ approved
→ indexed
→ published
→ stale
→ superseded
```

### Job lifecycle

```text
pending
→ running
→ completed
→ failed
→ retrying
→ cancelled
```

`librarian.py status` phải hiển thị documents changed, chunks stale, entities unresolved, relations pending review, claims without evidence, wiki nodes stale, source index version, wiki index version, graph version và failed jobs.

---

## 16. Quality gates

### Source gate

- metadata đầy đủ;
- content hash hợp lệ;
- stable chunk ID;
- offsets truy ngược được;
- bỏ TOC và boilerplate;
- không vượt max token.

### Entity gate

- canonical name bắt buộc;
- entity type thuộc ontology;
- alias được normalize;
- unresolved entity không vào production graph.

### Relation gate

- head, relation, tail đầy đủ;
- relation type thuộc registry;
- có evidence chunk;
- confidence thấp phải review.

### Claim gate

- claim text rõ;
- có evidence/counterevidence;
- có scope và condition nếu là causal claim;
- stale/superseded status rõ.

### Wiki gate

- thesis bắt buộc;
- claim refs cho luận điểm chính;
- evidence refs đến chunk;
- contradiction không bị xóa;
- Rule 0 pre-check.

### Query gate

- không dùng claim thiếu evidence;
- causal answer phải có mechanism;
- deep analysis phải có counterevidence;
- citation map được về chunk;
- context không vượt redundancy threshold.

---

## 17. Testing

### Unit tests

```text
chunk ID stability
content hash detection
entity normalization
relation validation
provenance resolution
graph traversal limits
manifest compatibility
```

### Retrieval tests

```text
exact lookup
semantic lookup
multi-hop question
causal question
contradiction question
temporal question
source-audit question
```

Metrics:

```text
Recall@K
MRR
nDCG
Evidence Coverage
Citation Accuracy
Graph Expansion Precision
Context Redundancy
Latency
```

---

## 18. Đặc thù vận hành Local ↔ Colab GPU

```text
┌─ LOCAL CPU ──────────────────────────────┐
│ edit source/wiki Markdown               │
│ normalize + chunk registry              │
│ small KG extraction                     │
│ entity resolution review                │
│ graph sync                              │
│ query + audit                           │
└──────────────────┬───────────────────────┘
                   │ Git / artifact transfer
                   ▼
┌─ COLAB GPU ──────────────────────────────┐
│ full BGE-M3 embedding build             │
│ large incremental embedding            │
│ reranker benchmark                     │
│ bulk extraction nếu cần                │
│ package index + manifest               │
└──────────────────┬───────────────────────┘
                   ▼
             pull artifact về local
```

Không dùng `mtime` làm nguồn xác định thay đổi giữa hai máy. Dùng content hash, model revision, chunking version, payload version và corpus hash.

---

## 19. Thứ tự triển khai

### Phase 1 — Evidence Foundation

```text
stable chunk registry
source index riêng
wiki index riêng
chunk-level provenance
BGE-M3 migration
```

### Phase 2 — Evidence Knowledge Graph

```text
entity ontology
relation ontology
claim extraction
entity resolution
evidence graph
KG staging/review
```

### Phase 3 — KG²RAG Query

```text
seed-to-entity mapping
graph expansion
candidate union
reranking
context organization
query trace
```

### Phase 4 — Analytical Debate

```text
hypothesis object
supporting evidence retrieval
counterevidence retrieval
red-team review
cross-review
confidence
invalidation trigger
```

### Phase 5 — Continuous Update

```text
source change detection
affected chunk detection
affected claim detection
stale wiki detection
partial graph rebuild
partial index rebuild
```

---

## 20. Kiến trúc đích end-to-end

```text
Raw Source
   ↓
Normalize
   ↓
Adaptive Chunking
   ├───────────────────────────────┐
   ↓                               ↓
Source Dense / BM25 Index     Entity Extraction
                              Relation Extraction
                              Claim Extraction
                                      ↓
                               Entity Resolution
                                      ↓
                               Evidence KG
                                      ↓
                           Wiki Node Generation
                                      ↓
                              Review / Publish
                                      ↓
                                Wiki Index

Query
   ↓
BM25 + Source Dense + Wiki Dense
   ↓
RRF Seed Retrieval
   ↓
Seed-to-Entity Mapping
   ↓
KG-Guided Expansion
   ↓
Evidence Join
   ↓
Cross-Encoder Reranking
   ↓
Graph-Based Context Organization
   ↓
Hypothesis + Counterevidence Analysis
   ↓
MODE DEEP Synthesis
   ↓
Answer with Claim-Level Provenance
```

---

## 21. Tóm tắt một câu

> **Wiki Link KG²RAG** = một hệ thống tri thức nguyên tử về macro / fixed-income / monetary plumbing, lấy Markdown làm source-of-truth, điều phối qua `librarian.py`, tách riêng source index và wiki index bằng **BGE-M3**, xây heterogeneous Evidence Knowledge Graph ở cấp `Document–Chunk–Entity–Relation–Claim–WikiNode`, truy vấn theo chuỗi `BM25/semantic seed → KG expansion → rerank → context organization`, đồng thời duy trì quality gate, contradiction, staleness và claim-level provenance để phục vụ phân tích MODE DEEP có phản biện.
