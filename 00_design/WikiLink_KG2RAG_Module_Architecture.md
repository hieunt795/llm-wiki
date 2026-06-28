# Wiki Link KG²RAG — Cấu trúc module hóa (modular architecture)

> Tài liệu phân rã hệ thống KG²RAG thành các **module có ranh giới rõ**: trách nhiệm đơn lẻ, contract dữ liệu tường minh giữa các tầng, luật phụ thuộc một chiều, và bản đồ tái dùng từ code hiện tại.
>
> Đi kèm: `WikiLink_KG2RAG_System_Architecture.md` (kiến trúc tổng) · `WikiLink_System_Architecture_2026-06-27.md` (trạng thái hiện tại).
>
> Phạm vi: tổ chức `05_scripts/` thành package; định nghĩa interface; không phải spec hành vi từng hàm.

---

## 1. Nguyên tắc module hóa

1. **Một module = một trách nhiệm.** Module không "biết" pipeline gọi nó; nó nhận input theo contract, trả output theo contract.
2. **Phụ thuộc một chiều, theo tầng.** Tầng trên gọi tầng dưới; cấm gọi ngược, cấm gọi ngang lén (phải qua contract). Layer order:
   `orchestrator → (synthesis | retrieval | kg | embedding | ingestion) → governance/io → schema/contracts`.
3. **`librarian.py` chỉ điều phối.** Không chứa logic miền. Mỗi pipeline = chuỗi lời gọi module + `StepRunner`.
4. **Contract = dataclass + manifest, không phải "đọc bừa file của nhau".** Mọi trao đổi liên-module đi qua object có schema (mục 5) hoặc artifact có manifest (mục 8).
5. **Source-of-truth là `.md` + registry YAML.** Mọi `.index/.db/.json` trong `.cache` là phái sinh, module nào sinh ra thì module đó sở hữu (mục 8).
6. **Determinism qua hash, không qua mtime.** ID và phát hiện thay đổi dùng `content_hash`; cấm dùng `mtime` làm nguồn xác định cross-machine.
7. **Stateless engine, stateful registry.** Engine module thuần hàm (input→output, không giữ state ngầm); state nằm ở registry/manifest tách riêng.

---

## 2. Sơ đồ tầng + luật phụ thuộc

```text
┌──────────────────────────────────────────────────────────────────────┐
│ L5  ORCHESTRATION         librarian.py  (pipelines + StepRunner)        │
└───────────────┬──────────────────────────────────────────────────────┘
                │ chỉ gọi xuống — không module nào import librarian
   ┌────────────┼─────────────┬──────────────┬───────────────┐
   ▼            ▼             ▼              ▼               ▼
┌────────┐ ┌──────────┐ ┌──────────┐  ┌──────────┐    ┌──────────┐
│L4 synth│ │L4 retriev│ │  L3 kg   │  │L2 embed  │    │L2 ingest │
└───┬────┘ └────┬─────┘ └────┬─────┘  └────┬─────┘    └────┬─────┘
    │           │            │             │               │
    └───────────┴─────┬──────┴─────────────┴───────────────┘
                      ▼
            ┌───────────────────────┐
            │ L1  governance + io   │  (audit · manifest · hashing · fs)
            └───────────┬───────────┘
                        ▼
            ┌───────────────────────┐
            │ L0  contracts/schema  │  (dataclasses · ontology YAML)
            └───────────────────────┘
```

**Luật cứng:**
- L0 không import gì trong repo (chỉ stdlib/pydantic).
- L1 chỉ import L0.
- L2/L3 import L0–L1, **không** import nhau ngang trừ qua contract object.
- L4 import L0–L3.
- L5 import tất cả nhưng **không chứa logic miền**.
- Cấm import vòng. Vi phạm = lỗi build (mục 10 có lint check).

---

## 3. Cây package đích (`05_scripts/`)

