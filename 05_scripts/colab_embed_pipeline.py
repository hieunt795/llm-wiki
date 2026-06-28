# -*- coding: utf-8 -*-
"""
colab_embed_pipeline.py — One-file Colab embedding pipeline for Wiki Link
==========================================================================
Chạy trên Google Colab để:
1. cài dependency cần thiết
2. build full embedding index bằng BGE-M3
3. zip artifact .cache/wiki_embed.*
4. tải zip về local hoặc copy sang Google Drive

USAGE (trong Colab, sau khi clone repo):
  %cd /content/WikiLink
  !python 05_scripts/colab_embed_pipeline.py

Tùy chọn:
  !python 05_scripts/colab_embed_pipeline.py --skip-install
  !python 05_scripts/colab_embed_pipeline.py --zip-name my_embed.zip
  !python 05_scripts/colab_embed_pipeline.py --drive-dir /content/drive/MyDrive/WikiLink_index
  !python 05_scripts/colab_embed_pipeline.py --no-download
"""

import argparse
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
WIKI_ROOT = SCRIPT_DIR.parent
CACHE_DIR = WIKI_ROOT / ".cache"
ARTIFACT_FILES = [
    CACHE_DIR / "wiki_embed.index",
    CACHE_DIR / "wiki_embed.meta.json",
    CACHE_DIR / "wiki_embed.manifest.json",
]


def _run(cmd: list[str], cwd: Path | None = None) -> None:
    print(f"[colab_embed] RUN: {' '.join(cmd)}", flush=True)
    subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=True)


def _in_colab() -> bool:
    try:
        import google.colab  # type: ignore
        return True
    except Exception:
        return False


def install_dependencies() -> None:
    _run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-q",
            "sentence-transformers",
            "faiss-cpu",
        ]
    )


def build_embedding() -> None:
    _run([sys.executable, "05_scripts/embed_index.py", "--build"], cwd=WIKI_ROOT)


def verify_artifacts() -> None:
    missing = [str(path.name) for path in ARTIFACT_FILES if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing embedding artifacts after build: {', '.join(missing)}")


def create_zip(zip_name: str) -> Path:
    zip_path = WIKI_ROOT / zip_name
    if zip_path.exists():
        zip_path.unlink()

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in ARTIFACT_FILES:
            zf.write(path, arcname=path.name)

    size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"[colab_embed] ZIP ready: {zip_path} ({size_mb:.1f} MB)", flush=True)
    return zip_path


def copy_to_drive(zip_path: Path, drive_dir: str) -> None:
    target_dir = Path(drive_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / zip_path.name
    shutil.copy2(zip_path, target_path)
    print(f"[colab_embed] Copied to Drive: {target_path}", flush=True)


def download_zip(zip_path: Path) -> None:
    if not _in_colab():
        print(f"[colab_embed] Not in Colab, skip browser download. File at: {zip_path}", flush=True)
        return

    from google.colab import files  # type: ignore

    print(f"[colab_embed] Starting browser download: {zip_path.name}", flush=True)
    files.download(str(zip_path))


def print_next_steps(zip_name: str) -> None:
    print("", flush=True)
    print("[colab_embed] Next step on local Windows:", flush=True)
    print(
        f"  powershell -ExecutionPolicy Bypass -File 05_scripts\\pull_embed_index.ps1 -Zip "
        f"\"%USERPROFILE%\\Downloads\\{zip_name}\"",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="One-file Colab pipeline for Wiki Link embedding artifacts"
    )
    parser.add_argument("--skip-install", action="store_true", help="Skip pip install step")
    parser.add_argument(
        "--zip-name",
        default="wiki_embed_artifacts.zip",
        help="Output zip filename (default: wiki_embed_artifacts.zip)",
    )
    parser.add_argument(
        "--drive-dir",
        default="",
        help="Optional Google Drive folder to copy artifact zip into",
    )
    parser.add_argument(
        "--no-download",
        action="store_true",
        help="Do not trigger browser download at the end",
    )
    args = parser.parse_args()

    print(f"[colab_embed] Repo root: {WIKI_ROOT}", flush=True)
    print("[colab_embed] Engine: BAAI/bge-m3", flush=True)

    if not args.skip_install:
        install_dependencies()

    build_embedding()
    verify_artifacts()
    zip_path = create_zip(args.zip_name)

    if args.drive_dir:
        copy_to_drive(zip_path, args.drive_dir)

    if not args.no_download:
        download_zip(zip_path)

    print_next_steps(args.zip_name)


if __name__ == "__main__":
    main()
