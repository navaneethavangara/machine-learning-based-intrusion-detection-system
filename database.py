import sqlite3
from datetime import datetime
import random

def init_db():
    conn = sqlite3.connect("ids.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time TEXT,
        ip TEXT,
        prediction TEXT,
        confidence REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_log():
    conn = sqlite3.connect("ids.db")
    cursor = conn.cursor()

    ip = f"192.168.0.{random.randint(1,255)}"
    prediction = random.choice(["Normal","Attack"])
    confidence = round(random.uniform(80,99),2)
    time = datetime.now().strftime("%H:%M:%S")

    cursor.execute("""
    INSERT INTO logs(time,ip,prediction,confidence)
    VALUES(?,?,?,?)
    """,(time,ip,prediction,confidence))

    conn.commit()
    conn.close()


def get_logs():
    conn = sqlite3.connect("ids.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 25")
    rows = cursor.fetchall()
    conn.close()
    return rows