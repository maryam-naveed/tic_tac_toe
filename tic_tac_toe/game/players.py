class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def player_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name}'s Turn ({self.marker}): Enter position (1-9): "))
                if 1 <= move <= 9 and board.is_valid_move(move):
                    return move
                else:
                    print("Invalid move! Please try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

