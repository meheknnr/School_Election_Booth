import sqlite3

DATABASE = "election.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Students Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT UNIQUE,
        name TEXT,
        grade TEXT,
        password TEXT,
        voted INTEGER DEFAULT 0
    )
    """)

    # Candidates Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        grade TEXT,
        symbol TEXT,
        votes INTEGER DEFAULT 0
    )
    """)

    # Votes Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS votes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        candidate_id INTEGER
    )
    """)

    # Admin Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

def create_default_admin():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM admin")

    if cursor.fetchone() is None:
        cursor.execute("""
        INSERT INTO admin(username,password)
        VALUES('admin','admin123')
        """)

    conn.commit()
    conn.close()

def add_sample_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")

    if cursor.fetchone()[0] == 0:

        for i in range(1,201):

            grade=((i-1)//20)+1

            cursor.execute("""
            INSERT INTO students(student_id,name,grade,password)
            VALUES(?,?,?,?)
            """,
            (
                f"STU{i:03}",
                f"Student {i}",
                f"Grade {grade}",
                "1234"
            ))

    conn.commit()
    conn.close()

def add_sample_candidates():

    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM candidates")

    if cursor.fetchone()[0]==0:

        candidates=[
            ("Ayaan","Grade 10","⭐"),
            ("Fatima","Grade 9","🌹"),
            ("Rahul","Grade 10","🦁"),
            ("Ayesha","Grade 8","🪔"),
            ("Arjun","Grade 9","🌳")
        ]

        cursor.executemany("""
        INSERT INTO candidates(name,grade,symbol)
        VALUES(?,?,?)
        """,candidates)

    conn.commit()
    conn.close()
