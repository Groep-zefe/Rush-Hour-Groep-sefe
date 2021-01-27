import os

from sys import argv

from code.classes.cars import Cars
from code.classes.board import Board
from code.classes.solution import Solution
from code.classes.load import Load_game
from code.classes.timer import Timer
from code.classes.moves import Winning_moves
from code.algorithms.random import Random
from code.algorithms.breadth_first import Breadth


# Check command line arguments
if len(argv) not in [1, 2, 3]:
    print("Usage: python rushhour.py [Game_name] [algorithm]")
    exit(1)

# Load the requested game and algorithm else 1 and random 
if len(argv) == 1:
    game_name = 1
    algorithm_name = "random"
elif len(argv) == 2:
    game_name = int(argv[1])
    algorithm_name = "random"
else: 
    game_name = int(argv[1])
    algorithm_name = argv[2] 

print("Welcome to Rush Hour!\n")

# Starts the timer voor the runnning time 
t = Timer()
t.start()

# Loads the requested game board 
load = Load_game()
board = load.game(game_name)

# Checks the algorithm that should be used 
if algorithm_name == 'random':
    algo = Random(board.board_size, board.cars)
elif algorithm_name == "breadth":
    algo = Breadth(board.board_size, board.cars)
else: 
    print("This algorithm doesn't exists")
    exit(1)

# The code to run the random algorithm with archive
if algorithm_name == 'random':
    
    previous_fastest = Solution(game_name, algo.all_moves)
    previous_fastest.find_fastest()

    tries = 0

    # Until manually stopped
    while True:
        tries += 1

        board = load.game(game_name)
        board.load_board()

        winning_coordinate = board.board_size - 2 
        red_car = board.cars['X']

        algorithm = Random(board.board_size, board.cars)
        
        # Plays a game to find a solution 
        while red_car.col != winning_coordinate: 
            load_board = board.load_board()
            algorithm.check_move(load_board)
            algorithm.move()
            board.load_board()
            algorithm.check_board(load_board)

            
            temp_solution = Solution(game_name, algorithm.all_moves)
            temp_solution.find_fastest()
            # Checks if the current result is not longer than the fastest else break
            if temp_solution.result_check():
                break
                
        # Makes and checks the games solution    
        solve_game = Solution(game_name, algorithm.all_moves)
        solve_game.find_fastest()
        solve_game.save_solution()

        # Clears the terminal and prints the number of tries and fastest solution
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"number of tries: {tries}")
        print(f"fastest: {solve_game.fastest_game}")

# The code to run the Breadth First algorithm 
else:
    board = load.game(game_name)
    board.load_board()

    algorithm = Breadth(board.board_size, board.cars)
    load_board = board.load_board()

    winning_coordinate = board.board_size - 2 
    red_car = board.cars['X']

   # Code to find the solution to a game  
    while algorithm.won() == False:
        algorithm.find_spaces(load_board)
        algorithm.check_move()
        algorithm.move()
        algorithm.next_child()

    t.stop() 
    
    # Checks all the moves that are made to find a solution
    moves = Winning_moves(board.board_size, board.cars, algorithm.traceback())
    moves.traceback_moves()

    # Saves the games solution    
    solve_game = Solution(game_name, moves.all_moves)
    solve_game.save_solution()
    print(f"I'm Speed: {solve_game.fastest_game}!!")

   

