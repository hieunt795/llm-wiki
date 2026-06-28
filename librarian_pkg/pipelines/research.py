from ..help_data import PIPELINE_HELP
from ..shared import BOLD, DIM, RESET, StepRunner, fail, header, run_script
from ..steps import step_claim_audit, step_embed_build, step_embed_stats, step_staleness
from .content import pipeline_organize, pipeline_review
from .maintenance import (
    pipeline_daily,
    pipeline_health,
    pipeline_ingest,
    pipeline_staleness,
    pipeline_sync,
    pipeline_validate,
)
from .content import pipeline_writeback


def pipeline_wisdom(runner, tag, no_llm=False, model="claude-sonnet-4-6"):
    header("PIPELINE: wisdom [{}]".format(tag))
    runner.step("staleness_check", lambda: step_staleness(tag=tag))

    cmd_args = [tag]
    if no_llm:
        cmd_args.append("--no-llm")
    else:
        cmd_args += ["--model", model]

    def _wisdom():
        ok_, out, err = run_script("auto_synthesis.py", cmd_args, timeout=None)
        text = out or err or ""
        for line in text.strip().splitlines()[:60]:
            print("    {}".format(line))
        return ok_, "report generated" if ok_ else (err[:80] if err else "FAILED")

    runner.step("auto_synthesis", _wisdom)
    runner.summary()


def pipeline_audit(runner, file_path):
    header("PIPELINE: audit")
    runner.step("claim_audit", lambda: step_claim_audit(file_path))
    runner.summary()


def pipeline_search(
    runner,
    query,
    deep=False,
    semantic=False,
    top=8,
    no_raw=False,
    no_wiki=False,
    raw_only=False,
    no_semantic=False,
    filter_type=None,
    min_confidence=0,
    export=None,
):
    mode = "[DEEP]" if deep else ("[SEMANTIC]" if semantic else "")
    header("PIPELINE: search {}  {}".format(mode, query))

    cmd_args = [query, "--top", str(top)]
    if deep:
        script_name = "deepdive_search.py"
        if raw_only:
            cmd_args.append("--raw-only")
        if no_raw:
            cmd_args.append("--no-raw")
        if no_wiki:
            cmd_args.append("--no-wiki")
        if no_semantic:
            cmd_args.append("--no-semantic")
    else:
        script_name = "wiki_search.py"
        if semantic:
            cmd_args.append("--semantic")
        if no_raw:
            cmd_args.append("--no-raw")
        if no_wiki:
            cmd_args.append("--no-wiki")
        if raw_only:
            cmd_args.append("--raw-only")
        if filter_type:
            cmd_args += ["--type", filter_type]
        if min_confidence:
            cmd_args += ["--min-confidence", str(min_confidence)]
        if export:
            cmd_args += ["--export", export]

    def _search():
        ok_, out, err = run_script(script_name, cmd_args, timeout=120)
        text = out or err or ""
        for line in text.strip().splitlines()[:120]:
            print("    {}".format(line))
        return ok_, "results shown" if ok_ else (err[:80] if err else "FAILED")

    runner.step("search", _search)
    runner.summary()


def pipeline_deepdive(runner, query, threshold=2):
    header("PIPELINE: deepdive  {}".format(query))
    cmd_args = [query, "--threshold", str(threshold)]

    def _deepdive():
        ok_, out, err = run_script("deepdive_search.py", cmd_args, timeout=180)
        text = out or err or ""
        for line in text.strip().splitlines()[:120]:
            print("    {}".format(line))
        return ok_, "draft generated" if ok_ else (err[:80] if err else "FAILED")

    runner.step("detect_drill_draft", _deepdive)
    runner.summary()


def pipeline_scout(runner, args):
    header("PIPELINE: scout")
    cmd_args = []
    if args.mode:
        cmd_args += ["--mode", args.mode]
    if args.n is not None:
        cmd_args += ["--n", str(args.n)]

    def _scout():
        ok_, out, err = run_script("raw_scout.py", cmd_args, timeout=90)
        text = out or err or ""
        for line in text.strip().splitlines()[:80]:
            print("    {}".format(line))
        return ok_, "scout complete" if ok_ else (err[:80] if err else "FAILED")

    runner.step("raw_scout", _scout)
    runner.summary()


