import sqlite3

# Initializes the database
def initialize_db():
    try:
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
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

# Adds the score and name to the database
def add_score(name, score):
    try:
        conn = sqlite3.connect("leaderboard.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (name, score))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error adding score: {e}")

# Shows the top 10 scores within the Leaderboard
def get_top_scores(limit=10):
    try:
        conn = sqlite3.connect("leaderboard.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT ?", (limit,))
        top_scores = cursor.fetchall()
        conn.close()
        return top_scores
    except sqlite3.Error as e:
        print(f"Error fetching top scores: {e}")
        return []

# Reset the leaderboard (if needed)
def reset_leaderboard():
    try:
        conn = sqlite3.connect("leaderboard.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM leaderboard")  # Correct query
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Error resetting leaderboard: {e}")

# Initialize database when script runs
initialize_db()
