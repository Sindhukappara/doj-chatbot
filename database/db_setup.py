import sqlite3

def create_database():
    conn = sqlite3.connect('doj_bot.db')
    c = conn.cursor()
    
    # Knowledge base table
    c.execute('''CREATE TABLE IF NOT EXISTS knowledge_base
                 (id INTEGER PRIMARY KEY, 
                  question TEXT,
                  answer TEXT,
                  category TEXT,
                  embedding BLOB)''')
    
    # Recent questions table
    c.execute('''CREATE TABLE IF NOT EXISTS recent_questions
                 (id INTEGER PRIMARY KEY,
                  query TEXT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    
    # Feedback table
    c.execute('''CREATE TABLE IF NOT EXISTS feedback
                 (id INTEGER PRIMARY KEY,
                  query_hash TEXT,
                  feedback_score INTEGER,
                  user_comments TEXT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