```text
05_scripts/
├── __init__.py
│
├── contracts/                 # L0 — schema/dataclass, không phụ thuộc gì
│   ├── ids.py                 # chunk_id/entity_id/claim_id hashing helpers
│   ├── source.py              # Document, SourceChunk
│   ├── kg.py                  # Entity, Relation, Claim, Hypothesis, Edge
│   ├── wiki.py                # WikiNode (frontmatter v4 + refs mới)
│   ├── retrieval.py           # Candidate, SeedSet, RankedContext
│   └── manifest.py            # SourceManifest, EmbeddingManifest, GraphManifest
│
├── io/                        # L1 — filesystem + state, thuần kỹ thuật
│   ├── fs.py                  # đọc/ghi .md, glob, atomic write
│   ├── hashing.py             # content_hash, payload_hash, corpus_hash
│   ├── manifest_store.py      # load/save manifest, so diff version
│   └── md_frontmatter.py      # parse/serialize YAML frontmatter
│
├── governance/                # L1 — quality gate, không sinh tri thức
│   ├── claim_auditor.py       # ♻ F.I.T.S.E.R.B.V.L (giữ)
│   ├── provenance_auditor.py  # ✚ claim→chunk→doc còn sống?
│   ├── contradiction_auditor.py # ✚ contradiction thật vs khác regime
│   ├── alias_guard.py         # ♻ Rule 0 pre-check (từ sync_registry/alias)
│   ├── find_orphans.py        # ♻ (giữ)
│   ├── auto_bridge.py         # ♻ (giữ)
│   └── rename_node.py         # ♻ (giữ)
│
├── ingestion/                 # L2 — raw → chunk
│   ├── normalize_source.py    # ✚ (gộp normalize_ocr_md + extract_pdf hậu xử lý)
│   ├── extract_pdf.py         # ♻ PDF→MD (giữ, + extract_pdf_docling)
│   ├── chunk_sources.py       # ✚ adaptive chunking
│   ├── chunk_registry.py      # ✚ stable chunk_id store
│   ├── source_manifest.py     # ✚ document_id + content_hash tracking
│   └── inbox_processor.py     # ♻ (giữ)
│
├── embedding/                 # L2 — text → vector (BGE-M3)
│   ├── encoder.py             # ✚ wrapper BGE-M3 (1 nơi load model)
│   ├── embed_source_index.py  # ✚ SourceChunk → source_dense.index
│   ├── embed_wiki_index.py    # ⟳ embed_index.py refactor → wiki_dense.index
│   └── embedding_manifest.py  # ✚ model/dim/version → trigger rebuild
│
├── kg/                        # L3 — Evidence Knowledge Graph
│   ├── extract_entities.py    # ✚
│   ├── extract_relations.py   # ✚ (mỗi relation phải có evidence chunk)
│   ├── extract_claims.py      # ✚
│   ├── resolve_entities.py    # ✚ alias → canonical
│   ├── resolve_relations.py   # ✚
│   ├── build_evidence_graph.py# ✚ → .cache/kg/evidence.db + evidence_graph.json
│   ├── build_wiki_graph.py    # ⟳ _build_wiki_graph.py (giữ logic, đổi output path)
│   ├── kg_validate.py         # ✚ gate trước publish
│   └── kg_staleness.py        # ✚ source đổi → object bị ảnh hưởng
│
├── retrieval/                 # L4 — query → context
│   ├── fts5_engine.py         # ♻ (giữ)
│   ├── wiki_search.py         # ♻ (giữ, RRF)
│   ├── semantic_search.py     # ⟳ trỏ encoder BGE-M3, 2 index
│   ├── hybrid_search.py       # ⟳ RRF: BM25 ⊕ source_dense ⊕ wiki_dense
│   ├── deepdive_search.py     # ♻ (giữ)
│   ├── kg_expand.py           # ✚ seed→entity→relation→claim (policy mục 5)
│   ├── candidate_union.py     # ✚ union + dedup + loại stale/superseded
│   ├── rerank.py              # ✚ bge-reranker-v2-m3 cross-encoder
│   └── context_organizer.py   # ✚ sắp xếp Observation→…→Boundary
│
└── synthesis/                 # L4 — phân tích/phản biện
    ├── auto_ingest.py         # ♻ (giữ, bán-tự-động W2)
    ├── auto_synthesis.py      # ♻ wisdom (giữ)
    ├── hypothesis_builder.py  # ✚ competing hypotheses
    └── analytical_review.py   # ✚ red-team + cross-review

# Chú thích: ♻ giữ nguyên · ⟳ refactor tại chỗ · ✚ viết mới
```

