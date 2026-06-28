import argparse
import sys

from .pipelines import (
    pipeline_audit,
    pipeline_batch,
    pipeline_daily,
    pipeline_deepdive,
    pipeline_embed,
    pipeline_extract,
    pipeline_health,
    pipeline_help,
    pipeline_inbox,
    pipeline_ingest,
    pipeline_organize,
    pipeline_rename,
    pipeline_review,
    pipeline_scout,
    pipeline_search,
    pipeline_section,
    pipeline_stage,
    pipeline_staleness,
    pipeline_status,
    pipeline_sync,
    pipeline_validate,
    pipeline_wisdom,
    pipeline_writeback,
)
from .shared import StepRunner, fail


def build_parser():
    parser = argparse.ArgumentParser(
        prog="librarian.py",
        description="Wiki Link Librarian v2.0 — single entry point for all pipelines.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("command", nargs="?", default="status", help="Pipeline to run (default: status)")
    parser.add_argument("targets", nargs="*", help="Positional args for the pipeline (query, tag, file, …)")
    parser.add_argument("--skip", default="", help="Comma-separated step names to skip")
    parser.add_argument("--only", default="", help="Comma-separated step names to run exclusively")
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--deep", action="store_true")
    parser.add_argument("--semantic", action="store_true")
    parser.add_argument("--no-raw", action="store_true")
    parser.add_argument("--no-wiki", action="store_true")
    parser.add_argument("--raw-only", action="store_true")
    parser.add_argument("--no-semantic", action="store_true")
    parser.add_argument("--type", dest="filter_type", default=None)
    parser.add_argument("--min-confidence", type=int, default=0)
    parser.add_argument("--export", default=None)
    parser.add_argument("--auto-mark", action="store_true")
    parser.add_argument("--threshold", type=float, default=None)
    parser.add_argument("--no-llm", action="store_true")
    parser.add_argument("--model", default="claude-sonnet-4-6")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--n", type=int, default=None)
    parser.add_argument("--book", default=None)
    parser.add_argument("--min-depth", type=int, default=None)
    parser.add_argument("--list-coverage", action="store_true")
    parser.add_argument("--staged", action="store_true")
    parser.add_argument("--accept", default=None)
    parser.add_argument("--accept-all", action="store_true")
    parser.add_argument("--file", default=None)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--skip-existing", action="store_true")
    parser.add_argument("--mode", default=None)
    parser.add_argument("--dir", default=None)
    parser.add_argument("--heading", default=None)
    parser.add_argument("--out", default=None)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--no-move", action="store_true")
    parser.add_argument("--fix-whitespace", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--watch", action="store_true")
    parser.add_argument("--incremental", action="store_true", help="Incremental embed (only new/changed files)")
    parser.add_argument("--scan", action="store_true", help="Scan inbox files (default)")
    parser.add_argument("--process", default=None, help="Process inbox → <book|clipping> folder (manual classify)")
    parser.add_argument("--list-books", action="store_true", help="List known book folders")
    return parser


def make_runner_factory(args):
    skip_set = {item.strip() for item in args.skip.split(",") if item.strip()}
    only_set = {item.strip() for item in args.only.split(",") if item.strip()}

    def make_runner():
        return StepRunner(skip_set=skip_set, only_set=only_set)

    return make_runner


def dispatch(args):
    make_runner = make_runner_factory(args)
    cmd = args.command.lower()
    targets = args.targets

    if cmd == "status":
        pipeline_status()
    elif cmd == "sync":
        pipeline_sync(make_runner())
    elif cmd == "ingest":
        pipeline_ingest(make_runner())
    elif cmd == "health":
        pipeline_health(make_runner())
    elif cmd == "daily":
        pipeline_daily(make_runner())
    elif cmd == "wisdom":
        tag = targets[0] if targets else None
        if not tag:
            fail("wisdom: <tag> required  (e.g. python librarian.py wisdom monetary-policy)")
            sys.exit(1)
        pipeline_wisdom(make_runner(), tag, no_llm=args.no_llm, model=args.model)
    elif cmd == "audit":
        file_path = targets[0] if targets else None
        if not file_path:
            fail("audit: <file> required  (e.g. python librarian.py audit 03_wiki/mechanisms/Foo.md)")
            sys.exit(1)
        pipeline_audit(make_runner(), file_path)
    elif cmd == "search":
        query = " ".join(targets) if targets else None
        if not query:
            fail("search: <query> required  (e.g. python librarian.py search 'fiscal dominance')")
            sys.exit(1)
        pipeline_search(
            make_runner(),
            query,
            deep=args.deep,
            semantic=args.semantic,
            top=args.top,
            no_raw=args.no_raw,
            no_wiki=args.no_wiki,
            raw_only=args.raw_only,
            no_semantic=args.no_semantic,
            filter_type=args.filter_type,
            min_confidence=args.min_confidence,
            export=args.export,
        )
    elif cmd == "deepdive":
        query = " ".join(targets) if targets else None
        if not query:
            fail("deepdive: <query> required  (e.g. python librarian.py deepdive 'repo mechanics')")
            sys.exit(1)
        threshold = int(args.threshold) if args.threshold is not None else 2
        pipeline_deepdive(make_runner(), query, threshold=threshold)
    elif cmd == "rename":
        if len(targets) < 2:
            fail("rename: <old_name> <new_name> required")
            sys.exit(1)
        pipeline_rename(make_runner(), targets[0], targets[1], dry_run=args.dry_run)
    elif cmd == "staleness":
        pipeline_staleness(make_runner(), auto_mark=args.auto_mark, threshold_multiplier=args.threshold)
    elif cmd == "stage":
        pipeline_stage(make_runner(), args)
    elif cmd == "review":
        action = targets[0] if targets else None
        target = targets[1] if len(targets) > 1 else None
        pipeline_review(make_runner(), action=action, target=target)
    elif cmd == "extract":
        pipeline_extract(make_runner(), args)
    elif cmd == "scout":
        pipeline_scout(make_runner(), args)
    elif cmd == "section":
        pipeline_section(make_runner(), args)
    elif cmd in ("organize", "cleanup"):
        pipeline_organize(make_runner(), args, force_cleanup_mode=(cmd == "cleanup"))
    elif cmd == "inbox":
        pipeline_inbox(make_runner(), args)
    elif cmd == "embed":
        pipeline_embed(make_runner(), args)
    elif cmd == "validate":
        pipeline_validate(make_runner())
    elif cmd == "writeback":
        pipeline_writeback(make_runner())
    elif cmd == "batch":
        pipelines_str = targets[0] if targets else ""
        extra_target = targets[1] if len(targets) > 1 else None
        if not pipelines_str:
            fail("batch: <pipelines> required  (e.g. python librarian.py batch sync,health)")
            sys.exit(1)
        pipeline_batch(make_runner(), pipelines_str, args, extra_target=extra_target)
    elif cmd == "help":
        pipeline_help(targets[0] if targets else None)
    else:
        fail("Unknown command: '{}'.  Run: python librarian.py help".format(cmd))
        sys.exit(1)


def main():
    parser = build_parser()
    args = parser.parse_args()
    dispatch(args)
