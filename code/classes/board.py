import csv

from code.classes.cars import Cars


class Board:
    def __init__(self):
        """ Loads the cars and creates a board with the cars on the right places."""
        
        self.cars = {}
        self.board_size = 0
        self.board = [[]]


    def load_cars(self, filename):
        """ Opens the right csv file and loads all the car information in a dictionary."""

        with open (filename, "r") as csvfile:
            datafile = csv.reader(csvfile)

            # Sets the cars and size of the board correctly 
            for row in datafile: 
                if row[0] != "car":
                    self.cars[row[0]] = Cars(row[0], row[1], row[3], row[2], row[4])
                    if int(row[2]) > self.board_size:
                        self.board_size = int(row[2])

        return self.cars

    
    def load_board(self):
        """ Creates a list that represents the board of the game."""

        self.board = [["_" for rows in range(self.board_size)] for colums in range(self.board_size)]
  
        car_keys = self.cars.keys()

        # Loop over all cars and fill in their coordinates
        for key in car_keys:
            list_coordinates = (self.cars[key].coordinates())
           
            car_id = list_coordinates[0]
            self.board[list_coordinates[1][0]][list_coordinates[1][1]] = car_id
            self.board[list_coordinates[2][0]][list_coordinates[2][1]] = car_id

            # Sets the board coordinates for the car ID
            if len(list_coordinates) == 4: 
                self.board[list_coordinates[3][0]][list_coordinates[3][1]] = car_id
 
        return(self.board)


    def visualize_board(self):    
        """ Makes a nice visualisation of the board."""  
        
        for i in self.board:
            print(" ".join(i))
        
    