> Các util không thuộc miền KG²RAG (`vis_protocol`, `gen_index`, `daily_quest`, `sla_*`, `organize_nodes`, `raw_scout`, `suggest_ideas`, `system_tools`) giữ ở `05_scripts/` gốc hoặc gom vào `tools/`; không nằm trong layering bắt buộc trên.

---

## 4. Đặc tả module (responsibility · interface · contract)

Mỗi module công khai **một bề mặt hàm hẹp**. Dưới đây là interface tối thiểu (signature minh họa, không phải code cuối).

### L2 · ingestion

| Module | Hàm public | Input → Output |
|---|---|---|
| `normalize_source` | `normalize(path) -> Document` | file thô → `Document` (UTF-8, heading chuẩn, `content_hash`) |
| `chunk_sources` | `chunk(doc: Document) -> list[SourceChunk]` | Document → chunks (400–600 tok, giữ heading_path/offset) |
| `chunk_registry` | `upsert(chunks) -> ChunkDiff` / `get(chunk_id)` | chunks → diff (added/changed/removed) |
| `source_manifest` | `record(doc) -> None` / `changed() -> list[doc_id]` | theo dõi content_hash, không mtime |

### L2 · embedding

| Module | Hàm public | Input → Output |
|---|---|---|
| `encoder` | `encode(texts: list[str]) -> np.ndarray` | nơi **duy nhất** load `BAAI/bge-m3`, normalize, **không prefix** |
| `embed_source_index` | `build(chunks, mode) -> EmbeddingManifest` | SourceChunk → `source_dense.index` |
| `embed_wiki_index` | `build(nodes, mode) -> EmbeddingManifest` | WikiNode → `wiki_dense.index` |
| `embedding_manifest` | `needs_rebuild(old, new) -> bool` | so model/dim/normalize/chunking/payload version |

### L3 · kg

| Module | Hàm public | Input → Output |
|---|---|---|
| `extract_entities` | `extract(chunk) -> list[Entity]` | chunk → entity theo ontology |
| `extract_relations` | `extract(chunk) -> list[Relation]` | chunk → relation (**bắt buộc** `evidence_chunk_id`) |
| `extract_claims` | `extract(chunk) -> list[Claim]` | chunk → claim (text/scope/conditions/confidence) |
| `resolve_entities` | `resolve(entities) -> list[Entity]` | alias → canonical (registry YAML) |
| `build_evidence_graph` | `build(objects) -> GraphManifest` | staged KG → `evidence.db` + `evidence_graph.json` |
| `kg_validate` | `validate(objects) -> GateReport` | gate: relation có evidence? entity resolved? |
| `kg_staleness` | `affected(doc_id) -> AffectedSet` | doc đổi → {chunk, claim, relation, node, index} |

### L4 · retrieval

| Module | Hàm public | Input → Output |
|---|---|---|
| `hybrid_search` | `seeds(query, k) -> SeedSet` | query → RRF(BM25 ⊕ source ⊕ wiki) |
| `kg_expand` | `expand(seeds, policy) -> list[Candidate]` | seed → graph candidates (≤2 hop) |
| `candidate_union` | `merge(*pools) -> list[Candidate]` | union + dedup + drop stale/superseded |
| `rerank` | `rank(query, candidates) -> list[Candidate]` | cross-encoder `bge-reranker-v2-m3` |
| `context_organizer` | `organize(ranked) -> RankedContext` | sắp Observation→mechanism→evidence→counter→boundary |

