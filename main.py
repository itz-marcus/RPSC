import random

def update_leaderboard(result, leaderboard):
    if result == "win":
        leaderboard["win_streak"] += 1
    else:
        leaderboard["win_streak"] = 0

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "loss"

def get_computer_choice(options):
    return random.choice(options)
