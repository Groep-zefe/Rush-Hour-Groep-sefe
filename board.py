import csv
import random

from cars import Cars

class Board:
    def __init__(self):
        self.cars = {}
        self.board_size = 0
        self.board = [[]]
        self.all_moves = []


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
        
        for i in self.board:
            print(" ".join(i))
        
        
    def move(self):
        empty_spaces = []
        move_car = 0 
        move_coordinates = 0
        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if self.board[rows][colums] == "_":
                    empty_spaces.append([rows, colums])
        
        random.shuffle(empty_spaces)
        for space in range(len(empty_spaces)):
            empty_temp = empty_spaces.pop()

            if empty_temp[0] + 1 < self.board_size:              
                if self.board[empty_temp[0] + 1][empty_temp[1]] != "_":
                    temp_car = self.board[empty_temp[0] + 1][empty_temp[1]]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "V":
                        move_coordinates = -1
                        move_car = temp_car

            if empty_temp[1] + 1 < self.board_size:
                if self.board[empty_temp[0]][empty_temp[1] + 1] != "_":
                    temp_car = self.board[empty_temp[0]][empty_temp[1] + 1]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "H":
                        move_coordinates = -1
                        move_car = temp_car


            if empty_temp[0] - 1 > 0:  
                if self.board[empty_temp[0] - 1][empty_temp[1]] != "_":
                    temp_car = self.board[empty_temp[0] - 1][empty_temp[1]]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "V":
                        move_coordinates = 1
                        move_car = temp_car

            if empty_temp[1] - 1  > 0:
                if self.board[empty_temp[0]][empty_temp[1] - 1] != "_":
                    temp_car = self.board[empty_temp[0]][empty_temp[1] - 1]
                    orientation = (self.cars[temp_car].orientation)
                    if orientation == "H":
                        move_coordinates = 1
                        move_car = temp_car
            
            if move_car != 0: 
                break

        car_orientation = self.cars[move_car].orientation

        if car_orientation == "V":
            self.cars[move_car].row = self.cars[move_car].row + move_coordinates
        else:
            self.cars[move_car].col = self.cars[move_car].col + move_coordinates

        self.all_moves.append([move_car, move_coordinates])




        
           
        
           