### L4 · synthesis

| Module | Hàm public | Input → Output |
|---|---|---|
| `hypothesis_builder` | `propose(context) -> list[Hypothesis]` | context → giả thuyết cạnh tranh |
| `analytical_review` | `red_team(h)` / `cross_review(out)` | kiểm reverse-causality/omitted-var/overclaim |

---

## 5. Data contracts (L0 — schema giữa các module)

Các object này là **API thật sự** giữa các tầng. Đổi field = đổi version (manifest), kéo theo rebuild.

```python
# contracts/source.py
@dataclass(frozen=True)
class Document:
    document_id: str            # hash(canonical_path)
    path: str
    title: str
    content_hash: str           # hash(normalized_text) — KHÔNG mtime
    source_version: int

@dataclass(frozen=True)
class SourceChunk:
    chunk_id: str               # hash(document_id + heading_path + normalized_text)
    document_id: str
    heading_path: list[str]
    text: str
    token_count: int
    char_offset: tuple[int, int]
    text_hash: str
    status: str                 # active | stale | superseded
```

```python
# contracts/kg.py
@dataclass(frozen=True)
class Entity:
    entity_id: str              # hash(canonical_name + type)
    canonical_name: str
    type: str                   # Institution|Country|Currency|... (ontology)
    aliases: list[str]
    resolved: bool

@dataclass(frozen=True)
class Relation:
    relation_id: str
    head: str                   # entity_id
    type: str                   # drains|funds|transmits_to|... (registry)
    tail: str                   # entity_id
    evidence_chunk_id: str      # BẮT BUỘC — không evidence = không vào graph
    confidence: float

@dataclass(frozen=True)
class Claim:
    claim_id: str
    text: str
    scope: str | None
    conditions: list[str]
    evidence_chunk_ids: list[str]
    counterevidence_chunk_ids: list[str]
    confidence: float
    valid_from: str | None
    valid_to: str | None
    superseded_by: str | None
```

```python
# contracts/wiki.py — mở rộng frontmatter v4 hiện tại (KHÔNG phá field cũ)
@dataclass
class WikiNode:
    # ── giữ nguyên v4 ──
    title: str; aliases: list[str]; type: str; tags: list[str]
    status: str; confidence: int; thesis: str
    source_refs: list[dict]     # [{file, page}]
    # ── thêm cho KG²RAG (optional, backward-compatible) ──
    claim_refs: list[str]       # claim_id
    entity_refs: list[str]      # entity_id
    evidence_refs: list[str]    # chunk_id
```

```python
# contracts/retrieval.py
@dataclass
class Candidate:
    ref_id: str                 # chunk_id | node_id | claim_id
    kind: str                   # source_chunk | wiki_node | claim
    score: float
    provenance: dict            # {claim_id?, chunk_id?, document_id?}

@dataclass
class RankedContext:
    sections: dict              # observation, mechanism, evidence, counter, boundary
    citations: list[dict]       # answer_span → claim_id → chunk_id → document_id
```

**KG-expansion policy** (`contracts/kg.py`, đọc bởi `kg_expand`):

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

---

## 6. Orchestrator: pipeline → module (L5)

`librarian.py` giữ pattern hiện tại (mỗi pipeline 1 hàm `cmd_*`, `StepRunner` hỗ trợ `--skip/--only`). Thêm pipeline = thêm hàm, **không sửa dispatch**.

