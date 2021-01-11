import csv

from board import Board
from solution import Solution

if __name__ == "__main__":

    from sys import argv

    # Check command line arguments
    if len(argv) not in [1, 2]:
        print("Usage: python rushhour.py [Game name]")
        exit(1)

    # Load the requested game or else 1
    if len(argv) == 1:
        game_name = 1
    elif len(argv) == 2:
        game_name = int(argv[1])
    
    print("Welcome to Rush Hour!\n")

    # def load_game(self): 
    board = Board()
    if self.game <= 3: # Hoe zat het ook alweer met self. in de main?
        board.load_cars(f"boards/Rushhour6x6_{self.game}.csv")
    elif self.game <= 6: 
        board.load_cars(f"boards/Rushhour9x9_{self.game}.csv")
    else: 
        board.load_cars(f"boards/Rushhour12x12_{self.game}.csv")
        
        # return board.load_board()

    solve_game = Solution(game_name)
    solve_game.load_game() # Zit ff hiermee lol

    solve_game.solution() # Hadden we iets van een solution member?
    