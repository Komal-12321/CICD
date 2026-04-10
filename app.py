print("Welcome to TicTacToe game")
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [""] * 9
current_player = "X"

def check_winner():
    print("Checking winner... Current board:", board)
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            print(f"Winner found: {board[a]}")
            return board[a]
    return None

@app.route("/")
def home():
    print("Home page loaded")
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    global current_player
    data = request.json
    idx = data["index"]

    print(f"Move received at index: {idx}")
    print(f"Current player: {current_player}")

    if board[idx] == "":
        board[idx] = current_player
        print("Board updated:", board)

        winner = check_winner()

        if winner:
            print(f"Game Over! Winner: {winner}")
            return jsonify({"winner": winner, "board": board})

        current_player = "O" if current_player == "X" else "X"
        print(f"Next player: {current_player}")
    else:
        print("Invalid move! Cell already filled.")

    return jsonify({"board": board})

@app.route("/reset")
def reset():
    global board, current_player
    print("Game reset triggered")

    board = [""] * 9
    current_player = "X"

    print("Board reset:", board)
    return jsonify({"board": board})

if __name__ == "__main__":
    print("Starting Flask Tic Tac Toe App...")
    app.run(host="0.0.0.0", port=5000)
