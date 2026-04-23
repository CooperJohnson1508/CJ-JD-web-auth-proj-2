import sqlite3

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# def get_entries_db():
#     conn = sqlite3.connect("player_data.db")
#     conn.row_factory = sqlite3.Row
#     return conn

def init_db():
    conn = get_db()
    # e_conn = get_entries_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS player_data (
            username TEXT PRIMARY KEY,
            pet_type TEXT,
            pet_name TEXT,
            pets INT
            )
        """)
    conn.commit()
    conn.close()