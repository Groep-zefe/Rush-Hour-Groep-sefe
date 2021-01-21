import queue
import random
import copy
import math


from code.classes.board import Board

class Breadth(): 
    def __init__(self, board_size, car):
        self.board_size = board_size
        self.cars = car
        self.board = None
        self.temp_board = None
        self.all_moves = []
        self.move_car = {}
        self.board_states = set()
        self.empty_spaces = []
        self.parent_board = None

    # check board to find a possible move
    def find_spaces(self, board):
        self.board = board
        self.parent_board = copy.deepcopy(board)

        # find empty spot on board
        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if self.board[rows][colums] == "_":
                    self.empty_spaces.append([rows, colums])

    def check_move(self, board):
        self.move_car = {}
        # choose a random empty spot on board
        for space in range(len(self.empty_spaces)):
            empty_temp = self.empty_spaces.pop()

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
            if len(self.empty_spaces) == 0:
                print(self.move_car)
                break

    # move a car to new location
    def move(self):
        breakcheck = 0
        car_keys = self.move_car.keys()
        # loop over all cars and fill in their coordinates
        for key in car_keys:
            car_id = key
            car_dir = self.move_car[car_id]
            orientation = (self.cars[car_id].orientation)
            car_length = (self.cars[car_id].length)
            
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
                      
            # print(f'papa {self.parent_board}')
            # print(f'kind {self.board}')
            # convert board to tuple in tuple
            self.temp_board = tuple(tuple(b) for b in self.board)
            # print(self.temp_board)
            
            # if this is a new board, add it to archive, add move to moveslist
            if self.temp_board not in self.board_states:
                self.board_states.add(self.temp_board)
                self.board = copy.deepcopy(self.parent_board)

        print(self.board_states)