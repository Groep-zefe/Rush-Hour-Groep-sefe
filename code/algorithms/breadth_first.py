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
        self.first_board = None
        self.temp_board = None
        self.all_moves = []
        self.moves_dict = {}
        self.move_car = {}
        self.board_states = set()
        self.empty_spaces = []
        self.parent_board = None
        self.queue = []

    # check board to find a possible move
    def find_spaces(self, board):
        if self.board == None:
            self.board = board
            self.first_board = tuple(tuple(b) for b in board)
            self.temp_board = tuple(tuple(b) for b in self.board)
            self.board_states.add(self.temp_board)
        self.parent_board = copy.deepcopy(self.board)
        
        # find empty spot on board
        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if self.board[rows][colums] == "_":
                    self.empty_spaces.append([rows, colums])

    def check_move(self):
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

            # retry when no car has been found
            if len(self.empty_spaces) == 0:
                break

    # move a car to new location
    def move(self):
        breakcheck = 0
        car_keys = self.move_car.keys()
        # loop over all cars and fill in their coordinates
        for key in car_keys:
            car_id = key[0]
            car_dir = self.move_car[key]
            orientation = (self.cars[car_id].orientation)
            car_length = (self.cars[car_id].length)
            
            self.board = copy.deepcopy(self.parent_board)

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
                    
            # convert board to tuple in tuple
            self.temp_board = tuple(tuple(b) for b in self.board)
            
            # if this is a new board, add it to archive, add move to moveslist
            if self.temp_board not in self.board_states:
                self.board_states.add(self.temp_board)
                self.moves_dict[self.temp_board] = tuple(tuple(b) for b in self.parent_board)
                self.queue.append(self.board)
                self.board = copy.deepcopy(self.parent_board)

    def next_child(self):
        self.board = self.queue.pop(0)
        
    def won(self):
        red_row = self.cars["X"].row
        if self.board[red_row][self.board_size - 1] == "X":
            return True

    def traceback(self):
        self.temp_board = tuple(tuple(b) for b in self.board)
        previous_board = self.moves_dict[self.temp_board]
        count = 1
        while previous_board != self.first_board:
            previous_board = self.moves_dict[previous_board]
            count += 1
        return count
        

        
  # prints each board to terminal. Not necessary for good result
    def visualize_board(self):      
        for i in self.board:
            print(" ".join(i))
        print("\n")