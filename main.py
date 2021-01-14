import csv
from sys import argv

from cars import Cars
from board import Board
from solution import Solution


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
if game_name <= 3:
    board.load_cars(f"boards/Rushhour6x6_{game_name}.csv")
elif game_name <= 6: 
    board.load_cars(f"boards/Rushhour9x9_{game_name}.csv")
else: 
    board.load_cars(f"boards/Rushhour12x12_{game_name}.csv")

board.load_board()
board.visualize_board()

winning_coordinate = board.board_size - 2 

red_car = board.cars['X']

while board.arch_count < 5:
    while red_car.col != winning_coordinate:
        board.check_move()
        board.move()
        board.load_board()
        board.visualize_board()
        print("\n")
        
board.visualize_board()

solve_game = Solution(game_name, board.all_moves)

solve_game.solution()
