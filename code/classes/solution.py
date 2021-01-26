import csv
import time


from pathlib import Path


from code.classes.board import Board
from code.algorithms.breadth_first import Breadth


# Class that generates a solution with the right output
class Solution:
    def __init__(self, game, results):
        self.game = game
        self.results = results
        self.fastest_game = 100000

    # Finds the fastest solution that has been found 
    def find_fastest(self):
        i = 0 
        while True:  
            my_file = Path(f'solutions/solution_game_{self.game}.{i}.csv')
            if my_file.is_file():
                with open(f'solutions/solution_game_{self.game}.{i}.csv', 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    row1 = next(reader)
                    self.fastest_game = int(row1[2])
                i += 1
            else: 
                break

    # Saves the solution in a new file 
    def save_solution(self): 
        # Only a solution less than the fastest will be saved 
        if len(self.results) < self.fastest_game:
            self.fastest_game = len(self.results)
            print(f"I am speed! {self.fastest_game}")
            time.sleep(2)
            i = 0 
            while True:  
                my_file = Path(f'solutions/solution_game_{self.game}.{i}.csv')
                if my_file.is_file():
                    i += 1
                else: break

            # Writes the solution in a csv file in the right format
            with open(f'solutions/solution_game_{self.game}.{i}.csv', 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['car', 'move', len(self.results)]) 
                writer.writerows(self.results)
    
    # Checks if the current solution is not longer than the fastest        
    def result_check(self):
        if len(self.results) >= self.fastest_game:
            return True
    

        
                
