
import sqlite3
import os

# The database file will be stored inside this same folder
DB_PATH = os.path.join(os.path.dirname(__file__), "students.db")

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # rows behave like dictionaries
    return conn

def init_db():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                idno   TEXT PRIMARY KEY,
                name   TEXT NOT NULL,
                course TEXT NOT NULL,
                level  INTEGER NOT NULL
            );
        """)
        conn.commit()

# Ensure table exists on import
init_db()

# -------- Public helpers used by app.py --------

def getall(tablename):
    if tablename != "students":
        return []
    with connect() as conn:
        cur = conn.execute(
            "SELECT idno, name, course, level FROM students ORDER BY name COLLATE NOCASE;"
        )
        return [dict(row) for row in cur.fetchall()]

def get_by_id(tablename, idno):
    if tablename != "students":
        return None
    with connect() as conn:
        cur = conn.execute(
            "SELECT idno, name, course, level FROM students WHERE idno = ?;",
            (idno,)
        )
        row = cur.fetchone()
        return dict(row) if row else None

def addrecord(tablename, **kwargs):
    if tablename != "students":
        return False
    try:
        with connect() as conn:
            conn.execute(
                "INSERT INTO students (idno, name, course, level) VALUES (?, ?, ?, ?);",
                (
                    kwargs["idno"],
                    kwargs["name"],
                    kwargs["course"],
                    int(kwargs["level"]),
                )
            )
            conn.commit()
        return True
    except Exception:
        return False

def updaterecord(tablename, **kwargs):
    if tablename != "students":
        return False
    try:
        with connect() as conn:
            cur = conn.execute(
                "UPDATE students SET name = ?, course = ?, level = ? WHERE idno = ?;",
                (
                    kwargs["name"],
                    kwargs["course"],
                    int(kwargs["level"]),
                    kwargs["idno"],
                )
            )
            conn.commit()
            return cur.rowcount > 0
    except Exception:
        return False

def deleterecord(tablename, idno):
    if tablename != "students":
        return False
    try:
        with connect() as conn:
            cur = conn.execute("DELETE FROM students WHERE idno = ?;", (idno,))
            conn.commit()
            return cur.rowcount > 0
    except Exception:
        return False