| Lệnh | Chuỗi module |
|---|---|
| `source ingest <f>` | `normalize_source` → `source_manifest` → `chunk_sources` → `chunk_registry` → `embed_source_index` |
| `kg build <doc>` | `extract_entities` → `extract_relations` → `extract_claims` → `resolve_entities` → stage (`io`) |
| `kg publish` | `kg_validate` → `build_evidence_graph` → `embedding_manifest.needs_rebuild?` |
| `wiki ingest <f>` | `alias_guard` (Rule 0) → stage → `claim_auditor`+`provenance_auditor` → accept → `embed_wiki_index` |
| `sync` | `build_wiki_graph` → `build_evidence_graph` → `gen_index` → `kg_staleness` |
| `search <q>` | `hybrid_search.seeds` (BM25⊕source⊕wiki RRF) |
| `search --kg <q>` | `hybrid_search` → `kg_expand` → `candidate_union` → `rerank` → `context_organizer` |
| `search --kg --deep <q>` | `…--kg` → `hypothesis_builder` → `analytical_review` → MODE DEEP (5 Lenses) |
| `health` | `find_orphans` → `kg_validate` → `kg_staleness` |
| `audit <f>` | `claim_auditor` → `provenance_auditor` → `contradiction_auditor` |
| `embed` | `embed_source_index` / `embed_wiki_index` (`--incremental`|`--build`) |

---

## 7. Bản đồ tái dùng (script hiện tại → module đích)

| Script hiện có | Đích | Việc cần làm |
|---|---|---|
| `librarian.py` | L5 orchestrator | Thêm hàm `cmd_*` mới; giữ dispatch |
| `embed_index.py` | `embedding/embed_wiki_index.py` | ⟳ tách `encoder`, đổi BGE-M3, bỏ prefix `passage:`/`query:`, dim 1024 |
| `fts5_engine.py` | `retrieval/fts5_engine.py` | ♻ giữ |
| `wiki_search.py` | `retrieval/wiki_search.py` | ♻ giữ |
| `semantic_search.py` | `retrieval/semantic_search.py` | ⟳ trỏ `encoder`, hỗ trợ 2 index |
| `hybrid_search.py` | `retrieval/hybrid_search.py` | ⟳ thêm nhánh `source_dense` vào RRF |
| `deepdive_search.py` | `retrieval/deepdive_search.py` | ♻ giữ |
| `_build_wiki_graph.py` | `kg/build_wiki_graph.py` | ⟳ đổi output path (`wiki_graph.json`) |
| `claim_auditor.py` | `governance/claim_auditor.py` | ♻ giữ |
| `sync_registry.py`/`alias_registry.md` | `governance/alias_guard.py` | ⟳ bọc thành Rule 0 API |
| `find_orphans/auto_bridge/rename_node` | `governance/` | ♻ giữ |
| `normalize_ocr_md.py` | `ingestion/normalize_source.py` | ⟳ gộp |
| `extract_pdf(_docling).py` | `ingestion/extract_pdf.py` | ♻ giữ |
| `auto_ingest/auto_synthesis.py` | `synthesis/` | ♻ giữ |
| — (chưa có) | `ingestion/chunk_*`, `kg/*`, `embedding/embed_source_*`, `retrieval/{kg_expand,candidate_union,rerank,context_organizer}`, `synthesis/{hypothesis_builder,analytical_review}` | ✚ viết mới |

---

## 8. Quyền sở hữu artifact (ai ghi cái gì)

Mỗi artifact `.cache` có **đúng một module owner** (writer); module khác chỉ đọc.

| Artifact | Owner (writer) | Reader |
|---|---|---|
| `.cache/source/source_dense.index` + `.meta.json` | `embed_source_index` | `semantic_search`, `hybrid_search` |
| `.cache/source/source_manifest.json` | `source_manifest` | `chunk_sources`, `embed_source_index` |
| `.cache/wiki/wiki_dense.index` + `.meta.json` | `embed_wiki_index` | `semantic_search`, `hybrid_search` |
| `.cache/sparse/wiki_index.db` (FTS5) | `fts5_engine` | `wiki_search` |
| `.cache/kg/evidence.db` + `evidence_graph.json` | `build_evidence_graph` | `kg_expand`, `kg_validate` |
| `.cache/kg/resolution_cache.json` | `resolve_entities` | `extract_relations` |
| `.cache/query/rerank_cache/`, `traces/` | `rerank`, `context_organizer` | — |
| `graphify-out/wiki_graph.json` | `build_wiki_graph` | viz |

