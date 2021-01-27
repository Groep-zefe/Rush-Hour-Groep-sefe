import random
import copy
import math

from code.classes.cars import Cars


class Random:
    def __init__(self, board_size, car):
        """ A random algorithm with archive to find a solution to a game."""
        
        self.board_size = board_size
        self.cars = car
        self.board = None
        self.move_car = {}
        self.failed_move = 0
        self.board_arch = []
        self.random_car = None
        self.temp_coordinates = None
        self.all_moves = []


    def check_board(self, board): 
        """ Checks if the board already exists if it doesn't adds it to an archive."""

        self.board = board
        
        # If this is a new board, add it to archive, add move to moveslist
        if self.board not in self.board_arch:
            self.failed_move = 0
            self.board_arch.append(self.board)
            if len(self.board_arch) > 1:
                self.all_moves.append([self.random_car, self.move_car[self.random_car]])
        # Go back to the previous board and try to make a move again
        else:
            car_orientation = self.cars[self.random_car].orientation
            # Set coordinates back
            if car_orientation == "V":
                self.cars[self.random_car].row = copy.deepcopy(self.temp_coordinates)
            else:
                self.cars[self.random_car].col = copy.deepcopy(self.temp_coordinates)
            self.failed_move += 1
            
        # If not possible to make a move 10 consecutive times
        if self.failed_move > 10: 
            # Remove last 10% boards from archive to be able to take steps back
            for board in range(math.ceil(len(self.board_arch)/10)):
                del self.board_arch[-1]
                self.failed_move = 0
  

    def check_move(self, board):
        """Check board to find a possible move for a random empty space."""

        self.move_car = {}
        self.board = board
        empty_spaces = []

        # Find empty spot on board
        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if self.board[rows][colums] == "_":
                    empty_spaces.append([rows, colums])
        
        # Choose a random empty spot on board
        random.shuffle(empty_spaces)
        for space in range(len(empty_spaces)):
            empty_temp = empty_spaces.pop()

            # Look for a car to move to that empty spot
            if empty_temp[1] + 1 < self.board_size:
                if self.board[empty_temp[0]][empty_temp[1] + 1] != "_":
                    temp_car = self.board[empty_temp[0]][empty_temp[1] + 1]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "H":
                        self.move_car[temp_car] = - 1
            
            if empty_temp[1] - 1  > 0:
                if self.board[empty_temp[0]][empty_temp[1] - 1] != "_":
                    temp_car = self.board[empty_temp[0]][empty_temp[1] - 1]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "H":
                        self.move_car[temp_car] = 1
             
            if empty_temp[0] + 1 < self.board_size:              
                if self.board[empty_temp[0] + 1][empty_temp[1]] != "_":
                    temp_car = self.board[empty_temp[0] + 1][empty_temp[1]]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "V":
                        self.move_car[temp_car] = - 1
          
            if empty_temp[0] - 1 > 0:  
                if self.board[empty_temp[0] - 1][empty_temp[1]] != "_":
                    temp_car = self.board[empty_temp[0] - 1][empty_temp[1]]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "V":
                        self.move_car[temp_car] = 1

            # Break when a car has been found
            if len(self.move_car.keys()) > 0:
                break


    def move(self):
        """ Changes the car coordinates to move the car to new location."""

        # If red car can move, move red car
        if ["X"] in list(self.move_car.keys()) and self.move_car["X"] == 1:
                self.random_car = "X"
        else:
            # Randomly pick one of the possibilities
            self.random_car = random.choice(list(self.move_car.keys()))
                    
        # Get and then change coordinates 
        car_orientation = self.cars[self.random_car].orientation
        if car_orientation == "V":
            self.temp_coordinates = copy.deepcopy(self.cars[self.random_car].row)
            self.cars[self.random_car].row = self.cars[self.random_car].row + self.move_car[self.random_car]
        else:
            self.temp_coordinates = copy.deepcopy(self.cars[self.random_car].col)
            self.cars[self.random_car].col = self.cars[self.random_car].col + self.move_car[self.random_car]

        

     