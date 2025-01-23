from flask import Flask, render_template, request, jsonify
from main import update_leaderboard, determine_winner, get_computer_choice

app = Flask(__name__)

options = ("rock", "paper", "scissors")
leaderboard = {"win_streak": 0}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game")
def index():
    return render_template("game.html", leaderboard_front=leaderboard["win_streak"])

@app.route("/play", methods=["POST"])
def play():
    # Get player's choice from the request
    player_choice = request.json.get("choice")
    if player_choice not in options:
        return jsonify({"error": "Invalid choice"}), 400

    # Generate computer's choice
    computer_choice = get_computer_choice(options)

    # Determine the result
    result = determine_winner(player_choice, computer_choice)

    # Update the leaderboard
    update_leaderboard(result, leaderboard)

    # Return the result to the frontend
    return jsonify({
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "result": result,
        "win_streak": leaderboard["win_streak"]
    })

if __name__ == "__main__":
    app.run()