**Manifest = hợp đồng rebuild.** `embedding_manifest.needs_rebuild()` so các trường: `model_name, dimension, normalize, max_length, chunking_version, payload_version, corpus_hash`. Lệch bất kỳ trường nào → full rebuild (chạy trên Colab GPU, không incremental cross-machine).

---

## 9. Lifecycle & state (ngang qua module)

```text
Object:  new → extracted → proposed → staged → reviewed → approved → indexed → published → stale → superseded
Job:     pending → running → completed → failed → retrying → cancelled
```

- State **không nằm trong engine module**; lưu ở `io/manifest_store` + frontmatter `status`.
- `librarian.py status` đọc state từ các manifest, hiển thị: documents changed · chunks stale · entities unresolved · relations pending · claims without evidence · wiki nodes stale · index versions · graph version · failed jobs.

---

## 10. Luật kiểm soát ranh giới (giữ module hóa không phân rã)

1. **Import lint:** L0 không import nội bộ; không import vòng; không ai import `librarian`. (CI: 1 script quét `import` theo layer.)
2. **Một điểm load model:** chỉ `embedding/encoder.py` được `SentenceTransformer(...)`. Grep thấy chỗ khác = vi phạm.
3. **Không đọc chéo artifact:** module chỉ chạm artifact mình sở hữu hoặc qua reader API (mục 8).
4. **Contract trước, code sau:** đổi dataclass L0 phải bump version + ghi vào `embedding_manifest`/`graph_manifest`.
5. **Engine thuần:** module L2–L4 không tự quyết định "có chạy hay không" — đó là việc của `StepRunner` ở L5.

---

## 11. Thứ tự build (map sang 5 Phase)

| Phase | Module mới đưa vào | Mốc verify |
|---|---|---|
| **1 — Evidence Foundation** | `contracts/*`, `io/*`, `encoder`, `chunk_sources`, `chunk_registry`, `source_manifest`, `embed_source_index`, refactor `embed_wiki_index` | Recall@K (BGE-M3) ≥ baseline e5; 2 index dựng được; giữ index e5 cũ làm fallback |
| **2 — Evidence KG** | `kg/extract_*`, `resolve_*`, `build_evidence_graph`, `kg_validate`, `governance/provenance_auditor`, `contradiction_auditor` | Evidence Coverage · mọi relation có evidence_chunk_id · entity resolution chính xác |
| **3 — KG²RAG Query** | `retrieval/{kg_expand, candidate_union, rerank, context_organizer}` | Graph Expansion Precision · Citation Accuracy · Context Redundancy dưới ngưỡng |
| **4 — Analytical Debate** | `synthesis/{hypothesis_builder, analytical_review}` | mỗi MODE DEEP có competing hypotheses + counterevidence + invalidation trigger |
| **5 — Continuous Update** | `kg/kg_staleness`, partial rebuild trong manifest | source đổi → chỉ rebuild phần bị ảnh hưởng |

> Nguyên tắc an toàn xuyên suốt: build artifact mới **song song**, không ghi đè index e5 cũ cho tới khi Phase 1 verify xong.

---

## 12. Tóm tắt một câu

> **Module hóa Wiki Link KG²RAG** = giữ `librarian.py` làm tầng điều phối mỏng, gom `05_scripts/` thành 6 package theo tầng (`ingestion → embedding → kg → retrieval → synthesis`, tựa trên `governance/io` và `contracts/`), bắt mọi trao đổi liên-module đi qua dataclass có version + manifest sở hữu-đơn-nhất, áp luật phụ thuộc một chiều và một-điểm-load-model — để nâng cấp được thực hiện **cộng thêm module mới** thay vì viết lại, tái dùng tối đa engine tìm kiếm và quality-gate hiện có.
