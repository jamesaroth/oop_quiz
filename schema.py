import sqlite3

def create_schema():
    conn = sqlite3.connect('tsla.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS stock (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Date DATE,
        Open REAL,
        High REAL,
        Low REAL,
        Close REAL,
        Adj_Close REAL,
        Volume INTEGER
    )""")

    
    c.close()

