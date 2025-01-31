import sqlite3
# Initializes the database

def initialize_db():
    conn = sqlite3.connect("leaderboard.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
# Adds the score and name to the database
def add_score(name, score):
    conn = sqlite3.connect("leaderboard.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()
# Shows the top 10 scores within the Leaderboard
def get_top_scores(limit=10):
    conn = sqlite3.connect("leaderboard.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT ?", (limit,))
    top_scores = cursor.fetchall()
    conn.close()
    return top_scores
#  Deleting a record from the Database
def reset_leaderboard():
    conn = sqlite3.connect("leaderboard.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM leaderboard WHERE score = 7")
    conn.commit()
    conn.close()
# Initialize database when script runs
initialize_db()