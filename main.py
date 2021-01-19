import csv
from sys import argv
import os

from cars import Cars
from board import Board
from solution import Solution
from load import Load_game


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

load = Load_game()
board = load.game(game_name)
previous_fastest = Solution(game_name, board.all_moves)
previous_fastest.find_fastest()

tries = 0

# until manually stopped
while True:
    tries += 1

    board = load.game(game_name)
    board.load_board()
    # print("trying new game")

    winning_coordinate = board.board_size - 2 
    red_car = board.cars['X']
    # play a game
    while red_car.col != winning_coordinate: 
        board.check_move()
        board.move()
        board.load_board()
        board.check_board()
        board.load_board()

        temp_solution = Solution(game_name, board.all_moves)
        temp_solution.find_fastest()
        if temp_solution.result_check():
            # print("too long")
            break

    # make and check the games solution    
    solve_game = Solution(game_name, board.all_moves)
    solve_game.find_fastest()
    solve_game.save_solution()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"number of tries: {tries}")
    print(f"fastest: {solve_game.fastest_game}")

