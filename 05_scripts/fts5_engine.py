import sqlite3
import shutil
import tempfile
from pathlib import Path

# Resolve from script location so it works regardless of CWD
_SCRIPT_DIR = Path(__file__).parent
_WIKI_ROOT   = _SCRIPT_DIR.parent
_MOUNTED_DB  = _WIKI_ROOT / ".cache" / "wiki_index.db"
_TMP_DB = None


def _get_tmp_db():
    global _TMP_DB
    if _TMP_DB is not None and Path(_TMP_DB).exists():
        return Path(_TMP_DB)
    tmp = tempfile.mktemp(suffix=".db", prefix="wiki_work_")
    _TMP_DB = tmp
    return Path(tmp)


def setup_fts5(index_data):
    tmp_db = _get_tmp_db()

    if _MOUNTED_DB.exists() and not tmp_db.exists():
        try:
            shutil.copy2(str(_MOUNTED_DB), str(tmp_db))
        except Exception:
            pass

    conn = sqlite3.connect(str(tmp_db))
    try:
        for tbl in ("wiki_index", "wiki_fts", "wiki_fts_data", "wiki_fts_idx",
                    "wiki_fts_content", "wiki_fts_docsize", "wiki_fts_config"):
            conn.execute("DROP TABLE IF EXISTS " + tbl)

        conn.execute("""CREATE TABLE wiki_index (
            id TEXT, label TEXT, source_file TEXT, source TEXT,
            thesis TEXT, snippet TEXT, tags TEXT, aliases TEXT,
            search_text TEXT, confidence TEXT
        )""")
        conn.execute(
            "CREATE VIRTUAL TABLE wiki_fts USING fts5(label, thesis, snippet, search_text)"
        )

        rows_i = []
        rows_f = []
        for node in index_data:
            rows_i.append((
                node['id'], node['label'], node['source_file'], node['source'],
                str(node['thesis']), node['snippet'],
                str(node['tags']), str(node['aliases']),
                node['search_text'], str(node.get('confidence', '?'))
            ))
            rows_f.append((
                node['label'], str(node['thesis']),
                node['snippet'], node['search_text']
            ))

        conn.executemany("INSERT INTO wiki_index VALUES (?,?,?,?,?,?,?,?,?,?)", rows_i)
        conn.executemany(
            "INSERT INTO wiki_fts (label, thesis, snippet, search_text) VALUES (?,?,?,?)",
            rows_f
        )
        conn.commit()
    finally:
        conn.close()

    return tmp_db


def search_fts5(query):
    clean_query = query.replace(" | ", " OR ").strip()
    tmp_db = _get_tmp_db()

    if tmp_db.exists():
        db_uri = str(tmp_db)
        use_uri = False
    elif _MOUNTED_DB.exists():
        db_uri = "file:{}?mode=ro&immutable=1".format(_MOUNTED_DB)
        use_uri = True
    else:
        return []

    try:
        conn = sqlite3.connect(db_uri, uri=use_uri)
        conn.row_factory = sqlite3.Row
        sql = """SELECT wi.* FROM wiki_fts
                 JOIN wiki_index wi ON wi.rowid = wiki_fts.rowid
                 WHERE wiki_fts MATCH ? LIMIT 200"""
        results = conn.execute(sql, (clean_query,)).fetchall()
        conn.close()
        return [dict(row) for row in results]
    except Exception:
        try:
            conn = sqlite3.connect(db_uri, uri=use_uri)
            conn.row_factory = sqlite3.Row
            like = "%{}%".format(clean_query)
            results = conn.execute(
                "SELECT * FROM wiki_index WHERE search_text LIKE ? LIMIT 100",
                (like,)
            ).fetchall()
            conn.close()
            return [dict(row) for row in results]
        except Exception:
            return []
