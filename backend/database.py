import sqlite3
import os

# Get absolute path to this file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "alerts.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            camera_id TEXT,
            gesture TEXT,
            image TEXT,
            time TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_alert(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO alerts (camera_id, gesture, image, time)
        VALUES (?, ?, ?, ?)
    """, (data['camera_id'], data['gesture'], data['image'], data['time']))
    conn.commit()
    conn.close()

def get_alerts():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM alerts ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows