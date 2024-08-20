import sqlite3
from datetime import datetime

def create_connection(db_file):
    """ Skapa en databasanslutning till SQLite-databasen """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    
    return conn

def create_table():
    """ Skapa en tabell för läxor om den inte redan finns """
    conn = create_connection("classroom.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS homework (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          assignment TEXT NOT NULL,
                          due_date TEXT NOT NULL);''')
        conn.commit()

def add_homework(assignment, due_date):
    """ Lägg till en ny läxa i databasen på ett säkert sätt """
    conn = create_connection("classroom.db")
    with conn:
        cursor = conn.cursor()
        # Använd parametrar (?) för att skydda mot SQL-injektion
        cursor.execute("INSERT INTO homework (assignment, due_date) VALUES (?, ?)", (assignment, due_date))
        conn.commit()

