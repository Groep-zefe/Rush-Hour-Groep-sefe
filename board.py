import csv


class Cars:
    def __init__(self, car_id, car_orie, car_row, car_col, car_len):
        self.id = car_id
        self.orientation = car_orie
        self.row = car_row
        self.col = car_col
        self.length = car_len

class Board:
    def __init__(self):
        self.cars = {}
    
    def load_cars(self):
        with open ("boards/Rushhour6x6_1.csv", "r") as csvfile:
            datafile = csv.reader(csvfile)

            for row in datafile: 
                if row[0] != "car":
                    self.cars[row[0]] = Cars(row[0], row[1], row[2], row[3], row[4])

            print(self.cars)

if __name__ == "__main__":
    board = Board()
    board.load_cars()
