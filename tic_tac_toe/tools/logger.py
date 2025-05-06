from pathlib import Path

class Logger:
    game_counter = 1

    def __init__(self, player1, player2):
        self.log_dir = Path("tic_tac_toe/game_log") / f"game{Logger.game_counter}"
        while self.log_dir.exists():
            Logger.game_counter += 1
            self.log_dir = Path("tic_tac_toe/game_log") / f"game{Logger.game_counter}"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / "log.txt"
        self.move_number = 1

        with self.log_file.open("w") as f:
            f.write(f"Game {Logger.game_counter} Log\n\n")
            f.write("Players:\n")
            f.write(f"{player1.name} ({player1.marker})\n")
            f.write(f"{player2.name} ({player2.marker})\n\n")
            f.write(f"First move: {player1.name}\n\nMoves:\n")

    def log_move(self, player, position, board):
        with self.log_file.open("a") as f:
            f.write(f"Move {self.move_number}: {player.name} -> Position {position}\n")
            f.write("Board After Move:\n")
            f.write(board.current_board() + "\n\n")
        self.move_number += 1

    def log_result(self, result):
        with self.log_file.open("a") as f:
            f.write(f"Result: {result}\n")
