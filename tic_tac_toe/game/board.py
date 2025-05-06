class Board:
    def __init__(self):
        self.cells = [str(i) for i in range(1, 10)]

    def current_board(self):
        return (
        f"{self.cells[0]} | {self.cells[1]} | {self.cells[2]}\n"
        f"---------\n"
        f"{self.cells[3]} | {self.cells[4]} | {self.cells[5]}\n"
        f"---------\n"
        f"{self.cells[6]} | {self.cells[7]} | {self.cells[8]}")

    def place_marker(self, position, marker):
        self.cells[position - 1] = marker

    def is_draw(self):
        return all(cell in ['X', 'O'] for cell in self.cells)

    def check_winner(self, marker):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],  
            [0,3,6], [1,4,7], [2,5,8],  
            [0,4,8], [2,4,6]]
        return any(all(self.cells[i] == marker for i in line) for line in wins)

'''
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def current_board(self):
        return "\n".join([f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} "
            + ("\n-----------" if i < 6 else "")
            for i in range(0, 9, 3)])


    def current_board():
        print("Current Board: ")
        board = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"
        ]
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])
'''