import csv


from code.classes.cars import Cars

class Board:
    def __init__(self):
        self.cars = {}
        self.board_size = 0
        self.board = [[]]

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
        
        return(self.board)


  # prints each board and made move to terminal. Not necessary for good result
    def visualize_board(self):      
        for i in self.board:
            print(" ".join(i))
        
    