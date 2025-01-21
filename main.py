from flask import Flask,render_template
import random

app=Flask(__name__)
@app.route('/')
def game():
    return render_template('game.html')

def update_leaderboard(result, leaderboard):
    if result == "win":
        leaderboard["win_streak"] += 1
    else:
        leaderboard["win_streak"] = 0

def display_leaderboard(leaderboard):
    print("\nLeaderboard:")
    print(f"Current Win Streak: {leaderboard['win_streak']}\n")

options = ("rock", "paper", "scissors")
running = True
leaderboard = {"win_streak": 0}
name = input('Enter your name : ')

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
        update_leaderboard("tie", leaderboard)
    elif player == "rock" and computer == "scissors":
        print("You win!")
        update_leaderboard("win", leaderboard)
    elif player == "paper" and computer == "rock":
        print("You win!")
        update_leaderboard("win", leaderboard)
    elif player == "scissors" and computer == "paper":
        print("You win!")
        update_leaderboard("win", leaderboard)
    else:
        print("You lose!")
        update_leaderboard("loss", leaderboard)

    display_leaderboard(leaderboard)

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing ," , name , "!")
if __name__ == "__main__":
 app.run(debug=True)
