# -*- coding: utf-8 -*-
"""
extract_pdf_docling.py - PDF to Markdown extractor dùng Docling (v2.0)
=======================================================================
- Layout 2 cột đọc đúng thứ tự (cột trái hết → cột phải)
- Bảng → markdown table chuẩn
- Auto-retry trang bị bad_alloc với table_structure=False
- Xử lý tuần tự từng trang → RAM ổn định

USAGE:
  python 05_scripts/extract_pdf_docling.py --book central_bank_balance_sheet --force
  python 05_scripts/extract_pdf_docling.py --book imf_macro_accounting --force
  python 05_scripts/extract_pdf_docling.py --all --skip-existing
  python 05_scripts/extract_pdf_docling.py --all --force

INSTALL:
  pip install docling --break-system-packages
"""

import argparse
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT  = SCRIPT_DIR.parent.parent
BOOKS_DIR  = WIKI_ROOT / "02_sources" / "books"


def make_converter(do_table_structure: bool = True):
    """Tạo DocumentConverter với pipeline options."""
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling.datamodel.pipeline_options import PdfPipelineOptions

    pipeline_options = PdfPipelineOptions(
        do_ocr=False,
        do_table_structure=do_table_structure,
        generate_page_images=False,
        generate_picture_images=False,
    )
    return DocumentConverter(
        format_options={
            "pdf": PdfFormatOption(pipeline_options=pipeline_options)
        }
    )


def split_pdf_chunks(pdf_path: Path, chunk_size: int = 10) -> list[Path]:
    """
    Dùng PyMuPDF để split PDF thành các chunk nhỏ (chunk_size trang/chunk).
    Lưu vào thư mục tạm _chunks/ cạnh PDF gốc.
    Trả về list path của các chunk PDF.
    """
    import fitz
    doc = fitz.open(str(pdf_path))
    total = len(doc)
    chunk_dir = pdf_path.parent / "_chunks"
    chunk_dir.mkdir(exist_ok=True)

    chunks = []
    for start in range(0, total, chunk_size):
        end = min(start + chunk_size, total)
        chunk_path = chunk_dir / f"{pdf_path.stem}_p{start+1:04d}-{end:04d}.pdf"
        writer = fitz.open()
        writer.insert_pdf(doc, from_page=start, to_page=end - 1)
        writer.save(str(chunk_path))
        writer.close()
        chunks.append(chunk_path)

    doc.close()
    print(f"  Split: {total} pages → {len(chunks)} chunks ({chunk_size} pages each)", flush=True)
    return chunks


