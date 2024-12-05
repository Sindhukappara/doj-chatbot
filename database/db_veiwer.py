import sqlite3
import pandas as pd

def view_database_contents():
    conn = sqlite3.connect('doj_bot.db')
    
    # View knowledge base
    kb_df = pd.read_sql_query("SELECT id, question, answer, category FROM knowledge_base", conn)
    print("\nKnowledge Base:")
    print(kb_df)
    
    # View recent questions
    recent_df = pd.read_sql_query("""
        SELECT * FROM recent_questions 
        ORDER BY timestamp DESC LIMIT 10
    """, conn)
    print("\nRecent Questions:")
    print(recent_df)
    
    # View feedback statistics
    feedback_df = pd.read_sql_query("""
        SELECT query_hash, 
               AVG(feedback_score) as avg_score,
               COUNT(*) as feedback_count
        FROM feedback 
        GROUP BY query_hash
    """, conn)
    print("\nFeedback Statistics:")
    print(feedback_df)
    
    conn.close()
