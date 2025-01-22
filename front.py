from flask import Flask,render_template
from main import leaderboard

app=Flask(__name__)
@app.route('/')

def game():
    leaderboard_front = leaderboard
    return render_template('game.html',leaderboard_front=leaderboard_front)

if __name__ == "__main__":
 app.run(debug=True)