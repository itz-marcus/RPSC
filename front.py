from flask import Flask, render_template, request, jsonify
from main import update_leaderboard, determine_winner, get_computer_choice
from leaderboard import add_score, get_top_scores

app = Flask(__name__)

options = ("rock", "paper", "scissors")
leaderboard = {"win_streak": 0}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game")
def index():
    top_scores = get_top_scores()  # Fetch leaderboard
    return render_template("game.html", leaderboard_front=leaderboard["win_streak"], top_scores=top_scores)

@app.route("/play", methods=["POST"])
def play():
    player_choice = request.json.get("choice")
    if player_choice not in options:
        return jsonify({"error": "Invalid choice"}), 400

    computer_choice = get_computer_choice(options)
    result = determine_winner(player_choice, computer_choice)

    previous_streak = leaderboard["win_streak"]
    update_leaderboard(result, leaderboard)

    # If the player loses and had a win streak, prompt for name and save
    if result == "loss" and previous_streak > 0:
        return jsonify({
            "player_choice": player_choice,
            "computer_choice": computer_choice,
            "result": result,
            "win_streak": leaderboard["win_streak"],
            "save_score": previous_streak
        })

    top_scores = get_top_scores()
    return jsonify({
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "result": result,
        "win_streak": leaderboard["win_streak"],
        "top_scores": top_scores
    })

@app.route("/save_score", methods=["POST"])
def save_score():
    name = request.json.get("name")
    score = request.json.get("score")
    if name and score:
        add_score(name, score)
    return jsonify({"message": "Score saved!", "top_scores": get_top_scores()})

if __name__ == "__main__":
    app.run()
