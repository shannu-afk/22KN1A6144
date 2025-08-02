import sqlite3
from datetime import datetime, timedelta
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY,original_url TEXT,short_code TEXT UNIQUE,created_at TEXT,expiry_minutes INTEGER)"""
    )
    conn.commit()
    conn.close()
def insert_url(original_url, short_code, expiry_minutes):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO urls (original_url, short_code, created_at, expiry_minutes) VALUES (?, ?, datetime('now'), ?)",
        (original_url, short_code, expiry_minutes),
    )
    conn.commit()
    conn.close()
def get_url(short_code):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(
        "SELECT original_url, created_at, expiry_minutes FROM urls WHERE short_code = ?",
        (short_code,),
    )
    result = c.fetchone()
    conn.close()
    return result
