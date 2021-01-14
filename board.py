import csv
import random

from cars import Cars

class Board:
    def __init__(self):
        self.cars = {}
        self.board_size = 0
        self.board = [[]]
        self.all_moves = []
        self.move_car = {}
        self.board_arch = []
        self.random_car = None


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

        for rows in range(self.board_size):
            for colums in range(self.board_size):
                self.board[rows][colums] = 0
        
        cars = self.cars
        car_keys = cars.keys()

        for key in car_keys:
            list_coordinates = (cars[key].coordinates())
            car_id = list_coordinates[0]
            self.board[list_coordinates[1][0]][list_coordinates[1][1]] = car_id
            self.board[list_coordinates[2][0]][list_coordinates[2][1]] = car_id

            if len(list_coordinates) == 4: 
                self.board[list_coordinates[3][0]][list_coordinates[3][1]] = car_id

       
        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if self.board[rows][colums] == 0:
                    self.board[rows][colums] = "_"
        
        no_moves = 0

        if self.board not in self.board_arch:
            no_moves = 0
            self.board_arch.append(self.board)
            if len(self.board_arch) > 1:
                self.all_moves.append([self.random_car, self.move_car[self.random_car]])
        else: 
            no_moves += 1

        if no_moves > 5: 
            for i in range(10):
                del self.board_arch[-1]
        
    def visualize_board(self):    
        for i in self.board:
            print(" ".join(i))
        
        print(f'the moved car is {self.random_car}')
        
        
    def check_move(self):
        self.move_car = {}
        empty_spaces = []
        random_keys = []

        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if self.board[rows][colums] == "_":
                    empty_spaces.append([rows, colums])
        
        random.shuffle(empty_spaces)
        for space in range(len(empty_spaces)):
            empty_temp = empty_spaces.pop()

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

            if len(self.move_car.keys()) > 0:
                break

    def move(self):    
        self.random_car = random.choice(list(self.move_car.keys()))
                    
        car_orientation = self.cars[self.random_car].orientation

        if car_orientation == "V":
            self.temp_coordinates = self.cars[self.random_car].row
            self.cars[self.random_car].row = self.cars[self.random_car].row + self.move_car[self.random_car]
        else:
            self.temp_coordinates = self.cars[self.random_car].col
            self.cars[self.random_car].col = self.cars[self.random_car].col + self.move_car[self.random_car]
        
       


     