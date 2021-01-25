
import copy

from code.algorithms.breadth_first import Breadth

class Winning_moves(): 
    def __init__(self, board_size, car, boards):
        self.board_size = board_size
        self.cars = car
        self.all_boards = boards
        self.all_moves = []
        self.board = None
    

    def traceback_moves(self): 

        while len(self.all_boards) > 1: 
            this_board = list(list(b) for b in self.all_boards.pop(-1))
            parent_board = this_board

            find_move = Breadth(self.board_size, self.cars)

            find_move.find_spaces(this_board)
            find_move.check_move()

            breakcheck = 0
        
            car_keys = find_move.move_car.keys()
            # loop over all cars and fill in their coordinates
            for key in car_keys:
                car_id = key[0]
                car_dir = find_move.move_car[key]
                orientation = (self.cars[car_id].orientation)
                car_length = (self.cars[car_id].length)
                
                self.board = copy.deepcopy(parent_board)

                for rows in range(self.board_size):
                    for colums in range(self.board_size):
                        if self.board[rows][colums] == car_id:
                            breakcheck = 1
                            if orientation == "H":
                                if car_length == "2":
                                    if car_dir == 1:
                                        self.board[rows][colums] = '_'
                                        self.board[rows][colums + 1] = car_id
                                        self.board[rows][colums + 2] = car_id
                                    else: 
                                        self.board[rows][colums - 1] = car_id
                                        self.board[rows][colums] = car_id
                                        self.board[rows][colums + 1] = '_'
                                # length is 3
                                else:
                                    if car_dir == 1:
                                        self.board[rows][colums] = '_'
                                        self.board[rows][colums + 1] = car_id
                                        self.board[rows][colums + 2] = car_id
                                        self.board[rows][colums + 3] = car_id
                                    else: 
                                        self.board[rows][colums - 1] = car_id
                                        self.board[rows][colums] = car_id
                                        self.board[rows][colums + 1] = car_id
                                        self.board[rows][colums + 2] = '_'
                            else:
                                if car_length == "2":
                                    if car_dir == 1:
                                        self.board[rows][colums] = '_'
                                        self.board[rows + 1][colums] = car_id
                                        self.board[rows + 2][colums] = car_id
                                    else: 
                                        self.board[rows - 1][colums] = car_id
                                        self.board[rows][colums] = car_id
                                        self.board[rows + 1][colums] = '_'
                                # length is 3
                                else:
                                    if car_dir == 1:
                                        self.board[rows][colums] = '_'
                                        self.board[rows + 1][colums] = car_id
                                        self.board[rows + 2][colums] = car_id
                                        self.board[rows + 3][colums] = car_id
                                    else: 
                                        self.board[rows - 1][colums] = car_id
                                        self.board[rows][colums] = car_id
                                        self.board[rows + 1][colums] = car_id
                                        self.board[rows + 2][colums] = '_'     
                        if breakcheck == 1:
                            break
                    if breakcheck == 1:
                        breakcheck = 0
                        break
                        
                if self.board == list(list(b) for b in self.all_boards[-1]):
                    self.all_moves.append([key[0][0], key[1]])

            
