
import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.db_name = 'notes.db'
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

    def create_note(self, content):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO notes (content) VALUES (?)', (content,))
            return {'id': cursor.lastrowid, 'content': content}

    def get_all_notes(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM notes ORDER BY created_at DESC')
            return [dict(row) for row in cursor.fetchall()]

    def get_note(self, note_id):
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM notes WHERE id = ?', (note_id,))
            return dict(cursor.fetchone())

    def delete_note(self, note_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
            return {'success': True}