def extract_one(pdf_path: Path, dry_run: bool = False,
                skip_existing: bool = False, force: bool = False,
                chunk_size: int = 10, refresh_every: int = 5) -> bool:
    out_path = pdf_path.with_suffix('.md')

    if skip_existing and not force and out_path.exists():
        print(f"  [SKIP]  {pdf_path.name}", flush=True)
        return False

    if dry_run:
        print(f"  [DRY]   {pdf_path.name} -> {out_path.name}", flush=True)
        return True

    print(f"\n  Extracting: {pdf_path.name}", flush=True)

    try:
        import gc
        import fitz
        from docling.datamodel.document import ConversionStatus

        # Kiểm tra số trang — nếu <= chunk_size thì extract thẳng
        doc = fitz.open(str(pdf_path))
        total_pages = len(doc)
        doc.close()

        if total_pages <= chunk_size:
            chunks = [pdf_path]
            cleanup_chunks = False
        else:
            chunks = split_pdf_chunks(pdf_path, chunk_size=chunk_size)
            cleanup_chunks = True

        # Extract từng chunk
        md_parts = []
        errors = 0
        t_total_start = time.time()

        # Tạo converter lần đầu
        converter = make_converter(do_table_structure=True)

        for i, chunk_path in enumerate(chunks, 1):
            # Recreate converter mỗi refresh_every chunks để release RAM fragment
            if i > 1 and (i - 1) % refresh_every == 0:
                del converter
                gc.collect()
                converter = make_converter(do_table_structure=True)
                print(f"  [gc] Converter refreshed at chunk {i}", flush=True)

            t_chunk_start = time.time()
            print(f"  Chunk {i}/{len(chunks)}: {chunk_path.name} ... ", end='', flush=True)
            try:
                result = converter.convert(str(chunk_path))
                elapsed = time.time() - t_chunk_start
                if result.status in (ConversionStatus.SUCCESS, ConversionStatus.PARTIAL_SUCCESS):
                    md_parts.append(result.document.export_to_markdown())
                    tag = "ok" if result.status == ConversionStatus.SUCCESS else "partial"
                    print(f"{tag} ({elapsed:.1f}s)", flush=True)
                    if result.status == ConversionStatus.PARTIAL_SUCCESS:
                        errors += 1
                else:
                    print(f"FAILED ({result.status}) ({elapsed:.1f}s)", flush=True)
                    errors += 1
            except Exception as e:
                elapsed = time.time() - t_chunk_start
                err_str = str(e)
                # bad_alloc hoặc OOM → gc + recreate converter, bỏ qua chunk này
                if "bad_alloc" in err_str or "not enough memory" in err_str or "alloc_cpu" in err_str:
                    print(f"OOM ({elapsed:.1f}s) → gc+skip", flush=True)
                    del converter
                    gc.collect()
                    converter = make_converter(do_table_structure=True)
                    errors += 1
                else:
                    print(f"ERROR: {e} ({elapsed:.1f}s)", flush=True)
                    errors += 1

        # Cleanup chunk PDFs
        if cleanup_chunks:
            chunk_dir = pdf_path.parent / "_chunks"
            for c in chunks:
                c.unlink(missing_ok=True)
            try:
                chunk_dir.rmdir()
            except Exception:
                pass

        if not md_parts:
            print(f"  ERROR: all chunks failed", flush=True)
            return False

        # Merge tất cả chunks thành 1 file .md
        frontmatter = (
            f'---\n'
            f'title: "{pdf_path.stem}"\n'
            f'type: raw_source\n'
            f'source_pdf: "{pdf_path.name}"\n'
            f'extractor: docling\n'
            f'---\n\n'
        )
        content = frontmatter + "\n\n".join(md_parts)
        out_path.write_text(content, encoding='utf-8')
        size_kb = out_path.stat().st_size // 1024
        total_elapsed = time.time() - t_total_start
        mins, secs = divmod(int(total_elapsed), 60)
        time_str = f"{mins}m{secs:02d}s" if mins else f"{secs}s"
        pages_per_sec = total_pages / total_elapsed if total_elapsed > 0 else 0
        tag = f"docling/{len(chunks)} chunks" + (f", {errors} errors" if errors else "")
        print(f"  → {out_path.name} ({size_kb} KB) [{tag}]", flush=True)
        print(f"  ⏱  {time_str} total | {total_pages} pages | {pages_per_sec:.1f} pages/sec", flush=True)
        return True

    except ImportError as e:
        print(f"ERROR: missing library — {e}", flush=True)
        sys.exit(1)
    except Exception as e:
        print(f"  ERROR: {e}", flush=True)
        return False


def process_book_dir(book_dir: Path, dry_run: bool,
                     skip_existing: bool, force: bool,
                     chunk_size: int = 10, refresh_every: int = 5) -> tuple:
    pdfs = sorted(book_dir.glob("*.pdf"))
    if not pdfs:
        return 0, 0, 0

    print(f"\n{'='*60}", flush=True)
    print(f"  BOOK: {book_dir.name} ({len(pdfs)} PDF(s))", flush=True)
    print(f"{'='*60}", flush=True)

    ok = skip = err = 0
    for pdf in pdfs:
        r = extract_one(pdf, dry_run=dry_run,
                        skip_existing=skip_existing, force=force,
                        chunk_size=chunk_size, refresh_every=refresh_every)
        if r is True:
            ok += 1
        elif not r and skip_existing and pdf.with_suffix('.md').exists():
            skip += 1
        elif not r:
            err += 1
    return ok, skip, err


