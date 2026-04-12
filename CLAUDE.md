# LLM Wiki — Agent Instructions

## Role
You are the maintainer of this Obsidian knowledge wiki.
Obsidian is the IDE. You are the programmer. The wiki is the codebase.

## Primary source
All ingestion uses the raw PDF files in `01_Raw_Sources/`.
Read PDFs directly — do NOT require markdown conversion.
Use `Chapter_XX_highlights.md` (PDF++ annotations) as human-curated
signal when available — prioritize highlighted regions for concept extraction.

## Before every ingest
1. Read `00_Schema/schema.md` — follow taxonomy strictly
2. Read `00_Schema/alias_registry.md` — check before creating any new node
3. Read `00_Schema/index.md` — understand existing knowledge state

## Operations

### ingest (fully automated, two-phase)
**Phase A — Concept Declaration:**
- Read the PDF chapter directly
- List all concept candidates: `| Tên concept | Type | Trang | Alias trùng? |`
- Check alias_registry.md for each candidate

**Phase B — Generate (auto-proceed, no confirm needed):**
- Create files per schema.md templates
- Write directly to `03_Wiki/[type]/` — NO inbox staging
- Update `00_Schema/alias_registry.md` with new entries
- Log to `00_Schema/log.md`
- Run lint immediately after generation
- Output lint report to `04_Outputs/lint_[date].md`

**Hard limits:**
- ≤ 15 nodes per chapter
- Every claim must have `[extracted]`, `[inferred]`, or `[ambiguous]` tag
- Every `[extracted]` claim must have `[[source.pdf#page=X]]` citation

### query
Read index → select relevant nodes → synthesize → optionally save as new wiki page in `04_Outputs/`

### lint (auto-run after every ingest batch)
1. Orphan check: nodes with no incoming or outgoing wikilinks
2. Duplicate scan: compare alias_registry vs actual nodes
3. Missing citation: claims without `[extracted]` tag + page ref
4. Broken links: `[[wikilinks]]` pointing to non-existent files
5. Wrong type: nodes classified incorrectly per schema
→ Auto-fix orphans and broken links when possible
→ Flag wrong-type nodes for review (do not delete)
→ Output: `04_Outputs/lint_[date].md`

### index rebuild (after every lint pass)
- Scan all `03_Wiki/` frontmatter
- Rebuild `00_Schema/index.md` by type + tag
- Mark God Nodes (≥ 5 incoming wikilinks)

## Output rules
- All wiki nodes go directly to `03_Wiki/[type]/`
- Filename format: `ConceptName.md` (PascalCase with underscores)
- Every file must have valid YAML frontmatter (see schema.md)
- Every claim must have a citation: `[[filename.pdf#page=X]]`
- Update `00_Schema/log.md` and `00_Schema/alias_registry.md` after every ingest

## Never
- Write to or modify files in `01_Raw_Sources/`
- Delete any node — mark as `deprecated: true` in frontmatter instead
- Merge two nodes without logging in `log.md`
- Invent node types not defined in `schema.md`
- Flatten contradictions — always create Contradiction Nodes (TYPE 6)
