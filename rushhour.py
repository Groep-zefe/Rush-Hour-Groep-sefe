from board import Cars, Board

class Solve_game:
    def __init__(self, game):

        board = Board()
        if game <= 3: 
            board.load_cars(f"boards/Rushhour6x6_{game}.csv")
        elif game <= 6: 
            board.load_cars(f"boards/Rushhour9x9_{game}.csv")
        else: 
            board.load_cars(f"boards/Rushhour12x12_{game}.csv")
        
        board.load_board()


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
