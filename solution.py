import csv

from board import Board

class Solution:

    def __init__(self, game):
        self.game = game

    def load_game(self): 
        board = Board()
        if self.game <= 3: 
            board.load_cars(f"boards/Rushhour6x6_{self.game}.csv")
        elif self.game <= 6: 
            board.load_cars(f"boards/Rushhour9x9_{self.game}.csv")
        else: 
            board.load_cars(f"boards/Rushhour12x12_{self.game}.csv")
        
        return board.load_board()