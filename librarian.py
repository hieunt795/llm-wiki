#!/usr/bin/env python3
"""
librarian.py — Wiki Link Librarian (v2.0)
Thin CLI entrypoint. Internal implementation now lives in `librarian_pkg/`.
"""

from librarian_pkg.cli import main


if __name__ == "__main__":
    main()
