import csv


class Cars:
    def __init__(self, car_id, car_orie, car_row, car_col, car_len):
        self.id = car_id
        self.orientation = car_orie
        self.row = int(car_row) - 1
        self.col = int(car_col) - 1
        self.length = car_len
    
    def coordinates(self): 

        self.coordinates_one = [self.row, self.col]

        if self.orientation == "H":
            self.coordinates_two = [self.row, self.col + 1]
        else: 
            self.coordinates_two = [self.row + 1, self.col]
        
        if self.length == "3":
            if self.orientation == "H": 
                self.coordinates_three = [self.row, self.col + 2]
            else: 
                self.coordinates_three = [self.row + 1 , self.col]
            
            return [self.id, self.coordinates_one, self.coordinates_two, self.coordinates_three]

        return [self.id, self.coordinates_one, self.coordinates_two]


class Board:
    def __init__(self):
        self.cars = {}
        self.board_size = 0 

    def load_cars(self):
        with open ("boards/Rushhour6x6_1.csv", "r") as csvfile:
            datafile = csv.reader(csvfile)

            for row in datafile: 
                if row[0] != "car":
                    self.cars[row[0]] = Cars(row[0], row[1], row[2], row[3], row[4])
                    if int(row[2]) > self.board_size:
                        self.board_size = int(row[2])
        return self.cars


    def load_board(self):
        # Bron: https://www.youtube.com/watch?v=JnujQxAqAIM&ab_channel=C0nti
        board = [["|   |" for rows in range(self.board_size)] for colums in range(self.board_size)]

        for rows in range(self.board_size):
            for colums in range(self.board_size):
                board[rows][colums] = 0
        
        cars = self.cars
        car_keys = cars.keys()

        #for key in car_keys:
        key = "A"
        list_coordinates = (cars[key].coordinates())
        car_id = list_coordinates[0]
        board[list_coordinates[1][0]][list_coordinates[1][1]] = car_id
        board[list_coordinates[2][0]][list_coordinates[2][1]] = car_id

        if len(list_coordinates) == 4: 
            board[list_coordinates[3][0]][list_coordinates[3][1]] = car_id

       
        for rows in range(self.board_size):
            for colums in range(self.board_size):
                if board[rows][colums] == 0:
                    board[rows][colums] = "|   |"
                else: 
                    board[rows][colums] = f'| {board[rows][colums]} |'

        for i in board:
            print("----- " * self.board_size)
            print(" ".join(i))
            print("----- " * self.board_size)
        
           
if __name__ == "__main__":
    board = Board()
    board.load_cars()
    board.load_board()

