# Wiki Schema v2

## Core principles
1. Raw PDF is the source of truth. The wiki is a derived artifact.
2. Every claim must cite a specific page: `[[file.pdf#page=X]]`
3. Never delete a contradicting viewpoint — tag it `[ambiguous]`
4. Check alias_registry.md before creating any new node
5. Provenance must be declared on every node

## Node taxonomy

### TYPE 1 — Definition
When: "X là gì"
Frontmatter:
  type: definition
  aliases: []
  sources: []
  confidence: high | medium | low
  provenance: extracted | inferred | ambiguous
Required headings: `## Định nghĩa`, `## Phân biệt với`, `## Nguồn`

### TYPE 2 — Mechanism
When: "X hoạt động như thế nào / tại sao Y xảy ra"
Frontmatter:
  type: mechanism
  trigger: ""
  output: ""
  constraints: []
  provenance: extracted | inferred | ambiguous
Required headings: `## Cơ chế`, `## Điều kiện`, `## Ví dụ số`

### TYPE 3 — Relationship
When: "X tác động đến Y qua Z"
Frontmatter:
  type: relationship
  from: "[[X]]"
  to: "[[Y]]"
  via: "[[Z]]"
  direction: unidirectional | bidirectional
  provenance: extracted | inferred | ambiguous

### TYPE 4 — Evidence
When: Số liệu thực nghiệm, dữ liệu, case study
Location: `03_Wiki/evidence/` — KHÔNG phải concepts/
Frontmatter:
  type: evidence
  date_observed: ""
  source_page: ""
  provenance: extracted

### TYPE 5 — Perspective
When: Quan điểm riêng của một tác giả
Frontmatter:
  type: perspective
  author: "[[Author_Name]]"
  stance: agrees_with | contradicts | extends
  ref_node: "[[Concept_Node]]"
  provenance: extracted

### TYPE 6 — Contradiction
When: Hai sources nói ngược nhau về cùng vấn đề
Location: `03_Wiki/contradictions/`
Requirements: Bắt buộc ≥ 2 citation từ 2 sources khác nhau
Required headings: `## Góc nhìn A`, `## Góc nhìn B`, `## Điểm mâu thuẫn`
Tags: #contradiction
Frontmatter:
  type: contradiction
  provenance: ambiguous

## Provenance inline tags
- `[extracted]` — trích thẳng từ source, có page cite
- `[inferred]` — LLM synthesis từ nhiều sources
- `[ambiguous]` — sources không đồng ý nhau

## Memory tiers (LLM Wiki v2)
Promote nodes lên tier cao hơn khi evidence tích lũy đủ:
- Tier 1 (episodic): seen once — `confidence: low`
- Tier 2 (semantic): seen 3+ times across sources — `confidence: medium`
- Tier 3 (procedural): core pattern, fully cross-referenced — `confidence: high`

## Citation format
[[filename.pdf#page=X]]
