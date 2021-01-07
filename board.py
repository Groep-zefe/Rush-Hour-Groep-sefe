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
                if board[rows][colums] == 0:
                    board[rows][colums] = "|   |"
                else:
                    car = "A"
                    board[rows][colums] = f"| {car} |"

        for i in board:
            print("----- " * self.board_size)
            print(" ".join(i))
            print("----- " * self.board_size)
        
        

            

    
if __name__ == "__main__":
    board = Board()
    cars = board.load_cars()
    car_keys = cars.keys()

    board.load_board()

    # for key in car_keys:
    #     print(cars[key].row)

