import csv


class Cars:
    def __init__(self, car_id, car_orie, car_row, car_col, car_len):
        self.id = car_id
        self.orientation = car_orie
        self.row = car_row
        self.col = car_col
        self.length = car_len
    
    def coordinates(self):


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
        for car in self.cars:
            thiscar = car 
            car_coordinates = car.coordinates

        for rows in range(self.board_size):
            print((self.board_size) * "#")
            

    
if __name__ == "__main__":
    board = Board()
    cars = board.load_cars()
    car_keys = cars.keys()

    board.load_board()

    # for key in car_keys:
    #     print(cars[key].row)

