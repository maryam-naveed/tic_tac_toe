from tools import display as dsp
from tools.logger import Logger
from game.board import Board
from game.players import Player
from game import utils
import time

def start_game():
     turn = 0
     b = Board()
     dsp.title()
     name_1 = input("Player 1: ")
     name_2 = input("Player 2: ")
     dsp.welcome(name_1, name_2)
     player_1 = Player(name_1, "X")
     player_2 = Player(name_2, "O")
     players = [player_1, player_2]
     
     log = Logger(player_1, player_2)
     
     while True:
        dsp.display_board(b)
        current_player = players[turn % 2]
        move = dsp.get_move(current_player)
        move = utils.clean_input(move)
        
        while not utils.valid_move(move, b):
            dsp.display_invalid()
            move = dsp.get_move(current_player)
            move = utils.clean_input(move)
            
        b.place_marker(move, current_player.marker)
        log.log_move(current_player, move, b)
        
        if b.check_winner(current_player.marker):
            dsp.display_board(b)
            dsp.display_result(current_player)
            log.log_result(f"{current_player.name} wins!")
            break
        
        elif b.is_draw():
            dsp.display_board(b)
            dsp.draw()
            log.log_result("It's a draw!")
            break
        
        turn += 1
        

if __name__ == "__main__":
    while True:
        start_game()
        again = input("Would you like to play again? (yes/no): ").lower()
        if again != 'yes':
            break