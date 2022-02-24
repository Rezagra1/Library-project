import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    curr = conn.cursor()
    curr.execute("CREAT TALBE IF NOT EXISTS BOOK(id INTEGER )")
    conn.commit()
    conn.close()

def insert(title, author, ):
