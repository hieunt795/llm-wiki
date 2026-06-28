import io
import subprocess
import sys
from pathlib import Path


def bootstrap_stdout():
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


bootstrap_stdout()


WIKI_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = WIKI_ROOT / "05_scripts"
WIKI_DIR = WIKI_ROOT / "03_wiki"
OUTPUT_DIR = WIKI_ROOT / "04_outputs" / "research"
STAGED_DIR = WIKI_ROOT / "04_outputs" / "staged_nodes"
HOT_MD = WIKI_ROOT / "01_schema" / "hot.md"
MEMORY_MD = WIKI_ROOT / "01_schema" / "memory.md"

GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def ok(msg):
    print("  {}[OK]{} {}".format(GREEN, RESET, msg))


def skip(msg):
    print("  {}[SKIP]{} {}".format(YELLOW, RESET, msg))


def fail(msg):
    print("  {}[FAIL]{} {}".format(RED, RESET, msg))


def info(msg):
    print("  {}[INFO]{} {}".format(CYAN, RESET, msg))


def header(msg):
    print("\n{}{}{}".format(BOLD, msg, RESET))


def run_script(script_name, args=None, timeout=120):
    script_path = SCRIPTS_DIR / script_name
    if not script_path.exists():
        return False, "", "Script not found: {}".format(script_path)
    cmd = [sys.executable, str(script_path)] + (args or [])
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
            cwd=str(WIKI_ROOT),
        )
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return False, "", "Timeout after {}s".format(timeout)
    except Exception as exc:
        return False, "", str(exc)


class StepRunner:
    def __init__(self, skip_set=None, only_set=None):
        self.skip_set = skip_set or set()
        self.only_set = only_set or set()
        self.results = []

    def should_run(self, name):
        if name in self.skip_set:
            return False
        if self.only_set and name not in self.only_set:
            return False
        return True

    def step(self, name, fn):
        if not self.should_run(name):
            skip(name)
            self.results.append((name, "SKIP", ""))
            return True

        print("  [ .. ] {}".format(name), end="\r")
        try:
            success, msg = fn()
        except Exception as exc:
            success, msg = False, str(exc)

        if success:
            ok("{:<35} {}".format(name, msg))
            self.results.append((name, "OK", msg))
        else:
            fail("{:<35} {}".format(name, msg))
            self.results.append((name, "FAIL", msg))
        return success

    def summary(self):
        total = len(self.results)
        n_ok = sum(1 for _, status, _ in self.results if status == "OK")
        n_skip = sum(1 for _, status, _ in self.results if status == "SKIP")
        n_fail = sum(1 for _, status, _ in self.results if status == "FAIL")
        print(
            "\n  ─── Summary: {}/{} OK | {} skipped | {} failed ───".format(
                n_ok,
                total - n_skip,
                n_skip,
                n_fail,
            )
        )
