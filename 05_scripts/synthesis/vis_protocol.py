"""
vis_protocol.py — Verified Institutional Search Protocol (v1.0)
Usage:
  python vis_protocol.py --query "CPI inflation 2025" --time 2025
  python vis_protocol.py --query "CAR bank vietnam" --source bis.org
  python vis_protocol.py --validate "https://example.com/report.pdf"
"""
import sys
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf-8-sig"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
import argparse
import re
from pathlib import Path
from urllib.parse import urlparse

SCRIPT_DIR = Path(__file__).parent
WIKI_ROOT = SCRIPT_DIR.parent.parent

def parse_args():
    parser = argparse.ArgumentParser(description="VIS Protocol - Verified Institutional Search")
    parser.add_argument("--query", "-q", help="Search query")
    parser.add_argument("--time", "-t", help="Timeframe (e.g., 2024, Q1 2025)")
    parser.add_argument("--source", "-s", help="Source domain (e.g., bis.org, imf.org)")
    parser.add_argument("--filetype", "-f", default="pdf", help="File type (pdf, html)")
    parser.add_argument("--validate", "-v", help="Validate URL accessibility")
    parser.add_argument("--example", "-e", action="store_true", help="Show query examples")
    return parser.parse_args()

def show_examples():
    examples = """
============================================================
VIS PROTOCOL QUERY EXAMPLES
============================================================

[1] Restricted Search (Layer 1)]
  site:bis.org "inflation" filetype:pdf
  site:imf.org "working paper" 2024 filetype:pdf
  site:fed.gov "monetary policy" filetype:pdf

[2] Institutional Focus]
  bis.org "car 2025" filetype:pdf
  imf.org "vn economy" filetype:pdf
  ecb.europa.eu "interest rate" filetype:pdf

[3] Time-Bound]
  "2024" site:imf.org "outlook" filetype:pdf
  "Q1 2025" site:bis.org "ctd" filetype:pdf

[4] Combined Pattern]
  site:bis.org "private credit" 2025 filetype:pdf
  site:imf.org "fiscal deficit" 2024 filetype:pdf

============================================================
"""
    print(examples)

def build_query(query, time=None, source=None, filetype="pdf"):
    """Build VIS-compliant search query"""
    queries = []
    
    # Base query
    q = f'"{query}"'
    if time:
        q += f' {time}'
    if source:
        q = f'site:{source} {q}'
    if filetype:
        q += f' filetype:{filetype}'
    
    return q

def validate_url(url):
    """Validate URL using web_fetch-like check (Layer 2)"""
    import urllib.request
    import urllib.error
    
    parsed = urlparse(url)
    if not parsed.scheme:
        url = "https://" + url
    
    print(f"Validating: {url}")
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'WikiLink-Bot/1.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.status
            content_type = response.headers.get('Content-Type', '')
            print(f"Status: {status}")
            print(f"Type: {content_type}")
            if status == 200:
                print("[OK] URL is accessible")
                return True
    except urllib.error.HTTPError as e:
        print(f"[ERROR] HTTP {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        print(f"[ERROR] {e.reason}")
    except Exception as e:
        print(f"[ERROR] {e}")
    
    return False

def main():
    args = parse_args()
    
    if args.example:
        show_examples()
        return
    
    if args.validate:
        validate_url(args.validate)
        return
    
    if args.query:
        q = build_query(args.query, args.time, args.source, args.filetype)
        print("\n=== VIS PROTOCOL SEARCH ===")
        print(f"Query: {q}\n")
        print("Copy and paste the query above into:")
        print("  - Google Search, or")
        print("  - Use: python -m websearch --query \"" + q + "\"")
    else:
        show_examples()

if __name__ == "__main__":
    main()
