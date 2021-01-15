import csv
import random
import copy

from cars import Cars

class Board:
    def __init__(self):
        self.cars = {}
        self.board_size = 0
        self.board = [[]]
        self.all_moves = []
        self.move_car = {}
        self.failed_move = 0
        self.board_arch = []
        self.random_car = None
        self.temp_coordinates = None


    def load_cars(self, filename):
        with open ( filename, "r") as csvfile:
            datafile = csv.reader(csvfile)

            for row in datafile: 
                if row[0] != "car":
                    self.cars[row[0]] = Cars(row[0], row[1], row[3], row[2], row[4])
                    if int(row[2]) > self.board_size:
                        self.board_size = int(row[2])

        return self.cars


    def load_board(self):
        self.board = [["_" for rows in range(self.board_size)] for colums in range(self.board_size)]

        # set whole board to 0 
        for rows in range(self.board_size):
            for colums in range(self.board_size):
                self.board[rows][colums] = 0
        
        cars = self.cars
        car_keys = cars.keys()
        # loop over all cars and fill in their coordinates
        for key in car_keys:
            list_coordinates = (cars[key].coordinates())
            print(list_coordinates)
            car_id = list_coordinates[0]
            self.board[list_coordinates[1][0]][list_coordinates[1][1]] = car_id
            self.board[list_coordinates[2][0]][list_coordinates[2][1]] = car_id

            if len(list_coordinates) == 4: 
                self.board[list_coordinates[3][0]][list_coordinates[3][1]] = car_id

        # fill in underscore for eacht empty spot on the board    
        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if self.board[rows][colums] == 0:
                    self.board[rows][colums] = "_"

        # if this is a new board, add it to archive, add move to moveslist
        if self.board not in self.board_arch:
            self.failed_move = 0
            self.board_arch.append(self.board)
            if len(self.board_arch) > 1:
                self.all_moves.append([self.random_car, self.move_car[self.random_car]])
        # go back to the previous board and try to make a move again
        else:  
            self.board = self.board_arch[-1]
            car_orientation = self.cars[self.random_car].orientation
            # set coordinates back
            if car_orientation == "V":
                self.cars[self.random_car].row = copy.deepcopy(self.temp_coordinates)
            else:
                self.cars[self.random_car].col = copy.deepcopy(self.temp_coordinates)
            self.failed_move += 1 
            
        # if not possible to make a move 5 consecutive times, remove boards from archive to be able to take steps back
        if self.failed_move > 5: 
            # print(f'all {self.board_arch}')
            for i in range(10):
                del self.board_arch[-1]
                #  print(f'removed {self.board_arch}')


    # prints each board and made move to terminal. Not necessary for good result
    def visualize_board(self):    
        
        for i in self.board:
            print(" ".join(i))
        
        print(f'try to move car {self.random_car}')
        
        
    # check board to find a possible move
    def check_move(self):
        self.move_car = {}
        empty_spaces = []
        random_keys = []

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
        print(self.move_car)
        # randomly pick one of the possibilities
        self.random_car = random.choice(list(self.move_car.keys()))
                    
        # get and then change coordinates 
        car_orientation = self.cars[self.random_car].orientation
        if car_orientation == "V":
            print(self.cars[self.random_car].row)
            self.temp_coordinates = copy.deepcopy(self.cars[self.random_car].row)
            print(self.temp_coordinates)
            self.cars[self.random_car].row = self.cars[self.random_car].row + self.move_car[self.random_car]
            print(self.cars[self.random_car].row)
        else:
            print(self.cars[self.random_car].col)
            self.temp_coordinates = copy.deepcopy(self.cars[self.random_car].col)
            print(self.temp_coordinates)
            self.cars[self.random_car].col = self.cars[self.random_car].col + self.move_car[self.random_car]
            print(self.cars[self.random_car].col)
        

     