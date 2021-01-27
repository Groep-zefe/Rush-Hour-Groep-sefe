class Cars:
    def __init__(self, car_id, car_orie, car_row, car_col, car_len):
        self.id = car_id
        self.orientation = car_orie
        self.row = int(car_row) - 1
        self.col = int(car_col) - 1
        self.length = car_len
    
    # Sets the first coordinates of the car
    def coordinates(self): 
        self.coordinates_one = [self.row, self.col]

        # Checks the orientation of the car for the second coordinates
        if self.orientation == "H":
            self.coordinates_two = [self.row, self.col + 1]
        else: 
            self.coordinates_two = [self.row + 1, self.col]
        
        if self.length == "3":
            if self.orientation == "H": 
                self.coordinates_three = [self.row, self.col + 2]
            else: 
                self.coordinates_three = [self.row + 2 , self.col]
            
            return [self.id, self.coordinates_one, self.coordinates_two, self.coordinates_three]

        return [self.id, self.coordinates_one, self.coordinates_two]
