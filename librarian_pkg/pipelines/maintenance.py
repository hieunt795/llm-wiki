from ..shared import GREEN, RED, RESET, SCRIPTS_DIR, WIKI_ROOT, YELLOW, header, info
from ..steps import (
    count_orphans,
    count_staged,
    count_stale_status,
    step_auto_bridge,
    step_build_graph,
    step_find_orphans,
    step_gen_index,
    step_missing_thesis,
    step_staleness,
    step_suggest_ideas,
    step_sync_registry,
)
from ..validation import validate_broken_wikilinks, validate_frontmatter_vs_schema, validate_orphan_refs


def pipeline_sync(runner):
    header("PIPELINE: sync")
    runner.step("build_graph", step_build_graph)
    runner.step("gen_index", step_gen_index)
    runner.step("sync_registry", step_sync_registry)
    runner.step("staleness", step_staleness)
    runner.summary()


def pipeline_ingest(runner):
    header("PIPELINE: ingest (post-ingest sync)")
    info("Run Phase A-C manually first (exact_extractor -> wiki audit -> SPAWN/EXPAND)")
    runner.step("build_graph", step_build_graph)
    runner.step("gen_index", step_gen_index)
    runner.step("auto_bridge", lambda: step_auto_bridge(dry_run=False))
    runner.step("staleness", step_staleness)
    runner.summary()


def pipeline_health(runner):
    header("PIPELINE: health")
    runner.step("find_orphans", step_find_orphans)
    runner.step("missing_thesis", step_missing_thesis)
    runner.step("staleness", step_staleness)
    runner.step("suggest_ideas", step_suggest_ideas)
    runner.summary()


def pipeline_daily(runner):
    header("PIPELINE: daily")
    runner.step("suggest_ideas", step_suggest_ideas)
    runner.step("find_orphans", step_find_orphans)
    runner.step("staleness", step_staleness)
    runner.step("missing_thesis", step_missing_thesis)
    runner.summary()


def pipeline_staleness(runner, auto_mark=False, threshold_multiplier=None):
    from ..shared import run_script

    header("PIPELINE: staleness")
    cmd_args = ["--check"]
    if auto_mark:
        cmd_args = ["--mark-stale"]
    if threshold_multiplier is not None:
        cmd_args += ["--threshold", str(threshold_multiplier)]

    def _run():
        ok_, out, err = run_script("auto_synthesis.py", cmd_args, timeout=None)
        text = out or err or ""
        for line in text.strip().splitlines()[:80]:
            print("    {}".format(line))
        return ok_, "done" if ok_ else (err[:80] if err else "FAILED")

    runner.step("staleness_scan", _run)
    runner.summary()


def pipeline_validate(runner):
    header("PIPELINE: validate")

    def _validate_frontmatter():
        ok_, issues = validate_frontmatter_vs_schema()
        for issue in issues[:10]:
            print("    {}".format(issue))
        if len(issues) > 10:
            print("    ... {} more issues".format(len(issues) - 10))
        return ok_, "0 issues" if ok_ else "{} issues found".format(len(issues))

    def _validate_wikilinks():
        ok_, broken = validate_broken_wikilinks()
        for item in broken[:10]:
            print("    {}".format(item))
        if len(broken) > 10:
            print("    ... {} more broken links".format(len(broken) - 10))
        return ok_, "OK" if ok_ else "{} broken links".format(len(broken))

    def _validate_orphan_refs():
        ok_, orphans = validate_orphan_refs()
        for item in orphans[:10]:
            print("    {}".format(item))
        if len(orphans) > 10:
            print("    ... {} more orphan refs".format(len(orphans) - 10))
        return ok_, "OK" if ok_ else "{} orphan refs".format(len(orphans))

    runner.step("schema_check", _validate_frontmatter)
    runner.step("wikilink_check", _validate_wikilinks)
    runner.step("orphan_ref_check", _validate_orphan_refs)
    runner.summary()


def pipeline_status():
    header("WIKI LINK — System Status  (librarian v2.0)")
    wiki_dir = WIKI_ROOT / "03_wiki"
    reports_dir = WIKI_ROOT / "04_outputs" / "research"
    node_count = len(list(wiki_dir.rglob("*.md"))) if wiki_dir.exists() else 0
    script_count = len(list(SCRIPTS_DIR.rglob("*.py"))) if SCRIPTS_DIR.exists() else 0
    report_count = len(list(reports_dir.glob("*.md"))) if reports_dir.exists() else 0
    staged_count = count_staged()
    stale_count = count_stale_status()
    orphan_count = count_orphans()

    print()
    print("  Wiki nodes      : {}".format(node_count))
    print("  Scripts         : {}".format(script_count))
    print("  Wisdom reports  : {}".format(report_count))
    print("  Staged (pending): {}{}{}".format(YELLOW if staged_count else GREEN, staged_count, RESET))
    print("  Status=stale    : {}{}{}".format(YELLOW if stale_count else GREEN, stale_count, RESET))
    print("  Orphans         : {}{}{}".format(RED if orphan_count else GREEN, orphan_count, RESET))
    print()