def pipeline_section(runner, args):
    header("PIPELINE: section")
    cmd_args = ["--dir", args.dir, "--heading", args.heading, "--out", args.out]

    def _section():
        ok_, out, err = run_script("exact_extractor.py", cmd_args, timeout=90)
        text = out or err or ""
        for line in text.strip().splitlines()[:40]:
            print("    {}".format(line))
        return ok_, "OK" if ok_ else (err[:80] if err else "FAILED")

    runner.step("exact_extractor", _section)
    runner.summary()


def pipeline_embed(runner, args):
    mode = "[INCREMENTAL]" if args.incremental else ""
    header("PIPELINE: embed {}".format(mode))
    if args.stats:
        runner.step("embed_stats", step_embed_stats)
        runner.summary()
        return
    if args.watch:
        runner.step("embed_build", lambda: step_embed_build(incremental=args.incremental))
        runner.summary()
        print("\n  [INFO] Entering watch mode (Ctrl+C to stop)...")
        try:
            run_script("embed_index.py", ["--watch"], timeout=None)
        except KeyboardInterrupt:
            print("\n  [INFO] Watch stopped.")
        return
    runner.step("embed_build", lambda: step_embed_build(incremental=args.incremental))
    runner.summary()


def pipeline_batch(runner, pipelines_str, args, extra_target=None):
    names = [name.strip() for name in pipelines_str.split(",") if name.strip()]
    header("PIPELINE: batch [{}]".format(" → ".join(names)))
    simple = {
        "sync": lambda: pipeline_sync(StepRunner()),
        "ingest": lambda: pipeline_ingest(StepRunner()),
        "health": lambda: pipeline_health(StepRunner()),
        "daily": lambda: pipeline_daily(StepRunner()),
        "staleness": lambda: pipeline_staleness(StepRunner()),
        "review": lambda: pipeline_review(StepRunner()),
        "validate": lambda: pipeline_validate(StepRunner()),
        "writeback": lambda: pipeline_writeback(StepRunner()),
    }
    for name in names:
        print()
        if name in simple:
            simple[name]()
        elif name == "wisdom":
            if not extra_target:
                fail("batch wisdom: tag required (e.g. batch daily,wisdom monetary-policy)")
                continue
            pipeline_wisdom(StepRunner(), extra_target, no_llm=args.no_llm, model=args.model)
        elif name == "deepdive":
            if not extra_target:
                fail("batch deepdive: query required")
                continue
            threshold = int(args.threshold) if args.threshold is not None else 2
            pipeline_deepdive(StepRunner(), extra_target, threshold=threshold)
        elif name == "embed":
            pipeline_embed(StepRunner(), args)
        elif name in ("organize", "cleanup"):
            pipeline_organize(StepRunner(), args, force_cleanup_mode=(name == "cleanup"))
        else:
            fail("batch: unknown pipeline '{}'".format(name))
    print("\n{}batch done: [{}]{}".format(BOLD, " → ".join(names), RESET))


def pipeline_help(target=None):
    if target and target in PIPELINE_HELP:
        item = PIPELINE_HELP[target]
        header("HELP: {}".format(target.upper()))
        print("\n  {}Description:{} {}".format(BOLD, RESET, item["desc"]))
        print("  {}When to use:{} {}".format(BOLD, RESET, item["when"]))
        print("\n  {}Steps:{}".format(BOLD, RESET))
        for step_name, step_desc in item["steps"]:
            print("    {:22s} {}".format(step_name, step_desc))
        print("\n  {}Examples:{}".format(BOLD, RESET))
        for example in item["examples"]:
            print("    {}".format(example))
        print()
        return

    header("LIBRARIAN v2.0 — Pipeline Reference")
    print()
    all_pipes = [
        "status", "inbox", "sync", "ingest", "health", "daily",
        "wisdom", "audit", "search", "deepdive",
        "rename", "staleness", "stage", "review",
        "extract", "scout", "section", "organize", "cleanup", "batch",
    ]
    for name in all_pipes:
        item = PIPELINE_HELP.get(name)
        if not item:
            continue
        print("  {}{:<10s}{}  {}".format(BOLD, name, RESET, item["desc"]))
        for example in item.get("examples", [])[:1]:
            print("              {}{}{}".format(DIM, example, RESET))
        print()
    print("  Tip: python librarian.py help <pipeline>  → chi tiết từng pipeline")
    print()
