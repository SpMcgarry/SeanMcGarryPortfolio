# backend/database.py

import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('sigmintdata.db.sql')  # Connect to your database
        self.cursor = self.conn.cursor()

    def get_comic_books(self):
        # Implement logic to fetch comic books from the database
        self.cursor.execute('SELECT * FROM ComicBooks')
        comic_books = self.cursor.fetchall()
        return comic_books

    # Implement other CRUD methods as needed

    def __del__(self):
        self.conn.close()
