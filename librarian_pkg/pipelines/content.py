from ..shared import fail, header, run_script
from ..steps import (
    step_build_graph,
    step_gen_index,
    step_inbox_list_books,
    step_inbox_process,
    step_inbox_scan,
)
from ..validation import process_writeback_queue


def pipeline_rename(runner, old_name, new_name, dry_run=False):
    header("PIPELINE: rename  {} -> {}".format(old_name, new_name))
    cmd_args = [old_name, new_name]
    if dry_run:
        cmd_args.append("--dry-run")

    def _rename():
        ok_, out, err = run_script("rename_node.py", cmd_args, timeout=120)
        text = out or err or ""
        for line in text.strip().splitlines()[:80]:
            print("    {}".format(line))
        return ok_, "renamed" if ok_ else (err[:80] if err else "FAILED")

    runner.step("rename_node", _rename)
    if not dry_run:
        runner.step("sync_graph", step_build_graph)
        runner.step("sync_index", step_gen_index)
    runner.summary()


def pipeline_stage(runner, args):
    header("PIPELINE: stage")
    cmd_args = []
    if args.dry_run:
        cmd_args.append("--dry-run")
    if args.n is not None:
        cmd_args += ["--n", str(args.n)]
    if args.book:
        cmd_args += ["--book", args.book]
    if args.min_depth is not None:
        cmd_args += ["--min-depth", str(args.min_depth)]
    if args.list_coverage:
        cmd_args.append("--list-coverage")
    if args.staged:
        cmd_args.append("--staged")
    if args.accept:
        cmd_args += ["--accept", args.accept]
    if args.accept_all:
        cmd_args.append("--accept-all")

    def _stage():
        ok_, out, err = run_script("auto_ingest.py", cmd_args, timeout=None)
        text = out or err or ""
        for line in text.strip().splitlines()[:120]:
            print("    {}".format(line))
        return ok_, "stage complete" if ok_ else (err[:80] if err else "FAILED")

    runner.step("auto_ingest", _stage)
    runner.summary()


def pipeline_review(runner, action=None, target=None):
    header("PIPELINE: review")
    if action == "accept-all":
        runner.step("accept_all", lambda: _review_action(["--accept-all"]))
    elif action == "accept":
        if not target:
            fail("review accept: target node required")
            return
        runner.step("accept_node", lambda: _review_action(["--accept", target]))
    else:
        runner.step("list_staged", lambda: _review_action(["--staged"]))
    runner.summary()


def _review_action(cmd_args):
    ok_, out, err = run_script("auto_ingest.py", cmd_args, timeout=None)
    text = out or err or ""
    for line in text.strip().splitlines()[:120]:
        print("    {}".format(line))
    return ok_, "review complete" if ok_ else (err[:80] if err else "FAILED")


def pipeline_extract(runner, args):
    header("PIPELINE: extract")
    cmd_args = []
    if args.book:
        cmd_args += ["--book", args.book]
    if args.file:
        cmd_args += ["--file", args.file]
    if args.all:
        cmd_args.append("--all")
    if args.skip_existing:
        cmd_args.append("--skip-existing")
    if args.dry_run:
        cmd_args.append("--dry-run")

    def _extract():
        ok_, out, err = run_script("extract_pdf.py", cmd_args, timeout=None)
        text = out or err or ""
        for line in text.strip().splitlines()[:120]:
            print("    {}".format(line))
        return ok_, "extract complete" if ok_ else (err[:80] if err else "FAILED")

    runner.step("extract_pdf", _extract)
    runner.summary()


def pipeline_organize(runner, args, force_cleanup_mode=False):
    header("PIPELINE: {}".format("cleanup" if force_cleanup_mode else "organize"))
    cmd_args = []
    if args.dir:
        cmd_args += ["--dir", args.dir]
    fix_ws = args.fix_whitespace or force_cleanup_mode
    no_move = args.no_move or force_cleanup_mode
    if args.apply and not args.dry_run:
        cmd_args.append("--apply")
    if no_move:
        cmd_args.append("--no-move")
    if fix_ws:
        cmd_args.append("--fix-whitespace")
    if args.limit is not None:
        cmd_args += ["--limit", str(args.limit)]

    def _organize():
        ok_, out, err = run_script("organize_nodes.py", cmd_args, timeout=120)
        text = out or err or ""
        for line in text.strip().splitlines()[:120]:
            print("    {}".format(line))
        return ok_, "OK" if ok_ else (err[:80] if err else "FAILED")

    runner.step("organize_nodes", _organize)
    if args.apply and not args.dry_run:
        runner.step("sync_graph", step_build_graph)
        runner.step("sync_index", step_gen_index)
    runner.summary()


def pipeline_inbox(runner, args):
    header("PIPELINE: inbox")
    if args.list_books:
        runner.step("list_books", step_inbox_list_books)
        runner.summary()
        return
    if args.process:
        runner.step("process", lambda: step_inbox_process(target_book=args.process))
        runner.step("sync_graph", step_build_graph)
        runner.step("sync_index", step_gen_index)
        runner.summary()
        return
    runner.step("scan_inbox", step_inbox_scan)
    runner.summary()


def pipeline_writeback(runner):
    header("PIPELINE: writeback")
    runner.step("process_queue", lambda: _writeback_queue())
    runner.step("sync_graph", step_build_graph)
    runner.step("sync_index", step_gen_index)
    runner.summary()


def _writeback_queue():
    ok_, applied = process_writeback_queue()
    return ok_, "{} nodes updated".format(applied)
