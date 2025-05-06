def title():
    print("Tic Tac Toe")
    print("Please enter your names")

def welcome(player1, player2):
    print(f"Welcome, {player1} and {player2}!")

def display_board(board):
    print("Current Board:")
    print(board.current_board())

def get_move(player):
    print(f"{player.name}'s Turn ({player.marker}):")
    return input(f"Enter a position (1-9): ")

def display_invalid():
    print("Invalid move. Try again.")

def display_result(player):
    print(f"Congratulations, {player.name}! You win!")

def draw():
    print("It's a draw!")