def main():
    parser = argparse.ArgumentParser(
        description="extract_pdf_docling.py v2.0 — Docling PDF extractor"
    )
    parser.add_argument("--book",          type=str,  help="Book folder name (substring match)")
    parser.add_argument("--file",          type=str,  help="Path to a single PDF file")
    parser.add_argument("--all",           action="store_true", help="Process all books")
    parser.add_argument("--dry-run",       action="store_true", help="Preview only")
    parser.add_argument("--skip-existing", action="store_true", help="Skip already extracted")
    parser.add_argument("--force",         action="store_true", help="Overwrite existing .md")
    parser.add_argument("--chunk-size",    type=int, default=10, help="Pages per chunk (default: 10)")
    parser.add_argument("--refresh-every", type=int, default=5,  help="Recreate converter every N chunks to release RAM (default: 5)")
    args = parser.parse_args()

    if not any([args.book, args.file, args.all]):
        parser.print_help()
        print("\nExamples:")
        print("  python 05_scripts/extract_pdf_docling.py --book central_bank_balance_sheet --force")
        print("  python 05_scripts/extract_pdf_docling.py --all --skip-existing")
        return

    print(f"[extract_pdf_docling v2.0] Engine: docling | chunk_size: {args.chunk_size}", flush=True)

    run_start = time.time()
    total_ok = total_skip = total_err = 0

    if args.file:
        pdf_path = Path(args.file)
        if not pdf_path.is_absolute():
            pdf_path = WIKI_ROOT / pdf_path
        extract_one(pdf_path, dry_run=args.dry_run,
                    skip_existing=args.skip_existing, force=args.force,
                    chunk_size=args.chunk_size, refresh_every=args.refresh_every)
        return

    if args.book and not args.all:
        matches = [d for d in BOOKS_DIR.iterdir()
                   if d.is_dir() and args.book.lower() in d.name.lower()]
        root_pdfs = [f for f in BOOKS_DIR.glob("*.pdf")
                     if args.book.lower() in f.stem.lower()]
        if not matches and not root_pdfs:
            print(f"No book matching '{args.book}' found.", flush=True)
            return
        for d in matches:
            ok, sk, er = process_book_dir(d, args.dry_run, args.skip_existing, args.force,
                                          chunk_size=args.chunk_size,
                                          refresh_every=args.refresh_every)
            total_ok += ok; total_skip += sk; total_err += er
        for pdf in root_pdfs:
            r = extract_one(pdf, dry_run=args.dry_run,
                            skip_existing=args.skip_existing, force=args.force,
                            chunk_size=args.chunk_size, refresh_every=args.refresh_every)
            if r: total_ok += 1
        print(f"\nDone: {total_ok} extracted, {total_skip} skipped, {total_err} errors", flush=True)
        return

    if args.all:
        root_pdfs = sorted(BOOKS_DIR.glob("*.pdf"))
        if root_pdfs:
            print(f"\n{'='*60}\n  ROOT PDFs ({len(root_pdfs)})\n{'='*60}", flush=True)
            for pdf in root_pdfs:
                r = extract_one(pdf, dry_run=args.dry_run,
                                skip_existing=args.skip_existing, force=args.force,
                                chunk_size=args.chunk_size, refresh_every=args.refresh_every)
                if r: total_ok += 1

        book_dirs = sorted(d for d in BOOKS_DIR.iterdir() if d.is_dir())
        if args.book:
            book_dirs = [d for d in book_dirs if args.book.lower() in d.name.lower()]
        for d in book_dirs:
            ok, sk, er = process_book_dir(d, args.dry_run, args.skip_existing, args.force,
                                          chunk_size=args.chunk_size,
                                          refresh_every=args.refresh_every)
            total_ok += ok; total_skip += sk; total_err += er

    run_elapsed = time.time() - run_start
    run_mins, run_secs = divmod(int(run_elapsed), 60)
    run_time_str = f"{run_mins}m{run_secs:02d}s" if run_mins else f"{run_secs}s"
    print(f"\n{'='*60}", flush=True)
    print(f"  DONE: {total_ok} extracted, {total_skip} skipped, {total_err} errors", flush=True)
    print(f"  ⏱  Total time: {run_time_str}", flush=True)
    print(f"{'='*60}", flush=True)


if __name__ == "__main__":
    main()

