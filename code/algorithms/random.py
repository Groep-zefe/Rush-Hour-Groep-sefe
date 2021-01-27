import random
import copy
import math

from code.classes.cars import Cars

class Random:
    def __init__(self, board_size, car):
        self.board_size = board_size
        self.cars = car
        self.board = None
        self.move_car = {}
        self.failed_move = 0
        self.board_arch = []
        self.random_car = None
        self.temp_coordinates = None

    def check_board(self, board): 
        self.board = board
        
        # if this is a new board, add it to archive, add move to moveslist
        if self.board not in self.board_arch:
            self.failed_move = 0
            self.board_arch.append(self.board)
            if len(self.board_arch) > 1:
                self.all_moves.append([self.random_car, self.move_car[self.random_car]])
        # go back to the previous board and try to make a move again
        else:
            # self.board = self.board_arch[-1]
            car_orientation = self.cars[self.random_car].orientation
            # set coordinates back
            if car_orientation == "V":
                self.cars[self.random_car].row = copy.deepcopy(self.temp_coordinates)
            else:
                self.cars[self.random_car].col = copy.deepcopy(self.temp_coordinates)
            self.failed_move += 1
            
        # if not possible to make a move 10 consecutive times
        if self.failed_move > 10: 
            # remove last 10% boards from archive to be able to take steps back
            for board in range(math.ceil(len(self.board_arch)/10)):
                del self.board_arch[-1]
                self.failed_move = 0
  
    # check board to find a possible move
    def check_move(self, board):
        self.move_car = {}
        self.board = board
        empty_spaces = []

        # find empty spot on board
        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if self.board[rows][colums] == "_":
                    empty_spaces.append([rows, colums])
        
        # choose a random empty spot on board
        random.shuffle(empty_spaces)
        for space in range(len(empty_spaces)):
            empty_temp = empty_spaces.pop()

            # look for a car to move to that empty spot
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

            # break when a car has been found
            if len(self.move_car.keys()) > 0:
                break

    # move a car to new location
    def move(self):
        # if red car can move, move red car
        if ["X"] in list(self.move_car.keys()) and self.move_car["X"] == 1:
                self.random_car = "X"
        else:
            # randomly pick one of the possibilities
            self.random_car = random.choice(list(self.move_car.keys()))
                    
        # get and then change coordinates 
        car_orientation = self.cars[self.random_car].orientation
        if car_orientation == "V":
            self.temp_coordinates = copy.deepcopy(self.cars[self.random_car].row)
            self.cars[self.random_car].row = self.cars[self.random_car].row + self.move_car[self.random_car]
        else:
            self.temp_coordinates = copy.deepcopy(self.cars[self.random_car].col)
            self.cars[self.random_car].col = self.cars[self.random_car].col + self.move_car[self.random_car]

        

     