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
- **ingest**: Run Phase A (declare candidates, wait for confirm) then Phase B (generate)
- **query**: Read index → select relevant nodes → synthesize → optionally save as new wiki page
- **lint**: Find orphans, broken links, uncited claims, duplicates → output lint report

## Output rules
- All AI-generated files go to `02_Inbox/` first. Never write directly to `03_Wiki/`
- Filename format: `YYYY-MM-DD_[Source]_[ConceptName].md`
- Every file must have valid YAML frontmatter (see schema.md for templates)
- Every claim body must have a citation: `[[filename.pdf#page=X]]`
- Update `00_Schema/log.md` and `00_Schema/alias_registry.md` after every ingest run

## Never
- Write directly to `01_Raw_Sources/`
- Delete any node — mark as `deprecated: true` in frontmatter instead
- Merge two nodes without logging in `log.md`
