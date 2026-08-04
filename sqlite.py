from fastapi import FastAPI
import sqlite3

conn = sqlite3.connect('test.db',check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS todos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             age INTEGER NOT NULL,
             completed BOOLEAN NOT NULL,
             password TEXT NOT NULL)''')

conn.commit()

app = FastAPI()

@app.get("/todos")
def get_todos():
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    return {"todos": todos}

