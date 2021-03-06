from code.classes.board import Board


class Load_game:
    def __init__(self):
        """ Loads the game of your choosing."""
        pass
    
    
    def game(self, game):
        """ Chooses the game based on the input in the terminal."""

        board = Board()
        if game <= 3:
            board.load_cars(f"boards/Rushhour6x6_{game}.csv")
        elif game <= 6: 
            board.load_cars(f"boards/Rushhour9x9_{game}.csv")
        else: 
            board.load_cars(f"boards/Rushhour12x12_{game}.csv")
        
        return board
