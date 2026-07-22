
import sqlite3

conn = sqlite3.connect("ids.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input_features TEXT,
    result TEXT
)
""")

conn.commit()
conn.close()

print("Database initialized successfully")
