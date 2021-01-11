import csv
from pathlib import Path

from board import Cars, Board

class Solve_game:
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
    
    def move(self): 
        pass

    def solution(self): 
        i = 0 

        test_solution = [ ['A', '1'], ['C', '-2'], ['G', '-1']]
        
        while True:  
            my_file = Path(f'solutions/solution_game_{self.game}.{i}.csv')
            if my_file.is_file():
                i += 1
            else: break

        with open(f'solutions/solution_game_{self.game}.{i}.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['car', 'move']) 
            writer.writerows(test_solution)


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

    solve_game = Solve_game(game_name)
    solve_game.load_game()

    solve_game.solution()
