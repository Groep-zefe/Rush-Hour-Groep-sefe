import csv
from sys import argv
import os

from code.classes.cars import Cars
from code.classes.board import Board
from code.classes.solution import Solution
from code.classes.load import Load_game
from code.classes.timer import Timer
from code.algorithms.random import Random
from code.algorithms.breadth_first import Breadth


# Check command line arguments
if len(argv) not in [1, 2, 3]:
    print("Usage: python rushhour.py [Game_name] [algorithm]")
    exit(1)

# Load the requested game or else 1
if len(argv) == 1:
    game_name = 1
    algorithm_name = random
elif len(argv) == 2:
    game_name = int(argv[1])
    algorithm_name = random 
else: 
    game_name = int(argv[1])
    algorithm_name = argv[2] 

print("Welcome to Rush Hour!\n")

t = Timer()
t.start()

load = Load_game()
board = load.game(game_name)
if algorithm_name == 'random':
    algo = Random(board.board_size, board.cars)
elif algorithm_name == "breadth":
    algo = Breadth(board.board_size, board.cars)
else: 
    print("This algorithm doesn't exists")
    exit(1)

previous_fastest = Solution(game_name, algo.all_moves)
previous_fastest.find_fastest()

tries = 0

if algorithm_name == 'random':
    # until manually stopped
    while True:
        tries += 1

        board = load.game(game_name)
        board.load_board()
        # print("trying new game")

        winning_coordinate = board.board_size - 2 
        red_car = board.cars['X']

        algorithm = Random(board.board_size, board.cars)
        # play a game
        while red_car.col != winning_coordinate: 
            load_board = board.load_board()
            algorithm.check_move(load_board)
            algorithm.move()
            board.load_board()
            algorithm.check_board(load_board)

            temp_solution = Solution(game_name, algorithm.all_moves)
            temp_solution.find_fastest()
            if temp_solution.result_check():
                # print("too long")
                break
        
        # make and check the games solution    
        solve_game = Solution(game_name, algorithm.all_moves)
        solve_game.find_fastest()
        solve_game.save_solution()

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"number of tries: {tries}")
        print(f"fastest: {solve_game.fastest_game}")
else:
    board = load.game(game_name)
    board.load_board()

    algorithm = Breadth(board.board_size, board.cars)
    load_board = board.load_board()

    winning_coordinate = board.board_size - 2 
    red_car = board.cars['X']

    while True:
        algorithm.find_spaces(load_board)
        algorithm.check_move()
        algorithm.move()
        algorithm.next_child()
        # algorithm.visualize_board()
        if algorithm.won():
            print(algorithm.traceback())
            break

    # make and check the games solution    
    solve_game = Solution(game_name, algorithm.all_moves)
    solve_game.find_fastest()
    # solve_game.save_solution()

t.stop()    

