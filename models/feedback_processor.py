import sqlite3
from datetime import datetime

class FeedbackProcessor:
    def __init__(self):
        self.conn = sqlite3.connect('doj_bot.db')
        
    def process_feedback(self, query, score):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO feedback (query_hash, feedback_score)
            VALUES (?, ?)
        """, (hash(query), score))
        self.conn.commit()
