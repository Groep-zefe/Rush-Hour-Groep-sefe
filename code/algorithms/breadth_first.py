import random
import copy


from code.classes.board import Board


class Breadth: 
    def __init__(self, board_size, cars):
        """ A Breadth First algorithm to solve the game."""
        
        self.board_size = board_size
        self.cars = cars
        self.board = None
        self.first_board = None
        self.temp_board = None
        self.all_moves = []
        self.moves_dict = {}
        self.empty_spaces = []
        self.move_car = {}
        self.parent_board = None
        self.queue = []


    def find_spaces(self, board):
        """Check board to find a possible move. """
        
        # If this is the first board
        if self.board == None:
            self.board = board
            self.first_board = tuple(tuple(b) for b in board)
        # Temporarily save parent board
        self.parent_board = copy.deepcopy(self.board)
        
        # Find empty spot on board
        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if self.board[rows][colums] == "_":
                    self.empty_spaces.append([rows, colums])

    
    def check_move(self):
        """ See if a move can be made."""

        self.move_car = {}
        # Loops over all empty spot on board
        for space in range(len(self.empty_spaces)):
            empty_temp = self.empty_spaces.pop()

            # Look for a car to move to that empty spot
            if empty_temp[1] + 1 < self.board_size:
                if self.board[empty_temp[0]][empty_temp[1] + 1] != "_":
                    temp_car = self.board[empty_temp[0]][empty_temp[1] + 1]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "H":
                        self.move_car[tuple([temp_car, -1])] = - 1
            
            if empty_temp[1] - 1  > 0:
                if self.board[empty_temp[0]][empty_temp[1] - 1] != "_":
                    temp_car = self.board[empty_temp[0]][empty_temp[1] - 1]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "H":
                        self.move_car[tuple([temp_car, 1])] = 1
             
            if empty_temp[0] + 1 < self.board_size:              
                if self.board[empty_temp[0] + 1][empty_temp[1]] != "_":
                    temp_car = self.board[empty_temp[0] + 1][empty_temp[1]]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "V":
                        self.move_car[tuple([temp_car, -1])] = - 1
          
            if empty_temp[0] - 1 > 0:  
                if self.board[empty_temp[0] - 1][empty_temp[1]] != "_":
                    temp_car = self.board[empty_temp[0] - 1][empty_temp[1]]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "V":
                        self.move_car[tuple([temp_car, 1])] = 1

            # Retry when no car has been found
            if len(self.empty_spaces) == 0:
                break


    def make_move(self, breakcheck, car_id, car_dir, orientation, car_length):
        """ Find car in the board and change the possition. """

        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if self.board[rows][colums] == car_id:
                    breakcheck = 1
                    # Horizontal cars
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
                        # Length is 3
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
                    # Vertical cars
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
                        # Length is 3
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


    def move(self):
        """ Makes all the possible boards"""

        breakcheck = 0
        car_keys = self.move_car.keys()
        # Loop over all cars and get their info
        for key in car_keys:
            car_id = key[0]
            car_dir = self.move_car[key]
            orientation = (self.cars[car_id].orientation)
            car_length = (self.cars[car_id].length)

            # (re)Set to parent board
            self.board = copy.deepcopy(self.parent_board)
            
            # Uses the make_move function to create a the possible boards
            self.make_move(breakcheck, car_id, car_dir, orientation, car_length)

            # Convert board to tuple in tuple
            self.temp_board = tuple(tuple(b) for b in self.board)
            
            # If this is a new board, add it to archive, add to queue
            if self.temp_board not in self.moves_dict.keys():
                self.moves_dict[self.temp_board] = tuple(tuple(b) for b in self.parent_board)
                self.queue.append(self.board)
              
    
    def next_child(self):
        """ Get next board in queue."""

        self.board = self.queue.pop(0)

    
    def won(self):
        """ Check if the game is won."""

        if self.board == None:
            return False
        # Get red car coordinates, check if on the winning location
        red_row = self.cars["X"].row
        if self.board[red_row][self.board_size - 1] == "X":
            return True
        else:
            return False


    def traceback(self):
        """ Trace back the boards in moves_dict to find the steps made."""
        # Make a list to save all boards in
        winning_states = []
        current_board = tuple(tuple(b) for b in self.board)
        # First add last and second to last board
        previous_board = self.moves_dict[current_board]
        winning_states.append(current_board)
        winning_states.append(previous_board)
        # Add all preceding boards
        while previous_board != self.first_board:
            previous_board = self.moves_dict[previous_board]
            winning_states.append(previous_board)
        return winning_states
        